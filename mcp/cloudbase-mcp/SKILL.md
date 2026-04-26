---
name: cloudbase-mcp
description: Tencent CloudBase MCP Server — full-stack cloud development including NoSQL/SQL databases, cloud functions, CloudRun, static hosting, storage, auth, gateway, permissions, logs, and AI model integration. Use when developing with CloudBase (腾讯云开发), deploying serverless apps, managing cloud databases, or building AI-augmented applications on Tencent Cloud.
version: 1.0.0
author: Tencent CloudBase
license: MIT
metadata:
  hermes:
    tags: [cloudbase, tencent, mcp, serverless, cloud-functions, database]
    mcp_server: cloudbase
related_skills: [native-mcp]
---

# CloudBase MCP Server

腾讯云开发 MCP Server，通过 AI 提示词和 MCP 协议 + 云开发，让开发更智能、更高效。

## Tool Naming

All tools are available as `mcp_cloudbase_*` (prefix `mcp_cloudbase_` + tool name).

## Quick Start

### 1. Login

```json
{
  "action": "start_auth",
  "authMode": "device"
}
```

Or use CLI: `cloudbase login`

### 2. Bind Environment

```json
{
  "action": "set_env",
  "envId": "your-env-id"
}
```

### 3. Query Environments

```json
{
  "action": "list"
}
```

## Core Tool Categories

### Environment

- `mcp_cloudbase_auth` — Login/logout, get status, bind env, temp credentials
- `mcp_cloudbase_envQuery` — List/query environments, domains, hosting config
- `mcp_cloudbase_envDomainManagement` — Add/remove safe domains (CORS)

### Databases

- `mcp_cloudbase_readNoSqlDatabaseStructure` — List collections, describe, indexes
- `mcp_cloudbase_writeNoSqlDatabaseStructure` — Create/delete collections, indexes
- `mcp_cloudbase_readNoSqlDatabaseContent` — Query NoSQL data (MongoDB-like)
- `mcp_cloudbase_writeNoSqlDatabaseContent` — Insert/update/delete NoSQL records
- `mcp_cloudbase_querySqlDatabase` — Query MySQL state, run read-only SQL
- `mcp_cloudbase_manageSqlDatabase` — Provision/destroy MySQL, run write SQL/DDL
- `mcp_cloudbase_manageDataModel` — Query/create data models (Mermaid classDiagram)
- `mcp_cloudbase_queryPermissions` / `mcp_cloudbase_managePermissions` — Database/function/storage permissions

### Cloud Functions

- `mcp_cloudbase_queryFunctions` — List/detail/logs/layers/triggers
- `mcp_cloudbase_manageFunctions` — Create/update/invoke/delete functions, triggers, layers

### CloudRun

- `mcp_cloudbase_queryCloudRun` — List/detail/templates/logs
- `mcp_cloudbase_manageCloudRun` — Init/deploy/delete CloudRun services

### Storage & Hosting

- `mcp_cloudbase_queryStorageFiles` — List/query storage files
- `mcp_cloudbase_manageStorageFiles` — Upload/delete storage files
- `mcp_cloudbase_manageHosting` — Static hosting management

### Auth

- `mcp_cloudbase_queryAppAuth` — Get login config, providers, client config
- `mcp_cloudbase_manageAppAuth` — Modify login methods, providers, API keys

### Gateway & API

- `mcp_cloudbase_queryGateway` / `mcp_cloudbase_manageGateway` — Custom domains, routes
- `mcp_cloudbase_callCloudApi` — Generic Tencent Cloud API calls (tcb/scf/sts/cam/cdn/vpc)

### AI Models

- `mcp_cloudbase_queryModels` — List AI models
- `mcp_cloudbase_generateText` — Text generation (Hunyuan, DeepSeek)
- `mcp_cloudbase_streamText` — Streaming text generation
- `mcp_cloudbase_generateImage` — Image generation (Hunyuan)

### Knowledge & Docs

- `mcp_cloudbase_searchKnowledgeBase` — Vector/skill/openapi/docs search

## Common Workflows

### Deploy a Cloud Function

1. `manageFunctions(action=createFunction, func={name, runtime, handler, ...})`
2. `manageFunctions(action=invokeFunction, func={name})`

### Deploy a CloudRun Service

1. `manageCloudRun(action=init, serverName, targetPath)` — from template
2. `manageCloudRun(action=deploy, serverName, targetPath, serverConfig)`

### Manage NoSQL Data

1. `readNoSqlDatabaseStructure(action=listCollections)` — find collection
2. `readNoSqlDatabaseContent(collectionName, query, limit)` — read
3. `writeNoSqlDatabaseContent(action=insert/update/delete, ...)` — write

### Database Permissions

```json
{
  "action": "updateResourcePermission",
  "resourceType": "noSqlDatabase",
  "resourceId": "collection-name",
  "permission": "CUSTOM",
  "securityRule": "{\"read\":\"auth.uid != null\",\"create\":\"auth.uid != null\"}"
}
```

## CLI Commands (cloudbase)

```bash
cloudbase login              # Login
cloudbase env list           # List environments
cloudbase fn list            # List functions
cloudbase fn deploy <name>   # Deploy function
cloudbase hosting deploy     # Deploy static hosting
cloudbase db query           # Query database
cloudbase ai                 # AI full-stack development
```

## Troubleshooting

- **Not logged in**: Use `cloudbase login` or `auth(action=start_auth)`
- **Wrong env**: Use `auth(action=set_env, envId="...")` to switch
- **CORS errors**: Add domain via `envDomainManagement(action=create, domains=[...])`
- **Permission denied**: Check `queryPermissions` and `managePermissions`

## Config

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  cloudbase:
    command: cloudbase-mcp
    timeout: 180
    connect_timeout: 60
```

Installed at: `~/.local/bin/cloudbase` and `~/.local/bin/cloudbase-mcp`