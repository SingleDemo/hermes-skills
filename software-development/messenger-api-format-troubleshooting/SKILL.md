---
name: messenger-api-format-troubleshooting
description: 排查微信/元宝等 messenger 平台无法对话的问题，根因是 iLink 会话过期或 AI provider 返回格式不兼容
---

# Messenger API 格式兼容性排查

## 问题症状
微信/元宝等 messenger 平台无法对话，错误信息：
- `Invalid API response: response has no 'choices' attribute` — API 返回格式不兼容
- `Session expired` (errcode -14) — iLink 会话过期，需要重新扫码登录

## Session expired 修复（errcode=-14）
微信登录 Session 过期后，gateway 会不断重连但报 `Session expired`。标准 `hermes gateway setup` 交互式命令无法通过管道输入，选择平台后行为异常。

**正确方法：直接调用 qr_login 函数**：
```python
python3 -c "
import asyncio, sys
sys.path.insert(0, '/home/agentuser/.hermes/hermes-agent')
from gateway.platforms.weixin import qr_login
asyncio.run(qr_login('/home/agentuser/.hermes'))
"
```
这会直接生成二维码并等待微信扫码确认（480秒超时）。扫码后会输出新 token 并自动保存到账号文件。

## 根因
不同 AI provider 返回的响应格式不同：

| Provider | 响应格式 | 是否有 `choices` 字段 |
|----------|----------|------------------------|
| `minimax-cn` (MiniMax 官方) | OpenAI 格式 | ✅ 有 |
| `mnapi` | OpenAI 格式 | ✅ 有 |
| `ruoli-*` | OpenAI 格式 | ✅ 有 |
| `nvidia-*` | OpenAI 格式 | ✅ 有 |

Messenger 平台（微信/元宝）走的是 `api_mode = "openai"` 代码路径，该路径校验 `choices` 字段的存在。如果 provider 返回 Anthropic 格式（无 `choices`），就会报错。

**关键判断**：实际测试证明 minimax-cn 返回标准 OpenAI 格式（有 `choices` 字段），与 mnapi/nvidia 等兼容。

## 修复步骤

1. **检查当前 provider 的响应格式**（用 curl 测试）：
   ```bash
   curl -s -X POST https://www.mnapi.com/v1/chat/completions \
     -H "Authorization: Bearer $API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model":"gpt-5.4","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
   ```
   看返回是否有 `choices` 字段。

2. **修改 config.yaml**（使用 MiniMax 官方 provider）：
   ```yaml
   model:
     default: MiniMax-M2.7        # 注意：官方模型名是 MiniMax-M2.7，不是 minimax-m2.7
     provider: minimax-cn
     base_url: https://api.minimaxi.com/v1
   ```
   minimax-cn 会自动从环境变量 `MINIMAX_CN_API_KEY` 读取 API key。

3. **验证**：重启 agent 后测试 messenger 是否正常。

## 关键代码位置
- 错误触发点：`run_agent.py:9358` — 检查 `hasattr(response, 'choices')`
- API 格式判断：`providers.py:418-465` — `determine_api_mode` 函数根据 base_url 路径判断
- Messenger 平台判断：走 OpenAI 格式路径但某些 provider 返回 Anthropic 格式

## 预防
配置 messenger 平台时，确保使用的 provider 返回标准 OpenAI JSON 格式（有 `choices` 字段）。minimax-cn/mnapi/nvidia/ruoli 均支持。
