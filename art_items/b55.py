from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def star_d(cx, cy, R, r, rot=-90):
    pts = []
    for i in range(10):
        a = (rot + i * 36) * pi / 180
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


def thick(d, color, w=11, inner=None):
    inner = inner if inner is not None else w - 6
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def head(cx, cy, r, hair='#5a4033', mouth='smile'):
    k = r / 34
    def p(v):
        return round(v * k, 1)
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{cx - r} {cy - p(2)} Q{cx - p(32)} {cy - p(36)} {cx} {cy - p(35)} Q{cx + p(32)} {cy - p(36)} {cx + r} {cy - p(2)} Q{cx + p(20)} {cy - p(18)} {cx} {cy - p(17)} Q{cx - p(20)} {cy - p(18)} {cx - r} {cy - p(2)}Z')
    o += dot(cx - p(12), cy + p(2), max(2.2, 3.5 * k)) + dot(cx + p(12), cy + p(2), max(2.2, 3.5 * k))
    o += cheeks(cx - p(20), cx + p(20), cy + p(13), p(7), p(4))
    o += mouth_(cx, cy, k, mouth)
    return o


def mouth_(cx, cy, k, mouth):
    def p(v):
        return round(v * k, 1)
    if mouth == 'smile':
        return s('path', d=f'M{cx - p(6)} {cy + p(16)} Q{cx} {cy + p(21)} {cx + p(6)} {cy + p(16)}', stroke_width=2.5)
    if mouth == 'open':
        return s('path', '#c0504d', d=f'M{cx - p(8)} {cy + p(14)} Q{cx} {cy + p(28)} {cx + p(8)} {cy + p(14)}Z', stroke_width=2.5)
    return f'<circle cx="{cx}" cy="{cy + p(18)}" r="{p(4.5)}" fill="#c0504d" stroke-width="2.5"/>'


def hand(x, y, r=6.5, c=SK):
    return z('circle', c, cx=x, cy=y, r=r)


def shoe(x, y, c='#5b6b7a', rx=10, ry=6, rot=0):
    return z('ellipse', c, cx=x, cy=y, rx=rx, ry=ry, transform=f'rotate({rot} {x} {y})')


def leg(d, c='#5b6b7a', w=14):
    return thick(d, c, w)


def arm(d, c=SK, w=11):
    return thick(d, c, w)


def drop(cx, cy, k=1.0, c='#8fc7e8'):
    return s('path', c, d=f'M{cx} {cy - 10 * k} Q{cx + 8 * k} {cy + 1 * k} {cx} {cy + 6 * k} Q{cx - 8 * k} {cy + 1 * k} {cx} {cy - 10 * k}Z', stroke_width=2)


def lines(segs, w=2.5, c=OUT):
    return ''.join(s('path', d=f'M{a} {b} L{x} {y}', stroke=c, stroke_width=w) for a, b, x, y in segs)


# 1. podium
ITEMS['podium'] = (
    s('path', d='M18 178 L182 178', stroke_width=2.5)
    + z('rect', '#c9d3db', x=24, y=124, width=50, height=54, rx=3)
    + z('rect', '#d9a66b', x=126, y=142, width=50, height=36, rx=3)
    + z('rect', '#ffc94d', x=72, y=98, width=56, height=80, rx=3)
    + s('path', '#ffffff', d=star_d(100, 136, 14, 6), stroke_width=2.5)
    + s('path', '#ffffff', d=star_d(49, 150, 11, 5), stroke_width=2.5)
    + s('path', '#ffffff', d=star_d(151, 160, 9, 4), stroke_width=2.5)
    + s('path', d='M86 58 Q70 56 72 68 Q74 76 88 74', stroke_width=3)
    + s('path', d='M114 58 Q130 56 128 68 Q126 76 112 74', stroke_width=3)
    + z('rect', '#ffc94d', x=88, y=84, width=24, height=10, rx=2)
    + s('rect', '#ffc94d', x=96, y=76, width=8, height=9, stroke_width=2.5)
    + z('path', '#ffc94d', d='M84 50 L116 50 Q116 74 100 78 Q84 74 84 50Z')
    + s('path', d='M92 56 Q92 66 98 70', stroke='#ffffff', stroke_width=2.5)
    + dot(40, 60, 3, '#f07a8a') + dot(158, 52, 3, '#8fc7e8') + dot(150, 96, 3, '#9ccf7a') + dot(52, 100, 3, '#ffc94d')
    + lines([(66, 38, 60, 30), (134, 38, 140, 30), (100, 34, 100, 26)])
)

# 2. stadium
ITEMS['stadium'] = (
    thick('M34 104 L34 40', '#b9a99c', 9, 4) + thick('M166 104 L166 40', '#b9a99c', 9, 4)
    + z('rect', '#ffe27a', x=20, y=28, width=28, height=16, rx=3)
    + z('rect', '#ffe27a', x=152, y=28, width=28, height=16, rx=3)
    + z('path', '#8fb3e0', d='M20 112 L20 130 A80 44 0 0 0 180 130 L180 112Z')
    + lines([(52, 154, 52, 166), (76, 162, 76, 172), (100, 164, 100, 174), (124, 162, 124, 172), (148, 154, 148, 166)], 2)
    + z('ellipse', '#c9d3db', cx=100, cy=112, rx=80, ry=44)
    + s('ellipse', cx=100, cy=112, rx=69, ry=36, stroke_width=2)
    + z('ellipse', '#9ccf7a', cx=100, cy=112, rx=56, ry=27)
    + s('path', d='M100 86 L100 138', stroke='#ffffff', stroke_width=2.5)
    + s('ellipse', cx=100, cy=112, rx=11, ry=7, stroke='#ffffff', stroke_width=2.5)
    + s('rect', x=50, y=102, width=12, height=20, stroke='#ffffff', stroke_width=2.5)
    + s('rect', x=138, y=102, width=12, height=20, stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M100 68 L100 50', stroke_width=2.5)
    + s('path', '#e04b5a', d='M100 50 L116 55 L100 60Z', stroke_width=2.5)
)

# 3. sneakers
ITEMS['sneakers'] = (
    z('path', '#f6a6b8', d='M70 86 Q72 62 90 62 Q98 64 96 96Z')
    + z('path', '#e8735a', d='M32 146 L34 90 Q36 76 50 80 L76 86 Q88 100 108 104 L150 112 Q176 118 178 146Z')
    + s('path', '#ffffff', d='M146 112 Q176 118 178 146 L152 146 Q152 126 140 111Z', stroke_width=2.5)
    + s('path', '#f5d58a', d='M46 128 Q90 112 132 124 L130 134 Q90 122 48 138Z', stroke_width=2.5)
    + s('path', '#8fb3e0', d='M32 104 L44 104 L42 140 L32 140Z', stroke_width=2.5)
    + s('path', d='M50 82 Q60 92 76 88', stroke_width=2.5)
    + lines([(84, 102, 94, 90), (96, 106, 106, 94), (108, 108, 118, 98), (88, 92, 102, 102), (100, 96, 114, 106)], 3, '#ffffff')
    + z('rect', '#ffffff', x=26, y=144, width=156, height=20, rx=10)
    + lines([(40, 156, 50, 156), (62, 156, 72, 156), (84, 156, 94, 156), (106, 156, 116, 156), (128, 156, 138, 156), (150, 156, 160, 156)], 2)
    + lines([(20, 64, 40, 64), (14, 76, 30, 76)], 3, '#b9a99c')
)

# 4. sports drink
ITEMS['sports-drink'] = (
    z('rect', '#f4f4f0', x=93, y=22, width=14, height=14, rx=4)
    + z('rect', '#5b6b7a', x=84, y=34, width=32, height=16, rx=4)
    + z('path', '#8fc7e8', d='M78 66 Q78 52 92 50 L108 50 Q122 52 122 66 L128 74 L128 102 Q120 116 128 130 L128 170 Q128 180 118 180 L82 180 Q72 180 72 170 L72 130 Q80 116 72 102 L72 74Z')
    + s('path', d='M74 76 Q100 84 126 76', stroke='#ffffff', stroke_width=2.5)
    + s('rect', '#ffffff', x=73, y=132, width=54, height=34, rx=3, stroke_width=2.5)
    + s('path', '#8fc7e8', d='M100 136 Q110 150 100 160 Q90 150 100 136Z', stroke_width=2)
    + dot(90, 96, 3) + dot(110, 96, 3) + cheeks(82, 118, 104, 5, 3)
    + s('path', d='M96 104 Q100 108 104 104', stroke_width=2.5)
    + drop(150, 70, 1.2) + drop(52, 100, 1.0) + drop(154, 120, 0.9)
    + lines([(44, 60, 52, 66), (156, 150, 164, 156)], 2.5, '#8fc7e8')
)

# 5. stretching (side bend)
ITEMS['stretching'] = (
    s('path', d='M40 180 L160 180', stroke_width=2.5)
    + leg('M92 140 L86 172') + leg('M110 140 L118 172')
    + shoe(84, 174, rx=11) + shoe(122, 174, rx=11)
    + arm('M120 104 L140 118 L124 132')
    + z('ellipse', '#7cc4b0', cx=102, cy=118, rx=22, ry=27, transform='rotate(14 102 118)')
    + hand(124, 132)
    + head(118, 68, 24, '#2b2220', 'smile')
    + arm('M94 100 Q64 48 112 26')
    + hand(116, 26)
    + s('path', d='M144 56 Q154 70 150 86', stroke_width=2.5) + s('path', d='M150 86 L144 80 M150 86 L156 79', stroke_width=2.5)
)

# 6. warm-up (jumping jacks)
ITEMS['warm-up'] = (
    s('path', d='M40 180 L160 180', stroke_width=2.5)
    + leg('M92 136 L72 170') + leg('M108 136 L128 170')
    + shoe(68, 172, rot=-10) + shoe(132, 172, rot=10)
    + arm('M84 104 L54 62') + arm('M116 104 L146 62')
    + z('ellipse', '#f5b971', cx=100, cy=118, rx=22, ry=24)
    + s('path', '#ffffff', d='M78 120 L122 120 L121 128 L79 128Z', stroke_width=2.5)
    + hand(52, 58) + hand(148, 58)
    + head(100, 70, 24, '#5a4033', 'open')
    + s('path', d='M36 74 Q32 60 40 48', stroke_width=2.5) + s('path', d='M164 74 Q168 60 160 48', stroke_width=2.5)
    + s('path', d='M52 150 Q48 160 52 170', stroke_width=2.5) + s('path', d='M148 150 Q152 160 148 170', stroke_width=2.5)
)


# 7. tug of war
def puller(m, shirt, hair, mouth):
    def X(x):
        return x if m == 1 else 200 - x
    def P(d):
        out = []
        for tok in d.split():
            if tok[0].isalpha():
                out.append(tok[0] + str(X(float(tok[1:]))) if len(tok) > 1 else tok)
            else:
                out.append(tok)
        return ' '.join(out)
    rot = -24 if m == 1 else 24
    o = leg(P('M56 114 L62 170')) + leg(P('M64 112 L82 166'))
    o += shoe(X(62), 172, rx=11, rot=0) + shoe(X(84), 168, rx=11)
    o += z('ellipse', shirt, cx=X(50), cy=96, rx=16, ry=21, transform=f'rotate({rot} {X(50)} {96})')
    o += head(X(38), 62, 18, hair, mouth)
    o += arm(P('M48 88 L78 110'), w=10)
    o += hand(X(80), 110, 6) + hand(X(94), 110, 6)
    o += s('path', d=P('M14 52 L22 56') + ' ' + P('M14 64 L22 64'), stroke_width=2.5)
    return o


ITEMS['tug-of-war'] = (
    s('path', d='M20 180 L180 180', stroke_width=2.5)
    + thick('M22 110 L178 110', '#d9a66b', 10, 5)
    + lines([(30 + i * 12, 107, 34 + i * 12, 113) for i in range(13)], 1.5)
    + puller(1, '#8fb3e0', '#2b2220', 'o') + puller(-1, '#f07a8a', '#5a4033', 'o')
    + z('path', '#e04b5a', d='M100 110 L92 132 L100 128 L108 132Z')
    + s('path', d='M100 150 L100 172', stroke_width=2, stroke_dasharray='4 5')
)

# 8. ball toss (tamaire)
ITEMS['ball-toss'] = (
    s('path', d='M20 180 L180 180', stroke_width=2.5)
    + thick('M120 178 L120 74', '#b9a99c', 10, 5)
    + s('circle', '#e04b5a', cx=108, cy=50, r=8, stroke_width=2.5) + s('circle', '#ffffff', cx=124, cy=48, r=8, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=136, cy=52, r=8, stroke_width=2.5)
    + z('path', '#f5d58a', d='M92 52 L148 52 L140 80 L100 80Z')
    + s('path', d='M98 66 L144 66 M108 52 L110 80 M120 52 L120 80 M132 52 L130 80', stroke_width=2)
    + z('circle', '#e04b5a', cx=82, cy=70, r=8) + z('circle', '#ffffff', cx=150, cy=96, r=8) + z('circle', '#e04b5a', cx=96, cy=106, r=8)
    + s('path', d='M66 92 Q70 84 74 80', stroke_width=2.5) + s('path', d='M86 124 Q88 118 90 114', stroke_width=2.5)
    + z('circle', '#ffffff', cx=150, cy=172, r=7) + z('circle', '#e04b5a', cx=164, cy=172, r=7) + z('circle', '#ffffff', cx=172, cy=160, r=6)
    + leg('M44 158 L42 172', w=12) + leg('M58 158 L62 172', w=12) + shoe(40, 175, rx=8, ry=5) + shoe(64, 175, rx=8, ry=5)
    + arm('M42 146 L30 158', w=10)
    + z('ellipse', '#7cc4b0', cx=50, cy=146, rx=16, ry=16)
    + head(48, 116, 18, '#2b2220', 'open')
    + arm('M60 140 L72 120', w=10) + hand(73, 116, 5.5) + hand(29, 160, 5.5)
)

# 9. sack race
ITEMS['sack-race'] = (
    z('ellipse', '#f5b971', cx=100, cy=100, rx=24, ry=22)
    + head(100, 58, 25, '#5a4033', 'open')
    + z('path', '#d9a66b', d='M68 102 L132 102 Q142 136 130 168 Q100 176 70 168 Q58 136 68 102Z')
    + s('path', d='M80 128 Q86 140 82 152 M118 124 Q114 138 120 150', stroke_width=2)
    + z('path', '#d9a66b', d='M64 100 Q74 108 84 100 Q92 108 100 100 Q108 108 116 100 Q126 108 136 100 L134 110 Q100 116 66 110Z')
    + arm('M82 92 L72 104', w=10) + arm('M118 92 L128 104', w=10)
    + hand(71, 106) + hand(129, 106)
    + s('path', d='M56 166 Q50 172 42 172 M144 166 Q150 172 158 172', stroke_width=2.5)
    + s('path', d='M80 182 L120 182', stroke_width=2.5, stroke_dasharray='6 6')
    + lines([(50, 140, 40, 140), (52, 152, 44, 156), (150, 140, 160, 140), (148, 152, 156, 156)], 2.5)
)

# 10. frisbee
ITEMS['frisbee'] = (
    s('path', d='M30 180 L170 180', stroke_width=2.5)
    + leg('M70 138 L64 172') + leg('M88 138 L98 172')
    + shoe(62, 174, rx=11) + shoe(102, 174, rx=11)
    + arm('M60 104 L42 124')
    + z('ellipse', '#f07a8a', cx=78, cy=116, rx=22, ry=25)
    + hand(41, 126)
    + head(74, 70, 24, '#c9a36b', 'smile')
    + arm('M94 106 L126 96') + hand(130, 95)
    + lines([(110, 74, 126, 66), (116, 86, 132, 78), (122, 56, 134, 52)], 2.5, '#b9a99c')
    + z('ellipse', '#7cc4b0', cx=156, cy=56, rx=24, ry=9, transform='rotate(-14 156 56)')
    + s('ellipse', cx=156, cy=55, rx=13, ry=4, transform='rotate(-14 156 55)', stroke_width=2)
)

# 11. dodgeball
ITEMS['dodgeball'] = (
    s('path', d='M30 180 L170 180', stroke_width=2.5)
    + leg('M84 140 L66 172') + leg('M98 140 L104 172')
    + shoe(62, 174, rx=11, rot=-8) + shoe(106, 174, rx=11)
    + arm('M98 100 L118 66') + arm('M76 104 L48 80')
    + z('ellipse', '#f5d58a', cx=88, cy=118, rx=22, ry=26, transform='rotate(-16 88 118)')
    + s('path', '#8fb3e0', d='M68 118 L106 106 L108 114 L70 126Z', stroke_width=2.5)
    + hand(120, 62) + hand(45, 77)
    + head(76, 70, 24, '#2b2220', 'o')
    + drop(108, 44, 1.0)
    + lines([(160, 104, 178, 104), (162, 118, 180, 118), (160, 132, 176, 132)], 3, '#b9a99c')
    + z('circle', '#e04b5a', cx=142, cy=118, r=16)
    + s('path', d='M128 110 Q142 118 156 110 M128 126 Q142 118 156 126', stroke_width=2)
)

# 12. soccer goal
net_v = ''.join(s('path', d=f'M{x} 72 L{x} 160', stroke='#b9a99c', stroke_width=1.5) for x in range(52, 150, 16))
net_h = ''.join(s('path', d=f'M40 {y} L160 {y}', stroke='#b9a99c', stroke_width=1.5) for y in range(82, 160, 14))
ITEMS['soccer-goal'] = (
    z('rect', '#9ccf7a', x=20, y=152, width=160, height=24, rx=6)
    + s('rect', '#f4f4f0', x=40, y=68, width=120, height=88, stroke='none')
    + net_v + net_h
    + thick('M36 160 L36 62 L164 62 L164 160', '#ffffff', 11, 5)
    + z('circle', '#ffffff', cx=128, cy=150, r=18)
    + s('path', OUT, d='M128 143 L134 147 L132 154 L124 154 L122 147Z', stroke_width=2)
    + s('path', d='M128 143 L128 133 M134 147 L144 143 M132 154 L138 162 M124 154 L118 162 M122 147 L112 143', stroke_width=2)
    + lines([(84, 150, 98, 150), (88, 140, 100, 142)], 2.5, '#5b6b7a')
)

# 13. basketball hoop
ITEMS['basketball-hoop'] = (
    thick('M100 178 L100 90', '#5b6b7a', 11, 5)
    + z('rect', '#5b6b7a', x=82, y=170, width=36, height=10, rx=3)
    + z('rect', '#ffffff', x=50, y=28, width=100, height=66, rx=5)
    + s('rect', x=80, y=60, width=40, height=28, stroke='#e8735a', stroke_width=3)
    + s('path', '#ffffff', d='M78 100 L84 132 L116 132 L122 100Z', stroke='none')
    + s('path', d='M78 100 L84 132 M122 100 L116 132 M88 100 L92 132 M100 100 L100 132 M112 100 L108 132 M80 112 L120 112 M82 122 L118 122 M84 132 L116 132', stroke_width=2)
    + thick('M74 100 L126 100', '#e8735a', 9, 5)
    + s('path', d='M150 168 Q164 120 154 96', stroke_width=2.5, stroke_dasharray='3 7')
    + z('circle', '#f5b971', cx=152, cy=80, r=16)
    + s('path', d='M136 80 L168 80 M152 64 L152 96 M141 69 Q148 80 141 91 M163 69 Q156 80 163 91', stroke_width=2)
)

# 14. tennis player
ITEMS['tennis-player'] = (
    s('path', d='M30 180 L170 180', stroke_width=2.5)
    + leg('M78 138 L70 172', SK, 12) + leg('M96 138 L106 172', SK, 12)
    + shoe(68, 174, '#ffffff', rx=11) + shoe(110, 174, '#ffffff', rx=11)
    + arm('M70 104 L50 124')
    + z('ellipse', '#ffffff', cx=88, cy=114, rx=22, ry=24)
    + z('path', '#8fb3e0', d='M66 124 L110 124 L116 146 L60 146Z')
    + hand(48, 126)
    + head(84, 68, 24, '#5a4033', 'open')
    + s('path', d='M60 58 Q84 46 108 58', stroke='#e04b5a', stroke_width=5)
    + arm('M104 104 L132 92')
    + thick('M134 90 L146 76', '#8b6b4f', 9, 4)
    + z('ellipse', '#8fb3e0', cx=156, cy=58, rx=17, ry=22, transform='rotate(32 156 58)')
    + s('ellipse', '#ffffff', cx=156, cy=58, rx=11, ry=16, transform='rotate(32 156 58)', stroke_width=2)
    + s('path', d='M148 50 L164 66 M150 58 L160 50 M156 64 L166 56 M146 56 L156 46', stroke='#b9a99c', stroke_width=1.5)
    + hand(134, 91)
    + z('circle', '#ffe27a', cx=118, cy=34, r=8)
    + s('path', d='M112 30 Q118 36 124 30', stroke_width=1.5)
    + lines([(92, 30, 104, 30), (94, 40, 104, 38)], 2.5, '#b9a99c')
)

# 15. baseball batter
ITEMS['baseball-player'] = (
    s('path', d='M30 180 L170 180', stroke_width=2.5)
    + leg('M86 138 L76 172', '#c9d3db') + leg('M104 138 L116 172', '#c9d3db')
    + shoe(74, 174, rx=11) + shoe(120, 174, rx=11)
    + z('ellipse', '#ffffff', cx=94, cy=116, rx=23, ry=25)
    + s('path', d='M94 92 L94 140', stroke='#8fb3e0', stroke_width=2.5)
    + s('path', '#5b6b7a', d='M72 128 L116 128 L116 134 L72 134Z', stroke_width=2.5)
    + z('path', '#d9a66b', d='M120 102 L148 40 Q154 32 160 38 Q162 44 128 106Z')
    + arm('M78 104 L116 106') + arm('M110 102 L120 100')
    + hand(120, 104, 7) + hand(126, 98, 7)
    + head(90, 68, 24, '#2b2220', 'smile')
    + z('path', '#5b6b7a', d='M65 68 Q64 42 90 42 Q116 42 115 68 Q90 56 65 68Z')
    + z('path', '#5b6b7a', d='M64 62 L46 68 Q52 74 66 70Z')
    + z('circle', '#ffffff', cx=38, cy=110, r=9)
    + s('path', d='M32 104 Q36 110 32 116 M44 104 Q40 110 44 116', stroke='#e04b5a', stroke_width=1.5)
    + lines([(52, 104, 62, 104), (52, 116, 60, 116)], 2.5, '#b9a99c')
)

# 16. soccer player (kick)
ITEMS['soccer-player'] = (
    s('path', d='M24 180 L176 180', stroke_width=2.5)
    + leg('M80 130 L78 170', SK, 12) + shoe(76, 174, '#e04b5a', rx=11)
    + leg('M96 128 Q116 150 132 152', SK, 12) + shoe(136, 152, '#e04b5a', rx=10, rot=-20)
    + s('path', d='M112 162 L98 164 M120 168 L108 172', stroke='#b9a99c', stroke_width=2.5)
    + z('path', '#ffffff', d='M68 118 L110 118 L114 136 L98 138 L90 130 L84 140 L66 138Z')
    + arm('M72 98 L48 86') + arm('M104 98 L126 82')
    + z('ellipse', '#8fb3e0', cx=88, cy=104, rx=22, ry=22)
    + hand(45, 85) + hand(129, 80)
    + head(86, 62, 24, '#5a4033', 'open')
    + z('circle', '#ffffff', cx=158, cy=154, r=16)
    + s('path', OUT, d='M158 148 L163 152 L161 158 L155 158 L153 152Z', stroke_width=2)
    + s('path', d='M158 148 L158 139 M163 152 L172 149 M161 158 L166 166 M155 158 L150 166 M153 152 L144 149', stroke_width=2)
)

# 17. volleyball spike
ITEMS['volleyball-player'] = (
    z('circle', '#ffffff', cx=140, cy=40, r=16)
    + s('path', d='M126 34 Q140 42 154 34 M140 24 Q134 40 140 56 M128 48 Q142 44 150 52', stroke_width=2)
    + s('path', d='M126 34 Q140 42 154 34 Q150 26 140 24 Q134 28 130 30Z', stroke='none', fill='#ffe27a')
    + lines([(160, 26, 168, 20), (162, 40, 172, 40)], 2.5, '#b9a99c')
    + leg('M84 148 Q70 160 78 174', '#5b6b7a') + leg('M100 148 Q114 156 110 172', '#5b6b7a')
    + shoe(80, 176, rx=10) + shoe(112, 174, rx=10)
    + arm('M76 120 L58 134')
    + z('ellipse', '#f07a8a', cx=92, cy=128, rx=22, ry=24)
    + hand(56, 136)
    + head(88, 82, 24, '#2b2220', 'open')
    + arm('M106 114 L126 62') + hand(127, 58)
    + s('path', d='M66 186 L84 186 M100 186 L120 186', stroke_width=2.5)
)

# 18. fencing
ITEMS['fencing'] = (
    s('path', d='M24 180 L176 180', stroke_width=2.5)
    + leg('M90 132 L56 172', '#ffffff') + shoe(52, 174, rx=11)
    + leg('M108 134 L134 146 L138 170', '#ffffff') + shoe(144, 174, rx=11)
    + arm('M88 104 L64 92 L54 72', '#ffffff') + hand(52, 68, 6, '#ffffff')
    + z('ellipse', '#ffffff', cx=100, cy=116, rx=22, ry=24, transform='rotate(12 100 116)')
    + s('path', d='M86 102 L106 96', stroke_width=2)
    + s('path', d='M150 92 L184 72', stroke_width=3)
    + s('ellipse', '#c9d3db', cx=150, cy=92, rx=4, ry=9, transform='rotate(-30 150 92)', stroke_width=2.5)
    + arm('M112 102 L144 94', '#ffffff') + hand(146, 94, 6.5, '#ffffff')
    + z('path', '#ffffff', d='M80 80 L118 80 L116 92 L82 92Z')
    + z('ellipse', '#5b6b7a', cx=98, cy=60, rx=22, ry=24)
    + s('ellipse', '#c9d3db', cx=98, cy=62, rx=16, ry=18, stroke_width=2)
    + s('path', d='M86 52 L110 52 M84 60 L112 60 M84 68 L112 68 M86 76 L110 76 M92 46 L92 78 M98 44 L98 80 M104 46 L104 78', stroke='#9aa6b0', stroke_width=1.2)
    + dot(92, 61, 2.6) + dot(104, 61, 2.6)
)

# 19. weightlifting
def plates(x, sgn):
    return (z('rect', '#e04b5a', x=x if sgn > 0 else x - 14, y=30, width=14, height=46, rx=4)
            + z('rect', '#8fb3e0', x=x + 14 if sgn > 0 else x - 24, y=38, width=10, height=30, rx=3))


ITEMS['weightlifting'] = (
    s('path', d='M30 182 L170 182', stroke_width=2.5)
    + leg('M88 156 L70 176') + leg('M112 156 L130 176')
    + shoe(66, 178, rx=11) + shoe(134, 178, rx=11)
    + arm('M80 128 L72 60') + arm('M120 128 L128 60')
    + z('ellipse', '#7cc4b0', cx=100, cy=142, rx=25, ry=22)
    + s('path', '#2b2220', d='M76 150 L124 150 L122 158 L78 158Z', stroke_width=2.5)
    + thick('M30 53 L170 53', '#c9d3db', 8, 3)
    + plates(26, 1) + plates(174, -1)
    + hand(72, 56, 7) + hand(128, 56, 7)
    + head(100, 98, 23, '#5a4033', 'o')
    + drop(130, 92, 0.9) + drop(70, 102, 0.8)
    + lines([(60, 22, 64, 28), (140, 22, 136, 28)], 2.5)
)

# 20. trampoline
ITEMS['trampoline'] = (
    thick('M44 154 L40 180', '#5b6b7a', 9, 4) + thick('M156 154 L160 180', '#5b6b7a', 9, 4) + thick('M100 164 L100 182', '#5b6b7a', 9, 4)
    + z('ellipse', '#8fb3e0', cx=100, cy=150, rx=70, ry=17)
    + s('ellipse', '#5b6b7a', cx=100, cy=150, rx=56, ry=10, stroke_width=2.5)
    + s('path', d='M84 138 Q88 132 84 126 M116 138 Q112 132 116 126', stroke_width=2.5)
    + leg('M94 108 L88 122', '#5b6b7a', 12) + leg('M106 108 L112 122', '#5b6b7a', 12)
    + shoe(86, 126, '#e8735a', rx=9) + shoe(114, 126, '#e8735a', rx=9)
    + arm('M88 84 L66 58') + arm('M112 84 L134 58')
    + z('ellipse', '#f5d58a', cx=100, cy=94, rx=18, ry=18)
    + hand(64, 55) + hand(136, 55)
    + head(100, 54, 22, '#c9a36b', 'open')
    + s('path', '#ffe27a', d=star_d(40, 40, 9, 4), stroke_width=2) + s('path', '#f6a6b8', d=star_d(162, 36, 7, 3), stroke_width=2)
)
