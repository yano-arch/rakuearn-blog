import math
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def tube(d, color, w=8):
    """outlined thick line (outline + inner color)"""
    return s('path', d=d, stroke_width=w + 5) + s('path', d=d, stroke=color, stroke_width=w)


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def mini_face(cx, cy, sc=1.0, mouth='smile'):
    o = dot(cx - 7 * sc, cy, 3 * sc) + dot(cx + 7 * sc, cy, 3 * sc) + cheeks(cx - 13 * sc, cx + 13 * sc, cy + 7 * sc, 4.5 * sc, 2.8 * sc)
    if mouth == 'smile':
        o += s('path', d=f'M{cx-4*sc} {cy+7*sc} Q{cx} {cy+11*sc} {cx+4*sc} {cy+7*sc}', stroke_width=2.5)
    else:
        o += s('path', d=f'M{cx-5*sc} {cy+8*sc} L{cx+5*sc} {cy+8*sc}', stroke_width=2.5)
    return o


def germ(cx, cy, r, col, n=8, rot=0):
    o = ''
    for i in range(n):
        a = math.radians(rot + i * 360 / n)
        x, y = cx + (r + 6) * math.cos(a), cy + (r + 6) * math.sin(a)
        o += s('path', d=f'M{cx + r*math.cos(a):.1f} {cy + r*math.sin(a):.1f} L{x:.1f} {y:.1f}', stroke_width=3)
        o += z('circle', col, cx=f'{x:.1f}', cy=f'{y:.1f}', r=f'{r*0.16+2:.1f}')
    o += z('circle', col, cx=cx, cy=cy, r=r)
    return o


# 1. no smoking
ITEMS['no-smoking'] = (
    z('circle', '#e04b5a', cx=100, cy=104, r=72)
    + s('circle', '#ffffff', cx=100, cy=104, r=58)
    + z('rect', '#ffffff', x=46, y=108, width=82, height=18, rx=3)
    + z('rect', '#f5b971', x=128, y=108, width=26, height=18, rx=3)
    + s('path', d='M54 98 Q46 86 56 76 Q66 66 58 54', stroke='#b9a99c', stroke_width=4)
    + '<g transform="rotate(45 100 104)">' + z('rect', '#e04b5a', x=34, y=96, width=132, height=16, rx=2) + '</g>'
)

# 2. germs
ITEMS['germs'] = (
    germ(72, 74, 26, '#9ccf7a', 8, 10) + mini_face(72, 72)
    + germ(140, 92, 22, '#a98bd0', 7, 0) + mini_face(140, 90, 0.9, 'flat')
    + germ(96, 144, 28, '#f5d58a', 9, 20) + mini_face(96, 142, 1.1)
    + s('circle', '#7cc4a0', cx=152, cy=148, r=6, stroke_width=2.5)
    + s('circle', '#7cc4a0', cx=40, cy=134, r=5, stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=152, cy=40, r=5, stroke_width=2.5)
)

# 3. immune shield
SH = 'M56 50 Q100 30 144 50 L144 98 Q144 148 100 176 Q56 148 56 98Z'
ITEMS['immune-shield'] = (
    z('path', '#8fb3e0', d=SH)
    + s('path', d='M68 58 Q100 44 132 58 L132 98 Q132 138 100 162 Q68 138 68 98Z', stroke='#ffffff', stroke_width=3)
    + z('path', '#f07a8a', d='M100 128 C86 116 76 106 82 94 C88 84 100 88 100 98 C100 88 112 84 118 94 C124 106 114 116 100 128Z')
    + dot(88, 76, 3.5) + dot(112, 76, 3.5) + cheeks(78, 122, 84, 5, 3) + s('path', d='M95 84 Q100 89 105 84', stroke_width=2.5)
    + germ(30, 68, 11, '#9ccf7a', 6) + mini_face(30, 66, 0.6, 'flat')
    + germ(172, 132, 11, '#a98bd0', 6, 15) + mini_face(172, 130, 0.6, 'flat')
    + s('path', d='M42 86 L50 94 M46 76 L52 78', stroke_width=2.5)
    + s('path', d='M158 116 L152 108 M156 126 L150 124', stroke_width=2.5)
)

# 4. doctor and patient
ITEMS['doctor-patient'] = (
    body('#ffffff', cx=60, top=126, bottom=186)
    + s('path', '#8fc7e8', d='M50 128 L60 144 L70 128Z', stroke_width=2.5)
    + s('path', d='M44 128 Q42 150 54 156 M76 128 Q78 150 66 156 M54 156 Q60 160 66 156', stroke='#5b6b7a', stroke_width=3.5)
    + z('circle', '#c9d3db', cx=60, cy=164, r=6)
    + face(60, 88, SK, '#2b2220', 'smile')
    + z('rect', '#d9a66b', x=82, y=140, width=26, height=34, rx=3)
    + s('rect', '#ffffff', x=86, y=146, width=18, height=24, rx=2, stroke_width=2)
    + s('path', d='M90 154 L100 154 M90 162 L100 162', stroke_width=2)
    + z('circle', SK, cx=88, cy=162, r=7)
    + body('#f6a6b8', cx=144, top=136, bottom=186)
    + face(144, 98, SK, '#c9a36b', 'open')
    + z('circle', SK, cx=120, cy=160, r=7)
    + z('path', '#ffffff', d='M104 30 Q104 22 112 22 L144 22 Q152 22 152 30 L152 44 Q152 52 144 52 L124 52 L114 60 L116 52 L112 52 Q104 52 104 44Z')
    + z('path', '#f07a8a', d='M128 45 C122 40 118 36 121 32 C124 28 128 30 128 33 C128 30 132 28 135 32 C138 36 134 40 128 45Z')
)

# 5. hospital bed
ITEMS['hospital-bed'] = (
    s('path', d='M168 34 L168 128 M154 34 L182 34', stroke='#5b6b7a', stroke_width=4)
    + z('path', '#ffe27a', d='M160 40 L176 40 L176 66 Q168 74 160 66Z')
    + s('path', d='M168 72 Q166 90 150 100', stroke='#8fc7e8', stroke_width=2.5)
    + z('rect', '#8fb3e0', x=26, y=72, width=14, height=98, rx=4)
    + z('rect', '#f4f4f0', x=34, y=116, width=130, height=18, rx=4)
    + z('ellipse', '#ffffff', cx=62, cy=108, rx=24, ry=12)
    + z('circle', SK, cx=66, cy=94, r=19)
    + s('path', '#5a4033', d='M47 92 Q48 74 66 75 Q84 76 85 90 Q72 82 60 84 Q52 86 47 92Z')
    + s('path', d='M57 98 Q60 101 63 98 M71 98 Q74 101 77 98', stroke_width=2.5)
    + cheeks(55, 79, 104, 4, 2.5)
    + z('path', '#8fc7e8', d='M80 118 Q82 98 104 98 L150 98 Q164 100 166 118Z')
    + s('path', d='M84 106 L162 106', stroke='#ffffff', stroke_width=3)
    + z('rect', '#c9d3db', x=30, y=134, width=144, height=10, rx=3)
    + z('rect', '#8fb3e0', x=164, y=100, width=12, height=70, rx=4)
    + s('path', d='M48 144 L48 166 M156 144 L156 166', stroke_width=4)
    + z('circle', '#5b6b7a', cx=48, cy=172, r=7) + z('circle', '#5b6b7a', cx=156, cy=172, r=7)
    + s('path', d='M122 72 L130 72 L122 82 L130 82 M136 58 L142 58 L136 66 L142 66', stroke_width=2.5)
)

# 6. pharmacy counter
def bottle(x, y, col, cap='#ffffff'):
    return z('rect', col, x=x, y=y + 8, width=14, height=18, rx=3) + z('rect', cap, x=x + 2, y=y + 2, width=10, height=7, rx=2)


ITEMS['pharmacy'] = (
    z('rect', '#d9a66b', x=24, y=36, width=40, height=96, rx=3)
    + s('path', d='M24 66 L64 66 M24 98 L64 98', stroke_width=3)
    + bottle(28, 38, '#e8735a') + bottle(46, 38, '#8fc7e8') + bottle(28, 70, '#9ccf7a') + bottle(46, 70, '#f5d58a') + bottle(36, 102, '#a98bd0')
    + z('rect', '#d9a66b', x=136, y=36, width=40, height=96, rx=3)
    + s('path', d='M136 66 L176 66 M136 98 L176 98', stroke_width=3)
    + bottle(140, 38, '#f6a6b8') + bottle(158, 38, '#7cc4b0') + bottle(140, 70, '#8fb3e0') + bottle(158, 70, '#e8735a') + bottle(150, 102, '#9ccf7a')
    + body('#ffffff', cx=100, top=112, bottom=150)
    + s('path', '#8fc7e8', d='M90 114 L100 128 L110 114Z', stroke_width=2.5)
    + face(100, 76, SK, '#5a4033', 'smile')
    + z('rect', '#7cc4b0', x=24, y=134, width=152, height=48, rx=3)
    + s('rect', '#f4f4f0', x=20, y=128, width=160, height=10, rx=3)
    + s('path', d='M24 138 L176 138', stroke_width=3)
    + z('rect', '#f5d58a', x=60, y=110, width=24, height=20, rx=3)
    + z('rect', '#ffffff', x=114, y=106, width=20, height=24, rx=3) + s('rect', '#e8735a', x=116, y=100, width=16, height=8, rx=2, stroke_width=2.5)
    + z('circle', SK, cx=88, cy=122, r=7)
)

# 7. medical chart
ITEMS['medical-chart'] = (
    z('rect', '#d9a66b', x=44, y=34, width=104, height=146, rx=8)
    + s('rect', '#ffffff', x=54, y=50, width=84, height=120, rx=3)
    + z('rect', '#c9d3db', x=76, y=26, width=40, height=18, rx=4)
    + s('circle', cx=96, cy=34, r=4, stroke_width=2.5)
    + s('path', d='M62 82 L76 82 L82 68 L90 98 L98 74 L104 82 L130 82', stroke='#e8735a', stroke_width=3)
    + s('rect', '#9ccf7a', x=62, y=108, width=10, height=10, rx=2, stroke_width=2)
    + s('rect', '#9ccf7a', x=62, y=126, width=10, height=10, rx=2, stroke_width=2)
    + s('rect', '#ffffff', x=62, y=144, width=10, height=10, rx=2, stroke_width=2)
    + s('path', d='M80 113 L126 113 M80 131 L120 131 M80 149 L114 149', stroke='#b9a99c', stroke_width=3)
    + s('path', d='M63 112 L66 116 L71 109 M63 130 L66 134 L71 127', stroke_width=2)
    + '<g transform="rotate(30 160 120)">' + z('rect', '#8fb3e0', x=154, y=74, width=12, height=70, rx=3)
    + z('path', '#f6e0c4', d='M154 144 L166 144 L160 160Z') + '</g>'
)

# 8. blood donation bag
ITEMS['blood-donation'] = (
    z('rect', '#f4f4f0', x=58, y=48, width=84, height=108, rx=14)
    + s('rect', '#f4f4f0', x=88, y=38, width=24, height=14, rx=5)
    + s('path', '#f07a8a', d='M60 86 L140 86 L140 142 Q140 154 128 154 L72 154 Q60 154 60 142Z', stroke='none')
    + s('rect', x=58, y=48, width=84, height=108, rx=14)
    + s('path', d='M60 86 L140 86', stroke_width=2.5)
    + s('path', d='M70 60 L70 76 M78 60 L78 70', stroke='#c9d3db', stroke_width=3)
    + dot(88, 112) + dot(112, 112) + cheeks(78, 122, 122, 5, 3) + s('path', d='M94 122 Q100 127 106 122', stroke_width=2.5)
    + s('path', d='M100 156 L100 166 Q100 180 120 178 L150 176', stroke_width=7)
    + s('path', d='M100 156 L100 166 Q100 180 120 178 L150 176', stroke='#f07a8a', stroke_width=3)
    + z('path', '#f07a8a', d='M164 70 C154 62 148 56 152 48 C156 42 164 44 164 50 C164 44 172 42 176 48 C180 56 174 62 164 70Z')
    + z('path', '#f6a6b8', d='M36 116 C30 111 26 107 29 102 C32 98 36 100 36 104 C36 100 40 98 43 102 C46 107 42 111 36 116Z')
)

# 9. checkup (height measurement)
ITEMS['checkup'] = (
    z('rect', '#d9a66b', x=136, y=30, width=12, height=146, rx=3)
    + ''.join(s('path', d=f'M136 {y} L{144 if (y // 12) % 2 else 140} {y}', stroke_width=2) for y in range(48, 170, 12))
    + z('rect', '#c9d3db', x=40, y=168, width=124, height=12, rx=4)
    + z('rect', '#7cc4b0', x=84, y=148, width=12, height=22, rx=4) + z('rect', '#7cc4b0', x=104, y=148, width=12, height=22, rx=4)
    + body('#8fc7e8', cx=100, top=112, bottom=156)
    + z('circle', SK, cx=64, cy=144, r=7) + z('circle', SK, cx=136, cy=144, r=7)
    + face(100, 76, SK, '#2b2220', 'smile')
    + z('rect', '#8fb3e0', x=78, y=34, width=74, height=8, rx=3)
    + s('path', d='M40 56 L48 62 M36 76 L46 76 M40 96 L48 90', stroke_width=2.5)
)

# 10. walking support
ITEMS['walking-support'] = (
    body('#7cc4b0', cx=140, top=124, bottom=184)
    + face(140, 86, SK, '#5a4033', 'smile')
    + body('#a98bd0', cx=68, top=134, bottom=184)
    + s('path', d='M36 118 Q36 106 44 106 Q52 106 52 114 L46 182', stroke='#8b6b4f', stroke_width=5)
    + z('circle', SK, cx=46, cy=150, r=7)
    + face(68, 96, SK, '#e8e1d8', 'smile')
    + z('circle', SK, cx=104, cy=150, r=8) + z('circle', SK, cx=112, cy=160, r=8)
)

# 11. rehabilitation (parallel bars)
ITEMS['rehabilitation'] = (
    s('path', d='M24 182 L176 182', stroke_width=2.5)
    + tube('M34 126 L34 180 M166 126 L166 180', '#c9d3db', 6)
    + z('rect', '#7cc4b0', x=88, y=148, width=11, height=32, rx=4) + z('rect', '#7cc4b0', x=104, y=150, width=11, height=26, rx=4)
    + z('ellipse', '#5b6b7a', cx=92, cy=180, rx=9, ry=5) + z('ellipse', '#5b6b7a', cx=112, cy=176, rx=9, ry=5)
    + body('#8fc7e8', cx=100, top=110, bottom=156)
    + tube('M26 122 L174 122', '#ffc94d', 6)
    + z('circle', SK, cx=60, cy=120, r=8) + z('circle', SK, cx=140, cy=120, r=8)
    + face(100, 74, SK, '#2b2220', 'smile')
    + s('path', d='M150 42 L156 30 M162 52 L174 46', stroke_width=2.5)
)

# 12. massage
ITEMS['massage'] = (
    body('#7cc4b0', cx=134, top=88, bottom=130)
    + face(134, 58, SK, '#2b2220', 'smile')
    + z('rect', '#d9a66b', x=22, y=128, width=160, height=12, rx=4)
    + s('path', d='M36 140 L36 178 M168 140 L168 178', stroke_width=5)
    + z('path', '#f4f4f0', d='M64 128 Q62 100 90 98 L160 98 Q182 100 182 128Z')
    + z('ellipse', '#ffffff', cx=44, cy=122, rx=20, ry=7)
    + z('circle', SK, cx=46, cy=104, r=20)
    + s('path', '#5a4033', d='M28 98 Q32 82 50 84 Q64 88 64 100 Q54 92 44 92 Q34 94 28 98Z')
    + s('path', d='M38 108 Q42 111 46 108', stroke_width=2.5) + cheeks(34, 58, 114, 4, 2.5)
    + z('circle', SK, cx=114, cy=98, r=8) + z('circle', SK, cx=150, cy=98, r=8)
    + s('path', d='M98 82 L104 76 M166 82 L172 76', stroke_width=2.5)
    + s('path', '#f6a6b8', d='M30 66 C25 62 22 58 25 54 C28 51 30 53 30 56 C30 53 32 51 35 54 C38 58 35 62 30 66Z', stroke_width=2)
    + s('path', '#f6a6b8', d='M74 52 C69 48 66 44 69 40 C72 37 74 39 74 42 C74 39 76 37 79 40 C82 44 79 48 74 52Z', stroke_width=2)
)


# 13. DNA helix
def helix():
    o = ''
    cols = ['#e8735a', '#7cc4b0', '#ffc94d', '#8fb3e0']
    pts1, pts2 = [], []
    for i in range(0, 61):
        y = 30 + i * 145 / 60
        t = (y - 30) / 145 * 2 * math.pi * 1.5
        pts1.append((100 + 38 * math.sin(t), y)); pts2.append((100 - 38 * math.sin(t), y))
    for k in range(1, 60, 4):
        (x1, y), (x2, _) = pts1[k], pts2[k]
        if abs(x1 - x2) > 10:
            o += s('path', d=f'M{x1:.1f} {y:.1f} L{x2:.1f} {y:.1f}', stroke_width=10)
            o += s('path', d=f'M{x1:.1f} {y:.1f} L{x2:.1f} {y:.1f}', stroke=cols[(k // 4) % 4], stroke_width=5)
    for pts, col in ((pts2, '#a98bd0'), (pts1, '#8fc7e8')):
        d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
        o += f'<g transform="translate(4 4)">' + s('path', d=d, stroke=col, stroke_width=11) + '</g>'
        o += s('path', d=d, stroke_width=14) + s('path', d=d, stroke=col, stroke_width=8)
    return o


ITEMS['dna'] = helix()


# 14. lab sample (test tubes)
def ttube(x, top, liq, col):
    d = f'M{x-10} {top} L{x-10} 160 Q{x-10} 174 {x} 174 Q{x+10} 174 {x+10} 160 L{x+10} {top}Z'
    l = f'M{x-10} {liq} L{x-10} 160 Q{x-10} 174 {x} 174 Q{x+10} 174 {x+10} 160 L{x+10} {liq}Z'
    return (z('path', '#ffffff', d=d) + s('path', col, d=l, stroke='none') + s('path', d=d)
            + s('path', d=f'M{x-10} {liq} L{x+10} {liq}', stroke_width=2.5)
            + z('rect', '#ffffff', x=x - 14, y=top - 6, width=28, height=8, rx=3))


ITEMS['lab-sample'] = (
    ttube(62, 56, 118, '#9ccf7a') + ttube(100, 40, 96, '#f6a6b8') + ttube(138, 56, 110, '#8fc7e8')
    + dot(95, 108, 2.8) + dot(105, 108, 2.8) + cheeks(93, 107, 115, 2.6, 2) + s('path', d='M97 114 Q100 117 103 114', stroke_width=2)
    + z('rect', '#d9a66b', x=34, y=132, width=132, height=14, rx=3)
    + s('path', d='M42 146 L42 182 M158 146 L158 182', stroke_width=5)
    + z('rect', '#d9a66b', x=34, y=172, width=132, height=10, rx=3)
    + s('circle', '#ffffff', cx=100, cy=82, r=3, stroke_width=2) + s('circle', '#ffffff', cx=95, cy=70, r=2.5, stroke_width=2)
    + s('circle', '#ffffff', cx=138, cy=96, r=3, stroke_width=2)
)

# 15. pulse oximeter
ITEMS['pulse-oximeter'] = (
    z('path', SK, d='M70 112 L118 112 Q130 112 130 122 Q130 132 118 132 L70 132Z')
    + z('ellipse', SK, cx=50, cy=136, rx=28, ry=30)
    + s('path', d='M40 120 Q52 116 60 124 M36 138 Q50 134 60 142 M38 156 Q50 152 58 158', stroke_width=2.5)
    + z('rect', '#8fb3e0', x=92, y=132, width=74, height=30, rx=10)
    + z('rect', '#8fb3e0', x=92, y=66, width=74, height=48, rx=12)
    + s('rect', '#5b6b7a', x=102, y=74, width=54, height=32, rx=4, stroke_width=2.5)
    + s('path', d='M106 92 L118 92 L122 82 L128 100 L132 90 L152 90', stroke='#9ccf7a', stroke_width=2.5)
    + s('path', '#f07a8a', d='M114 86 C110 83 108 80 110 78 C112 76 114 77 114 79 C114 77 116 76 118 78 C120 80 118 83 114 86Z', stroke='none')
    + s('path', d='M164 92 Q178 98 174 120 Q170 132 164 136', stroke_width=3)
    + dot(129, 147, 3.5, '#ffffff')
)


# 16. crutches
def crutch(cx, ang):
    o = (tube(f'M{cx-14} 42 L{cx-5} 128 M{cx+14} 42 L{cx+5} 128', '#c9d3db', 5)
         + z('rect', '#5b6b7a', x=cx - 20, y=30, width=40, height=14, rx=7)
         + z('rect', '#5b6b7a', x=cx - 14, y=88, width=28, height=10, rx=4)
         + z('rect', '#c9d3db', x=cx - 6, y=124, width=12, height=46, rx=3)
         + z('rect', '#5b6b7a', x=cx - 8, y=166, width=16, height=12, rx=4))
    return f'<g transform="rotate({ang} {cx} 178)">{o}</g>'


ITEMS['crutches'] = crutch(76, -8) + crutch(124, 8)

# 17. wheelchair
spokes = ' '.join(f'M{96 + 8*math.cos(math.radians(a)):.1f} {132 + 8*math.sin(math.radians(a)):.1f} '
                  f'L{96 + 34*math.cos(math.radians(a)):.1f} {132 + 34*math.sin(math.radians(a)):.1f}' for a in range(0, 360, 45))
ITEMS['wheelchair'] = (
    s('path', d='M62 44 L76 44', stroke_width=7)
    + z('rect', '#8fb3e0', x=72, y=40, width=14, height=72, rx=4)
    + z('rect', '#8fb3e0', x=76, y=100, width=74, height=14, rx=4)
    + s('path', d='M110 92 L148 92', stroke_width=5)
    + s('path', d='M146 92 L146 100', stroke_width=4)
    + s('path', d='M142 114 L150 164 M144 132 L166 150 L176 150', stroke_width=5)
    + z('circle', '#5b6b7a', cx=96, cy=132, r=44)
    + s('circle', '#f4f4f0', cx=96, cy=132, r=34)
    + s('path', d=spokes, stroke_width=2.5)
    + s('circle', '#c9d3db', cx=96, cy=132, r=8)
    + z('circle', '#5b6b7a', cx=152, cy=170, r=9)
    + dot(152, 170, 3, '#c9d3db')
)

# 18. hearing aid
EAR = 'M74 70 Q78 34 112 34 Q146 36 148 74 Q148 104 128 120 Q118 130 118 146 Q116 170 94 170 Q78 168 76 152'
ITEMS['hearing-aid'] = (
    z('path', SK, d=EAR + ' Q88 140 86 120 Q70 100 74 70Z')
    + s('path', d='M92 64 Q98 50 114 52 Q130 56 130 78 Q128 96 110 104 Q102 112 104 124', stroke_width=3)
    + s('path', d='M100 82 Q108 74 114 82', stroke_width=2.5)
    + z('path', '#8fb3e0', d='M136 44 Q166 56 162 104 Q158 122 150 124 Q144 124 146 112 Q152 70 130 54 Q126 44 136 44Z')
    + dot(154, 86, 2.5, '#ffffff') + dot(156, 98, 2.5, '#ffffff')
    + s('path', d='M134 46 Q112 24 98 50 Q92 66 96 92', stroke_width=5)
    + s('path', d='M134 46 Q112 24 98 50 Q92 66 96 92', stroke='#f4f4f0', stroke_width=2)
    + z('circle', '#ffffff', cx=96, cy=96, r=7)
    + s('path', d='M54 82 Q46 96 54 110 M40 74 Q28 96 40 118', stroke='#7cc4b0', stroke_width=4)
)

# 19. contact lens case
ITEMS['contact-lens'] = (
    z('rect', '#f6e0c4', x=30, y=100, width=140, height=50, rx=25)
    + z('circle', '#8fc7e8', cx=58, cy=125, r=26)
    + s('circle', '#d8eef8', cx=58, cy=125, r=18)
    + s('path', '#ffffff', d='M46 131 Q46 114 58 114 Q70 114 70 131 Q58 125 46 131Z', stroke_width=2.5)
    + z('circle', '#f6a6b8', cx=142, cy=125, r=26)
    + s('circle', cx=142, cy=125, r=18, stroke_width=2)
    + ''.join(s('path', d=f'M{142 + 20*math.cos(math.radians(a)):.1f} {125 + 20*math.sin(math.radians(a)):.1f} L{142 + 24*math.cos(math.radians(a)):.1f} {125 + 24*math.sin(math.radians(a)):.1f}', stroke_width=2) for a in range(0, 360, 30))
    + dot(93, 122, 3) + dot(107, 122, 3) + cheeks(90, 110, 130, 3.5, 2.3) + s('path', d='M96 129 Q100 133 104 129', stroke_width=2.2)
    + z('circle', '#8fc7e8', cx=66, cy=58, r=24)
    + s('circle', cx=66, cy=58, r=16, stroke_width=2)
    + ''.join(s('path', d=f'M{66 + 18*math.cos(math.radians(a)):.1f} {58 + 18*math.sin(math.radians(a)):.1f} L{66 + 22*math.cos(math.radians(a)):.1f} {58 + 22*math.sin(math.radians(a)):.1f}', stroke_width=2) for a in range(0, 360, 30))
    + s('path', d='M140 52 L140 72 M130 62 L150 62', stroke='#ffc94d', stroke_width=3)
    + s('path', d='M162 80 L162 90 M157 85 L167 85', stroke='#ffc94d', stroke_width=2.5)
)

# 20. toothbrush and toothpaste
ITEMS['toothbrush'] = (
    z('rect', '#8fc7e8', x=30, y=64, width=120, height=14, rx=7)
    + z('rect', '#8fc7e8', x=128, y=60, width=44, height=20, rx=8)
    + z('rect', '#ffffff', x=132, y=40, width=36, height=20, rx=2)
    + s('path', d='M141 42 L141 58 M150 42 L150 58 M159 42 L159 58', stroke_width=2)
    + z('path', '#ffffff', d='M128 40 Q130 26 142 30 Q150 22 158 30 Q172 28 172 40Z')
    + s('path', d='M136 36 Q148 28 166 36', stroke='#7cc4b0', stroke_width=3)
    + z('path', '#f4f4f0', d='M36 112 L44 112 Q50 122 50 132 Q50 142 44 152 L36 152Z')
    + z('path', '#ffffff', d='M44 112 L134 116 Q140 118 140 132 Q140 146 134 148 L44 152 Q50 142 50 132 Q50 122 44 112Z')
    + s('path', '#7cc4b0', d='M66 113 L106 115 L106 149 L66 151Z', stroke_width=2.5)
    + z('rect', '#e8735a', x=138, y=120, width=26, height=24, rx=4)
    + dot(80, 130, 3.5) + dot(96, 130, 3.5) + cheeks(72, 104, 139, 5, 3) + s('path', d='M84 138 Q88 142 92 138', stroke_width=2.5)
    + s('path', d='M40 116 L40 148', stroke_width=2)
    + s('circle', '#ffffff', cx=56, cy=176, r=6, stroke_width=2.5) + s('circle', '#ffffff', cx=150, cy=172, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=110, cy=182, r=4, stroke_width=2.5)
)
