#!/usr/bin/env python3
# ~/self-improving/scripts/heartbeat.sh -> heartbeat.py
# 自动化心跳脚本：检测 pending/ 并处理

import os
import re
import glob
import subprocess
from datetime import datetime

SELF = os.path.expanduser("~/self-improving")
PENDING = os.path.join(SELF, "pending")
ARCHIVE = os.path.join(SELF, "archive")
STATE = os.path.join(SELF, "heartbeat-state.md")
INDEX = os.path.join(SELF, "index.md")
MEMORY = os.path.join(SELF, "memory.md")
CORRECTIONS = os.path.join(SELF, "corrections.md")

def stamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")

def log(msg):
    print(f"[{stamp()}] {msg}")

def update_state(field, value):
    """Update a field in heartbeat-state.md"""
    if not os.path.exists(STATE):
        log(f"ERROR: {STATE} not found")
        return
    with open(STATE) as f:
        content = f.read()
    # Replace field: value
    pattern = rf'^({re.escape(field)}:).*$'
    replacement = rf'\1 {value}'
    content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    with open(STATE, 'w') as f:
        f.write(content)

def append_last_action(action):
    """Append to ## Last actions section"""
    if not os.path.exists(STATE):
        return
    with open(STATE) as f:
        content = f.read()
    marker = "## Last actions"
    if marker in content:
        # Append after existing entries
        idx = content.rindex(marker) + len(marker)
        content = content[:idx] + f"\n- {action}" + content[idx:]
    else:
        content = content.rstrip() + f"\n\n{marker}\n- {action}\n"
    with open(STATE, 'w') as f:
        f.write(content)

def file_lines(path):
    return str(sum(1 for _ in open(path))) if os.path.exists(path) else "0"

def process_entry(entry_path):
    """Process a single pending entry, return (summary, entry_type)"""
    with open(entry_path) as f:
        raw = f.read()

    parts = raw.split('---', 2)
    meta = parts[1] if len(parts) > 1 else ""
    detail = parts[2].strip() if len(parts) > 2 else ""

    summary = re.search(r'^summary:\s*(.+)$', meta, re.MULTILINE)
    summary = summary.group(1).strip() if summary else "unknown"

    ts_match = re.search(r'^timestamp:\s*(.+)$', meta, re.MULTILINE)
    timestamp = ts_match.group(1).strip() if ts_match else stamp()

    lc = summary.lower()
    if re.search(r'纠正|错误|修正|wrong|mistake|fix|bug|error', lc):
        target, etype = CORRECTIONS, "correction"
    elif re.search(r'学会|learned|新技能|新方法|技能|skill|workflow|流程', lc):
        target, etype = MEMORY, "learned"
    else:
        target, etype = MEMORY, "note"

    entry_text = f"\n## {stamp()} [{etype}] {summary}\n"
    if detail:
        entry_text += f"\n{detail}\n"

    with open(target, 'a') as f:
        f.write(entry_text)

    # Move to archive
    safe_ts = timestamp.replace(':', '-')
    archive_name = f"{safe_ts}-{os.path.basename(entry_path)}"
    os.makedirs(ARCHIVE, exist_ok=True)
    os.rename(entry_path, os.path.join(ARCHIVE, archive_name))

    return summary, etype

def main():
    log("===== self-improving heartbeat started =====")

    if not os.path.exists(STATE):
        log(f"ERROR: {STATE} not found")
        return

    now = stamp()
    update_state("last_heartbeat_started_at", now)

    processed = 0
    pending_files = glob.glob(os.path.join(PENDING, "*.md"))

    if pending_files:
        log(f"发现 {len(pending_files)} 个待处理记录")
        for entry in sorted(pending_files):
            try:
                summary, etype = process_entry(entry)
                log(f"  处理: {summary} → {etype}")
                processed += 1
            except Exception as e:
                log(f"  错误: {entry}: {e}")
    else:
        log("无待处理记录")

    # Update index
    index_content = f"""# Memory Index

## HOT
- memory.md: {file_lines(MEMORY)} lines
- corrections.md: {file_lines(CORRECTIONS)} lines

## WARM
- (no namespaces yet)

## COLD
- archive/: {len(glob.glob(os.path.join(ARCHIVE, '*')))} files

Last heartbeat: {now}
Last compaction: never
"""
    with open(INDEX, 'w') as f:
        f.write(index_content)

    # Update state
    update_state("last_reviewed_change_at", now)
    update_state("last_heartbeat_result", "HEARTBEAT_OK")
    append_last_action(f"[{now}] heartbeat: {processed} pending processed")

    log(f"===== heartbeat 完成: processed={processed} =====")

if __name__ == "__main__":
    main()
