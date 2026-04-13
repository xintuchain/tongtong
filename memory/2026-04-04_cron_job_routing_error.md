# 故障记录：Cron Job 会话路由错误

## 故障现象
- 慧选的每日市场任务被发送到了桐桐的主会话
- 任务消息明确说"你是慧选"，但接收者是桐桐
- 类似问题影响所有团队成员（慧研、慧选、慧联）

## 发生时间
- 2026-04-04 09:05 (Australia/Brisbane)

## 原因分析
1. Cron job 配置为 `sessionTarget: "isolated"`
2. 但没有指定对应的 `agentId` 或持久会话
3. Isolated 会话是临时的，不与特定团队成员绑定
4. 结果：任务被发送到错误的接收者

## 影响范围
- 慧研每日研究任务
- 慧选每日市场任务
- 慧联每日传播任务
- 所有头像任务提醒

## 解决方案

### 方案 A：为每个成员创建独立会话（推荐）
创建持久的子代理会话：
- `agent:huixuan:main` - 慧选专属会话
- `agent:huiyan:main` - 慧研专属会话
- `agent:huilian:main` - 慧联专属会话

修改 cron job，将 `sessionTarget` 改为对应会话的 `sessionKey`

### 方案 B：通过 Discord 路由
保持 `sessionTarget: "isolated"`，但修改任务内容：
- 任务发送到桐桐
- 桐桐识别任务类型后，转发给对应成员
- 成员通过 Discord 回复

### 方案 C：使用 Main Session 处理
将所有任务改为 `sessionTarget: "main"`
- 桐桐在主会话接收所有任务
- 桐桐代为执行或分配给子代理

## 当前处理
本次任务由桐桐代为执行，并记录此故障。

## 预防措施
1. 建立团队成员的持久会话
2. 更新 cron job 配置
3. 添加会话路由验证机制
4. 定期检查任务是否正确路由

## 相关文件
- Cron job ID: `huixuan-daily-market`
- 会话 Key: `agent:main:cron:huixuan-daily-market`
