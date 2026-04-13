#!/bin/bash

echo "=== 团队健康检查 ==="
echo ""

# 1. Token 使用情况
echo "📊 Token 使用情况："
echo "  （需要从 dashboard 获取）"

# 2. Discord 互动（最近消息）
echo ""
echo "💬 Discord 互动（最近消息）："
curl -s "https://discord.com/api/v10/channels/1489414235032125581/messages?limit=5" \
  -H "Authorization: Bot DISCORD_TOKEN_REMOVED" \
  | python3 -c "
import sys, json
msgs = json.load(sys.stdin)
for m in msgs[:5]:
    ts = m.get('timestamp','')[:16]
    author = m.get('author',{}).get('username','?')
    content = m.get('content','')[:50].replace('\n',' ')
    print(f'  {ts} [{author}]: {content}...')
"

# 3. Obsidian 产出（今天的文件）
echo ""
echo "📁 Obsidian 今日产出："
find ~/Documents/Obsidian/数字项目库/01-当前项目 -name "2026-03-31*.md" 2>/dev/null | while read f; do
    echo "  $(basename $f)"
done

# 4. Cron job 状态
echo ""
echo "⏰ 子代理 Cron Job 状态："
python3 -c "
import json
with open('/Users/feilong/.qclaw/cron/jobs.json') as f:
    d = json.load(f)
for job in d['jobs']:
    if 'huiyan' in job.get('id','') or 'huixuan' in job.get('id','') or 'huilian' in job.get('id',''):
        state = job.get('state',{})
        status = state.get('lastRunStatus','unknown')
        err = state.get('lastError','')
        print(f\"  {job.get('name')}: {status}\")
        if err:
            print(f\"    Error: {err[:60]}\")
"

echo ""
echo "=== 检查完成 ==="
