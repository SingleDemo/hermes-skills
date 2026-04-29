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
| [agent-browser](skills/agent-browser/) | Rust无头浏览器CLI，No dependencies | 需要操控网页、抓取动态内容、滚动翻页时 |
| [minimax-mcp](skills/minimax-mcp/) | MiniMax Token Plan完整指南，含API_HOST/模型版本/歌词必填坑点 | 配置MiniMax MCP或用MiniMax音乐/语音/图片生成时 |
| [summarize](skills/summarize/) | summarize CLI总结URL/文件，支持网页/PDF/音频/YouTube | 快速总结网页、文档、视频、音频时 |
| [web-fetch-performance](skills/web-fetch-performance/) | 网页抓取速度排行与降级策略 | 抓取任意网页时优先加载，按速度排行依次尝试 |
| [jina-web-fetcher](skills/jina-web-fetcher/) | Jina AI抓取网页，支持任意URL和Google搜索结果 | 备选网页抓取，实测curl更快时才用 |
| [self-improving](skills/self-improving/) | 自我反思+自组织记忆，触发：命令失败/用户纠正/发现更好方法 | 命令失败、用户纠正、知识过时时 |
| [github](skills/github/) | GitHub CLI (gh) 工作流 — PR/Issue/Repo/CodeReview | 操作GitHub Repo、PR、Issue、代码审查时 |
| [hermes-gateway-debug](skills/hermes-gateway-debug/) | Hermes Gateway连接状态排查 | Gateway报disconnected、微信/元宝无响应时 |
| [weixin-reconnect](skills/weixin-reconnect/) | 微信重连完整流程 | 微信Session expired或账号失联时 |
| [messenger-api-format-troubleshooting](skills/messenger-api-format-troubleshooting/) | 排查微信/元宝等messenger平台无法对话 | iLink会话过期或AI provider无响应时 |
| [find-skills](skills/find-skills/) | SkillHub/ClawHub技能搜索与安装 | 用户请求找/装技能时最高优先级触发 |
| [playwright](skills/playwright/) | 浏览器自动化，支持截图/爬虫/MCP | 需要无头浏览器操控网页时 |
| [browser-use](skills/browser-use/) | browser-use CLI，persistent session，支持cookie/profile/cloud | 需要复杂浏览器交互、cookie同步时 |
| [browser-screenshot](skills/browser-screenshot/) | 截图工具对比：npx playwright最佳，滚动翻页用Node脚本 | 需要截图网页、滚动翻页抓数据时 |
| [ocr-local-v2](skills/ocr-local-v2/) | Tesseract.js本地OCR，无需API Key | 图片文字识别、截图转文字时 |
| [data-analysis-skill](skills/data-analysis-skill/) | 数据分析技能包，抓取/清洗/可视化/报告 | 数据分析、Excel自动化、运营报告时 |
| [yuanbao](skills/yuanbao/) | 元宝群交互 — @成员、查询群信息 | 元宝群@提及其他用户、查询群信息时 |
| [skillhub-hermes-sync](skills/skillhub-hermes-sync/) | SkillHub与Hermes技能目录同步方法 | 同步/安装SkillHub技能时 |
| [miniprogram-architect](skills/miniprogram-architect/) | 小程序架构设计与分层 | 小程序项目架构设计、技术选型时 |
| [miniprogram-development](skills/miniprogram-development/) | 小程序开发全流程指南 | 小程序开发调试时 |
| [wechat-miniprogram-automator](skills/wechat-miniprogram-automator/) | 自动化微信小程序DevTools | 小程序自动化测试、DevTools驱动时 |
| [wechat-miniprogram-skill](skills/wechat-miniprogram-skill/) | 微信小程序入门到精通 | 小程序入门学习、开发时 |
| [wechat-miniprogram-toolkit](skills/wechat-miniprogram-toolkit/) | 小程序全栈开发（数据库/云函数/支付/TRTC） | 小程序全栈开发、微信支付、直播等复杂场景时 |
| [wechat-miniprogram-ui-ux](skills/wechat-miniprogram-ui-ux/) | 小程序UI/UX设计指南 | 小程序页面设计、交互优化时 |
| [tencentmap-miniprogram-skill](skills/tencentmap-miniprogram-skill/) | 腾讯位置服务小程序开发 | 小程序地图功能、LBS服务时 |
| [cloudbase](skills/cloudbase/) | CloudBase全栈开发套件（网站/小程序/云函数/数据库/托管） | CloudBase全栈开发、部署、数据库、云函数时 |
| [cloudbase-mcp](skills/cloudbase-mcp/) | CloudBase MCP Server | MCP配置、腾讯云开发工具集成时 |
| [session-lessons](skills/session-lessons/) | 本次对话积累的实战经验（技能安装/GitHub同步/微信Git认证） | 执行技能安装、GitHub同步、git.weixin.qq.com认证时 |
| [qq-email-reader](skills/qq-email-reader/) | QQ邮箱IMAP读取，用Python imaplib无需安装额外软件 | 读/搜索/整理QQ邮箱邮件时 |
| [himalaya](skills/himalaya/) | CLI邮件客户端，支持IMAP/SMTP/Notmuch | 终端管理邮件时（需先安装himalaya二进制） |
| [academic-deep-research](skills/academic-deep-research/) | 透明、严谨的学术研究方法论 | 学术研究、论文综述时 |
| [arxiv](skills/arxiv/) | 搜索、下载、总结arXiv论文 | 查找学术论文时 |
| [context7-api](skills/context7-api/) | Context7 API获取最新库文档 | 查询最新库文档时 |
| [deep-research-pro](skills/deep-research-pro/) | 多源深度研究Agent | 需要深度研究、多源搜索时 |
| [docker](skills/docker/) | Docker容器、镜像、Compose、网络、卷管理 | Docker相关操作时 |
| [dogfood](skills/dogfood/) | Web应用探索式QA测试 | 测试web应用时 |
| [excel-xlsx-1](skills/excel-xlsx-1/) | 创建、检查、编辑Excel/XLSX工作簿 | Excel相关操作时 |
| [frinkiac](skills/frinkiac/) | 搜索 Simpsons 剧照、生成表情包 | 需要 Simpsons meme 时 |
| [frontend-design-3](skills/frontend-design-3/) | 前端界面设计指南 | 前端界面设计时 |
| [frontend-design-ultimate](skills/frontend-design-ultimate/) | 静态站点React开发，含精美设计系统 | 高级前端开发时 |
| [gemini-deep-research](skills/gemini-deep-research/) | Gemini深度研究Agent | Gemini深度研究时 |
| [lb-shadcn-ui-skill](skills/lb-shadcn-ui-skill/) | shadcn/ui完整文档 | shadcn/ui组件使用时 |
| [markdown-converter](skills/markdown-converter/) | 文档转换为Markdown | 文档格式转换时 |
| [multi-search-engine](skills/multi-search-engine/) | 17个搜索引擎集成（8中文+9英文） | 需要多源搜索时 |
| [nextjs](skills/nextjs/) | Next.js 15 App Router开发 | Next.js项目开发时 |
| [ocr-local](skills/ocr-local/) | Tesseract OCR本地文字识别 | 图片文字识别时 |
| [qmd-cli](skills/qmd-cli/) | 本地知识库搜索 | 搜索本地笔记时 |
| [qmd-external](skills/qmd-external/) | 本地+外部混合搜索 | 混合搜索时 |
| [research-paper-writer](skills/research-paper-writer/) | IEEE/ACM格式学术论文写作 | 写学术论文时 |
| [tailwindcss](skills/tailwindcss/) | Tailwind CSS工具类 | Tailwind CSS开发时 |
| [tencent-docs](skills/tencent-docs/) | 腾讯文档在线协作 | 腾讯文档操作时 |
| [ui-ux-pro-max](skills/ui-ux-pro-max/) | UI/UX设计智能实现指导 | UI/UX设计时 |
| [weapp-automated-testing](skills/weapp-automated-testing/) | 小程序自动化测试工具包 | 小程序自动化测试时 |
| [weather](skills/weather/) | 天气查询，无需API Key | 查询天气时 |
| [web-search](skills/web-search/) | 网络搜索 | 需要网络搜索时 |
| [wechat-article-search](skills/wechat-article-search/) | 微信公众号文章搜索 | 搜索公众号文章时 |
| [wechat-article-spider](skills/wechat-article-spider/) | 微信公众号文章爬虫 | 爬取公众号文章时 |
| [wechat-sticker-maker](skills/wechat-sticker-maker/) | 微信表情包制作 | 制作微信表情包时 |
| [word-docx-1](skills/word-docx-1/) | 创建、检查、编辑Word文档 | Word文档操作时 |
| [youtube-watcher](skills/youtube-watcher/) | YouTube视频字幕抓取 | 获取YouTube字幕时 |

---

## 完整技能分类列表

### academic-deep-research
- academic-deep-research

### arxiv
- arxiv

### autonomous-ai-agents
- claude-code, codex, hermes-agent, opencode

### browser-use
- browser-use

### cloudbase
- ai-model-nodejs, ai-model-web, ai-model-wechat, auth-nodejs-cloudbase, auth-tool-cloudbase, auth-web-cloudbase, auth-wechat-miniprogram, cloud-functions, cloud-storage-web, cloudbase-agent, cloudbase-document-database-in-wechat, cloudbase-document-database-web-sdk, cloudbase-platform, cloudrun-development, data-model-creation, http-api-cloudbase, relational-database-mcp-cloudbase, relational-database-web-cloudbase, spec-workflow, ui-design, web-development

### creative
- architecture-diagram, ascii-art, ascii-video, baoyu-infographic, excalidraw, frinkiac, ideation, manim-video, p5js, pixel-art, songwriting-and-ai-music, wechat-sticker-maker

### data-science
- jupyter-live-kernel

### deep-research-pro
- deep-research-pro

### devops
- docker, webhook-subscriptions

### diagramming
- diagramming

### docker
- docker

### dogfood
- dogfood

### domain
- domain

### email
- himalaya, qq-email-reader

### excel-xlsx-1
- excel-xlsx-1

### feeds
- feeds

### frontend-design-3
- frontend-design-3

### frontend-design-ultimate
- frontend-design-ultimate

### gaming
- minecraft-modpack-server, pokemon-player

### gemini-deep-research
- gemini-deep-research

### gifs
- gif-search, gif-sticker-maker

### github
- claude-code, codebase-inspection, github, github-auth, github-cli-auth, github-code-review, github-issues, github-pr-workflow, github-repo-management

### hermes-gateway-debug
- hermes-gateway-debug

### inference-sh
- llama-cpp, obliteratus, outlines, serving-llms-vllm

### jina-web-fetcher
- jina-web-fetcher

### lb-shadcn-ui-skill
- lb-shadcn-ui-skill

### markdown-converter
- markdown-converter

### media
- gif-search, heartmula, songsee, youtube-content

### miniprogram-architect
- miniprogram-architect

### minimax
- android-native-dev, frontend-dev, frontend-design-ultimate, frontend-design-3, fullstack-dev, gif-sticker-maker, ios-application-dev, minimax-docx, minimax-multimodal-toolkit, minimax-pdf, minimax-xlsx, pptx-generator, shader-dev

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

### multi-search-engine
- multi-search-engine

### nextjs
- nextjs

### note-taking
- obsidian

### openclaw-imports
- find-skills, skillhub-preference

### playwright
- playwright

### productivity
- browser-screenshot, excel-xlsx-1, google-workspace, linear, maps, markdown-converter, nano-pdf, notion, ocr-and-documents, ocr-local, powerpoint, tencent-docs, weather, word-docx-1

### red-teaming
- godmode

### research
- academic-deep-research, arxiv, blogwatcher, context7-api, deep-research-pro, gemini-deep-research, multi-search-engine, qmd-cli, qmd-external, research-paper-writer, web-search, youtube-watcher

### research-paper-writer
- research-paper-writer

### self-improving
- self-improving

### session-lessons
- session-lessons

### shadcn
- lb-shadcn-ui-skill

### skillhub-hermes-sync
- skillhub-hermes-sync

### smart-home
- openhue

### software-development
- messenger-api-format-troubleshooting, plan, requesting-code-review, session-lessons, subagent-driven-development, systematic-debugging, test-driven-development, writing-plans

### summarize
- summarize

### tailwindcss
- tailwindcss

### tencent-docs
- tencent-docs

### tencentmap-miniprogram-skill
- tencentmap-miniprogram-skill

### ui-ux-pro-max
- ui-ux-pro-max

### weapp-automated-testing
- weapp-automated-testing

### weather
- weather

### web-fetch-performance
- web-fetch-performance

### wechat-article-search
- wechat-article-search

### wechat-article-spider
- wechat-article-spider

### wechat-miniprogram
- miniprogram-architect, miniprogram-development, wechat-miniprogram-automator, wechat-miniprogram-skill, wechat-miniprogram-toolkit, wechat-miniprogram-ui-ux, tencentmap-miniprogram-skill, weapp-automated-testing

### wechat-sticker-maker
- wechat-sticker-maker

### weixin-reconnect
- weixin-reconnect

### word-docx-1
- word-docx-1

### youtube-watcher
- youtube-watcher

### yuanbao
- yuanbao
