#!/bin/bash
# 数字团队日志系统启动脚本
# 放在 ~/.openclaw/workspace/startup.sh
# 每次开机或OpenClaw启动时执行

set -e

echo "🚀 启动数字团队日志系统..."

# 1. 运行日志系统检查
python3 ~/Desktop/daily_log_system.py

# 2. 检查是否需要生成新的日志
TODAY=$(date +%Y-%m-%d)
LOG_FILE="$HOME/Documents/Obsidian/数字项目库/00-项目总览/日志/${TODAY}_日志.md"

if [ ! -f "$LOG_FILE" ]; then
    echo ""
    echo "📝 生成今天的日志模板..."
    # 这里可以调用一个Python脚本来生成日志模板
fi

# 3. 生成PDF
echo ""
echo "📄 生成PDF日志..."
~/Desktop/pdf_venv/bin/python ~/Desktop/gen_daily_log.py

# 4. 显示完成信息
echo ""
echo "✨ 日志系统启动完成！"
echo "📍 日志位置：$LOG_FILE"
echo "📄 PDF位置：$HOME/Desktop/${TODAY}_日志.pdf"
echo ""
echo "💡 提示：编辑日志后，运行以下命令发送微信备份："
echo "   python3 ~/Desktop/send_log_to_wechat.py"
