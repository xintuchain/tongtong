#!/bin/bash
cd ~/.openclaw/workspace
git add -A
git commit -m "auto-backup: $(date +%Y-%m-%d_%H:%M)" 2>/dev/null
git push origin main 2>/dev/null
echo "✅ GitHub 备份完成: $(date)"
