---
name: skillhub-scrape
description: SkillHub (skillhub.cn) 数据抓取方法 — API 和浏览器翻页两种方式
triggers:
  - "skillhub 抓取"
  - "skillhub 翻页"
  - "skillhub 截图"
  - "skillhub skills list"
---

# SkillHub Scrape

SkillHub (skillhub.cn / skillhub.website) 数据抓取方法。

## 环境判断

- `agent-browser open` 失败 → 沙箱问题
- `npx playwright` + `/tmp/pw/node_modules/playwright` → 可用（自带 Chromium）
- `browser-use` CLI → 不兼容（daemon socket 架构，服务器环境天然超时）

## API 抓取（推荐，快）

```python
import urllib.request, json

url = "https://api.skillhub.cn/api/skills?page=1&pageSize=100&sortBy=downloads&order=desc"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Referer': 'https://www.skillhub.cn/'
})
resp = urllib.request.urlopen(req, timeout=15)
data = json.loads(resp.read())
# total=34867, skills在 data['data']['skills']
```

注意：默认 pageSize=20，必须显式传 pageSize=100 才批量返回。

## 浏览器翻页抓文字（当 API 不足时）

页面是 SPA，`window.scrollTo` 对其无效，必须操作内部滚动容器：

```javascript
// 找滚动容器（特征：class 含 "overflow-auto"，scrollHeight > clientHeight）
const container = await page.$('.overflow-auto');
const scrollHeight = await container.evaluate(el => el.scrollHeight);
const clientHeight = await container.evaluate(el => el.clientHeight);
const maxScroll = scrollHeight - clientHeight;

// 分步滚动截图/提取
const steps = 4;
for (let i = 0; i <= steps; i++) {
  const scrollTop = Math.round((i / steps) * maxScroll);
  await container.evaluate((el, top) => { el.scrollTop = top; }, scrollTop);
  await page.waitForTimeout(2000);
  const text = await page.evaluate(() => document.body.innerText);
  // 处理 text...
}
```

## 页面数据格式

页面显示两个数字：**安装数**（如 "2.9 千"）+ **下载数**（如 "52.9 万"）
API 字段：`installs`（安装数）和 `downloads`（下载数）

## 完整抓取 >1K 安装技能

```python
import urllib.request, json

all_skills = []
page = 1
while True:
    url = f'https://api.skillhub.cn/api/skills?page={page}&pageSize=100&sortBy=downloads&order=desc'
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'})
    data = json.loads(urllib.request.urlopen(req, timeout=15).read())
    skills = data['data']['skills']
    if not skills or skills[-1]['installs'] < 1000:
        break
    all_skills.extend(skills)
    page += 1
# 约 700 条，installs >= 1K
```

## 分类页面

`https://www.skillhub.cn/skills?category=developer-tools` 等，但每个分类只返回该分类内评分最高的 20 条，无法按下载量排序遍历全部分类。
