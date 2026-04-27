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

- [14:27] 批量安装技能时不要逐个调用 skills-sync.sh
  - skills-sync.sh 每次都 git fetch 远程（30-40s），N 个技能串行就很慢
  - 正确做法：所有技能安装完成后，统一做一次 SKILLS.md 更新 + git add + commit + push
  - Commit 已经 staging 了，直接 amend 或新开一个 commit 都比串行快
  - 发现场景：连续安装 7 个微信小程序技能时，逐个调用导致前台阻塞
