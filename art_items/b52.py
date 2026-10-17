from math import sin, cos, pi, sqrt
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def P(a):
    return f'{a[0]:.1f} {a[1]:.1f}'


def star_d(cx, cy, R, r, rot=-90, n=5):
    pts = []
    for i in range(n * 2):
        a = (rot + i * 180 / n) * pi / 180
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


def thick(d, color, w=9, inner=4.5):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def burst(cx, cy, R, color, n=10, rot=0):
    o = ''
    for i in range(n):
        a = (rot + i * 360 / n) * pi / 180
        x1, y1 = cx + R * 0.35 * cos(a), cy + R * 0.35 * sin(a)
        x2, y2 = cx + R * 0.85 * cos(a), cy + R * 0.85 * sin(a)
        o += thick(f'M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}', color, 8, 4)
        o += s('circle', color, cx=round(cx + R * cos(a), 1), cy=round(cy + R * sin(a), 1), r=3.2, stroke_width=2)
    return o + z('circle', color, cx=cx, cy=cy, r=round(R * 0.18, 1))


def maple(cx, cy, R, c, rot=0):
    a = (90 + rot) * pi / 180
    stem = s('path', d=f'M{cx:.1f} {cy:.1f} L{cx + R * 1.0 * cos(a):.1f} {cy + R * 1.0 * sin(a):.1f}', stroke_width=2.5)
    pts = []
    for i, ang in enumerate((-90, -30, 30, 150, 210)):
        A = (ang + rot) * pi / 180
        rr = R if i == 0 else R * 0.9
        pts.append((cx + rr * cos(A), cy + rr * sin(A)))
    d = ''
    for i, ang in enumerate((-90, -30, 30, 150, 210)):
        A = (ang + rot) * pi / 180
        nxt = (-30, 30, 90, 210, 270)[i]
        B = ((ang + nxt) / 2 + rot) * pi / 180
        k = 0.3 if nxt == 90 else 0.62
        d += f'L{pts[i][0]:.1f} {pts[i][1]:.1f} L{cx + R * k * cos(B):.1f} {cy + R * k * sin(B):.1f} '
    d = 'M' + d[1:] + 'Z'
    veins = s('path', d=''.join(f'M{cx:.1f} {cy:.1f} L{cx + (x - cx) * .6:.1f} {cy + (y - cy) * .6:.1f} ' for x, y in pts), stroke_width=1.8)
    if R >= 12:
        return stem + z('path', c, d=d) + veins
    return stem + s('path', c, d=d, stroke_width=2.5)


def sakura(cx, cy, r, c='#f6a6b8'):
    o = ''
    for i in range(5):
        a = (i * 72 - 90) * pi / 180
        o += s('circle', c, cx=round(cx + r * 0.55 * cos(a), 1), cy=round(cy + r * 0.55 * sin(a), 1), r=round(r * 0.48, 1), stroke_width=2)
    return o + dot(cx, cy, r * 0.28, '#f07a8a')


def sparkle(cx, cy, r, c='#ffe27a'):
    return s('path', c, d=f'M{cx} {cy - r} Q{cx + r * .2} {cy - r * .2} {cx + r} {cy} Q{cx + r * .2} {cy + r * .2} {cx} {cy + r} Q{cx - r * .2} {cy + r * .2} {cx - r} {cy} Q{cx - r * .2} {cy - r * .2} {cx} {cy - r}Z', stroke_width=2)


def flake(cx, cy, r, c='#8fc7e8'):
    o = ''
    for k in range(3):
        a = (90 + k * 60) * pi / 180
        o += s('path', d=f'M{cx - r * cos(a):.1f} {cy - r * sin(a):.1f} L{cx + r * cos(a):.1f} {cy + r * sin(a):.1f}', stroke=c, stroke_width=2.5)
    return o


def heart_d(cx, cy, k):
    pts = [(0, 24), (-12, 14), (-20, 6), (-14, -4), (-8, -12), (0, -7), (0, 0), (0, -7), (8, -12), (14, -4), (20, 6), (12, 14), (0, 24)]
    q = [f'{cx + x * k:.1f} {cy + y * k:.1f}' for x, y in pts]
    return f'M{q[0]} C{q[1]} {q[2]} {q[3]} C{q[4]} {q[5]} {q[6]} C{q[7]} {q[8]} {q[9]} C{q[10]} {q[11]} {q[12]}Z'


def sface(cx, cy, k, skin, hair, mouth='smile'):
    return f'<g transform="translate({cx} {cy}) scale({k}) translate({-cx} {-cy})">' + face(cx, cy, skin, hair, mouth) + '</g>'


def box(x, y, w, h, c, rc, bow=False):
    cx = x + w / 2
    o = z('rect', c, x=x, y=y, width=w, height=h, rx=3)
    o += s('rect', rc, x=cx - 5, y=y, width=10, height=h, stroke_width=2.5)
    o += s('rect', rc, x=x, y=y + h / 2 - 5, width=w, height=10, stroke_width=2.5)
    if bow:
        o += z('path', rc, d=f'M{cx} {y} Q{cx - 24} {y - 22} {cx - 18} {y - 4} Q{cx - 12} {y + 2} {cx} {y}Z')
        o += z('path', rc, d=f'M{cx} {y} Q{cx + 24} {y - 22} {cx + 18} {y - 4} Q{cx + 12} {y + 2} {cx} {y}Z')
        o += s('circle', rc, cx=cx, cy=y - 1, r=4.5, stroke_width=2.5)
    return o


def cone(tip, opn, hw, c, stripe):
    dx, dy = opn[0] - tip[0], opn[1] - tip[1]
    L = sqrt(dx * dx + dy * dy)
    px, py = -dy / L * hw, dx / L * hw
    a = (opn[0] + px, opn[1] + py)
    b = (opn[0] - px, opn[1] - py)
    o = z('path', c, d=f'M{P(tip)} L{P(a)} Q{P((opn[0] + dx / L * 4, opn[1] + dy / L * 4))} {P(b)}Z')
    for t in (0.45, 0.72):
        m1 = (tip[0] + (a[0] - tip[0]) * t, tip[1] + (a[1] - tip[1]) * t)
        m2 = (tip[0] + (b[0] - tip[0]) * t, tip[1] + (b[1] - tip[1]) * t)
        o += s('path', d=f'M{P(m1)} L{P(m2)}', stroke=stripe, stroke_width=3.5)
    return o


def confetti(pts):
    cols = ['#f07a8a', '#8fc7e8', '#ffc94d', '#9ccf7a', '#a98bd0', '#f5b971']
    o = ''
    for i, (x, y) in enumerate(pts):
        c = cols[i % len(cols)]
        if i % 2:
            o += s('rect', c, x=x - 3, y=y - 3, width=7, height=7, stroke_width=2, transform=f'rotate({20 + i * 23} {x} {y})')
        else:
            o += s('circle', c, cx=x, cy=y, r=3.5, stroke_width=2)
    return o


# 1. fireworks festival over the river
ITEMS['fireworks-festival'] = (
    burst(72, 68, 40, '#f07a8a', 12)
    + burst(140, 58, 28, '#ffc94d', 10, 15)
    + burst(144, 112, 18, '#8fc7e8', 8, 10)
    + z('rect', '#b9a99c', x=24, y=138, width=20, height=14, rx=2) + z('path', '#e8735a', d='M20 140 L34 128 L48 140Z')
    + z('rect', '#b9a99c', x=156, y=140, width=18, height=12, rx=2) + z('path', '#e8735a', d='M152 142 L165 131 L178 142Z')
    + z('path', '#8fc7e8', d='M20 152 Q60 146 100 152 Q140 158 180 152 L180 180 L20 180Z')
    + thick('M62 162 L82 162', '#f07a8a', 7, 3.5) + thick('M66 172 L78 172', '#f07a8a', 7, 3.5)
    + thick('M132 164 L150 164', '#ffc94d', 7, 3.5) + thick('M136 173 L146 173', '#ffc94d', 7, 3.5)
    + s('path', d='M30 168 Q38 164 46 168', stroke_width=2.5) + s('path', d='M100 170 Q108 166 116 170', stroke_width=2.5)
    + dot(34, 34, 2.5, '#ffc94d') + dot(168, 30, 2.5, '#f07a8a') + dot(110, 100, 2.5, '#9ccf7a')
)

# 2. snow festival - bear snow sculpture
ITEMS['snow-festival'] = (
    z('rect', '#c9d3db', x=36, y=150, width=128, height=28, rx=4)
    + s('path', d='M50 164 L66 164 M134 164 L150 164', stroke_width=2)
    + z('ellipse', '#f4f4f0', cx=100, cy=124, rx=44, ry=30)
    + z('circle', '#f4f4f0', cx=74, cy=48, r=11) + z('circle', '#f4f4f0', cx=126, cy=48, r=11)
    + z('circle', '#f4f4f0', cx=100, cy=78, r=34)
    + z('ellipse', '#f4f4f0', cx=72, cy=146, rx=14, ry=8) + z('ellipse', '#f4f4f0', cx=128, cy=146, rx=14, ry=8)
    + s('circle', '#c9d3db', cx=74, cy=48, r=5, stroke='none') + s('circle', '#c9d3db', cx=126, cy=48, r=5, stroke='none')
    + dot(88, 74) + dot(112, 74) + cheeks(78, 122, 88, 6, 3.5)
    + z('ellipse', '#ffffff', cx=100, cy=90, rx=12, ry=9) + f'<ellipse cx="100" cy="86" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + s('path', d='M95 94 Q100 98 105 94', stroke_width=2.5)
    + s('path', d='M86 118 Q90 124 86 130 M114 118 Q110 124 114 130', stroke='#c9d3db', stroke_width=2.5)
    + flake(34, 42, 9) + flake(166, 40, 9) + flake(28, 104, 7) + flake(172, 100, 7) + flake(150, 72, 6)
)

# 3. lantern floating
def lantern(cx, base, w, h):
    x = cx - w / 2
    return (z('rect', '#f5d58a', x=x, y=base - h, width=w, height=h, rx=2)
            + s('ellipse', '#ffc94d', cx=cx, cy=base - h / 2, rx=w * 0.22, ry=h * 0.24, stroke='none')
            + s('path', d=f'M{cx} {base - h} L{cx} {base} M{x} {base - h * 0.5} L{x + w} {base - h * 0.5}', stroke='#9a6a3f', stroke_width=2)
            + z('rect', '#9a6a3f', x=x - 2, y=base - h - 5, width=w + 4, height=6, rx=2)
            + z('rect', '#9a6a3f', x=x - 5, y=base, width=w + 10, height=7, rx=2)
            + s('path', d=f'M{x - 6} {base + 13} Q{cx} {base + 17} {x + w + 6} {base + 13}', stroke_width=2.5))


ITEMS['lantern-floating'] = (
    z('circle', '#ffe27a', cx=152, cy=44, r=18)
    + dot(44, 36, 2.5, '#ffc94d') + dot(84, 56, 2.5, '#ffc94d') + dot(118, 30, 2.5, '#ffc94d')
    + z('path', '#8fb3e0', d='M20 112 Q60 106 100 112 Q140 118 180 112 L180 180 L20 180Z')
    + lantern(136, 126, 24, 28)
    + lantern(62, 140, 30, 36)
    + lantern(110, 162, 26, 30)
    + s('path', d='M150 164 Q158 160 166 164 M32 168 Q40 164 48 168', stroke_width=2.5)
)

# 4. christmas presents under the tree
ITEMS['christmas-presents'] = (
    z('rect', '#8b6b4f', x=92, y=132, width=16, height=20, rx=2)
    + z('path', '#7cc4a0', d='M46 138 Q100 148 154 138 L120 100 L80 100Z')
    + z('path', '#7cc4a0', d='M56 110 Q100 118 144 110 L114 72 L86 72Z')
    + z('path', '#7cc4a0', d='M66 82 Q100 90 134 82 L100 44Z')
    + s('path', d='M64 126 Q100 136 134 122', stroke='#f5d58a', stroke_width=3)
    + s('path', d='M74 98 Q100 106 126 94', stroke='#f5d58a', stroke_width=3)
    + s('circle', '#e04b5a', cx=70, cy=134, r=5.5, stroke_width=2.5) + s('circle', '#8fb3e0', cx=124, cy=130, r=5.5, stroke_width=2.5)
    + s('circle', '#ffc94d', cx=96, cy=114, r=5, stroke_width=2.5) + s('circle', '#e04b5a', cx=118, cy=106, r=5, stroke_width=2.5)
    + s('circle', '#8fb3e0', cx=86, cy=86, r=4.5, stroke_width=2.5)
    + z('path', '#ffe27a', d=star_d(100, 40, 15, 6.5))
    + box(28, 140, 50, 38, '#e8735a', '#ffe27a', True)
    + box(122, 134, 50, 44, '#8fc7e8', '#f07a8a', True)
    + box(80, 154, 40, 26, '#f5d58a', '#9ccf7a', True)
)

# 5. mochi pounding
ITEMS['mochi-pounding'] = (
    z('path', '#7cc4b0', d='M28 182 Q30 124 64 122 Q98 124 100 182Z')
    + s('path', d='M50 124 L64 152 L78 124', stroke_width=2.5)
    + z('path', '#d9a66b', d='M112 140 L176 140 L170 180 L118 180Z')
    + s('path', d='M116 158 L172 158', stroke='#9a6a3f', stroke_width=2.5)
    + z('ellipse', '#9a6a3f', cx=144, cy=140, rx=33, ry=8)
    + z('path', '#ffffff', d='M120 140 Q122 120 144 120 Q166 120 168 140Z')
    + thick('M90 148 L144 92', '#d9a66b', 11, 5.5)
    + z('rect', '#d9a66b', x=128, y=74, width=44, height=22, rx=6, transform='rotate(45 150 85)')
    + s('path', d='M162 70 L172 60 M170 82 L182 78 M150 62 L154 50', stroke_width=2.5)
    + face(64, 82, '#ffd9b8', '#2b2220', 'open')
    + s('path', '#ffffff', d='M31 72 Q64 60 97 72 L97 78 Q64 66 31 78Z', stroke_width=2.5)
    + z('circle', '#ffd9b8', cx=94, cy=144, r=8) + z('circle', '#ffd9b8', cx=112, cy=126, r=8)
)

# 6. autumn festival lantern
def chochin_rib(y, cy=88, rx=40, ry=44):
    hw = rx * sqrt(max(0, 1 - ((y - cy) / ry) ** 2))
    return f'M{100 - hw:.1f} {y} Q100 {y + 8} {100 + hw:.1f} {y} '


ITEMS['autumn-festival'] = (
    s('path', d='M100 20 L100 36', stroke_width=3)
    + z('ellipse', '#e8735a', cx=100, cy=88, rx=40, ry=44)
    + s('path', d=''.join(chochin_rib(y) for y in (62, 76, 90, 104, 118)), stroke='#9a6a3f', stroke_width=2)
    + z('rect', '#5b6b7a', x=82, y=36, width=36, height=12, rx=3)
    + z('rect', '#5b6b7a', x=82, y=128, width=36, height=12, rx=3)
    + s('path', d='M92 140 L92 152 M100 140 L100 154 M108 140 L108 152', stroke='#ffc94d', stroke_width=3)
    + maple(40, 58, 17, '#e8735a', -15) + maple(160, 54, 16, '#f5b971', 20)
    + maple(40, 128, 15, '#ffc94d', 10) + maple(160, 124, 17, '#e04b5a', -20)
    + maple(70, 164, 13, '#f5b971', 30) + maple(134, 164, 13, '#e8735a', -30)
    + dot(64, 100, 2.5, '#ffc94d') + dot(140, 94, 2.5, '#ffc94d')
)

# 7. cherry blossom party
ITEMS['cherry-blossom-party'] = (
    thick('M22 54 Q80 28 178 38', '#8b6b4f', 11, 5.5) + thick('M110 36 Q126 54 150 60', '#8b6b4f', 9, 4.5)
    + sakura(44, 44, 18) + sakura(82, 34, 16) + sakura(122, 30, 18) + sakura(162, 40, 16) + sakura(146, 62, 14)
    + z('path', '#8fc7e8', d='M32 116 L168 116 L180 176 L20 176Z')
    + s('path', d='M68 116 L62 176 M132 116 L138 176 M26 146 L174 146', stroke='#ffffff', stroke_width=3)
    + z('rect', '#e8735a', x=54, y=110, width=92, height=56, rx=6)
    + s('rect', '#ffffff', x=60, y=116, width=40, height=44, rx=3, stroke_width=2.5)
    + dot(80, 138, 5, '#e04b5a')
    + s('rect', '#f5d58a', x=106, y=118, width=34, height=16, rx=3, stroke_width=2.5)
    + s('path', d='M117 118 L117 134 M128 118 L128 134', stroke_width=2)
    + s('circle', '#9ccf7a', cx=114, cy=148, r=7, stroke_width=2.5) + s('ellipse', '#f6a6b8', cx=132, cy=148, rx=8, ry=6, stroke_width=2.5)
    + s('ellipse', '#f6a6b8', cx=40, cy=90, rx=5, ry=3.5, stroke_width=2, transform='rotate(30 40 90)')
    + s('ellipse', '#f6a6b8', cx=96, cy=82, rx=5, ry=3.5, stroke_width=2, transform='rotate(-20 96 82)')
    + s('ellipse', '#f6a6b8', cx=166, cy=94, rx=5, ry=3.5, stroke_width=2, transform='rotate(40 166 94)')
)

# 8. ramune bottle
ITEMS['ramune-bottle'] = (
    z('path', '#8fc7e8', d='M70 172 Q70 180 78 180 L122 180 Q130 180 130 172 L130 120 Q130 104 115 97 Q110 93 112 87 Q120 78 117 68 Q114 60 112 54 L88 54 Q86 60 83 68 Q80 78 88 87 Q90 93 85 97 Q70 104 70 120Z')
    + s('circle', '#ffffff', cx=100, cy=72, r=10, stroke_width=2.5)
    + z('rect', '#8fb3e0', x=84, y=36, width=32, height=18, rx=4)
    + s('rect', '#ffffff', x=70, y=126, width=60, height=14, stroke_width=2.5)
    + s('circle', '#ffffff', cx=84, cy=110, r=3, stroke_width=2) + s('circle', '#ffffff', cx=116, cy=114, r=2.5, stroke_width=2)
    + s('circle', '#ffffff', cx=88, cy=172, r=2.5, stroke_width=2) + s('circle', '#ffffff', cx=118, cy=166, r=3, stroke_width=2)
    + dot(88, 152) + dot(112, 152) + cheeks(80, 120, 162, 6, 3.5) + s('path', d='M95 160 Q100 165 105 160', stroke_width=2.5)
    + sparkle(150, 60, 10) + sparkle(46, 96, 8, '#8fc7e8') + sparkle(156, 140, 7, '#8fc7e8')
    + s('path', d='M58 52 Q52 60 58 66 Q64 60 58 52Z', fill='#8fc7e8', stroke_width=2)
)

# 9. cake with candles
def candle(x, yb, c):
    return (s('rect', c, x=x - 4, y=yb - 30, width=8, height=30, rx=2, stroke_width=2.5)
            + s('path', d=f'M{x - 4} {yb - 20} L{x + 4} {yb - 24} M{x - 4} {yb - 10} L{x + 4} {yb - 14}', stroke='#ffffff', stroke_width=2)
            + z('path', '#ffc94d', d=f'M{x} {yb - 32} Q{x - 7} {yb - 40} {x} {yb - 50} Q{x + 7} {yb - 40} {x} {yb - 32}Z'))


ITEMS['cake-candles'] = (
    z('ellipse', '#ffffff', cx=100, cy=164, rx=72, ry=14)
    + z('path', '#f6e0c4', d='M42 112 L42 154 Q100 174 158 154 L158 112Z')
    + s('path', '#f07a8a', d='M42 130 Q100 148 158 130 L158 138 Q100 156 42 138Z', stroke_width=2.5)
    + z('ellipse', '#ffffff', cx=100, cy=112, rx=58, ry=18)
    + s('path', '#ffffff', d='M44 114 Q46 126 52 124 Q56 118 60 124 Q66 128 70 122', stroke_width=2.5)
    + s('path', '#ffffff', d='M130 124 Q136 128 140 122 Q146 126 150 120 Q156 124 156 114', stroke_width=2.5)
    + candle(74, 108, '#8fb3e0') + candle(100, 102, '#f6a6b8') + candle(126, 108, '#9ccf7a')
    + candle(87, 120, '#f6a6b8') + candle(113, 120, '#8fb3e0')
    + s('path', '#e04b5a', d='M60 116 Q54 124 60 128 Q66 124 60 116Z', stroke_width=2)
    + s('path', '#e04b5a', d='M140 116 Q134 124 140 128 Q146 124 140 116Z', stroke_width=2)
    + sparkle(36, 64, 9) + sparkle(164, 60, 9)
)

# 10. pile of presents
ITEMS['present-mountain'] = (
    box(28, 128, 64, 50, '#e8735a', '#ffe27a')
    + box(96, 122, 76, 56, '#8fc7e8', '#f07a8a')
    + box(52, 84, 58, 44, '#9ccf7a', '#e04b5a')
    + box(114, 94, 44, 28, '#f6a6b8', '#ffffff')
    + box(74, 50, 44, 34, '#ffe27a', '#8fb3e0', True)
    + sparkle(40, 80, 9) + sparkle(160, 64, 10) + sparkle(144, 32, 6, '#f6a6b8')
)

# 11. kids with party crackers
def kid(cx, cy, shirt, hair, mouth):
    return (z('path', shirt, d=f'M{cx - 30} 182 Q{cx - 28} 140 {cx} 138 Q{cx + 28} 140 {cx + 30} 182Z')
            + sface(cx, cy, 0.8, '#ffd9b8', hair, mouth))


ITEMS['party-cracker-kids'] = (
    thick('M80 46 Q66 34 70 22', '#f07a8a', 8, 4) + thick('M86 44 Q60 46 46 34', '#9ccf7a', 8, 4)
    + thick('M120 46 Q134 34 130 22', '#8fc7e8', 8, 4) + thick('M114 44 Q140 46 154 34', '#ffc94d', 8, 4)
    + confetti([(100, 30), (56, 52), (144, 52), (92, 44), (110, 24), (38, 64), (162, 66), (86, 26), (116, 40)])
    + kid(58, 112, '#f5b971', '#5a4033', 'open') + kid(142, 112, '#7cc4b0', '#2b2220', 'smile')
    + thick('M74 152 L92 96', '#f5b971', 12, 6) + thick('M126 152 L108 96', '#7cc4b0', 12, 6)
    + cone((92, 90), (82, 52), 11, '#ffc94d', '#e04b5a') + cone((108, 90), (118, 52), 11, '#a98bd0', '#ffffff')
    + z('circle', '#ffd9b8', cx=91, cy=94, r=7) + z('circle', '#ffd9b8', cx=109, cy=94, r=7)
)

# 12. dance party - disco ball
ITEMS['dance-party'] = (
    s('path', '#ffe27a', d='M92 112 L40 178 L68 180Z', stroke_width=2.5)
    + s('path', '#f6a6b8', d='M100 116 L88 180 L114 180Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M108 112 L134 180 L162 178Z', stroke_width=2.5)
    + s('path', d='M100 18 L100 34', stroke_width=3)
    + z('circle', '#c9d3db', cx=100, cy=74, r=40)
    + s('ellipse', cx=100, cy=74, rx=20, ry=40, stroke_width=2) + s('path', d='M100 34 L100 114', stroke_width=2)
    + s('path', d='M66 54 Q100 62 134 54 M60 74 Q100 82 140 74 M66 94 Q100 102 134 94', stroke_width=2)
    + s('rect', '#ffffff', x=84, y=60, width=12, height=10, stroke='none') + s('rect', '#ffffff', x=104, y=80, width=12, height=10, stroke='none')
    + s('rect', '#8fb3e0', x=120, y=58, width=12, height=10, stroke='none') + s('rect', '#f6a6b8', x=70, y=80, width=10, height=10, stroke='none')
    + z('rect', '#5b6b7a', x=92, y=30, width=16, height=8, rx=2)
    + sparkle(150, 40, 10) + sparkle(46, 120, 8, '#f6a6b8') + sparkle(160, 120, 8, '#8fc7e8')
    + z('ellipse', OUT, cx=38, cy=72, rx=7, ry=5) + s('path', d='M44 70 L44 40 Q52 44 56 52', stroke_width=3)
    + z('ellipse', OUT, cx=156, cy=84, rx=6, ry=4.5) + s('path', d='M161 82 L161 60', stroke_width=3)
)

# 13. award ceremony
ITEMS['award-ceremony'] = (
    z('rect', '#c9d3db', x=24, y=154, width=46, height=26, rx=3)
    + z('rect', '#f5b971', x=130, y=162, width=46, height=18, rx=3)
    + z('path', '#8fb3e0', d='M68 142 Q70 96 100 94 Q130 96 132 142Z')
    + z('rect', '#f5d58a', x=64, y=140, width=72, height=40, rx=3)
    + face(100, 62, '#ffd9b8', '#5a4033', 'open')
    + s('path', d='M88 112 Q74 112 76 100 Q78 94 88 100 M112 112 Q126 112 124 100 Q122 94 112 100', stroke_width=3)
    + z('path', '#ffc94d', d='M86 98 L114 98 Q114 120 100 122 Q86 120 86 98Z')
    + z('rect', '#ffc94d', x=96, y=120, width=8, height=8)
    + z('rect', '#d9a66b', x=86, y=128, width=28, height=10, rx=2)
    + z('circle', '#ffd9b8', cx=80, cy=118, r=7) + z('circle', '#ffd9b8', cx=120, cy=118, r=7)
    + z('path', '#ffe27a', d=star_d(40, 128, 11, 5)) + z('path', '#ffe27a', d=star_d(160, 136, 11, 5))
    + confetti([(30, 40), (170, 36), (24, 90), (176, 92), (150, 20), (50, 20)])
)

# 14. celebration banner / garland
def garland(y0, ymid, cols):
    o = s('path', d=f'M24 {y0} Q100 {2 * ymid - y0} 176 {y0}', stroke_width=3)
    n = len(cols)
    for i, c in enumerate(cols):
        t = (i + 0.5) / n
        x = (1 - t) ** 2 * 24 + 2 * (1 - t) * t * 100 + t * t * 176
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (2 * ymid - y0) + t * t * y0
        o += z('path', c, d=f'M{x - 10:.1f} {y - 1:.1f} L{x + 10:.1f} {y - 1:.1f} L{x:.1f} {y + 24:.1f}Z')
    return o


ITEMS['celebration-banner'] = (
    garland(32, 58, ['#f07a8a', '#ffc94d', '#8fc7e8', '#9ccf7a', '#a98bd0', '#f5b971', '#f07a8a'])
    + garland(96, 120, ['#8fc7e8', '#f6a6b8', '#ffe27a', '#7cc4b0', '#e8735a', '#8fb3e0', '#ffc94d'])
    + z('path', '#ffe27a', d=star_d(48, 162, 15, 6.5)) + z('path', '#f6a6b8', d=star_d(152, 158, 13, 5.5))
    + z('path', '#8fc7e8', d=star_d(100, 170, 10, 4.5))
    + sparkle(76, 150, 6) + sparkle(126, 150, 6, '#8fc7e8') + sparkle(176, 128, 6, '#f6a6b8') + sparkle(26, 128, 6)
)

# 15. thank-you flowers with heart card
def flower(cx, cy, r, pc, cc):
    o = ''
    for i in range(6):
        a = i * 60 * pi / 180
        o += z('circle', pc, cx=round(cx + r * 0.62 * cos(a), 1), cy=round(cy + r * 0.62 * sin(a), 1), r=round(r * 0.42, 1))
    return o + z('circle', cc, cx=cx, cy=cy, r=round(r * 0.42, 1))


ITEMS['thank-you-flowers'] = (
    z('ellipse', '#9ccf7a', cx=58, cy=98, rx=16, ry=8, transform='rotate(-30 58 98)')
    + z('ellipse', '#9ccf7a', cx=142, cy=98, rx=16, ry=8, transform='rotate(30 142 98)')
    + flower(100, 52, 24, '#ffe27a', '#f5b971')
    + flower(70, 80, 22, '#f6a6b8', '#ffe27a')
    + flower(130, 80, 22, '#f07a8a', '#ffe27a')
    + z('path', '#8fc7e8', d='M54 98 L146 98 L110 178 L90 178Z')
    + s('path', d='M78 100 L96 176 M122 100 L104 176', stroke='#ffffff', stroke_width=2.5)
    + z('path', '#f07a8a', d='M100 136 Q80 118 76 132 Q78 146 100 136Z') + z('path', '#f07a8a', d='M100 136 Q120 118 124 132 Q122 146 100 136Z')
    + s('circle', '#f07a8a', cx=100, cy=136, r=5, stroke_width=2.5)
    + s('path', d='M106 140 Q124 152 134 146', stroke_width=2)
    + z('rect', '#ffffff', x=130, y=130, width=38, height=32, rx=3, transform='rotate(8 149 146)')
    + s('path', '#f07a8a', d=heart_d(149, 140, 0.55), stroke_width=2)
)

# 16. countdown party clock
ticks = ''.join(f'M{100 + 38 * cos(a * pi / 6):.1f} {108 + 38 * sin(a * pi / 6):.1f} L{100 + 43 * cos(a * pi / 6):.1f} {108 + 43 * sin(a * pi / 6):.1f} ' for a in range(12))
ITEMS['countdown-party'] = (
    thick('M40 150 Q26 132 34 112', '#f07a8a', 8, 4) + thick('M160 150 Q176 132 166 114', '#9ccf7a', 8, 4)
    + z('circle', '#8fb3e0', cx=100, cy=108, r=56)
    + s('circle', '#ffffff', cx=100, cy=108, r=47)
    + s('path', d=ticks, stroke_width=3)
    + s('path', d='M100 108 L98 84', stroke_width=5) + s('path', d='M100 108 L82 77', stroke_width=3)
    + dot(100, 108, 5)
    + z('path', '#f07a8a', d='M72 64 L114 54 L84 20Z')
    + s('path', d='M78 46 L98 41 M75 56 L106 48', stroke='#ffe27a', stroke_width=3.5)
    + z('circle', '#ffe27a', cx=84, cy=20, r=7)
    + confetti([(30, 40), (150, 30), (170, 66), (36, 80), (164, 166), (34, 172), (128, 22), (54, 30), (178, 140)])
    + sparkle(144, 48, 8)
)

# 17. heart-shaped gift box
ITEMS['heart-gift'] = (
    z('path', '#f07a8a', d=heart_d(100, 86, 3.4))
    + z('path', '#f6a6b8', d=heart_d(100, 72, 3.4))
    + s('path', d='M100 48 L100 150', stroke='#ffffff', stroke_width=7)
    + s('path', d='M100 150 L100 166', stroke='#ffffff', stroke_width=7)
    + z('path', '#ffe27a', d='M100 64 Q72 36 66 56 Q66 72 100 64Z') + z('path', '#ffe27a', d='M100 64 Q128 36 134 56 Q134 72 100 64Z')
    + z('circle', '#ffe27a', cx=100, cy=63, r=6)
    + s('path', '#f6a6b8', d=heart_d(36, 42, 0.5), stroke_width=2) + s('path', '#f07a8a', d=heart_d(166, 40, 0.45), stroke_width=2)
    + sparkle(168, 150, 8) + sparkle(32, 150, 7)
)

# 18. autumn leaf viewing
ITEMS['leaf-viewing'] = (
    s('path', d='M22 180 L178 180', stroke_width=2.5)
    + z('path', '#8b6b4f', d='M132 180 L136 96 L150 96 L156 180Z')
    + s('path', d='M140 112 Q128 102 120 86 M146 108 Q156 98 164 90', stroke_width=3)
    + z('path', '#e8735a', d='M112 92 Q96 86 102 70 Q100 50 120 46 Q130 26 152 32 Q174 30 176 52 Q186 70 176 86 Q174 102 156 100 Q142 108 130 98 Q118 102 112 92Z')
    + maple(126, 64, 9, '#f5b971', -15) + maple(156, 52, 9, '#ffc94d', 20) + maple(158, 84, 8, '#e04b5a', 0)
    + z('path', '#f5b971', d='M30 182 Q32 148 62 146 Q92 148 94 182Z')
    + face(62, 114, '#ffd9b8', '#5a4033', 'open')
    + z('circle', '#ffd9b8', cx=100, cy=154, r=8)
    + maple(106, 136, 12, '#e8735a', 10)
    + maple(40, 50, 13, '#e8735a', -20) + maple(80, 40, 11, '#ffc94d', 25) + maple(112, 106, 10, '#e04b5a', 40)
    + maple(174, 140, 10, '#f5b971', -10)
)

# 19. summer vacation
ITEMS['summer-vacation'] = (
    z('circle', '#ffe27a', cx=156, cy=46, r=18)
    + s('path', d='M156 18 L156 12 M156 74 L156 80 M128 46 L122 46 M184 46 L188 46 M136 26 L132 22 M176 26 L180 22 M136 66 L132 70 M176 66 L180 70', stroke_width=2.5)
    + z('ellipse', '#f5d58a', cx=76, cy=88, rx=56, ry=20)
    + z('path', '#f5d58a', d='M48 86 Q48 46 76 46 Q104 46 104 86 Q76 94 48 86Z')
    + z('path', '#e8735a', d='M48 74 Q76 82 104 74 L104 86 Q76 94 48 86Z')
    + s('path', d='M30 92 L38 90 M112 94 L120 92 M64 104 L72 104', stroke='#d9a66b', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M82 132 A46 46 0 0 0 174 132Z')
    + s('path', '#f4f4f0', d='M88 132 A40 40 0 0 0 168 132Z', stroke_width=2.5)
    + s('path', '#f07a8a', d='M94 132 A34 34 0 0 0 162 132Z', stroke_width=2.5)
    + s('ellipse', OUT, cx=110, cy=146, rx=2, ry=3, stroke='none') + s('ellipse', OUT, cx=146, cy=146, rx=2, ry=3, stroke='none')
    + s('ellipse', OUT, cx=128, cy=158, rx=2, ry=3, stroke='none')
    + dot(118, 138, 3) + dot(138, 138, 3) + cheeks(110, 146, 136, 5, 3) + s('path', d='M124 140 Q128 144 132 140', stroke_width=2.5)
    + s('path', d='M24 150 Q34 142 44 150 Q54 158 64 150 M28 166 Q38 158 48 166 Q58 174 68 166', stroke='#8fc7e8', stroke_width=4)
)

# 20. christmas cookies
ITEMS['christmas-cookies'] = (
    z('ellipse', '#ffffff', cx=100, cy=150, rx=78, ry=26)
    + s('ellipse', cx=100, cy=150, rx=60, ry=17, stroke='#c9d3db', stroke_width=2)
    + z('path', '#f5d58a', d=star_d(46, 130, 22, 10))
    + s('path', d=star_d(46, 130, 15, 7), stroke='#ffffff', stroke_width=2)
    + z('path', '#7cc4a0', d='M138 152 L174 152 L162 132 L170 132 L156 106 L142 132 L150 132Z')
    + s('path', d='M146 142 Q156 146 166 140', stroke='#ffffff', stroke_width=2.5)
    + dot(150, 124, 2.5, '#e04b5a') + dot(160, 146, 2.5, '#ffc94d')
    + z('path', '#d9a66b', d='M86 92 L62 100 Q54 108 62 116 L82 112 L76 150 Q78 162 90 158 L100 136 L110 158 Q122 162 124 150 L118 112 L138 116 Q146 108 138 100 L114 92Z')
    + s('path', d='M64 104 Q68 108 64 112 M136 104 Q132 108 136 112 M82 146 Q86 150 90 146 M110 146 Q114 150 118 146', stroke='#ffffff', stroke_width=2.5)
    + dot(100, 104, 4, '#e04b5a') + dot(100, 120, 4, '#9ccf7a')
    + z('circle', '#d9a66b', cx=100, cy=72, r=22)
    + dot(92, 70) + dot(108, 70) + cheeks(86, 114, 79, 4.5, 3) + s('path', d='M94 80 Q100 86 106 80', stroke='#ffffff', stroke_width=2.5)
    + sparkle(40, 60, 8) + sparkle(160, 66, 8, '#8fc7e8')
)
