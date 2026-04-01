# OpenCode 一键安装指南

在 OpenCode 中直接对话完成安装，无需手动操作。

## 方法：直接对话安装

复制以下内容，直接在 OpenCode 聊天框中发送：

```
帮我安装 oh-my-opencode。

项目地址：https://github.com/l17396917969-cell/Liu-opencodep-config

请帮我：
1. 下载项目到 ~/oh-my-opencode（Windows 下载到 C:\Tools\oh-my-opencode）
2. 检查 Python 3.9+、Git 是否已安装，如未安装请帮我安装
3. 运行安装脚本：python install/install.py
4. 在交互式向导中，帮我选择以下配置（询问我确认）：
   - 推荐模型提供商（Codex、MiniMax、Kimi 等）
   - 输入 API Key（问我）
   - 安装 preset（推荐 standard）
5. 安装完成后验证：python install/install.py doctor

请逐步执行，每完成一步告诉我结果，需要我输入信息时暂停并询问我。
```

## 更简洁的版本

```
请为我安装 oh-my-opencode（https://github.com/l17396917969-cell/Liu-opencodep-config）：
1. 下载并解压到合适位置
2. 运行 install/install.py 安装
3. 配置模型时询问我 API Key
4. 验证安装

开始吧。
```

## 安装后使用

安装完成后，你可以随时让我帮你：

- **更新 skills**："帮我更新 oh-my-opencode 的 skills"
- **检查配置**："检查我的 opencode 配置"
- **安装新 skill**："帮我安装 agent-browser skill"

## Troubleshooting

如果安装失败，告诉我错误信息，我会帮你解决。
