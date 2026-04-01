#!/usr/bin/env python3

import sys
import json
import shutil
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "lib"))

from dependency_checker import DependencyChecker
from skills_installer import SkillsInstaller
from config_renderer import ConfigRenderer
from model_configurator import (
    ModelConfigurator,
    MODEL_PRESETS,
    RECOMMENDED_CONFIGURATIONS,
)


def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           🚀 Oh My OpenCode - 自动化配置工具 🚀              ║
║                                                              ║
║     一键配置 OpenCode 完整开发环境                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)


def _save_opencode_config(config: dict, output_path: str):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"✅ 配置已保存: {output_file}")


def _copy_static_configs(output_dir: str):
    templates_dir = Path(__file__).parent.parent / "templates"
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    static_files = ["oh-my-openagent.json", "AGENTS.md"]

    for filename in static_files:
        src = templates_dir / filename
        dst = output_path / filename

        if src.exists():
            shutil.copy2(src, dst)
            print(f"✅ 已复制: {filename}")


def cmd_doctor(args):
    print("🔍 运行诊断检查...\n")

    checker = DependencyChecker()
    results = checker.check_all()
    all_ok = checker.print_status(results)

    installer = SkillsInstaller()
    installed = installer.list_installed()

    print("📦 已安装的 Skills:")
    if installed:
        for item in installed:
            print(f"  ✅ {item}")
    else:
        print("  ⚠️  未安装任何 skills")

    config_file = installer.config_dir / "opencode.json"
    print(f"\n⚙️  配置文件状态:")
    if config_file.exists():
        print(f"  ✅ {config_file}")
    else:
        print(f"  ❌ {config_file} (不存在)")

    return 0 if all_ok else 1


def cmd_install(args):
    print_banner()

    checker = DependencyChecker()
    print("📋 第一步: 检查依赖")
    results = checker.check_all()
    checker.print_status(results)

    print("\n📋 第二步: 配置 AI 模型")
    configurator = ModelConfigurator()
    model_config = configurator.run_interactive_setup()

    config_path = Path.home() / ".config" / "opencode" / "opencode.json"

    if config_path.exists() and not args.force:
        print(f"\n⚠️  配置文件已存在: {config_path}")
        response = input("是否覆盖? [y/N]: ").strip().lower()
        if response != "y":
            print("⏭️  跳过配置文件生成")
        else:
            opencode_config = configurator.render_opencode_json(model_config)
            _save_opencode_config(opencode_config, str(config_path))
    else:
        opencode_config = configurator.render_opencode_json(model_config)
        _save_opencode_config(opencode_config, str(config_path))

    _copy_static_configs(str(config_path.parent))

    if not args.skip_skills:
        print("\n📋 第三步: 安装 Skills")
        installer = SkillsInstaller()

        if args.preset:
            print(f"🎯 使用预设: {args.preset}")
            success, messages = installer.install_preset(args.preset, force=args.force)
            for msg in messages:
                if "安装完成" in msg or "安装" in msg and "错误" not in msg:
                    print(f"  ✅ {msg}")
                else:
                    print(f"  ⚠️  {msg}")
        elif args.skills:
            skill_list = [s.strip() for s in args.skills.split(",")]
            for skill_name in skill_list:
                success, msg = installer.install_skill(skill_name, force=args.force)
                status = "✅" if success else "❌"
                print(f"  {status} {skill_name}: {msg}")
        else:
            print("可用预设:")
            presets = installer.get_presets()
            for name, info in presets.items():
                print(f"  • {name}: {info['description']}")

            preset = input("\n选择预设 (或输入 skill 名称): ").strip()
            if preset in presets:
                success, messages = installer.install_preset(preset, force=args.force)
                for msg in messages:
                    if "安装完成" in msg or ("安装" in msg and "错误" not in msg):
                        print(f"  ✅ {msg}")
                    else:
                        print(f"  ⚠️  {msg}")
            else:
                success, msg = installer.install_skill(preset, force=args.force)
                status = "✅" if success else "❌"
                print(f"  {status} {preset}: {msg}")

    print("\n" + "=" * 60)
    print("🎉 安装完成!")
    print("=" * 60)
    print("\n配置摘要:")
    print(f"  📁 配置文件: {config_path}")
    if model_config.get("providers"):
        print(f"  🤖 已配置提供商: {', '.join(model_config['providers'].keys())}")
    if model_config.get("default_model"):
        print(f"  ⭐ 默认模型: {model_config['default_model']}")
    print("\n下一步:")
    print("  1. 运行 'opencode doctor' 验证配置")
    print("  2. 运行 'opencode' 开始使用")
    print("  3. 如需修改模型，直接编辑配置文件或重新运行安装")
    print("\n")

    return 0


def cmd_update(args):
    print("🔄 更新 Skills...")

    installer = SkillsInstaller()
    installed = installer.list_installed()

    if not installed:
        print("⚠️  未安装任何 skills")
        return 1

    print(f"发现 {len(installed)} 个已安装 skills，开始更新...")

    for item in installed:
        if "(集合)" in item:
            coll_name = item.replace(" (集合)", "")
            success, msg = installer.install_collection(coll_name, force=True)
        else:
            success, msg = installer.install_skill(item, force=True)

        status = "✅" if success else "❌"
        print(f"  {status} {item}")

    print("\n✅ 更新完成")
    return 0


def cmd_list(args):
    installer = SkillsInstaller()

    print("\n📦 可用 Presets:")
    presets = installer.get_presets()
    for name, info in presets.items():
        print(f"  • {name}: {info['description']}")
        skills = info.get("skills", [])
        collections = info.get("collections", [])
        if skills:
            print(f"    Skills: {', '.join(skills)}")
        if collections:
            print(f"    集合: {', '.join(collections)}")

    print("\n📦 可用 Skills:")
    skills = installer.get_available_skills()
    for name, info in skills.items():
        skill_type = "集合" if info.get("is_collection") else "skill"
        print(f"  • {name} ({skill_type}): {info['description']}")

    print("\n📦 已安装:")
    installed = installer.list_installed()
    if installed:
        for item in installed:
            print(f"  ✅ {item}")
    else:
        print("  (无)")

    return 0


def cmd_uninstall(args):
    if not args.name:
        print("❌ 请指定要卸载的 skill 名称")
        return 1

    installer = SkillsInstaller()
    success, msg = installer.uninstall_skill(args.name)

    if success:
        print(f"✅ {msg}")
    else:
        print(f"❌ {msg}")

    return 0 if success else 1


def main():
    parser = argparse.ArgumentParser(
        description="Oh My OpenCode - OpenCode 自动化配置工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s install                    # 交互式安装
  %(prog)s install --preset standard  # 使用标准预设
  %(prog)s install --skills frontend-design,find-skills
  %(prog)s doctor                     # 检查配置
  %(prog)s list                       # 列出可用 skills
  %(prog)s update                     # 更新所有 skills
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    install_parser = subparsers.add_parser("install", help="安装配置和 skills")
    install_parser.add_argument(
        "--preset", help="使用预设配置 (minimal/standard/full/aviation)"
    )
    install_parser.add_argument("--skills", help="指定要安装的 skills，逗号分隔")
    install_parser.add_argument(
        "--force", "-f", action="store_true", help="强制覆盖现有配置"
    )
    install_parser.add_argument(
        "--skip-skills", action="store_true", help="跳过 skills 安装"
    )

    subparsers.add_parser("doctor", help="检查配置和依赖")
    subparsers.add_parser("update", help="更新所有 skills")
    subparsers.add_parser("list", help="列出可用 skills 和 presets")

    uninstall_parser = subparsers.add_parser("uninstall", help="卸载 skill")
    uninstall_parser.add_argument("name", help="要卸载的 skill 名称")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    commands = {
        "install": cmd_install,
        "doctor": cmd_doctor,
        "update": cmd_update,
        "list": cmd_list,
        "uninstall": cmd_uninstall,
    }

    if args.command in commands:
        return commands[args.command](args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
