---
name: minimax-mcp
description: MiniMax Token Plan 完整指南（mmx-cli 替代 minimax-mcp-js）：sk-cp- token、mmx-cli 安装、music-2.6 配额、视频无配额等坑点
---

# MiniMax MCP 配置

## 安装 minimax-mcp-js

```bash
npm install -g minimax-mcp-js --prefix ~/.local
```

## 关键配置（踩坑经验）

### 1. API_HOST 必须是中国的
```yaml
env:
  MINIMAX_API_HOST: https://api.minimaxi.com   # ❌ 不是 api.minimax.chat（国际版）
```

### 2. minimax 必须嵌套在 mcp_servers 下（缩进踩坑）
```yaml
# ❌ 错误：minimax 在根级，不在 mcp_servers 下，Hermes 不会加载
mcp_servers:
  cloudbase: ...
minimax:    # ← 根级，Hermes 不认
  command: ...

# ✅ 正确：minimax 是 mcp_servers 的子键
mcp_servers:
  cloudbase: ...
  minimax:   # ← 两个空格缩进嵌套
    command: ...
```

### 3. music_generation 歌词必填
```javascript
// ❌ music-2.6 要求 lyrics 必须有内容，不能省略
// 必须提供完整歌词或至少结构标签如 [Verse][Chorus]
```

### 4. 歌词结构标签
```
支持: [Intro][Verse][Chorus][Bridge][Outro]
每行用 \n 分隔
```

### 5. 音乐模型版本（MCP SDK 无法指定 music-2.6）

SDK 源码 `build/const/index.js` 硬编码：
```javascript
export const DEFAULT_MUSIC_MODEL = 'music-1.5';
```
`build/api/music.js` 的 `generateMusic()` 直接用 `DEFAULT_MUSIC_MODEL`，**不读任何环境变量**，无法通过 `MINIMAX_MUSIC_MODEL` 覆盖。

**结论**：MCP SDK 只能生成 music-1.5，不支持 music-2.6。

### 6. 音乐生成正确方案：用 mmx-cli（推荐）

MCP 不支持 music-2.6，用 MiniMax 官方 CLI 代替：

```bash
# 安装
npm install -g mmx-cli --prefix ~/.local

# 登录（sk-cp- 音乐 token）
mmx auth login --api-key sk-cp-V0Xs9Yy1Vk4QvDbR6j-A_eH-ZhWdkTtvo6V5SHX_R_fGn25FyRe5zxgeXbtxJxj-4gK7Rb-9gOc6kXTY0Rj1_PZKe761AYe8wwsTaUxkoZrigiLeVH_1HUQ

# 生成音乐（music-2.6，自动使用）
mkdir -p ~/minimax-output
mmx music generate \
  --prompt "轻快的民谣风格，吉他伴奏" \
  --lyrics "[Verse]\n歌词内容\n[Chorus]\n副歌内容" \
  --out ~/minimax-output/song.mp3
```

**mmx-cli 配额示例**（Token Plan 每周）：
- music-2.6: 100 首/周
- speech-hd: 4000 次/周
- image-01: 50 张/周

## Hermes config.yaml 配置示例（仅语音/TTS 用途）

```yaml
mcp_servers:
  cloudbase:
    command: cloudbase-mcp
    timeout: 180
    connect_timeout: 60
  minimax:
    command: ~/.local/bin/minimax-mcp-js
    env:
      MINIMAX_API_KEY: sk-api-xxx           # 注意：sk-api- 开头（非音乐 token）
      MINIMAX_API_HOST: https://api.minimaxi.com
      MINIMAX_MCP_BASE_PATH: /home/agentuser/minimax-output
    timeout: 300
    connect_timeout: 60
```

> 注意：MCP 只能用 sk-api- token（普通 API），不支持 sk-cp- 音乐 token。

## 工具清单（minimax-mcp-js 0.0.17）

| 工具 | 说明 | 必填参数 |
|------|------|----------|
| `music_generation` | 音乐生成（只能用 music-1.5） | prompt, lyrics |
| `text_to_audio` | 语音合成 | text, voice_id |
| `text_to_image` | 图片生成 | prompt |
| `generate_video` | 视频生成 | prompt 或 first_frame_image |
| `voice_clone` | 音色克隆 | voice_id, file |
| `voice_design` | 音色设计 | prompt, preview_text |
| `list_voices` | 查询音色列表 | - |
| `play_audio` | 播放音频 | input_file_path |

## 坑点汇总

1. **API_HOST 错误**：`api.minimax.chat` 是国际版，中国区要用 `api.minimaxi.com`
2. **歌词为空**：music-2.6 强制要求 lyrics，不能省略
3. **环境变量优先级**：CLI 参数 > 环境变量 > 配置文件
4. **输出路径**：需预先创建目录，否则 MCP 启动失败

## 重要结论：MCP 已被放弃，mmx-cli 是正确方案

**minimax-mcp-js 的根本缺陷（无法绕过）**：
- `music_generation` 硬编码 `DEFAULT_MUSIC_MODEL = 'music-1.5'`
- `MINIMAX_MUSIC_MODEL` 环境变量在 SDK 中**未被使用**，设置无效
- 即使用户有 `music-2.6` 配额，MCP 始终请求 `music-1.5`，导致 API Error

**解决方案：mmx-cli（推荐）**
- npm 包名：`mmx-cli`（不是 minimax-cli）
- 安装：`npm install -g mmx-cli --prefix ~/.local`
- 登录：`mmx auth login --api-key sk-cp-xxx`（用 sk-cp- 前缀的音乐 token）
- 可用模型自动识别，无需手动指定
- 支持：text、image、music、video、speech

**token 类型区别**：
- `sk-api-` 前缀：API 调用（文本/图像等），MCP 用这个
- `sk-cp-` 前缀：**Token Plan 专属**，音乐/视频/语音权益，只能通过 mmx-cli 使用
- 两者不可混用，sk-cp- token 无法用于 MCP

**mmx-cli 常用命令**：
```bash
mmx auth login --api-key sk-cp-xxx          # 登录
mmx music generate --prompt "..." --lyrics "..." --out file.mp3   # 音乐
mmx image "prompt" --out file.png           # 图片
mmx speech synthesize --text "..." --out file.mp3  # 语音
mmx text chat --message "..."               # 文本对话
```
5. **Token 类型**：MCP 用 sk-api-，音乐用 mmx-cli + sk-cp-

## 官方资源

- mmx-cli GitHub: https://github.com/MiniMax-AI/cli
- mmx-cli npm: `mmx-cli`
- minimax-mcp-js GitHub: https://github.com/MiniMax-AI/MiniMax-MCP-JS
- minimax-mcp-js npm: `minimax-mcp-js`
- 文档: https://platform.minimaxi.com/docs/token-plan/minimax-cli
