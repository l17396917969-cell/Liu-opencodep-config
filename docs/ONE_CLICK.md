# OpenCode 一键命令

## 最简安装（推荐）

在 OpenCode 聊天框中发送：

```bash
curl -fsSL https://raw.githubusercontent.com/l17396917969-cell/Liu-opencodep-config/main/install/remote_install.sh | bash
```

或让 OpenCode 帮你执行：

```
请执行这个命令帮我安装 oh-my-opencode：
curl -fsSL https://raw.githubusercontent.com/l17396917969-cell/Liu-opencodep-config/main/install/remote_install.sh | bash
```

## 分步安装（更可控）

如果你想看到每一步的过程：

```
请帮我完成以下步骤安装 oh-my-opencode：

步骤 1: 下载项目
- 使用 git clone https://github.com/l17396917969-cell/Liu-opencodep-config.git ~/oh-my-opencode

步骤 2: 运行安装向导
- cd ~/oh-my-opencode
- 运行 python3 install/install.py
- 在交互式向导中帮我选择配置

步骤 3: 验证
- 运行 python3 install/install.py doctor 检查安装

请每完成一步告诉我结果，需要我输入 API Key 时暂停询问。
```

## 对于 Windows 用户

在 OpenCode 中（CMD/PowerShell 模式）：

```
请帮我在 Windows 上安装 oh-my-opencode：
1. 下载 https://github.com/l17396917969-cell/Liu-opencodep-config/releases/download/v1.0.0/oh-my-opencode-1.0.0.zip
2. 解压到 C:\Tools\oh-my-opencode
3. 运行 python install\install.py
4. 引导我完成配置
```

## 安装完成后

告诉 OpenCode：

```
oh-my-opencode 安装好了，帮我检查配置
```

OpenCode 会运行诊断命令并报告状态。

## Troubleshooting

如果自动安装失败，可以分步排查：

```
oh-my-opencode 安装失败，帮我排查：
1. 检查 Python 是否已安装（python --version）
2. 检查 Git 是否已安装（git --version）
3. 查看具体错误信息
4. 修复问题后重新安装
```
