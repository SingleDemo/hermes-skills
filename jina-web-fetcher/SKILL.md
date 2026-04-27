---
name: jina-web-fetcher
description: 使用 Jina AI 抓取网页内容，绕过搜索引擎限制。支持任意URL，支持 Google 搜索结果抓取。
---

# Jina Web Fetcher

使用 Jina AI 服务抓取网页内容。

## 安装
无需安装，直接使用 curl。

## 使用
```bash
# 抓取任意网页
curl -s "https://r.jina.ai/http://目标URL"

# 抓取 Google 搜索结果
curl -s "https://r.jina.ai/http://www.google.com/search?q=搜索词"
```

## 示例
```bash
# 抓取 GitHub Trending
curl -s "https://r.jina.ai/http://github.com/trending"

# 抓取 Hacker News
curl -s "https://r.jina.ai/http://news.ycombinator.com"

# 抓取特定文章
curl -s "https://r.jina.ai/http://example.com/article"
```

## 注意
- Google 被封锁时使用 r.jina.ai 仍可能被拦截
- 大部分网站都可以正常抓取

## ⚠️ 性能陷阱（经验总结）

**实测速度排行**（对 platform.minimaxi.com 测试）：

| 方式 | 耗时 | 结果 |
|------|------|------|
| `curl` 直接请求 | **~5s** | ✅ 最快 |
| `mcp_fetch_fetch` | ~4-5s+协议开销 | 中等 |
| jina (r.jina.ai) | **~15s**（超时） | ❌ 最慢 |

**结论**：jina 对被墙站点反而更慢，因为它绕路了。不要默认用 jina，正确的降级顺序是：

```
curl 直接 → mcp_fetch_fetch → jina → agent-browser
```

**何时用 jina**：
- Google 搜索结果抓取
- 直接 curl 和 mcp_fetch 都失败的站点
- 被直接屏蔽但 jina 绕得过的场景
