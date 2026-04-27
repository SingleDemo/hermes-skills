---
name: web-fetch-performance
description: Web fetching speed comparison for terminal/Hermes use
---

# Web Fetching Speed Ranking

Tested on `platform.minimaxi.com` (blocked site, requires TCP over IPv4):

| Method | Speed | Notes |
|--------|-------|-------|
| `curl` direct | **5s** | Fastest for blocked/CN sites |
| `mcp_fetch_fetch` | ~4-5s+ | MCP protocol overhead adds ~4s fixed cost |
| `jina-web-fetcher` | **15s+** | Slowest — bad for blocked sites, adds extra latency |

## Recommendation

1. **First try**: `curl -s --max-time 15 "URL"` — fastest for most sites
2. **If blocked**: `curl -s --max-time 15 -4 "URL"` (force IPv4) or use browser tools
3. **mcp_fetch_fetch**: Only use if site requires MCP protocol or curl fails
4. **jina-web-fetcher**: Skip — slower than curl for blocked sites

## CN Sites (TCP blocked)
Many Chinese sites (minimaxi, etc.) require IPv4. If curl times out:
```bash
curl -4s --max-time 15 "URL"
```
