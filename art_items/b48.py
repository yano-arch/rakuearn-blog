from math import sin, cos, pi
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
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def pine(cx, base, h, w, color='#7cc4a0'):
    return (s('rect', '#8b6b4f', x=cx - 3, y=base - 8, width=6, height=8, stroke_width=2.5)
            + z('path', color, d=f'M{cx - w / 2} {base - 8} L{cx} {base - 8 - h} L{cx + w / 2} {base - 8}Z'))


def small_head(cx, cy, hair='#5a4033', r=11):
    return (z('circle', '#ffd9b8', cx=cx, cy=cy, r=r)
            + s('path', hair, d=f'M{cx - r} {cy - 1} Q{cx - r} {cy - r - 1} {cx} {cy - r} Q{cx + r} {cy - r - 1} {cx + r} {cy - 1} Q{cx} {cy - r * 0.45} {cx - r} {cy - 1}Z', stroke_width=2.5)
            + dot(cx - r * 0.38, cy + 2, 2) + dot(cx + r * 0.38, cy + 2, 2)
            + cheeks(cx - r * 0.62, cx + r * 0.62, cy + r * 0.5, 2.6, 1.6))


def lantern(cx, y0, k, glow=True):
    def p(v):
        return round(v * k, 1)
    o = s('path', d=f'M{cx - p(16)} {y0 + p(20)} Q{cx} {y0 - p(6)} {cx + p(16)} {y0 + p(20)}', stroke_width=max(2, 3 * min(k, 1)))
    o += z('path', '#5b6b7a', d=f'M{cx - p(24)} {y0 + p(34)} L{cx - p(14)} {y0 + p(18)} L{cx + p(14)} {y0 + p(18)} L{cx + p(24)} {y0 + p(34)}Z')
    o += z('rect', '#ffe27a', x=cx - p(20), y=y0 + p(34), width=p(40), height=p(56), rx=p(6))
    o += s('path', '#f5b971', d=f'M{cx} {y0 + p(48)} Q{cx - p(10)} {y0 + p(66)} {cx} {y0 + p(76)} Q{cx + p(10)} {y0 + p(66)} {cx} {y0 + p(48)}Z', stroke_width=max(2, 2.5 * min(k, 1)))
    o += z('rect', '#5b6b7a', x=cx - p(26), y=y0 + p(90), width=p(52), height=p(14), rx=p(4))
    if glow:
        for (x1, y1, x2, y2) in ((-32, 50, -42, 44), (-34, 66, -46, 66), (-32, 82, -42, 88),
                                 (32, 50, 42, 44), (34, 66, 46, 66), (32, 82, 42, 88)):
            o += s('path', d=f'M{cx + p(x1)} {y0 + p(y1)} L{cx + p(x2)} {y0 + p(y2)}', stroke='#f5b971', stroke_width=3)
    return o


def cloud(cx, cy, k=1.0):
    return z('path', '#ffffff', d=f'M{cx - 22 * k} {cy + 8 * k} Q{cx - 26 * k} {cy - 4 * k} {cx - 12 * k} {cy - 4 * k} Q{cx - 8 * k} {cy - 16 * k} {cx + 4 * k} {cy - 10 * k} Q{cx + 20 * k} {cy - 14 * k} {cx + 20 * k} {cy} Q{cx + 28 * k} {cy + 4 * k} {cx + 22 * k} {cy + 8 * k}Z')


def fish(cx, cy, color, k=1.0, left=False):
    sgn = -1 if left else 1
    o = z('path', color, d=f'M{cx - sgn * 12 * k} {cy} L{cx - sgn * 24 * k} {cy - 9 * k} L{cx - sgn * 24 * k} {cy + 9 * k}Z')
    o += z('ellipse', color, cx=cx, cy=cy, rx=16 * k, ry=10 * k)
    o += dot(cx + sgn * 8 * k, cy - 2 * k, 2.2)
    return o


def cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t * t, t ** 3
        pts.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return pts


# 1. map with route
ITEMS['map-route'] = (
    z('path', '#f6e0c4', d='M28 52 L74 38 L74 160 L28 174Z')
    + z('path', '#f5d58a', d='M74 38 L126 52 L126 174 L74 160Z')
    + z('path', '#f6e0c4', d='M126 52 L172 38 L172 160 L126 174Z')
    + s('path', '#9ccf7a', d='M36 70 Q52 60 64 70 Q66 88 50 90 Q36 88 36 70Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M90 120 Q104 108 116 118 Q118 134 102 136 Q88 134 90 120Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M134 130 Q150 122 162 132 Q162 150 146 150 Q132 146 134 130Z', stroke_width=2.5)
    + s('path', d='M46 150 Q70 150 80 124 Q90 96 120 100 Q146 104 148 84', stroke_width=4, stroke_dasharray='1 9')
    + z('circle', '#7cc4b0', cx=44, cy=150, r=7)
    + z('path', '#e04b5a', d='M148 86 Q132 66 134 56 A14 14 0 1 1 162 56 Q164 66 148 86Z')
    + s('circle', '#ffffff', cx=148, cy=56, r=5, stroke_width=2.5)
)

# 2. tent under the stars
ITEMS['tent-stars'] = (
    z('rect', '#5b6b7a', x=24, y=24, width=152, height=152, rx=22)
    + s('path', '#9ccf7a', d='M24 142 Q100 128 176 142 L176 154 Q176 176 154 176 L46 176 Q24 176 24 154Z')
    + s('path', '#ffe27a', d='M146 40 A16 16 0 1 0 156 70 A13 13 0 1 1 146 40Z', stroke_width=2.5)
    + s('path', '#ffe27a', d=star_d(48, 48, 7, 3), stroke_width=2)
    + s('path', '#ffe27a', d=star_d(92, 38, 5, 2.2), stroke_width=2)
    + s('path', '#ffe27a', d=star_d(118, 64, 6, 2.6), stroke_width=2)
    + s('path', '#ffe27a', d=star_d(40, 96, 5, 2.2), stroke_width=2)
    + dot(70, 70, 2, '#ffe27a') + dot(160, 96, 2, '#ffe27a') + dot(140, 116, 2, '#ffe27a')
    + s('path', d='M100 76 L100 64', stroke_width=3)
    + z('path', '#e8735a', d='M46 160 L100 76 L154 160Z')
    + s('path', '#f5d58a', d='M100 102 L84 160 L116 160Z', stroke_width=2.5)
    + s('path', d='M100 76 L100 102', stroke_width=2.5)
)

# 3. mountain cabin
ITEMS['mountain-cabin'] = (
    z('path', '#b9a99c', d='M20 146 L74 58 L128 146Z')
    + s('path', '#ffffff', d='M61 79 L74 58 L87 79 L80 74 L74 82 L68 74Z', stroke_width=2.5)
    + z('path', '#c9d3db', d='M82 146 L134 40 L180 146Z')
    + s('path', '#ffffff', d='M120 68 L134 40 L148 68 L140 62 L134 72 L127 62Z', stroke_width=2.5)
    + pine(36, 176, 40, 26) + pine(164, 176, 46, 28)
    + s('rect', '#b9a99c', x=116, y=84, width=12, height=24)
    + z('rect', '#d9a66b', x=62, y=116, width=76, height=60)
    + s('path', d='M62 132 L80 132 M120 132 L138 132 M62 148 L80 148 M120 148 L138 148 M62 162 L80 162 M120 162 L138 162', stroke_width=2)
    + z('path', '#e8735a', d='M50 122 L100 82 L150 122Z')
    + z('rect', '#8b6b4f', x=86, y=140, width=26, height=36, rx=3)
    + z('rect', '#ffe27a', x=68, y=128, width=14, height=14, rx=2)
    + z('rect', '#ffe27a', x=118, y=128, width=14, height=14, rx=2)
    + s('path', d='M24 178 L176 178', stroke_width=2.5)
)

# 4. view from an airplane window
ITEMS['airplane-window'] = (
    z('rect', '#f4f4f0', x=46, y=24, width=108, height=154, rx=50)
    + z('rect', '#8fc7e8', x=60, y=40, width=80, height=122, rx=38)
    + cloud(92, 72, 0.8) + cloud(110, 138, 0.7)
    + z('path', '#c9d3db', d='M140 98 L80 128 L86 136 L140 118Z')
    + s('rect', '#c9d3db', x=88, y=166, width=24, height=5, rx=2.5, stroke_width=2)
)

# 5. airport check-in counter
ITEMS['check-in-counter'] = (
    z('rect', '#8fb3e0', x=36, y=22, width=128, height=26, rx=5)
    + s('path', '#ffffff', d='M84 35 Q84 31 90 31 L112 31 Q118 32 118 35 Q118 38 112 39 L90 39 Q84 39 84 35Z', stroke_width=2)
    + s('path', '#ffffff', d='M98 33 L92 26 L98 26 L106 33Z M98 37 L92 44 L98 44 L106 37Z', stroke_width=2)
    + z('path', '#8fb3e0', d='M50 146 Q52 114 84 112 Q116 114 118 146Z')
    + s('path', '#ffffff', d='M76 113 L84 124 L92 113', stroke_width=2.5)
    + face(84, 84, '#ffd9b8', '#2b2220', 'smile')
    + z('rect', '#f5d58a', x=26, y=128, width=110, height=48, rx=4)
    + s('rect', '#f6e0c4', x=26, y=128, width=110, height=10, rx=3)
    + z('rect', '#c9d3db', x=136, y=164, width=42, height=12, rx=3)
    + z('rect', '#e8735a', x=140, y=114, width=34, height=50, rx=6)
    + s('path', d='M150 114 L150 104 L164 104 L164 114', stroke_width=3)
    + s('path', d='M150 122 L150 156 M164 122 L164 156', stroke_width=2)
)

# 6. neck pillow
ITEMS['travel-pillow'] = (
    z('path', '#8fc7e8', d='M46 66 Q32 162 100 172 Q168 162 154 66 Q152 42 132 44 Q114 46 116 68 Q122 132 100 134 Q78 132 84 68 Q86 46 68 44 Q48 42 46 66Z')
    + s('path', d='M58 70 Q50 150 100 160 Q150 150 142 70', stroke='#ffffff', stroke_width=2.5, stroke_dasharray='5 6')
    + dot(88, 149, 3) + dot(112, 149, 3) + cheeks(78, 122, 156, 5, 3)
    + s('path', d='M96 155 Q100 159 104 155', stroke_width=2.5)
)

# 7. camping chair with lantern
ITEMS['camping-chair'] = (
    thick('M52 128 L118 176 M118 128 L52 176', '#5b6b7a', 9, 4.5)
    + z('rect', '#7cc4b0', x=44, y=50, width=82, height=62, rx=6)
    + s('path', d='M44 70 L126 70', stroke='#ffffff', stroke_width=3)
    + thick('M36 108 L36 96 Q36 92 40 92 L50 92 M134 108 L134 96 Q134 92 130 92 L120 92', '#5b6b7a', 9, 4.5)
    + z('path', '#7cc4b0', d='M36 110 L134 110 L126 134 L44 134Z')
    + lantern(156, 118, 0.56, glow=False)
    + s('path', d='M24 178 L178 178', stroke_width=2.5)
)

# 8. camping lantern
ITEMS['lantern'] = lantern(100, 24, 1.5)

# 9. canoe on a lake
ITEMS['canoe-lake'] = (
    pine(36, 122, 40, 24) + pine(58, 120, 30, 20) + pine(160, 122, 44, 26)
    + z('ellipse', '#8fc7e8', cx=100, cy=146, rx=78, ry=30)
    + z('path', '#ffc94d', d='M70 140 Q72 112 100 110 Q128 112 130 140Z')
    + face(100, 80, '#ffd9b8', '#5a4033', 'smile')
    + z('path', '#e8735a', d='M38 132 Q100 142 162 132 Q150 160 100 162 Q50 160 38 132Z')
    + s('path', d='M46 138 Q100 148 154 138', stroke='#f5d58a', stroke_width=3)
    + thick('M62 104 L150 158', '#d9a66b', 8, 4)
    + z('ellipse', '#d9a66b', cx=154, cy=162, rx=8, ry=12, transform='rotate(-58 154 162)')
    + z('circle', '#ffd9b8', cx=82, cy=116, r=7) + z('circle', '#ffd9b8', cx=118, cy=138, r=7)
    + s('path', d='M30 166 Q38 162 46 166 M140 176 Q148 172 156 176', stroke='#ffffff', stroke_width=2.5)
)

# 10. ski lift
ITEMS['ski-resort'] = (
    z('path', '#f4f4f0', d='M20 178 L60 112 L84 136 L126 82 L180 178Z')
    + pine(44, 172, 24, 16) + pine(166, 172, 22, 14)
    + s('path', d='M22 32 L178 66', stroke_width=3)
    + thick('M148 62 L148 162', '#5b6b7a', 9, 4.5)
    + z('rect', '#5b6b7a', x=144, y=56, width=10, height=8, rx=2)
    + z('path', '#8fb3e0', d='M68 152 Q70 124 98 122 Q126 124 128 152Z')
    + z('circle', '#ffd9b8', cx=70, cy=140, r=7)
    + face(98, 96, '#ffd9b8', '#5a4033', 'open')
    + z('path', '#e04b5a', d='M64 92 Q62 58 98 58 Q134 58 132 92 Q98 80 64 92Z')
    + z('circle', '#ffffff', cx=98, cy=56, r=7)
    + z('rect', '#5b6b7a', x=58, y=150, width=94, height=10, rx=3)
    + thick('M84 160 L80 172 M112 160 L116 172', '#8fb3e0', 10, 5)
    + thick('M60 176 L96 170 M104 170 L140 176', '#e8735a', 8, 4)
)

# 11. ticket gates
def gate(x):
    return (z('rect', '#c9d3db', x=x, y=88, width=32, height=88, rx=6)
            + s('rect', '#f4f4f0', x=x, y=88, width=32, height=14, rx=6)
            + s('rect', '#8fc7e8', x=x + 7, y=110, width=18, height=12, rx=3, stroke_width=2.5)
            + s('path', '#9ccf7a', d=f'M{x + 10} {x * 0 + 136} L{x + 18} {136} L{x + 18} {131} L{x + 26} {139} L{x + 18} {147} L{x + 18} {142} L{x + 10} {142}Z', stroke_width=2))


ITEMS['train-ticket-gate'] = (
    z('path', '#f07a8a', d='M52 124 L66 120 L66 136 L52 136Z')
    + z('path', '#f07a8a', d='M148 124 L134 120 L134 136 L148 136Z')
    + gate(20) + gate(84) + gate(148)
    + s('path', d='M18 178 L182 178', stroke_width=2.5)
    + z('rect', '#8fb3e0', x=88, y=66, width=26, height=18, rx=3, transform='rotate(-10 101 75)')
    + z('path', '#ffd9b8', d='M108 92 Q100 82 106 72 Q114 64 126 66 L150 54 L158 66 L132 80 Q126 92 108 92Z')
    + s('path', d='M110 74 Q104 80 110 86', stroke_width=2)
)

# 12. double decker sightseeing bus
ITEMS['sightseeing-bus'] = (
    small_head(58, 70, '#2b2220') + small_head(92, 72, '#c9a36b') + small_head(126, 70, '#5a4033')
    + thick('M134 72 L146 54', '#ffd9b8', 7, 3.5) + z('circle', '#ffd9b8', cx=147, cy=52, r=5)
    + z('rect', '#e04b5a', x=24, y=80, width=152, height=84, rx=10)
    + s('path', d='M24 80 L24 70 M64 80 L64 70 M104 80 L104 70 M144 80 L144 70 M176 80 L176 70 M24 70 L176 70', stroke_width=3)
    + s('rect', '#f5d58a', x=24, y=110, width=152, height=8)
    + s('rect', '#8fc7e8', x=34, y=88, width=30, height=16, rx=3, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=72, y=88, width=30, height=16, rx=3, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=110, y=88, width=30, height=16, rx=3, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=34, y=124, width=26, height=18, rx=3, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=68, y=124, width=26, height=18, rx=3, stroke_width=2.5)
    + s('rect', '#f4f4f0', x=104, y=124, width=22, height=36, rx=3, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=148, y=88, width=22, height=54, rx=4, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=166, cy=152, r=4, stroke_width=2)
    + z('circle', '#5b6b7a', cx=58, cy=164, r=14) + s('circle', '#c9d3db', cx=58, cy=164, r=5, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=146, cy=164, r=14) + s('circle', '#c9d3db', cx=146, cy=164, r=5, stroke_width=2.5)
)

# 13. hot air balloons
def balloon(cx, cy, r, c1, c2):
    b = cy + 1.15 * r
    return (s('path', d=f'M{cx - 0.3 * r} {b} L{cx - 0.2 * r} {cy + 1.5 * r} M{cx + 0.3 * r} {b} L{cx + 0.2 * r} {cy + 1.5 * r}', stroke_width=2 if r < 30 else 2.5)
            + z('path', c1, d=f'M{cx - 0.3 * r} {b} Q{cx - r} {cy + 0.5 * r} {cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy} Q{cx + r} {cy + 0.5 * r} {cx + 0.3 * r} {b}Z')
            + s('path', c2, d=f'M{cx} {cy - r} Q{cx - 0.5 * r} {cy + 0.2 * r} {cx - 0.14 * r} {b} L{cx + 0.14 * r} {b} Q{cx + 0.5 * r} {cy + 0.2 * r} {cx} {cy - r}Z', stroke_width=2 if r < 30 else 2.5)
            + z('rect', '#d9a66b', x=cx - 0.24 * r, y=cy + 1.5 * r, width=0.48 * r, height=0.32 * r, rx=2))


ITEMS['hot-air-balloons'] = (
    cloud(48, 168, 0.8) + cloud(150, 172, 0.7)
    + balloon(44, 116, 19, '#8fc7e8', '#ffffff')
    + balloon(152, 106, 23, '#9ccf7a', '#ffe27a')
    + balloon(96, 68, 40, '#e8735a', '#f5d58a')
)

# 14. ferris wheel
_g = ''
_cols = ['#e8735a', '#8fc7e8', '#ffe27a', '#9ccf7a', '#f6a6b8', '#a98bd0', '#f5b971', '#7cc4b0']
_sp = ''
for i in range(8):
    a = (i * 45 - 90) * pi / 180
    x, y = 100 + 56 * cos(a), 84 + 56 * sin(a)
    _sp += f'M100 84 L{x:.1f} {y:.1f} '
    _g += s('path', d=f'M{x:.1f} {y:.1f} L{x:.1f} {y + 6:.1f}', stroke_width=2.5)
    _g += z('rect', _cols[i], x=round(x - 9, 1), y=round(y + 5, 1), width=18, height=15, rx=5)
ITEMS['amusement-park'] = (
    thick('M100 84 L62 176 M100 84 L138 176', '#c9d3db', 10, 5)
    + s('path', d=_sp, stroke_width=2)
    + s('circle', cx=100, cy=84, r=56, stroke_width=9) + s('circle', cx=100, cy=84, r=56, stroke='#f6a6b8', stroke_width=4.5)
    + _g
    + z('circle', '#f5d58a', cx=100, cy=84, r=10)
    + s('path', d='M40 178 L160 178', stroke_width=2.5)
)

# 15. roller coaster
_seg1 = cubic((22, 164), (52, 164), (56, 72), (90, 70))
_seg2 = cubic((90, 70), (124, 68), (118, 150), (148, 134))
_seg3 = cubic((148, 134), (164, 126), (170, 112), (178, 112))
_pts = _seg1 + _seg2[1:] + _seg3[1:]


def _y_at(x):
    best = min(_pts, key=lambda p: abs(p[0] - x))
    return best[1]


_track = ('M22 164 C52 164 56 72 90 70 C124 68 118 150 148 134 C164 126 170 112 178 112')
_sup = ''.join(f'M{x} {_y_at(x) + 4:.1f} L{x} 176 ' for x in (40, 52, 66, 104, 118, 132, 160, 174))
ITEMS['roller-coaster'] = (
    s('path', d=_sup, stroke='#b9a99c', stroke_width=4)
    + s('path', d='M40 156 L52 132 L66 104 M104 84 L118 122 L132 142 M160 128 L174 116', stroke='#b9a99c', stroke_width=3)
    + thick(_track, '#e04b5a', 10, 5)
    + small_head(78, 50, '#2b2220', 9) + small_head(102, 50, '#c9a36b', 9)
    + thick('M70 44 L64 30 M110 44 L116 30', '#ffd9b8', 7, 3.5)
    + z('rect', '#ffc94d', x=66, y=52, width=48, height=12, rx=4)
    + z('circle', '#5b6b7a', cx=74, cy=66, r=4) + z('circle', '#5b6b7a', cx=106, cy=66, r=4)
    + s('path', d='M20 178 L180 178', stroke_width=2.5)
)

# 16. aquarium tunnel
ITEMS['aquarium'] = (
    z('path', '#8fc7e8', d='M24 176 L24 100 A76 76 0 0 1 176 100 L176 176Z')
    + s('path', d='M50 176 L50 104 A50 50 0 0 1 150 104 L150 176', stroke='#ffffff', stroke_width=3)
    + s('path', '#f4f4f0', d='M50 176 L82 150 L118 150 L150 176Z', stroke_width=2.5)
    + s('path', '#c9d3db', d='M82 150 L82 110 A18 18 0 0 1 118 110 L118 150Z', stroke_width=2.5)
    + s('path', '#7cc4a0', d='M30 176 Q26 156 34 142 Q40 156 36 176Z', stroke_width=2.5)
    + s('path', '#7cc4a0', d='M164 176 Q160 150 170 136 Q174 156 170 176Z', stroke_width=2.5)
    + fish(70, 66, '#f5b971') + fish(130, 52, '#f6a6b8', 0.8, left=True)
    + fish(40, 118, '#ffe27a', 0.7) + fish(158, 104, '#e8735a', 0.85, left=True)
    + fish(100, 88, '#a98bd0', 0.55)
    + s('circle', '#ffffff', cx=96, cy=40, r=3, stroke_width=2) + s('circle', '#ffffff', cx=104, cy=32, r=2, stroke_width=1.5)
    + s('circle', '#ffffff', cx=150, cy=80, r=3, stroke_width=2)
)

# 17. zoo entrance
def paw(cx, cy):
    return (f'<ellipse cx="{cx}" cy="{cy + 3}" rx="5" ry="4" fill="{OUT}" stroke="none"/>'
            + dot(cx - 6, cy - 4, 2) + dot(cx, cy - 7, 2) + dot(cx + 6, cy - 4, 2))


ITEMS['zoo-gate'] = (
    z('rect', '#f5d58a', x=108, y=92, width=14, height=84)
    + s('path', d='M112 84 L110 76 M120 84 L122 76', stroke_width=3) + dot(110, 75, 3) + dot(122, 75, 3)
    + z('ellipse', '#f5d58a', cx=110, cy=92, rx=16, ry=10)
    + dot(104, 90, 2.5) + dot(116, 90, 2.5) + cheeks(99, 121, 96, 3.5, 2)
    + s('circle', '#d9a66b', cx=115, cy=120, r=3, stroke_width=2) + s('circle', '#d9a66b', cx=114, cy=150, r=3, stroke_width=2)
    + s('path', d='M56 104 L144 104 M56 176 L144 176', stroke_width=3)
    + s('path', d=''.join(f'M{x} 104 L{x} 176 ' for x in range(66, 140, 12)), stroke='#5b6b7a', stroke_width=4)
    + z('rect', '#d9a66b', x=30, y=74, width=26, height=102, rx=3)
    + z('rect', '#d9a66b', x=144, y=74, width=26, height=102, rx=3)
    + z('circle', '#f5d58a', cx=43, cy=66, r=10) + z('circle', '#f5d58a', cx=157, cy=66, r=10)
    + z('path', '#9ccf7a', d='M26 76 Q100 26 174 76 L174 98 Q100 50 26 98Z')
    + paw(68, 70) + paw(100, 56) + paw(132, 70)
)

# 18. museum
ITEMS['museum'] = (
    z('rect', '#f6e0c4', x=42, y=82, width=116, height=74)
    + ''.join(z('rect', '#f4f4f0', x=x - 6, y=86, width=12, height=68) for x in (52, 76, 124, 148))
    + z('rect', '#8b6b4f', x=90, y=118, width=20, height=36, rx=8)
    + z('rect', '#c9d3db', x=34, y=72, width=132, height=14)
    + z('path', '#c9d3db', d='M30 72 L100 32 L170 72Z')
    + s('circle', '#f4f4f0', cx=100, cy=56, r=7, stroke_width=2.5)
    + z('rect', '#c9d3db', x=32, y=154, width=136, height=10)
    + z('rect', '#c9d3db', x=24, y=164, width=152, height=12)
)

# 19. city tower
ITEMS['tower'] = (
    z('rect', '#c9d3db', x=30, y=134, width=24, height=42) + z('rect', '#8fb3e0', x=148, y=124, width=24, height=52)
    + s('path', d='M100 18 L100 40', stroke_width=3)
    + z('path', '#e8735a', d='M68 176 Q90 146 92 112 L108 112 Q110 146 132 176Z')
    + z('rect', '#f4f4f0', x=92, y=40, width=16, height=96)
    + s('path', '#e8735a', d='M92 56 L108 56 L108 64 L92 64Z M92 110 L108 110 L108 118 L92 118Z', stroke_width=2.5)
    + z('ellipse', '#8fb3e0', cx=100, cy=84, rx=30, ry=12)
    + s('path', d='M72 84 L128 84', stroke='#ffffff', stroke_width=3)
    + z('ellipse', '#f5d58a', cx=100, cy=44, rx=13, ry=6)
    + s('path', d='M24 178 L176 178', stroke_width=2.5)
)


# 20. city skyline
def bldg(x, y, w, color, cols=2):
    o = z('rect', color, x=x, y=y, width=w, height=176 - y, rx=2)
    gap = w / cols
    for cx in range(cols):
        for ry in range(int(y) + 10, 166, 16):
            o += s('rect', '#ffffff', x=round(x + gap * cx + gap / 2 - 3.5, 1), y=ry, width=7, height=8, rx=1, stroke_width=2)
    return o


ITEMS['skyline'] = (
    z('circle', '#ffe27a', cx=146, cy=48, r=18)
    + cloud(54, 50, 0.8)
    + bldg(80, 44, 30, '#5b6b7a', 2) + s('path', d='M95 44 L95 30', stroke_width=3)
    + bldg(130, 72, 28, '#8fc7e8', 2)
    + bldg(52, 76, 30, '#c9d3db', 2)
    + bldg(108, 98, 26, '#f5d58a', 2)
    + bldg(26, 108, 28, '#8fb3e0', 2)
    + bldg(156, 112, 22, '#f6a6b8', 1)
    + s('path', d='M20 178 L180 178', stroke_width=2.5)
)
