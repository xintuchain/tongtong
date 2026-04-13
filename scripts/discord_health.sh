#!/bin/bash
# Discord 健康检查脚本
# 从 openclaw.json 读取最新 token

CONFIG_FILE="$HOME/.qclaw/openclaw.json"

# 解析 JSON 中的 discord tokens
BOT_TOKENS=$(python3 -c "
import json, sys
with open('$CONFIG_FILE') as f:
    cfg = json.load(f)
accounts = cfg.get('channels', {}).get('discord', {}).get('accounts', {})
for name, info in accounts.items():
    token = info.get('token', '')
    if token:
        print(f'{name}|{token}')
")

HEALTHY=0
UNHEALTHY=0
DETAILS=""

while IFS='|' read -r name token; do
  if [ -z "$name" ]; then continue; fi
  
  http_code=$(curl -s -o /dev/null -w "%{http_code}" "https://discord.com/api/v10/gateway/bot" \
    -H "Authorization: Bot $token" 2>/dev/null)
  
  if [ "$http_code" = "200" ]; then
    HEALTHY=$((HEALTHY + 1))
    DETAILS="${DETAILS}✅ ${name} OK\n"
  else
    UNHEALTHY=$((UNHEALTHY + 1))
    DETAILS="${DETAILS}❌ ${name} (HTTP ${http_code})\n"
  fi
done <<< "$BOT_TOKENS"

echo "Discord 健康检查:"
echo -e "$DETAILS"
echo "---"
echo "健康: $HEALTHY, 异常: $UNHEALTHY"

# 如果有异常，更新状态文件
STATUS_FILE="$HOME/.openclaw/workspace/memory/discord-status.json"
if [ "$UNHEALTHY" -gt 0 ]; then
  echo "{\"last_check\": $(date +%s), \"healthy\": false, \"healthy_count\": $HEALTHY, \"unhealthy_count\": $UNHEALTHY}" > "$STATUS_FILE"
else
  echo "{\"last_check\": $(date +%s), \"healthy\": true, \"healthy_count\": $HEALTHY, \"unhealthy_count\": 0}" > "$STATUS_FILE"
fi
