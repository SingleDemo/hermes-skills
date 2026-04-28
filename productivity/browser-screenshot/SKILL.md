---
name: browser-screenshot
description: 浏览器截图工具对比与最佳实践。2026-04-28 测试结论：npx playwright screenshot 最可靠，browser-use CLI 在容器环境有 daemon 超时问题。
---

# Browser Screenshot 工具对比

## 测试环境
- 容器环境，Playwright Chromium 已缓存于 `~/.cache/ms-playwright`
- `browser-use` CLI 装好但 daemon socket 通讯超时
- `agent-browser` open 命令因沙箱限制失败

## 推荐方案：npx playwright

### 截图（一屏）
```bash
npx playwright screenshot "https://example.com" /tmp/screenshot.png
```

### 截图 + 滚动翻页（Node.js 脚本）
```bash
PLAYWRIGHT_BROWSERS_PATH=$HOME/.cache/ms-playwright node -e "
const { chromium } = require('/tmp/pw/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('https://example.com', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/tmp/p1.png', fullPage: false });
  
  await page.evaluate(() => window.scrollBy(0, 900));
  await page.waitForTimeout(800);
  await page.screenshot({ path: '/tmp/p2.png', fullPage: false });
  console.log('Done');
  await browser.close();
})().catch(e => { console.error('ERR:', e.message); process.exit(1); });
"
```

注意：Playwright Node 模块默认不在路径里，需先安装：
```bash
npm install playwright --prefix /tmp/pw
```
浏览器二进制已缓存在 `~/.cache/ms-playwright`，设置 `PLAYWRIGHT_BROWSERS_PATH` 复用。

## 其他工具结论

| 工具 | 状态 | 备注 |
|------|------|------|
| npx playwright screenshot | ✅ 推荐 | 一条命令，无需安装 |
| browser-use | ❌ daemon 超时 | skill 代码装好，CLI 跑不起来 |
| agent-browser open | ❌ 沙箱失败 | 截图功能不可用 |
| playwright Node 脚本 | ✅ | 滚动翻页必备 |

## browser-use 备查
- CLI 安装：`uvx browser-use` 或 `uv run --with browser-use browser-use`
- 需要 daemon 进程保持运行（socket 通讯）
- 容器环境 socket 超时，暂时不可用
- `--cdp-url http://127.0.0.1:9222` 可连已有 Chromium（未验证成功）
