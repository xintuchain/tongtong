# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Telegram Bot 配置（2026-04-13）

| Bot | Token 环境变量 | Bot 链接 |
|-----|----------------|----------|
| 桐桐 (longaidtt_bot) | `TELEGRAM_BOT_TOKEN` | https://t.me/longaidtt_bot |

**Token 存储**：`~/.zshrc` / `~/.bash_profile` 中的环境变量 `TELEGRAM_BOT_TOKEN`
**openclaw.json 引用**：`${TELEGRAM_BOT_TOKEN}`

---

## 飞书 Bot 配置（2026-04-06）

| 成员 | App ID | App Secret |
|------|--------|------------|
| 慧研 | cli_a958455093789cc0 | FEISHU_SECRET_REMOVED |
| 慧选 | cli_a95843bab1b8dcef | FEISHU_SECRET_REMOVED |
| 慧联 | cli_a95841ae2db85cc3 | FEISHU_SECRET_REMOVED |
| 慧维 | cli_a959bd4d19341cb5 | FEISHU_SECRET_REMOVED |

## Discord Bot 配置

| Bot | Bot ID | Token |
|-----|--------|-------|
| 桐桐 | 1487389807150759997 | DISCORD_TOKEN_REMOVED |
| 慧研 | 1487400110550945925 | DISCORD_TOKEN_REMOVED |
| 慧选 | 1487401590037024840 | DISCORD_TOKEN_REMOVED |
| 慧联 | 1487403119393636474 | DISCORD_TOKEN_REMOVED |

## 飞书群信息

| 项目 | 值 |
|------|-----|
| 群聊 chat_id | oc_b3954ab01295369c556f15e659c8e3e4 |
| 用户 Fei open_id | ou_8b2762538fb2b0e93b5fa4bdf311c999 |
| 桐桐 bot open_id | ou_5f288229c4eb1146a7e4e937bd3d48f4 |

## Discord 频道配置（重要！）

> ⚠️ 频道 ID 不能搞混！Discord channel ID ≠ Discord guild/server ID。
> Bot 必须被 invited 到正确的频道才能读写消息。

| Bot | 频道 ID | 用途 | 备注 |
|-----|---------|------|------|
| 桐桐 | `1489414235032125581` | 主控汇报 | ❌ 旧的 `1487386985852178617` 已废弃 |
| 慧研 | `1489414235661533336` | 慧研专属 | |
| 慧选 | `1489414235279589508` | 慧选专属 | |
| 慧联 | `1489414234939854859` | 慧联专属 | |
| 慧维 | `1489414235481051338` | 慧维专属 | |

**教训**：建立任何 channel 后，立即记录 channel ID 到此处，不要写在 cron job 消息里。

---

## Discord 发送规则（2026-04-08 更新）

**必须指定 accountId**：`accountId: tongtong`，不能依赖 defaultAccount。
不带 accountId 会导致 401 Unauthorized。

**成功发送示例**：
```json
{
  "action": "send",
  "accountId": "tongtong",
  "target": "1489414235032125581",
  "message": "..."
}
```

---

Add whatever helps you do your job. This is your cheat sheet.
