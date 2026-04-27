# Self-Improving Memory

## Confirmed Preferences
<!-- Patterns confirmed by user, never decay -->

## Active Patterns
<!-- Patterns observed 3+ times, subject to decay -->

## Recent (last 7 days)
<!-- New corrections pending confirmation -->

## 2026-04-26T22:38:12 [note] 测试记录：Self-improving pending 机制上线

heartbeat.sh 自动处理 pending/ 目录，分类写入 memory.md 或 corrections.md

## 2026-04-27

### Hermes Skills Physical Copy Rule
SkillHub 安装的技能必须物理复制到 `~/.hermes/skills/`，symlink 不被 Hermes 识别为 local 技能。

### GitHub Push Diagnostics
GitHub push 超时/失败时，用 `background + log` 方式排查比直接等待更有效：`GIT_TRACE=1 git push > /tmp/git-push.log 2>&1`

### GitHub Sync Protocol (hermes-skills)
- 仓库：`SingleDemo/hermes-skills`，同步脚本：`~/.hermes/skills-sync.sh`
- 增删技能后 SKILLS.md 必须同步更新并 commit
- `.hub/` 目录已加入 .gitignore 不上传
