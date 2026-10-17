from math import sqrt, sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SKIN = '#ffd9b8'


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def limb(d, color=SKIN, w=13):
    return thick(d, color, w, w - 6)


def hand(x, y, r=7, c=SKIN):
    return s('circle', c, cx=x, cy=y, r=r)


def taper(x1, y1, x2, y2, r1, r2):
    dx, dy = x2 - x1, y2 - y1
    L = sqrt(dx * dx + dy * dy)
    nx, ny = -dy / L, dx / L
    f = lambda v: f'{v:.1f}'
    return (f'M{f(x1+nx*r1)} {f(y1+ny*r1)} L{f(x2+nx*r2)} {f(y2+ny*r2)} '
            f'A{r2} {r2} 0 0 0 {f(x2-nx*r2)} {f(y2-ny*r2)} L{f(x1-nx*r1)} {f(y1-ny*r1)} '
            f'A{r1} {r1} 0 0 0 {f(x1+nx*r1)} {f(y1+ny*r1)}Z')


def head(cx, cy, r, skin, hair, mouth='smile', eyes='dot', flip=False):
    """face() と同じ描き方で半径を変えられる頭（flip=True で逆さま）"""
    k = r / 34
    sg = -1 if flip else 1
    P = lambda dx, dy: f'{cx + dx * k:.1f} {cy + sg * dy * k:.1f}'
    o = z('circle', skin, cx=cx, cy=cy, r=r)
    if hair:
        o += s('path', hair, d=f'M{P(-34,-2)} Q{P(-32,-36)} {P(0,-35)} Q{P(32,-36)} {P(34,-2)} '
                              f'Q{P(20,-18)} {P(0,-17)} Q{P(-20,-18)} {P(-34,-2)}Z')
    ey = cy + sg * 2 * k
    if eyes == 'closed':
        for ex in (cx - 12 * k, cx + 12 * k):
            o += s('path', d=f'M{ex-5:.1f} {ey:.1f} Q{ex:.1f} {ey+5*sg:.1f} {ex+5:.1f} {ey:.1f}', stroke_width=2.5)
    elif eyes == 'dot':
        o += dot(cx - 12 * k, ey, 3.5 * max(k, 0.8)) + dot(cx + 12 * k, ey, 3.5 * max(k, 0.8))
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + sg * 13 * k, 7 * k, 4 * k)
    my = cy + sg * 16 * k
    if mouth == 'smile':
        o += s('path', d=f'M{cx-6*k:.1f} {my:.1f} Q{cx:.1f} {my+5*k*sg:.1f} {cx+6*k:.1f} {my:.1f}', stroke_width=2.5)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{cx-7*k:.1f} {my-2*k*sg:.1f} Q{cx:.1f} {my+11*k*sg:.1f} {cx+7*k:.1f} {my-2*k*sg:.1f}Z', stroke_width=2.5)
    elif mouth == 'line':
        o += s('path', d=f'M{cx-6*k:.1f} {my+1:.1f} L{cx+6*k:.1f} {my+1:.1f}', stroke_width=2.5)
    else:
        o += f'<circle cx="{cx:.1f}" cy="{my+2*k*sg:.1f}" r="{3.5*k:.1f}" fill="#c0504d" stroke-width="2.5"/>'
    return o


def puff(cx, cy, r=8, c='#ffffff'):
    return s('circle', c, cx=cx, cy=cy, r=r, stroke_width=2.5)


def speed(lines, w=2.5):
    return ''.join(s('path', d=f'M{a} {b} L{c} {d}', stroke_width=w) for a, b, c, d in lines)


# 1. baseball
ITEMS['baseball'] = (
    z('path', '#d9a66b', d=taper(40, 172, 124, 60, 6, 15))
    + thick('M44 166 L58 148', '#5b6b7a', 14, 8)
    + z('circle', '#d9a66b', cx=38, cy=175, r=8)
    + z('circle', '#ffffff', cx=140, cy=138, r=32)
    + s('path', d='M118 114 Q132 138 118 162', stroke='#e04b5a', stroke_width=2.5)
    + s('path', d='M162 114 Q148 138 162 162', stroke='#e04b5a', stroke_width=2.5)
    + ''.join(s('path', d=f'M{x-4} {y} L{x+4} {y-1}', stroke='#e04b5a', stroke_width=2) for x, y in ((123, 124), (127, 138), (123, 152)))
    + ''.join(s('path', d=f'M{x-4} {y-1} L{x+4} {y}', stroke='#e04b5a', stroke_width=2) for x, y in ((157, 124), (153, 138), (157, 152)))
    + dot(133, 138, 3) + dot(147, 138, 3) + cheeks(128, 152, 147, 5, 3)
    + s('path', d='M136 148 Q140 152 144 148', stroke_width=2.5)
)

# 2. volleyball
def _vb(cx=100, cy=100, R=64):
    def seam(a):
        ar = a * pi / 180; ac = (a + 50) * pi / 180
        return ((cx + R * cos(ar), cy + R * sin(ar)), (cx + R * 0.6 * cos(ac), cy + R * 0.6 * sin(ac)))
    def panel(a1, a2, col):
        (e1, c1), (e2, c2) = seam(a1), seam(a2)
        return s('path', col, d=f'M{cx} {cy} Q{c1[0]:.1f} {c1[1]:.1f} {e1[0]:.1f} {e1[1]:.1f} '
                                 f'A{R} {R} 0 0 1 {e2[0]:.1f} {e2[1]:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {cx} {cy}Z')
    o = z('circle', '#ffffff', cx=cx, cy=cy, r=R)
    o += panel(-90, 30, '#8fc7e8') + panel(150, 270, '#ffe27a') + panel(30, 150, '#ffffff')
    return o + s('circle', cx=cx, cy=cy, r=R)


ITEMS['volleyball'] = _vb()

# 3. american football
def _af():
    ux, uy = 0.79, -0.62; px, py = 0.62, 0.79
    o = z('path', '#9a6a3f', d='M36 150 Q48 34 164 50 Q152 166 36 150Z')
    o += thick(f'M{100-ux*26:.1f} {100-uy*26:.1f} L{100+ux*26:.1f} {100+uy*26:.1f}', '#ffffff', 8, 3.5)
    for t in (-18, -6, 6, 18):
        x, y = 100 + ux * t, 100 + uy * t
        o += thick(f'M{x-px*8:.1f} {y-py*8:.1f} L{x+px*8:.1f} {y+py*8:.1f}', '#ffffff', 7, 3)
    for t, k in ((-50, 13), (50, 13)):
        x, y = 100 + ux * t, 100 + uy * t
        o += thick(f'M{x-px*k:.1f} {y-py*k:.1f} Q{x+ux*(-4 if t<0 else 4):.1f} {y+uy*(-4 if t<0 else 4):.1f} {x+px*k:.1f} {y+py*k:.1f}', '#ffffff', 10, 5)
    return o


ITEMS['american-football'] = _af()

# 4. rugby
ITEMS['rugby'] = (
    z('ellipse', '#f4f4f0', cx=100, cy=102, rx=74, ry=46, transform='rotate(-25 100 102)')
    + '<g transform="rotate(-25 100 102)">'
    + thick('M60 64 Q52 102 60 140', '#e8735a', 14, 8)
    + thick('M140 64 Q148 102 140 140', '#e8735a', 14, 8)
    + s('path', d='M28 102 Q100 74 172 102', stroke_width=2.5)
    + s('path', d='M76 92 L124 92', stroke_width=3)
    + ''.join(s('path', d=f'M{x} 86 L{x} 98', stroke_width=2.5) for x in (84, 94, 104, 114))
    + dot(88, 114, 3) + dot(112, 114, 3) + cheeks(80, 120, 122, 5, 3)
    + s('path', d='M96 122 Q100 126 104 122', stroke_width=2.5)
    + '</g>'
)

# 5. golf
ITEMS['golf'] = (
    z('ellipse', '#9ccf7a', cx=100, cy=166, rx=82, ry=16)
    + s('ellipse', OUT, cx=150, cy=164, rx=9, ry=3)
    + s('path', d='M150 162 L150 60', stroke_width=3)
    + z('path', '#e04b5a', d='M150 60 L180 72 L150 84Z')
    + thick('M48 34 L98 150', '#c9d3db', 8, 3.5)
    + thick('M48 34 L58 58', '#5b6b7a', 14, 8)
    + z('path', '#5b6b7a', d='M92 146 L104 144 Q124 150 124 160 Q122 168 110 168 L92 164 Q86 154 92 146Z')
    + z('path', '#f5d58a', d='M56 158 L72 158 L66 166 L65 176 L63 176 L62 166Z')
    + z('circle', '#ffffff', cx=64, cy=144, r=14)
    + ''.join(dot(x, y, 1.6, '#b9a99c') for x, y in ((58, 140), (66, 136), (70, 146), (60, 150), (66, 152)))
)

# 6. table tennis
ITEMS['table-tennis'] = (
    z('path', '#d9a66b', d=taper(108, 108, 146, 160, 10, 10))
    + s('path', d='M128 136 L140 152', stroke_width=2)
    + z('circle', '#e04b5a', cx=84, cy=84, r=50)
    + dot(72, 86) + dot(96, 86) + cheeks(64, 104, 98, 7, 4)
    + s('path', d='M78 100 Q84 106 90 100', stroke_width=2.5)
    + z('circle', '#f5b971', cx=154, cy=50, r=13)
    + speed(((150, 74, 132, 92), (164, 72, 152, 86), (172, 64, 166, 72)))
)

# 7. badminton
def _bm():
    cx, cy, a = 80, 78, -30
    o = thick('M100 112 L120 148', '#c9d3db', 8, 3.5)
    o += z('path', '#e8735a', d=taper(118, 144, 136, 174, 8, 8))
    o += z('ellipse', '#8fb3e0', cx=cx, cy=cy, rx=32, ry=42, transform=f'rotate({a} {cx} {cy})')
    o += f'<g transform="rotate({a} {cx} {cy})">'
    o += s('ellipse', '#ffffff', cx=cx, cy=cy, rx=24, ry=34)
    for x in range(-16, 17, 8):
        h = 34 * sqrt(1 - (x / 24) ** 2)
        o += s('path', d=f'M{cx+x} {cy-h:.1f} L{cx+x} {cy+h:.1f}', stroke='#b9a99c', stroke_width=1.5)
    for y in range(-24, 25, 8):
        w = 24 * sqrt(1 - (y / 34) ** 2)
        o += s('path', d=f'M{cx-w:.1f} {cy+y} L{cx+w:.1f} {cy+y}', stroke='#b9a99c', stroke_width=1.5)
    o += s('ellipse', cx=cx, cy=cy, rx=24, ry=34) + '</g>'
    T = 'rotate(40 150 66)'
    o += z('path', '#ffffff', d='M139 88 L128 46 Q150 38 172 46 L161 88Z', transform=T)
    o += f'<g transform="{T}">' + s('path', d='M144 88 L138 44 M150 88 L150 41 M156 88 L162 44', stroke_width=2) + '</g>'
    o += z('path', '#e8735a', d='M137 88 L163 88 L163 92 Q163 106 150 106 Q137 106 137 92Z', transform=T)
    o += speed(((128, 112, 140, 104), (134, 122, 146, 114)))
    return o


ITEMS['badminton'] = _bm()

# 8. swimming
ITEMS['swimming'] = (
    limb('M84 126 Q64 104 54 74', SKIN, 14) + hand(52, 68, 9)
    + head(114, 88, 34, SKIN, '#e8735a', 'o', eyes='none')
    + s('path', d='M80 84 L148 84', stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=102, cy=88, r=8, stroke_width=2.5) + s('circle', '#8fc7e8', cx=126, cy=88, r=8, stroke_width=2.5)
    + dot(102, 89, 3) + dot(126, 89, 3)
    + z('path', '#8fc7e8', d='M26 124 Q44 112 62 124 Q80 136 98 124 Q116 112 134 124 Q152 136 170 124 Q178 118 182 122 L182 162 Q182 176 166 176 L42 176 Q26 176 26 162Z')
    + s('path', d='M44 146 Q56 140 68 146 M110 156 Q122 150 134 156 M140 142 Q150 137 160 142', stroke='#ffffff', stroke_width=3)
    + puff(40, 112, 5, '#ffffff') + puff(30, 96, 4, '#ffffff') + puff(70, 108, 4, '#ffffff')
)

# 9. cycling race
def wheel(cx, cy, r=26):
    o = s('circle', cx=cx, cy=cy, r=r, stroke_width=6) + s('circle', cx=cx, cy=cy, r=r - 3, stroke='#c9d3db', stroke_width=1.5)
    for a in range(0, 180, 45):
        ar = a * pi / 180
        o += s('path', d=f'M{cx-(r-4)*cos(ar):.1f} {cy-(r-4)*sin(ar):.1f} L{cx+(r-4)*cos(ar):.1f} {cy+(r-4)*sin(ar):.1f}', stroke='#b9a99c', stroke_width=1.5)
    return o + dot(cx, cy, 3.5)


ITEMS['cycling-race'] = (
    speed(((24, 120, 40, 120), (20, 136, 32, 136), (26, 104, 38, 104)))
    + wheel(52, 152) + wheel(148, 152)
    + thick('M52 152 L84 124 L134 124 L148 152 M84 124 L96 152 L134 124 M96 152 L52 152', '#e04b5a', 9, 4.5)
    + thick('M134 124 L140 102 Q150 98 152 108', '#5b6b7a', 8, 3.5)
    + thick('M80 116 L92 116', '#5b6b7a', 8, 3.5)
    + limb('M88 116 Q112 124 100 152', '#2b2220', 13) + dot(102, 154, 5)
    + z('ellipse', '#8fc7e8', cx=104, cy=104, rx=28, ry=17, transform='rotate(-18 104 104)')
    + head(126, 70, 30, SKIN, '#5a4033', 'smile')
    + z('path', '#ffc94d', d='M96 66 Q96 36 126 36 Q154 38 160 62 Q130 52 96 66Z')
    + s('path', d='M114 42 L118 52 M130 40 L132 50 M144 44 L142 52', stroke_width=2)
    + limb('M128 102 L150 108', '#8fc7e8', 11) + hand(152, 108, 6)
)

# 10. skiing
ITEMS['skiing'] = (
    z('path', '#f4f4f0', d='M22 150 Q100 166 180 180 Q180 184 172 184 L30 184 Q22 184 22 176Z')
    + thick('M68 128 L46 176', '#b9a99c', 6, 2.5) + thick('M138 134 L156 182', '#b9a99c', 6, 2.5)
    + z('path', '#e8735a', d='M40 152 L164 176 Q174 178 172 170 L168 168 L44 146Z')
    + z('path', '#8fb3e0', d='M74 156 Q70 130 84 124 L120 128 Q134 136 128 162Z')
    + s('path', d='M86 160 L88 140 M114 162 L116 142', stroke_width=2.5)
    + z('ellipse', '#e8735a', cx=102, cy=118, rx=30, ry=22)
    + limb('M80 116 Q66 124 68 130', '#e8735a', 12) + hand(68, 130, 6, '#5b6b7a')
    + limb('M124 116 Q138 126 138 134', '#e8735a', 12) + hand(138, 134, 6, '#5b6b7a')
    + head(100, 72, 32, SKIN, '#e04b5a', 'open')
    + s('circle', '#ffffff', cx=100, cy=38, r=7)
    + s('path', d='M70 70 Q100 62 130 70', stroke='#ffffff', stroke_width=3)
    + puff(30, 150, 6) + puff(40, 140, 5) + puff(24, 136, 4)
)

# 11. snowboarding
ITEMS['snowboarding'] = (
    puff(40, 172, 8) + puff(54, 178, 6) + puff(28, 160, 5)
    + limb('M86 130 L80 156', '#5b6b7a', 14) + limb('M114 130 L124 154', '#5b6b7a', 14)
    + z('path', '#a98bd0', d='M44 166 Q42 154 56 154 L150 146 Q164 146 164 156 Q164 166 150 166 L58 172 Q44 174 44 166Z')
    + s('path', d='M70 158 L140 152', stroke='#ffffff', stroke_width=3)
    + limb('M80 108 Q60 98 40 104', '#f5b971', 13) + hand(36, 104, 7, '#7cc4b0')
    + limb('M120 108 Q142 98 160 90', '#f5b971', 13) + hand(164, 88, 7, '#7cc4b0')
    + z('path', '#f5b971', d='M74 134 Q72 98 100 96 Q128 98 126 134Z')
    + head(100, 64, 32, SKIN, '#7cc4b0', 'open')
    + s('circle', '#7cc4b0', cx=100, cy=30, r=6)
)

# 12. ice skating
ITEMS['ice-skating'] = (
    z('ellipse', '#c9d3db', cx=100, cy=176, rx=80, ry=12)
    + s('path', d='M42 174 Q70 168 96 172', stroke='#ffffff', stroke_width=3)
    + limb('M96 134 L94 162', SKIN, 12)
    + limb('M108 132 Q138 132 160 116', SKIN, 12)
    + z('path', '#ffffff', d='M86 160 L100 160 L102 168 L84 168Z') + s('path', d='M82 172 L104 172', stroke_width=3)
    + z('path', '#ffffff', d='M156 108 L168 104 L171 116 L159 120Z') + s('path', d='M157 126 L175 120', stroke_width=3)
    + z('path', '#f6a6b8', d='M100 92 Q84 100 82 116 L72 140 Q100 148 128 136 L116 114 Q114 98 100 92Z')
    + limb('M88 102 Q66 98 48 82', SKIN, 11) + limb('M112 102 Q136 96 150 84', SKIN, 11)
    + z('circle', '#c9a36b', cx=110, cy=30, r=11)
    + head(100, 62, 30, SKIN, '#c9a36b', 'smile')
    + s('path', '#f6a6b8', d='M88 136 L112 138', stroke_width=2.5)
)

# 13. surfing
ITEMS['surfing'] = (
    z('path', '#8fc7e8', d='M22 180 L22 90 Q30 40 76 40 Q104 42 106 66 Q96 54 82 58 Q62 66 70 96 Q80 140 182 156 L182 166 Q182 180 166 180 L38 180 Q22 180 22 166Z')
    + s('path', d='M76 40 Q104 42 106 66 Q96 54 82 58 Q66 64 68 84', stroke='#ffffff', stroke_width=6)
    + s('path', d='M76 40 Q104 42 106 66 Q96 54 82 58 Q66 64 68 84', stroke_width=2)
    + s('path', d='M34 150 Q44 144 54 150 M30 120 Q38 114 46 120', stroke='#ffffff', stroke_width=3)
    + limb('M114 140 L98 156', SKIN, 12) + limb('M134 140 L148 152', SKIN, 12)
    + z('path', '#ffe27a', d='M72 162 Q96 150 150 150 Q180 152 176 158 Q150 168 96 170 Q70 170 72 162Z')
    + s('path', d='M88 162 L168 156', stroke='#e8735a', stroke_width=3)
    + limb('M110 112 Q90 104 80 90', SKIN, 12) + hand(78, 86, 6)
    + limb('M140 114 Q158 110 170 98', SKIN, 12) + hand(172, 96, 6)
    + z('path', '#e8735a', d='M106 146 Q102 114 124 108 Q146 112 142 146Z')
    + head(124, 80, 30, SKIN, '#2b2220', 'open')
)

# 14. skateboarding
ITEMS['skateboarding'] = (
    speed(((24, 140, 44, 140), (28, 154, 42, 154)))
    + limb('M88 140 L80 158', '#5b6b7a', 14) + limb('M112 140 L124 156', '#5b6b7a', 14)
    + z('path', '#e8735a', d='M42 160 Q44 152 54 154 L150 160 Q166 156 166 150 Q172 152 168 162 Q164 172 150 170 L54 166 Q40 166 42 160Z', transform='rotate(-6 100 160)')
    + s('circle', '#f5d58a', cx=70, cy=176, r=7) + s('circle', '#f5d58a', cx=136, cy=168, r=7)
    + limb('M80 110 Q60 104 46 112', '#9ccf7a', 12) + hand(42, 114, 7)
    + limb('M120 110 Q140 102 156 106', '#9ccf7a', 12) + hand(160, 106, 7)
    + z('path', '#9ccf7a', d='M74 146 Q72 106 100 102 Q128 106 126 146Z')
    + head(100, 68, 32, SKIN, '#2b2220', 'smile')
    + z('path', '#e04b5a', d='M68 62 Q68 30 100 30 Q132 30 132 58 L152 60 Q152 66 132 66 Q100 54 68 62Z')
)

# 15. boxing gloves
def glove(cx, cy, flip=1, col='#e04b5a'):
    f = lambda x: cx + flip * x
    return (z('rect', '#ffffff', x=min(f(-22), f(22)), y=cy + 34, width=44, height=26, rx=6)
            + s('path', d=f'M{f(-22)} {cy+46} L{f(22)} {cy+46}', stroke_width=2.5)
            + z('path', col, d=f'M{f(-24)} {cy+36} Q{f(-34)} {cy-10} {f(-14)} {cy-34} Q{f(10)} {cy-50} {f(28)} {cy-26} '
                                f'Q{f(38)} {cy-6} {f(30)} {cy+12} Q{f(26)} {cy+36} {f(24)} {cy+36}Z')
            + z('path', col, d=f'M{f(-28)} {cy+20} Q{f(-48)} {cy+8} {f(-40)} {cy-10} Q{f(-30)} {cy-18} {f(-22)} {cy-4}Z')
            + s('path', d=f'M{f(-20)} {cy-2} Q{f(0)} {cy+8} {f(16)} {cy-4}', stroke_width=2.5))


ITEMS['boxing'] = (
    s('path', d='M74 136 Q100 160 128 140', stroke='#ffffff', stroke_width=7) + s('path', d='M74 136 Q100 160 128 140', stroke_width=2)
    + glove(68, 82, 1) + glove(134, 98, -1)
    + s('path', d='M74 136 Q90 152 100 152', stroke='#ffffff', stroke_width=4)
)

# 16. karate
ITEMS['karate'] = (
    limb('M88 150 L80 178', SKIN, 13) + z('ellipse', SKIN, cx=78, cy=180, rx=10, ry=5)
    + z('path', '#ffffff', d='M80 156 L76 132 L104 132 L100 158 Q90 160 80 156Z')
    + limb('M104 140 Q136 136 168 120', '#ffffff', 16) + z('ellipse', SKIN, cx=172, cy=118, rx=9, ry=7)
    + limb('M84 112 Q60 118 50 108', '#ffffff', 14) + hand(46, 106, 8)
    + z('path', '#ffffff', d='M70 140 Q70 104 96 100 Q124 104 122 140Z')
    + s('path', d='M86 104 L96 122 L106 104', stroke_width=2.5)
    + s('rect', OUT, x=70, y=128, width=52, height=8, rx=2)
    + s('path', d='M94 136 L88 150 M100 136 L104 150', stroke_width=5)
    + limb('M114 112 Q132 106 144 96', '#ffffff', 14) + hand(148, 94, 8)
    + head(96, 66, 32, SKIN, '#2b2220', 'open')
    + s('path', '#e04b5a', d='M64 56 Q96 46 128 56 L127 63 Q96 54 65 63Z', stroke_width=2.5)
    + s('path', d='M128 58 L142 52 M128 60 L140 64', stroke='#e04b5a', stroke_width=4)
)

# 17. judo
ITEMS['judo'] = (
    z('ellipse', '#d9a66b', cx=100, cy=180, rx=78, ry=8)
    + limb('M118 150 L110 176', SKIN, 13) + limb('M134 150 L146 176', SKIN, 13)
    + limb('M150 36 Q140 56 128 64', '#8fb3e0', 15) + limb('M168 44 Q158 62 140 68', '#8fb3e0', 15)
    + z('ellipse', '#8fb3e0', cx=100, cy=76, rx=36, ry=20, transform='rotate(-24 100 76)')
    + s('path', d='M118 66 L124 82', stroke=OUT, stroke_width=5)
    + head(56, 102, 24, SKIN, '#5a4033', 'o', flip=True)
    + z('path', '#ffffff', d='M104 158 Q98 118 126 112 Q152 116 150 158Z')
    + s('rect', OUT, x=104, y=146, width=46, height=7, rx=2)
    + limb('M114 120 Q100 108 92 90', '#ffffff', 13) + hand(90, 86, 7)
    + head(128, 104, 26, SKIN, '#2b2220', 'line')
    + speed(((40, 40, 56, 52), (30, 58, 44, 64)))
)

# 18. sumo
ITEMS['sumo'] = (
    z('ellipse', '#d9a66b', cx=100, cy=178, rx=82, ry=9)
    + limb('M48 150 L42 172', SKIN, 16) + limb('M74 154 L76 174', SKIN, 16)
    + limb('M126 154 L124 174', SKIN, 16) + limb('M152 150 L158 172', SKIN, 16)
    + z('ellipse', SKIN, cx=62, cy=124, rx=38, ry=36)
    + z('ellipse', SKIN, cx=138, cy=124, rx=38, ry=36)
    + z('path', '#5b6b7a', d='M26 134 Q62 144 98 132 L96 152 Q62 164 30 150Z')
    + z('path', '#8b6b4f', d='M102 132 Q138 144 174 134 L170 150 Q138 164 104 152Z')
    + limb('M80 104 L106 110', SKIN, 14) + limb('M120 112 L94 118', SKIN, 14)
    + head(62, 70, 26, SKIN, '#2b2220', 'line') + z('ellipse', '#2b2220', cx=60, cy=40, rx=9, ry=6)
    + head(138, 70, 26, SKIN, '#2b2220', 'line') + z('ellipse', '#2b2220', cx=140, cy=40, rx=9, ry=6)
)

# 19. kendo
ITEMS['kendo'] = (
    thick('M104 140 L172 34', '#f5d58a', 11, 5) + s('path', d='M150 68 L158 56', stroke_width=5)
    + z('path', '#5b6b7a', d='M66 182 L74 136 L126 136 L134 182Z')
    + s('path', d='M88 140 L84 182 M112 140 L116 182', stroke_width=2.5)
    + z('path', '#5b6b7a', d='M66 140 Q64 104 100 100 Q136 104 134 140Z')
    + z('path', '#8b6b4f', d='M72 112 Q100 96 128 112 L126 136 Q100 144 74 136Z')
    + s('path', d='M80 118 Q100 110 120 118 M78 128 Q100 120 122 128', stroke_width=2)
    + limb('M84 118 Q92 134 104 140', '#5b6b7a', 14) + limb('M118 116 Q120 130 110 140', '#5b6b7a', 14)
    + z('circle', '#e8735a', cx=106, cy=138, r=9)
    + z('path', '#5b6b7a', d='M60 96 Q56 34 100 30 Q144 34 140 96 L152 112 L124 106 L76 106 L48 112Z')
    + z('ellipse', SKIN, cx=100, cy=72, rx=28, ry=28)
    + dot(89, 72) + dot(111, 72) + cheeks(82, 118, 82, 6, 3.5)
    + s('path', d='M95 86 Q100 90 105 86', stroke_width=2.5)
    + s('path', d='M100 42 L100 102', stroke='#c9d3db', stroke_width=3)
    + ''.join(s('path', d=f'M{100-w} {y} L{100+w} {y}', stroke='#c9d3db', stroke_width=2.5) for y, w in ((52, 22), (62, 27), (72, 28), (82, 27), (92, 22)))
    + s('ellipse', cx=100, cy=72, rx=28, ry=28)
)

# 20. yoga
ITEMS['yoga'] = (
    z('rect', '#a98bd0', x=26, y=168, width=148, height=12, rx=6)
    + z('path', '#7cc4b0', d='M36 166 Q38 144 72 142 L128 142 Q162 144 164 166Z')
    + s('path', d='M70 156 Q100 146 130 156', stroke_width=2.5)
    + z('path', '#7cc4b0', d='M72 150 Q70 104 100 100 Q130 104 128 150Z')
    + limb('M78 112 Q62 130 60 150', SKIN, 12) + limb('M122 112 Q138 130 140 150', SKIN, 12)
    + hand(58, 152, 7) + hand(142, 152, 7)
    + head(100, 66, 32, SKIN, '#5a4033', 'smile', eyes='closed')
    + z('circle', '#5a4033', cx=100, cy=32, r=10)
    + s('path', d='M44 70 Q38 62 44 54 M156 70 Q162 62 156 54', stroke='#9ccf7a', stroke_width=3)
)
