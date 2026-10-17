from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def bar(d, color, w=10, inner=4):
    """太い棒（外線＋色の芯）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def ground(x1=20, x2=180, y=180):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2)


def mini_face(cx, cy, r=2.5, gap=10, ch=(4, 2.5)):
    return (dot(cx - gap, cy, r) + dot(cx + gap, cy, r)
            + cheeks(cx - gap - 6, cx + gap + 6, cy + 6, ch[0], ch[1])
            + s('path', d=f'M{cx-3} {cy+5} Q{cx} {cy+8} {cx+3} {cy+5}', stroke_width=2))


# 1. dining-table
ITEMS['dining-table'] = (
    # left chair (side view)
    z('rect', '#d9a66b', x=24, y=66, width=10, height=112, rx=3)
    + s('rect', '#9a6a3f', x=60, y=134, width=7, height=44, rx=2)
    + z('rect', '#d9a66b', x=24, y=124, width=46, height=12, rx=3)
    # right chair
    + z('rect', '#d9a66b', x=162, y=66, width=10, height=112, rx=3)
    + s('rect', '#9a6a3f', x=129, y=134, width=7, height=44, rx=2)
    + z('rect', '#d9a66b', x=126, y=124, width=46, height=12, rx=3)
    # table
    + z('rect', '#9a6a3f', x=60, y=108, width=10, height=70, rx=2)
    + z('rect', '#9a6a3f', x=126, y=108, width=10, height=70, rx=2)
    + z('rect', '#d9a66b', x=46, y=98, width=104, height=14, rx=4)
    + s('rect', '#f6a6b8', x=64, y=104, width=68, height=8, stroke_width=2.5)
    # vase with flower
    + s('path', d='M98 78 L96 58', stroke_width=2.5)
    + z('circle', '#f07a8a', cx=95, cy=54, r=7)
    + s('circle', '#ffe27a', cx=95, cy=54, r=2.5, stroke='none')
    + z('path', '#8fc7e8', d='M90 98 Q86 86 92 78 L104 78 Q110 86 106 98 Z')
    # plate
    + z('ellipse', '#ffffff', cx=128, cy=95, rx=14, ry=4)
    + ground(16, 184)
)

# 2. chair
ITEMS['chair'] = (
    s('rect', '#9a6a3f', x=126, y=114, width=8, height=56, rx=2)
    + z('rect', '#d9a66b', x=60, y=30, width=12, height=146, rx=3)
    + z('rect', '#d9a66b', x=128, y=30, width=12, height=146, rx=3)
    + z('rect', '#d9a66b', x=60, y=30, width=80, height=18, rx=6)
    + s('rect', '#d9a66b', x=82, y=48, width=8, height=60)
    + s('rect', '#d9a66b', x=110, y=48, width=8, height=60)
    + z('path', '#f5b971', d='M50 112 L150 112 L158 132 L42 132 Z')
    + z('rect', '#d9a66b', x=42, y=132, width=116, height=10, rx=3)
    + z('rect', '#d9a66b', x=46, y=142, width=12, height=36, rx=3)
    + z('rect', '#d9a66b', x=142, y=142, width=12, height=36, rx=3)
    + ground(28, 172)
)

# 3. bookshelf
_books = ''
for (x, w, h, c) in [(58, 12, 32, '#e8735a'), (70, 10, 36, '#8fc7e8'), (80, 14, 30, '#9ccf7a'),
                     (94, 10, 36, '#f5d58a'), (104, 12, 34, '#a98bd0')]:
    _books += s('rect', c, x=x, y=70 - h, width=w, height=h, rx=1.5, stroke_width=2.5)
_books += s('path', '#f6a6b8', d='M118 70 L130 38 L140 42 L128 70 Z', stroke_width=2.5)
for (x, w, h, c) in [(58, 14, 34, '#8fb3e0'), (72, 10, 30, '#f07a8a'), (82, 12, 36, '#7cc4b0'),
                     (114, 10, 34, '#f5b971'), (124, 14, 30, '#e8735a'), (138, 6, 28, '#9ccf7a')]:
    _books += s('rect', c, x=x, y=118 - h, width=w, height=h, rx=1.5, stroke_width=2.5)
_books += s('path', '#c9d3db', d='M96 118 Q94 98 102 96 Q110 98 108 118 Z', stroke_width=2.5)
_books += (s('rect', '#8fc7e8', x=58, y=156, width=40, height=10, rx=1.5, stroke_width=2.5)
           + s('rect', '#f5d58a', x=60, y=146, width=36, height=10, rx=1.5, stroke_width=2.5)
           + s('rect', '#f07a8a', x=62, y=136, width=32, height=10, rx=1.5, stroke_width=2.5))
for (x, w, h, c) in [(112, 12, 34, '#9ccf7a'), (124, 10, 30, '#a98bd0'), (134, 12, 36, '#e8735a')]:
    _books += s('rect', c, x=x, y=166 - h, width=w, height=h, rx=1.5, stroke_width=2.5)
ITEMS['bookshelf'] = (
    z('rect', '#d9a66b', x=46, y=24, width=108, height=154, rx=4)
    + s('rect', '#f6e0c4', x=54, y=32, width=92, height=38)
    + s('rect', '#f6e0c4', x=54, y=80, width=92, height=38)
    + s('rect', '#f6e0c4', x=54, y=128, width=92, height=38)
    + _books
    + ground(28, 172)
)

# 4. wardrobe
ITEMS['wardrobe'] = (
    s('rect', '#9a6a3f', x=52, y=168, width=10, height=12, rx=2)
    + s('rect', '#9a6a3f', x=138, y=168, width=10, height=12, rx=2)
    + z('rect', '#d9a66b', x=44, y=22, width=112, height=148, rx=6)
    + s('rect', '#f5b971', x=52, y=32, width=46, height=128, rx=3)
    + s('rect', '#f5b971', x=102, y=32, width=46, height=128, rx=3)
    + s('rect', '#f6e0c4', x=60, y=44, width=30, height=46, rx=3, stroke_width=2.5)
    + s('rect', '#f6e0c4', x=110, y=44, width=30, height=46, rx=3, stroke_width=2.5)
    + s('rect', '#f6e0c4', x=60, y=102, width=30, height=46, rx=3, stroke_width=2.5)
    + s('rect', '#f6e0c4', x=110, y=102, width=30, height=46, rx=3, stroke_width=2.5)
    + s('rect', '#9a6a3f', x=91, y=84, width=5, height=20, rx=2.5, stroke_width=2)
    + s('rect', '#9a6a3f', x=104, y=84, width=5, height=20, rx=2.5, stroke_width=2)
    + ground(28, 172)
)

# 5. drawers
ITEMS['drawers'] = (
    # small plant on top
    s('path', d='M120 50 L120 36', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M120 44 Q106 42 106 30 Q118 30 120 44 Z')
    + z('path', '#9ccf7a', d='M120 40 Q134 38 134 26 Q122 26 120 40 Z')
    + z('path', '#e8735a', d='M110 50 L130 50 L127 68 L113 68 Z')
    # lamp-ish photo frame
    + z('rect', '#f5d58a', x=62, y=46, width=26, height=22, rx=2)
    + s('rect', '#8fc7e8', x=67, y=51, width=16, height=12, stroke_width=2)
    + s('rect', '#9a6a3f', x=46, y=164, width=10, height=14, rx=2)
    + s('rect', '#9a6a3f', x=144, y=164, width=10, height=14, rx=2)
    + z('rect', '#d9a66b', x=38, y=68, width=124, height=98, rx=5)
    + s('rect', '#f5b971', x=46, y=76, width=108, height=24, rx=3)
    + s('rect', '#f5b971', x=46, y=106, width=108, height=24, rx=3)
    + s('rect', '#f5b971', x=46, y=136, width=108, height=24, rx=3)
    + s('rect', '#9a6a3f', x=88, y=85, width=24, height=6, rx=3, stroke_width=2)
    + s('rect', '#9a6a3f', x=88, y=115, width=24, height=6, rx=3, stroke_width=2)
    + s('rect', '#9a6a3f', x=88, y=145, width=24, height=6, rx=3, stroke_width=2)
    + ground(24, 176)
)

# 6. mirror (standing)
ITEMS['mirror'] = (
    bar('M80 140 L60 178', '#9a6a3f')
    + bar('M120 140 L140 178', '#9a6a3f')
    + bar('M100 150 L100 172', '#9a6a3f')
    + z('ellipse', '#d9a66b', cx=100, cy=86, rx=46, ry=64)
    + s('ellipse', '#d8eef8', cx=100, cy=86, rx=36, ry=54)
    + s('path', d='M78 70 Q82 50 96 42', stroke='#ffffff', stroke_width=5)
    + s('path', d='M80 86 L86 78', stroke='#ffffff', stroke_width=5)
    + s('path', d='M108 128 L122 112', stroke='#ffffff', stroke_width=4)
    + ground(36, 164)
)

# 7. window-curtains
ITEMS['window-curtains'] = (
    z('rect', '#f4f4f0', x=46, y=40, width=108, height=112, rx=4)
    + s('rect', '#8fc7e8', x=54, y=48, width=92, height=96)
    + s('path', '#ffffff', d='M66 82 Q66 72 76 72 Q80 64 90 68 Q100 66 100 76 Q108 78 104 84 Z', stroke_width=2.5)
    + s('circle', '#ffe27a', cx=126, cy=66, r=9, stroke_width=2.5)
    + s('path', d='M100 48 L100 144 M54 96 L146 96', stroke_width=4)
    + z('rect', '#d9a66b', x=40, y=148, width=120, height=10, rx=3)
    # curtains
    + z('path', '#f6a6b8', d='M30 34 L74 34 Q68 70 52 96 Q60 130 50 162 L32 162 Q38 130 36 100 Q30 70 30 34 Z')
    + z('path', '#f6a6b8', d='M170 34 L126 34 Q132 70 148 96 Q140 130 150 162 L168 162 Q162 130 164 100 Q170 70 170 34 Z')
    + s('path', d='M42 40 Q44 70 44 96 M58 40 Q56 64 52 86', stroke_width=2)
    + s('path', d='M158 40 Q156 70 156 96 M142 40 Q144 64 148 86', stroke_width=2)
    + z('rect', '#f5b971', x=34, y=92, width=24, height=8, rx=4)
    + z('rect', '#f5b971', x=142, y=92, width=24, height=8, rx=4)
    + bar('M24 32 L176 32', '#9a6a3f', w=9, inner=3)
    + z('circle', '#9a6a3f', cx=24, cy=32, r=5) + z('circle', '#9a6a3f', cx=176, cy=32, r=5)
)

# 8. kotatsu
ITEMS['kotatsu'] = (
    z('path', '#e8735a', d='M42 104 L158 104 Q164 140 172 170 Q154 178 136 170 Q118 178 100 170 Q82 178 64 170 Q46 178 28 170 Q36 140 42 104 Z')
    + s('path', d='M56 120 Q52 146 48 166 M100 118 L100 168 M144 120 Q148 146 152 166', stroke_width=2)
    + s('path', d='M40 136 Q100 128 160 136', stroke='#f5d58a', stroke_width=5)
    + s('path', d='M36 152 Q100 144 164 152', stroke='#f5d58a', stroke_width=5)
    + z('rect', '#d9a66b', x=30, y=96, width=140, height=14, rx=4)
    # mikan
    + s('ellipse', '#c9d3db', cx=100, cy=96, rx=34, ry=5)
    + z('circle', '#ffc94d', cx=86, cy=80, r=13)
    + z('circle', '#ffc94d', cx=112, cy=80, r=13)
    + z('circle', '#ffc94d', cx=99, cy=62, r=12)
    + s('path', '#9ccf7a', d='M99 50 Q106 42 112 48 Q104 52 99 50 Z', stroke_width=2)
    + ground(16, 184, 182)
)

# 9. futon (top-down)
ITEMS['futon'] = (
    z('rect', '#ffffff', x=44, y=24, width=112, height=154, rx=10)
    + z('rect', '#f5d58a', x=70, y=32, width=60, height=28, rx=12)
    + s('path', d='M80 46 L120 46', stroke_width=2)
    + z('path', '#8fb3e0', d='M48 76 Q100 68 152 76 L152 166 Q152 174 144 174 L56 174 Q48 174 48 166 Z')
    + s('path', '#ffffff', d='M48 76 Q100 68 152 76 L152 88 Q100 80 48 88 Z', stroke_width=2.5)
    + ''.join(s('path', d=f'M{x-5} {y} Q{x} {y-6} {x+5} {y}', stroke='#ffffff', stroke_width=3)
              for (x, y) in [(72, 108), (100, 104), (128, 108), (86, 132), (114, 132), (72, 156), (100, 152), (128, 156)])
)

# 10. cushion
ITEMS['cushion'] = (
    z('path', '#f6a6b8', d='M38 46 Q70 58 100 54 Q130 58 162 46 Q150 78 154 108 Q150 138 162 170 Q130 158 100 162 Q70 158 38 170 Q50 138 46 108 Q50 78 38 46 Z')
    + s('path', d='M54 62 Q100 72 146 62 M54 154 Q100 146 146 154', stroke_width=2, stroke='#f07a8a')
    + dot(82, 104) + dot(118, 104) + cheeks(72, 128, 118, 7, 4)
    + s('path', d='M94 122 Q100 127 106 122', stroke_width=2.5)
)

# 11. refrigerator
ITEMS['refrigerator'] = (
    s('rect', '#b9a99c', x=60, y=174, width=12, height=6, rx=2, stroke_width=2.5)
    + s('rect', '#b9a99c', x=128, y=174, width=12, height=6, rx=2, stroke_width=2.5)
    + z('rect', '#8fc7e8', x=54, y=18, width=92, height=158, rx=12)
    + s('path', d='M54 70 L146 70')
    + bar('M130 38 L130 58', '#c9d3db', w=9, inner=3)
    + bar('M130 84 L130 120', '#c9d3db', w=9, inner=3)
    + s('circle', '#f07a8a', cx=72, cy=36, r=5, stroke_width=2)
    + s('circle', '#ffe27a', cx=86, cy=44, r=5, stroke_width=2)
    + s('rect', '#ffffff', x=68, y=84, width=22, height=16, rx=2, stroke_width=2)
    + dot(84, 132) + dot(112, 132) + cheeks(76, 120, 142, 6, 3.5)
    + s('path', d='M93 142 Q98 147 103 142', stroke_width=2.5)
    + ground(30, 170, 180)
)

# 12. microwave
ITEMS['microwave'] = (
    s('rect', '#b9a99c', x=40, y=150, width=14, height=8, rx=2, stroke_width=2.5)
    + s('rect', '#b9a99c', x=146, y=150, width=14, height=8, rx=2, stroke_width=2.5)
    + z('rect', '#f4f4f0', x=26, y=56, width=148, height=96, rx=10)
    + s('rect', '#5b6b7a', x=38, y=68, width=94, height=72, rx=6)
    + s('rect', '#f5d58a', x=46, y=76, width=78, height=56, rx=4, stroke='none')
    + z('ellipse', '#ffffff', cx=85, cy=122, rx=30, ry=7)
    + z('path', '#e8735a', d='M66 118 Q66 98 85 98 Q104 98 104 118 Z')
    + s('path', d='M80 92 Q76 86 80 80 M90 92 Q86 86 90 80', stroke_width=2)
    + s('path', d='M140 68 L140 140', stroke_width=2.5)
    + s('rect', '#8fc7e8', x=146, y=70, width=20, height=10, rx=2, stroke_width=2)
    + s('circle', '#c9d3db', cx=156, cy=98, r=8)
    + s('path', d='M156 92 L156 98', stroke_width=2)
    + s('circle', '#c9d3db', cx=156, cy=124, r=8)
    + s('path', d='M156 118 L156 124', stroke_width=2)
    + ground(20, 180, 158)
)

# 13. rice-cooker
ITEMS['rice-cooker'] = (
    s('path', d='M86 40 Q84 30 90 22 M110 40 Q108 30 114 22', stroke_width=2.5)
    + z('path', '#f4f4f0', d='M38 98 Q40 170 56 176 L144 176 Q160 170 162 98 Z')
    + z('path', '#f6a6b8', d='M34 100 Q36 52 100 50 Q164 52 166 100 Z')
    + z('rect', '#c9d3db', x=82, y=44, width=36, height=14, rx=7)
    + z('rect', '#c9d3db', x=30, y=96, width=140, height=12, rx=6)
    + s('rect', '#c9d3db', x=72, y=120, width=56, height=34, rx=8)
    + s('circle', '#e8735a', cx=88, cy=137, r=6, stroke_width=2)
    + s('rect', '#8fc7e8', x=100, y=130, width=20, height=14, rx=2, stroke_width=2)
    + dot(70, 78, 3) + dot(130, 78, 3) + cheeks(60, 140, 86, 5, 3)
    + s('path', d='M96 82 Q100 86 104 82', stroke_width=2)
    + ground(24, 176, 180)
)

# 14. toaster
ITEMS['toaster'] = (
    s('path', d='M70 30 L66 22 M100 26 L100 18 M130 30 L134 22', stroke_width=2.5)
    + z('path', '#f5b971', d='M60 104 L60 52 Q60 40 72 40 Q82 36 88 44 L88 104 Z')
    + s('path', '#f6e0c4', d='M66 100 L66 56 Q66 48 72 48 Q78 46 82 52 L82 100 Z', stroke='none')
    + z('path', '#f5b971', d='M110 104 L110 46 Q110 34 122 34 Q132 30 138 38 L138 104 Z')
    + s('path', '#f6e0c4', d='M116 100 L116 50 Q116 42 122 42 Q128 40 132 46 L132 100 Z', stroke='none')
    + z('rect', '#e8735a', x=40, y=92, width=120, height=80, rx=20)
    + s('rect', OUT, x=56, y=94, width=36, height=6, rx=3, stroke='none')
    + s('rect', OUT, x=106, y=94, width=36, height=6, rx=3, stroke='none')
    + z('rect', '#c9d3db', x=158, y=112, width=12, height=24, rx=4)
    + dot(86, 130) + dot(114, 130) + cheeks(76, 124, 142, 6, 3.5)
    + s('path', d='M94 142 Q100 147 106 142', stroke_width=2.5)
    + ground(26, 178, 178)
)

# 15. kettle
ITEMS['kettle'] = (
    s('path', d='M158 64 Q150 54 158 44 Q166 34 158 24', stroke_width=3)
    + s('path', d='M172 70 Q166 62 172 54', stroke_width=2.5)
    + z('path', '#7cc4b0', d='M128 132 Q150 116 158 80 L166 80 Q160 132 136 152 Z')
    + s('path', d='M74 68 Q74 32 100 32 Q126 32 126 68', stroke_width=10)
    + s('path', d='M74 68 Q74 32 100 32 Q126 32 126 68', stroke='#9a6a3f', stroke_width=4)
    + z('path', '#7cc4b0', d='M56 172 Q42 172 46 148 Q54 92 76 72 Q100 60 124 72 Q146 92 154 148 Q158 172 144 172 Z')
    + z('ellipse', '#7cc4b0', cx=100, cy=72, rx=26, ry=7)
    + z('circle', '#9a6a3f', cx=100, cy=62, r=6)
    + dot(86, 124) + dot(114, 124) + cheeks(76, 124, 136, 6, 3.5)
    + s('path', d='M94 136 Q100 141 106 136', stroke_width=2.5)
    + ground(26, 176, 178)
)

# 16. vacuum-cleaner (canister)
ITEMS['vacuum-cleaner'] = (
    s('path', d='M74 128 Q60 70 100 56 Q126 50 132 70', stroke_width=12)
    + s('path', d='M74 128 Q60 70 100 56 Q126 50 132 70', stroke='#c9d3db', stroke_width=6)
    + s('path', d='M80 124 Q68 74 102 62', stroke='#b9a99c', stroke_width=2)
    + bar('M136 66 L154 156', '#c9d3db', w=10, inner=4)
    + z('rect', '#e8735a', x=124, y=56, width=22, height=16, rx=6)
    + z('rect', '#5b6b7a', x=134, y=154, width=46, height=16, rx=6)
    + z('path', '#e8735a', d='M28 170 Q22 120 64 116 Q104 116 104 156 Q104 172 90 172 L40 172 Q28 172 28 170 Z')
    + z('circle', '#5b6b7a', cx=46, cy=168, r=10)
    + s('circle', '#c9d3db', cx=46, cy=168, r=4, stroke_width=2)
    + s('rect', '#f5d58a', x=56, y=126, width=30, height=10, rx=5, stroke_width=2.5)
    + ground(16, 184, 180)
)

# 17. robot-vacuum
ITEMS['robot-vacuum'] = (
    s('path', d='M22 104 L40 104 M18 120 L34 120 M24 136 L38 136', stroke_width=2.5)
    + s('path', d='M54 150 L46 166 M54 150 L60 168 M54 150 L40 156', stroke_width=2)
    + s('path', d='M146 150 L154 166 M146 150 L140 168 M146 150 L160 156', stroke_width=2)
    + z('path', '#5b6b7a', d='M30 110 L30 132 Q30 158 100 158 Q170 158 170 132 L170 110 Z')
    + z('ellipse', '#c9d3db', cx=100, cy=110, rx=70, ry=30)
    + s('ellipse', '#f4f4f0', cx=100, cy=106, rx=48, ry=18)
    + z('circle', '#8fc7e8', cx=100, cy=104, r=8)
    + s('path', d='M34 130 Q100 150 166 130', stroke='#c9d3db', stroke_width=3)
    + dot(84, 140, 4.5, '#ffffff') + dot(116, 140, 4.5, '#ffffff') + cheeks(72, 128, 146, 5, 3)
    + s('path', d='M94 145 Q100 151 106 145', stroke='#ffffff', stroke_width=2.5)
    + s('circle', '#9ccf7a', cx=130, cy=92, r=3, stroke_width=1.5)
    + ground(20, 180, 172)
)

# 18. air-conditioner
ITEMS['air-conditioner'] = (
    z('rect', '#f4f4f0', x=24, y=50, width=152, height=64, rx=16)
    + s('path', d='M30 98 L170 98', stroke_width=2.5)
    + z('path', '#c9d3db', d='M38 104 L162 104 L156 116 L44 116 Z')
    + s('path', d='M44 64 L120 64 M44 74 L120 74 M44 84 L120 84', stroke='#c9d3db', stroke_width=3)
    + s('circle', '#9ccf7a', cx=156, cy=72, r=4, stroke_width=2)
    + s('rect', '#8fc7e8', x=136, y=80, width=26, height=10, rx=2, stroke_width=2)
    + s('path', d='M60 132 Q52 142 60 152 Q68 162 60 172', stroke='#8fc7e8', stroke_width=5)
    + s('path', d='M100 132 Q92 142 100 152 Q108 162 100 172', stroke='#8fc7e8', stroke_width=5)
    + s('path', d='M140 132 Q132 142 140 152 Q148 162 140 172', stroke='#8fc7e8', stroke_width=5)
    + s('path', '#ffffff', d='M80 150 L80 162 M74 156 L86 156 M76 152 L84 160 M84 152 L76 160', stroke='#8fc7e8', stroke_width=2.5)
    + s('path', '#ffffff', d='M120 150 L120 162 M114 156 L126 156 M116 152 L124 160 M124 152 L116 160', stroke='#8fc7e8', stroke_width=2.5)
)

# 19. electric-fan
_blades = ''.join(
    z('ellipse', '#8fc7e8', cx=100, cy=58, rx=13, ry=21, transform=f'rotate({a} 100 78)') for a in (0, 120, 240))
ITEMS['electric-fan'] = (
    z('ellipse', '#7cc4b0', cx=100, cy=170, rx=46, ry=10)
    + bar('M100 130 L100 166', '#f4f4f0', w=14, inner=8)
    + z('rect', '#7cc4b0', x=88, y=118, width=24, height=20, rx=6)
    + s('circle', '#ffffff', cx=100, cy=78, r=54)
    + _blades
    + ''.join(s('path', d=f'M100 78 L{100 + 54 * c:.1f} {78 + 54 * sn:.1f}', stroke_width=1.5)
              for (c, sn) in [(1, 0), (0.707, 0.707), (0, 1), (-0.707, 0.707), (-1, 0), (-0.707, -0.707), (0, -1), (0.707, -0.707)])
    + s('circle', cx=100, cy=78, r=36, stroke_width=1.5)
    + s('circle', cx=100, cy=78, r=54, stroke_width=4)
    + z('circle', '#7cc4b0', cx=100, cy=78, r=10)
    + s('circle', '#ffe27a', cx=88, cy=170, r=3, stroke_width=1.5)
    + s('circle', '#f6a6b8', cx=100, cy=172, r=3, stroke_width=1.5)
    + s('circle', '#8fc7e8', cx=112, cy=170, r=3, stroke_width=1.5)
)

# 20. heater
ITEMS['heater'] = (
    s('path', d='M70 50 Q62 40 70 30 Q78 20 70 12', stroke='#e8735a', stroke_width=4)
    + s('path', d='M100 46 Q92 36 100 26 Q108 16 100 8', stroke='#e8735a', stroke_width=4)
    + s('path', d='M130 50 Q122 40 130 30 Q138 20 130 12', stroke='#e8735a', stroke_width=4)
    + s('rect', '#9a6a3f', x=54, y=166, width=14, height=12, rx=2)
    + s('rect', '#9a6a3f', x=132, y=166, width=14, height=12, rx=2)
    + z('rect', '#f5d58a', x=42, y=58, width=116, height=110, rx=14)
    + s('rect', '#5b6b7a', x=54, y=72, width=92, height=68, rx=6)
    + ''.join(s('rect', '#ffc94d', x=62, y=y, width=76, height=8, rx=4, stroke='#e8735a', stroke_width=2.5) for y in (80, 96, 112, 128))
    + s('circle', '#c9d3db', cx=134, cy=154, r=7, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=112, cy=154, r=4, stroke_width=2)
    + s('path', d='M58 154 L94 154', stroke='#c9d3db', stroke_width=4)
    + ground(28, 172, 180)
)
