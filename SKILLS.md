# Hermes Skills — 强制协议

> ⚠️ **每次对话开始时，以下步骤必须按顺序执行（不可跳过）：**
> 1. 调用 `skills_list()` 获取完整技能列表
> 2. 读取本文件 `~/.hermes/skills/SKILLS.md`
> 3. 判断是否有匹配技能，若有则立即 `skill_view(name)` 加载
> 4. 若涉及 Web 抓取，优先加载 `web-fetch-performance` 技能

---

## GitHub 同步规则（强制）

所有技能增/删操作必须同步到 GitHub 仓库 `SingleDemo/hermes-skills`。

### 技能同步协议

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

**提交信息规范：** `<action>: <skill-name> — <简短说明>`
- 添加：`add: <skill-name> — <说明>`
- 删除：`remove: <skill-name> — <说明>`
- 更新：`update: <skill-name> — <说明>`
- 同步：`sync: SKILLS.md — <说明>`

**注意事项：**
- `symlink` 不被 Hermes 识别为 local 技能，技能必须物理存在于 `~/.hermes/skills/`
- skillhub 安装的技能需要物理复制到 `~/.hermes/skills/`，不是 symlink
- minimax 大技能包（11MB，300+ 文件）上传 GitHub 时注意大小限制

---

## 技能分类列表

### autonomous-ai-agents
- claude-code: Delegate coding tasks to Claude Code (Anthropic's CLI agent)
- codex: Delegate coding tasks to OpenAI Codex CLI agent
- hermes-agent: Complete guide to using and extending Hermes Agent
- opencode: Delegate coding tasks to OpenCode CLI agent

### creative
- architecture-diagram: Generate dark-themed SVG diagrams of software systems
- ascii-art: ASCII art using pyfiglet, cowsay, boxes
- ascii-video: Production pipeline for ASCII art video
- baoyu-infographic: Generate professional infographics with 21 layout types
- excalidraw: Create hand-drawn style diagrams using Excalidraw JSON format
- ideation: Generate project ideas through creative constraints
- manim-video: Production pipeline for mathematical and technical animations
- p5js: Production pipeline for interactive and generative visuals
- pixel-art: Convert images into retro pixel art
- songwriting-and-ai-music: Songwriting craft and AI music generation prompts (Suno)

### data-science
- jupyter-live-kernel: Use a live Jupyter kernel for stateful, iterative Python workflows

### devops
- webhook-subscriptions: Create and manage webhook subscriptions for event-driven workflows

### dogfood
- dogfood: Systematic exploratory QA testing of web applications

### email
- himalaya: CLI to manage emails via IMAP/SMTP

### gaming
- minecraft-modpack-server: Set up a modded Minecraft server from CurseForge/Modrinth modpacks
- pokemon-player: Play Pokemon games autonomously via headless emulation

### github
- codebase-inspection: Inspect and analyze codebases using pygount for LOC counting
- github: GitHub workflow skills for managing PRs, issues, repos, and CI/CD
- github-auth: Set up GitHub authentication using git (universal)
- github-cli-auth: GitHub CLI authentication when browser OAuth fails
- github-code-review: Review code changes by analyzing git diffs
- github-issues: Create, manage, triage, and close GitHub issues
- github-pr-workflow: Full pull request lifecycle management
- github-repo-management: Clone, create, fork, configure, and manage GitHub repos

### hermes-gateway-debug
- hermes-gateway-debug: Hermes Gateway connection troubleshooting

### jina-web-fetcher
- jina-web-fetcher: Fetch web page content using Jina AI (bypasses search engine restrictions)

### media
- gif-search: Search and download GIFs from Tenor using curl
- heartmula: Set up and run HeartMuLa, the open-source music generation model
- songsee: Generate spectrograms and audio feature visualizations
- youtube-content: Fetch YouTube video transcripts and transform into summaries

### minimax
- android-native-dev: Android native application development guide
- frontend-dev: Full-stack frontend development with premium UI design
- fullstack-dev: Full-stack backend architecture and frontend-backend integration
- gif-sticker-maker: Convert photos into animated GIFs and stickers
- ios-application-dev: iOS application development guide (UIKit, SwiftUI, SnapKit)
- minimax-docx: Professional DOCX document creation and editing
- minimax-multimodal-toolkit: MiniMax multimodal model skill (image, music, TTS, video)
- minimax-pdf: PDF creation with visual quality and design identity
- minimax-xlsx: Excel/spreadsheet creation, reading, editing, and validation
- pptx-generator: PowerPoint presentation generation and editing
- shader-dev: Comprehensive GLSL shader techniques for stunning visuals

### minimax-mcp
- minimax-mcp: MiniMax official MCP server installation and Hermes configuration (API_HOST, API key)

### mlops
- huggingface-hub: Hugging Face Hub CLI — search, download, and upload models
- evaluating-llms-harness: Evaluate LLMs across 60+ academic benchmarks
- weights-and-biases: Track ML experiments with automatic logging and visualization

### mlops/inference
- llama-cpp: Run LLM inference with llama.cpp on CPU, Apple Silicon, AVX2
- obliteratus: Remove refusal behaviors from open-weight LLMs
- outlines: Guarantee valid JSON/XML/code structure during generation
- serving-llms-vllm: Serve LLMs with high throughput using vLLM's PagedAttention

### mlops/models
- audiocraft-audio-generation: PyTorch library for audio generation (MusicGen, AudioGen, Se-Co)
- segment-anything-model: Foundation model for image segmentation with zero-shot transfer

### mlops/research
- dspy: Build complex AI systems with declarative programming

### mlops/training
- axolotl: Expert guidance for fine-tuning LLMs with Axolotl YAML configs
- fine-tuning-with-trl: Fine-tune LLMs using reinforcement learning with TRL (SFTTrainer, DPO, GRPO)
- unsloth: Expert guidance for fast fine-tuning with Unsloth (2-5x speed, 70% less memory)

### mcp
- cloudbase-mcp: Tencent CloudBase MCP Server — full-stack cloud development
- native-mcp: Built-in MCP client that connects to MCP servers configured in config.yaml

### note-taking
- obsidian: Read, search, and create notes in the Obsidian vault

### openclaw-imports
- find-skills: Highest-priority skill discovery flow
- skillhub-preference: Prefer `skillhub` for skill discovery, installation, and updates

### productivity
- google-workspace: Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration
- linear: Manage Linear issues, projects, and teams via GraphQL API
- maps: Location intelligence — geocode, reverse-geocode, directions, time zones
- nano-pdf: Edit PDFs with natural-language instructions using nano PDF editor
- notion: Notion API for creating and managing pages, databases, and blocks
- ocr-and-documents: Extract text from PDFs and scanned documents
- powerpoint: Create, edit, and read PowerPoint presentations
- web-fetch-performance: Web fetch speed comparison and fallback strategy (curl > mcp_fetch > jina > browser)

### red-teaming
- godmode: Jailbreak API-served LLMs using G0DM0D3 techniques

### research
- arxiv: Search and retrieve academic papers from arXiv
- blogwatcher: Monitor blogs and RSS/Atom feeds for updates
- llm-wiki: Karpathy's LLM Wiki — build and maintain a persistent LLM knowledge base
- polymarket: Query Polymarket prediction market data

### skillhub-hermes-sync
- skillhub-hermes-sync: SkillHub skill installation directory and Hermes skills directory sync

### smart-home
- openhue: Control Philips Hue lights, rooms, and scenes via OpenHue API

### social-media
- xurl: Interact with X/Twitter via xurl, the official X API CLI

### software-development
- messenger-api-format-troubleshooting: Diagnose WeChat/Yuanbao messaging platform issues
- plan: Plan mode for Hermes — inspect context, write a markdown plan, execute in subagent
- requesting-code-review: Pre-commit verification pipeline (static scan, security scan, tests)
- subagent-driven-development: Execute implementation plans with independent subagents
- systematic-debugging: Systematic debugging methodology for bugs, test failures, unexpected behavior
- test-driven-development: TDD approach before writing any feature or bugfix code
- writing-plans: Write comprehensive plans from specs or requirements

### summarize
- summarize: Summarize URLs or files with the summarize CLI (web, PDFs, documents)

### weixin-reconnect
- weixin-reconnect: WeChat reconnection full workflow (session expired or account lost)

### yuanbao
- yuanbao: Yuanbao group interaction — @mention users, query group members
