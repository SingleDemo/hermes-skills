---
name: github-proxy-workaround
description: Use gh-proxy.com to download GitHub release binaries and repo archives when direct GitHub access is slow or blocked in CLI environments.
category: devops
---

# GitHub Proxy Workaround

## Problem
GitHub direct access is extremely slow or times out in certain CLI environments. `gh api` works but release binary downloads and git clone are very slow or fail.

## Solution
Use `gh-proxy.com` as an HTTP proxy intermediary for downloading GitHub release files and repo archives.

## Usage

### Download a release binary
```bash
curl -L --max-time 90 -o output.bin \
  "https://gh-proxy.com/https://github.com/OWNER/REPO/releases/download/TAG/filename"
```

### Download a repo as zip
```bash
curl -L --max-time 60 -o repo.zip \
  "https://gh-proxy.com/https://github.com/OWNER/REPO/archive/refs/heads/BRANCH.zip"
```

## Important Notes
- `gh-proxy.com` is an **HTTP proxy** (not SOCKS). Use with `curl -x http://gh-proxy.com`
- Does NOT support CONNECT tunneling for non-HTTP protocols
- `gh release download` does NOT use system proxy — use curl directly instead
- GitHub API (`gh api`) works fine without proxy — only use proxy for large binary downloads

## Environment Verification
```bash
curl -L --max-time 10 -o /dev/null \
  "https://gh-proxy.com/https://github.com/MetaCubeX/mihomo/releases/download/v1.19.24/mihomo-linux-amd64-v3-v1.19.24.gz" \
  -w "%{http_code} %{speed_download}"
# Expected: HTTP 200, speed > 500KB/s (vs. ~2KB/s direct)
```

## Speed Comparison (this environment)
| Method | Speed |
|--------|-------|
| Direct GitHub | ~2-50 KB/s (often times out) |
| `gh api` | Works fine |
| `gh-proxy.com` + curl | 500KB - 2MB/s |

## Why Not mihomo as Proxy?
The original goal was to set up mihomo (clash-meta) as a local proxy to access GitHub. However:
1. mihomo binary itself needs downloading from GitHub (circular dependency)
2. The ClashVerge subscription contained hysteria2 nodes that were all dead (server reachable, protocol not responding)
3. hysteria2 nodes use `anytls://` protocol — not standard HTTP/SOCKS, so curl can't test them directly

## When This Works
- Downloading release binaries (.gz, .zip, .deb, etc.)
- Downloading repo archives (.zip via archive URLs)
- Any HTTP GET requests to github.com URLs

## When This Doesn't Work
- git clone (needs SOCKS5 or git's native HTTP backend)
- Interactive gh operations (gh repo clone, gh pr checkout, etc.)
- WebSocket-based operations
