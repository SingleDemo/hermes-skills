---
name: qq-email-reader
description: Read, search, summarize, and manage QQ邮箱 via IMAP using Python imaplib. No extra install needed — uses stdlib. QQ邮箱 IMAP 端口 993，授权码认证。
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [email, QQ邮箱, IMAP]
prerequisites:
  commands: [python3]
  credentials:
    - QQ邮箱地址: 1634064164@qq.com
    - IMAP授权码: zjmwduyzutxmbheb (stored in memory only)
---

# QQ邮箱读取器

## 连接参数

- Host: `imap.qq.com` / Port: `993` (IMAP over SSL)
- SMTP: `smtp.qq.com` / Port: `465` 或 `587`
- 登录方式: 邮箱地址 + **IMAP授权码**（不是登录密码）
- 授权码在 QQ 邮箱网页版 → 设置 → 账户 → POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务 → 生成授权码

## Python 连接模板

```python
import imaplib, email
from email.header import decode_header

def decode_str(s):
    """解码 email header"""
    if not s: return ''
    parts = decode_header(s)
    result = []
    for part, enc in parts:
        if isinstance(part, bytes):
            result.append(part.decode(enc or 'utf-8', errors='replace'))
        else:
            result.append(part)
    return ''.join(result)

def connect_qq_mail():
    mail = imaplib.IMAP4_SSL('imap.qq.com', 993)
    mail.login('你的QQ号@qq.com', '授权码')
    return mail

# 使用示例
mail = connect_qq_mail()
mail.select('INBOX')
status, msgs = mail.search(None, 'ALL')
ids = msgs[0].split()
print(f'总邮件数: {len(ids)}')
mail.logout()
```

## 常用操作

### 读取最新 N 封邮件摘要

```python
mail = connect_qq_mail()
mail.select('INBOX')
_, msgs = mail.search(None, 'ALL')
ids = msgs[0].split()
recent = ids[-10:]  # 最新10封

for uid in reversed(recent):
    _, msg = mail.fetch(uid, '(RFC822.HEADER)')
    m = email.message_from_bytes(msg[0][1])
    print(f'ID:{uid.decode()} | {m["Date"]} | {decode_str(m["From"])} | {decode_str(m["Subject"])}')
mail.logout()
```

### 搜索邮件

```python
# 按发件人搜索
_, msgs = mail.search(None, 'FROM "github.com"')

# 按主题搜索
_, msgs = mail.search(None, 'SUBJECT "GitHub"')

# 组合搜索
_, msgs = mail.search(None, 'FROM "github.com" SUBJECT "PAT"')

# 按日期搜索 (最近7天)
from datetime import datetime, timedelta
date = (datetime.now() - timedelta(days=7)).strftime('%d-%b-%Y')
_, msgs = mail.search(None, f'SINCE {date}')
```

### 读取邮件正文

```python
_, msg = mail.fetch(msg_id, '(RFC822)')
m = email.message_from_bytes(msg[0][1])

# 提取纯文本正文
def get_body(m):
    if m.is_multipart():
        for part in m.walk():
            ct = part.get_content_type()
            if ct == 'text/plain':
                charset = part.get_content_charset() or 'utf-8'
                return part.get_payload(decode=True).decode(charset, errors='replace')
    else:
        charset = m.get_content_charset() or 'utf-8'
        return m.get_payload(decode=True).decode(charset, errors='replace')
    return ''

print(get_body(m))
```

### 读懂 QQ 邮箱文件夹

```
INBOX          收件箱
Sent          已发送
Drafts        草稿箱
Trash         垃圾箱
&quot;INBOX/Drafts&quot;  自定义文件夹（如有）
```

### 标记已读/删除

```python
# 标记已读
mail.store(msg_id, '+FLAGS', '\\Seen')

# 删除邮件
mail.store(msg_id, '+FLAGS', '\\Deleted')

# 彻底删除（删除已标记的邮件）
mail.expunge()
```

## 发送邮件（需要 SMTP）

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = '1634064164@qq.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = '测试邮件'
msg.attach(MIMEText('邮件正文', 'plain', 'utf-8'))

# QQ 邮箱 SMTP
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login('1634064164@qq.com', '授权码')
server.send_message(msg)
server.quit()
```

## 注意事项

- 授权码 ≠ 登录密码，必须在 QQ 邮箱设置中单独生成
- IMAP 授权码和 SMTP 授权码相同
- 每天发信上限约 100 封（QQ 邮箱限制）
- 搜索是服务器端匹配，支持 AND/OR/NOT 操作符
