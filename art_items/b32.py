from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def _r(v):
    return round(v, 1)


def rot(pts, cx, cy, deg):
    a = math.radians(deg)
    c, sn = math.cos(a), math.sin(a)
    return [(_r(cx + x * c - y * sn), _r(cy + x * sn + y * c)) for x, y in pts]


def kface(cx, cy, sp=10, r=3.5):
    return (dot(cx - sp, cy, r) + dot(cx + sp, cy, r) + cheeks(cx - sp - 8, cx + sp + 8, cy + 8, 5, 3)
            + s('path', d=f'M{cx - 4} {cy + 7} Q{cx} {cy + 11} {cx + 4} {cy + 7}', stroke_width=2.5))


def leaf(x1, y1, x2, y2, w=0.4):
    """先端 x2,y2 の葉（左右ふくらみ）"""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    nx, ny = -dy * w, dx * w
    return (f'M{x1} {y1} Q{_r(mx + nx)} {_r(my + ny)} {x2} {y2} '
            f'Q{_r(mx - nx)} {_r(my - ny)} {x1} {y1}Z')


def tri_tree(cx, base, w, h, col='#7cc4a0', tiers=3):
    o = z('rect', '#9a6a3f', x=cx - 6, y=base - 4, width=12, height=18, rx=2)
    for i in range(tiers):
        top = base - h + i * h * 0.28
        bot = base - h * 0.62 + i * h * 0.28 + h * 0.1
        ww = w * (0.55 + 0.22 * i)
        o += z('path', col, d=f'M{cx} {_r(top)} L{_r(cx + ww / 2)} {_r(bot)} Q{cx} {_r(bot + 6)} {_r(cx - ww / 2)} {_r(bot)}Z')
    return o


def palm(bx, by, tx, ty, size=1.0):
    k = size
    o = z('path', '#d9a66b', d=f'M{bx - 8 * k} {by} Q{_r((bx + tx) / 2 - 10 * k)} {_r((by + ty) / 2)} {tx - 5 * k} {ty} L{tx + 5 * k} {ty} Q{_r((bx + tx) / 2 + 4 * k)} {_r((by + ty) / 2)} {bx + 8 * k} {by}Z')
    for t in (0.25, 0.45, 0.65, 0.82):
        yy = by + (ty - by) * t
        xx = bx + (tx - bx) * t - 3 * k
        o += s('path', d=f'M{_r(xx - 6 * k)} {_r(yy)} Q{_r(xx)} {_r(yy + 3 * k)} {_r(xx + 6 * k)} {_r(yy - 1)}', stroke_width=2)
    for ang, ln in ((200, 48), (240, 44), (300, 44), (340, 48), (160, 40), (20, 40)):
        a = math.radians(ang)
        ex, ey = tx + ln * k * math.cos(a), ty + ln * k * math.sin(a) + 14 * k
        o += z('path', '#7cc4a0', d=leaf(tx, ty, _r(ex), _r(ey), 0.3))
    o += z('circle', '#9a6a3f', cx=tx - 6 * k, cy=ty + 8 * k, r=6 * k) + z('circle', '#9a6a3f', cx=tx + 6 * k, cy=ty + 9 * k, r=6 * k)
    return o


def puff(cx, cy, w, col='#ffffff'):
    k = w / 100
    return z('path', col, d=(f'M{_r(cx - 46 * k)} {cy} Q{_r(cx - 58 * k)} {_r(cy - 22 * k)} {_r(cx - 30 * k)} {_r(cy - 26 * k)} '
                              f'Q{_r(cx - 20 * k)} {_r(cy - 52 * k)} {_r(cx + 6 * k)} {_r(cy - 44 * k)} '
                              f'Q{_r(cx + 30 * k)} {_r(cy - 50 * k)} {_r(cx + 34 * k)} {_r(cy - 24 * k)} '
                              f'Q{_r(cx + 58 * k)} {_r(cy - 20 * k)} {_r(cx + 46 * k)} {cy}Z'))


# 1 cactus
ITEMS['cactus'] = (
    z('path', '#7cc4a0', d='M74 116 Q58 116 58 100 L58 78 Q58 70 66 70 Q74 70 74 78 L74 100 L80 100 L80 116Z')
    + z('path', '#7cc4a0', d='M126 96 L136 96 L136 70 Q136 62 144 62 Q152 62 152 70 L152 92 Q152 110 134 110 L126 110Z')
    + z('path', '#7cc4a0', d='M76 140 L76 64 Q76 40 100 40 Q124 40 124 64 L124 140Z')
    + s('path', d='M88 56 L84 52 M114 56 L118 52 M86 120 L82 120 M116 116 L120 116 M100 128 L100 132 M64 86 L60 86 M146 78 L150 78', stroke_width=2)
    + z('circle', '#f6a6b8', cx=100, cy=38, r=8) + dot(100, 38, 3, '#ffe27a')
    + kface(100, 88)
    + z('path', '#e8735a', d='M70 140 L130 140 L122 182 L78 182Z') + z('rect', '#e8735a', x=62, y=132, width=76, height=14, rx=3))

# 2 forest
ITEMS['forest'] = (
    z('rect', '#9a6a3f', x=46, y=120, width=10, height=40, rx=2)
    + z('circle', '#9ccf7a', cx=51, cy=102, r=28)
    + z('rect', '#9a6a3f', x=144, y=124, width=10, height=36, rx=2)
    + z('circle', '#7cc4b0', cx=149, cy=108, r=24)
    + tri_tree(100, 160, 74, 124, '#7cc4a0')
    + z('path', '#9ccf7a', d='M24 172 Q24 158 40 158 L160 158 Q176 158 176 172 Q176 180 168 180 L32 180 Q24 180 24 172Z')
    + s('path', d='M60 168 L64 162 L68 168 M128 170 L132 164 L136 170', stroke_width=2)
    + s('circle', '#e8735a', cx=44, cy=96, r=3.5, stroke_width=1.5) + s('circle', '#e8735a', cx=60, cy=108, r=3.5, stroke_width=1.5)
    + s('circle', '#e8735a', cx=48, cy=116, r=3.5, stroke_width=1.5))

# 3 palm-tree
ITEMS['palm-tree'] = (
    z('path', '#f5d58a', d='M30 180 Q40 152 100 150 Q160 152 170 180Z')
    + palm(110, 164, 96, 66, 1.15)
    + s('path', d='M54 172 L60 172 M140 168 L146 168', stroke_width=2))

# 4 pine-tree
ITEMS['pine-tree'] = (
    z('rect', '#9a6a3f', x=92, y=156, width=16, height=24, rx=2)
    + z('path', '#7cc4a0', d='M100 104 L150 156 Q100 166 50 156Z')
    + z('path', '#7cc4a0', d='M100 70 L140 120 Q100 130 60 120Z')
    + z('path', '#7cc4a0', d='M100 28 L128 82 Q100 90 72 82Z')
    + s('path', d='M80 182 L120 182', stroke_width=2.5)
    + s('path', d='M76 112 L84 108 M122 140 L130 136 M84 148 L90 144 M112 74 L118 70', stroke_width=2))

# 5 bamboo
def stalk(x, top, bot, w=14):
    o = z('rect', '#9ccf7a', x=x - w / 2, y=top, width=w, height=bot - top, rx=4)
    y = top + 30
    while y < bot - 8:
        o += s('path', d=f'M{x - w / 2 - 2} {y} L{x + w / 2 + 2} {y}', stroke_width=3)
        y += 34
    return o


ITEMS['bamboo'] = (
    stalk(70, 40, 182) + stalk(104, 24, 182, 16) + stalk(138, 52, 182)
    + z('path', '#7cc4a0', d=leaf(104, 58, 150, 36, 0.22)) + z('path', '#7cc4a0', d=leaf(104, 58, 140, 60, 0.22))
    + z('path', '#7cc4a0', d=leaf(70, 74, 30, 56, 0.22)) + z('path', '#7cc4a0', d=leaf(70, 74, 34, 84, 0.22))
    + z('path', '#7cc4a0', d=leaf(138, 120, 172, 106, 0.22)) + z('path', '#7cc4a0', d=leaf(138, 120, 170, 132, 0.22))
    + z('path', '#7cc4a0', d=leaf(104, 126, 76, 116, 0.22))
    + s('path', d='M40 182 L170 182', stroke_width=2.5))

# 6 four-leaf-clover
_heart = [(0, 0), (-30, -22), (-30, -46), (-14, -54), (0, -44), (14, -54), (30, -46), (30, -22)]
_cl = ''
for ang in (45, 135, 225, 315):
    p = rot(_heart, 100, 92, ang)
    _cl += z('path', '#9ccf7a', d=(f'M{p[0][0]} {p[0][1]} C{p[1][0]} {p[1][1]} {p[2][0]} {p[2][1]} {p[3][0]} {p[3][1]} '
                                   f'Q{p[4][0]} {p[4][1]} {p[4][0]} {p[4][1]} Q{p[4][0]} {p[4][1]} {p[5][0]} {p[5][1]} '
                                   f'C{p[6][0]} {p[6][1]} {p[7][0]} {p[7][1]} {p[0][0]} {p[0][1]}Z'))
    q = rot([(0, -6), (0, -34)], 100, 92, ang)
    _cl += s('path', d=f'M{q[0][0]} {q[0][1]} L{q[1][0]} {q[1][1]}', stroke_width=2)
ITEMS['four-leaf-clover'] = (s('path', d='M100 96 Q104 140 128 180', stroke_width=7) + s('path', d='M100 96 Q104 140 128 180', stroke='#7cc4a0', stroke_width=2.5)
                             + _cl + s('circle', '#9ccf7a', cx=100, cy=92, r=5, stroke_width=2))

# 7 dandelion
_seeds = ''
for i in range(16):
    a = math.radians(i * 22.5)
    x1, y1 = 82 + 8 * math.cos(a), 74 + 8 * math.sin(a)
    x2, y2 = 82 + 34 * math.cos(a), 74 + 34 * math.sin(a)
    _seeds += s('path', d=f'M{_r(x1)} {_r(y1)} L{_r(x2)} {_r(y2)}', stroke_width=1.5) + s('circle', '#ffffff', cx=_r(x2), cy=_r(y2), r=4, stroke_width=1.5)


def flyseed(x, y, a):
    p = rot([(0, 0), (0, -14), (-5, -18), (5, -18), (0, -20)], x, y, a)
    return (s('path', d=f'M{p[0][0]} {p[0][1]} L{p[1][0]} {p[1][1]}', stroke_width=1.5)
            + s('path', d=f'M{p[1][0]} {p[1][1]} L{p[2][0]} {p[2][1]} M{p[1][0]} {p[1][1]} L{p[3][0]} {p[3][1]} M{p[1][0]} {p[1][1]} L{p[4][0]} {p[4][1]}', stroke_width=1.5)
            + dot(p[0][0], p[0][1], 2))


ITEMS['dandelion'] = (
    z('circle', '#f4f4f0', cx=82, cy=74, r=40) + _seeds + z('circle', '#d9a66b', cx=82, cy=74, r=8)
    + s('path', d='M82 82 Q86 140 80 178', stroke_width=7) + s('path', d='M82 82 Q86 140 80 178', stroke='#9ccf7a', stroke_width=2.5)
    + s('path', d='M140 178 L140 140', stroke_width=7) + s('path', d='M140 178 L140 140', stroke='#9ccf7a', stroke_width=2.5)
    + z('circle', '#ffc94d', cx=140, cy=130, r=18) + z('circle', '#ffe27a', cx=140, cy=130, r=10)
    + z('path', '#7cc4a0', d='M80 178 Q50 166 46 140 Q62 150 66 144 Q72 160 80 178Z')
    + z('path', '#7cc4a0', d='M82 178 Q112 168 120 146 Q104 154 100 148 Q94 164 82 178Z')
    + flyseed(146, 60, 30) + flyseed(164, 88, 50) + flyseed(132, 34, 15)
    + s('path', d='M40 180 L160 180', stroke_width=2.5))

# 8 hydrangea
def floret(x, y, col, r=7):
    o = ''
    for dx, dy in ((0, -r), (r, 0), (0, r), (-r, 0)):
        o += s('circle', col, cx=x + dx, cy=y + dy, r=r * 0.85, stroke_width=1.8)
    return o + dot(x, y, 2.2, '#ffffff')


_fl = ''
_pos = [(100, 46), (78, 56), (122, 56), (62, 76), (100, 70), (138, 76), (80, 92), (120, 92), (100, 106), (60, 102), (140, 102), (100, 88), (82, 120), (118, 120)]
_cols = ['#8fb3e0', '#a98bd0', '#8fc7e8']
for i, (x, y) in enumerate(_pos):
    _fl += floret(x, y, _cols[i % 3])
ITEMS['hydrangea'] = (
    z('path', '#7cc4a0', d=leaf(96, 138, 40, 160, 0.35)) + z('path', '#7cc4a0', d=leaf(104, 138, 162, 158, 0.35))
    + s('path', d='M100 130 L100 182', stroke_width=6) + s('path', d='M100 130 L100 182', stroke='#7cc4a0', stroke_width=2)
    + z('circle', '#8fb3e0', cx=100, cy=86, r=52) + _fl
    + s('path', d='M54 162 L84 148 M146 160 L116 148', stroke_width=2))

# 9 lotus
ITEMS['lotus'] = (
    z('ellipse', '#8fc7e8', cx=100, cy=158, rx=80, ry=24)
    + s('path', d='M40 158 Q50 154 60 158 M140 168 Q150 164 160 168', stroke='#ffffff', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M38 150 A26 12 0 1 0 72 144 L56 148Z')
    + z('path', '#7cc4a0', d='M50 150 Q48 132 100 134 Q152 132 150 150 Q100 166 50 150Z')
    + z('path', '#f6a6b8', d='M100 140 Q46 140 40 106 Q74 108 100 140Z')
    + z('path', '#f6a6b8', d='M100 140 Q154 140 160 106 Q126 108 100 140Z')
    + z('path', '#f6a6b8', d='M100 140 Q60 120 70 74 Q96 96 100 140Z')
    + z('path', '#f6a6b8', d='M100 140 Q140 120 130 74 Q104 96 100 140Z')
    + z('path', '#f6a6b8', d='M100 140 Q80 100 100 50 Q120 100 100 140Z')
    + s('path', d='M100 70 L100 120 M76 92 L90 124 M124 92 L110 124', stroke='#f07a8a', stroke_width=2)
    + s('ellipse', '#ffe27a', cx=100, cy=138, rx=14, ry=5, stroke_width=2))

# 10 morning-glory
_mg = ''
for i in range(5):
    p = rot([(0, -14), (0, -40)], 124, 96, i * 72 + 36)
    _mg += s('path', d=f'M{p[0][0]} {p[0][1]} L{p[1][0]} {p[1][1]}', stroke='#ffffff', stroke_width=3)
def hleaf(x, y, ang, k=1.0):
    h = [(0, 0), (-22, -8), (-24, -34), (-8, -36), (0, -28), (8, -36), (24, -34), (22, -8), (0, -48)]
    P = rot([(a * k, b * k) for a, b in h], x, y, ang)
    return z('path', '#7cc4a0', d=(f'M{P[0][0]} {P[0][1]} C{P[1][0]} {P[1][1]} {P[2][0]} {P[2][1]} {P[3][0]} {P[3][1]} '
                                   f'Q{P[4][0]} {P[4][1]} {P[4][0]} {P[4][1]} Q{P[4][0]} {P[4][1]} {P[5][0]} {P[5][1]} '
                                   f'C{P[6][0]} {P[6][1]} {P[7][0]} {P[7][1]} {P[0][0]} {P[0][1]}Z'))


ITEMS['morning-glory'] = (
    s('path', d='M52 182 Q40 150 62 132 Q86 114 70 86 Q60 64 80 48 Q96 38 104 50', stroke_width=3)
    + s('path', d='M62 132 Q78 140 96 136', stroke_width=3)
    + hleaf(60, 136, -70, 0.9) + hleaf(72, 88, -60, 0.8) + hleaf(50, 174, -80, 0.7)
    + z('path', '#7cc4a0', d='M100 150 L92 132 L110 124 L114 146Z')
    + z('circle', '#8fb3e0', cx=124, cy=96, r=44) + _mg
    + z('circle', '#ffffff', cx=124, cy=96, r=12) + dot(124, 96, 4, '#ffe27a')
    + z('path', '#a98bd0', d='M150 168 Q140 150 152 134 Q164 150 156 168Z')
    + s('path', d='M152 168 Q150 178 146 182', stroke_width=3))

# 11 ginkgo-leaf
def ginkgo(x, y, ang, k=1.0, col='#ffc94d'):
    p = rot([(0, 0), (-50, -46), (-30, -66), (0, -64), (30, -66), (50, -46), (0, 34), (-4, -58), (4, -58)], 0, 0, 0)
    pts = rot([(px * k, py * k) for px, py in p], x, y, ang)
    P = pts
    return (s('path', d=f'M{P[0][0]} {P[0][1]} L{P[6][0]} {P[6][1]}', stroke_width=4)
            + s('path', d=f'M{P[0][0]} {P[0][1]} L{P[6][0]} {P[6][1]}', stroke='#d9a66b', stroke_width=1.5)
            + z('path', col, d=(f'M{P[0][0]} {P[0][1]} L{P[1][0]} {P[1][1]} Q{P[2][0]} {P[2][1]} {P[3][0]} {P[3][1]} '
                                f'L{P[0][0]} {P[0][1]} L{P[3][0]} {P[3][1]} Q{P[4][0]} {P[4][1]} {P[5][0]} {P[5][1]}Z'))
            + s('path', d=f'M{P[0][0]} {P[0][1]} L{P[7][0]} {P[7][1]} M{P[0][0]} {P[0][1]} L{P[8][0]} {P[8][1]}', stroke_width=1.5))


ITEMS['ginkgo-leaf'] = (ginkgo(72, 120, -25, 0.95, '#f5d58a') + ginkgo(122, 100, 20, 1.15, '#ffc94d')
                        + dot(112, 66, 3.5) + dot(136, 74, 3.5) + cheeks(104, 142, 78, 5, 3)
                        + s('path', d='M120 76 Q125 80 129 77', stroke_width=2.5))

# 12 acorns
def acorn(cx, cy, k=1.0, ang=0):
    def P(pts):
        return rot([(x * k, y * k) for x, y in pts], cx, cy, ang)
    b = P([(-28, -4), (-28, 30), (0, 52), (28, 30), (28, -4)])
    c = P([(-34, 0), (-36, -30), (0, -34), (36, -30), (34, 0), (0, 6)])
    st = P([(0, -32), (4, -44), (10, -48)])
    pat = P([(-20, -22), (-6, -6), (-6, -28), (10, -6), (10, -28), (24, -10), (24, -24), (30, -16)])
    f = P([(-11, 14), (11, 14), (0, 24)])
    return (z('path', '#d9a66b', d=f'M{b[0][0]} {b[0][1]} L{b[1][0]} {b[1][1]} Q{b[2][0]} {b[2][1]} {b[2][0]} {b[2][1]} Q{b[2][0]} {b[2][1]} {b[3][0]} {b[3][1]} L{b[4][0]} {b[4][1]}Z')
            + s('path', d=f'M{st[0][0]} {st[0][1]} Q{st[1][0]} {st[1][1]} {st[2][0]} {st[2][1]}', stroke_width=5)
            + z('path', '#9a6a3f', d=f'M{c[0][0]} {c[0][1]} Q{c[1][0]} {c[1][1]} {c[2][0]} {c[2][1]} Q{c[3][0]} {c[3][1]} {c[4][0]} {c[4][1]} Q{c[5][0]} {c[5][1]} {c[0][0]} {c[0][1]}Z')
            + s('path', d=f'M{pat[0][0]} {pat[0][1]} L{pat[1][0]} {pat[1][1]} M{pat[2][0]} {pat[2][1]} L{pat[3][0]} {pat[3][1]} M{pat[4][0]} {pat[4][1]} L{pat[5][0]} {pat[5][1]} M{pat[6][0]} {pat[6][1]} L{pat[7][0]} {pat[7][1]}', stroke_width=1.5)
            + dot(f[0][0], f[0][1], 3.2 * k) + dot(f[1][0], f[1][1], 3.2 * k)
            + cheeks(_r(f[0][0] - 6 * k), _r(f[1][0] + 6 * k), _r(f[0][1] + 7 * k), 4.5 * k, 2.8 * k)
            + s('path', d=f'M{_r(f[2][0] - 3 * k)} {_r(f[2][1] - 2 * k)} Q{f[2][0]} {_r(f[2][1] + 1.5 * k)} {_r(f[2][0] + 3 * k)} {_r(f[2][1] - 2 * k)}', stroke_width=2.2))


ITEMS['acorns'] = (z('path', '#ffc94d', d=leaf(40, 170, 92, 150, 0.3)) + z('path', '#e8735a', d=leaf(170, 172, 126, 146, 0.3))
                   + acorn(70, 98, 1.15, -12) + acorn(134, 112, 1.0, 14)
                   + s('path', d='M30 180 L170 180', stroke_width=2.5))

# 13 pinecone
_sc = ''
for row, (y, w, n) in enumerate([(62, 34, 3), (84, 50, 4), (106, 56, 5), (128, 54, 4), (148, 42, 3)]):
    for j in range(n):
        x = 100 - w / 2 + (j + 0.5) * w / n
        _sc += s('path', '#d9a66b', d=f'M{_r(x - w / n / 2 - 2)} {y} Q{_r(x)} {y + 22} {_r(x + w / n / 2 + 2)} {y}', stroke_width=2.2)
ITEMS['pinecone'] = (
    s('path', d='M100 44 Q104 30 112 26', stroke_width=5)
    + z('path', '#9a6a3f', d='M100 40 Q148 50 146 112 Q140 170 100 178 Q60 170 54 112 Q52 50 100 40Z')
    + _sc
    + z('path', '#7cc4a0', d=leaf(110, 30, 150, 22, 0.15)) + z('path', '#7cc4a0', d=leaf(110, 30, 146, 40, 0.15)))

# 14 winter-tree
ITEMS['winter-tree'] = (
    z('path', '#ffffff', d='M24 176 Q30 156 70 158 Q100 150 130 158 Q170 156 176 176 Q176 184 168 184 L32 184 Q24 184 24 176Z')
    + z('path', '#9a6a3f', d='M90 162 L94 110 L64 80 L60 62 L70 74 L96 98 L94 64 L84 46 L96 58 L102 86 L120 60 L126 40 L130 50 L124 70 L106 100 L136 84 L148 70 L146 86 L108 112 L110 162Z')
    + z('path', '#ffffff', d='M56 60 Q60 52 68 56 Q74 62 68 72 Q62 68 56 60Z')
    + z('path', '#ffffff', d='M80 44 Q86 36 94 42 Q98 50 92 56 Q86 50 80 44Z')
    + z('path', '#ffffff', d='M120 40 Q126 30 134 38 Q136 46 128 52 Q122 46 120 40Z')
    + z('path', '#ffffff', d='M138 70 Q146 62 154 70 Q154 78 146 82 Q140 76 138 70Z')
    + z('path', '#ffffff', d='M84 80 Q90 74 98 80 L96 90 Q88 86 84 80Z')
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=3, stroke_width=1.5) for x, y in ((36, 40), (48, 110), (160, 112), (168, 40), (40, 140), (150, 140), (100, 24))))

# 15 ocean-waves
ITEMS['ocean-waves'] = (
    z('path', '#8fb3e0', d='M24 182 L24 150 Q60 134 96 152 Q130 168 176 146 L176 182Z')
    + z('path', '#8fc7e8', d='M24 160 Q30 92 82 56 Q134 26 164 60 Q178 78 164 96 Q154 106 142 98 Q150 82 136 74 Q116 66 104 92 Q96 116 116 136 Q90 150 60 156 Q40 160 24 160Z')
    + z('path', '#ffffff', d='M142 98 Q150 82 136 74 Q122 70 114 82 Q126 78 132 86 Q136 94 142 98Z')
    + s('path', '#ffffff', d='M100 56 Q130 40 154 54 Q136 52 120 60Z', stroke_width=2)
    + s('path', d='M40 172 Q50 166 60 172 M110 174 Q120 168 130 174', stroke='#ffffff', stroke_width=3)
    + s('path', d='M60 110 Q66 90 80 76', stroke='#ffffff', stroke_width=3)
    + s('circle', '#ffffff', cx=170, cy=110, r=4, stroke_width=1.5) + s('circle', '#ffffff', cx=160, cy=120, r=3, stroke_width=1.5))

# 16 island
ITEMS['island'] = (
    z('ellipse', '#8fc7e8', cx=100, cy=166, rx=82, ry=18)
    + z('path', '#f5d58a', d='M40 164 Q56 136 100 134 Q146 136 162 164 Q100 174 40 164Z')
    + palm(104, 152, 88, 70, 1.0)
    + s('path', d='M30 178 Q38 174 46 178 M150 180 Q158 176 166 180', stroke='#ffffff', stroke_width=2.5)
    + puff(150, 40, 40))

# 17 river
ITEMS['river'] = (
    z('path', '#9ccf7a', d='M24 60 Q24 40 44 40 L156 40 Q176 40 176 60 L176 164 Q176 180 160 180 L40 180 Q24 180 24 164Z')
    + s('path', '#8fc7e8', d='M92 40 L116 40 Q140 66 110 88 Q78 110 106 140 Q120 160 128 180 L84 180 Q80 160 68 144 Q46 110 88 84 Q110 66 92 40Z')
    + s('path', d='M104 54 Q110 60 104 66 M96 112 Q90 118 96 124 M100 150 Q106 158 104 166', stroke='#ffffff', stroke_width=2.5)
    + z('circle', '#7cc4a0', cx=48, cy=74, r=12) + z('circle', '#7cc4a0', cx=150, cy=124, r=13) + z('circle', '#7cc4a0', cx=58, cy=154, r=10)
    + s('path', d='M144 64 L148 56 L152 64 M38 112 L42 104 L46 112 M150 162 L154 154 L158 162', stroke_width=2)
    + s('circle', '#f6a6b8', cx=140, cy=86, r=4, stroke_width=1.5) + s('circle', '#ffe27a', cx=40, cy=128, r=4, stroke_width=1.5))

# 18 waterfall
ITEMS['waterfall'] = (
    z('path', '#b9a99c', d='M24 150 L24 52 Q24 34 44 36 L80 40 L80 150Z')
    + z('path', '#b9a99c', d='M120 150 L120 44 L156 36 Q176 34 176 52 L176 150Z')
    + z('path', '#9ccf7a', d='M24 54 Q24 32 46 34 L82 40 L82 52 Q60 46 24 60Z')
    + z('path', '#9ccf7a', d='M118 52 L118 42 L156 34 Q176 34 176 54 Q150 46 118 52Z')
    + z('rect', '#8fc7e8', x=80, y=42, width=40, height=118)
    + s('path', d='M90 54 L90 90 M104 64 L104 120 M112 50 L112 80 M94 104 L94 140', stroke='#ffffff', stroke_width=3)
    + z('ellipse', '#8fc7e8', cx=100, cy=166, rx=78, ry=16)
    + puff(100, 164, 70)
    + s('path', d='M34 172 Q42 168 50 172 M150 174 Q158 170 166 174', stroke='#ffffff', stroke_width=2.5))

# 19 volcano
ITEMS['volcano'] = (
    puff(80, 54, 48, '#c9d3db') + puff(116, 40, 56, '#c9d3db')
    + z('path', '#9a6a3f', d='M20 180 L78 76 Q100 70 122 76 L180 180Z')
    + z('path', '#e8735a', d='M78 76 Q100 70 122 76 L126 86 Q118 98 114 92 Q108 108 100 96 Q92 112 86 94 Q80 100 74 86Z')
    + z('path', '#ffc94d', d='M84 80 Q100 76 116 80 Q100 86 84 80Z')
    + s('path', d='M54 140 L64 132 M140 150 L130 142 M100 160 L108 154', stroke_width=2)
    + s('circle', '#e8735a', cx=58, cy=52, r=4, stroke_width=1.5) + s('circle', '#e8735a', cx=144, cy=58, r=4, stroke_width=1.5))

# 20 desert
_sr = ''
for i in range(10):
    p = rot([(0, -24), (0, -32)], 146, 52, i * 36)
    _sr += s('path', d=f'M{p[0][0]} {p[0][1]} L{p[1][0]} {p[1][1]}', stroke_width=2.5)
ITEMS['desert'] = (
    z('circle', '#ffc94d', cx=146, cy=52, r=18) + _sr
    + z('path', '#f5d58a', d='M24 180 L24 130 Q70 106 120 134 Q150 120 176 128 L176 180Z')
    + z('path', '#f5b971', d='M24 180 L24 158 Q80 140 176 162 L176 180Z')
    + z('path', '#7cc4a0', d='M62 118 Q50 118 50 106 L50 92 Q50 86 56 86 Q62 86 62 92 L62 106 L66 106 L66 118Z')
    + z('path', '#7cc4a0', d='M88 104 L94 104 L94 84 Q94 78 100 78 Q106 78 106 84 L106 100 Q106 112 92 112 L88 112Z')
    + z('path', '#7cc4a0', d='M64 136 L64 74 Q64 60 76 60 Q88 60 88 74 L88 136Z')
    + s('path', d='M72 76 L72 84 M80 96 L80 104 M72 112 L72 120', stroke_width=2)
    + s('path', d='M140 146 Q146 142 152 146 M40 166 Q46 162 52 166', stroke='#d9a66b', stroke_width=2.5))
