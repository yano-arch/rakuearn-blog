from math import cos, sin, pi
from art import z, s, dot, cheeks, face, OUT, CH


def tube(d, color, w=6):
    """thick colored line with brown outline"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def mini_face(cx, cy, k=1.0):
    return (dot(cx - 10 * k, cy, 3.5 * k) + dot(cx + 10 * k, cy, 3.5 * k)
            + cheeks(cx - 17 * k, cx + 17 * k, cy + 8 * k, 6 * k, 3.5 * k)
            + s('path', d=f'M{cx-5*k} {cy+8*k} Q{cx} {cy+13*k} {cx+5*k} {cy+8*k}', stroke_width=2.5))


def sparkle(cx, cy, r):
    q = r * 0.28
    return (f'M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} '
            f'Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r}Z')


def gear(cx, cy, r_out, r_in, n):
    pts = []
    for i in range(n):
        a = 2 * pi * i / n
        w = pi / n * 0.55
        for ang, r in ((a - w, r_in), (a - w * 0.6, r_out), (a + w * 0.6, r_out), (a + w, r_in)):
            pts.append(f'{cx + r * cos(ang):.1f} {cy + r * sin(ang):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


ITEMS = {}

ITEMS['desktop-computer'] = (
    z('path', '#c9d3db', d='M90 128 L110 128 L114 158 L86 158Z')
    + z('rect', '#c9d3db', x=62, y=154, width=76, height=14, rx=6)
    + z('rect', '#5b6b7a', x=30, y=36, width=140, height=98, rx=10)
    + s('rect', '#d8eef8', x=40, y=46, width=120, height=76, rx=4)
    + z('rect', '#ffffff', x=56, y=58, width=74, height=50, rx=3)
    + s('rect', '#8fc7e8', x=56, y=58, width=74, height=12, rx=3, stroke_width=2.5)
    + dot(63, 64, 2.2, '#e8735a') + dot(70, 64, 2.2, '#ffc94d') + dot(77, 64, 2.2, '#9ccf7a')
    + s('path', d='M66 82 L116 82 M66 94 L100 94', stroke_width=2.5)
    + dot(100, 128, 2.5, '#c9d3db')
    + s('path', d='M24 180 L176 180', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=140, y=168, width=26, height=12, rx=6)
)

icons = ''
cols = ['#f07a8a', '#ffc94d', '#9ccf7a', '#8fc7e8', '#a98bd0', '#f5b971', '#7cc4b0', '#e8735a', '#8fb3e0']
for i, c in enumerate(cols):
    x = 72 + (i % 3) * 20
    y = 58 + (i // 3) * 24
    icons += s('rect', c, x=x, y=y, width=14, height=14, rx=4, stroke_width=2)
ITEMS['tablet'] = (
    z('rect', '#5b6b7a', x=50, y=28, width=100, height=146, rx=14)
    + s('rect', '#d8eef8', x=59, y=40, width=82, height=116, rx=4)
    + icons
    + s('rect', '#ffffff', x=72, y=132, width=54, height=14, rx=7, stroke_width=2)
    + dot(100, 165, 3.5, '#c9d3db')
)

ITEMS['smartwatch'] = (
    z('rect', '#7cc4b0', x=78, y=24, width=44, height=50, rx=8)
    + z('rect', '#7cc4b0', x=78, y=126, width=44, height=52, rx=8)
    + s('path', d='M86 150 L114 150 M86 162 L114 162', stroke_width=2)
    + dot(100, 156, 2.5)
    + z('rect', '#c9d3db', x=146, y=88, width=10, height=24, rx=4)
    + z('rect', '#5b6b7a', x=56, y=56, width=92, height=88, rx=24)
    + s('rect', '#d8eef8', x=66, y=66, width=72, height=68, rx=16)
    + s('path', '#f07a8a',
        d='M102 112 C92 104 86 98 90 90 C94 84 102 87 102 93 C102 87 110 84 114 90 C118 98 112 104 102 112Z',
        stroke_width=2.5)
    + s('path', d='M74 120 L84 120 L88 112 L94 126 L98 120 L130 120', stroke_width=2)
)

ITEMS['headphones'] = (
    tube('M48 118 Q40 40 100 38 Q160 40 152 118', '#8fb3e0', 10)
    + z('rect', '#5b6b7a', x=30, y=104, width=24, height=60, rx=10)
    + z('rect', '#5b6b7a', x=146, y=104, width=24, height=60, rx=10)
    + z('rect', '#8fb3e0', x=44, y=96, width=30, height=76, rx=13)
    + z('rect', '#8fb3e0', x=126, y=96, width=30, height=76, rx=13)
)

def bud(cx, cy, flip=1):
    return (z('rect', '#ffffff', x=cx - 7, y=cy, width=14, height=40, rx=7)
            + z('circle', '#ffffff', cx=cx, cy=cy, r=16)
            + s('circle', '#c9d3db', cx=cx + 6 * flip, cy=cy - 4, r=6, stroke_width=2.5))

ITEMS['earbuds'] = (
    z('rect', '#f4f4f0', x=46, y=108, width=108, height=66, rx=30)
    + s('path', d='M48 128 L152 128', stroke_width=2.5)
    + dot(100, 150, 3.5, '#9ccf7a')
    + bud(76, 60, -1) + bud(124, 60, 1)
    + s('path', d='M48 38 L42 30 M152 38 L158 30 M100 28 L100 20', stroke_width=2.5)
)

keys = ''
for r in range(3):
    off = (0, 6, 12)[r]
    for c in range(9 - (1 if r else 0)):
        x = 30 + off + c * 16
        keys += s('rect', '#ffffff', x=x, y=82 + r * 18, width=12, height=13, rx=3, stroke_width=2)
ITEMS['keyboard'] = (
    z('rect', '#c9d3db', x=20, y=70, width=160, height=86, rx=10)
    + keys
    + s('rect', '#ffffff', x=36, y=136, width=12, height=13, rx=3, stroke_width=2)
    + s('rect', '#ffffff', x=54, y=136, width=92, height=13, rx=3, stroke_width=2)
    + s('rect', '#ffffff', x=152, y=136, width=12, height=13, rx=3, stroke_width=2)
    + s('rect', '#f07a8a', x=158, y=118, width=12, height=13, rx=3, stroke_width=2)
    + s('path', d='M100 70 Q100 50 118 46 Q140 42 142 26', stroke_width=3)
)

ITEMS['computer-mouse'] = (
    s('path', d='M100 46 Q100 26 124 26 Q150 26 152 44', stroke_width=3)
    + z('path', '#8fb3e0', d='M100 46 Q144 46 146 106 Q148 172 100 174 Q52 172 54 106 Q56 46 100 46Z')
    + s('path', d='M54 98 Q100 104 146 98 M100 46 L100 101')
    + z('rect', '#5b6b7a', x=94, y=62, width=12, height=24, rx=6)
    + mini_face(100, 128)
)

ITEMS['printer'] = (
    z('rect', '#ffffff', x=62, y=28, width=76, height=56)
    + s('path', d='M74 44 L122 44 M74 56 L112 56', stroke_width=2.5)
    + z('rect', '#c9d3db', x=30, y=74, width=140, height=72, rx=12)
    + s('rect', '#5b6b7a', x=56, y=82, width=88, height=8, rx=4, stroke_width=2.5)
    + dot(150, 98, 4, '#9ccf7a') + dot(150, 112, 4, '#f5d58a')
    + z('rect', '#8fb3e0', x=40, y=124, width=120, height=24, rx=6)
    + z('path', '#ffffff', d='M62 138 L138 138 L144 176 L56 176Z')
    + s('path', '#8fc7e8', d='M72 150 Q86 144 96 156 Q110 168 124 152 L128 168 L70 168Z', stroke_width=2)
    + dot(116, 148, 4, '#ffc94d')
)

ITEMS['usb-drive'] = (
    z('rect', '#c9d3db', x=24, y=80, width=50, height=40, rx=3)
    + s('rect', '#5b6b7a', x=36, y=90, width=10, height=8, stroke_width=2)
    + s('rect', '#5b6b7a', x=52, y=90, width=10, height=8, stroke_width=2)
    + z('rect', '#e8735a', x=68, y=68, width=104, height=64, rx=14)
    + s('circle', '#fbf6ee', cx=156, cy=100, r=6)
    + mini_face(108, 96)
    + s('path', d='M178 60 L186 52 M182 76 L192 74', stroke_width=2.5)
)

units = ''
for i, y in enumerate((40, 74, 108, 142)):
    units += s('rect', '#5b6b7a', x=64, y=y, width=72, height=26, rx=4, stroke_width=2.5)
    units += s('path', d=f'M74 {y+9} L104 {y+9} M74 {y+17} L104 {y+17}', stroke='#c9d3db', stroke_width=2.5)
    units += dot(118, y + 13, 3.5, '#9ccf7a') + dot(127, y + 13, 3.5, '#ffc94d' if i % 2 else '#8fc7e8')
ITEMS['server'] = (
    z('rect', '#c9d3db', x=54, y=28, width=92, height=148, rx=8)
    + units
    + z('rect', '#5b6b7a', x=58, y=176, width=12, height=8, rx=2)
    + z('rect', '#5b6b7a', x=130, y=176, width=12, height=8, rx=2)
)

ITEMS['vr-headset'] = (
    z('path', '#a98bd0', d='M62 186 Q64 126 100 124 Q136 126 138 186Z')
    + face(100, 94, '#ffd9b8', '#5a4033', 'open')
    + s('path', d='M66 86 L58 86 M134 86 L142 86', stroke='#5b6b7a', stroke_width=8)
    + z('rect', '#5b6b7a', x=62, y=70, width=76, height=34, rx=14)
    + s('rect', '#8fb3e0', x=70, y=77, width=60, height=20, rx=9, stroke_width=2.5)
    + s('path', d='M78 82 Q84 79 90 82', stroke='#ffffff', stroke_width=2.5)
    + z('path', '#ffe27a', d=sparkle(156, 52, 12))
    + z('path', '#ffe27a', d=sparkle(42, 60, 9))
)

def rotor(cx, cy):
    return (s('path', d=f'M{cx} {cy} L{cx} {cy-10}', stroke_width=4)
            + z('ellipse', '#c9d3db', cx=cx, cy=cy - 12, rx=26, ry=6))

ITEMS['drone'] = (
    tube('M80 96 L44 74', '#5b6b7a', 6) + tube('M120 96 L156 74', '#5b6b7a', 6)
    + rotor(44, 74) + rotor(156, 74)
    + s('path', d='M78 120 L68 146 M122 120 L132 146', stroke_width=4)
    + s('path', d='M58 146 L80 146 M120 146 L142 146', stroke_width=4)
    + z('rect', '#ffffff', x=66, y=84, width=68, height=40, rx=16)
    + mini_face(100, 100, 0.9)
    + z('rect', '#5b6b7a', x=88, y=124, width=24, height=16, rx=5)
    + s('circle', '#8fc7e8', cx=100, cy=132, r=4, stroke_width=2)
)

ITEMS['3d-printer'] = (
    z('rect', '#5b6b7a', x=40, y=36, width=12, height=124, rx=3)
    + z('rect', '#5b6b7a', x=148, y=36, width=12, height=124, rx=3)
    + z('rect', '#5b6b7a', x=36, y=28, width=128, height=14, rx=4)
    + s('path', d='M52 66 L148 66', stroke_width=4)
    + z('rect', '#e8735a', x=98, y=54, width=28, height=24, rx=4)
    + z('path', '#c9d3db', d='M106 78 L118 78 L112 88Z')
    + z('path', '#9ccf7a', d='M88 140 L120 140 L116 112 Q104 104 92 112Z')
    + s('path', d='M90 128 L118 128 M90 120 L116 120', stroke_width=2)
    + z('rect', '#c9d3db', x=56, y=140, width=88, height=10, rx=3)
    + z('rect', '#f4f4f0', x=28, y=156, width=144, height=24, rx=6)
    + dot(48, 168, 4, '#9ccf7a') + s('rect', '#8fc7e8', x=120, y=162, width=38, height=12, rx=3, stroke_width=2)
)

grill = ''
for r in range(4):
    for c in range(5):
        grill += dot(78 + c * 11, 120 + r * 12, 2.4, '#5b6b7a')
ITEMS['smart-speaker'] = (
    z('path', '#c9d3db', d='M60 66 Q60 54 100 54 Q140 54 140 66 L140 166 Q140 178 100 178 Q60 178 60 166Z')
    + s('ellipse', '#f4f4f0', cx=100, cy=64, rx=40, ry=10)
    + s('ellipse', '#8fc7e8', cx=100, cy=64, rx=26, ry=5, stroke_width=2.5)
    + grill
    + dot(89, 90, 3.5) + dot(111, 90, 3.5) + cheeks(80, 120, 98, 5.5, 3)
    + s('path', d='M95 98 Q100 103 105 98', stroke_width=2.5)
    + s('path', d='M152 90 Q162 104 152 118 M164 80 Q180 104 164 128', stroke_width=3)
    + s('path', d='M48 90 Q38 104 48 118 M36 80 Q20 104 36 128', stroke_width=3)
)

ITEMS['ai-chat'] = (
    z('path', '#a98bd0', d='M50 40 L150 40 Q172 40 172 62 L172 116 Q172 138 150 138 L88 138 L56 166 L62 138 L50 138 '
                         'Q28 138 28 116 L28 62 Q28 40 50 40Z')
    + z('path', '#ffe27a', d=sparkle(92, 88, 30))
    + z('path', '#ffffff', d=sparkle(136, 66, 14))
    + z('path', '#ffffff', d=sparkle(134, 112, 10))
)

pins = ''
for i in range(4):
    p = 66 + i * 22
    pins += s('rect', '#c9d3db', x=p - 4, y=26, width=8, height=18, rx=2, stroke_width=2.5)
    pins += s('rect', '#c9d3db', x=p - 4, y=156, width=8, height=18, rx=2, stroke_width=2.5)
    pins += s('rect', '#c9d3db', x=26, y=p - 4, width=18, height=8, rx=2, stroke_width=2.5)
    pins += s('rect', '#c9d3db', x=156, y=p - 4, width=18, height=8, rx=2, stroke_width=2.5)
ITEMS['ai-chip'] = (
    pins
    + z('rect', '#5b6b7a', x=40, y=40, width=120, height=120, rx=14)
    + s('rect', '#7cc4b0', x=56, y=56, width=88, height=88, rx=8)
    + s('path', '#f6a6b8', d='M100 72 Q86 62 76 72 Q64 74 66 88 Q58 98 66 108 Q66 124 82 124 Q92 132 100 124Z', stroke_width=2.5)
    + s('path', '#f6a6b8', d='M100 72 Q114 62 124 72 Q136 74 134 88 Q142 98 134 108 Q134 124 118 124 Q108 132 100 124Z', stroke_width=2.5)
    + s('path', d='M100 72 L100 124 M76 86 Q84 90 82 98 M70 108 Q80 104 88 112 M124 86 Q116 90 118 98 M130 108 Q120 104 112 112',
        stroke_width=2.2)
)

def code_lines():
    rows = [(0, 40, '#f07a8a'), (14, 30, '#ffc94d'), (14, 22, '#8fc7e8'), (28, 34, '#9ccf7a'),
            (14, 18, '#a98bd0'), (0, 26, '#f07a8a')]
    o = ''
    for i, (ind, w, c) in enumerate(rows):
        y = 62 + i * 11
        o += s('path', d=f'M{54+ind} {y} L{54+ind+w} {y}', stroke=c, stroke_width=5)
        if i in (0, 3):
            o += s('path', d=f'M{54+ind+w+10} {y} L{54+ind+w+26} {y}', stroke='#f4f4f0', stroke_width=5)
    return o

ITEMS['coding-screen'] = (
    z('path', '#c9d3db', d='M90 128 L110 128 L114 158 L86 158Z')
    + z('rect', '#c9d3db', x=62, y=154, width=76, height=14, rx=6)
    + z('rect', '#5b6b7a', x=30, y=36, width=140, height=98, rx=10)
    + s('rect', '#3d4a5c', x=40, y=46, width=120, height=76, rx=4)
    + code_lines()
    + s('rect', '#ffe27a', x=136, y=113, width=8, height=4, stroke='none')
    + s('path', d='M24 180 L176 180', stroke_width=2.5)
)

ITEMS['bug-code'] = (
    z('rect', '#5b6b7a', x=24, y=30, width=152, height=110, rx=10)
    + s('rect', '#d8eef8', x=34, y=40, width=132, height=90, rx=4)
    + s('path', d='M44 54 L80 54 M44 66 L70 66 M128 112 L156 112 M136 124 L156 124', stroke='#8fc7e8', stroke_width=5)
    + s('path', d='M78 80 L62 72 M78 96 L60 96 M80 112 L64 122 M122 80 L138 72 M122 96 L140 96 M120 112 L136 122',
        stroke_width=3)
    + s('path', d='M92 60 Q86 48 78 46 M108 60 Q114 48 122 46', stroke_width=3)
    + dot(78, 46, 4) + dot(122, 46, 4)
    + z('ellipse', '#9ccf7a', cx=100, cy=98, rx=26, ry=30)
    + s('path', d='M100 74 L100 126', stroke_width=2.5)
    + z('ellipse', '#7cc4a0', cx=100, cy=72, rx=18, ry=13)
    + dot(93, 71, 3) + dot(107, 71, 3) + cheeks(86, 114, 77, 4, 2.5)
    + dot(88, 98, 4, '#5b6b7a') + dot(112, 106, 4, '#5b6b7a') + dot(90, 116, 3, '#5b6b7a')
    + z('path', '#c9d3db', d='M90 140 L110 140 L114 166 L86 166Z')
    + z('rect', '#c9d3db', x=64, y=162, width=72, height=14, rx=6)
)

ITEMS['settings-gear'] = (
    z('path', '#8fb3e0', d=gear(142, 58, 30, 22, 8))
    + s('circle', '#fbf6ee', cx=142, cy=58, r=9)
    + z('path', '#c9d3db', d=gear(88, 114, 62, 48, 10))
    + s('circle', '#f4f4f0', cx=88, cy=114, r=32)
    + dot(78, 112, 3.5) + dot(98, 112, 3.5) + cheeks(70, 106, 121, 5.5, 3)
    + s('path', d='M83 121 Q88 126 93 121', stroke_width=2.5)
)

ITEMS['download'] = (
    z('path', '#7cc4b0', d='M86 26 L114 26 L114 82 L138 82 L100 124 L62 82 L86 82Z')
    + z('path', '#8fb3e0', d='M30 116 L56 116 L56 140 Q56 146 62 146 L138 146 Q144 146 144 140 L144 116 L170 116 '
                          'L170 166 Q170 178 158 178 L42 178 Q30 178 30 166Z')
    + dot(148, 162, 4, '#9ccf7a')
)
