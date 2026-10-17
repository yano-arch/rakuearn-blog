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
    """ふわっとした雲（幅 w の中央 cx, 底 cy）"""
    k = w / 100
    p = [(-50, 0), (-50, -18), (-30, -26), (-22, -48), (6, -52), (22, -38), (44, -36), (50, -14), (50, 0)]
    d = f'M{_r(cx + p[0][0] * k)} {_r(cy)}'
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


# 1. sun
_rays = ''
for i in range(12):
    a = math.radians(i * 30)
    ca, sa = math.cos(a), math.sin(a)
    tip = (100 + 74 * ca, 100 + 74 * sa)
    b1 = (100 + 56 * ca - 8 * sa, 100 + 56 * sa + 8 * ca)
    b2 = (100 + 56 * ca + 8 * sa, 100 + 56 * sa - 8 * ca)
    _rays += z('path', '#ffc94d', d=f'M{_r(b1[0])} {_r(b1[1])} L{_r(tip[0])} {_r(tip[1])} L{_r(b2[0])} {_r(b2[1])}Z')
ITEMS['sun'] = (_rays + z('circle', '#ffe27a', cx=100, cy=100, r=48)
                + dot(86, 98, 4) + dot(114, 98, 4) + cheeks(74, 126, 112, 7, 4)
                + s('path', d='M92 114 Q100 122 108 114'))

# 2. rain-cloud
ITEMS['rain-cloud'] = (
    z('path', '#8fc7e8', d=drop(64, 138, 18)) + z('path', '#8fc7e8', d=drop(100, 148, 18))
    + z('path', '#8fc7e8', d=drop(136, 138, 18)) + z('path', '#8fc7e8', d=drop(82, 168, 14))
    + z('path', '#8fc7e8', d=drop(118, 168, 14))
    + z('path', '#c9d3db', d=cloud(100, 128, 124))
    + dot(86, 104, 4) + dot(114, 104, 4) + cheeks(74, 126, 114, 7, 4)
    + s('path', d='M94 116 Q100 120 106 116'))


# 3. rainbow
def band(cx, cy, R, r):
    return f'M{cx - R} {cy} A{R} {R} 0 0 1 {cx + R} {cy} L{cx + r} {cy} A{r} {r} 0 0 0 {cx - r} {cy}Z'


ITEMS['rainbow'] = (z('path', '#e8735a', d=band(100, 146, 72, 58)) + z('path', '#ffc94d', d=band(100, 146, 58, 44))
                    + z('path', '#9ccf7a', d=band(100, 146, 44, 30)) + z('path', '#8fc7e8', d=band(100, 146, 30, 16))
                    + z('path', '#ffffff', d=cloud(40, 168, 58)) + z('path', '#ffffff', d=cloud(160, 168, 58)))

# 4. snowman
ITEMS['snowman'] = (
    s('path', d='M66 128 L40 108 M48 114 L40 102', stroke=OUT, stroke_width=3)
    + s('path', d='M134 128 L160 108 M152 114 L162 104', stroke_width=3)
    + z('ellipse', '#ffffff', cx=100, cy=146, rx=40, ry=34)
    + z('circle', '#ffffff', cx=100, cy=86, r=30)
    + dot(100, 138, 3.5) + dot(100, 154, 3.5)
    + z('path', '#e8735a', d='M70 108 Q100 120 130 108 L130 118 Q100 130 70 118Z')
    + z('path', '#e8735a', d='M112 118 L122 146 L108 146 L104 122Z')
    + z('path', '#8fb3e0', d='M78 64 L82 38 Q100 32 118 38 L122 64Z')
    + z('rect', '#8fb3e0', x=68, y=60, width=64, height=10, rx=5)
    + dot(90, 84, 3.5) + dot(110, 84, 3.5) + cheeks(80, 120, 94, 6, 3.5)
    + z('path', '#f5b971', d='M98 88 L114 92 L98 95Z')
    + s('path', d='M95 100 Q100 104 105 100', stroke_width=2.5)
    + s('path', d='M36 182 L164 182', stroke_width=2.5))

# 5. tree
ITEMS['tree'] = (
    z('path', '#9a6a3f', d='M90 180 L92 118 L108 118 L110 180Z')
    + z('path', '#9ccf7a', d='M60 128 Q34 126 36 100 Q32 76 54 70 Q56 40 86 38 Q102 22 122 38 Q152 38 152 66 '
                            'Q172 80 164 104 Q166 128 140 130 Q120 142 100 132 Q80 142 60 128Z')
    + s('path', d='M66 84 Q72 78 80 80 M116 58 Q124 54 130 58 M132 102 Q140 98 146 102 M86 112 Q92 108 98 112', stroke_width=2.5)
    + s('path', d='M40 182 L160 182', stroke_width=2.5))

# 6. tulip
ITEMS['tulip'] = (
    s('path', d='M100 182 L100 100', stroke_width=3)
    + z('path', '#7cc4a0', d='M100 178 Q64 162 60 116 Q92 132 100 178Z')
    + z('path', '#7cc4a0', d='M100 172 Q136 160 144 124 Q110 132 100 172Z')
    + z('path', '#f07a8a', d='M68 54 Q66 104 100 108 Q134 104 132 54 Q118 70 112 66 Q104 46 100 40 Q96 46 88 66 Q82 70 68 54Z')
    + s('path', d='M88 66 Q90 90 100 108 Q110 90 112 66', stroke_width=2.5)
    + s('path', d='M66 182 L134 182', stroke_width=2.5))

# 7. mountain
ITEMS['mountain'] = (
    z('circle', '#ffe27a', cx=148, cy=48, r=18)
    + s('path', d='M148 20 L148 14 M170 30 L175 25 M176 52 L182 52 M126 30 L121 25', stroke_width=2.5)
    + z('path', '#7cc4b0', d='M24 176 L90 62 Q100 50 110 62 L176 176Z')
    + z('path', '#ffffff', d='M73 92 L90 62 Q100 50 110 62 L127 92 L116 86 L108 96 L100 86 L92 96 L84 86Z')
    + z('path', '#ffffff', d=cloud(52, 62, 46))
    + s('path', d='M54 158 L57 150 L60 156 L63 150 L66 158 M128 162 L131 154 L134 160 L137 154 L140 162', stroke_width=2.5))

# 8. moon-stars
_R, _cx, _cy = 60, 92, 104
_r2, _c2x, _c2y = 50, 122, 82
_d = math.hypot(_c2x - _cx, _c2y - _cy)
_a = (_R ** 2 - _r2 ** 2 + _d ** 2) / (2 * _d)
_h = math.sqrt(_R ** 2 - _a ** 2)
_mx, _my = _cx + _a * (_c2x - _cx) / _d, _cy + _a * (_c2y - _cy) / _d
_p1 = (_mx + _h * (_c2y - _cy) / _d, _my - _h * (_c2x - _cx) / _d)
_p2 = (_mx - _h * (_c2y - _cy) / _d, _my + _h * (_c2x - _cx) / _d)
# p1/p2: pick the one with smaller y as top
_top, _bot = sorted([_p1, _p2], key=lambda p: p[1])
_moon = (f'M{_r(_top[0])} {_r(_top[1])} A{_R} {_R} 0 1 0 {_r(_bot[0])} {_r(_bot[1])} '
         f'A{_r2} {_r2} 0 0 1 {_r(_top[0])} {_r(_top[1])}Z')
ITEMS['moon-stars'] = (
    z('path', '#ffe27a', d=_moon)
    + s('path', d='M50 102 Q57 109 64 102', stroke_width=2.5)
    + f'<ellipse cx="54" cy="116" rx="6" ry="3.5" fill="{CH}" stroke="none"/>'
    + s('path', d='M62 128 Q68 133 74 128', stroke_width=2.5)
    + z('path', '#ffc94d', d=star(160, 132, 15)) + z('path', '#ffc94d', d=star(140, 46, 11))
    + z('path', '#ffc94d', d=star(170, 86, 8)) + z('path', '#ffc94d', d=star(138, 172, 8)))


# 9. autumn-leaves
def maple(cx, cy, R, rot=0):
    lob = [-90, -150, -30, 150, 30]
    order = [-90, -30, 30, 90, 150, 210]  # walk around (90 = stem gap)
    angs = [-90, -40, 20, 90, 160, 220]
    pts = []
    lobes = [(-90, 1.0), (-35, 0.92), (25, 0.75), (155, 0.75), (215, 0.92)]
    seq = []
    for i, (a, k) in enumerate(lobes):
        seq += [(a - 13, R * k * 0.62, 's'), (a - 9, R * k * 0.72, 's'), (a, R * k, 'tip'),
                (a + 9, R * k * 0.72, 's'), (a + 13, R * k * 0.62, 's')]
        nxt = lobes[(i + 1) % len(lobes)][0]
        if nxt < a:
            nxt += 360
        seq.append(((a + nxt) / 2, R * (0.34 if nxt - a > 100 else 0.4), 'in'))
    d = ''
    for j, (a, rr, kind) in enumerate(seq):
        t = math.radians(a + rot)
        x, y = _r(cx + rr * math.cos(t)), _r(cy + rr * math.sin(t))
        d += (f'M{x} {y}' if j == 0 else f' L{x} {y}')
    return d + 'Z'


def leaf_full(cx, cy, R, rot, col):
    t = math.radians(90 + rot)
    sx, sy = _r(cx + R * 0.95 * math.cos(t)), _r(cy + R * 0.95 * math.sin(t))
    v = ''
    for a in (-90, -35, 215):
        u = math.radians(a + rot)
        v += f'M{cx} {cy} L{_r(cx + R * 0.55 * math.cos(u))} {_r(cy + R * 0.55 * math.sin(u))} '
    return (s('path', d=f'M{cx} {cy} L{sx} {sy}', stroke_width=3)
            + z('path', col, d=maple(cx, cy, R, rot))
            + s('path', d=v + f'M{cx} {cy} L{_r(cx + R * 0.3 * math.cos(t))} {_r(cy + R * 0.3 * math.sin(t))}', stroke_width=2))


ITEMS['autumn-leaves'] = (leaf_full(70, 82, 44, -20, '#ffc94d') + leaf_full(132, 92, 44, 18, '#e8735a')
                          + leaf_full(96, 140, 36, -4, '#e04b5a'))

# 10. sprout
ITEMS['sprout'] = (
    s('path', d='M100 132 Q98 112 100 92', stroke_width=3.5)
    + z('path', '#9ccf7a', d='M100 96 Q86 58 46 66 Q52 104 100 96Z')
    + z('path', '#7cc4a0', d='M100 92 Q112 54 154 58 Q150 98 100 92Z')
    + s('path', d='M96 92 Q78 80 62 74 M104 88 Q122 76 138 66', stroke_width=2)
    + z('path', '#9a6a3f', d='M40 176 Q44 130 100 126 Q156 130 160 176Z')
    + dot(86, 152, 3.5, '#3b2f2a') + dot(114, 152, 3.5) + cheeks(76, 124, 162, 6, 3.5)
    + s('path', d='M95 160 Q100 164 105 160', stroke_width=2.5)
    + s('path', d='M30 178 L170 178', stroke_width=2.5))
