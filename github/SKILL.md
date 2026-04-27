---
name: github
description: GitHub workflow skills for managing repositories, pull requests, code reviews, issues, and CI/CD pipelines using the gh CLI and git via terminal.
---

# GitHub Skill

## 子技能（按需使用）

| 子技能 | 说明 |
|--------|------|
| [github-pr-workflow](github-pr-workflow/) | PR 完整生命周期 |
| [github-issues](github-issues/) | Issue 管理 |
| [github-code-review](github-code-review/) | 代码审查 |
| [github-repo-management](github-repo-management/) | Repo 管理 |
| [github-auth](github-auth/) | GitHub 认证 |
| [github-cli-auth](github-cli-auth/) | GitHub CLI 认证（PAT） |
| [codebase-inspection](codebase-inspection/) | 代码库统计 |

## 快速使用

```bash
# 查看 PR
gh pr list

# 创建 PR
gh pr create -t "标题" -b "描述"

# 代码审查
gh pr review PR号 --comment "评论"

# 查看 Issue
gh issue list
```
