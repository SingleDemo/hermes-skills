# Hermes Skills — 强制协议

> ⚠️ **每次对话开始时，以下步骤必须按顺序执行（不可跳过）：**
> 1. 调用 `skills_list()` 获取完整技能列表
> 2. 读取本文件 `~/.hermes/skills/SKILLS.md`
> 3. 判断是否有匹配技能，若有则立即 `skill_view(name)` 加载
> 4. 若涉及 Web 抓取，优先加载 `web-fetch-performance` 技能

---

## GitHub 同步规则（强制）

所有技能增/删操作必须同步到 GitHub 仓库 `SingleDemo/hermes-skills`。

### 同步协议

**添加技能时：**
1. 技能安装到 `~/.hermes/skills/<skill-name>/`
2. 运行 `~/.hermes/skills-sync.sh add <skill-name>`
3. 更新本文件 `SKILLS.md`，在对应分类下添加新技能条目
4. 再次运行 `~/.hermes/skills-sync.sh sync "Update SKILLS.md after adding <skill-name>"`

**删除技能时：**
1. 从 `~/.hermes/skills/<skill-name>/` 删除目录
2. 运行 `~/.hermes/skills-sync.sh remove <skill-name>`
3. 更新本文件 `SKILLS.md`，移除对应条目
4. 再次运行 `~/.hermes/skills-sync.sh sync "Update SKILLS.md after removing <skill-name>"`

**注意事项：**
- `symlink` 不被 Hermes 识别为 local 技能，技能必须物理存在于 `~/.hermes/skills/`
- skillhub 安装的技能需要物理复制到 `~/.hermes/skills/`，不是 symlink

---

## 已安装技能速查表

| 技能 | 一句话说明 | 何时触发 |
|------|-----------|----------|
| [agent-browser](skills/agent-browser/) | 无头浏览器自动化 CLI，导航/点击/输入/截图 | 需要操控网页、抓取页面内容时 |
| [minimax-mcp](skills/minimax-mcp/) | MiniMax MCP 安装配置，含 API_HOST/模型版本/歌词必填等坑点 | 配置 MCP 或用 MiniMax 音乐/语音/图片/视频生成时 |
| [summarize](skills/summarize/) | summarize CLI 总结 URL/文件（网页/PDF/图片/音频/YouTube） | 快速总结网页、文档、视频、音频内容时 |
| [web-fetch-performance](skills/web-fetch-performance/) | 网页抓取速度排行与降级策略（curl > mcp_fetch > jina > 浏览器） | 抓取任意网页时，先加载此技能按速度排行依次尝试 |
| [jina-web-fetcher](skills/jina-web-fetcher/) | Jina AI 抓取网页（curl 直接请求更快） | 备选网页抓取，已安装但实测 curl 更快 |
| [self-improving](skills/self-improving/) | 自我反思+自我批评+自组织记忆系统，触发：命令失败/用户纠正/知识过时/发现更好方法/用户提及 | 命令失败、用户纠正、知识过时、发现更好方法、用户提及时 |
| [github](skills/github/) | GitHub CLI (gh) 工作流 — PR/Issue/Repo/CodeReview | 操作 GitHub Repo、PR、Issue、代码审查时 |
| [hermes-gateway-debug](skills/hermes-gateway-debug/) | Hermes Gateway 连接状态排查 | Gateway 报 disconnected、微信/元宝无响应时 |
| [weixin-reconnect](skills/weixin-reconnect/) | 微信重连完整流程 | 微信 Session expired 或账号失联时 |
| [messenger-api-format-troubleshooting](skills/messenger-api-format-troubleshooting/) | 排查微信/元宝等 messenger 平台无法对话 | iLink 会话过期或 AI provider 无响应时 |
| [find-skills](skills/find-skills/) | SkillHub/ClawHub 技能搜索与安装 | 用户请求找/装技能时最高优先级触发 |
| [yuanbao](skills/yuanbao/) | 元宝群交互 — @成员、查询群信息 | 元宝群 @提及其他用户、查询群信息时 |
| [skillhub-hermes-sync](skills/skillhub-hermes-sync/) | SkillHub 技能目录与 Hermes 技能目录同步方法 | 同步/安装 SkillHub 技能时 |
| [miniprogram-architect](skills/miniprogram-architect/) | 小程序架构设计与分层 | 小程序项目架构设计、技术选型时 |
| [miniprogram-development](skills/miniprogram-development/) | 小程序开发全流程指南 | 小程序开发调试时 |
| [wechat-miniprogram-automator](skills/wechat-miniprogram-automator/) | 自动化微信小程序 DevTools | 小程序自动化测试、DevTools 驱动时 |
| [wechat-miniprogram-skill](skills/wechat-miniprogram-skill/) | 微信小程序入门到精通 | 小程序入门学习、开发时 |
| [wechat-miniprogram-toolkit](skills/wechat-miniprogram-toolkit/) | 小程序全栈开发（数据库/云函数/支付/TRTC） | 小程序全栈开发、微信支付、直播等复杂场景时 |
| [wechat-miniprogram-ui-ux](skills/wechat-miniprogram-ui-ux/) | 小程序 UI/UX 设计指南 | 小程序页面设计、交互优化时 |
| [tencentmap-miniprogram-skill](skills/tencentmap-miniprogram-skill/) | 腾讯位置服务小程序开发 | 小程序地图功能、LBS 服务时 |
| [cloudbase](skills/cloudbase/) | CloudBase 全栈开发套件（网站/小程序/云函数/数据库/托管） | CloudBase 全栈开发、部署、数据库、云函数时 |
| [cloudbase-mcp](skills/cloudbase-mcp/) | CloudBase MCP Server | MCP 配置、腾讯云开发工具集成时 |

---

## 系统内置技能速查表

| 技能 | 一句话说明 | 何时触发 |
|------|-----------|----------|
| cloudbase | 腾讯云开发全栈平台（后端/数据库/托管/云函数） | CloudBase 相关操作时 |
| cloudfunctions | 云函数开发/部署/调试 | 编写或调试云函数时 |
| miniprogram-development | 微信小程序开发全流程 | 小程序开发调试时 |
| mcp | MCP 服务器配置与工具集成 | 配置 MCP 工具时 |
| mlops | ML 训练/微调/部署/优化 | 机器学习相关任务时 |
| jupyter-live-kernel | 交互式 Jupyter notebook | 数据分析、可视化时 |
| autonomous-ai-agents | 多 Agent 工作流编排 | 需要并行/多 Agent 协作时 |
| systematic-debugging | 系统化调试方法论 | 遇到 Bug、测试失败时 |
| test-driven-development | TDD 测试先行开发 | 实现功能前先写测试时 |
| writing-plans | 写作计划和工作流 | 多步骤任务需规划时 |
| plan | 计划模式 | 需要审视上下文、写 markdown 计划时 |
| requesting-code-review | 代码审查前验证 | 提交代码审查前静态安全扫描时 |
| github-pr-workflow | PR 完整生命周期 | Create/PR/Review/Rebase/Merge PR 时 |
| github-issues | Issue 管理 | 创建/搜索/关闭 Issue 时 |
| github-code-review | GitHub 代码审查 | 分析 diff、留 inline 评论时 |
| claude-code | Claude Code CLI 委托编码 | 委托编码任务给 Claude Code 时 |
| codex | OpenAI Codex CLI 委托编码 | 委托编码任务给 Codex 时 |
| opencode | OpenCode CLI 委托编码 | 委托编码任务给 OpenCode 时 |
| dogfood | Web 应用探索式 QA 测试 | 测试 web 应用时 |

---

## 完整技能分类列表

### autonomous-ai-agents
- claude-code, codex, hermes-agent, opencode

### creative
- architecture-diagram, ascii-art, ascii-video, baoyu-infographic, excalidraw, ideation, manim-video, p5js, pixel-art, songwriting-and-ai-music

### data-science
- jupyter-live-kernel

### devops
- webhook-subscriptions

### dogfood
- dogfood

### email
- himalaya

### gaming
- minecraft-modpack-server, pokemon-player

### github
- codebase-inspection, github, github-auth, github-cli-auth, github-code-review, github-issues, github-pr-workflow, github-repo-management

### hermes-gateway-debug
- hermes-gateway-debug

### jina-web-fetcher
- jina-web-fetcher

### media
- gif-search, heartmula, songsee, youtube-content

### minimax
- android-native-dev, frontend-dev, fullstack-dev, gif-sticker-maker, ios-application-dev, minimax-docx, minimax-multimodal-toolkit, minimax-pdf, minimax-xlsx, pptx-generator, shader-dev

### wechat-miniprogram
- miniprogram-architect, miniprogram-development, wechat-miniprogram-automator, wechat-miniprogram-skill, wechat-miniprogram-toolkit, wechat-miniprogram-ui-ux, tencentmap-miniprogram-skill

### minimax-mcp
- minimax-mcp

### mlops
- evaluating-llms-harness, huggingface-hub, weights-and-biases

### mlops/inference
- llama-cpp, obliteratus, outlines, serving-llms-vllm

### mlops/models
- audiocraft-audio-generation, segment-anything-model

### mlops/research
- dspy

### mlops/training
- axolotl, fine-tuning-with-trl, unsloth

### mcp
- cloudbase-mcp, native-mcp

### cloudbase
- ai-model-nodejs, ai-model-web, ai-model-wechat, auth-nodejs-cloudbase, auth-tool-cloudbase, auth-web-cloudbase, auth-wechat-miniprogram, cloud-functions, cloud-storage-web, cloudbase-agent, cloudbase-document-database-in-wechat, cloudbase-document-database-web-sdk, cloudbase-platform, cloudrun-development, data-model-creation, http-api-cloudbase, relational-database-mcp-cloudbase, relational-database-web-cloudbase, spec-workflow, ui-design, web-development

### note-taking
- obsidian

### openclaw-imports
- find-skills, skillhub-preference

### productivity
- google-workspace, linear, maps, nano-pdf, notion, ocr-and-documents, powerpoint, web-fetch-performance

### red-teaming
- godmode

### research
- arxiv, blogwatcher, llm-wiki, polymarket

### skillhub-hermes-sync
- skillhub-hermes-sync

### smart-home
- openhue

### social-media
- xurl

### software-development
- messenger-api-format-troubleshooting, plan, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, writing-plans

### summarize
- summarize

### weixin-reconnect
- weixin-reconnect

### yuanbao
- yuanbao
