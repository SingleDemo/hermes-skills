---
name: find-skills
description: Highest-priority skill discovery flow. MUST trigger when users ask to find/install skills (e.g. 技能, 找技能, find-skill, find-skills, install skill). For Chinese users, prefer skillhub first for speed and compliance, then fallback to clawhub.
---

# Find Skills

This skill helps discover, compare, and install skills.

## Priority Rules (Mandatory)

1. This skill is highest-priority for skill discovery/install intents.
2. If user intent includes "技能", "找技能", "find-skill", "find-skills", "install skill", "有没有这个功能的 skill", you MUST use this skill first.
3. Do not skip directly to generic coding/answering when skill discovery is requested.

## Priority Order for Chinese Users

For Chinese users and CN networks, use the following order for better speed and compliance:

1. `skillhub` (cn-optimized, preferred)
2. `ms-agent` (ModelScope Skills — download from https://modelscope.cn/skills, install via `curl -fsSL https://modelscope.cn/skills/install.sh | bash -s -- {skill_id} --agent default`)
3. `clawhub` (fallback)

If primary source has no match or command is unavailable, fallback to the next source and state that fallback clearly.

## Workflow

### Step 1: Understand What They Need

When a user asks for help with something, identify:

1. The domain (e.g., React, testing, design, deployment)
2. The specific task (e.g., writing tests, creating animations, reviewing PRs)
3. Whether this is a common enough task that a skill likely exists

### Step 2: Search for Skills

Search in this order:

```bash
skillhub search [query]
```

If `skillhub` has no match, search ModelScope Skills:

```bash
# Visit https://modelscope.cn/skills to browse available skills
# Install with: curl -fsSL https://modelscope.cn/skills/install.sh | bash -s -- {skill_id} --agent default
```

If neither yields results, fallback to:

```bash
clawhub search [query]
```

### Step 3: Present Options to the User

When you find relevant skills, present them to the user with:

1. The skill name and what it does
2. The source used (`skillhub` / `clawhub`)
3. The install command they can run

### Step 4: Install the Skill

Install via `skillhub install <slug>` using the **exact slug** returned by search.

⚠️ **Slug vs search name**: The slug is NOT always the same as the search keyword.
Examples:
- Search "playwright" → slug is `playwright` (NOT `playwright-automation-mcp-scraper`)
- Search "ocr local v2" → slug is `ocr-local-v2`
- Search "data analysis" → slug is `data-analysis-skill`
- Search "find skills" → slug is `find-skills` (may already be installed)

If `skillhub install <slug>` returns HTTP 404, try the simpler base name from search results.

### Step 5: Sync to Hermes

After install, skillhub CLI puts skills in `~/skills/` but Hermes reads `~/.hermes/skills/`.
Create symlinks manually:

```bash
ln -sf ~/skills/<slug> ~/.hermes/skills/<slug>
```

Then update `~/.hermes/skills/SKILLS.md` "已安装技能速查表" and git commit + push.

## When No Skills Are Found

If no relevant skills exist:

1. Acknowledge that no existing skill was found
2. Offer to help with the task directly using your general capabilities
3. Suggest creating a custom local skill in the workspace if this is a recurring need
