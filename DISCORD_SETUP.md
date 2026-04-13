# 🔧 启用 Discord Bot Presence Intent

## 问题
四个 Bot 都显示 "offline"，因为没有启用 **Presence Intent**。

## 解决步骤

### 对每个 Bot 执行以下操作：

#### 1️⃣ 桐桐 Bot
1. 打开 [Discord Developer Portal](https://discord.com/developers/applications)
2. 找到 "桐桐" 应用
3. 左侧菜单 → **Bot**
4. 向下滚动到 **Privileged Gateway Intents**
5. 启用以下三个：
   - ✅ **PRESENCE INTENT**（关键！）
   - ✅ **SERVER MEMBERS INTENT**
   - ✅ **MESSAGE CONTENT INTENT**
6. 点击 **Save Changes**

#### 2️⃣ 慧研 Bot
重复上述步骤，应用名称改为 "慧研"

#### 3️⃣ 慧选 Bot
重复上述步骤，应用名称改为 "慧选"

#### 4️⃣ 慧联 Bot
重复上述步骤，应用名称改为 "慧联"

## 启用后

1. 回到 OpenClaw，我会重启 Gateway
2. 四个 Bot 应该会在 Discord 上显示 "在线"

## 为什么需要这个

- **Presence Intent**: 让 Bot 能设置和广播在线状态
- **Server Members Intent**: 让 Bot 能看到服务器成员
- **Message Content Intent**: 让 Bot 能读取消息内容

---

**这是 Discord 的安全机制，防止 Bot 滥用权限。**
