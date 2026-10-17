from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def heart_d(cx, cy, w):
    return (f'M{cx} {cy+0.5*w:.1f} C{cx-0.15*w:.1f} {cy+0.3*w:.1f} {cx-0.55*w:.1f} {cy+0.1*w:.1f} {cx-0.5*w:.1f} {cy-0.2*w:.1f} '
            f'C{cx-0.45*w:.1f} {cy-0.5*w:.1f} {cx-0.05*w:.1f} {cy-0.5*w:.1f} {cx} {cy-0.25*w:.1f} '
            f'C{cx+0.05*w:.1f} {cy-0.5*w:.1f} {cx+0.45*w:.1f} {cy-0.5*w:.1f} {cx+0.5*w:.1f} {cy-0.2*w:.1f} '
            f'C{cx+0.55*w:.1f} {cy+0.1*w:.1f} {cx+0.15*w:.1f} {cy+0.3*w:.1f} {cx} {cy+0.5*w:.1f}Z')


def mini_face(cx, cy, r, hair, skin='#ffd9b8'):
    """小さめの人の顔（2人以上並べる時用）"""
    o = z('circle', skin, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{cx-r} {cy-1} Q{cx-r} {cy-r-1} {cx} {cy-r} Q{cx+r} {cy-r-1} {cx+r} {cy-1} '
                         f'Q{cx+r*0.6} {cy-r*0.5} {cx} {cy-r*0.5} Q{cx-r*0.6} {cy-r*0.5} {cx-r} {cy-1}Z', stroke_width=2.5)
    o += dot(cx - r * 0.36, cy + r * 0.08, 2.3) + dot(cx + r * 0.36, cy + r * 0.08, 2.3)
    o += cheeks(cx - r * 0.6, cx + r * 0.6, cy + r * 0.4, r * 0.2, r * 0.12)
    o += s('path', d=f'M{cx-r*0.18:.1f} {cy+r*0.48:.1f} Q{cx} {cy+r*0.65:.1f} {cx+r*0.18:.1f} {cy+r*0.48:.1f}', stroke_width=2)
    return o


def cute(cx, cy, sp=12, r=3.5, ck=6):
    """点の目＋ほっぺ＋口"""
    return (dot(cx - sp, cy, r) + dot(cx + sp, cy, r) + cheeks(cx - sp - 8, cx + sp + 8, cy + 9, ck, ck * 0.6)
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))


def sanbo(cx, y, w):
    """三方（お供え台）"""
    return (z('path', '#d9a66b', d=f'M{cx-w*0.38} {y+10} L{cx+w*0.38} {y+10} L{cx+w*0.3} {y+34} L{cx-w*0.3} {y+34}Z')
            + s('ellipse', '#9a6a3f', cx=cx, cy=y + 23, rx=w * 0.09, ry=6, stroke_width=2.5)
            + z('rect', '#d9a66b', x=cx - w / 2, y=y, width=w, height=11, rx=3))


# 1. new year sunrise
rays = ''.join(thick(f'M{100+58*cos(a*pi/180):.1f} {124+58*sin(a*pi/180):.1f} L{100+74*cos(a*pi/180):.1f} {124+74*sin(a*pi/180):.1f}', '#ffc94d', 8, 4)
               for a in (195, 225, 255, 285, 315, 345))
ITEMS['new-year-sunrise'] = (
    rays
    + z('path', '#e8735a', d='M52 124 A48 48 0 0 1 148 124Z')
    + dot(86, 100) + dot(114, 100) + cheeks(76, 124, 110, 6, 3.5)
    + s('path', d='M94 108 Q100 114 106 108', stroke_width=2.5)
    + z('ellipse', '#ffffff', cx=44, cy=52, rx=20, ry=9) + z('ellipse', '#ffffff', cx=160, cy=40, rx=18, ry=8)
    + z('rect', '#8fc7e8', x=26, y=124, width=148, height=52, rx=8)
    + thick('M78 136 L122 136', '#ffc94d', 8, 4) + thick('M86 148 L114 148', '#ffc94d', 8, 4)
    + thick('M94 160 L106 160', '#ffc94d', 8, 4)
    + s('path', d='M38 146 Q46 140 54 146 Q62 152 70 146', stroke_width=2.5)
    + s('path', d='M130 160 Q138 154 146 160 Q154 166 162 160', stroke_width=2.5)
)

# 2. kadomatsu
ITEMS['kadomatsu'] = (
    z('path', '#7cc4a0', d='M50 136 Q40 112 60 108 Q62 92 80 100 L84 134Z')
    + z('path', '#7cc4a0', d='M150 136 Q160 112 140 108 Q138 92 120 100 L116 134Z')
    + z('path', '#9ccf7a', d='M62 82 L86 68 L86 150 L62 150Z')
    + z('path', '#9ccf7a', d='M114 74 L138 60 L138 150 L114 150Z')
    + z('path', '#9ccf7a', d='M88 52 L112 36 L112 150 L88 150Z')
    + s('ellipse', '#f6e0c4', cx=74, cy=75, rx=11, ry=4, transform='rotate(-30 74 75)', stroke_width=2)
    + s('ellipse', '#f6e0c4', cx=126, cy=67, rx=11, ry=4, transform='rotate(-30 126 67)', stroke_width=2)
    + s('ellipse', '#f6e0c4', cx=100, cy=44, rx=13, ry=4, transform='rotate(-34 100 44)', stroke_width=2)
    + s('path', d='M64 112 Q74 116 84 112 M90 96 Q100 100 110 96 M116 108 Q126 112 136 108', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M46 146 Q40 128 58 126 Q66 114 82 124 Q100 116 118 124 Q134 114 142 126 Q160 128 154 146Z')
    + s('circle', '#f6a6b8', cx=60, cy=134, r=5, stroke_width=2) + s('circle', '#f6a6b8', cx=140, cy=132, r=5, stroke_width=2)
    + s('circle', '#ffffff', cx=96, cy=128, r=4.5, stroke_width=2)
    + z('rect', '#d9a66b', x=50, y=142, width=100, height=38, rx=6)
    + thick('M50 154 L150 154', '#9a6a3f', 8, 4) + thick('M50 168 L150 168', '#9a6a3f', 8, 4)
    + s('path', d='M64 142 L62 180 M80 142 L80 180 M100 142 L100 180 M120 142 L120 180 M136 142 L138 180', stroke_width=1.5)
)

# 3. kagami mochi
ITEMS['kagami-mochi'] = (
    sanbo(100, 146, 112)
    + z('path', '#ffffff', d='M52 146 L148 146 L140 160 L60 160Z')
    + s('path', '#e04b5a', d='M60 156 L140 156 L140 160 L60 160Z', stroke='none')
    + z('ellipse', '#f4f4f0', cx=100, cy=124, rx=52, ry=26)
    + z('ellipse', '#f4f4f0', cx=100, cy=92, rx=40, ry=21)
    + dot(88, 130) + dot(112, 130) + cheeks(76, 124, 139, 6, 3.5)
    + s('path', d='M95 138 Q100 143 105 138', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M102 52 Q114 36 130 44 Q118 56 102 52Z')
    + z('circle', '#f5b971', cx=100, cy=64, r=16)
    + s('path', d='M100 50 L102 46', stroke_width=3)
)

# 4. lucky bag
ITEMS['lucky-bag'] = (
    s('path', d='M70 80 Q70 50 86 50 Q100 50 100 80', stroke_width=9) + s('path', d='M70 80 Q70 50 86 50 Q100 50 100 80', stroke='#e04b5a', stroke_width=4)
    + z('rect', '#9ccf7a', x=104, y=52, width=34, height=30, rx=3) + s('rect', '#f5d58a', x=116, y=52, width=10, height=30, stroke_width=2)
    + z('rect', '#f6a6b8', x=62, y=62, width=22, height=24, rx=8)
    + s('path', d='M100 80 Q100 50 116 50 Q130 50 130 80', stroke_width=9) + s('path', d='M100 80 Q100 50 116 50 Q130 50 130 80', stroke='#e04b5a', stroke_width=4)
    + z('path', '#e04b5a', d='M50 78 L150 78 L158 180 L42 180Z')
    + z('circle', '#ffc94d', cx=100, cy=130, r=27)
    + ''.join(s('circle', '#ffffff', cx=round(100 + 10 * cos((a * 72 - 90) * pi / 180), 1), cy=round(130 + 10 * sin((a * 72 - 90) * pi / 180), 1), r=7.5, stroke_width=2) for a in range(5))
    + dot(100, 130, 3.5, '#ffc94d')
    + s('path', d='M166 56 L166 72 M158 64 L174 64 M30 92 L30 104 M24 98 L36 98 M168 104 L168 114 M163 109 L173 109', stroke_width=2.5)
)

# 5. setsubun (oni mask & beans)
beans = ''.join(s('circle', '#f5d58a', cx=x, cy=y, r=5.5, stroke_width=2) for x, y in
                ((124, 128), (136, 126), (148, 128), (160, 127), (130, 120), (144, 119), (156, 121), (138, 113), (150, 113)))
ITEMS['setsubun'] = (
    z('path', '#f5d58a', d='M50 64 L42 28 L70 50Z') + z('path', '#f5d58a', d='M106 50 L116 26 L124 64Z')
    + z('circle', '#e04b5a', cx=82, cy=90, r=44)
    + z('path', '#5b6b7a', d='M38 88 Q36 56 56 50 Q62 38 76 44 Q86 34 98 44 Q110 38 114 50 Q130 56 126 88 Q118 66 82 64 Q46 66 38 88Z')
    + s('path', d='M60 82 L74 88 M104 82 L90 88', stroke_width=3)
    + dot(68, 96) + dot(96, 96) + cheeks(56, 108, 108, 7, 4)
    + s('path', d='M70 112 Q82 124 94 112', stroke_width=3)
    + s('path', '#ffffff', d='M73 114 L76 121 L79 116Z', stroke_width=2) + s('path', '#ffffff', d='M85 116 L88 121 L91 114Z', stroke_width=2)
    + z('path', '#d9a66b', d='M162 136 L174 124 L174 166 L162 178Z')
    + z('rect', '#d9a66b', x=110, y=136, width=52, height=42, rx=2)
    + s('path', '#f6e0c4', d='M110 136 L122 124 L174 124 L162 136Z', stroke_width=2.5)
    + beans
    + s('circle', '#f5d58a', cx=40, cy=160, r=5.5, stroke_width=2) + s('circle', '#f5d58a', cx=58, cy=170, r=5.5, stroke_width=2)
    + s('circle', '#f5d58a', cx=80, cy=158, r=5.5, stroke_width=2)
)

# 6. valentine chocolate box
choc = ''
for x, y in ((78, 100), (122, 100), (86, 128), (114, 128)):
    choc += s('circle', '#9a6a3f', cx=x, cy=y, r=10, stroke_width=2.5) + s('path', d=f'M{x-5} {y-2} Q{x} {y-6} {x+5} {y-2}', stroke='#f6e0c4', stroke_width=2)
choc += s('path', '#8b6b4f', d=heart_d(100, 112, 22), stroke_width=2.5) + s('path', '#8b6b4f', d=heart_d(100, 148, 20), stroke_width=2.5)
ITEMS['valentine-chocolate'] = (
    z('path', '#f07a8a', d=heart_d(100, 110, 134))
    + s('path', '#f6e0c4', d=heart_d(100, 112, 100), stroke_width=2.5)
    + choc
    + z('path', '#e04b5a', d='M146 58 Q150 34 168 42 Q170 58 146 58Z') + z('path', '#e04b5a', d='M146 58 Q130 38 120 50 Q128 64 146 58Z')
    + z('path', '#e04b5a', d='M146 58 L156 80 L148 78 L144 84Z')
    + z('circle', '#e04b5a', cx=146, cy=58, r=6)
)

# 7. hinamatsuri
ITEMS['hinamatsuri'] = (
    z('rect', '#f5d58a', x=30, y=34, width=140, height=112, rx=3)
    + s('path', d='M65 34 L65 146 M100 34 L100 146 M135 34 L135 146', stroke_width=2)
    # 男雛
    + z('path', '#5b6b7a', d='M36 164 Q38 116 64 112 Q90 116 92 164Z')
    + s('path', '#ffffff', d='M56 114 L64 130 L72 114Z', stroke_width=2) + s('path', '#9ccf7a', d='M59 114 L64 124 L69 114Z', stroke_width=2)
    + s('rect', '#f6e0c4', x=60, y=126, width=8, height=26, rx=2, stroke_width=2)
    + z('path', '#2b2220', d='M54 74 Q52 50 66 46 Q72 52 74 74Z')
    + mini_face(64, 92, 20, '#2b2220')
    # 女雛
    + z('path', '#2b2220', d='M114 92 Q112 70 136 70 Q160 70 158 92 L162 126 L110 126Z')
    + z('path', '#f07a8a', d='M108 164 Q110 116 136 112 Q162 116 164 164Z')
    + s('path', '#ffffff', d='M128 114 L136 130 L144 114Z', stroke_width=2) + s('path', '#9ccf7a', d='M131 114 L136 124 L141 114Z', stroke_width=2)
    + z('path', '#f6a6b8', d='M140 150 L156 126 L166 136Z')
    + mini_face(136, 92, 20, '#2b2220')
    + s('path', '#ffc94d', d='M124 70 L128 62 L132 68 L136 60 L140 68 L144 62 L148 70Z', stroke_width=2)
    + z('rect', '#e04b5a', x=28, y=160, width=144, height=20, rx=3)
)

# 8. hanami
petals = ''.join(s('ellipse', '#f6a6b8', cx=x, cy=y, rx=4, ry=2.5, transform=f'rotate({r} {x} {y})', stroke_width=2)
                 for x, y, r in ((40, 120, 20), (150, 112, -30), (170, 132, 40), (130, 126, 10), (30, 150, -20)))
ITEMS['hanami'] = (
    z('path', '#8b6b4f', d='M58 156 Q66 124 62 84 L80 84 Q78 124 84 156Z')
    + s('path', d='M72 100 Q92 92 100 80', stroke_width=5)
    + z('path', '#f6a6b8', d='M28 76 Q22 50 48 44 Q54 22 84 26 Q104 10 126 26 Q154 22 156 50 Q176 66 156 86 Q144 100 118 92 Q98 104 78 92 Q40 100 28 76Z')
    + ''.join(s('circle', c, cx=x, cy=y, r=4, stroke_width=2) for x, y, c in
              ((52, 62, '#ffffff'), (80, 46, '#f07a8a'), (108, 40, '#ffffff'), (134, 52, '#f07a8a'), (144, 74, '#ffffff'), (98, 70, '#ffffff'), (66, 80, '#f07a8a'), (120, 76, '#f07a8a')))
    + petals
    + z('path', '#8fc7e8', d='M50 146 L174 146 L166 178 L36 178Z')
    + s('path', d='M92 146 L84 178 M134 146 L130 178', stroke='#ffffff', stroke_width=2)
    + z('rect', '#e8735a', x=60, y=140, width=44, height=26, rx=4)
    + s('rect', '#ffffff', x=65, y=145, width=16, height=16, rx=2, stroke_width=2)
    + s('circle', '#ffe27a', cx=88, cy=150, r=4.5, stroke_width=2) + s('circle', '#9ccf7a', cx=96, cy=157, r=4.5, stroke_width=2)
    + s('circle', '#e04b5a', cx=73, cy=153, r=2.5, stroke_width=1.5)
    + z('path', '#ffffff', d='M132 164 L142 138 Q146 132 150 138 L160 164Z')
    + s('rect', '#2b2220', x=137, y=152, width=18, height=12, stroke_width=2)
)

# 9. easter eggs in basket
ITEMS['easter-eggs'] = (
    thick('M50 112 Q50 34 100 34 Q150 34 150 112', '#d9a66b', 12, 6)
    + z('ellipse', '#f6a6b8', cx=70, cy=100, rx=16, ry=21)
    + s('path', d='M55 98 L62 92 L70 98 L78 92 L85 98', stroke_width=2.5)
    + z('ellipse', '#ffe27a', cx=130, cy=100, rx=16, ry=21)
    + s('path', d='M116 94 L144 94 M115 104 L145 104', stroke='#e8735a', stroke_width=3)
    + z('ellipse', '#8fc7e8', cx=100, cy=90, rx=17, ry=23)
    + dot(94, 82, 3.5, '#ffffff') + dot(106, 88, 3.5, '#ffffff') + dot(96, 98, 3.5, '#ffffff')
    + z('path', '#9ccf7a', d='M42 116 L48 104 L54 114 L60 104 L66 114 L74 104 L82 114 L90 106 L98 114 L106 104 L114 114 L122 104 L130 114 L138 104 L146 114 L152 104 L158 116Z')
    + z('path', '#d9a66b', d='M40 114 L160 114 L146 176 L54 176Z')
    + s('path', d='M44 132 L156 132 M48 150 L152 150 M80 114 L84 176 M120 114 L116 176', stroke='#9a6a3f', stroke_width=2.5)
    + z('ellipse', '#a98bd0', cx=166, cy=166, rx=12, ry=15)
    + s('path', d='M155 166 L177 166', stroke='#ffffff', stroke_width=3)
)

# 10. easter bunny with egg
ITEMS['easter-bunny'] = (
    z('ellipse', '#ffffff', cx=84, cy=50, rx=12, ry=28, transform='rotate(-12 84 50)')
    + z('ellipse', '#ffffff', cx=116, cy=50, rx=12, ry=28, transform='rotate(12 116 50)')
    + s('ellipse', '#f6a6b8', cx=84, cy=52, rx=5, ry=18, transform='rotate(-12 84 52)', stroke='none')
    + s('ellipse', '#f6a6b8', cx=116, cy=52, rx=5, ry=18, transform='rotate(12 116 52)', stroke='none')
    + z('ellipse', '#ffffff', cx=100, cy=146, rx=44, ry=34)
    + z('ellipse', '#ffffff', cx=72, cy=176, rx=14, ry=7) + z('ellipse', '#ffffff', cx=128, cy=176, rx=14, ry=7)
    + z('circle', '#ffffff', cx=100, cy=96, r=32)
    + dot(88, 94) + dot(112, 94) + cheeks(78, 122, 106, 6, 3.5)
    + s('ellipse', '#f07a8a', cx=100, cy=103, rx=3.5, ry=2.5, stroke_width=1.5)
    + s('path', d='M94 108 Q97 112 100 107 Q103 112 106 108', stroke_width=2.5)
    + z('ellipse', '#8fc7e8', cx=100, cy=150, rx=22, ry=27)
    + s('path', d='M80 146 L87 139 L94 146 L100 139 L106 146 L113 139 L120 146', stroke='#ffe27a', stroke_width=4)
    + dot(92, 162, 3, '#f6a6b8') + dot(108, 162, 3, '#f6a6b8') + dot(100, 128, 3, '#f6a6b8')
    + z('ellipse', '#ffffff', cx=78, cy=146, rx=9, ry=8) + z('ellipse', '#ffffff', cx=122, cy=146, rx=9, ry=8)
)


# 11. carnation bouquet
def carnation(cx, cy, r, color):
    pts = []
    for i in range(17):
        a = (180 + i * 180 / 16) * pi / 180
        rr = r if i % 2 == 0 else r * 0.8
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a) * 0.85:.1f}')
    d = 'M' + ' L'.join(pts) + f' Q{cx + r*0.7:.1f} {cy + r*0.35:.1f} {cx + r*0.35:.1f} {cy + r*0.45:.1f} L{cx - r*0.35:.1f} {cy + r*0.45:.1f} Q{cx - r*0.7:.1f} {cy + r*0.35:.1f} {pts[0]}Z'
    return (z('path', '#9ccf7a', d=f'M{cx-r*0.3:.1f} {cy+r*0.4:.1f} L{cx+r*0.3:.1f} {cy+r*0.4:.1f} L{cx+r*0.18:.1f} {cy+r*0.85:.1f} L{cx-r*0.18:.1f} {cy+r*0.85:.1f}Z')
            + z('path', color, d=d)
            + s('path', d=f'M{cx-r*0.55:.1f} {cy-r*0.1:.1f} L{cx-r*0.3:.1f} {cy-r*0.3:.1f} L{cx-r*0.1:.1f} {cy-r*0.1:.1f} L{cx+r*0.1:.1f} {cy-r*0.3:.1f} L{cx+r*0.3:.1f} {cy-r*0.1:.1f} L{cx+r*0.55:.1f} {cy-r*0.3:.1f}', stroke_width=2))


ITEMS['carnation'] = (
    s('path', d='M64 102 L94 150 M100 92 L100 150 M136 102 L106 150', stroke='#7cc4a0', stroke_width=6)
    + z('path', '#7cc4a0', d='M82 120 Q60 112 52 124 Q68 130 82 120Z') + z('path', '#7cc4a0', d='M118 120 Q140 112 148 124 Q132 130 118 120Z')
    + carnation(64, 84, 24, '#f6a6b8') + carnation(136, 84, 24, '#f07a8a') + carnation(100, 64, 30, '#e04b5a')
    + z('path', '#f6e0c4', d='M56 120 L144 120 L110 180 L90 180Z')
    + s('path', d='M78 120 L96 180 M122 120 L104 180', stroke_width=2)
    + z('path', '#f07a8a', d='M100 146 Q80 128 74 142 Q80 154 100 146Z') + z('path', '#f07a8a', d='M100 146 Q120 128 126 142 Q120 154 100 146Z')
    + z('circle', '#f07a8a', cx=100, cy=146, r=6)
)

# 12. father's day necktie gift
ITEMS['fathers-day'] = (
    z('rect', '#8fb3e0', x=28, y=72, width=66, height=18, rx=3, transform='rotate(-24 61 81)')
    + s('rect', '#ffc94d', x=54, y=72, width=14, height=18, transform='rotate(-24 61 81)', stroke_width=2.5)
    + z('path', '#e8735a', d='M94 62 L106 62 L122 128 L100 146 L78 128Z')
    + s('path', d='M88 92 L110 70 M84 114 L114 84 M86 130 L117 100', stroke='#f5d58a', stroke_width=4)
    + s('path', d='M94 62 L106 62 L122 128 L100 146 L78 128Z')
    + z('path', '#e8735a', d='M88 44 L112 44 L107 62 L93 62Z')
    + z('rect', '#8fb3e0', x=46, y=118, width=108, height=60, rx=3)
    + s('rect', '#ffc94d', x=92, y=118, width=16, height=60, stroke_width=2.5)
    + s('path', d='M150 52 L150 68 M142 60 L158 60 M164 82 L164 92 M159 87 L169 87', stroke_width=2.5)
    + s('path', '#f07a8a', d=heart_d(154, 106, 18), stroke_width=2.5)
)


# 13. koinobori
def carp(x0, y, ln, h, color, light):
    d = (f'M{x0} {y-h/2} Q{x0+ln*0.5} {y-h*0.75} {x0+ln*0.82} {y-h*0.28} L{x0+ln} {y-h*0.6} L{x0+ln*0.9} {y} '
         f'L{x0+ln} {y+h*0.6} L{x0+ln*0.82} {y+h*0.28} Q{x0+ln*0.5} {y+h*0.75} {x0} {y+h/2}Z')
    sc = ''.join(s('path', d=f'M{x0+ln*k:.1f} {y-h*0.25:.1f} Q{x0+ln*(k+0.07):.1f} {y:.1f} {x0+ln*k:.1f} {y+h*0.25:.1f}', stroke=light, stroke_width=3)
                 for k in (0.42, 0.55, 0.68))
    ex = x0 + ln * 0.17
    return (z('path', color, d=d) + sc
            + s('path', d=f'M{x0+ln*0.3:.1f} {y-h*0.42:.1f} Q{x0+ln*0.36:.1f} {y} {x0+ln*0.3:.1f} {y+h*0.42:.1f}', stroke_width=2.5)
            + s('ellipse', '#ffffff', cx=x0, cy=y, rx=4, ry=h / 2, stroke_width=2.5)
            + s('circle', '#ffffff', cx=ex, cy=y - h * 0.08, r=h * 0.2, stroke_width=2.5) + dot(ex + 1, y - h * 0.08, h * 0.09)
            + f'<ellipse cx="{ex+2:.1f}" cy="{y+h*0.25:.1f}" rx="{h*0.13:.1f}" ry="{h*0.08:.1f}" fill="{CH}" stroke="none"/>')


ITEMS['koinobori'] = (
    z('ellipse', '#ffffff', cx=150, cy=172, rx=22, ry=8)
    + thick('M38 30 L38 182', '#d9a66b', 9, 4.5)
    + z('circle', '#ffc94d', cx=38, cy=26, r=7)
    + carp(42, 54, 130, 36, '#5b6b7a', '#8fb3e0')
    + carp(42, 100, 116, 32, '#e8735a', '#f5d58a')
    + carp(42, 142, 100, 28, '#8fb3e0', '#ffffff')
)

# 14. tanabata
def strip(x, y, color, rot):
    return (s('path', d=f'M{x} {y} L{x} {y+8}', stroke_width=1.5)
            + z('rect', color, x=x - 6, y=y + 8, width=12, height=30, rx=1, transform=f'rotate({rot} {x} {y})'))


def leaf(x, y, rot, ln=26):
    return z('path', '#7cc4a0', d=f'M{x} {y} Q{x+ln/2} {y-8} {x+ln} {y} Q{x+ln/2} {y+8} {x} {y}Z', transform=f'rotate({rot} {x} {y})')


ITEMS['tanabata'] = (
    s('path', d='M86 62 Q120 48 156 50 M84 104 Q56 92 34 96 M82 132 Q120 118 158 116', stroke_width=3)
    + leaf(150, 50, -30) + leaf(156, 50, 20) + leaf(40, 96, 200) + leaf(34, 96, 150) + leaf(152, 116, -25) + leaf(158, 116, 25)
    + leaf(100, 32, -60, 22) + leaf(98, 30, -120, 22)
    + thick('M78 182 Q84 110 98 30', '#9ccf7a', 14, 8)
    + s('path', d='M80 156 L88 156 M84 112 L92 112 M90 72 L97 72', stroke_width=2.5)
    + strip(110, 56, '#f6a6b8', 4) + strip(134, 51, '#8fc7e8', -4)
    + strip(64, 96, '#ffe27a', -4) + strip(44, 96, '#a98bd0', 4)
    + strip(108, 125, '#9ccf7a', 4) + strip(132, 120, '#f07a8a', -4)
    + s('path', '#ffe27a', d='M164 70 L167 78 L175 79 L169 84 L171 92 L164 88 L157 92 L159 84 L153 79 L161 78Z', stroke_width=2)
    + s('path', '#ffe27a', d='M40 46 L42 51 L47 52 L43 55 L44 60 L40 57 L36 60 L37 55 L33 52 L38 51Z', stroke_width=2)
)

# 15. yukata
ITEMS['yukata'] = (
    z('circle', '#2b2220', cx=126, cy=40, r=13)
    + z('path', '#8fb3e0', d='M60 182 Q62 112 100 106 Q138 112 140 182Z')
    + s('path', d='M88 107 L100 126 L114 107 M100 126 L84 182', stroke_width=3)
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=5, stroke_width=2) + dot(x, y, 2, '#f07a8a') for x, y in ((74, 162), (120, 168), (104, 122)))
    + z('rect', '#ffc94d', x=62, y=134, width=76, height=16, rx=2)
    + s('path', d='M62 142 L138 142', stroke='#e8735a', stroke_width=2)
    + s('path', d='M154 122 L146 132', stroke='#8b6b4f', stroke_width=4)
    + z('circle', '#f07a8a', cx=160, cy=104, r=20)
    + s('path', d='M160 104 L148 94 M160 104 L160 86 M160 104 L172 94', stroke='#ffffff', stroke_width=2.5)
    + z('path', '#8fb3e0', d='M126 112 Q150 116 148 136 L130 140Z')
    + z('circle', '#ffd9b8', cx=146, cy=132, r=8)
    + face(100, 72, '#ffd9b8', '#2b2220', 'smile')
    + s('circle', '#f07a8a', cx=116, cy=44, r=6, stroke_width=2) + dot(116, 44, 2, '#ffe27a')
)


# 16. summer festival lanterns
def lantern(cx, cy, rx, ry, color, ribs=True):
    o = s('path', d=f'M{cx} {cy-ry-14} L{cx} {cy-ry}', stroke_width=2.5)
    o += z('ellipse', color, cx=cx, cy=cy, rx=rx, ry=ry)
    if ribs:
        o += ''.join(s('path', d=f'M{cx-rx*w:.1f} {cy+k} Q{cx} {cy+k+5} {cx+rx*w:.1f} {cy+k}', stroke_width=1.8)
                     for k, w in ((-ry * 0.55, 0.82), (ry * 0.55, 0.82)))
    o += z('rect', '#5b6b7a', x=cx - rx * 0.5, y=cy - ry - 4, width=rx, height=8, rx=2)
    o += z('rect', '#5b6b7a', x=cx - rx * 0.5, y=cy + ry - 4, width=rx, height=8, rx=2)
    return o


ITEMS['summer-festival'] = (
    s('path', d='M22 40 Q100 76 178 40', stroke_width=3)
    + lantern(52, 88, 22, 26, '#f4f4f0') + lantern(148, 88, 22, 26, '#f4f4f0')
    + lantern(100, 100, 28, 32, '#e04b5a', ribs=False)
    + s('path', d='M74 82 Q100 87 126 82 M74 118 Q100 123 126 118', stroke_width=1.8)
    + dot(90, 98) + dot(110, 98) + cheeks(82, 118, 106, 5, 3) + s('path', d='M96 106 Q100 110 104 106', stroke_width=2.5)
    + z('rect', '#d9a66b', x=34, y=164, width=132, height=14, rx=2)
    + z('path', '#ffffff', d='M30 146 L170 146 L170 160 Q160 168 150 160 Q140 168 130 160 Q120 168 110 160 Q100 168 90 160 Q80 168 70 160 Q60 168 50 160 Q40 168 30 160Z')
    + ''.join(s('path', '#e04b5a', d=f'M{x} 146 L{x+20} 146 L{x+20} 160 Q{x+10} 168 {x} 160Z', stroke_width=2.5) for x in (30, 70, 110, 150))
)

# 17. bon dance
lan = ''
for t in (0.25, 0.5, 0.75):
    for side in (-1, 1):
        x = 100 + side * 72 * t
        y = 26 + 64 * t + 6 * sin(t * pi)
        lan += s('ellipse', '#e04b5a' if t != 0.5 else '#ffffff', cx=round(x, 1), cy=round(y + 7, 1), rx=6, ry=8, stroke_width=2)
ITEMS['bon-dance'] = (
    s('path', d='M100 26 Q66 64 28 92 M100 26 Q134 64 172 92', stroke_width=2.5) + lan
    + s('path', d='M100 26 L100 70', stroke_width=3)
    + z('path', '#e8735a', d='M80 74 Q100 68 120 74 L120 104 Q100 110 80 104Z')
    + z('ellipse', '#f6e0c4', cx=80, cy=89, rx=6, ry=15) + z('ellipse', '#f6e0c4', cx=120, cy=89, rx=6, ry=15)
    + s('path', d='M88 72 L72 56 M112 72 L128 56', stroke='#8b6b4f', stroke_width=4)
    + z('rect', '#d9a66b', x=48, y=106, width=104, height=10, rx=2)
    + z('rect', '#ffffff', x=52, y=116, width=96, height=24)
    + ''.join(s('rect', '#e04b5a', x=x, y=116, width=12, height=24, stroke='none') for x in (52, 76, 100, 124))
    + s('rect', x=52, y=116, width=96, height=24)
    + z('rect', '#d9a66b', x=58, y=140, width=10, height=38) + z('rect', '#d9a66b', x=132, y=140, width=10, height=38)
    + s('path', d='M68 146 L132 174 M68 174 L132 146', stroke='#8b6b4f', stroke_width=3)
    # dancers
    + z('path', '#8fb3e0', d='M22 180 Q24 150 38 148 Q52 150 54 180Z') + s('path', d='M28 156 L16 134 M48 156 L58 140', stroke_width=4)
    + mini_face(38, 134, 13, '#2b2220')
    + z('path', '#f6a6b8', d='M146 180 Q148 150 162 148 Q176 150 178 180Z') + s('path', d='M152 156 L142 140 M172 156 L184 134', stroke_width=4)
    + mini_face(162, 134, 13, '#5a4033')
)

# 18. moon viewing
dango = ''.join(z('circle', '#f4f4f0', cx=x, cy=y, r=12) for x, y in
                ((100, 132), (124, 132), (148, 132), (112, 112), (136, 112), (124, 92)))
plume = lambda x, y, r: z('path', '#f6e0c4', d=f'M{x} {y} Q{x-10} {y-18} {x+r*0.3:.1f} {y-r:.1f} Q{x+12} {y-18} {x} {y}Z')
ITEMS['moon-viewing'] = (
    z('circle', '#ffe27a', cx=64, cy=60, r=34)
    + s('circle', '#f5d58a', cx=50, cy=48, r=5, stroke='none') + s('circle', '#f5d58a', cx=80, cy=76, r=4, stroke='none')
    + dot(54, 62, 3) + dot(74, 62, 3) + cheeks(46, 82, 70, 5, 3) + s('path', d='M60 70 Q64 74 68 70', stroke_width=2.5)
    + s('path', d='M42 180 Q40 130 30 96 M48 180 Q52 130 62 104 M54 180 Q66 140 84 122', stroke='#9ccf7a', stroke_width=4)
    + plume(30, 112, 34) + plume(62, 118, 30) + plume(84, 134, 28)
    + s('path', d='M150 34 L150 46 M144 40 L156 40 M174 62 L174 70 M170 66 L178 66', stroke_width=2.5)
    + sanbo(124, 144, 90)
    + dango
)

# 19. autumn harvest basket
grapes = ''.join(s('circle', '#a98bd0', cx=x, cy=y, r=8, stroke_width=2.5) for x, y in
                 ((120, 68), (136, 68), (152, 70), (128, 82), (144, 84), (136, 98)))
ITEMS['harvest'] = (
    z('path', '#ffe27a', d='M150 108 Q148 56 170 40 Q180 64 166 110Z')
    + s('path', d='M156 92 L168 84 M156 76 L168 66 M160 60 L170 52', stroke='#f5b971', stroke_width=3)
    + z('path', '#9ccf7a', d='M150 112 Q140 70 152 56 Q158 84 166 112Z')
    + s('path', d='M134 60 Q136 50 144 46', stroke_width=3) + grapes
    + z('path', '#9ccf7a', d='M136 58 Q146 44 158 52 Q148 62 136 58Z')
    + s('path', d='M64 74 Q64 64 72 60', stroke='#8b6b4f', stroke_width=5)
    + z('ellipse', '#f5b971', cx=68, cy=96, rx=32, ry=24)
    + s('path', d='M52 76 Q44 96 54 116 M84 76 Q92 96 82 116 M68 72 L68 120', stroke_width=2.5)
    + z('circle', '#e04b5a', cx=108, cy=102, r=16)
    + s('path', d='M108 88 L110 80', stroke_width=3) + z('path', '#9ccf7a', d='M110 82 Q118 72 126 78 Q118 86 110 82Z')
    + z('path', '#d9a66b', d='M36 116 L164 116 L150 178 L50 178Z')
    + s('path', d='M40 136 L160 136 M45 156 L155 156', stroke='#9a6a3f', stroke_width=2.5)
    + s('path', d='M70 116 L76 178 M100 116 L100 178 M130 116 L124 178', stroke='#9a6a3f', stroke_width=2.5)
    + z('rect', '#d9a66b', x=30, y=108, width=140, height=12, rx=6)
    + z('path', '#e8735a', d='M28 170 Q26 150 44 146 Q46 166 28 170Z') + z('path', '#f5b971', d='M172 170 Q174 150 156 148 Q156 166 172 170Z')
)

# 20. thanksgiving turkey
ITEMS['thanksgiving'] = (
    z('ellipse', '#f4f4f0', cx=100, cy=152, rx=76, ry=24)
    + z('circle', '#9ccf7a', cx=40, cy=146, r=10) + z('circle', '#9ccf7a', cx=160, cy=146, r=10)
    + z('ellipse', '#d9a66b', cx=100, cy=118, rx=58, ry=36)
    + s('path', '#f5d58a', d='M76 96 Q96 86 120 92 Q100 96 82 104Z', stroke='none')
    + z('ellipse', '#d9a66b', cx=66, cy=112, rx=15, ry=24, transform='rotate(-35 66 112)')
    + z('ellipse', '#d9a66b', cx=134, cy=112, rx=15, ry=24, transform='rotate(35 134 112)')
    + s('path', d='M54 98 L44 84', stroke_width=11) + s('path', d='M54 98 L44 84', stroke='#ffffff', stroke_width=5)
    + s('path', d='M146 98 L156 84', stroke_width=11) + s('path', d='M146 98 L156 84', stroke='#ffffff', stroke_width=5)
    + s('circle', '#ffffff', cx=38, cy=80, r=5, stroke_width=2.5) + s('circle', '#ffffff', cx=46, cy=76, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=162, cy=80, r=5, stroke_width=2.5) + s('circle', '#ffffff', cx=154, cy=76, r=5, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=56, cy=156, r=6, stroke_width=2.5) + s('circle', '#e04b5a', cx=144, cy=158, r=6, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=100, cy=164, r=6, stroke_width=2.5)
    + s('path', '#ffe27a', d='M72 160 Q80 152 88 160Z', stroke_width=2.5) + s('path', '#ffe27a', d='M112 160 Q120 152 128 160Z', stroke_width=2.5)
)
