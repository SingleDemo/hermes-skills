---
name: minimax-mcp
description: MiniMax 官方 MCP (minimax-mcp-js) 安装与 Hermes 配置，含 API_HOST/模型版本/歌词必填等坑点
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

### 2. 音乐生成模型版本
```javascript
// 默认模型是 music-1.5，但实际应查官方文档
// 文档写的是 music-2.6，但 MCP JS SDK 默认用 music-1.5
// 需确认当前最新可用版本
```

### 3. music_generation 歌词必填
```javascript
// ❌ 旧版可传空 lyrics，但 music-2.6 要求 lyrics 必须有内容
// 必须提供完整歌词或至少结构标签如 [Verse][Chorus]
```

### 4. 歌词结构标签
```
支持: [Intro][Verse][Chorus][Bridge][Outro]
每行用 \n 分隔
```

## Hermes config.yaml 配置示例

```yaml
mcp_servers:
  minimax:
    command: ~/.local/bin/minimax-mcp-js
    env:
      MINIMAX_API_KEY: sk-api-xxx           # MiniMax API Key（sk-api- 开头）
      MINIMAX_API_HOST: https://api.minimaxi.com
      MINIMAX_MCP_BASE_PATH: /home/agentuser/minimax-output  # 输出目录
    timeout: 300
    connect_timeout: 60
```

## 工具清单（minimax-mcp-js 0.0.17）

| 工具 | 说明 | 必填参数 |
|------|------|----------|
| `music_generation` | 音乐生成 | prompt, lyrics |
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

## 官方资源

- GitHub: https://github.com/MiniMax-AI/MiniMax-MCP-JS
- npm: `minimax-mcp-js`
- 文档: https://platform.minimaxi.com/docs/guides/mcp-guide.md
