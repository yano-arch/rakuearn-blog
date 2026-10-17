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


def tube(d, color, w=8):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def mini(cx, cy, gap=10, ch=16, r=3, my=8):
    return (dot(cx - gap, cy, r) + dot(cx + gap, cy, r) + cheeks(cx - ch, cx + ch, cy + 7, 5, 3)
            + s('path', d=f'M{cx - 4} {cy + my} Q{cx} {cy + my + 4} {cx + 4} {cy + my}', stroke_width=2.5))


def rays(cx, cy, r0, r1, n=10, w=7, col='#ffc94d', start=0, span=360):
    o = ''
    for i in range(n):
        a = math.radians(start + i * span / n)
        ca, sa = math.cos(a), math.sin(a)
        b1 = (cx + r0 * ca - w * sa, cy + r0 * sa + w * ca)
        b2 = (cx + r0 * ca + w * sa, cy + r0 * sa - w * ca)
        t = (cx + r1 * ca, cy + r1 * sa)
        o += z('path', col, d=f'M{_r(b1[0])} {_r(b1[1])} L{_r(t[0])} {_r(t[1])} L{_r(b2[0])} {_r(b2[1])}Z')
    return o


def flower(cx, cy, R, petal, center, n=6, pr=None):
    pr = pr or R * 0.55
    o = ''
    for i in range(n):
        a = math.radians(i * 360 / n - 90)
        o += z('circle', petal, cx=_r(cx + R * 0.62 * math.cos(a)), cy=_r(cy + R * 0.62 * math.sin(a)), r=_r(pr))
    return o + z('circle', center, cx=cx, cy=cy, r=_r(R * 0.42))


def sparkle(x, y, k=1.0, col='#ffe27a'):
    return s('path', col, d=f'M{x} {_r(y - 7 * k)} Q{_r(x + 1.5 * k)} {_r(y - 1.5 * k)} {_r(x + 7 * k)} {y} '
             f'Q{_r(x + 1.5 * k)} {_r(y + 1.5 * k)} {x} {_r(y + 7 * k)} Q{_r(x - 1.5 * k)} {_r(y + 1.5 * k)} '
             f'{_r(x - 7 * k)} {y} Q{_r(x - 1.5 * k)} {_r(y - 1.5 * k)} {x} {_r(y - 7 * k)}Z', stroke_width=2)


# 1. puddle
ITEMS['puddle'] = (
    z('path', '#8fc7e8', d='M34 136 Q30 112 62 108 Q84 100 108 106 Q140 100 164 114 Q182 130 164 148 '
      'Q140 166 104 162 Q70 168 46 156 Q30 150 34 136Z')
    + s('ellipse', cx=84, cy=132, rx=26, ry=9, stroke='#ffffff', stroke_width=3)
    + s('ellipse', cx=84, cy=132, rx=12, ry=4, stroke='#ffffff', stroke_width=3)
    + s('ellipse', cx=138, cy=140, rx=16, ry=6, stroke='#ffffff', stroke_width=3)
    + z('path', '#8fc7e8', d=drop(84, 52, 22)) + z('path', '#8fc7e8', d=drop(138, 76, 18))
    + z('path', '#8fc7e8', d=drop(56, 82, 14))
    + s('path', d='M66 112 L60 102 M102 112 L106 100 M84 114 L84 100', stroke_width=2.5)
    + mini(110, 144, 9, 15, 3, 7))

# 2. icicle
_ic = ''
for x, ln, w in ((46, 58, 10), (73, 92, 11), (100, 116, 13), (127, 84, 11), (154, 62, 10)):
    _ic += z('path', '#8fc7e8', d=f'M{x - w} 60 Q{x - w * 0.6} {60 + ln * 0.7} {x} {60 + ln} Q{x + w * 0.6} {60 + ln * 0.7} {x + w} 60Z')
    _ic += s('path', d=f'M{_r(x - w * 0.4)} 70 Q{_r(x - w * 0.35)} {_r(60 + ln * 0.4)} {_r(x - w * 0.15)} {_r(60 + ln * 0.6)}',
             stroke='#ffffff', stroke_width=2.5)
ITEMS['icicle'] = (
    _ic
    + z('rect', '#8b6b4f', x=26, y=46, width=148, height=16, rx=3)
    + z('path', '#ffffff', d='M24 50 Q30 32 56 36 Q74 26 96 34 Q120 26 140 34 Q166 30 176 50 Q178 60 168 60 L32 60 Q22 60 24 50Z')
    + z('path', '#8fc7e8', d=drop(100, 176, 10))
    + dot(95, 92, 2.6) + dot(105, 92, 2.6) + cheeks(91, 109, 98, 3, 2)
    + s('path', d='M98 100 Q100 102 102 100', stroke_width=2))

# 3. sunbeam-clouds
ITEMS['sunbeam-clouds'] = (
    rays(84, 92, 50, 76, 9, 7, start=150, span=240)
    + z('circle', '#ffe27a', cx=84, cy=92, r=44)
    + dot(70, 84, 3.5) + dot(96, 84, 3.5) + cheeks(60, 106, 96, 6, 3.5)
    + s('path', d='M78 98 Q84 104 90 98')
    + z('path', '#ffffff', d=cloud(116, 166, 128))
    + z('path', '#ffffff', d=cloud(48, 168, 46))
    + s('path', d='M150 46 L158 38 M164 66 L176 62', stroke_width=2.5))

# 4. crescent-moon


def crescent(cx, cy, R, ox, oy, r):
    dx, dy = ox - cx, oy - cy
    d = math.hypot(dx, dy)
    a = (R * R - r * r + d * d) / (2 * d)
    h = math.sqrt(R * R - a * a)
    mx, my = cx + a * dx / d, cy + a * dy / d
    p1 = (mx + h * dy / d, my - h * dx / d)
    p2 = (mx - h * dy / d, my + h * dx / d)
    return (f'M{_r(p1[0])} {_r(p1[1])} A{R} {R} 0 1 0 {_r(p2[0])} {_r(p2[1])} '
            f'A{r} {r} 0 1 1 {_r(p1[0])} {_r(p1[1])}Z')


ITEMS['crescent-moon'] = (
    z('path', '#ffe27a', d=crescent(96, 104, 66, 132, 80, 56))
    + dot(56, 116, 3.5) + dot(76, 128, 3.5) + cheeks(48, 82, 132, 6, 3.5)
    + s('path', d='M60 136 Q64 142 70 140')
    + z('path', '#ffc94d', d=star(152, 128, 14)) + z('path', '#ffc94d', d=star(160, 50, 10))
    + sparkle(126, 168, 1.0) + sparkle(178, 90, 0.8))

# 5. milky-way
_mw = ''
for x, y, r in ((52, 150, 2.2), (64, 128, 1.8), (80, 120, 2.4), (92, 104, 1.8), (100, 96, 2.6), (116, 84, 2),
                (124, 70, 2.4), (140, 62, 1.8), (148, 48, 2.2), (72, 140, 1.6), (108, 112, 1.6), (132, 88, 1.6),
                (88, 132, 2), (156, 72, 1.6), (60, 112, 1.6), (112, 64, 1.6)):
    _mw += dot(x, y, r, '#ffffff')
ITEMS['milky-way'] = (
    z('rect', '#5b6b7a', x=26, y=28, width=146, height=146, rx=16)
    + s('path', '#a98bd0', d='M30 150 Q60 136 80 108 Q104 72 150 32 L170 32 L170 74 Q134 100 114 132 Q92 164 70 170 L30 170Z',
        stroke='none')
    + s('path', '#8fb3e0', d='M38 162 Q70 144 90 116 Q112 84 166 46 L168 60 Q126 92 104 124 Q82 158 54 170Z', stroke='none')
    + _mw
    + z('path', '#ffe27a', d=star(56, 62, 11)) + z('path', '#ffe27a', d=star(146, 138, 13))
    + sparkle(88, 50, 0.9, '#ffffff') + sparkle(150, 100, 0.8, '#ffffff') + sparkle(48, 104, 0.7, '#ffffff'))

# 6. planet-earth-moon
ITEMS['planet-earth-moon'] = (
    s('path', d='M30 150 Q20 104 76 70 Q130 40 172 56', stroke='#b9a99c', stroke_width=2.5, stroke_dasharray='6 7')
    + z('circle', '#8fc7e8', cx=88, cy=118, r=56)
    + s('path', '#9ccf7a', d='M54 92 Q72 76 88 88 Q90 106 70 108 Q52 108 54 92Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M104 120 Q128 108 138 128 Q130 150 112 148 Q98 136 104 120Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M44 130 Q58 128 62 140 Q56 154 46 146Z', stroke_width=2.5)
    + dot(78, 122, 3.5) + dot(98, 122, 3.5) + cheeks(68, 108, 132, 6, 3.5)
    + s('path', d='M83 131 Q88 136 93 131', stroke_width=2.5)
    + z('circle', '#f4f4f0', cx=152, cy=58, r=24)
    + s('circle', '#c9d3db', cx=144, cy=48, r=5, stroke_width=2) + s('circle', '#c9d3db', cx=164, cy=66, r=4, stroke_width=2)
    + dot(146, 60, 2.5) + dot(158, 60, 2.5) + s('path', d='M149 67 Q152 70 155 67', stroke_width=2)
    + sparkle(170, 116, 0.9) + sparkle(36, 54, 0.8))

# 7. lavender


def lav(x0, y0, x1, y1, n=5):
    o = tube(f'M{x0} {y0} L{x1} {y1}', '#7cc4a0', 3)
    for i in range(n):
        t = i / n
        x = x1 + (x0 - x1) * t * 0.5
        y = y1 + (y0 - y1) * t * 0.5
        sd = -5 if i % 2 else 5
        o += z('ellipse', '#a98bd0', cx=_r(x + sd), cy=_r(y), rx=6, ry=8)
    return o + z('ellipse', '#a98bd0', cx=x1, cy=y1 - 4, rx=5, ry=7)


ITEMS['lavender'] = (
    lav(100, 178, 58, 46) + lav(100, 178, 142, 46) + lav(100, 178, 100, 34)
    + z('path', '#f6a6b8', d='M100 142 Q76 128 74 142 Q78 154 100 146Z')
    + z('path', '#f6a6b8', d='M100 142 Q124 128 126 142 Q122 154 100 146Z')
    + z('path', '#f6a6b8', d='M98 146 L88 170 L96 168 L100 148 L104 168 L112 170 L102 146Z')
    + z('circle', '#f6a6b8', cx=100, cy=144, r=6))

# 8. poppy


def poppy(cx, cy, R, col='#e04b5a'):
    o = z('path', col, d=f'M{cx} {cy} Q{cx - R * 1.3} {cy - R * 0.2} {cx - R * 0.9} {cy - R * 0.9} Q{cx - R * 0.4} {cy - R * 1.2} {cx} {cy - R * 0.6}Z')
    o += z('path', col, d=f'M{cx} {cy} Q{cx + R * 1.3} {cy - R * 0.2} {cx + R * 0.9} {cy - R * 0.9} Q{cx + R * 0.4} {cy - R * 1.2} {cx} {cy - R * 0.6}Z')
    o += z('path', col, d=f'M{cx - R} {cy - R * 0.3} Q{cx - R * 1.1} {cy + R * 0.8} {cx} {cy + R * 0.85} Q{cx + R * 1.1} {cy + R * 0.8} {cx + R} {cy - R * 0.3} Q{cx} {cy + R * 0.1} {cx - R} {cy - R * 0.3}Z')
    o += s('ellipse', OUT, cx=cx, cy=_r(cy - R * 0.1), rx=_r(R * 0.32), ry=_r(R * 0.22))
    return o


ITEMS['poppy'] = (
    tube('M70 92 Q64 140 76 182', '#7cc4a0', 4) + tube('M130 80 Q140 130 126 182', '#7cc4a0', 4)
    + tube('M100 118 Q102 150 100 182', '#7cc4a0', 4) + tube('M156 132 Q160 160 150 182', '#7cc4a0', 3)
    + z('path', '#9ccf7a', d='M74 166 Q50 150 46 160 Q56 174 74 172Z')
    + z('path', '#9ccf7a', d='M126 166 Q152 150 156 160 Q146 176 126 172Z')
    + poppy(70, 82, 30) + poppy(130, 70, 30, '#e8735a') + poppy(100, 112, 24)
    + z('ellipse', '#9ccf7a', cx=156, cy=126, rx=7, ry=10)
    + s('path', d='M30 182 L170 182', stroke_width=2.5))

# 9. daisy
_dp = ''
for i in range(12):
    a = i * 30
    _dp += (f'<g transform="rotate({a} 100 82)">' + z('ellipse', '#ffffff', cx=100, cy=44, rx=11, ry=24) + '</g>')
ITEMS['daisy'] = (
    tube('M100 110 Q96 150 102 186', '#7cc4a0', 5)
    + z('path', '#9ccf7a', d='M99 160 Q70 136 54 146 Q70 170 99 166Z')
    + z('path', '#9ccf7a', d='M100 150 Q130 126 146 136 Q130 160 100 156Z')
    + _dp
    + z('circle', '#ffc94d', cx=100, cy=82, r=24)
    + dot(92, 80, 3) + dot(108, 80, 3) + cheeks(86, 114, 87, 4.5, 2.8)
    + s('path', d='M96 89 Q100 93 104 89', stroke_width=2.5))

# 10. bonsai
ITEMS['bonsai'] = (
    tube('M98 150 Q80 132 96 112 Q112 96 92 80', '#9a6a3f', 10)
    + tube('M96 112 Q120 106 132 92', '#9a6a3f', 6) + tube('M90 88 Q72 84 62 92', '#9a6a3f', 5)
    + z('path', '#7cc4a0', d='M42 96 Q40 80 58 80 Q66 68 82 76 Q92 86 80 96 Q62 104 42 96Z')
    + z('path', '#7cc4a0', d='M110 92 Q110 74 130 76 Q142 66 156 76 Q166 92 150 98 Q126 104 110 92Z')
    + z('path', '#9ccf7a', d='M62 64 Q62 44 86 44 Q100 30 118 42 Q140 44 136 64 Q120 76 98 72 Q74 76 62 64Z')
    + s('path', d='M80 60 Q88 56 96 60 M106 56 Q114 52 122 56', stroke_width=2)
    + z('path', '#8fb3e0', d='M46 150 L154 150 L146 176 L54 176Z')
    + z('rect', '#5b6b7a', x=40, y=144, width=120, height=10, rx=3)
    + z('rect', '#5b6b7a', x=62, y=176, width=12, height=6, rx=2) + z('rect', '#5b6b7a', x=126, y=176, width=12, height=6, rx=2)
    + s('path', '#9ccf7a', d='M66 146 Q100 138 134 146', stroke_width=2.5))

# 11. seed
_seeds = ''
for x, y, rt in ((78, 112, -20), (96, 106, 10), (114, 112, 30), (88, 120, 60), (108, 122, -40), (124, 118, 0)):
    _seeds += f'<g transform="rotate({rt} {x} {y})">' + z('ellipse', '#9a6a3f', cx=x, cy=y, rx=7, ry=5) + '</g>'
ITEMS['seed'] = (
    z('path', '#8fb3e0', d='M58 160 L50 190 L92 190 L96 162Z') + z('path', '#8fb3e0', d='M142 160 L150 190 L108 190 L104 162Z')
    + _seeds
    + tube('M100 104 Q98 86 102 70', '#7cc4a0', 3)
    + z('path', '#9ccf7a', d='M101 76 Q82 56 70 64 Q80 82 101 76Z')
    + z('path', '#9ccf7a', d='M102 72 Q118 48 134 58 Q124 76 102 72Z')
    + z('path', '#ffd9b8', d='M42 112 Q60 124 100 126 Q140 124 158 112 Q164 150 136 162 Q118 168 100 164 Q82 168 64 162 Q36 150 42 112Z')
    + s('path', d='M100 130 L100 164', stroke_width=2.5)
    + ''.join(f'<g transform="rotate({r} {x} {y})">' + z('rect', '#ffd9b8', x=x - 14, y=y - 7, width=28, height=14, rx=7) + '</g>'
              for x, y, r in ((40, 116, 70), (40, 132, 60), (46, 146, 45), (160, 116, -70), (160, 132, -60), (154, 146, -45)))
    + s('path', d='M66 128 Q76 132 84 130 M134 128 Q124 132 116 130', stroke_width=2.5))

# 12. mushroom-forest


def tree(cx, base, h, col):
    return (z('rect', '#9a6a3f', x=cx - 7, y=base - h * 0.4, width=14, height=h * 0.4, rx=3)
            + z('circle', col, cx=cx, cy=base - h * 0.65, r=h * 0.38))


ITEMS['mushroom-forest'] = (
    tree(52, 150, 100, '#7cc4a0') + tree(150, 146, 110, '#9ccf7a')
    + z('path', '#9ccf7a', d='M24 182 Q24 152 60 156 Q100 146 140 156 Q178 152 178 182Z')
    + s('path', d='M40 160 L44 152 L48 160 M156 160 L160 152 L164 160', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=88, y=136, width=26, height=36, rx=10)
    + z('path', '#e04b5a', d='M66 140 Q66 98 101 98 Q136 98 136 140 Q101 132 66 140Z')
    + s('circle', '#ffffff', cx=86, cy=118, r=6, stroke_width=2) + s('circle', '#ffffff', cx=110, cy=110, r=5, stroke_width=2)
    + s('circle', '#ffffff', cx=122, cy=126, r=4, stroke_width=2)
    + dot(95, 152, 2.8) + dot(107, 152, 2.8) + cheeks(91, 111, 159, 3.5, 2.2)
    + s('path', d='M98 158 Q101 161 104 158', stroke_width=2)
    + z('rect', '#f6e0c4', x=136, y=152, width=14, height=22, rx=6)
    + z('path', '#d9a66b', d='M124 156 Q124 132 143 132 Q162 132 162 156 Q143 151 124 156Z')
    + z('rect', '#f6e0c4', x=50, y=158, width=10, height=16, rx=4)
    + z('path', '#f5b971', d='M42 160 Q42 142 55 142 Q68 142 68 160 Q55 156 42 160Z'))

# 13. snow-mountain
ITEMS['snow-mountain'] = (
    z('circle', '#ffe27a', cx=154, cy=50, r=16)
    + z('path', '#8fb3e0', d='M18 176 L64 92 L104 176Z')
    + z('path', '#8fb3e0', d='M96 176 L146 82 L184 176Z')
    + z('path', '#7cc4b0', d='M46 176 L102 50 L158 176Z')
    + z('path', '#ffffff', d='M102 50 L126 104 L116 98 L108 108 L100 98 L90 108 L84 96 L78 104Z')
    + z('path', '#ffffff', d='M64 92 L78 118 L70 114 L64 120 L58 114 L52 118Z')
    + z('path', '#ffffff', d='M146 82 L160 108 L152 104 L146 110 L140 104 L133 108Z')
    + s('path', d='M14 178 L186 178', stroke_width=2.5))

# 14. aurora
ITEMS['aurora'] = (
    z('rect', '#5b6b7a', x=24, y=26, width=150, height=148, rx=16)
    + s('path', '#7cc4a0', d='M28 92 Q60 54 96 80 Q130 104 170 60 L170 92 Q130 130 96 106 Q60 82 28 118Z', stroke_width=2.5)
    + s('path', '#a98bd0', d='M28 118 Q60 82 96 106 Q130 130 170 92 L170 110 Q130 146 96 122 Q60 100 28 132Z', stroke_width=2.5)
    + s('path', d='M50 96 L50 120 M72 82 L72 104 M120 98 L120 120 M146 82 L146 106', stroke='#ffffff', stroke_width=2)
    + dot(48, 46, 2, '#ffffff') + dot(140, 40, 2.2, '#ffffff') + dot(100, 52, 1.8, '#ffffff') + dot(160, 140, 1.6, '#ffffff')
    + sparkle(76, 44, 0.8, '#ffffff') + sparkle(156, 52, 0.7, '#ffffff')
    + s('path', '#7a5ea8', d='M28 150 L56 124 L80 146 L108 118 L140 150 L170 132 L170 160 Q170 170 160 170 L38 170 Q28 170 28 160Z',
        stroke_width=2.5)
    + ''.join(s('path', '#3b2f2a', d=f'M{x} 170 L{x} 162 L{x - 8} 162 L{x} 150 L{x - 6} 150 L{x + 1} 138 L{x + 8} 150 L{x + 2} 150 L{x + 10} 162 L{x + 2} 162 L{x + 2} 170Z', stroke_width=1.5)
              for x in (48, 66, 140, 156)))

# 15. coral-reef
ITEMS['coral-reef'] = (
    tube('M62 168 L62 130 M62 140 Q44 128 42 104 M62 132 Q66 110 56 88 M62 146 Q80 130 84 106', '#f6a6b8', 9)
    + tube('M134 168 L134 134 M134 150 Q152 136 156 112 M134 140 Q124 120 128 98 M140 128 Q150 110 146 92', '#e8735a', 8)
    + z('ellipse', '#a98bd0', cx=100, cy=158, rx=26, ry=20)
    + s('path', d='M80 156 Q90 146 100 156 Q110 166 120 154 M84 166 Q100 158 116 166', stroke_width=2)
    + z('path', '#f5d58a', d='M24 182 Q40 168 70 172 Q100 164 130 172 Q162 166 178 182Z')
    + z('path', '#ffc94d', d='M98 66 Q112 52 128 66 Q112 80 98 66Z')
    + z('path', '#ffc94d', d='M98 66 L88 58 L88 74Z')
    + dot(120, 64, 2.5)
    + s('circle', cx=146, cy=56, r=4, stroke='#8fc7e8', stroke_width=2.5) + s('circle', cx=154, cy=42, r=6, stroke='#8fc7e8', stroke_width=2.5)
    + s('circle', cx=74, cy=50, r=5, stroke='#8fc7e8', stroke_width=2.5))

# 16. sea-grass


def weed(x, top, col, amp=10):
    return z('path', col, d=f'M{x - 7} 176 Q{x - 7 - amp} 150 {x - 4} 128 Q{x + amp - 4} 108 {x - 2} {top + 20} '
             f'Q{x - amp} {top + 8} {x} {top} Q{x + amp + 6} {top + 14} {x + 6} {top + 26} Q{x + amp + 6} 110 {x + 5} 130 '
             f'Q{x - amp + 8} 152 {x + 7} 176Z')


ITEMS['sea-grass'] = (
    weed(60, 54, '#7cc4a0') + weed(96, 34, '#9ccf7a', 12) + weed(132, 64, '#7cc4a0', 9) + weed(160, 96, '#9ccf7a', 7)
    + z('ellipse', '#b9a99c', cx=82, cy=174, rx=30, ry=12) + z('ellipse', '#c9d3db', cx=140, cy=176, rx=24, ry=9)
    + s('path', d='M24 184 L176 184', stroke_width=2.5)
    + s('circle', '#ffffff', cx=124, cy=44, r=7, stroke_width=2.5) + s('circle', '#ffffff', cx=138, cy=28, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=118, cy=24, r=4, stroke_width=2.5) + s('circle', '#ffffff', cx=40, cy=92, r=6, stroke_width=2.5)
    + s('circle', '#ffffff', cx=34, cy=70, r=4, stroke_width=2.5)
    + s('circle', '#ffffff', cx=150, cy=74, r=5, stroke_width=2.5))

# 17. weather-umbrella-sun
ITEMS['weather-umbrella-sun'] = (
    rays(66, 66, 34, 52, 10, 6)
    + z('circle', '#ffe27a', cx=66, cy=66, r=30)
    + dot(56, 62, 3) + dot(76, 62, 3) + cheeks(48, 84, 72, 5, 3) + s('path', d='M62 74 Q66 78 70 74', stroke_width=2.5)
    + tube('M128 98 L128 168 Q128 180 116 180 Q106 180 106 170', '#9a6a3f', 4)
    + z('path', '#e8735a', d='M74 108 Q76 66 128 64 Q180 66 182 108 Q168 98 155 108 Q142 98 128 108 Q114 98 101 108 Q88 98 74 108Z')
    + s('path', d='M128 64 Q114 80 101 108 M128 64 Q142 80 155 108', stroke_width=2.5)
    + z('rect', '#9a6a3f', x=125, y=54, width=6, height=12, rx=2)
    + z('path', '#8fc7e8', d=drop(70, 132, 16)) + z('path', '#8fc7e8', d=drop(86, 158, 14))
    + z('path', '#8fc7e8', d=drop(52, 160, 14)))

# 18 / 19. thermometers


def thermo(level, col):
    top = 30
    return (z('rect', '#ffffff', x=84, y=top, width=32, height=128, rx=16)
            + s('rect', col, x=93, y=level, width=14, height=150 - level, rx=7, stroke='none')
            + z('circle', col, cx=100, cy=160, r=24)
            + s('path', d='M116 58 L124 58 M116 78 L124 78 M116 98 L124 98 M116 118 L124 118', stroke_width=2.5)
            + s('rect', x=84, y=top, width=32, height=110, rx=16)
            + dot(92, 158, 3) + dot(108, 158, 3) + cheeks(86, 114, 166, 4.5, 2.6))


ITEMS['thermometer-hot'] = (
    rays(150, 58, 26, 40, 10, 5)
    + z('circle', '#ffe27a', cx=150, cy=58, r=22)
    + thermo(46, '#e04b5a')
    + s('path', '#c0504d', d='M93 165 Q100 176 107 165Z', stroke_width=2)
    + z('path', '#8fc7e8', d=drop(64, 80, 14)) + z('path', '#8fc7e8', d=drop(54, 110, 12))
    + s('path', d='M44 150 Q52 142 44 134 Q36 126 44 118 M152 150 Q160 142 152 134 Q144 126 152 118', stroke='#e8735a', stroke_width=3))


def snowflake(cx, cy, R):
    o = ''
    for i in range(6):
        a = math.radians(i * 60)
        ca, sa = math.cos(a), math.sin(a)
        ex, ey = cx + R * ca, cy + R * sa
        mx, my = cx + R * 0.6 * ca, cy + R * 0.6 * sa
        b = math.radians(i * 60 + 35)
        c = math.radians(i * 60 - 35)
        o += (f'M{cx} {cy} L{_r(ex)} {_r(ey)} M{_r(mx)} {_r(my)} L{_r(mx + R * 0.32 * math.cos(b))} {_r(my + R * 0.32 * math.sin(b))} '
              f'M{_r(mx)} {_r(my)} L{_r(mx + R * 0.32 * math.cos(c))} {_r(my + R * 0.32 * math.sin(c))} ')
    return s('path', d=o, stroke_width=7) + s('path', d=o, stroke='#8fc7e8', stroke_width=3)


ITEMS['thermometer-cold'] = (
    snowflake(150, 60, 26)
    + thermo(124, '#8fb3e0')
    + s('path', d='M93 168 L97 166 L100 169 L103 166 L107 168', stroke_width=2)
    + s('path', d='M50 70 Q56 80 50 90 M62 104 Q68 114 62 124', stroke='#8fc7e8', stroke_width=3)
    + snowflake(52, 140, 12) + sparkle(160, 120, 0.9, '#ffffff'))

# 20. wildflowers
ITEMS['wildflowers'] = (
    tube('M100 150 L70 60 M100 150 L100 44 M100 150 L132 58 M100 150 L56 96 M100 150 L148 92', '#7cc4a0', 3)
    + z('path', '#9ccf7a', d='M88 116 Q64 104 60 118 Q72 128 88 122Z') + z('path', '#9ccf7a', d='M112 112 Q136 98 142 112 Q128 124 112 118Z')
    + flower(70, 60, 24, '#f6a6b8', '#ffc94d', 5)
    + flower(132, 58, 22, '#8fb3e0', '#ffe27a', 6)
    + flower(100, 42, 20, '#ffffff', '#ffc94d', 8, 8)
    + flower(56, 96, 18, '#ffe27a', '#e8735a', 5)
    + flower(148, 92, 18, '#a98bd0', '#ffe27a', 5)
    + z('path', '#f6e0c4', d='M60 120 L140 120 L112 186 L88 186Z')
    + s('path', d='M74 124 L94 184 M126 124 L106 184', stroke_width=2)
    + z('path', '#e8735a', d='M100 150 Q78 136 76 150 Q80 160 100 154Z') + z('path', '#e8735a', d='M100 150 Q122 136 124 150 Q120 160 100 154Z')
    + z('circle', '#e8735a', cx=100, cy=152, r=5))
