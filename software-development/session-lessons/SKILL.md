---
name: session-lessons
description: 本次对话积累的实战经验与教训，覆盖技能安装、GitHub同步、微信Git认证等操作规范。触发时机：执行技能安装、GitHub同步、git.weixin.qq.com认证、memory工具调用时。
version: 1.0.0
author: hermes
tags: [workflow, git, skillhub, github, wechat]
---

# Session Lessons — 实战经验积累

> 本次对话（2026-04-27）积累的教训与经验，可复用的工作流。

---

## 经验一：技能安装同步流程（强制）

**场景**：用户请求安装 SkillHub 技能

**标准流程（必须按顺序执行）**：

1. 检查 SkillHub 是否已安装：`which skillhub`
2. `skillhub install <skill-name>`
3. `cp -r ~/skills/<skill-name> ~/.hermes/skills/`（物理复制，非 symlink）
4. `hermes skills list --source local` 验证
5. **更新 SKILLS.md**：在"已安装技能速查表"和"完整技能分类列表"添加条目
6. **同步 GitHub**：`cd ~/.hermes/skills && git add -A && git commit -m "Add <skill-name>" && git push origin main`
   - 注意：多个技能一起装时，先全部 commit 再 push，比逐个 sync 快得多

**踩坑**：Hermes 的 `hermes skills list --source local` 只识别物理存在的目录，symlink 不算 local。

---

## 经验二：GitHub push 加速

**场景**：需要频繁 push 到 GitHub

**问题**：`~/.hermes/skills-sync.sh` 脚本每次都 `git fetch` 远程再做比较，7 个技能串行调用极慢。

**解法**：多个技能一起装时，直接：
```bash
cd ~/.hermes/skills
git add -A
git commit -m "Add X skills"
git push origin main
```
一次 push 完成，比逐个调用 sync 脚本快 5-8 倍。

---

## 经验三：git.weixin.qq.com 认证

**场景**：访问微信开发者平台 Git 仓库

**认证命令**：
```bash
git config --global credential.helper store
git credential approve <<'EOF'
protocol=https
host=git.weixin.qq.com
username=<用户名>
password=<密码>
EOF
git ls-remote https://git.weixin.qq.com/<账号>/<仓库名>.git
```

**踩坑**：
- git.weixin.qq.com 不支持 Access Token，只支持用户名+密码
- 微信开发者工具扫码登录 ≠ Git 凭证，需要单独配置
- SSH 方式 (`git@git.weixin.qq.com`) 需要 SSH key 且 port 22 可能不通

---

## 经验四：浏览器在此环境无法启动

**场景**：需要操控浏览器时

**问题**：Chrome/agent-browser 在此 Linux 环境因沙箱限制无法启动，报 `No usable sandbox!`

**解法**：
- agent-browser CLI 同样受影响
- 改用 `curl` 直接请求验证连通性
- Web 抓取用 `curl` 而非浏览器

---

## 经验五：MCP fetch 配置已删除

**时间**：2026-04-27

**原因**：用户明确要求删除，理由：不好用、不稳定、不是最优方案

**删除内容**：`config.yaml` 中的 `mcp_servers.fetch` 配置块（modelscope streamable_http）

**现状**：MiniMax MCP (`minimax-mcp-js`) 保留，CloudBase MCP (`cloudbase-mcp`) 保留，fetch 已移除。

---

## 经验六：微信开发者平台 Access Token 路径不存在

**场景**：用户问 git.weixin.qq.com 的 Access Token 在哪里

**结论**：微信公众平台后台没有 Git 私人令牌生成入口。git.weixin.qq.com 使用标准 HTTP Basic Auth（用户名+密码），不支持 OAuth2 token。

---

## 经验七：SKILLS.md 格式维护

**场景**：更新 SKILLS.md 时

**注意**：
- "已安装技能速查表"和"完整技能分类列表"是独立区域，patch 时要精确匹配避免误伤相邻条目
- 新增条目只追加不删除已有内容
- 表格格式：`| [name](skills/name/) | 说明 | 触发时机 |`

---

## 经验八：YAML 配置文件中替换 token 的正确方法

**场景**：替换 `config.yaml` 中的 API token

**踩坑汇总**：

1. **终端显示截断 ≠ 文件内容截断**：很多工具（`cat`、terminal output）碰到超长行会用 `...` 截断显示，但实际文件内容可能是完整的。用 Python 读取文件逐行检查 token 长度才能确认。

2. **heredoc 变量展开问题**：`cat <<EOF` 在 zsh/bash 中会展开 `$variable`，如果 token 包含 `$` 或看起来像变量名，会被替换成空值导致 token 损坏。解法：用 Python 写入或 `cat <<'EOF'`（单引号抑制展开）。

3. **sed/patch 文本替换失败**：当 old_string 和实际文件内容之间有不可见字符差异（制表符 vs 空格、隐藏字符）时，patch/replace 会匹配失败。解法：用 Python 打开文件，print repr 确认实际字节内容，再决定怎么替换。

4. **正确替换流程**：
   ```python
   python3 -c "
   with open('/path/to/config.yaml', 'rb') as f:
       content = f.read()
   # 用 b'...' bytes 方式处理，避免编码问题
   old = b'old-token'
   new = b'new-token'
   if old in content:
       content = content.replace(old, new)
       with open('/path/to/config.yaml', 'wb') as f:
           f.write(content)
       print('替换成功')
   else:
       print('未找到目标')
   "
   ```

5. **验证 token 完整性**：替换后用 Python 逐字节读取，不要依赖终端显示。
   ```python
   with open('/path/to/config.yaml') as f:
       for i, line in enumerate(f, 1):
           if 'MINIMAX_API_KEY' in line:
               token = line.strip().split(': ', 1)[1]
               print(f'长度: {len(token)}, 前缀: {token[:10]}, 后缀: {token[-10:]}')
   ```

---

## 经验九：memory 工具会冻结 Hermes（重要）

**触发条件**：`memory` 工具被调用后，Hermes 平台会在对话中显示"💾 Memory updated"标记，随后 Hermes 无法响应。

**发现过程**：
- 用户观察到：每次说完某类内容后 Hermes 就冻住，排查发现是 memory 工具调用
- memory 工具调用成功后会返回完整 memory entries，Hermes 渲染该消息时触发冻结
- 触发后的恢复方式：用户手动 restart Hermes

**解法**：
- 不在对话中调用 memory 工具（改为 execute_code/python 写文件）
- 如必须使用 memory 工具，不在对话中返回结果给用户（工具本身不显示结果）
- 重要记忆直接写在对话里告知用户，由用户在后续新会话中自己写入

**备查：记忆文件写入方式**
```python
# 用 execute_code 写记忆文件
with open('/home/agentuser/.hermes/memory_notes.txt', 'a') as f:
    f.write(f"{datetime}: {重要内容}\n")
```

---

---

## 经验十：himalaya CLI 在此环境无法安装，但 imaplib 完美替代

**时间**：2026-04-29
**场景**：用户要求配置 QQ 邮箱（1634064164@qq.com）用于读取/整理邮件

**himalaya 安装尝试（全部失败）**：
- 官方安装脚本 → 超时（GitHub 下载被拦截）
- cargo install → cargo 不存在
- 直接下载 release tarball → 被拦截
- apt/snap → 无包

**但发现**：`python3 -c "import imaplib"` 直接可用！QQ 邮箱 IMAP 完全正常。

**教训**：配置邮件客户端前先测 `python3 -c "import imaplib"`——Python stdlib 在此环境比任何第三方 CLI 都靠谱。QQ 邮箱授权码在网页版 QQ邮箱设置 → 账户 → 生成 IMAP 授权码。

**附：GitHub push 超时 → 用后台模式**
```bash
# 前台超时（30s内无法完成）
git push

# 后台模式
terminal(background=true, command="cd ~/.hermes/skills && git push", notify_on_complete=true)
# 然后 poll session 检查结果
```

---

## 经验十一：SKILLS.md 重建脚本

**时间**：2026-04-29

**发现**：目录有 78 个，SKILLS.md 表格只记录了 28 个——严重脱节。原因：之前多次安装 skill 但没同步更新 SKILLS.md。

**重建脚本**：`~/.hermes/scripts/rebuild-skills-md.py`

**重建后**：
- 实际 top-level skill：49 个
- 加上子目录（如 email/）：51 个
- SKILLS.md 表格：76 个全部录入
- GitHub commit: `de2196e`

**教训**：以后每次增删 skill 后，同步更新 SKILLS.md + commit 不要分两次提交（容易忘）。

*本 skill 由 session-lessons 自动积累，下次遇到相同场景直接加载使用。*
