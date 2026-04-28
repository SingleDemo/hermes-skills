---
name: skillhub-hermes-sync
description: SkillHub 技能安装目录与 Hermes 技能目录的对应关系，软链接同步方法
---

# SkillHub 与 Hermes 技能目录同步

## 问题背景

- SkillHub 安装路径：`~/skills/`（如 `~/skills/jina-web-fetcher/`）
- Hermes 技能目录：`~/.hermes/skills/`
- Hermes 只读 `~/.hermes/skills/` 下的技能，不会自动读 `~/skills/`

## 解决方案：物理复制（不能用软链接）

**重要：** Hermes 只识别 `~/.hermes/skills/` 下的物理目录。软链接不被识别为 local 技能。

正确的同步步骤：

```bash
# 1. 安装到 ~/skills/
skillhub install <slug>

# 2. 如果目标已是 symlink，先删除（rm -rf 不是 rm -f）
rm -rf ~/.hermes/skills/<slug>

# 3. 物理复制到 Hermes 技能目录（cp -r 或 Python shutil.copytree）
cp -r ~/skills/<slug>/ ~/.hermes/skills/<slug>/
# 或者用 Python:
# shutil.copytree(os.path.expanduser("~/skills/<slug>"),
#                 os.path.expanduser("~/.hermes/skills/<slug>"))

# 4. 验证是物理目录（不是 symlink）
ls -la ~/.hermes/skills/<slug>/ | head -3
# 正确输出: drwxr-xr-x ...  SKILL.md  (d 开头，不是 l 开头)

# 5. Git 提交（不要提交 symlink）
cd ~/.hermes/skills
git add <slug>/
git commit -m "feat: add <slug> from skillhub"
git push origin main
```

## 为什么不能 symlink

`.hermes/skills/` 下的 symlink 不会被 Hermes 识别为 local 技能目录。
即使 `readlink` 显示正确指向，Hermes Agent 的技能加载器也只认物理文件。

## 批量安装时的清理顺序

如果先 `ln -sf` 创建了 symlink，再 `shutil.copytree()` 会因目标已存在而失败。
正确顺序：**先 `rm -rf` 清理，再用 `cp -r` 复制**。

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
