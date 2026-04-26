---
name: hermes-gateway-debug
description: Hermes Gateway 连接状态排查。Gateway 报 disconnected、微信/元宝无响应时使用。
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, gateway, debugging, weixin, yuanbao]
    related_skills: [messenger-api-format-troubleshooting, weixin-reconnect]
---

# Hermes Gateway 连接状态排查

## 排查步骤

### 1. 查状态
```bash
cat ~/.hermes/gateway_state.json
```
看 `platforms.weixin.state` / `platforms.yuanbao.state`，connected 或 disconnected

### 2. 查日志
```bash
tail -100 ~/.hermes/logs/agent.log | grep -i "weixin\|gateway\|error\|expired"
```
关键错误：
- `Session expired` → ilink session 过期，需重新扫码
- `unknown config keys ignored` → 配置格式错误（嵌套、字段名不支持）
- `choices` → API 返回格式问题（见 messenger-api-format-troubleshooting）

### 3. 查 .env（微信）
检查 WEIXIN_ACCOUNT_ID 是否唯一（多余的旧账号行会导致旧账号覆盖新账号）。扫码链接：`https://ilinkai.weixin.qq.com/ilink/bot/get_bot_qrcode?bot_type=3`

### 4. 重启后等待
Gateway 重连后约30秒才变 connected，等60秒再查状态确认，不要重复执行重连命令。

### 5. 手动重连
用户倾向手动重连（hermes setup 慢）。Gateway 报 disconnected 时先问用户是否已在手动重连。
