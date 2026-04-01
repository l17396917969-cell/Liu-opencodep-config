#!/bin/bash
#
# Oh My OpenCode - 远程一键安装脚本
# 使用方法: curl -fsSL https://raw.githubusercontent.com/l17396917969-cell/Liu-opencodep-config/main/install/remote_install.sh | bash
#

set -e

REPO_URL="https://github.com/l17396917969-cell/Liu-opencodep-config.git"
INSTALL_DIR="$HOME/oh-my-opencode"

print_banner() {
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                                                              ║"
    echo "║     🚀 Oh My OpenCode - 自动化安装                          ║"
    echo "║                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
}

check_dependencies() {
    echo "🔍 检查依赖..."
    
    if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
        echo "❌ 错误: Python 未安装"
        echo "请先安装 Python 3.9+: https://python.org/downloads"
        exit 1
    fi
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    else
        PYTHON_CMD="python"
    fi
    
    echo "  ✅ Python: $($PYTHON_CMD --version 2>&1)"
    
    if ! command -v git &> /dev/null; then
        echo "❌ 错误: Git 未安装"
        echo "请先安装 Git: https://git-scm.com/downloads"
        exit 1
    fi
    
    echo "  ✅ Git: $(git --version)"
    echo ""
}

download_project() {
    echo "📥 下载项目..."
    
    if [ -d "$INSTALL_DIR" ]; then
        echo "  发现已存在的安装，备份到 $INSTALL_DIR.backup"
        rm -rf "$INSTALL_DIR.backup" 2>/dev/null || true
        mv "$INSTALL_DIR" "$INSTALL_DIR.backup"
    fi
    
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
    echo "  ✅ 下载完成"
    echo ""
}

run_installer() {
    echo "🚀 启动安装向导..."
    echo "========================================"
    echo ""
    
    cd "$INSTALL_DIR"
    $PYTHON_CMD install/install.py
}

main() {
    print_banner
    check_dependencies
    download_project
    run_installer
    
    echo ""
    echo "========================================"
    echo "🎉 安装完成！"
    echo "========================================"
    echo ""
    echo "提示:"
    echo "  - 安装目录: $INSTALL_DIR"
    echo "  - 配置文件: ~/.config/opencode/"
    echo "  - 重新加载 OpenCode 即可使用"
    echo ""
}

main "$@"
