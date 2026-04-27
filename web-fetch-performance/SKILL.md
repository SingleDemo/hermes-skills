---
name: web-fetch-performance
description: 网页抓取速度排行与降级策略，优先用最快的方式，失败后自动降级
---

# Web Fetch Performance

## 实测速度排行（越快越优先）

| 排名 | 方式 | 命令/工具 | 典型耗时 | 适用场景 |
|------|------|-----------|----------|----------|
| 1 | `curl` 直接 | `curl -s --max-time 15 "URL"` | **~5s** | 普通网页，被墙站点 |
| 2 | `mcp_fetch_fetch` | MCP 协议调用 | ~4-5s+ | MCP 生态内，已连接的 MCP 服务器 |
| 3 | `jina-web-fetcher` | `curl -s "https://r.jina.ai/http://URL"` | **~15s**（绕路，慎用） | 搜索引擎结果页、被直接屏蔽的站点 |

> **注意**：jina 对被墙站点反而更慢，因为绕路了。除非直接 curl 和 mcp_fetch 都失败再试 jina。

## 降级策略（依次尝试）

```
curl 直接 → mcp_fetch_fetch → jina → agent-browser(无头浏览器)
```

1. **第一优先**：`curl -s --max-time 15 "目标URL"`
2. **第二优先**：`mcp_fetch_fetch(url="目标URL")` — MCP 已连接时
3. **第三优先**：`curl -s --max-time 15 "https://r.jina.ai/http://目标URL"`
4. **最后手段**：`agent-browser` 无头浏览器截图/抓取

## 触发条件

- 用户说"抓取网页"、"获取页面内容"、"上网查"等
- 需要获取任意 URL 的内容时
- 先查此技能，按排行依次尝试

## 已验证站点

| 站点 | curl 直接 | jina | mcp_fetch |
|------|-----------|------|-----------|
| platform.minimaxi.com | ✅ ~5s | ❌ 超时 | 未测 |
| github.com | ✅ ~3s | 未测 | 未测 |
| news.ycombinator.com | 未测 | ✅ 正常 | 未测 |

## 注意事项

- Google 搜索结果页：用 jina（`https://r.jina.ai/http://www.google.com/search?q=xxx`）
- 被墙的国内站点：直接 curl 通常最快
- HTTPS/CDN 加速站点：curl 直接最优
