# OpenCode 对话式安装指南

## 对用户说

在 OpenCode 中直接发送：

```
帮我安装 oh-my-opencode
```

OpenCode 会自动完成后续所有步骤。

## 对 OpenCode AI 的指令

当用户说"帮我安装 oh-my-opencode"或类似的话时，请按以下流程执行：

### 步骤 1: 欢迎和说明

先回复用户：

```
🚀 我来帮你安装 oh-my-opencode！

这是一个自动化配置工具，包含：
- 20+ 预置 Skills
- 交互式模型配置向导
- 自动化依赖检查

我会自动完成下载和安装，你只需要在需要输入 API Key 时提供即可。

开始安装...
```

### 步骤 2: 下载项目

```python
# 使用 OpenCode 的 Bash 工具
import os
os.chdir(os.path.expanduser("~"))

# 克隆仓库
bash_command = "git clone https://github.com/l17396917969-cell/Liu-opencodep-config.git oh-my-opencode"
```

如果 git clone 失败，尝试下载 ZIP：
- Windows: 使用 curl 或 Invoke-WebRequest
- Mac/Linux: 使用 curl 和 tar

### 步骤 3: 检查依赖

检查以下依赖：
1. **Python 3.9+** - 必须
2. **Git** - 必须
3. **Node.js** - 可选（用于 agent-browser skill）

如果缺少依赖，告诉用户并询问是否要自动安装。

### 步骤 4: 运行安装脚本

进入项目目录：
```
cd ~/oh-my-opencode
```

运行安装：
```
python3 install/install.py  # Mac/Linux
python install\install.py   # Windows
```

### 步骤 5: 引导配置

安装脚本会启动交互式向导，请帮用户完成：

**选择模型提供商**（询问用户）：
```
📋 推荐配置：
1. Codex GPT-5 - 自定义 Codex 服务
2. MiniMax 中文 - MiniMax 中文 API
3. Kimi (Moonshot) - 月之暗面
4. DeepSeek - 深度求索
5. 跳过，稍后手动配置

你想配置哪个？（输入数字）
```

**输入 API Key**（提示用户）：
```
请提供 MiniMax API Key（输入时不会显示）：
```

**选择 Preset**（建议标准）：
```
📦 安装 preset：
- minimal: 最小安装
- standard: 标准安装（推荐）
- full: 完整安装
- aviation: 航空工业专用

选择：standard
```

### 步骤 6: 验证安装

运行：
```
python3 install/install.py doctor  # Mac/Linux
python install\install.py doctor    # Windows
```

检查：
- ✅ 所有依赖已安装
- ✅ 配置文件正确生成
- ✅ Skills 正确安装

### 步骤 7: 完成

告诉用户：

```
🎉 安装完成！

配置摘要：
- 配置文件：~/.config/opencode/opencode.json
- 已安装 Skills：[列出已安装的]
- 默认模型：[如果配置了]

下一步：
1. 重新加载 OpenCode（如果已打开）
2. 运行 `opencode doctor` 验证
3. 开始使用！

如需更新 skills，随时告诉我："帮我更新 oh-my-opencode"
```

## Troubleshooting

如果安装过程中出错：

### 下载失败
- 检查网络连接
- 尝试使用代理
- 或让用户手动下载 ZIP

### Python 未安装
告诉用户：
```
⚠️ 需要先安装 Python 3.9+

请访问 https://python.org/downloads 下载安装
安装时记得勾选 "Add Python to PATH"

安装完成后，重新说"帮我安装 oh-my-opencode"
```

### 权限错误（Mac/Linux）
可能需要 sudo：
```
sudo python3 install/install.py
```

## 安装后维护

用户可能会要求：

- **更新 skills**: "帮我更新 oh-my-opencode"
- **检查状态**: "检查我的 opencode 配置"  
- **添加 skill**: "帮我安装 [skill-name]"
- **卸载**: "帮我卸载 oh-my-opencode"

对应的命令：
```bash
# 更新
cd ~/oh-my-opencode && python3 install/install.py update

# 检查
cd ~/oh-my-opencode && python3 install/install.py doctor

# 安装特定 skill
cd ~/oh-my-opencode && python3 install/install.py --skills [skill-name]

# 卸载
cd ~/oh-my-opencode && python3 install/install.py uninstall [skill-name]
```
