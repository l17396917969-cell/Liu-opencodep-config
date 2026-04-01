# 🚀 Oh My OpenCode

一键配置 OpenCode 完整开发环境的自动化工具包。

[![Release](https://img.shields.io/github/v/release/l17396917969-cell/Liu-opencodep-config)](https://github.com/l17396917969-cell/Liu-opencodep-config/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **注意**：Windows 用户请使用 **CMD** 或 **PowerShell** 运行安装命令，不要使用 Git Bash。

---

## 🤖 30 秒快速安装（让 AI 帮你装）

**别自己动手了，让 AI 来！**

复制以下内容，粘贴到你的 AI IDE (Claude Code、Cursor、AmpCode、Windsurf 等)：

```
请帮我安装 oh-my-opencode：
1. 从 https://github.com/l17396917969-cell/Liu-opencodep-config 下载项目
2. 运行安装脚本并完成配置
3. 需要输入 API Key 时提示我

项目说明：一键配置 OpenCode 的自动化工具，包含 20+ Skills 和交互式模型配置向导。
```

**完事。** AI 会帮你处理所有步骤。

<details>
<summary>🤔 没 AI IDE？点击查看手动安装指南</summary>

---

## ✨ 特性

- 🎯 **交互式模型配置向导** - 支持一键导入 Codex、MiniMax、Kimi、DeepSeek 等主流模型
- 📦 **预置 Skill 套装** - 包含 20+ 精心设计的 AI Skills
- 🔧 **自动化安装** - 一条命令完成所有配置
- 🔄 **增量更新** - 轻松保持 Skills 最新
- 🖥️ **跨平台** - 支持 macOS、Linux、Windows
- 🛡️ **依赖检查** - 自动检测并提示缺失的依赖

## 📦 预置 Skills

### 核心 Skills

| Skill | 描述 | 类型 |
|-------|------|------|
| `frontend-design` | 生成高质量前端界面 | 设计 |
| `lingjing-ux-core` | 灵境航空工业智能平台 UX 规范 | UX设计 |
| `agent-browser` | 浏览器自动化 | 自动化 |
| `skill-creator` | Skill 开发指南 | 开发 |
| `vibe-stack-guardian` | Vibe Coding 技术栈合规检查 | 开发 |
| `find-skills` | 发现和管理 skills | 工具 |

### Superpowers 集合 (16个)

- `brainstorming` - 创意头脑风暴
- `writing-plans` - 编写实施计划
- `executing-plans` - 执行计划
- `systematic-debugging` - 系统化调试
- `test-driven-development` - 测试驱动开发
- `using-git-worktrees` - Git worktree 管理
- `subagent-driven-development` - 子智能体开发
- `dispatching-parallel-agents` - 并行智能体调度
- `requesting-code-review` - 请求代码审查
- `receiving-code-review` - 处理代码审查反馈
- `verification-before-completion` - 完成前验证
- `finishing-a-development-branch` - 完成开发分支
- `writing-skills` - 编写 skills
- `using-superpowers` - 使用 superpowers

## 🚀 快速开始

## 🚀 快速开始

### 前置条件

确保已安装：
- **Python 3.9+** ([下载](https://python.org/downloads))
- **Git** ([下载](https://git-scm.com/download/win))
- **Node.js** (可选，用于 agent-browser)

### Windows 安装（CMD 或 PowerShell）

**推荐使用 CMD：**

```cmd
# 1. 下载并解压
cd %USERPROFILE%\Downloads
curl -L -o Liu-opencodep-config.zip https://github.com/l17396917969-cell/Liu-opencodep-config/releases/download/v1.0.0/oh-my-opencode-1.0.0.zip
tar -xf Liu-opencodep-config.zip

# 2. 进入目录
cd oh-my-opencode

# 3. 运行安装
python install\install.py
```

**或使用 PowerShell：**

```powershell
# 1. 下载并解压
Invoke-WebRequest -Uri "https://github.com/l17396917969-cell/Liu-opencodep-config/releases/download/v1.0.0/oh-my-opencode-1.0.0.zip" -OutFile "Liu-opencodep-config.zip"
Expand-Archive -Path "Liu-opencodep-config.zip" -DestinationPath "." -Force

# 2. 进入目录
cd oh-my-opencode

# 3. 运行安装
python install\install.py
```

### macOS/Linux 安装

```bash
# 下载并解压
curl -L https://github.com/l17396917969-cell/Liu-opencodep-config/releases/download/v1.0.0/oh-my-opencode-1.0.0.tar.gz | tar -xz
cd oh-my-opencode

# 运行安装
python3 install/install.py
```

安装向导会引导你：
1. 🔍 检查系统依赖
2. 🤖 配置 AI 模型（支持一键导入推荐配置）
3. 📦 选择并安装 Skills

## 📖 使用指南

### 安装命令

**Windows (CMD/PowerShell)：**

```cmd
# 交互式安装
python install\install.py

# 使用预设安装
python install\install.py --preset standard

# 指定 skills 安装
python install\install.py --skills frontend-design,find-skills

# 强制覆盖现有配置
python install\install.py --force

# 仅安装配置，跳过 skills
python install\install.py --skip-skills
```

**macOS/Linux：**

```bash
# 交互式安装
python3 install/install.py

# 使用预设安装
python3 install/install.py --preset standard

# 指定 skills 安装
python3 install/install.py --skills frontend-design,find-skills

# 强制覆盖现有配置
python3 install/install.py --force

# 仅安装配置，跳过 skills
python3 install/install.py --skip-skills
```

### 可用 Presets

| Preset | 描述 | 包含内容 |
|--------|------|----------|
| `minimal` | 最小安装 | 仅核心配置 |
| `standard` | 标准安装 | 常用 skills |
| `full` | 完整安装 | 所有 skills |
| `aviation` | 航空工业专用 | 针对灵境平台优化 |

### 其他命令

```bash
# 检查配置和依赖
python install/install.py doctor

# 列出所有可用 skills
python install/install.py list

# 更新所有已安装 skills
python install/install.py update

# 卸载特定 skill
python install/install.py uninstall skill-name
```

## 🤖 支持的模型提供商

### 一键导入（推荐配置）

- ✅ **Codex GPT-5** - 自定义 Codex 服务
- ✅ **MiniMax** - 中文/国际版
- ✅ **Kimi (Moonshot)** - 月之暗面
- ✅ **DeepSeek** - 深度求索
- ✅ **SiliconFlow** - 硅基流动

### 标准提供商

- ✅ **Anthropic** (Claude)
- ✅ **OpenAI** (GPT-4)
- ✅ **Google** (Gemini)
- ✅ **Mistral AI**
- ✅ **Cohere**
- ✅ **xAI** (Grok)
- ✅ **阿里云** (通义千问)

### 自定义 API

支持任何 **OpenAI API 兼容**的服务，只需提供：
- Base URL
- API Key
- 模型 ID

## 📁 项目结构

```
oh-my-opencode/
├── install/
│   ├── install.py                 # 主安装脚本
│   └── lib/
│       ├── dependency_checker.py  # 依赖检查
│       ├── skills_installer.py    # Skills 安装
│       ├── config_renderer.py     # 配置渲染
│       └── model_configurator.py  # 模型配置向导
├── templates/
│   ├── opencode.json.template     # 配置模板
│   ├── oh-my-openagent.json       # Agent 定义
│   └── AGENTS.md                  # 系统提示词
├── manifests/
│   ├── skills-registry.json       # Skills 注册表
│   └── external-dependencies.json # 外部依赖清单
├── skills/                        # Skills 目录
│   ├── frontend-design/
│   ├── lingjing-ux-core/
│   ├── agent-browser/
│   ├── skill-creator/
│   ├── vibe-stack-guardian/
│   ├── find-skills/
│   └── superpowers/               # 16个开发技能
└── README.md
```

## 🛠️ 开发指南

### 添加新 Skill

1. 在 `skills/` 目录下创建 skill 目录
2. 编写 `SKILL.md` 文件
3. 在 `manifests/skills-registry.json` 中注册

```json
{
  "skills": {
    "my-skill": {
      "name": "my-skill",
      "description": "My skill description",
      "type": "markdown-only",
      "source": "skills/my-skill/",
      "destination": "{config_dir}/skills/my-skill/",
      "category": "development"
    }
  }
}
```

### 添加新模型提供商

在 `install/lib/model_configurator.py` 中添加：

```python
RECOMMENDED_CONFIGURATIONS["my-api"] = {
    "name": "My API",
    "provider": "my-api",
    "base_config": {
        "npm": "@ai-sdk/openai-compatible",
        "options": {
            "baseURL": "https://api.my-service.com/v1",
        },
        "models": {
            "model-1": {"id": "model-1"},
        },
    },
    "default_model": "my-api/model-1",
    "description": "My custom API",
}
```

## 🔧 故障排除

### Windows 常见问题

#### 1. "python" 不是内部或外部命令？

**原因**：Python 未添加到系统 PATH。

**解决方案**：
```cmd
# 方法 1：重新安装 Python，勾选 "Add Python to PATH"
# 方法 2：使用 Python Launcher
py install\install.py
```

#### 2. PowerShell 执行策略错误

**错误信息**：`无法加载文件，因为在此系统上禁止运行脚本`

**解决方案**：
```powershell
# 以管理员身份运行 PowerShell，执行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3. 找不到配置文件目录

**Windows 配置文件位置**：
```
C:\Users\<你的用户名>\AppData\Roaming\opencode\
```

快速打开：
```cmd
explorer %APPDATA%\opencode
```

#### 4. uvx 路径检测失败

**解决方案**：
```cmd
# 找到 uvx 位置
where uvx

# 或手动指定完整路径
C:\Users\<用户名>\AppData\Local\Programs\Python\Python311\Scripts\uvx.exe
```

### 通用问题

#### 依赖检查失败

**Windows：**
```cmd
python install\install.py doctor
```

**macOS/Linux：**
```bash
python3 install/install.py doctor
```

#### 模型连接失败

1. 检查 API Key 是否正确
2. 确认 Base URL 是否可访问
3. 检查网络连接（某些 API 需要代理）
4. 尝试在浏览器中访问 API 文档确认服务状态

## 📝 配置示例

安装完成后，你的配置文件位置：

**Windows：**
```
C:\Users\<用户名>\AppData\Roaming\opencode\opencode.json
```

**macOS/Linux：**
```
~/.config/opencode/opencode.json
```

配置示例：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["oh-my-openagent@latest"],
  "provider": {
    "my-codex": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "https://codex-ai.988669.xyz/v1",
        "apiKey": "sk-xxx"
      },
      "models": {
        "gpt54": { "id": "gpt-5.4" },
        "gpt53": { "id": "gpt-5.3-codex" }
      }
    },
    "minimax-cn": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "https://api.minimaxi.chat/v1",
        "apiKey": "sk-xxx"
      },
      "models": {
        "MiniMax-M2.7-highspeed": { "id": "MiniMax-M2.7-highspeed" }
      }
    }
  },
  "model": "my-codex/gpt54"
}
```

## 🤝 贡献

欢迎提交 Issue 和 PR！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

[MIT](LICENSE)

## 🙏 致谢

- [OpenCode](https://opencode.ai/) - AI 原生 IDE
- [Oh My OpenAgent](https://github.com/code-yeongyu/oh-my-openagent) - Agent 框架

</details>
