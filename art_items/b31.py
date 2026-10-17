from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def _r(v):
    return round(v, 1)


def star(cx, cy, R, r=None, n=5, rot=-90):
    r = r or R * 0.48
    pts = []
    for i in range(n * 2):
        a = math.radians(rot + i * 180 / n)
        rr = R if i % 2 == 0 else r
        pts.append(f'{_r(cx + rr * math.cos(a))} {_r(cy + rr * math.sin(a))}')
    return 'M' + ' L'.join(pts) + 'Z'


def cloud(cx, cy, w):
    k = w / 100
    d = f'M{_r(cx - 50 * k)} {_r(cy)}'
    d += f' Q{_r(cx - 58 * k)} {_r(cy - 8 * k)} {_r(cx - 48 * k)} {_r(cy - 20 * k)}'
    d += f' Q{_r(cx - 44 * k)} {_r(cy - 34 * k)} {_r(cx - 28 * k)} {_r(cy - 30 * k)}'
    d += f' Q{_r(cx - 22 * k)} {_r(cy - 56 * k)} {_r(cx + 2 * k)} {_r(cy - 52 * k)}'
    d += f' Q{_r(cx + 20 * k)} {_r(cy - 50 * k)} {_r(cx + 24 * k)} {_r(cy - 34 * k)}'
    d += f' Q{_r(cx + 48 * k)} {_r(cy - 36 * k)} {_r(cx + 50 * k)} {_r(cy - 16 * k)}'
    d += f' Q{_r(cx + 60 * k)} {_r(cy - 4 * k)} {_r(cx + 48 * k)} {_r(cy)}Z'
    return d


def drop(x, y, h=14):
    w = h * 0.45
    return f'M{x} {y} Q{_r(x + w)} {_r(y + h * 0.7)} {x} {_r(y + h)} Q{_r(x - w)} {_r(y + h * 0.7)} {x} {y}Z'


def cface(cx, cy, mouth='smile', e=4):
    o = dot(cx - 13, cy, e) + dot(cx + 13, cy, e) + cheeks(cx - 25, cx + 25, cy + 10, 7, 4)
    if mouth == 'smile':
        o += s('path', d=f'M{cx - 6} {cy + 9} Q{cx} {cy + 15} {cx + 6} {cy + 9}')
    elif mouth == 'o':
        o += f'<circle cx="{cx}" cy="{cy + 13}" r="4" fill="#c0504d" stroke-width="2.5"/>'
    elif mouth == 'flat':
        o += s('path', d=f'M{cx - 6} {cy + 12} L{cx + 6} {cy + 12}')
    elif mouth == 'wavy':
        o += s('path', d=f'M{cx - 9} {cy + 13} Q{cx - 4.5} {cy + 8} {cx} {cy + 13} Q{cx + 4.5} {cy + 18} {cx + 9} {cy + 13}', stroke_width=2.5)
    return o


def thick(d, color, w=6):
    """太い色付き線（線の外側をこげ茶で縁取り）"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def flake_d(cx, cy, R):
    d = ''
    for i in range(6):
        a = math.radians(i * 60 - 90)
        ca, sa = math.cos(a), math.sin(a)
        ex, ey = cx + R * ca, cy + R * sa
        d += f'M{cx} {cy} L{_r(ex)} {_r(ey)} '
        m = 0.58 * R
        mx, my = cx + m * ca, cy + m * sa
        for sgn in (1, -1):
            b = a + sgn * math.radians(45)
            bl = 0.32 * R
            d += f'M{_r(mx)} {_r(my)} L{_r(mx + bl * math.cos(b))} {_r(my + bl * math.sin(b))} '
    return d.strip()


def mini_flake(cx, cy, R, w=2.5):
    return s('path', d=flake_d(cx, cy, R), stroke_width=w)


def sparkle(cx, cy, r, c='#ffe27a'):
    k = r * 0.28
    d = (f'M{cx} {cy - r} Q{_r(cx + k)} {_r(cy - k)} {cx + r} {cy} Q{_r(cx + k)} {_r(cy + k)} {cx} {cy + r} '
         f'Q{_r(cx - k)} {_r(cy + k)} {cx - r} {cy} Q{_r(cx - k)} {_r(cy - k)} {cx} {cy - r}Z')
    return s('path', c, d=d, stroke_width=2.5)


def bolt(x, y, k=1.0):
    p = [(0, 0), (26, 0), (14, 26), (30, 26), (-4, 72), (6, 38), (-10, 38)]
    return 'M' + ' L'.join(f'{_r(x + px * k)} {_r(y + py * k)}' for px, py in p) + 'Z'


# 1. cloudy
ITEMS['cloudy'] = (
    z('path', '#c9d3db', d=cloud(132, 92, 90))
    + z('path', '#ffffff', d=cloud(92, 156, 136))
    + cface(92, 124)
    + z('path', '#ffffff', d=cloud(46, 80, 44)))

# 2. thunder-cloud
ITEMS['thunder-cloud'] = (
    z('path', '#ffc94d', d=bolt(92, 108, 1.15))
    + z('path', '#b9a99c', d=cloud(100, 120, 140))
    + dot(86, 92, 4) + dot(114, 92, 4) + cheeks(74, 126, 102, 7, 4)
    + s('path', d='M80 82 L92 86 M120 82 L108 86', stroke_width=2.5)
    + f'<circle cx="100" cy="108" r="4" fill="#c0504d" stroke-width="2.5"/>'
    + z('path', '#ffc94d', d=bolt(40, 132, 0.55)) + z('path', '#ffc94d', d=bolt(150, 130, 0.55)))

# 3. snow-falling
_fl = ''
for (x, y, r) in [(52, 46, 14), (104, 34, 10), (150, 56, 16), (78, 88, 10), (128, 104, 12), (44, 126, 12), (164, 132, 10), (98, 140, 14)]:
    _fl += s('path', d=flake_d(x, y, r), stroke_width=6) + s('path', d=flake_d(x, y, r), stroke='#8fc7e8', stroke_width=2.5)
_fl += ''.join(z('circle', '#8fc7e8', cx=x, cy=y, r=4) for x, y in [(70, 60), (130, 30), (112, 76), (156, 92), (64, 108), (140, 150), (30, 90)])
ITEMS['snow-falling'] = (
    z('path', '#c9d3db', d='M26 182 Q40 162 70 166 Q100 156 128 166 Q160 158 176 182Z')
    + z('path', '#f4f4f0', d='M26 182 Q46 168 74 172 Q104 162 132 172 Q160 166 176 182Z')
    + _fl)

# 4. wind
_leaf = 'M0 0 Q12 -12 26 0 Q12 12 0 0Z'
def leaf(x, y, a, c='#9ccf7a'):
    return (z('path', c, d=_leaf, transform=f'translate({x} {y}) rotate({a})')
            + s('path', d='M2 0 L22 0', transform=f'translate({x} {y}) rotate({a})', stroke_width=2))
ITEMS['wind'] = (
    thick('M28 74 L118 74 Q148 74 148 52 Q148 32 128 32 Q110 32 112 50', '#8fc7e8')
    + thick('M44 110 L150 110 Q176 110 176 132 Q176 152 156 152 Q138 152 140 136', '#8fc7e8')
    + thick('M30 144 L104 144 Q124 144 124 162 Q124 178 108 178', '#8fc7e8')
    + leaf(68, 46, -20) + leaf(150, 84, 30, '#f5b971') + leaf(86, 168, 15, '#e8735a') + leaf(40, 100, -35))

# 5. storm
_rain = ''.join(s('path', d=f'M{x} {y} L{x - 14} {y + 26}', stroke_width=8) + s('path', d=f'M{x} {y} L{x - 14} {y + 26}', stroke='#8fc7e8', stroke_width=3.5)
                for x, y in [(62, 122), (92, 126), (122, 122), (152, 120), (76, 156), (108, 160), (140, 154)])
ITEMS['storm'] = (
    _rain
    + z('path', '#5b6b7a', d=cloud(100, 116, 144))
    + dot(86, 92, 4, '#ffffff') + dot(114, 92, 4, '#ffffff') + cheeks(74, 126, 102, 7, 4)
    + s('path', d='M80 80 L92 85 M120 80 L108 85', stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M92 108 Q96 103 100 108 Q104 113 108 108', stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M150 44 L176 44 Q186 44 184 36 Q182 30 176 32 M146 56 L168 56', stroke_width=3)
    + s('path', d='M24 72 L40 72 Q48 72 46 64 Q44 58 38 61', stroke_width=3))

# 6. heat-sun
_rays = ''
for i in range(10):
    a = math.radians(i * 36 - 90)
    ca, sa = math.cos(a), math.sin(a)
    cx, cy = 100, 86
    tip = (cx + 68 * ca, cy + 68 * sa)
    b1 = (cx + 50 * ca - 9 * sa, cy + 50 * sa + 9 * ca)
    b2 = (cx + 50 * ca + 9 * sa, cy + 50 * sa - 9 * ca)
    _rays += z('path', '#e8735a', d=f'M{_r(b1[0])} {_r(b1[1])} L{_r(tip[0])} {_r(tip[1])} L{_r(b2[0])} {_r(b2[1])}Z')
ITEMS['heat-sun'] = (
    _rays + z('circle', '#ffc94d', cx=100, cy=86, r=44)
    + s('path', d='M82 84 Q88 78 94 84 M106 84 Q112 78 118 84', stroke_width=3)
    + cheeks(74, 126, 96, 8, 5)
    + s('path', '#c0504d', d='M90 100 Q100 116 110 100Z', stroke_width=2.5)
    + z('path', '#8fc7e8', d=drop(132, 64, 14))
    + s('path', d='M40 166 Q50 158 60 166 Q70 174 80 166 Q90 158 100 166 Q110 174 120 166 Q130 158 140 166 Q150 174 160 166', stroke='#e8735a', stroke_width=3.5)
    + s('path', d='M54 182 Q64 174 74 182 Q84 190 94 182 Q104 174 114 182 Q124 190 134 182 Q144 174 150 180', stroke='#f5b971', stroke_width=3.5))

# 7. sunrise
_rr = ''
for i in range(7):
    a = math.radians(-180 + 15 + i * 25)
    ca, sa = math.cos(a), math.sin(a)
    _rr += s('path', d=f'M{_r(100 + 58 * ca)} {_r(128 + 58 * sa)} L{_r(100 + 76 * ca)} {_r(128 + 76 * sa)}', stroke='#f5b971', stroke_width=7) if False else thick(f'M{_r(100 + 58 * ca)} {_r(128 + 58 * sa)} L{_r(100 + 74 * ca)} {_r(128 + 74 * sa)}', '#ffc94d', 4)
ITEMS['sunrise'] = (
    _rr
    + z('path', '#ffe27a', d='M54 128 A46 46 0 0 1 146 128Z')
    + dot(86, 112, 4) + dot(114, 112, 4) + cheeks(74, 126, 120, 6, 3.5)
    + s('path', d='M95 118 Q100 122 105 118', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M24 128 L176 128 L176 150 Q140 140 100 152 Q60 164 24 150Z')
    + z('path', '#7cc4a0', d='M24 156 Q60 168 100 158 Q140 146 176 156 L176 178 L24 178Z')
    + s('path', d='M150 52 Q156 46 162 52 Q168 46 174 52', stroke_width=2.5)
    + s('path', d='M128 34 Q133 29 138 34 Q143 29 148 34', stroke_width=2.5))

# 8. sunset
ITEMS['sunset'] = (
    z('circle', '#f5b971', cx=100, cy=108, r=48)
    + dot(86, 98, 4) + s('path', d='M108 98 Q114 92 120 98', stroke_width=3) + cheeks(74, 126, 108, 6, 3.5)
    + s('path', d='M94 110 Q100 116 106 110', stroke_width=2.5)
    + z('path', '#8fb3e0', d='M24 122 Q36 116 48 122 Q60 128 72 122 Q84 116 96 122 Q108 128 120 122 Q132 116 144 122 Q156 128 168 122 L176 122 L176 178 L24 178Z')
    + s('rect', '#ffc94d', x=74, y=134, width=52, height=7, rx=3.5, stroke_width=2.5)
    + s('rect', '#ffc94d', x=84, y=148, width=32, height=6, rx=3, stroke_width=2.5)
    + s('rect', '#ffc94d', x=92, y=161, width=16, height=5, rx=2.5, stroke_width=2.5)
    + s('path', d='M34 54 Q40 48 46 54 Q52 48 58 54', stroke_width=2.5)
    + s('path', d='M146 46 Q151 41 156 46 Q161 41 166 46', stroke_width=2.5))

# 9. tornado
ITEMS['tornado'] = (
    z('path', '#c9d3db', d='M36 36 Q100 22 164 36 Q170 50 150 60 Q140 74 128 86 Q122 104 112 118 Q108 136 102 150 Q98 164 92 174 Q86 176 88 166 Q90 150 86 134 Q78 118 76 98 Q66 82 54 66 Q34 56 36 36Z')
    + s('path', d='M42 46 Q100 58 158 44', stroke_width=2.5)
    + s('path', d='M58 70 Q100 80 144 64', stroke_width=2.5)
    + s('path', d='M76 100 Q104 106 124 92', stroke_width=2.5)
    + s('path', d='M86 128 Q100 132 112 122', stroke_width=2.5)
    + s('path', d='M90 152 Q98 154 104 148', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M150 106 Q160 96 172 104 Q162 114 150 106Z')
    + z('rect', '#d9a66b', x=34, y=114, width=14, height=10, rx=2, transform='rotate(-20 41 119)')
    + s('path', d='M150 150 Q160 146 168 152 M38 156 Q46 150 56 154', stroke_width=2.5)
    + s('path', d='M64 182 Q100 172 140 182', stroke_width=2.5))

# 10. snowflake
ITEMS['snowflake'] = (
    s('path', d=flake_d(104, 104, 70), stroke='#c9d3db', stroke_width=10)
    + s('path', d=flake_d(100, 100, 70), stroke_width=16)
    + s('path', d=flake_d(100, 100, 70), stroke='#8fc7e8', stroke_width=9)
    + z('path', '#ffffff', d=star(100, 100, 24, 24 * 0.866, 6, -90).replace('L', 'L') if False else
        'M' + ' L'.join(f'{_r(100 + 22 * math.cos(math.radians(i * 60)))} {_r(100 + 22 * math.sin(math.radians(i * 60)))}' for i in range(6)) + 'Z')
    + dot(93, 99, 3) + dot(107, 99, 3) + cheeks(88, 112, 106, 3.5, 2.2)
    + s('path', d='M97 106 Q100 109 103 106', stroke_width=2))

# 11. saturn
_tr = 'translate(100 102) rotate(-16)'
ITEMS['saturn'] = (
    z('path', '#a98bd0', fill_rule='evenodd', transform=_tr,
      d='M-80 0 A80 22 0 1 1 80 0 A80 22 0 1 1 -80 0Z M-58 0 A58 12 0 1 0 58 0 A58 12 0 1 0 -58 0Z')
    + z('circle', '#f5b971', cx=100, cy=100, r=46)
    + s('path', d='M62 80 Q100 72 138 80', stroke='#d9a66b', stroke_width=5)
    + z('path', '#a98bd0', transform=_tr, d='M-80 0 A80 22 0 0 0 80 0 L58 0 A58 12 0 0 1 -58 0Z')
    + dot(86, 96, 4) + dot(114, 96, 4) + cheeks(74, 126, 104, 6, 3.5)
    + s('path', d='M95 102 Q100 106 105 102', stroke_width=2.5)
    + sparkle(40, 50, 9) + sparkle(160, 156, 8) + sparkle(162, 40, 6))

# 12. shooting-star
ITEMS['shooting-star'] = (
    thick('M30 168 L104 94', '#f5d58a', 10)
    + thick('M60 176 L112 120', '#f6a6b8', 6)
    + thick('M24 136 L90 84', '#8fc7e8', 6)
    + z('path', '#ffe27a', d=star(124, 76, 46, 22, 5, -72))
    + dot(116, 76, 4) + dot(134, 72, 4) + cheeks(108, 144, 84, 5.5, 3.2)
    + s('path', d='M122 84 Q127 89 132 83', stroke_width=2.5)
    + sparkle(170, 140, 9) + sparkle(46, 46, 8) + sparkle(160, 170, 5))

# 13. ufo
ITEMS['ufo'] = (
    z('path', '#ffe27a', d='M82 118 L118 118 L148 182 L52 182Z')
    + z('path', '#8fc7e8', d='M66 96 Q66 50 100 50 Q134 50 134 96Z')
    + dot(92, 76, 3.5) + dot(108, 76, 3.5) + cheeks(84, 116, 84, 4.5, 2.8)
    + s('path', d='M96 84 Q100 88 104 84', stroke_width=2.5)
    + z('ellipse', '#c9d3db', cx=100, cy=104, rx=74, ry=20)
    + s('path', d='M30 100 Q100 116 170 100', stroke_width=2.5)
    + dot(52, 108, 5, '#f07a8a') + dot(76, 113, 5, '#ffc94d') + dot(100, 115, 5, '#9ccf7a') + dot(124, 113, 5, '#ffc94d') + dot(148, 108, 5, '#f07a8a')
    + sparkle(36, 44, 8) + sparkle(164, 40, 6))

# 14. comet
ITEMS['comet'] = (
    z('path', '#8fc7e8', d='M130 52 Q60 70 26 170 Q90 120 150 98Z')
    + z('path', '#ffffff', d='M134 62 Q84 84 58 146 Q106 108 146 92Z')
    + z('circle', '#ffe27a', cx=142, cy=72, r=28)
    + dot(134, 70, 3.5) + dot(152, 70, 3.5) + cheeks(126, 160, 79, 5, 3)
    + s('path', d='M139 78 Q143 82 147 78', stroke_width=2.5)
    + sparkle(60, 50, 9) + sparkle(170, 150, 8) + sparkle(110, 168, 5))

# 15. full-moon
ITEMS['full-moon'] = (
    z('circle', '#ffe27a', cx=100, cy=100, r=64)
    + s('circle', '#f5d58a', cx=66, cy=72, r=9, stroke_width=2.5)
    + s('circle', '#f5d58a', cx=134, cy=136, r=11, stroke_width=2.5)
    + s('circle', '#f5d58a', cx=128, cy=62, r=6, stroke_width=2.5)
    + s('path', d='M82 100 Q88 94 94 100 M106 100 Q112 94 118 100', stroke_width=3)
    + cheeks(74, 126, 112, 7, 4)
    + s('path', d='M94 116 Q100 122 106 116', stroke_width=2.5)
    + sparkle(172, 40, 8) + sparkle(30, 160, 7))

# 16. stars
ITEMS['stars'] = (
    z('path', '#ffe27a', d=star(92, 112, 56, 27))
    + dot(80, 112, 4) + dot(104, 112, 4) + cheeks(70, 114, 122, 6, 3.5)
    + s('path', d='M87 122 Q92 127 97 122', stroke_width=2.5)
    + z('path', '#f5b971', d=star(150, 50, 24, 11, 5, -80))
    + z('path', '#ffc94d', d=star(46, 46, 18, 9, 5, -100))
    + sparkle(160, 120, 12) + sparkle(150, 168, 7) + sparkle(36, 172, 8) + sparkle(100, 32, 6))

# 17. rocket
_rk = (z('path', '#e8735a', d='M84 136 Q66 140 60 160 L84 152Z')
       + z('path', '#e8735a', d='M116 136 Q134 140 140 160 L116 152Z')
       + z('path', '#f4f4f0', d='M100 26 Q132 58 120 146 L80 146 Q68 58 100 26Z')
       + z('path', '#e8735a', d='M100 26 Q114 40 120 60 L80 60 Q86 40 100 26Z')
       + z('circle', '#8fc7e8', cx=100, cy=90, r=13)
       + s('circle', 'none', cx=100, cy=90, r=13)
       + s('path', d='M100 132 L100 152', stroke_width=3))
ITEMS['rocket'] = (
    z('path', '#ffc94d', d='M84 150 Q84 176 100 190 Q116 176 116 150Z')
    + s('path', '#e8735a', d='M92 150 Q92 168 100 176 Q108 168 108 150Z', stroke_width=2.5)
    + f'<g transform="rotate(30 100 110)">{_rk}</g>'
    + sparkle(40, 48, 9) + sparkle(168, 160, 8) + sparkle(48, 150, 6) + sparkle(160, 36, 5))
# 炎も機体と一緒に回す
ITEMS['rocket'] = (
    f'<g transform="rotate(35 100 110)">'
    + z('path', '#ffc94d', d='M84 146 Q84 178 100 194 Q116 178 116 146Z')
    + s('path', '#e8735a', d='M92 146 Q92 166 100 176 Q108 166 108 146Z', stroke_width=2.5)
    + _rk + '</g>'
    + sparkle(36, 52, 9) + sparkle(172, 168, 7) + sparkle(46, 160, 6) + sparkle(164, 40, 6))

# 18. sunflower
_pt = ''.join(z('ellipse', '#ffc94d', cx=100, cy=48, rx=11, ry=22, transform=f'rotate({i * 30} 100 78)') for i in range(12))
ITEMS['sunflower'] = (
    thick('M100 110 Q96 150 100 184', '#9ccf7a', 6)
    + z('path', '#7cc4a0', d='M99 152 Q72 156 60 136 Q86 128 99 152Z')
    + z('path', '#7cc4a0', d='M100 140 Q126 140 140 122 Q114 114 100 140Z')
    + _pt
    + z('circle', '#9a6a3f', cx=100, cy=78, r=26)
    + dot(91, 76, 3.5) + dot(109, 76, 3.5) + cheeks(84, 116, 85, 5, 3)
    + s('path', d='M96 85 Q100 89 104 85', stroke_width=2.5))

# 19. rose
ITEMS['rose'] = (
    thick('M100 106 Q104 146 98 186', '#7cc4a0', 6)
    + z('path', '#9ccf7a', d='M101 150 Q74 154 64 134 Q90 128 101 150Z')
    + z('path', '#9ccf7a', d='M102 166 Q128 166 140 146 Q114 140 102 166Z')
    + s('path', d='M103 130 L110 124 M96 172 L90 168', stroke_width=2.5)
    + z('path', '#e04b5a', d='M60 56 Q58 104 100 112 Q142 104 140 56 Q124 34 100 36 Q76 34 60 56Z')
    + s('path', d='M76 52 Q100 34 124 52 Q130 72 112 78 Q92 82 86 68 Q86 56 100 54 Q112 56 110 66', stroke_width=2.5)
    + s('path', d='M62 62 Q66 96 100 100 Q126 98 136 66', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M84 108 L100 98 L116 108 L100 118Z'))

# 20. cherry-blossom
def blossom(cx, cy, r):
    o = ''
    for i in range(5):
        a = i * 72
        o += z('path', '#f6a6b8',
               d=f'M{cx} {cy} Q{cx - r * 0.75} {_r(cy - r * 0.6)} {_r(cx - r * 0.3)} {_r(cy - r)} L{cx} {_r(cy - r * 0.84)} L{_r(cx + r * 0.3)} {_r(cy - r)} Q{cx + r * 0.75} {_r(cy - r * 0.6)} {cx} {cy}Z',
               transform=f'rotate({a} {cx} {cy})')
    o += dot(cx, cy, r * 0.22, '#f07a8a')
    return o
ITEMS['cherry-blossom'] = (
    thick('M24 160 Q80 140 112 104 Q138 76 178 64', '#8b6b4f', 8)
    + thick('M98 118 Q110 140 134 150', '#8b6b4f', 5)
    + thick('M134 84 Q130 58 112 44', '#8b6b4f', 4)
    + blossom(62, 134, 22) + blossom(110, 44, 20) + blossom(134, 150, 20) + blossom(160, 90, 18)
    + blossom(96, 92, 16)
    + z('ellipse', '#f6a6b8', cx=48, cy=60, rx=6, ry=9, transform='rotate(30 48 60)')
    + z('ellipse', '#f6a6b8', cx=70, cy=178, rx=6, ry=9, transform='rotate(-40 70 178)')
    + z('circle', '#f6a6b8', cx=176, cy=128, r=8))
