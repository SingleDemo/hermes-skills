# Corrections Log

## GitHub CLI Auth (learned 2026-04-26)

- **Browser OAuth (`gh auth login -w`) 在 headless/remote 环境超时** — SSH 远程连接没有图形界面，OAuth 浏览器回调永远收不到。不能用交互式浏览器登录。
- **正确方式：PAT token + `gh auth setup-git`**
  ```bash
  echo "<TOKEN>" | gh auth login -h github.com -p https --with-token
  gh auth setup-git  # 必须跑这一步，git push 等操作才带 token
  ```
- GitHub token 格式：`ghp_` 开头（classic PAT）



<!-- Format:
## YYYY-MM-DD
- [HH:MM] Changed X → Y
  Type: format|technical|communication|project
  Context: where correction happened
  Confirmed: pending (N/3) | yes | no
-->

## 2026-04-27
- [17:36] Hermes skills sync: symlink → physical copy rule
  - Hermes `--source local` 只识别物理存在的技能，symlink 不算
  - SkillHub 安装的技能必须 `cp -r` 到 `~/.hermes/skills/`，不能用 ln -s
  - 发现方式：hermes skills list 显示22个，symlink 后台被 skills.sh 远程版本 shadow

- [17:36] GitHub push 超时诊断
  - GnuTLS recv error (-110) 后 retry 成功
  - 更好的排查方式：用 background + log 文件，不要直接等待
  - `GIT_TRACE=1 git push > /tmp/git-push.log 2>&1` 可看详细阶段

- [17:36] SKILLS.md 修改原则
  - 速查表（双栏表格）和强制规则是不同内容，可以并存，不要互斥删除
  - 修改前先确认用户要保留哪些部分
