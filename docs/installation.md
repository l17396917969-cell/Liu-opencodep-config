# 🤖 AI 安装指南

让 AI 帮你完成所有安装和配置。

## 一键安装提示词

复制以下内容，粘贴到你的 AI IDE (Claude Code、Cursor、AmpCode 等)：

```
请帮我安装和配置 oh-my-opencode。

项目地址: https://github.com/l17396917969-cell/Liu-opencodep-config

请按以下步骤执行：

1. **下载项目**
   - Windows: 从 https://github.com/l17396917969-cell/Liu-opencodep-config/releases/download/v1.0.0/oh-my-opencode-1.0.0.zip 下载
   - 解压到合适的位置（如 C:\Tools\oh-my-opencode）

2. **检查依赖**
   - 检查是否已安装 Python 3.9+
   - 检查是否已安装 Git
   - 检查是否已安装 Node.js（可选）
   - 如缺少，请帮我安装

3. **运行安装脚本**
   - 进入项目目录
   - 执行: python install\install.py (Windows) 或 python3 install/install.py (Mac/Linux)
   - 跟随交互式向导完成配置

4. **配置模型**
   - 在向导中选择需要的 AI 模型提供商
   - 输入 API Keys
   - 选择安装 preset（推荐 standard）

5. **验证安装**
   - 运行: python install\install.py doctor
   - 确认所有检查通过

请自动处理所有步骤，只在需要我输入 API Key 或做选择时询问我。
```

---

## 或者，更简单的版本

如果你已经在项目目录中：

```
我在这个目录中: [粘贴你的项目路径]

请帮我运行安装脚本 python install\install.py，并跟随向导完成配置。
当我需要输入 API Key 或做选择时，请提示我。
```

---

## 安装后验证

安装完成后，验证是否成功：

```
请帮我验证 oh-my-opencode 是否安装成功：
1. 检查配置文件是否存在
2. 检查 skills 是否正确安装
3. 运行诊断命令确认一切正常
```

## Troubleshooting

如果 AI 安装过程中遇到问题，可以问：

```
安装失败了，错误信息是: [粘贴错误]

请帮我诊断问题并修复。
```

或者查看 [手动安装指南](README.md)。
