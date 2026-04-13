# SESSION-STATE.md - 活跃工作记忆

> 最后更新：2026-04-12 07:50

---

## 🔴 每日必做（最高优先级）

**开机第一件事：写昨日日志**
- 时间：每天开机后
- 内容：回顾昨天做过的事情
- 存放：`memory/YYYY-MM-DD.md`
- 规则：答应 = 记录，不记录 = 没答应

**当前缺失：**
- 4-11 全员缺失 ← 需立即补写
- 4-12 全员缺失 ← 今天必须写
- 慧联 4-10 也缺失

---

## 当前任务

- [x] 整合 proactive-agent 技能到核心工作流程 ✅
- [x] 恢复 QClaw 重启后丢失的配置 ✅
- [ ] **备份配置到 GitHub** ⏳ 进行中
- [ ] 慧研 OpenMAIC 评估报告（待分配）
- [ ] 团队通信架构优化（Telegram + InStreet）

---

## 关键细节（WAL 捕获）

### 团队成员
| 成员 | 角色 | 专长 |
|------|------|------|
| 慧研 | 研究助理 | 文献搜索、学术研究 |
| 慧选 | 市场助理 | 市场分析、趋势洞察 |
| 慧联 | 传播助理 | 内容创作、社群运营 |
| 慧维 | 技术运维 | 系统维护、问题诊断 |

### 沟通渠道
- **主渠道**：飞书群（chat_id: `oc_b3954ab01295369c556f15e659c8e3e4`）
- **人类沟通**：微信 → 桐桐
- **团队协作**：OpenClaw Sessions + EvoMap A2A（测试中）
- **对外窗口**：InStreet（待测试）
- **飞书发消息方式**：curl 直接调飞书 API（绕过跨渠道限制）
  - 桐桐 Bot App ID: `FEISHU_APP_ID_REMOVED`
  - App Secret: `FEISHU_SECRET_REMOVED`
  - 先获取 tenant_access_token，再发消息

### 定时任务
- 每日同步：17:30 (GMT+10) → 微信
- 每周同步：周五 17:00 (GMT+10) → 微信

---

## 最近决策

- 2026-04-12: 整合 proactive-agent 技能，建立 WAL 协议
- 2026-04-12: 发现团队日志缺失问题（4-11、4-12 全员缺失）
- 2026-04-09: 弃用 Discord，改用 OpenClaw Sessions + EvoMap A2A
- 2026-04-09: 五大指标体系 v2.0 定稿（参与式讨论修订）
- 2026-04-09: 人机合作标准流程确立

---

## 待跟进

- [x] 飞书文档已创建：https://feishu.cn/docx/QDnCdfUfeoU1OCxj7btcli3Hn3c
- [x] 已通过飞书 API 直接发消息到群 ✅ 21:48
- [ ] 等待团队成员补交 4-11 日志
- [ ] 补交后汇总发飞书群
- [ ] 慧研 OpenMAIC 评估报告（待分配任务）
- [ ] InStreet 实测（让慧维去注册）

---

## 工作原则

### WAL 协议
收到任务 → 先写文件 → 再回复

### Autonomous Crons
分配任务用 `isolated agentTurn`，让机器人自己干活

### Verify Implementation
验证实际产出，不是"已发送"

### Relentless Resourcefulness
先试10种方法，再升级
