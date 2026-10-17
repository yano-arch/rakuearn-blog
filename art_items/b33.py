from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def _r(v):
    return round(v, 1)


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


def blob(cx, cy, rx, ry, n=9, bump=0.16):
    """ぼこぼこした丸（木の葉っぱのかたまり等）"""
    pts = []
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    d = f'M{_r(pts[0][0])} {_r(pts[0][1])}'
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        am = math.radians(-90 + (i + 0.5) * 360 / n)
        c = (cx + rx * (1 + bump * 2) * math.cos(am), cy + ry * (1 + bump * 2) * math.sin(am))
        d += f' Q{_r(c[0])} {_r(c[1])} {_r(q[0])} {_r(q[1])}'
    return d + 'Z'


def sparkle(x, y, r, c='#ffe27a', sw=2):
    return s('path', c, d=f'M{x} {y - r} Q{x + r * .2} {y - r * .2} {x + r} {y} Q{x + r * .2} {y + r * .2} {x} {y + r} '
             f'Q{x - r * .2} {y + r * .2} {x - r} {y} Q{x - r * .2} {y - r * .2} {x} {y - r}Z', stroke_width=sw)


def flower(x, y, r, petal, center='#ffe27a', stem=True, sw=2.5):
    o = ''
    if stem:
        o += s('path', d=f'M{x} {y} L{x} {_r(y + r * 3.2)}', stroke_width=sw)
    for i in range(5):
        a = math.radians(-90 + i * 72)
        o += s('circle', petal, cx=_r(x + r * math.cos(a)), cy=_r(y + r * math.sin(a)), r=_r(r * 0.75), stroke_width=sw)
    o += s('circle', center, cx=x, cy=y, r=_r(r * 0.6), stroke_width=sw)
    return o


def petal(x, y, rot, c='#f6a6b8', k=1):
    return s('path', c, d='M0 -6 Q5 -2 3 4 Q0 2 -3 4 Q-5 -2 0 -6Z', stroke_width=2,
             transform=f'translate({x} {y}) rotate({rot}) scale({k})')


def leafy(x, y, rot, c, k=1):
    return z('path', c, d='M0 -10 Q8 -2 0 10 Q-8 -2 0 -10Z', stroke_width=2,
             transform=f'translate({x} {y}) rotate({rot}) scale({k})')


def pine(x, base, h, c='#7cc4a0', snow=False):
    w = h * 0.42
    o = s('rect', '#8b6b4f', x=x - 4, y=base - 10, width=8, height=10, stroke_width=2.5)
    o += z('path', c, d=f'M{x} {base - h} L{_r(x + w * .7)} {_r(base - h * .5)} L{_r(x + w * .45)} {_r(base - h * .5)} '
                       f'L{_r(x + w)} {base - 8} L{_r(x - w)} {base - 8} L{_r(x - w * .45)} {_r(base - h * .5)} '
                       f'L{_r(x - w * .7)} {_r(base - h * .5)}Z')
    if snow:
        o += s('path', '#ffffff', d=f'M{x} {base - h} L{_r(x + w * .35)} {_r(base - h * .75)} Q{x} {_r(base - h * .68)} '
                                   f'{_r(x - w * .35)} {_r(base - h * .75)}Z', stroke_width=2)
    return o


def mini_face(cx, cy, sp=10, dr=3.5, ck=(6, 3.5)):
    return (dot(cx - sp, cy, dr) + dot(cx + sp, cy, dr) + cheeks(cx - sp - 8, cx + sp + 8, cy + 9, *ck)
            + s('path', d=f'M{cx - 5} {cy + 8} Q{cx} {cy + 13} {cx + 5} {cy + 8}', stroke_width=2.5))


# 1. lake
ITEMS['lake'] = (
    z('path', '#8fb3e0', d='M30 112 L78 50 L126 112Z')
    + s('path', '#ffffff', d='M78 50 L92 68 L84 66 L78 72 L71 66 L64 68Z', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M96 112 L134 70 L172 112Z')
    + z('ellipse', '#9ccf7a', cx=100, cy=144, rx=78, ry=38)
    + z('ellipse', '#8fc7e8', cx=100, cy=146, rx=62, ry=26)
    + s('path', '#c9e2f2', d='M58 126 L78 160 L98 126Z', stroke='none')
    + s('path', '#bfe3d8', d='M104 126 L128 150 L152 126Z', stroke='none')
    + s('path', d='M70 136 L88 136 M108 152 L128 152 M84 164 L100 164', stroke='#ffffff', stroke_width=3)
    + pine(34, 150, 40) + pine(166, 154, 36)
    + z('ellipse', '#ffffff', cx=150, cy=40, rx=18, ry=8))

# 2. flower-field
_ff = z('path', '#9ccf7a', d='M24 110 Q60 92 100 100 Q140 92 176 106 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
_ff += s('path', '#9ccf7a', d='M24 110 Q60 92 100 100 Q140 92 176 106', stroke='none')
for (x, y, r, c) in [(44, 106, 6, '#f5d58a'), (70, 100, 6, '#ffffff'), (130, 100, 6, '#f6a6b8'), (156, 104, 6, '#ffffff'),
                     (100, 106, 6, '#8fb3e0')]:
    _ff += flower(x, y, r, c, sw=2)
for (x, y, r, c) in [(54, 126, 9, '#f07a8a'), (100, 124, 9, '#ffe27a'), (146, 126, 9, '#a98bd0')]:
    _ff += flower(x, y, r, c, '#ffffff' if c == '#ffe27a' else '#ffe27a')
for (x, y, r, c) in [(36, 150, 11, '#f6a6b8'), (78, 148, 12, '#ffffff'), (122, 150, 12, '#f07a8a'), (164, 148, 11, '#f5b971')]:
    _ff += s('path', d=f'M{x} {y} L{x} 178', stroke_width=3) + flower(x, y, r, c, stem=False, sw=2.5)
ITEMS['flower-field'] = (z('ellipse', '#ffffff', cx=64, cy=52, rx=22, ry=10) + z('ellipse', '#ffffff', cx=140, cy=40, rx=18, ry=8)
                         + _ff)

# 3. rice-paddy
_rp = (z('path', '#7cc4a0', d='M24 84 Q60 40 100 66 Q136 44 176 78 L176 92 L24 92Z')
       + z('path', '#9ccf7a', d='M24 92 L176 92 L176 104 L24 104Z')
       + z('path', '#8fc7e8', d='M30 108 L170 108 L176 134 L24 134Z')
       + z('path', '#8fc7e8', d='M24 140 L176 140 L176 176 L24 176Z'))
_rp += s('path', d='M40 120 L56 120 M130 126 L150 126 M60 164 L84 164 M124 158 L144 158', stroke='#ffffff', stroke_width=3)


def tuft(x, y, k=1):
    return s('path', d=f'M{x} {y} Q{_r(x - 5 * k)} {_r(y - 6 * k)} {_r(x - 7 * k)} {_r(y - 12 * k)} M{x} {y} L{x} {_r(y - 14 * k)} '
                       f'M{x} {y} Q{_r(x + 5 * k)} {_r(y - 6 * k)} {_r(x + 7 * k)} {_r(y - 12 * k)}', stroke='#4f9a5a', stroke_width=2.5)


for row_y, xs, k in [(128, range(44, 170, 18), 0.8), (156, range(40, 172, 22), 1.1), (174, range(51, 172, 22), 1.1)]:
    for x in xs:
        _rp += tuft(x, row_y, k)
ITEMS['rice-paddy'] = z('ellipse', '#ffffff', cx=150, cy=40, rx=18, ry=8) + _rp

# 4. fire
ITEMS['fire'] = (
    z('rect', '#9a6a3f', x=46, y=158, width=108, height=16, rx=8, transform='rotate(-10 100 166)')
    + z('rect', '#9a6a3f', x=46, y=158, width=108, height=16, rx=8, transform='rotate(10 100 166)')
    + z('path', '#e8735a', d='M100 166 Q52 164 52 124 Q52 94 74 72 Q76 92 86 96 Q82 64 104 32 Q110 66 128 74 Q132 60 128 50 Q152 76 150 122 Q148 164 100 166Z')
    + z('path', '#ffc94d', d='M100 162 Q70 160 70 132 Q70 112 84 100 Q88 114 96 116 Q96 92 110 76 Q114 104 128 112 Q134 124 132 136 Q128 160 100 162Z')
    + dot(88, 132, 4) + dot(112, 132, 4) + cheeks(78, 122, 144, 6, 3.5)
    + s('path', d='M94 144 Q100 150 106 144', stroke_width=2.5))

# 5. water-drop
ITEMS['water-drop'] = (
    z('path', '#8fc7e8', d='M100 28 Q122 64 142 96 Q158 124 150 146 Q138 176 100 176 Q62 176 50 146 Q42 124 58 96 Q78 64 100 28Z')
    + s('path', '#ffffff', d='M70 112 Q72 96 84 82 Q80 100 76 116 Q72 120 70 112Z', stroke='none')
    + dot(86, 132, 4.5) + dot(114, 132, 4.5) + cheeks(74, 126, 146, 7, 4)
    + s('path', d='M93 146 Q100 154 107 146')
    + z('path', '#8fc7e8', d='M164 56 Q172 68 170 74 Q166 80 160 76 Q156 70 164 56Z', stroke_width=2.5)
    + z('path', '#8fc7e8', d='M36 52 Q42 62 40 66 Q37 70 33 67 Q30 63 36 52Z', stroke_width=2.5))


# 6. recycle
def _pt(r, a):
    return f'{_r(100 + r * math.cos(math.radians(a)))} {_r(102 + r * math.sin(math.radians(a)))}'


_rc = ''
for k in range(3):
    a0 = -80 + 120 * k
    a1 = a0 + 78
    R, r = 70, 48
    _rc += z('path', ['#9ccf7a', '#7cc4a0', '#7cc4b0'][k],
             d=f'M{_pt(R, a0)} A{R} {R} 0 0 1 {_pt(R, a1)} L{_pt(R + 10, a1)} L{_pt((R + r) / 2, a1 + 26)} '
               f'L{_pt(r - 10, a1)} L{_pt(r, a1)} A{r} {r} 0 0 0 {_pt(r, a0)}Z')
ITEMS['recycle'] = (_rc
                    + z('path', '#9ccf7a', d='M100 120 Q78 112 82 86 Q104 88 100 120Z', stroke_width=2.5)
                    + z('path', '#9ccf7a', d='M100 120 Q122 112 118 86 Q96 88 100 120Z', stroke_width=2.5)
                    + s('path', d='M100 128 L100 112', stroke_width=2.5))

# 7. earth-eco
ITEMS['earth-eco'] = (
    s('path', d='M100 62 Q100 50 104 40', stroke_width=3)
    + z('path', '#9ccf7a', d='M104 42 Q112 20 138 22 Q134 46 104 42Z')
    + z('path', '#7cc4a0', d='M102 48 Q92 30 70 34 Q76 54 102 48Z')
    + z('circle', '#8fc7e8', cx=100, cy=118, r=56)
    + s('path', '#9ccf7a', d='M62 92 Q82 78 98 92 Q96 112 76 110 Q58 108 62 92Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M114 120 Q140 110 150 132 Q138 158 118 150 Q104 138 114 120Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M54 130 Q70 128 76 142 Q70 156 58 148Z', stroke_width=2.5)
    + dot(88, 124) + dot(112, 124) + cheeks(78, 122, 134, 6, 3.5) + s('path', d='M94 134 Q100 140 106 134', stroke_width=2.5)
    + leafy(36, 70, -30, '#9ccf7a', 0.9) + leafy(166, 86, 35, '#7cc4a0', 0.9))

# 8. rock
ITEMS['rock'] = (
    z('path', '#c9d3db', d='M128 174 Q126 146 146 140 Q168 136 174 156 Q178 174 164 174Z')
    + z('path', '#b9a99c', d='M30 172 Q24 140 42 112 Q56 80 92 72 Q126 68 142 96 Q156 122 150 150 Q148 172 130 174 L42 174 Q32 174 30 172Z')
    + s('path', d='M58 102 Q66 96 72 100 M126 140 L134 132 L140 136', stroke_width=2.5)
    + s('path', '#a3958a', d='M60 150 Q70 144 78 150 Q70 156 60 150Z', stroke='none')
    + dot(80, 120, 4) + dot(110, 120, 4) + cheeks(68, 122, 132, 7, 4) + s('path', d='M88 132 Q95 139 102 132')
    + s('path', d='M152 174 L148 162 M158 174 L160 160 M164 174 L170 164', stroke='#4f9a5a', stroke_width=2.5)
    + s('path', d='M22 178 L178 178', stroke_width=2.5))

# 9. gem
ITEMS['gem'] = (
    z('path', '#8fc7e8', d='M48 84 L72 52 L128 52 L152 84 L100 160Z')
    + s('path', '#d8eef8', d='M72 52 L86 84 L100 52Z', stroke='none')
    + s('path', '#d8eef8', d='M86 84 L100 160 L66 84Z', stroke='none')
    + s('path', d='M48 84 L152 84 M72 52 L86 84 L100 52 L114 84 L128 52 M86 84 L100 160 L114 84', stroke_width=2.5)
    + s('path', d='M48 84 L72 52 L128 52 L152 84 L100 160Z')
    + sparkle(160, 46, 12) + sparkle(42, 130, 10) + sparkle(152, 132, 7) + sparkle(46, 46, 6))

# 10. seashell
_cx, _cy, _R = 100, 152, 92
_angs = [-150 + i * 20 for i in range(7)]
_P = [(_cx + _R * math.cos(math.radians(a)), _cy + _R * math.sin(math.radians(a))) for a in _angs]
_d = f'M{_cx} {_cy} L{_r(_P[0][0])} {_r(_P[0][1])}'
for i in range(6):
    am = math.radians((_angs[i] + _angs[i + 1]) / 2)
    c = (_cx + (_R + 16) * math.cos(am), _cy + (_R + 16) * math.sin(am))
    _d += f' Q{_r(c[0])} {_r(c[1])} {_r(_P[i + 1][0])} {_r(_P[i + 1][1])}'
_d += 'Z'
_ribs = ' '.join(f'M{_r(_cx + 50 * math.cos(math.radians(a)))} {_r(_cy + 50 * math.sin(math.radians(a)))} L{_r(p[0])} {_r(p[1])}' for a, p in zip(_angs[1:-1], _P[1:-1]))
ITEMS['seashell'] = (
    z('path', '#f6a6b8', d=_d)
    + s('path', d=_ribs, stroke_width=2.5)
    + z('path', '#f6a6b8', d='M78 150 L122 150 L130 172 L70 172Z')
    + s('path', d='M88 158 L112 158 M84 165 L116 165', stroke_width=2)
    + dot(84, 120, 3.5) + dot(116, 120, 3.5) + cheeks(72, 128, 130, 6, 3.5)
    + s('path', d='M95 130 Q100 135 105 130', stroke_width=2.5)
    + sparkle(160, 52, 9) + sparkle(38, 160, 7))

# 11. spring
ITEMS['spring'] = (
    z('path', '#9ccf7a', d='M24 150 Q100 132 176 150 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
    + z('path', '#9a6a3f', d='M92 160 L94 110 Q80 98 72 96 L78 92 Q90 98 98 104 L104 88 L110 90 L106 108 Q118 100 128 98 L130 104 Q114 110 108 118 L110 160Z')
    + z('path', '#f6a6b8', d=blob(100, 76, 66, 44, 11, 0.1))
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=5, stroke_width=2) + dot(x, y, 1.6, '#f07a8a')
              for x, y in [(64, 70), (86, 52), (112, 60), (138, 72), (96, 86), (124, 94), (70, 96), (150, 56)])
    + petal(42, 128, 20) + petal(160, 124, -30) + petal(132, 140, 60) + petal(60, 142, -20)
    + flower(46, 158, 5, '#ffe27a', '#f5b971', stem=False, sw=2) + flower(152, 160, 5, '#ffffff', '#ffe27a', stem=False, sw=2)
    + flower(130, 166, 4, '#f6a6b8', '#ffe27a', stem=False, sw=2))

# 12. summer
_rays = ''
for i in range(8):
    a = math.radians(i * 45)
    _rays += s('path', d=f'M{_r(56 + 30 * math.cos(a))} {_r(54 + 30 * math.sin(a))} L{_r(56 + 40 * math.cos(a))} {_r(54 + 40 * math.sin(a))}',
               stroke_width=3)
ITEMS['summer'] = (
    _rays + z('circle', '#ffc94d', cx=56, cy=54, r=22) + dot(49, 52, 3) + dot(63, 52, 3) + cheeks(43, 69, 60, 4.5, 2.5)
    + s('path', d='M52 60 Q56 64 60 60', stroke_width=2)
    + z('ellipse', '#ffffff', cx=142, cy=46, rx=22, ry=10)
    + z('path', '#8fc7e8', d='M24 104 Q37 96 50 104 Q63 112 76 104 Q89 96 102 104 Q115 112 128 104 Q141 96 154 104 Q165 110 176 104 L176 150 L24 150Z')
    + s('path', d='M40 124 Q48 118 56 124 M100 132 Q108 126 116 132 M140 120 Q148 114 156 120', stroke='#ffffff', stroke_width=3)
    + z('path', '#f5d58a', d='M24 146 Q70 134 120 142 Q150 146 176 138 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
    + s('path', d='M138 170 L120 94', stroke_width=4)
    + z('path', '#e8735a', d='M84 110 Q100 74 132 80 Q158 88 160 118 Q144 104 128 108 Q110 100 84 110Z')
    + s('path', '#ffffff', d='M107 79 Q110 90 128 108 Q124 92 121 78Z', stroke_width=2.5)
    + z('ellipse', '#e8735a', cx=60, cy=164, rx=12, ry=8) + s('path', d='M50 160 Q60 154 70 160', stroke_width=2))

# 13. autumn
ITEMS['autumn'] = (
    z('path', '#f5d58a', d='M24 156 Q100 140 176 156 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
    + z('path', '#9a6a3f', d='M90 164 L94 112 Q84 104 76 104 L80 98 Q90 102 96 106 L100 92 L106 94 L104 108 Q114 102 124 104 L124 110 Q110 112 106 120 L110 164Z')
    + z('path', '#f5b971', d=blob(100, 74, 62, 46, 10, 0.12))
    + z('path', '#e8735a', d=blob(72, 84, 24, 18, 7, 0.12)) + z('path', '#e04b5a', d=blob(128, 66, 22, 18, 7, 0.12))
    + z('path', '#ffc94d', d=blob(102, 54, 18, 14, 7, 0.12))
    + leafy(38, 120, 30, '#e8735a') + leafy(160, 112, -40, '#e04b5a') + leafy(146, 140, 70, '#f5b971')
    + leafy(52, 146, -60, '#e04b5a', 0.9) + leafy(130, 162, 90, '#e8735a', 0.8) + leafy(70, 166, 80, '#ffc94d', 0.8))

# 14. winter
_flakes = ''
for (x, y, r) in [(40, 48, 7), (78, 34, 5), (150, 36, 7), (168, 76, 5), (34, 96, 5), (122, 52, 5)]:
    _flakes += s('path', d=f'M{x - r} {y} L{x + r} {y} M{_r(x - r * .5)} {_r(y - r * .87)} L{_r(x + r * .5)} {_r(y + r * .87)} '
                           f'M{_r(x - r * .5)} {_r(y + r * .87)} L{_r(x + r * .5)} {_r(y - r * .87)}', stroke='#8fb3e0', stroke_width=2.5)
ITEMS['winter'] = (
    _flakes
    + pine(152, 152, 60, snow=True) + pine(46, 148, 46, snow=True)
    + z('path', '#ffffff', d='M24 146 Q100 128 176 148 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
    + z('circle', '#ffffff', cx=100, cy=138, r=32)
    + z('circle', '#ffffff', cx=100, cy=86, r=26)
    + z('path', '#e8735a', d='M76 104 Q100 116 124 104 L124 112 Q100 124 76 112Z', stroke_width=2.5)
    + z('rect', '#e8735a', x=106, y=110, width=11, height=24, rx=3, stroke_width=2.5)
    + dot(91, 82) + dot(109, 82) + cheeks(82, 118, 92, 5, 3)
    + s('path', '#f5b971', d='M98 88 L112 92 L98 94Z', stroke_width=2)
    + dot(100, 132, 3) + dot(100, 146, 3)
    + z('path', '#5b6b7a', d='M80 68 Q100 58 120 68 L116 52 Q100 46 84 52Z', stroke_width=2.5))

# 15. leaf
ITEMS['leaf'] = (
    s('path', d='M54 150 Q44 164 34 176', stroke_width=4)
    + z('path', '#9ccf7a', d='M54 150 Q30 90 76 56 Q114 30 164 34 Q168 92 136 126 Q100 162 54 150Z')
    + s('path', d='M54 150 Q100 104 156 42', stroke_width=2.5)
    + s('path', d='M80 122 L70 98 M100 100 L94 72 M124 76 L122 54 M88 112 L114 120 M110 88 L138 92 M132 64 L152 66', stroke_width=2)
    + dot(96, 124, 3.5) + dot(118, 124, 3.5) + cheeks(87, 127, 133, 5, 3)
    + s('path', d='M103 132 Q107 136 111 132', stroke_width=2.5)
    + z('path', '#8fc7e8', d='M150 92 Q156 100 155 104 Q152 108 148 105 Q145 100 150 92Z', stroke_width=2))


# 16. clover-field
HEART = 'M0 0 C-3 -5 -15 -10 -14 -21 C-13 -29 -3 -29 0 -21 C3 -29 13 -29 14 -21 C15 -10 3 -5 0 0Z'


def clover(x, y, k, n=3, c='#7cc4a0'):
    o = ''
    for i in range(n):
        o += z('path', c, d=HEART, transform=f'translate({x} {y}) rotate({_r(i * 360 / n)}) scale({k})', stroke_width=_r(2.5 / k))
    return o + s('circle', '#9ccf7a', cx=x, cy=y, r=_r(3 * k), stroke='none')


_cf = z('path', '#9ccf7a', d='M24 130 Q100 116 176 130 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
_cf += s('path', d='M44 130 L40 118 L48 126 M150 128 L154 116 L158 126 M120 124 L118 114 L124 122', stroke_width=2.5)
_cf += s('path', d='M66 160 Q62 130 60 112 M140 160 Q144 126 144 106 M100 170 Q102 120 100 78', stroke_width=3)
_cf += clover(60, 104, 0.95) + clover(144, 98, 0.95) + clover(100, 72, 1.25, 4, '#9ccf7a')
_cf += clover(42, 160, 0.6) + clover(164, 162, 0.6) + clover(124, 168, 0.5)
ITEMS['clover-field'] = _cf + sparkle(150, 46, 8) + sparkle(52, 52, 6)

# 17. moss-stump
ITEMS['moss-stump'] = (
    z('path', '#d9a66b', d='M48 172 Q58 162 58 140 L58 92 L142 92 L142 140 Q142 162 154 172 Q130 166 120 174 Q100 166 82 174 Q70 166 48 172Z')
    + z('ellipse', '#f6e0c4', cx=100, cy=92, rx=42, ry=16)
    + s('ellipse', cx=100, cy=92, rx=26, ry=9, stroke_width=2) + s('ellipse', cx=100, cy=92, rx=11, ry=4, stroke_width=2)
    + z('path', '#9ccf7a', d='M56 98 Q58 84 74 84 Q86 80 92 90 Q86 104 74 104 Q60 110 56 98Z')
    + z('path', '#7cc4a0', d='M120 100 Q128 86 142 92 Q150 102 144 110 Q134 112 120 100Z', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M54 160 Q56 144 70 148 Q84 146 84 158 Q86 170 70 168 Q56 170 54 160Z', stroke_width=2.5)
    + s('path', d='M126 150 Q130 136 128 120', stroke_width=2)
    + dot(88, 128, 4) + dot(114, 128, 4) + cheeks(78, 124, 139, 6, 3.5) + s('path', d='M95 138 Q101 144 107 138', stroke_width=2.5)
    + s('rect', '#f6e0c4', x=156, y=150, width=8, height=20, rx=3, stroke_width=2.5)
    + z('path', '#e8735a', d='M148 152 Q150 132 160 132 Q170 132 172 152Z', stroke_width=2.5)
    + dot(156, 142, 2.2, '#ffffff') + dot(165, 145, 2, '#ffffff')
    + s('path', d='M26 176 L176 176', stroke_width=2.5))

# 18. cave
ITEMS['cave'] = (
    z('path', '#b9a99c', d='M24 174 Q24 120 46 92 Q66 56 104 52 Q144 52 162 88 Q178 118 176 174Z')
    + z('path', '#9ccf7a', d='M54 80 Q70 56 104 52 Q132 52 150 72 Q138 70 128 76 Q116 66 104 72 Q90 64 80 74 Q66 70 54 80Z', stroke_width=2.5)
    + z('path', '#5b6b7a', d='M64 174 Q60 112 100 104 Q140 112 136 174Z')
    + s('path', d='M40 128 Q48 122 54 128 M150 120 Q156 116 162 122 M146 150 Q152 146 158 150', stroke_width=2.5)
    + z('ellipse', '#c9d3db', cx=46, cy=170, rx=16, ry=9, stroke_width=2.5)
    + z('ellipse', '#c9d3db', cx=154, cy=170, rx=14, ry=8, stroke_width=2.5)
    + s('path', d='M74 176 L70 164 M80 176 L82 164 M124 176 L122 164 M130 176 L134 166', stroke='#4f9a5a', stroke_width=2.5)
    + dot(94, 140, 3, '#ffe27a') + dot(106, 140, 3, '#ffe27a')
    + s('path', d='M20 178 L180 178', stroke_width=2.5))

# 19. cliff-sea
ITEMS['cliff-sea'] = (
    z('circle', '#ffe27a', cx=150, cy=46, r=16)
    + s('path', d='M128 72 Q134 66 140 72 Q146 66 152 72 M104 52 Q109 47 114 52 Q119 47 124 52', stroke_width=2.5)
    + z('path', '#8fc7e8', d='M80 118 Q96 110 112 118 Q128 126 144 118 Q160 110 176 118 L176 172 Q176 178 170 178 L80 178Z')
    + s('path', d='M110 140 Q118 134 126 140 M146 150 Q154 144 162 150 M118 164 Q126 158 134 164', stroke='#ffffff', stroke_width=3)
    + z('path', '#d9a66b', d='M24 72 Q50 62 92 70 Q100 90 92 108 Q104 124 100 146 Q110 162 104 178 L30 178 Q24 178 24 172Z')
    + s('path', d='M48 100 L60 112 M70 130 L86 128 M50 150 L64 160', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M22 74 Q50 60 94 68 Q96 80 88 80 Q80 76 74 84 Q64 76 54 84 Q44 76 34 84 Q26 80 22 74Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M100 168 Q106 156 114 162 Q120 152 128 162 Q132 170 124 172 L104 174Z', stroke_width=2.5))

# 20. hill
ITEMS['hill'] = (
    z('ellipse', '#ffffff', cx=56, cy=50, rx=22, ry=10) + z('ellipse', '#ffffff', cx=146, cy=40, rx=18, ry=8)
    + z('path', '#7cc4a0', d='M24 112 Q70 64 120 100 Q150 76 176 92 L176 140 L24 140Z')
    + z('path', '#9ccf7a', d='M24 146 Q76 102 132 132 Q156 120 176 128 L176 172 Q176 178 170 178 L30 178 Q24 178 24 172Z')
    + z('path', '#f5d58a', d='M110 178 Q96 160 112 146 Q124 136 118 124 Q132 136 124 150 Q112 164 128 178Z', stroke_width=2.5)
    + s('rect', '#8b6b4f', x=147, y=106, width=6, height=14, stroke_width=2.5)
    + z('circle', '#7cc4a0', cx=150, cy=98, r=12, stroke_width=2.5)
    + s('rect', '#8b6b4f', x=57, y=86, width=5, height=12, stroke_width=2)
    + z('circle', '#9ccf7a', cx=59, cy=80, r=9, stroke_width=2.5)
    + flower(52, 158, 4, '#ffffff', '#ffe27a', stem=False, sw=2) + flower(156, 156, 4, '#f6a6b8', '#ffe27a', stem=False, sw=2)
    + flower(76, 168, 3.5, '#ffe27a', '#f5b971', stem=False, sw=2))
