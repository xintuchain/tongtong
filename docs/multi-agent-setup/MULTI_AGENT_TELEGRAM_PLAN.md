# 多智能体独立运营方案

**版本**: v1.1（补充 bindings 插入位置和完整配置块）
**日期**: 2026-04-26
**作者**: 慧维（系统运维专家）
**状态**: 桐桐已批准，等最终确认后执行

---

## 一、问题诊断

| 问题 | 说明 |
|------|------|
| `channels.telegram.accounts.*.agent` 字段 | ❌ schema 中不存在，为无效配置 |
| `bindings` 数组 | ❌ 当前完全缺失 |
| 5个 bot 的 DM 无法路由到对应 agent | 因为 `agent` 字段无效，bindings 缺失 |

**核心机制**: Telegram 使用 Long Polling（不需要公网访问）

---

## 二、目标

| Agent | Bot | Telegram Chat ID |
|-------|-----|-----------------|
| tongtong | @longaidtt_bot | （pairing 后分配） |
| huiyan | @longaidhy_bot | （pairing 后分配） |
| huixuan | @longaidhx_bot | （pairing 后分配） |
| huilian | @longaidhl_bot | （pairing 后分配） |
| huiwei | @longaidhw_bot | （pairing 后分配） |

---

## 三、修复配置（Step 1）

### 3.1 Bindings 插入位置

**`bindings` 是顶层字段**，与 `agents`、`channels`、`plugins` 同级。

当前 `openclaw.json` 顶层 keys：
```
agents, skills, models, tools, browser, gateway, channels, plugins, messages, session, meta
```

`bindings` 不存在，需要新增。插入位置：**在 `channels` 和 `plugins` 之间**。

### 3.2 完整配置修改

**需要两步**：

**① 删除每个 account 中的无效 `agent` 字段**

从以下 5 个 account 中移除 `"agent": "xxx"` 字段：
- `channels.telegram.accounts.tongtong`
- `channels.telegram.accounts.huiyan`
- `channels.telegram.accounts.huixuan`
- `channels.telegram.accounts.huilian`
- `channels.telegram.accounts.huiwei`

**② 在顶层新增 `bindings` 数组**

```json
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
```

### 3.3 验证命令

```bash
# Schema 验证
openclaw config schema | grep -A5 '"bindings"'

# 配置生效后查看路由
openclaw agents list --bindings
```

---

## 四、Pairing 配对（Step 2）

Gateway 重启后，向每个 bot 发 DM 触发 pairing，然后：

```bash
# 查看待配对请求
openclaw pairing list telegram

# 批准（每个 bot 一个配对码，连续批准5次）
openclaw pairing approve telegram <PAIRING_CODE_1>
openclaw pairing approve telegram <PAIRING_CODE_2>
openclaw pairing approve telegram <PAIRING_CODE_3>
openclaw pairing approve telegram <PAIRING_CODE_4>
openclaw pairing approve telegram <PAIRING_CODE_5>
```

---

## 五、执行顺序

```
[Step 0] 备份当前配置
         ↓
[Step 1] 删除无效 agent 字段 + 新增 bindings 数组
         ↓
[Step 2] 重启 gateway
         ↓
[Step 3] 验证路由: openclaw agents list --bindings
         ↓
[Step 4] 向每个 bot 发 DM，批准 5 个 pairing 请求
         ↓
[Step 5] 测试各 bot 独立运营
         ↓
[Step 6] 飞书配置（OpenClaw 升级后单独处理）
```

---

## 六、风险与缓解

| 风险 | 缓解 |
|------|------|
| 配置错误导致 gateway 启动失败 | 先用 schema 验证 |
| Pairing 码过期（1小时） | 及时操作 5 个 |
| 意外删除有效配置 | 先备份 openclaw.json |

