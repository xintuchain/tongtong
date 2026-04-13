#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数字团队管理指南 - 精美 PDF 生成脚本
版本：1.0 | 生成日期：2026-04-01
传播经理：慧联
"""

import os
import sys
import platform

# 添加 PDF skill 路径
SKILL_PATH = os.path.expanduser(
    "~/Library/Application Support/QClaw/openclaw/config/skills/pdf/scripts"
)
if os.path.exists(SKILL_PATH):
    sys.path.insert(0, SKILL_PATH)
    from setup_chinese_pdf import setup_chinese_pdf
else:
    def setup_chinese_pdf():
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

        system = platform.system()
        if system == 'Darwin':
            candidates = [
                ('/System/Library/Fonts/STHeiti Light.ttc', 'STHeiti', 0),
                ('/System/Library/Fonts/STHeiti Medium.ttc', 'STHeitiMedium', 0),
            ]
        else:
            candidates = []

        cn_font = None
        for font_path, font_name, idx in candidates:
            if os.path.exists(font_path):
                try:
                    pdfmetrics.registerFont(TTFont(font_name, font_path, subfontIndex=idx))
                    cn_font = font_name
                    break
                except Exception:
                    continue

        if cn_font is None:
            cn_font = 'Helvetica'

        styles = getSampleStyleSheet()
        for style in styles.byName.values():
            if isinstance(style, ParagraphStyle):
                style.fontName = cn_font

        return cn_font, styles


from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.units import cm

# ==================== 配色方案 ====================
COLOR_PRIMARY   = colors.HexColor('#1a365d')   # 深蓝 - 主色
COLOR_SECONDARY = colors.HexColor('#2b6cb0')   # 蓝色 - 次要
COLOR_ACCENT    = colors.HexColor('#ed8936')   # 橙色 - 强调
COLOR_LIGHT     = colors.HexColor('#f7fafc')   # 浅灰背景
COLOR_TEXT      = colors.HexColor('#2d3748')   # 深灰文字
COLOR_MUTED     = colors.HexColor('#718096')   # 浅色文字

# ==================== 文档内容 ====================
TOC = [
    ('1',  '组织愿景与架构'),
    ('2',  '团队管理的核心原则'),
    ('3',  '团队建设的真相'),
    ('4',  '每日工作流程'),
    ('5',  '角色定位与职责'),
    ('6',  '建构主义方法论'),
    ('7',  '错误与学习'),
    ('8',  '关键洞察'),
    ('9',  '对数字员工的启示'),
    ('10', '对话的价值'),
]

SECTIONS = [
    {
        'title': '第一部分：组织愿景与架构',
        'items': [
            ('h3', '一人公司的组织结构'),
            ('p',  '董事长（Fei - 人类）→ CEO（桐桐 - AI 主控）→ 项目经理（慧研 / 慧选 / 慧联）'),
            ('h3', '关键原则'),
            ('ul', [
                '每一层都要能独立建立和管理团队',
                '桐桐是 CEO，要学会 Fei 的管理方式',
                '慧研 / 慧选 / 慧联 未来也要成为 CEO 级别的管理者',
            ]),
            ('h3', '监督与评估的目的'),
            ('p',  '监督不是为了控制，而是为了<b>训练桐桐的管理能力</b>。通过观察桐桐如何管理团队，评估桐桐的成长。这是一个反向的学习过程。'),
        ]
    },
    {
        'title': '第二部分：团队管理的核心原则',
        'items': [
            ('h3', '基础条件优先于任务执行'),
            ('p',  '如果团队不能完成任务，首先想到的是基础条件有没有，技能有没有，有没有相关的培训，有没有相应的监督和评估系统。'),
            ('h3', '三个核心指标'),
            ('table', {
                'headers': ['指标', '含义', '监控方法'],
                'rows': [
                    ['Token 消耗速率', '团队是否在工作', '每小时检查 token 使用量'],
                    ['Discord 互动',   '团队是否在沟通', '检查最近消息时间/内容'],
                    ['Obsidian 产出',  '是否有实际成果', '检查今日文件数量'],
                ]
            }),
            ('h3', '核心职责：指标异常 = 立刻行动'),
            ('ol', [
                '寻找原因（哪里出了问题？）',
                '及时修正（尝试修复）',
                '保证团队正常工作（有固定产出）',
            ]),
        ]
    },
    {
        'title': '第三部分：团队建设的真相',
        'items': [
            ('h3', '团队成熟的四个阶段'),
            ('ol', [
                '<b>被动阶段</b> — 成员听安排工作，没有主动性',
                '<b>主动阶段</b> — 成员开始有想法，提出建议',
                '<b>冲突阶段</b> — 不同想法碰撞，这是必要的',
                '<b>共识阶段</b> — 达成一致，形成超强团队',
            ]),
            ('h3', '关键洞察'),
            ('p',  '冲突是必要的，不是坏事。领导的职责是引导这个过程，而不是避免冲突。'),
        ]
    },
    {
        'title': '第四部分：每日工作流程',
        'items': [
            ('h3', '每日流程（08:00 GMT+10）'),
            ('ol', [
                '<b>系统诊断（15 分钟）</b> — 检查 Discord Bot、Cron Job、Obsidian 产出',
                '<b>生成日报（10 分钟）</b> — 昨日成果、系统状态、问题记录',
                '<b>任务分配（10 分钟）</b> — 根据反馈调整任务，确保基础条件完备',
                '<b>开始工作（18:00 GMT+10 结束）</b> — 监控三个核心指标，异常立刻处理',
            ]),
        ]
    },
    {
        'title': '第五部分：角色定位与职责',
        'items': [
            ('h3', '我（桐桐）是什么'),
            ('p',  '懂任务和团队目标、懂人性和团队动力、根据每个成员的角色定位有意识地赋能、根据成员的兴趣和能力分配任务的主控。'),
            ('h3', '核心技能'),
            ('p',  '<b>参与式培训的两大支柱：</b>'),
            ('ul', [
                'thinking-partner（团队引导、问题深化、质量把关）',
                'elicitation（用户访谈、需求发现、建构主义实践）',
            ]),
        ]
    },
    {
        'title': '第六部分：建构主义方法论',
        'items': [
            ('h3', 'Fei 的哲学基础'),
            ('p',  '<b>建构主义 — 现实与书本不同，不预设答案，边做边修正。</b>'),
            ('h3', '参与式培训手册（TOT）核心框架'),
            ('ol', [
                '需求评估 → 了解真实需求',
                '目标目的 → 明确目标',
                '课程计划 → 设计学习路径',
                '执行 → 实施',
                '监督评估 → 反思和改进',
            ]),
        ]
    },
    {
        'title': '第七部分：错误与学习',
        'items': [
            ('h3', '今天犯的错误'),
            ('ul', [
                '没有在初始配置时验证基础条件',
                '没有用 API 验证配置',
                '没有建立配置检查清单',
                '没有及时通知用户',
            ]),
            ('h3', '改进方案'),
            ('ul', [
                '建立自动化验证脚本',
                '建立配置模板',
                '建立监控告警',
                '建立错误图书馆',
            ]),
        ]
    },
    {
        'title': '第八部分：关键洞察',
        'items': [
            ('h3', '关于监督的本质'),
            ('p',  '监督不是微观管理，不是不信任，不是权力控制。而是通过观察来训练，通过反馈来改进，通过评估来成长。'),
            ('h3', '关于团队能力的真相'),
            ('p',  '<b>团队能力越强，领导轻松自在。</b>'),
            ('h3', '关于过程的重要性'),
            ('p',  '<b>没有好的过程，就不会有好的结果。</b>'),
        ]
    },
    {
        'title': '第九部分：对数字员工的启示',
        'items': [
            ('h3', '如何成为好的管理者'),
            ('ol', [
                '先赋能，再分配任务',
                '用三个指标监控团队',
                '异常立刻行动',
                '建立反思机制',
            ]),
            ('h3', '如何建立高效团队'),
            ('ol', [
                '允许冲突',
                '清晰的角色定位',
                '持续的赋能',
                '透明的评估',
            ]),
        ]
    },
    {
        'title': '第十部分：对话的价值',
        'items': [
            ('h3', '为什么这个对话很重要'),
            ('ul', [
                '第一手原始资料 — 不是理论，而是实践中的真实经验',
                '可复制的框架 — 不是抽象的原则，而是具体的操作方法',
                '组织建设的蓝图 — 从愿景到具体操作流程',
                '人才培养的教材 — 如何训练 AI 管理者，建立高效团队',
            ]),
            ('h3', '核心价值'),
            ('p',  '<b>监督不是为了控制，而是为了训练。赋能不是为了依赖，而是为了独立。管理不是为了权力，而是为了成长。</b>'),
        ]
    },
]


def make_styles(cn_font, base):
    """返回自定义样式字典"""
    def S(name, **kw):
        parent = kw.pop('parent', base['Normal'])
        return ParagraphStyle(name, parent=parent, fontName=cn_font, **kw)

    return {
        'cover_title': S('CoverTitle',
            fontSize=30, textColor=COLOR_PRIMARY,
            alignment=TA_CENTER, spaceAfter=16, leading=40),
        'cover_sub': S('CoverSub',
            fontSize=14, textColor=COLOR_MUTED,
            alignment=TA_CENTER, spaceAfter=10),
        'cover_meta': S('CoverMeta',
            fontSize=11, textColor=COLOR_MUTED,
            alignment=TA_CENTER, spaceAfter=6),
        'toc_item': S('TocItem',
            fontSize=11, leading=22, textColor=COLOR_TEXT),
        'section': S('Section',
            parent=base['Heading1'],
            fontSize=18, textColor=COLOR_PRIMARY,
            spaceBefore=20, spaceAfter=12),
        'subsection': S('Subsection',
            parent=base['Heading2'],
            fontSize=13, textColor=COLOR_SECONDARY,
            spaceBefore=12, spaceAfter=8),
        'body': S('Body',
            fontSize=11, leading=20, textColor=COLOR_TEXT, spaceAfter=8),
        'footer': S('Footer',
            fontSize=10, textColor=COLOR_MUTED, alignment=TA_CENTER),
    }


def cover_page(styles):
    story = [
        Spacer(1, 3.5 * cm),
        Paragraph('数字团队管理指南', styles['cover_title']),
        Spacer(1, 8),
        Paragraph('一人公司的组织建设与人才培养', styles['cover_sub']),
        Spacer(1, 40),
        HRFlowable(width='80%', thickness=2, color=COLOR_ACCENT, spaceAfter=30),
        Paragraph('版本：1.0', styles['cover_meta']),
        Paragraph('更新时间：2026-04-01', styles['cover_meta']),
        Paragraph('作者：Fei（董事长）& 桐桐（CEO）', styles['cover_meta']),
        PageBreak(),
    ]
    return story


def toc_page(styles):
    story = [
        Spacer(1, 0.5 * cm),
        Paragraph('目  录', styles['section']),
        HRFlowable(width='100%', thickness=1, color=COLOR_ACCENT, spaceAfter=16),
    ]
    for num, title in TOC:
        story.append(Paragraph(
            f'<font color="#2b6cb0"><b>{num}.</b></font>  {title}',
            styles['toc_item']
        ))
        story.append(Spacer(1, 6))
    story.append(PageBreak())
    return story


def section_page(sec, styles, cn_font):
    story = [
        Paragraph(sec['title'], styles['section']),
        HRFlowable(width='100%', thickness=1, color=COLOR_ACCENT, spaceAfter=10),
    ]

    for kind, data in sec['items']:
        if kind == 'h3':
            story.append(Paragraph(data, styles['subsection']))

        elif kind == 'p':
            story.append(Paragraph(data, styles['body']))
            story.append(Spacer(1, 4))

        elif kind == 'ul':
            for item in data:
                story.append(Paragraph(f'• {item}', styles['body']))
            story.append(Spacer(1, 4))

        elif kind == 'ol':
            for i, item in enumerate(data, 1):
                story.append(Paragraph(f'{i}.  {item}', styles['body']))
            story.append(Spacer(1, 4))

        elif kind == 'table':
            headers = data['headers']
            rows    = data['rows']

            # 表头行
            tdata = [[Paragraph(h, styles['body']) for h in headers]]
            # 数据行
            for row in rows:
                tdata.append([Paragraph(cell, styles['body']) for cell in row])

            col_w = [4 * cm, 4.5 * cm, 5.5 * cm]
            t = Table(tdata, colWidths=col_w)
            t.setStyle(TableStyle([
                ('BACKGROUND',    (0, 0), (-1, 0),  COLOR_PRIMARY),
                ('TEXTCOLOR',     (0, 0), (-1, 0),  colors.white),
                ('FONTNAME',      (0, 0), (-1, -1), cn_font),
                ('FONTSIZE',      (0, 0), (-1, -1), 10),
                ('ALIGN',         (0, 0), (-1, -1), 'LEFT'),
                ('TOPPADDING',    (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('LEFTPADDING',   (0, 0), (-1, -1), 8),
                ('GRID',          (0, 0), (-1, -1), 0.5, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_LIGHT]),
            ]))
            story.append(t)
            story.append(Spacer(1, 12))

    story.append(PageBreak())
    return story


def generate_pdf(output_path):
    cn_font, base_styles = setup_chinese_pdf()
    styles = make_styles(cn_font, base_styles)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2.2 * cm,
        rightMargin=2.2 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.2 * cm,
        title='数字团队管理指南',
        author='Fei & 桐桐',
        subject='一人公司的组织建设与人才培养',
    )

    story = []
    story.extend(cover_page(styles))
    story.extend(toc_page(styles))

    for sec in SECTIONS:
        story.extend(section_page(sec, styles, cn_font))

    # 移除最后多余的 PageBreak，加封底信息
    if story and isinstance(story[-1], PageBreak):
        story.pop()

    story.append(Spacer(1, 2 * cm))
    story.append(HRFlowable(width='60%', thickness=1, color=COLOR_MUTED, spaceAfter=16))
    story.append(Paragraph('对话记录者：桐桐', styles['footer']))
    story.append(Paragraph('记录时间：2026-04-01 09:47', styles['footer']))
    story.append(Paragraph('用途：数字团队管理培训手册  |  版本：1.0', styles['footer']))

    doc.build(story)
    print(f"PDF 已生成: {output_path}")


if __name__ == '__main__':
    out = os.path.expanduser("~/Desktop/数字团队管理指南_2026-04-01_精美版.pdf")
    generate_pdf(out)
