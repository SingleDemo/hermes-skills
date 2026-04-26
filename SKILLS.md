---
name: skills-directory
description: "MANDATORY: Skill directory for quick reference. Must be reviewed at conversation start and updated after every skill installation."
---

# Skills Directory

> **强制规则（每次对话必须遵守）：>
>
> 1. **对话开始时**：审阅本目录，判断当前任务是否有匹配的技能可用。如果有，立即调用。
> 2. **安装新技能后**：必须更新本目录，补充新技能的条目。
> 3. **不确定是否适用时**：优先查看技能的 SKILL.md 确认触发条件。

---

## 已安装技能速查表

| 技能 | 一句话说明 | 何时触发 |
|------|-----------|----------|
| [agent-browser](skills/agent-browser/) | 无头浏览器自动化 CLI，导航/点击/输入/截图 | 需要操控网页、抓取页面内容、浏览器自动化时 |
| [summarize](skills/summarize/) | summarize CLI 总结 URL/文件（网页/PDF/图片/音频/YouTube） | 需要快速总结网页、文档、视频、音频内容时 |
| [self-improving](skills/self-improving/) | 自我反思+自我批评+自组织记忆系统 | 命令失败、用户纠正、知识过时时 |
| [github](skills/github/) | GitHub CLI (gh) 工作流 — PR/Issue/Repo/CodeReview | 操作 GitHub Repo、PR、Issue、代码审查时 |
| [hermes-gateway-debug](skills/hermes-gateway-debug/) | Hermes Gateway 连接状态排查 | Gateway 报 disconnected、微信/元宝无响应时 |
| [weixin-reconnect](skills/weixin-reconnect/) | 微信重连完整流程 | 微信 Session expired、或账号失联时 |
| [messenger-api-format-troubleshooting](skills/messenger-api-format-troubleshooting/) | 排查微信/元宝等 messenger 平台无法对话 | iLink 会话过期或 AI provider 无响应时 |
| [find-skills](skills/find-skills/) | SkillHub/ClawHub 技能搜索与安装 | 用户请求找/装技能时最高优先级触发 |
| [yuanbao](skills/yuanbao/) | 元宝群交互 — @成员、查询群信息 | 元宝群 @提及其他用户、查询群信息时 |
| [weixin-reconnect](skills/weixin-reconnect/) | 微信重连完整流程 | 微信 Session expired 或账号失联时 |

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
| security-review | 安全审查 | 对变更做安全审查时 |
| github-pr-workflow | PR 完整生命周期 | Create/PR/Review/Rebase/Merge PR 时 |
| github-issues | Issue 管理 | 创建/搜索/关闭 Issue 时 |
| github-code-review | GitHub 代码审查 | 分析 diff、留 inline 评论时 |
| claude-code | Claude Code CLI 委托编码 | 委托编码任务给 Claude Code 时 |
| codex | OpenAI Codex CLI 委托编码 | 委托编码任务给 Codex 时 |
| opencode | OpenCode CLI 委托编码 | 委托编码任务给 OpenCode 时 |
| dogfood | Web 应用探索式 QA 测试 | 测试 web 应用时 |
| heartbeat | 定时任务管理 | 管理 cron job 时 |

---

## 维护规则

- **新增技能后**：在对应表格中添加一行
- **删除技能后**：必须同步移除对应行
- **技能描述保持一句话**，详细信息查看 SKILL.md
- **不确定触发条件时**，阅读技能的 SKILL.md
