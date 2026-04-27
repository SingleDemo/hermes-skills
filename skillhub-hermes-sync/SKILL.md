---
name: skillhub-hermes-sync
description: SkillHub 技能安装目录与 Hermes 技能目录的对应关系，软链接同步方法
---

# SkillHub 与 Hermes 技能目录同步

## 问题背景

- SkillHub 安装路径：`~/skills/`（如 `~/skills/jina-web-fetcher/`）
- Hermes 技能目录：`~/.hermes/skills/`
- Hermes 只读 `~/.hermes/skills/` 下的技能，不会自动读 `~/skills/`

## 解决方案：软链接同步

SkillHub 安装后，需要手动（或通过 skill_manage）同步到 `.hermes/skills/`：

```bash
ln -sf ~/skills/jina-web-fetcher ~/.hermes/skills/jina-web-fetcher
ln -sf ~/skills/agent-browser ~/.hermes/skills/agent-browser
ln -sf ~/skills/summarize ~/.hermes/skills/summarize
ln -sf ~/skills/self-improving ~/.hermes/skills/self-improving
```

## 验证

```bash
ls -la ~/.hermes/skills/技能名   # 应该显示 -> 指向 ~/skills/xxx 的软链接
```

## SKILLS.md 更新

新增技能后，必须同步更新 `~/.hermes/skills/SKILLS.md` 的"已安装技能速查表"。

## 已验证需要同步的技能

| 技能 | 来源 | 状态 |
|------|------|------|
| jina-web-fetcher | SkillHub | ✅ 已同步 |
| agent-browser | SkillHub | ✅ 已同步 |
| summarize | SkillHub | ✅ 已同步 |
| self-improving | SkillHub | ✅ 已同步 |
| web-fetch-performance | 手动创建 | ✅ 已在 .hermes/skills/ |
| github | 内置+SkillHub混合 | ✅ 已补全根 SKILL.md |
