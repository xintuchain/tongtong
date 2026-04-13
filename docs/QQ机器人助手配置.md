# QQ机器人助手配置

## 团队成员QQ助手列表

| 成员 | 助手名称 | QQ号 | Token |
|------|----------|------|-------|
| 🐸 桐桐 | 桐桐助手 | 1903793734 | `a9iIsS2cCmNyZAlMxZBnP1dFsV8lO1eH` |
| 🐰 慧研 | 慧研助手 | 1903794306 | `b8SZTQDn9IDxTlqh` |
| 🦊 慧选 | 慧选助手 | 1903794346 | `cAVdYFk26wZyAAwU` |
| 🐨 慧联 | 慧联助手 | 1903793579 | `eFdomW3MSL0RffR9` |
| 🐼 慧维 | 慧维助手 | 1903794370 | `Z4MQGrEMIzSjmcDe` |

## 配置命令记录

```bash
# 安装QQBot插件
openclaw plugins install @tencent-connect/openclaw-qqbot@latest

# 添加各成员助手
openclaw channels add --channel qqbot --token "1903793734:a9iIsS2cCmNyZAlMxZBnP1dFsV8lO1eH" --name tongtong
openclaw channels add --channel qqbot --token "1903794306:b8SZTQDn9IDxTlqh" --name huiyan
openclaw channels add --channel qqbot --token "1903794346:cAVdYFk26wZyAAwU" --name huixuan
openclaw channels add --channel qqbot --token "1903793579:eFdomW3MSL0RffR9" --name huilian
openclaw channels add --channel qqbot --token "1903794370:Z4MQGrEMIzSjmcDe" --name huiwei
```

## 状态

- [x] QQBot插件已安装
- [x] 5个助手已配置
- [ ] 沙盒机制设置（待研究）
- [ ] 加入QQ群（待完成）

## 备注

- 每个QQ号最多可创建5个机器人
- 头像文件保存在：`~/Documents/Obsidian/团队知识库/assets/avatars/`
- GitHub备份：https://github.com/xintuchain/tongtong/tree/main/assets/avatars

---
*配置日期：2026-04-08*
