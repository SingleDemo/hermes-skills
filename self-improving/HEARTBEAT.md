## Self-Improving Check

- Read `./skills/self-improving/heartbeat-rules.md`
- Use `~/self-improving/heartbeat-state.md` for last-run markers and action notes
- If no file inside `~/self-improving/` changed since the last reviewed change, return `HEARTBEAT_OK`
- **Pending inbox**: `~/self-improving/pending/` — records go here via `log-pending.sh`
- **Heartbeat script**: `~/self-improving/scripts/heartbeat.sh` — processes pending/ and updates index
