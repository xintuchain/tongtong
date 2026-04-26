# 多智能体独立运营方案

**版本**: v1.0
**日期**: 2026-04-26
**作者**: 慧维（系统运维专家）
**状态**: 待龙飞审批后执行

---

## 一、问题诊断总结

### 1.1 当前配置状态

| 项目 | 状态 | 说明 |
|------|------|------|
| 6个 agent 定义 | ✅ 已配置 | main, tongtong, huiyan, huixuan, huilian, huiwei |
| 5个 Telegram bot tokens | ✅ 已配置 | 每个 bot 在 channels.telegram.accounts 中 |
| Telegram bot → agent 绑定 | ❌ **配置位置错误** | 用 `agent` 字段，但 schema 不支持该字段 |
| `bindings` 路由规则 | ❌ **缺失** | 根本没有配置 bindings |
| `dmPolicy: pairing` | ⚠️ 待配对 | 每个 bot 需要和对应 agent 配对 |
| 飞书插件 | ❌ **完全缺失** | plugins.entries 和 channels 里都没有 feishu |
| Gateway 绑定模式 | ⚠️ loopback | Telegram 用 Long Polling，无需公网访问 |

### 1.2 核心发现（关键！）

**Telegram 使用 Long Polling，不使用 Webhook**

- Gateway 主动轮询 Telegram 服务器获取消息
- **不需要公网访问！** 这是一个重大误解
- `bind: loopback` 对 Telegram 本身不是问题

**Telegram account schema 没有 `agent` 字段**

当前配置的 `channels.telegram.accounts.huiwei.agent = "huiwei"` 是**无效配置**，schema 根本不识别这个字段。

**正确的路由方式：通过 `bindings` 数组**

OpenClaw 官方标准路由机制：
```json
bindings: [
  {
    "type": "route",
    "agentId": "huiwei",
    "match": {
      "channel": "telegram",
      "accountId": "huiwei",
      "peer": { "kind": "direct" }
    }
  }
]
```

---

## 二、目标

每个 team member 通过自己的 Telegram bot 独立运营：

| Agent | Bot Username | 用途 |
|-------|-------------|------|
| tongtong | @longaid_bot | 桐桐（团队主管） |
| huiyan | @longaidhy_bot | 慧研（研究助理） |
| huixuan | @longaidhx_bot | 慧选（程序员助理） |
| huilian | @longaidhl_bot | 慧联（传播助理） |
| huiwei | @longaidhw_bot | 慧维（系统运维） |

---

## 三、修复方案（三步）

### 第一步：修正 Telegram bot → agent 路由（修复 bindings）

**文件**: `~/.qclaw/openclaw.json`

**操作**: 删除所有 account 中的无效 `agent` 字段，改为添加正确的 `bindings` 数组

**正确配置示例**:
```json
{
  "channels": {
    "telegram": {
      "defaultAccount": "tongtong",
      "accounts": {
        "tongtong": {
          "dmPolicy": "pairing",
          "botToken": "xxx:xxx"
        },
        "huiyan": {
          "dmPolicy": "pairing",
          "botToken": "xxx:xxx"
        },
        "huixuan": {
          "dmPolicy": "pairing",
          "botToken": "xxx:xxx"
        },
        "huilian": {
          "dmPolicy": "pairing",
          "botToken": "xxx:xxx"
        },
        "huiwei": {
          "dmPolicy": "pairing",
          "botToken": "xxx:xxx"
        }
      }
    }
  },
  "bindings": [
    {
      "type": "route",
      "agentId": "tongtong",
      "match": {
        "channel": "telegram",
        "accountId": "tongtong",
        "peer": { "kind": "direct" }
      }
    },
    {
      "type": "route",
      "agentId": "huiyan",
      "match": {
        "channel": "telegram",
        "accountId": "huiyan",
        "peer": { "kind": "direct" }
      }
    },
    {
      "type": "route",
      "agentId": "huixuan",
      "match": {
        "channel": "telegram",
        "accountId": "huixuan",
        "peer": { "kind": "direct" }
      }
    },
    {
      "type": "route",
      "agentId": "huilian",
      "match": {
        "channel": "telegram",
        "accountId": "huilian",
        "peer": { "kind": "direct" }
      }
    },
    {
      "type": "route",
      "agentId": "huiwei",
      "match": {
        "channel": "telegram",
        "accountId": "huiwei",
        "peer": { "kind": "direct" }
      }
    }
  ]
}
```

**验证命令**:
```bash
openclaw agents list --bindings
```

---

### 第二步：每个 bot 完成 pairing 配对

**前提**: 第一步配置生效 + gateway 重启

**操作**: 对每个 bot 执行配对
```bash
# 查看待配对请求
openclaw pairing list telegram

# 批准配对（每个 bot 收到 DM 后会有配对码）
openclaw pairing approve telegram <PAIRING_CODE>
```

**注意**: 需要依次向5个 bot 发送 DM，触发配对流程，然后批准每个请求。

---

### 第三步：飞书插件安装与配置（单独处理）

**问题**: 当前完全没有飞书配置（plugins.entries 和 channels 都缺失）

**飞书需要 OpenClaw 2026.4.25+**，当前版本是 2026.4.5，**需要升级 OpenClaw**。

**步骤**:
1. 升级 OpenClaw: `openclaw update`
2. 运行飞书配置向导: `openclaw channels login --channel feishu`
3. 重启 gateway
4. 配置飞书 bindings（如需多账号）

---

## 四、执行顺序

```
[Step 0] 备份当前配置
         ↓
[Step 1] 修改 bindings（Telegram 路由修正）
         ↓
[Step 2] 重启 gateway
         ↓
[Step 3] 验证路由: openclaw agents list --bindings
         ↓
[Step 4] 向每个 bot 发 DM 触发 pairing
         ↓
[Step 5] 批准 pairing 请求
         ↓
[Step 6] 测试每个 bot 的独立运营
         ↓
[Step 7] 处理飞书（升级 OpenClaw 后）
```

---

## 五、风险评估

| 步骤 | 风险 | 缓解措施 |
|------|------|----------|
| 修改 bindings | 配置错误导致 gateway 无法启动 | 先备份，schema 验证后再重启 |
| pairing | 配对码过期（1小时） | 及时操作 |
| 飞书升级 | OpenClaw 版本兼容问题 | 先在测试环境验证 |

---

## 六、验证标准

1. `openclaw agents list --bindings` 显示所有5个 bot → agent 路由
2. 向 @longaidhw_bot 发消息，慧维 bot 回复
3. 向 @longaidhy_bot 发消息，慧研 bot 回复
4. 5个 bot 完全独立，不互相干扰

---

## 七、Schema 参考（官方标准）

**bindings 正确字段**:
- `type`: "route"（路由绑定）
- `agentId`: agent ID 字符串（不是 `agent`）
- `match.channel`: "telegram"
- `match.accountId`: 账号 ID（如 "huiwei"）
- `match.peer.kind`: "direct"（不是 "dm"，"dm" 已废弃）

**dmPolicy 合法值**: "pairing" | "allowlist" | "open" | "disabled"

