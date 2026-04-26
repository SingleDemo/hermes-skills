---
name: weixin-reconnect
description: 微信重连完整流程。微信 Session expired、或账号失联时使用。
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [weixin, reconnect, ilink, qrcode]
    related_skills: [hermes-gateway-debug, messenger-api-format-troubleshooting]
---

# 微信重连流程

## 完整流程

### Step 1: 检查 .env 中的 WEIXIN_ACCOUNT_ID
确认只有一行，多余的旧账号行必须删除（最后一个会覆盖前面的）。

### Step 2: 检查 ilink session 状态
日志搜 `Session expired`：
- 有 `Session expired` → 需要重新扫码
- 无 → session 仍有效，可直接重启 gateway

### Step 3: 重新扫码（session 过期时）
微信扫码链接：
```
https://ilinkai.weixin.qq.com/ilink/bot/get_bot_qrcode?bot_type=3
```
扫码后拿到 ilink_token 和 ilink_device_id，更新到 .env。

### Step 4: 重启 gateway
```bash
hermes gateway restart
```

### Step 5: 等待连接建立
约30秒后 connected，等60秒确认状态，不要重复执行重启。
