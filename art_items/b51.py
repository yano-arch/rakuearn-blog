from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def qpt(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
    return x, y


def bunting(p0, p1, p2, colors, n, size=11, drop=16):
    """ひもに三角旗を並べる（文字なしのガーランド）"""
    o = s('path', d=f'M{p0[0]} {p0[1]} Q{p1[0]} {p1[1]} {p2[0]} {p2[1]}', stroke_width=2.5)
    for i in range(n):
        t1 = (i + 0.15) / n
        t2 = (i + 0.85) / n
        a = qpt(p0, p1, p2, t1)
        b = qpt(p0, p1, p2, t2)
        m = qpt(p0, p1, p2, (t1 + t2) / 2)
        o += z('path', colors[i % len(colors)],
               d=f'M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f} L{m[0]:.1f} {m[1] + drop:.1f}Z', stroke_width=2.5)
    return o


def balloon(cx, cy, rx, ry, color, sx, sy):
    """風船（ひもの終点 sx, sy まで）"""
    by = cy + ry
    return (s('path', d=f'M{cx} {by + 4} Q{(cx + sx) / 2 + 6} {(by + sy) / 2} {sx} {sy}', stroke_width=2)
            + z('path', color, d=f'M{cx - 4} {by + 6} L{cx + 4} {by + 6} L{cx} {by - 1}Z', stroke_width=2)
            + z('ellipse', color, cx=cx, cy=cy, rx=rx, ry=ry)
            + s('path', '#ffffff', d=f'M{cx - rx * 0.55:.1f} {cy - ry * 0.2:.1f} Q{cx - rx * 0.5:.1f} {cy - ry * 0.6:.1f} {cx - rx * 0.15:.1f} {cy - ry * 0.7:.1f}',
                stroke='#ffffff', stroke_width=3.5))


def confetti_bits(pts):
    """紙吹雪（小さい四角・丸・くるくる）"""
    o = ''
    for kind, x, y, c, r in pts:
        if kind == 'r':
            o += s('rect', c, x=x - 4, y=y - 2.5, width=8, height=5, rx=1, transform=f'rotate({r} {x} {y})', stroke_width=2)
        elif kind == 'c':
            o += s('circle', c, cx=x, cy=y, r=3.5, stroke_width=2)
        else:
            o += s('path', d=f'M{x} {y} q4 -6 8 0 q4 6 8 0', stroke=c, stroke_width=3)
    return o


def heart_d(cx, cy, w):
    k = w / 28
    return (f'M{cx} {cy + 16 * k:.1f} C{cx - 16 * k:.1f} {cy + 4 * k:.1f} {cx - 16 * k:.1f} {cy - 12 * k:.1f} {cx - 7 * k:.1f} {cy - 12 * k:.1f} '
            f'C{cx - 2 * k:.1f} {cy - 12 * k:.1f} {cx} {cy - 8 * k:.1f} {cx} {cy - 5 * k:.1f} '
            f'C{cx} {cy - 8 * k:.1f} {cx + 2 * k:.1f} {cy - 12 * k:.1f} {cx + 7 * k:.1f} {cy - 12 * k:.1f} '
            f'C{cx + 16 * k:.1f} {cy - 12 * k:.1f} {cx + 16 * k:.1f} {cy + 4 * k:.1f} {cx} {cy + 16 * k:.1f}Z')


def sparkle(cx, cy, r, c='#ffc94d'):
    return s('path', c, d=f'M{cx} {cy - r} Q{cx + r * 0.2} {cy - r * 0.2} {cx + r} {cy} Q{cx + r * 0.2} {cy + r * 0.2} {cx} {cy + r} '
                         f'Q{cx - r * 0.2} {cy + r * 0.2} {cx - r} {cy} Q{cx - r * 0.2} {cy - r * 0.2} {cx} {cy - r}Z', stroke_width=2)


def mini_face(cx, cy, r, hair):
    k = r / 34
    o = z('circle', '#ffd9b8', cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{cx - r} {cy - 2 * k:.1f} Q{cx - 32 * k:.1f} {cy - 36 * k:.1f} {cx} {cy - 35 * k:.1f} Q{cx + 32 * k:.1f} {cy - 36 * k:.1f} {cx + r} {cy - 2 * k:.1f} Q{cx + 20 * k:.1f} {cy - 18 * k:.1f} {cx} {cy - 17 * k:.1f} Q{cx - 20 * k:.1f} {cy - 18 * k:.1f} {cx - r} {cy - 2 * k:.1f}Z')
    o += dot(cx - 12 * k, cy + 2 * k, 3) + dot(cx + 12 * k, cy + 2 * k, 3) + cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, 5, 3)
    o += s('path', '#c0504d', d=f'M{cx - 6 * k:.1f} {cy + 13 * k:.1f} Q{cx} {cy + 26 * k:.1f} {cx + 6 * k:.1f} {cy + 13 * k:.1f}Z', stroke_width=2.5)
    return o


# 1. balloon bunch
ITEMS['balloon-bunch'] = (
    balloon(64, 72, 24, 29, '#8fc7e8', 100, 168)
    + balloon(136, 72, 24, 29, '#9ccf7a', 100, 168)
    + balloon(78, 112, 22, 26, '#ffc94d', 100, 168)
    + balloon(124, 112, 22, 26, '#a98bd0', 100, 168)
    + balloon(100, 56, 26, 31, '#f07a8a', 100, 168)
    + z('path', '#e8735a', d='M100 166 Q84 156 82 170 Q86 180 100 166Z', stroke_width=2.5)
    + z('path', '#e8735a', d='M100 166 Q116 156 118 170 Q114 180 100 166Z', stroke_width=2.5)
    + s('path', d='M98 168 L92 184 M102 168 L108 184', stroke_width=2.5)
)

# 2. confetti
ITEMS['confetti'] = (
    thick('M34 40 Q54 30 60 50 Q66 70 86 58', '#f07a8a', 8, 4)
    + thick('M120 34 Q136 50 156 40 Q174 32 170 56', '#8fc7e8', 8, 4)
    + thick('M44 132 Q30 150 48 160 Q66 170 58 184', '#9ccf7a', 8, 4)
    + thick('M146 120 Q166 132 156 150 Q146 168 168 176', '#ffc94d', 8, 4)
    + z('path', '#ffc94d', d='M84 92 L104 84 L110 100 L90 108Z', stroke_width=2.5)
    + z('path', '#a98bd0', d='M118 70 L134 76 L128 92 L112 86Z', stroke_width=2.5)
    + z('path', '#7cc4b0', d='M118 118 L138 112 L142 128 L122 134Z', stroke_width=2.5)
    + z('circle', '#f6a6b8', cx=72, cy=120, r=9, stroke_width=2.5)
    + z('path', '#e8735a', d='M86 140 L100 128 L108 144Z', stroke_width=2.5)
    + z('circle', '#8fb3e0', cx=100, cy=166, r=7, stroke_width=2.5)
    + confetti_bits([('r', 62, 84, '#8fc7e8', 30), ('r', 148, 96, '#f07a8a', -20), ('c', 98, 46, '#9ccf7a', 0),
                     ('c', 168, 92, '#a98bd0', 0), ('r', 128, 156, '#a98bd0', 40), ('c', 36, 98, '#ffc94d', 0),
                     ('r', 82, 176, '#7cc4b0', -30), ('c', 120, 182, '#f07a8a', 0), ('s', 72, 152, '#e8735a', 0),
                     ('s', 92, 26, '#7cc4b0', 0), ('r', 106, 112, '#f07a8a', 60), ('c', 142, 62, '#ffc94d', 0)])
)

# 3. pinata (donkey)
ITEMS['pinata'] = (
    s('path', d='M106 22 L106 96', stroke_width=2.5) + s('circle', cx=106, cy=22, r=4, stroke_width=2.5)
    + z('rect', '#f5d58a', x=78, y=134, width=14, height=40, rx=3)
    + z('rect', '#f5d58a', x=124, y=134, width=14, height=40, rx=3)
    + z('rect', '#f5d58a', x=60, y=96, width=94, height=48, rx=10)
    + s('path', '#f07a8a', d='M60 108 L154 108 L154 118 L60 118Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M60 128 L154 128 L154 136 L60 136Z', stroke_width=2.5)
    + s('path', d='M154 104 Q172 110 168 128', stroke_width=3)
    + s('path', '#f07a8a', d='M166 126 L162 140 M168 128 L170 142 M164 128 L156 138', stroke='#f07a8a', stroke_width=4)
    + z('rect', '#f5d58a', x=46, y=58, width=30, height=50, rx=8)
    + z('path', '#f5d58a', d='M52 62 L46 30 L60 48Z', stroke_width=2.5)
    + z('path', '#f5d58a', d='M68 58 L72 28 L78 50Z', stroke_width=2.5)
    + s('path', '#f07a8a', d='M76 58 L92 50 L88 60 L100 56 L92 70 L76 72Z', stroke_width=2.5)
    + z('rect', '#f5d58a', x=30, y=74, width=40, height=26, rx=10)
    + dot(48, 70, 3.2) + dot(40, 86, 2.2) + cheeks(56, 56, 88, 5, 3)
    + s('path', d='M38 92 Q44 96 50 92', stroke_width=2.5)
)

# 4. festival food stall (yatai)
ITEMS['festival-stall'] = (
    z('rect', '#d9a66b', x=42, y=56, width=8, height=118)
    + z('rect', '#d9a66b', x=150, y=56, width=8, height=118)
    + z('path', '#e8735a', d='M30 64 L48 34 L152 34 L170 64Z')
    + s('path', '#ffffff', d='M65 34 L56 64 L74 64 L82 34Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M101 34 L96 64 L114 64 L117 34Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M135 34 L134 64 L152 64 L152 34Z', stroke_width=2.5)
    + z('path', '#ffffff', d='M30 64 L170 64 L170 72 Q161 82 152 72 Q144 82 135 72 Q126 82 117 72 Q108 82 100 72 Q91 82 83 72 Q74 82 65 72 Q56 82 48 72 Q39 82 30 72Z', stroke_width=2.5)
    + s('path', d='M66 80 L66 88 M134 80 L134 88', stroke_width=2)
    + z('ellipse', '#f07a8a', cx=66, cy=100, rx=11, ry=13)
    + s('path', d='M57 94 L75 94 M57 106 L75 106', stroke_width=2)
    + z('ellipse', '#ffc94d', cx=134, cy=100, rx=11, ry=13)
    + s('path', d='M125 94 L143 94 M125 106 L143 106', stroke_width=2)
    + z('rect', '#5b6b7a', x=74, y=118, width=52, height=12, rx=3)
    + s('circle', '#f5b971', cx=86, cy=114, r=6, stroke_width=2.5)
    + s('circle', '#f5b971', cx=100, cy=114, r=6, stroke_width=2.5)
    + s('circle', '#f5b971', cx=114, cy=114, r=6, stroke_width=2.5)
    + z('rect', '#f6e0c4', x=36, y=132, width=128, height=42, rx=3)
    + s('path', d='M36 146 L164 146', stroke_width=2)
    + s('path', d='M70 146 L70 174 M100 146 L100 174 M130 146 L130 174', stroke_width=2)
    + s('path', d='M24 180 L176 180', stroke_width=2.5)
)

# 5. goldfish scooping
def goldfish(cx, cy, flip=1, c='#e8735a'):
    f = flip
    return (z('path', c, d=f'M{cx - 10 * f} {cy} L{cx - 22 * f} {cy - 9} L{cx - 19 * f} {cy} L{cx - 22 * f} {cy + 9}Z', stroke_width=2.5)
            + z('ellipse', c, cx=cx, cy=cy, rx=13, ry=8, stroke_width=2.5)
            + dot(cx + 6 * f, cy - 2, 2))


ITEMS['goldfish-scooping'] = (
    z('path', '#8fc7e8', d='M24 116 Q24 96 60 96 L140 96 Q176 96 176 116 L170 170 Q168 180 156 180 L44 180 Q32 180 30 170Z')
    + s('path', d='M30 116 Q100 126 170 116', stroke='#ffffff', stroke_width=3)
    + goldfish(56, 140, 1) + goldfish(100, 160, -1, '#e04b5a') + goldfish(140, 140, -1)
    + goldfish(84, 130, 1, '#f5b971')
    + s('path', d='M150 116 L182 60', stroke_width=10) + s('path', d='M150 116 L182 60', stroke='#f6a6b8', stroke_width=5)
    + z('circle', '#f6a6b8', cx=136, cy=126, r=20)
    + s('circle', '#ffffff', cx=136, cy=126, r=14, stroke_width=2.5)
    + goldfish(136, 126, 1)
    + z('path', '#ffffff', d='M30 44 Q30 76 56 78 Q82 76 82 44Z')
    + s('path', d='M28 44 L84 44', stroke_width=3)
    + s('path', d='M36 58 Q56 64 76 58', stroke='#8fc7e8', stroke_width=3)
    + goldfish(58, 66, 1)
)

# 6. candy apple
ITEMS['candy-apple'] = (
    z('rect', '#f6e0c4', x=95, y=20, width=10, height=64, rx=3)
    + z('path', '#e04b5a', d='M100 70 Q72 58 56 80 Q42 106 56 136 Q70 162 100 156 Q130 162 144 136 Q158 106 144 80 Q128 58 100 70Z')
    + s('path', '#f07a8a', d='M56 126 Q64 146 80 150 Q90 140 96 152 Q104 142 112 150 Q122 140 132 150 Q144 144 146 128 Q130 136 100 134 Q74 136 56 126Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M66 92 Q70 80 82 76', stroke='#ffffff', stroke_width=5)
    + z('path', '#9ccf7a', d='M106 70 Q122 50 140 58 Q126 74 106 70Z', stroke_width=2.5)
    + dot(86, 106) + dot(114, 106) + cheeks(76, 124, 116, 7, 4)
    + s('path', d='M94 116 Q100 122 106 116', stroke_width=2.5)
    + z('ellipse', '#f6e0c4', cx=100, cy=166, rx=58, ry=10)
)

# 7. taiko drum
ITEMS['taiko-drum'] = (
    s('path', d='M62 140 L44 182 M138 140 L156 182 M52 162 L148 162', stroke_width=7)
    + s('path', d='M62 140 L44 182 M138 140 L156 182 M52 162 L148 162', stroke='#8b6b4f', stroke_width=3)
    + z('circle', '#e8735a', cx=100, cy=104, r=58)
    + z('circle', '#f6e0c4', cx=100, cy=104, r=46)
    + ''.join(dot(round(100 + 52 * cos(a * pi / 10), 1), round(104 + 52 * sin(a * pi / 10), 1), 2.6) for a in range(20))
    + dot(88, 104) + dot(112, 104) + cheeks(78, 122, 114, 6, 3.5)
    + s('path', d='M94 114 Q100 120 106 114', stroke_width=2.5)
    + s('path', d='M30 30 L74 66', stroke_width=9) + s('path', d='M30 30 L74 66', stroke='#d9a66b', stroke_width=4.5)
    + z('circle', '#d9a66b', cx=30, cy=30, r=6, stroke_width=2.5)
    + s('path', d='M170 30 L126 66', stroke_width=9) + s('path', d='M170 30 L126 66', stroke='#d9a66b', stroke_width=4.5)
    + z('circle', '#d9a66b', cx=170, cy=30, r=6, stroke_width=2.5)
    + s('path', d='M86 40 L82 30 M100 36 L100 26 M114 40 L118 30', stroke_width=2.5)
)

# 8. carnival mask
ITEMS['carnival-mask'] = (
    s('path', d='M150 124 L170 182', stroke_width=9) + s('path', d='M150 124 L170 182', stroke='#d9a66b', stroke_width=4.5)
    + z('path', '#7cc4b0', d='M118 76 Q110 40 126 24 Q136 50 126 78Z', stroke_width=2.5)
    + z('path', '#f07a8a', d='M128 80 Q136 44 158 34 Q154 64 134 84Z', stroke_width=2.5)
    + z('path', '#ffc94d', d='M136 88 Q160 64 178 66 Q164 90 140 94Z', stroke_width=2.5)
    + z('path', '#a98bd0', d='M28 102 Q30 74 64 76 Q86 78 100 90 Q114 78 136 76 Q170 74 172 102 Q170 132 136 128 Q114 126 100 114 Q86 126 64 128 Q30 132 28 102Z')
    + s('path', '#ffffff', d='M48 102 Q52 90 66 90 Q80 92 84 102 Q78 112 66 112 Q52 112 48 102Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M152 102 Q148 90 134 90 Q120 92 116 102 Q122 112 134 112 Q148 112 152 102Z', stroke_width=2.5)
    + dot(66, 102, 4) + dot(134, 102, 4)
    + s('path', d='M40 86 Q36 96 38 104 M160 86 Q164 96 162 104', stroke='#ffe27a', stroke_width=3)
    + dot(100, 102, 4, '#ffe27a') + s('circle', cx=100, cy=102, r=5, stroke_width=2)
    + dot(52, 120, 3, '#ffe27a') + dot(148, 120, 3, '#ffe27a')
)

# 9. music festival stage
ITEMS['music-festival'] = (
    z('path', '#ffe27a', d='M58 50 L36 140 L80 140Z', stroke_width=0)
    + z('path', '#ffe27a', d='M142 50 L120 140 L164 140Z', stroke_width=0)
    + z('rect', '#5b6b7a', x=28, y=36, width=144, height=14, rx=2)
    + s('path', d='M36 36 L48 50 L60 36 L72 50 L84 36 L96 50 L108 36 L120 50 L132 36 L144 50 L156 36 L168 50', stroke='#c9d3db', stroke_width=2)
    + z('rect', '#5b6b7a', x=28, y=50, width=10, height=96)
    + z('rect', '#5b6b7a', x=162, y=50, width=10, height=96)
    + s('rect', '#ffc94d', x=50, y=50, width=16, height=10, rx=2, stroke_width=2.5)
    + s('rect', '#ffc94d', x=134, y=50, width=16, height=10, rx=2, stroke_width=2.5)
    + z('rect', '#5b6b7a', x=44, y=106, width=22, height=34, rx=3)
    + s('circle', '#c9d3db', cx=55, cy=126, r=7, stroke_width=2.5) + dot(55, 113, 3, '#c9d3db')
    + z('rect', '#5b6b7a', x=134, y=106, width=22, height=34, rx=3)
    + s('circle', '#c9d3db', cx=145, cy=126, r=7, stroke_width=2.5) + dot(145, 113, 3, '#c9d3db')
    + s('path', d='M100 98 L100 140', stroke_width=3)
    + z('circle', '#5b6b7a', cx=100, cy=96, r=5, stroke_width=2.5)
    + s('path', '#f07a8a', d='M86 70 C80 64 78 60 81 56 C84 53 86 55 86 58 C86 55 88 53 91 56 C94 60 91 64 86 70Z', stroke_width=2)
    + s('path', d='M114 60 L114 76 M114 60 L124 58 L124 72', stroke_width=2.5)
    + dot(111, 77, 3.5) + dot(121, 73, 3.5)
    + z('rect', '#9a6a3f', x=24, y=140, width=152, height=12, rx=2)
    + z('circle', '#5a4033', cx=46, cy=172, r=13) + z('circle', '#2b2220', cx=78, cy=168, r=13)
    + z('circle', '#c9a36b', cx=110, cy=172, r=13) + z('circle', '#5a4033', cx=144, cy=168, r=13)
    + s('path', d='M64 166 L58 152 M92 162 L98 150 M128 164 L126 150 M158 162 L166 152', stroke_width=7)
    + s('path', d='M64 166 L58 152 M92 162 L98 150 M128 164 L126 150 M158 162 L166 152', stroke='#ffd9b8', stroke_width=3)
)

# 10. sparklers
def spark_burst(cx, cy, R, n=12, rot=0):
    o = ''
    for i in range(n):
        a = (rot + i * 360 / n) * pi / 180
        r1 = R * (0.35 if i % 2 else 0.3)
        r2 = R * (1.0 if i % 2 else 0.75)
        o += s('path', d=f'M{cx + r1 * cos(a):.1f} {cy + r1 * sin(a):.1f} L{cx + r2 * cos(a):.1f} {cy + r2 * sin(a):.1f}', stroke='#ffc94d', stroke_width=3)
    return o + z('circle', '#ffe27a', cx=cx, cy=cy, r=R * 0.22, stroke_width=2.5)


ITEMS['sparklers'] = (
    s('path', d='M92 150 L70 66', stroke_width=6) + s('path', d='M92 150 L70 66', stroke='#b9a99c', stroke_width=2.5)
    + s('path', d='M106 150 L130 70', stroke_width=6) + s('path', d='M106 150 L130 70', stroke='#b9a99c', stroke_width=2.5)
    + spark_burst(68, 58, 32, 14) + spark_burst(132, 62, 30, 14, 12)
    + sparkle(36, 104, 7, '#ffe27a') + sparkle(166, 108, 7, '#ffe27a') + sparkle(100, 30, 6, '#ffe27a')
    + dot(48, 120, 2.5, '#ffc94d') + dot(156, 128, 2.5, '#ffc94d') + dot(100, 92, 2.5, '#ffc94d')
    + z('path', '#7cc4b0', d='M70 186 L76 160 L124 160 L130 186Z')
    + z('path', '#ffd9b8', d='M76 166 Q72 140 86 136 L114 136 Q128 140 124 166Z')
    + s('path', d='M86 136 Q80 144 88 150 M100 136 L100 148 M114 136 Q120 144 112 150', stroke_width=2.5)
)

# 11. kid's birthday
ITEMS['kids-birthday'] = (
    z('path', '#8fb3e0', d='M62 184 Q64 128 100 124 Q136 128 138 184Z')
    + face(100, 84, '#ffd9b8', '#5a4033', 'open')
    + z('path', '#f07a8a', d='M78 56 L104 18 L120 52 Q100 46 78 56Z', stroke_width=2.5)
    + s('path', d='M86 44 L110 34 M94 32 L106 28', stroke='#ffe27a', stroke_width=3)
    + z('circle', '#ffe27a', cx=104, cy=18, r=6, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=97, y=124, width=6, height=16, stroke_width=2)
    + z('path', '#ffc94d', d='M100 124 Q94 116 100 108 Q106 116 100 124Z', stroke_width=2)
    + z('rect', '#f6e0c4', x=66, y=140, width=68, height=38, rx=4)
    + s('path', '#f6a6b8', d='M66 144 L134 144 L134 150 Q125 158 117 150 Q108 158 100 150 Q92 158 83 150 Q75 158 66 150Z', stroke_width=2.5)
    + dot(84, 166, 4, '#e04b5a') + dot(100, 166, 4, '#e04b5a') + dot(116, 166, 4, '#e04b5a')
    + z('circle', '#ffd9b8', cx=62, cy=160, r=9) + z('circle', '#ffd9b8', cx=138, cy=160, r=9)
    + confetti_bits([('r', 36, 40, '#9ccf7a', 30), ('c', 160, 36, '#a98bd0', 0), ('r', 164, 82, '#ffc94d', -20), ('c', 30, 96, '#f07a8a', 0)])
)

# 12. surprise party
ITEMS['surprise-party'] = (
    bunting((24, 26), (100, 62), (176, 26), ['#f07a8a', '#ffc94d', '#8fc7e8', '#9ccf7a', '#a98bd0'], 7, drop=16)
    + z('path', '#f5b971', d='M62 186 Q64 138 100 134 Q136 138 138 186Z')
    + s('path', d='M72 150 L46 96', stroke_width=12) + s('path', d='M72 150 L46 96', stroke='#f5b971', stroke_width=6)
    + s('path', d='M128 150 L154 96', stroke_width=12) + s('path', d='M128 150 L154 96', stroke='#f5b971', stroke_width=6)
    + z('circle', '#ffd9b8', cx=44, cy=90, r=9) + z('circle', '#ffd9b8', cx=156, cy=90, r=9)
    + face(100, 100, '#ffd9b8', '#2b2220', 'open')
    + confetti_bits([('r', 30, 128, '#f07a8a', 30), ('c', 170, 134, '#8fc7e8', 0), ('r', 166, 66, '#9ccf7a', -30),
                     ('c', 34, 64, '#ffc94d', 0), ('s', 22, 160, '#a98bd0', 0), ('r', 172, 168, '#ffc94d', 50)])
    + s('path', d='M60 72 L54 66 M142 72 L148 66', stroke_width=2.5)
)

# 13. gift wrapping
ITEMS['gift-wrapping'] = (
    z('path', '#f6a6b8', d='M60 156 L176 156 L176 180 L60 180Z')
    + z('rect', '#f6a6b8', x=22, y=154, width=44, height=28, rx=6)
    + z('ellipse', '#f6a6b8', cx=24, cy=168, rx=7, ry=14, stroke_width=2.5)
    + dot(24, 168, 3)
    + z('rect', '#7cc4b0', x=72, y=96, width=80, height=62, rx=3)
    + ''.join(dot(x, y, 3, '#ffffff') for x, y in ((84, 110), (84, 146), (140, 110), (140, 146), (128, 128), (96, 128)))
    + s('rect', '#ffc94d', x=106, y=96, width=12, height=62, stroke_width=2.5)
    + s('rect', '#ffc94d', x=72, y=121, width=80, height=12, stroke_width=2.5)
    + z('path', '#ffc94d', d='M112 96 Q84 72 82 86 Q84 98 112 96Z', stroke_width=2.5)
    + s('path', d='M112 96 Q136 60 152 70', stroke='#ffc94d', stroke_width=8)
    + s('path', d='M112 96 Q136 60 152 70', stroke_width=2)
    + s('path', d='M54 70 L74 90', stroke_width=12) + s('path', d='M54 70 L74 90', stroke='#8fb3e0', stroke_width=6)
    + z('circle', '#ffd9b8', cx=80, cy=88, r=11)
    + s('path', d='M172 54 L156 68', stroke_width=12) + s('path', d='M172 54 L156 68', stroke='#8fb3e0', stroke_width=6)
    + z('circle', '#ffd9b8', cx=152, cy=72, r=11)
    + dot(118, 172, 3, '#ffffff') + dot(146, 168, 3, '#ffffff') + dot(90, 170, 3, '#ffffff') + dot(44, 166, 3, '#ffffff')
)

# 14. invitation with a wax seal
ITEMS['invitation'] = (
    z('path', '#ffffff', d='M58 30 L146 30 L146 116 L58 116Z')
    + s('path', d='M72 48 L132 48', stroke='#c9d3db', stroke_width=4)
    + s('path', d='M78 62 L126 62 M78 74 L126 74', stroke='#c9d3db', stroke_width=3)
    + s('path', '#f6a6b8', d=heart_d(102, 92, 18), stroke_width=2)
    + z('path', '#f6e0c4', d='M34 86 L166 86 L166 176 L34 176Z')
    + s('path', d='M34 176 L90 128 M166 176 L110 128', stroke_width=2.5)
    + z('path', '#f5d58a', d='M34 86 L100 136 L166 86Z')
    + z('circle', '#e04b5a', cx=100, cy=134, r=17)
    + s('circle', cx=100, cy=134, r=11, stroke='#f07a8a', stroke_width=2.5)
    + s('path', '#f07a8a', d=heart_d(100, 134, 12), stroke='#f07a8a', stroke_width=1.5)
    + sparkle(160, 46, 8) + sparkle(36, 56, 6)
)

# 15. cheers glasses
def wine_glass(cx, cy, rot, wine):
    return (f'<g transform="rotate({rot} {cx} {cy})">'
            + s('path', d=f'M{cx} {cy + 30} L{cx} {cy + 64}', stroke_width=4)
            + z('ellipse', '#f4f4f0', cx=cx, cy=cy + 66, rx=18, ry=5, stroke_width=2.5)
            + z('path', wine, d=f'M{cx - 22} {cy - 6} Q{cx - 22} {cy + 30} {cx} {cy + 31} Q{cx + 22} {cy + 30} {cx + 22} {cy - 6}Z')
            + s('path', d=f'M{cx - 24} {cy - 42} Q{cx - 28} {cy + 30} {cx} {cy + 31} Q{cx + 28} {cy + 30} {cx + 24} {cy - 42}')
            + s('path', d=f'M{cx - 14} {cy - 30} L{cx - 15} {cy - 16}', stroke='#c9d3db', stroke_width=3)
            + '</g>')


ITEMS['cheers-glasses'] = (
    wine_glass(68, 92, 16, '#e04b5a') + wine_glass(132, 92, -16, '#f5d58a')
    + s('path', d='M100 40 L100 26 M82 46 L74 34 M118 46 L126 34', stroke_width=3)
    + sparkle(42, 40, 8) + sparkle(160, 40, 8)
    + s('circle', '#ffffff', cx=134, cy=86, r=2.5, stroke_width=1.5) + s('circle', '#ffffff', cx=142, cy=74, r=2, stroke_width=1.5)
)

# 16. anniversary hearts and cake
ITEMS['anniversary'] = (
    s('path', d='M100 76 L100 108', stroke_width=3)
    + z('path', '#f07a8a', d=heart_d(100, 66, 34))
    + z('rect', '#ffffff', x=72, y=106, width=56, height=30, rx=4)
    + s('path', '#f6a6b8', d='M72 110 L128 110 L128 116 Q121 123 114 116 Q107 123 100 116 Q93 123 86 116 Q79 123 72 116Z', stroke_width=2.5)
    + z('rect', '#ffffff', x=52, y=136, width=96, height=40, rx=4)
    + s('path', '#f6a6b8', d='M52 140 L148 140 L148 147 Q136 155 124 147 Q112 155 100 147 Q88 155 76 147 Q64 155 52 147Z', stroke_width=2.5)
    + s('path', '#f07a8a', d=heart_d(76, 162, 12), stroke_width=2) + s('path', '#f07a8a', d=heart_d(100, 162, 12), stroke_width=2)
    + s('path', '#f07a8a', d=heart_d(124, 162, 12), stroke_width=2)
    + s('path', d='M36 182 L164 182', stroke_width=2.5)
    + z('path', '#f6a6b8', d=heart_d(42, 70, 22), stroke_width=2.5)
    + z('path', '#f6a6b8', d=heart_d(158, 84, 22), stroke_width=2.5)
    + z('path', '#f07a8a', d=heart_d(150, 38, 14), stroke_width=2)
    + sparkle(48, 116, 7) + sparkle(152, 122, 6)
)

# 17. baby shower
ITEMS['baby-shower'] = (
    balloon(44, 52, 18, 22, '#8fc7e8', 58, 120)
    + balloon(156, 52, 18, 22, '#f6a6b8', 142, 120)
    + balloon(72, 34, 15, 18, '#ffe27a', 64, 120)
    + z('path', '#f4f4f0', d='M78 70 Q88 82 100 82 Q112 82 122 70 L150 84 L140 112 L128 108 L128 152 Q120 166 112 166 L88 166 Q80 166 72 152 L72 108 L60 112 L50 84Z')
    + s('path', d='M86 72 Q100 92 114 72', stroke_width=2.5)
    + dot(92, 160, 2.5) + dot(100, 160, 2.5) + dot(108, 160, 2.5)
    + s('path', '#f6a6b8', d=heart_d(100, 118, 20), stroke_width=2.5)
    + s('path', d='M56 100 L66 96 M144 100 L134 96', stroke='#8fc7e8', stroke_width=3)
    + s('path', d='M72 140 L128 140', stroke='#8fc7e8', stroke_width=3)
    + sparkle(30, 140, 7, '#ffe27a') + sparkle(170, 144, 7, '#ffe27a')
    + dot(40, 170, 3, '#a98bd0') + dot(160, 174, 3, '#9ccf7a')
)

# 18. graduation party
ITEMS['graduation-party'] = (
    z('rect', '#f6e0c4', x=38, y=136, width=110, height=24, rx=12, transform='rotate(-10 93 148)')
    + s('ellipse', '#f4f4f0', cx=146, cy=139, rx=7, ry=12, transform='rotate(-10 93 148)', stroke_width=2.5)
    + s('path', d='M88 132 L92 164 M100 130 L104 162', stroke='#e04b5a', stroke_width=5, transform='rotate(-10 93 148)')
    + z('path', '#5b6b7a', d='M66 88 L66 110 Q100 126 134 110 L134 88Z')
    + z('path', '#5b6b7a', d='M100 46 L170 76 L100 104 L30 76Z')
    + dot(100, 75, 4, '#ffc94d')
    + s('path', d='M100 75 Q132 80 146 88 L146 116', stroke='#ffc94d', stroke_width=3)
    + z('path', '#ffc94d', d='M140 114 L152 114 L154 132 L138 132Z', stroke_width=2)
    + confetti_bits([('r', 36, 40, '#f07a8a', 30), ('c', 60, 30, '#8fc7e8', 0), ('r', 160, 36, '#9ccf7a', -30),
                     ('c', 176, 110, '#a98bd0', 0), ('s', 28, 112, '#ffc94d', 0), ('r', 128, 30, '#ffc94d', 60),
                     ('c', 30, 172, '#f07a8a', 0), ('r', 166, 166, '#8fc7e8', -40), ('s', 150, 178, '#e8735a', 0)])
)

# 19. sports day flags
ITEMS['sports-day-flags'] = (
    s('path', d='M22 184 L178 184', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=26, y=40, width=8, height=144, rx=3)
    + z('rect', '#f4f4f0', x=166, y=40, width=8, height=144, rx=3)
    + z('circle', '#ffc94d', cx=30, cy=38, r=6, stroke_width=2.5) + z('circle', '#ffc94d', cx=170, cy=38, r=6, stroke_width=2.5)
    + bunting((34, 48), (100, 84), (166, 48), ['#e8735a', '#8fc7e8', '#ffc94d', '#9ccf7a', '#a98bd0', '#f6a6b8'], 6, drop=20)
    + bunting((34, 96), (100, 132), (166, 96), ['#ffc94d', '#7cc4b0', '#f07a8a', '#8fb3e0', '#ffc94d', '#9ccf7a'], 6, drop=20)
)

# 20. school (cultural) festival stage
ITEMS['cultural-festival'] = (
    z('rect', '#f5d58a', x=26, y=30, width=148, height=124)
    + z('path', '#e04b5a', d='M26 30 L64 30 Q60 90 70 150 L26 150Z')
    + z('path', '#e04b5a', d='M174 30 L136 30 Q140 90 130 150 L174 150Z')
    + s('path', d='M40 40 Q38 90 44 146 M52 40 Q50 90 58 146 M160 40 Q162 90 156 146 M148 40 Q150 90 142 146', stroke_width=2)
    + z('path', '#e04b5a', d='M26 30 L174 30 L174 42 Q161 52 149 42 Q136 52 124 42 Q112 52 100 42 Q88 52 76 42 Q64 52 51 42 Q39 52 26 42Z', stroke_width=2.5)
    + bunting((66, 50), (100, 66), (134, 50), ['#8fc7e8', '#ffc94d', '#9ccf7a', '#f6a6b8'], 4, size=8, drop=11)
    + z('path', '#7cc4b0', d='M78 152 Q80 120 100 118 Q120 120 122 152Z')
    + mini_face(100, 96, 24, '#5a4033')
    + s('path', d='M114 128 L126 108', stroke_width=4) + z('circle', '#5b6b7a', cx=127, cy=105, r=5, stroke_width=2.5)
    + z('circle', '#ffd9b8', cx=114, cy=130, r=6, stroke_width=2.5)
    + z('rect', '#9a6a3f', x=20, y=148, width=160, height=18, rx=2)
    + s('path', d='M20 166 L20 180 M180 166 L180 180 M100 166 L100 180', stroke_width=3)
)
