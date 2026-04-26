---
name: github-cli-auth
description: GitHub CLI 认证。当浏览器 OAuth 流程失败（超时、TTY 问题）时，使用 PAT token 登录。登录后必须运行 gh auth setup-git 才能执行 git push。
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, gh, auth, pat, ssh]
    related_skills: [github/github-repo-management, github/github-pr-workflow]
---

# GitHub CLI 认证

## 场景一：浏览器 OAuth 登录失败

在非交互式/PTY 受限环境下（terminal timeout、session 中断、CLI 无 TTY），浏览器 OAuth 流程（`gh auth login -w`）会失败：OAuth 回调超时、无法接收 device code。

**解决方案：用 PAT（Personal Access Token）登录**

```bash
# 1. 获取 PAT（勾选 repo, read:user 权限）
# 2. 用 token 登录
echo "$GITHUB_TOKEN" | gh auth login -h github.com -p https --with-token

# 3. 启用 git 操作（必须，否则 git push 失败）
gh auth setup-git
```

## 场景二：正常浏览器登录

```bash
gh auth login -h github.com -p ssh -w
# 浏览器打开 https://github.com/login/device，输入验证码
```

## 验证

```bash
gh auth status
```

## 注意事项

- `gh auth setup-git` 必须在 token 登录后单独执行，否则 git push 报 `could not read Username`
- HTTPS protocol（`-p https`）比 SSH 更可靠，不依赖 SSH key
- PAT 方式登录后 token 已保存，后续无需再登录
