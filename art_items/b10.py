from math import sin, cos, pi, sqrt
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def star_d(cx, cy, R, r, rot=-90):
    pts = []
    for i in range(10):
        a = (rot + i * 36) * pi / 180
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


# 1. christmas tree
ITEMS['christmas-tree'] = (
    z('rect', '#8b6b4f', x=90, y=150, width=20, height=26, rx=3)
    + z('path', '#7cc4a0', d='M48 156 Q100 166 152 156 L118 112 L82 112Z')
    + z('path', '#7cc4a0', d='M58 124 Q100 134 142 124 L114 82 L86 82Z')
    + z('path', '#7cc4a0', d='M68 92 Q100 100 132 92 L100 48Z')
    + s('path', d='M66 140 Q100 150 132 134', stroke='#f5d58a', stroke_width=3)
    + s('path', d='M76 108 Q100 116 124 104', stroke='#f5d58a', stroke_width=3)
    + s('circle', '#e04b5a', cx=76, cy=150, r=6, stroke_width=2.5)
    + s('circle', '#8fb3e0', cx=118, cy=146, r=6, stroke_width=2.5)
    + s('circle', '#ffc94d', cx=96, cy=124, r=5.5, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=124, cy=118, r=5.5, stroke_width=2.5)
    + s('circle', '#8fb3e0', cx=84, cy=96, r=5, stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=110, cy=82, r=5, stroke_width=2.5)
    + z('path', '#ffe27a', d=star_d(100, 40, 17, 7.5))
    + s('path', d='M36 180 L164 180', stroke_width=2.5)
)

# 2. halloween pumpkin
ITEMS['halloween-pumpkin'] = (
    z('path', '#9ccf7a', d='M96 62 Q94 46 104 36 L112 42 Q104 50 106 62Z')
    + z('path', '#9ccf7a', d='M108 50 Q128 36 140 50 Q124 58 108 50Z')
    + z('ellipse', '#f5b971', cx=100, cy=120, rx=66, ry=56)
    + s('path', d='M78 68 Q56 120 80 174')
    + s('path', d='M122 68 Q144 120 120 174')
    + s('path', '#3b2f2a', d='M68 112 L80 94 L92 112Z', stroke_width=2.5)
    + s('path', '#3b2f2a', d='M108 112 L120 94 L132 112Z', stroke_width=2.5)
    + cheeks(62, 138, 126, 8, 5)
    + s('path', '#3b2f2a', d='M72 132 Q100 162 128 132 Q114 140 108 138 L104 146 L96 146 L92 138 Q86 140 72 132Z', stroke_width=2.5)
)

# 3. fireworks
def burst(cx, cy, R, color, n=10, rot=0):
    o = ''
    for i in range(n):
        a = (rot + i * 360 / n) * pi / 180
        x1, y1 = cx + R * 0.35 * cos(a), cy + R * 0.35 * sin(a)
        x2, y2 = cx + R * 0.85 * cos(a), cy + R * 0.85 * sin(a)
        o += thick(f'M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}', color, 8, 4)
        o += s('circle', color, cx=round(cx + R * cos(a), 1), cy=round(cy + R * sin(a), 1), r=3.2, stroke_width=2)
    return o + z('circle', color, cx=cx, cy=cy, r=R * 0.18)


ITEMS['fireworks'] = (
    burst(82, 78, 50, '#f07a8a', 12)
    + burst(144, 116, 34, '#8fc7e8', 10, 18)
    + burst(64, 148, 26, '#ffc94d', 8, 22)
    + dot(150, 40, 2.5, '#ffc94d') + dot(170, 64, 2.5, '#9ccf7a') + dot(34, 108, 2.5, '#8fc7e8')
    + dot(112, 170, 2.5, '#f6a6b8')
)

# 4. party popper
ITEMS['party-popper'] = (
    thick('M104 96 Q118 70 108 52 Q100 38 116 30', '#8fc7e8', 9, 5)
    + thick('M108 102 Q136 92 146 72 Q154 56 172 60', '#f6a6b8', 9, 5)
    + thick('M112 110 Q140 116 156 134 Q166 146 178 138', '#9ccf7a', 9, 5)
    + z('path', '#f5d58a', d='M36 176 L92 86 Q112 92 122 120Z')
    + s('path', d='M54 146 L104 106')
    + s('path', d='M70 120 L96 98')
    + s('path', '#e8735a', d='M57 141 L102 104 Q108 108 110 114 L48 156Z', stroke_width=2.5)
    + s('rect', '#ffc94d', x=136, y=36, width=9, height=9, rx=1.5, stroke_width=2, transform='rotate(25 140 40)')
    + s('rect', '#7cc4b0', x=150, y=94, width=9, height=9, rx=1.5, stroke_width=2, transform='rotate(-20 154 98)')
    + s('rect', '#f07a8a', x=84, y=40, width=9, height=9, rx=1.5, stroke_width=2, transform='rotate(40 88 44)')
    + s('rect', '#8fb3e0', x=170, y=104, width=8, height=8, rx=1.5, stroke_width=2, transform='rotate(15 174 108)')
    + s('circle', '#e04b5a', cx=132, cy=58, r=4, stroke_width=2)
    + s('circle', '#ffc94d', cx=162, cy=40, r=4, stroke_width=2)
    + s('circle', '#9ccf7a', cx=126, cy=136, r=4, stroke_width=2)
    + s('circle', '#f6a6b8', cx=88, cy=64, r=3.5, stroke_width=2)
)

# 5. heart balloons
def heart_d(cx, cy, k):
    """中心(cx,cy)、大きさk(=1で幅約56)のハート"""
    def p(x, y): return f'{cx + x * k:.1f} {cy + y * k:.1f}'
    return (f'M{p(0, 26)} C{p(-20, 10)} {p(-30, -2)} {p(-26, -14)} C{p(-22, -28)} {p(-4, -28)} {p(0, -14)} '
            f'C{p(4, -28)} {p(22, -28)} {p(26, -14)} C{p(30, -2)} {p(20, 10)} {p(0, 26)}Z')


ITEMS['heart-balloons'] = (
    s('path', d='M66 96 Q78 130 100 158', stroke_width=2)
    + s('path', d='M136 90 Q124 128 100 158', stroke_width=2)
    + s('path', d='M102 72 Q96 120 100 158', stroke_width=2)
    + s('path', d='M100 158 Q92 170 100 182', stroke_width=2)
    + z('path', '#f6a6b8', d=heart_d(64, 70, 1.15))
    + z('path', '#f07a8a', d=heart_d(138, 64, 1.15))
    + z('path', '#e04b5a', d=heart_d(102, 46, 1.25))
    + s('path', '#ffffff', d='M50 58 Q50 50 58 50', stroke='#ffffff', stroke_width=4)
    + s('path', '#ffffff', d='M124 52 Q124 44 132 44', stroke='#ffffff', stroke_width=4)
    + s('path', '#ffffff', d='M86 32 Q86 24 94 24', stroke='#ffffff', stroke_width=4)
    + z('path', '#ffc94d', d='M100 158 L88 150 L88 166Z')
    + z('path', '#ffc94d', d='M100 158 L112 150 L112 166Z')
)

# 6. soccer ball
cx, cy = 116, 100
pent = star_d(cx, cy, 20, 20, -90)
pent_pts = []
for i in range(5):
    a = (-90 + i * 72) * pi / 180
    pent_pts.append((cx + 20 * cos(a), cy + 20 * sin(a)))
spokes = ''
outer = ''
for i, (px, py) in enumerate(pent_pts):
    a = (-90 + i * 72) * pi / 180
    ex, ey = cx + 40 * cos(a), cy + 40 * sin(a)
    spokes += f'M{px:.1f} {py:.1f} L{ex:.1f} {ey:.1f} '
    # 外周のパッチ（円周に沿う部分五角形）
    a1, a2 = a - 0.32, a + 0.32
    q1 = (cx + 47 * cos(a1), cy + 47 * sin(a1))
    q2 = (cx + 47 * cos(a2), cy + 47 * sin(a2))
    e1 = (cx + 56 * cos(a - 0.42), cy + 56 * sin(a - 0.42))
    e2 = (cx + 56 * cos(a + 0.42), cy + 56 * sin(a + 0.42))
    outer += s('path', '#5b6b7a', d=(f'M{ex:.1f} {ey:.1f} L{q1[0]:.1f} {q1[1]:.1f} L{e1[0]:.1f} {e1[1]:.1f} '
                                      f'A56 56 0 0 1 {e2[0]:.1f} {e2[1]:.1f} L{q2[0]:.1f} {q2[1]:.1f}Z'), stroke_width=2.5)
ITEMS['soccer-ball'] = (
    z('circle', '#ffffff', cx=cx, cy=cy, r=56)
    + s('path', d=spokes, stroke_width=2.5)
    + outer
    + s('path', '#5b6b7a', d=pent, stroke_width=2.5)
    + s('circle', cx=cx, cy=cy, r=56)
    + s('path', d='M28 78 L50 78 M22 100 L48 100 M30 122 L52 122', stroke_width=3)
    + s('path', d='M70 176 Q116 184 162 176', stroke_width=2.5)
)

# 7. basketball
ITEMS['basketball'] = (
    z('circle', '#f5b971', cx=100, cy=100, r=64)
    + s('path', d='M100 36 L100 164')
    + s('path', d='M36 100 L164 100')
    + s('path', d='M54 55 Q80 100 54 145')
    + s('path', d='M146 55 Q120 100 146 145')
    + s('path', '#ffffff', d='M62 70 Q70 56 84 50', stroke='#ffffff', stroke_width=4)
)

# 8. person running (skin #c68642)
SK = '#c68642'
ITEMS['person-running'] = (
    s('path', d='M22 92 L40 92 M18 112 L38 112 M24 132 L42 132', stroke_width=3)
    # 後ろ脚
    + thick('M92 146 Q76 160 60 154', SK, 11, 6)
    + z('ellipse', '#e8735a', cx=54, cy=154, rx=11, ry=7, transform='rotate(-25 54 154)')
    # 前脚
    + thick('M112 146 Q124 158 122 174', SK, 11, 6)
    + z('ellipse', '#e8735a', cx=130, cy=176, rx=12, ry=7)
    # 短パン
    + z('path', '#5b6b7a', d='M84 136 L126 134 L128 152 L112 154 L104 146 L96 156 L82 152Z')
    # 後ろ腕
    + thick('M90 112 Q74 116 70 128', SK, 10, 5)
    + z('circle', SK, cx=68, cy=130, r=6)
    # 胴体（シャツ）
    + z('path', '#7cc4b0', d='M82 140 Q78 108 102 102 Q128 104 128 140Z')
    + s('path', d='M88 116 L120 116', stroke='#ffffff', stroke_width=3)
    # 前腕
    + thick('M118 112 Q134 120 140 104', SK, 10, 5)
    + z('circle', SK, cx=142, cy=100, r=6)
    + face(106, 66, SK, '#2b2220', 'open')
    + s('path', '#f07a8a', d='M73 54 Q106 38 139 54 L139 60 Q106 46 73 60Z', stroke_width=2.5)
)

# 9. tennis racket and ball
R = 'rotate(-35 92 96)'
hx, hy, rx, ry = 92, 68, 26, 36
strings = ''
for dx in range(-20, 21, 8):
    h = ry * sqrt(max(0, 1 - (dx / rx) ** 2))
    strings += f'M{hx + dx} {hy - h:.1f} L{hx + dx} {hy + h:.1f} '
for dy in range(-28, 29, 8):
    w = rx * sqrt(max(0, 1 - (dy / ry) ** 2))
    strings += f'M{hx - w:.1f} {hy + dy} L{hx + w:.1f} {hy + dy} '
ITEMS['tennis-racket'] = (
    z('path', '#e8735a', d='M84 108 L80 124 L104 124 L100 108Z', transform=R)
    + z('rect', '#5b6b7a', x=84, y=122, width=16, height=52, rx=6, transform=R)
    + s('path', d='M84 138 L100 134 M84 150 L100 146 M84 162 L100 158', stroke_width=2, transform=R)
    + z('ellipse', '#e8735a', cx=hx, cy=hy, rx=rx + 8, ry=ry + 8, transform=R)
    + s('ellipse', '#ffffff', cx=hx, cy=hy, rx=rx, ry=ry, stroke_width=2.5, transform=R)
    + s('path', d=strings, stroke='#b9a99c', stroke_width=1.6, transform=R)
    + s('ellipse', cx=hx, cy=hy, rx=rx, ry=ry, stroke_width=2.5, transform=R)
    + z('circle', '#ffe27a', cx=56, cy=150, r=20)
    + s('path', d='M38 142 Q52 148 50 168', stroke='#ffffff', stroke_width=3)
    + s('path', d='M62 131 Q60 150 75 156', stroke='#ffffff', stroke_width=3)
)

# 10. trophy
ITEMS['trophy'] = (
    s('path', d='M62 58 Q34 58 38 82 Q42 102 70 104', stroke_width=11)
    + s('path', d='M62 58 Q34 58 38 82 Q42 102 70 104', stroke='#ffc94d', stroke_width=5)
    + s('path', d='M138 58 Q166 58 162 82 Q158 102 130 104', stroke_width=11)
    + s('path', d='M138 58 Q166 58 162 82 Q158 102 130 104', stroke='#ffc94d', stroke_width=5)
    + z('rect', '#ffc94d', x=90, y=118, width=20, height=28, rx=2)
    + z('path', '#ffc94d', d='M56 44 L144 44 Q146 112 100 124 Q54 112 56 44Z')
    + z('rect', '#ffc94d', x=50, y=36, width=100, height=14, rx=4)
    + z('path', '#ffffff', d=star_d(100, 80, 20, 9))
    + s('path', '#ffffff', d='M68 58 Q68 86 80 102', stroke='#ffffff', stroke_width=4)
    + z('rect', '#ffc94d', x=74, y=144, width=52, height=10, rx=3)
    + z('rect', '#8b6b4f', x=62, y=152, width=76, height=26, rx=4)
    + s('rect', '#f5d58a', x=80, y=158, width=40, height=13, rx=2, stroke_width=2.5)
)
