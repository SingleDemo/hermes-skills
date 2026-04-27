#!/usr/bin/env bash
# Usage: log-pending.sh <summary> [detail]
# Example: log-pending.sh "修复了 WeChat 重连慢的问题" "在 weixin-reconnect skill 里加了 direct reconnect 步骤"
# Example: log-pending.sh "GitHub OAuth 超时改用 PAT" "browser login 一直超时，改用 gh auth login --with-token"

set -euo pipefail

PENDING_DIR="$HOME/self-improving/pending"
mkdir -p "$PENDING_DIR"

summary="${1:-}"
detail="${2:-}"

if [[ -z "$summary" ]]; then
  echo "Usage: log-pending.sh <summary> [detail]"
  exit 1
fi

timestamp=$(date '+%Y-%m-%d %H:%M:%S')
safe_name=$(echo "$summary" | tr -cd '[:alnum:] _-' | tr ' ' '-' | head -c 60)
entry_file="$PENDING_DIR/$(date '+%Y%m%d-%H%M%S')-${safe_name}.md"

cat > "$entry_file" <<EOF
---
timestamp: $timestamp
summary: $summary
status: pending
---

$detail
EOF

echo "✓ 记录已保存: $entry_file"
echo ""
cat "$entry_file"
