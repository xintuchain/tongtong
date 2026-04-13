# 🔐 Discord Bot 权限配置

## 权限对比表

| 权限 | 桐桐 | 慧研 | 慧选 | 慧联 | 说明 |
|------|------|------|------|------|------|
| **View Channels** | ✅ | ✅ | ✅ | ✅ | 必需 - 看到频道 |
| **Send Messages** | ✅ | ✅ | ✅ | ✅ | 必需 - 发送消息 |
| **Read Message History** | ✅ | ✅ | ✅ | ✅ | 必需 - 读取历史 |
| **Embed Links** | ✅ | ✅ | ✅ | ✅ | 推荐 - 发送嵌入 |
| **Attach Files** | ✅ | ✅ | ✅ | ✅ | 推荐 - 上传文件 |
| **Add Reactions** | ✅ | ✅ | ✅ | ✅ | 可选 - 添加反应 |
| **Manage Messages** | ❌ | ❌ | ❌ | ❌ | 不需要 |
| **Manage Channels** | ❌ | ❌ | ❌ | ❌ | 不需要 |
| **Kick Members** | ❌ | ❌ | ❌ | ❌ | 不需要 |
| **Ban Members** | ❌ | ❌ | ❌ | ❌ | 不需要 |
| **Administrator** | ❌ | ❌ | ❌ | ❌ | 不需要 - 太危险 |

## 设置步骤

### 对每个 Bot 执行：

1. **Discord Developer Portal** → 选择 Bot
2. **OAuth2** → **URL Generator**
3. **Scopes** 选择：
   - ✅ `bot`
   - ✅ `applications.commands`

4. **Bot Permissions** 选择：
   - ✅ View Channels
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Embed Links
   - ✅ Attach Files
   - ✅ Add Reactions

5. 复制生成的 URL，在浏览器打开
6. 选择服务器，点击 **Continue**

## 关键点

- **四个 Bot 权限完全相同**
- **不需要 Administrator 权限**
- **不需要 Manage 权限**
- 只需要基本的消息和文件权限

## 为什么权限都一样

- 桐桐：主控，需要发送消息和读取历史
- 慧研：研究助理，需要发送消息和上传文件
- 慧选：技术助理，需要发送消息和上传文件
- 慧联：传播助理，需要发送消息和上传文件

**都是一样的工作流程，所以权限相同。**
