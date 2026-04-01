#!/usr/bin/env python3
"""
OpenCode 自动化安装引导脚本
使用方法：在 OpenCode 中运行: python -c "$(curl -fsSL https://raw.githubusercontent.com/l17396917969-cell/Liu-opencodep-config/main/install/opencode_bootstrap.py)"
"""

import os
import sys
import platform
from pathlib import Path


def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🤖 OpenCode 自动化安装引导                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")


def detect_os():
    """检测操作系统"""
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Darwin":
        return "macos"
    else:
        return "linux"


def get_install_dir(os_type):
    """获取安装目录"""
    home = Path.home()
    if os_type == "windows":
        return home / "oh-my-opencode"
    else:
        return home / "oh-my-opencode"


def check_dependencies():
    """检查依赖"""
    print("🔍 检查依赖...")

    deps = {
        "python": False,
        "git": False,
        "node": False,
    }

    # Check Python
    try:
        import subprocess

        result = subprocess.run(["python", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            deps["python"] = True
            print(f"  ✅ Python: {result.stdout.strip()}")
        else:
            # Try python3
            result = subprocess.run(
                ["python3", "--version"], capture_output=True, text=True
            )
            if result.returncode == 0:
                deps["python"] = True
                print(f"  ✅ Python: {result.stdout.strip()}")
    except:
        pass

    if not deps["python"]:
        print("  ❌ Python: 未安装 (需要 3.9+)")

    # Check Git
    try:
        import subprocess

        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            deps["git"] = True
            print(f"  ✅ Git: {result.stdout.strip()}")
        else:
            print("  ❌ Git: 未安装")
    except:
        print("  ❌ Git: 未安装")

    # Check Node (optional)
    try:
        import subprocess

        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            deps["node"] = True
            print(f"  ✅ Node.js: {result.stdout.strip()}")
    except:
        print("  ⚠️  Node.js: 未安装 (可选，用于 agent-browser)")

    return deps


def download_project(install_dir):
    """下载项目"""
    print(f"\n📥 下载项目到 {install_dir}...")

    import subprocess
    import shutil

    # Remove existing directory if exists
    if install_dir.exists():
        print(f"  发现已存在的目录，备份到 {install_dir}.backup")
        backup_dir = Path(str(install_dir) + ".backup")
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.move(install_dir, backup_dir)

    # Clone repository
    repo_url = "https://github.com/l17396917969-cell/Liu-opencodep-config.git"
    result = subprocess.run(
        ["git", "clone", repo_url, str(install_dir)], capture_output=True, text=True
    )

    if result.returncode == 0:
        print("  ✅ 下载完成")
        return True
    else:
        print(f"  ❌ 下载失败: {result.stderr}")
        return False


def run_installer(install_dir):
    """运行安装脚本"""
    print("\n🚀 运行安装脚本...")
    print("=" * 60)
    print()

    import subprocess

    os.chdir(install_dir)

    # Determine python command
    python_cmd = "python3"
    try:
        result = subprocess.run(["python", "--version"], capture_output=True)
        if result.returncode == 0:
            python_cmd = "python"
    except:
        pass

    # Run installer interactively
    install_script = install_dir / "install" / "install.py"

    print(f"正在执行: {python_cmd} {install_script}")
    print("请跟随交互式向导完成配置...")
    print("-" * 60)
    print()

    result = subprocess.run([python_cmd, str(install_script)])

    return result.returncode == 0


def main():
    print_banner()

    os_type = detect_os()
    print(f"检测到操作系统: {os_type.upper()}")

    install_dir = get_install_dir(os_type)

    # Check dependencies
    deps = check_dependencies()

    if not deps["python"]:
        print("\n❌ 错误: Python 未安装")
        print("请先安装 Python 3.9+:")
        print("  Windows: https://python.org/downloads")
        print("  macOS: brew install python@3.11")
        print("  Linux: sudo apt-get install python3")
        return 1

    if not deps["git"]:
        print("\n❌ 错误: Git 未安装")
        print("请先安装 Git:")
        print("  Windows: https://git-scm.com/download/win")
        print("  macOS: brew install git")
        print("  Linux: sudo apt-get install git")
        return 1

    # Confirm installation
    print(f"\n📦 准备安装到: {install_dir}")
    response = input("开始安装? [Y/n]: ").strip().lower()
    if response and response not in ["y", "yes"]:
        print("取消安装")
        return 0

    # Download
    if not download_project(install_dir):
        return 1

    # Run installer
    if run_installer(install_dir):
        print("\n" + "=" * 60)
        print("🎉 安装完成!")
        print("=" * 60)
        print("\n提示:")
        print("  - 配置文件位于: ~/.config/opencode/")
        print("  - 重新打开 OpenCode 即可使用新配置")
        print("  - 运行 'opencode doctor' 验证安装")
        return 0
    else:
        print("\n❌ 安装失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
