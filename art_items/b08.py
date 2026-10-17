from art import z, s, dot, cheeks, face, OUT, CH
import math

ITEMS = {}


def _f(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def _frame(cx, cy, deg):
    """回転座標系: u=長さ方向, v=幅方向 -> 画面座標"""
    a = math.radians(deg)
    ux, uy = math.cos(a), math.sin(a)
    vx, vy = -uy, ux

    def P(u, v):
        return (cx + u * ux + v * vx, cy + u * uy + v * vy)
    return P


def _poly(pts):
    return 'M' + ' L'.join(f'{_f(x)} {_f(y)}' for x, y in pts) + 'Z'


def _line(a, b):
    return f'M{_f(a[0])} {_f(a[1])} L{_f(b[0])} {_f(b[1])}'


# 1. pencil
P = _frame(100, 104, -45)
pen = (z('path', '#f6e0c4', d=_poly([P(-40, -16), P(-70, 0), P(-40, 16)]))
       + z('path', '#5b6b7a', d=_poly([P(-60, -5.4), P(-72, 0), P(-60, 5.4)]))
       + z('path', '#ffc94d', d=_poly([P(-40, -16), P(46, -16), P(46, 16), P(-40, 16)]))
       + s('path', d=_line(P(-40, -5.5), P(46, -5.5)) + ' ' + _line(P(-40, 5.5), P(46, 5.5)), stroke_width=2)
       + z('path', '#f6a6b8', d=_poly([P(56, -16), P(66, -16), P(70, -10), P(70, 10), P(66, 16), P(56, 16)]))
       + z('path', '#b9a99c', d=_poly([P(44, -17), P(58, -17), P(58, 17), P(44, 17)]))
       + s('path', d=_line(P(51, -17), P(51, 17)), stroke_width=2)
       + f'<g>{dot(94, 100)}{dot(108, 100)}{cheeks(88, 114, 110, 5, 3)}</g>'
       + s('path', d='M97 109 Q101 113 105 109', stroke_width=2.5))
ITEMS['pencil'] = pen

# 2. notebook-pen
nb = (z('path', '#8fb3e0', d='M24 66 Q62 52 100 64 Q138 52 176 66 L176 168 Q138 156 100 170 Q62 156 24 168Z')
      + z('path', '#ffffff', d='M30 62 Q66 50 100 62 L100 160 Q66 148 30 158Z')
      + z('path', '#ffffff', d='M170 62 Q134 50 100 62 L100 160 Q134 148 170 158Z')
      + ''.join(s('path', d=f'M40 {y} Q66 {y-8} 92 {y+2}', stroke='#8fc7e8', stroke_width=2) for y in (80, 96, 112, 128, 144))
      + ''.join(s('path', d=f'M108 {y+2} Q134 {y-8} 160 {y}', stroke='#8fc7e8', stroke_width=2) for y in (80, 96, 112))
      + s('path', d='M100 62 L100 160'))
P = _frame(140, 128, -50)
nb += (z('path', '#e8735a', d=_poly([P(-26, -7), P(40, -7), P(46, -4), P(46, 4), P(40, 7), P(-26, 7)]))
       + z('path', '#f6e0c4', d=_poly([P(-26, -7), P(-40, 0), P(-26, 7)]))
       + s('path', d=_line(P(-26, -7), P(-26, 7)))
       + s('path', d=_line(P(14, -7), P(14, 7)))
       + s('path', d=_line(P(18, -7), P(36, -11)), stroke_width=2.5))
ITEMS['notebook-pen'] = nb

# 3. stack-of-books
bk = ''
for (x, y, w, c, band) in ((36, 142, 128, '#e8735a', '#f5d58a'), (46, 112, 112, '#8fc7e8', '#ffffff'), (40, 82, 118, '#9ccf7a', '#f5d58a')):
    bk += (z('rect', c, x=x, y=y, width=w, height=30, rx=5)
           + s('rect', '#f4f4f0', x=x + w - 22, y=y + 5, width=22, height=20, stroke_width=2.5)
           + s('path', d=f'M{x+w-18} {y+11} L{x+w} {y+11} M{x+w-18} {y+19} L{x+w} {y+19}', stroke_width=1.5)
           + s('rect', band, x=x + 14, y=y + 9, width=w - 52, height=12, rx=3, stroke_width=2.5))
bk += z('path', '#e04b5a', d='M70 82 L70 64 L78 70 L86 64 L86 82Z')
bk = bk.replace(z('path', '#e04b5a', d='M70 82 L70 64 L78 70 L86 64 L86 82Z'), '')
bk += (s('path', '#e04b5a', d='M118 112 L118 124 L123 120 L128 124 L128 112', stroke_width=2.5))
ITEMS['stack-of-books'] = bk

# 4. school-backpack
bp = (s('path', d='M84 44 Q84 26 100 26 Q116 26 116 44', stroke_width=6)
      + s('path', d='M84 44 Q84 26 100 26 Q116 26 116 44', stroke='#e8735a', stroke_width=2)
      + z('rect', '#e8735a', x=44, y=60, width=12, height=70, rx=6)
      + z('rect', '#e8735a', x=144, y=60, width=12, height=70, rx=6)
      + z('rect', '#e8735a', x=52, y=40, width=96, height=140, rx=30)
      + z('path', '#f07a8a', d='M52 72 Q52 40 84 40 L116 40 Q148 40 148 72 L148 84 Q100 98 52 84Z')
      + z('rect', '#f5b971', x=66, y=120, width=68, height=48, rx=12)
      + s('path', d='M72 132 L128 132', stroke_width=2)
      + s('rect', '#ffe27a', x=94, y=126, width=12, height=12, rx=3, stroke_width=2.5)
      + dot(88, 106) + dot(112, 106) + cheeks(80, 120, 114, 5, 3)
      + s('path', d='M96 112 Q100 116 104 112', stroke_width=2.5))
ITEMS['school-backpack'] = bp

# 5. graduation-cap
gc = (z('path', '#5b6b7a', d='M62 82 L62 116 Q100 132 138 116 L138 82Z')
      + z('path', '#5b6b7a', d='M100 46 L172 74 L100 102 L28 74Z')
      + s('path', d='M100 74 Q130 80 150 82 L150 106', stroke='#ffc94d', stroke_width=3)
      + s('path', d='M100 74 Q130 80 150 82 L150 106', stroke_width=0.0001)
      + z('path', '#ffc94d', d='M144 106 L156 106 L160 124 L140 124Z')
      + dot(100, 74, 5, '#ffc94d')
      + z('rect', '#f4f4f0', x=44, y=142, width=112, height=26, rx=13)
      + s('ellipse', '#f6e0c4', cx=57, cy=155, rx=7, ry=13)
      + s('path', d='M54 155 Q57 150 60 155', stroke_width=2)
      + s('rect', '#e04b5a', x=96, y=140, width=12, height=30, rx=2, stroke_width=2.5)
      + s('path', '#e04b5a', d='M102 170 L94 182 M102 170 L110 182', stroke='#e04b5a', stroke_width=4))
gc = gc.replace(s('path', d='M100 74 Q130 80 150 82 L150 106', stroke_width=0.0001), '')
gc = gc.replace(s('path', d='M100 74 Q130 80 150 82 L150 106', stroke='#ffc94d', stroke_width=3),
                s('path', d='M100 74 Q130 80 150 82 L150 106', stroke_width=6)
                + s('path', d='M100 74 Q130 80 150 82 L150 106', stroke='#ffc94d', stroke_width=2.5))
ITEMS['graduation-cap'] = gc

# 6. microscope
P = _frame(88, 82, -68)  # 鏡筒（左下→右上）
ms = (z('path', '#8fb3e0', d='M108 158 Q146 148 146 108 Q146 68 118 56 L112 72 Q130 82 130 110 Q130 140 100 146Z')
      + z('rect', '#5b6b7a', x=44, y=158, width=112, height=20, rx=7)
      + z('rect', '#5b6b7a', x=54, y=124, width=72, height=10, rx=3)
      + s('rect', '#c9d3db', x=72, y=119, width=36, height=5, rx=2, stroke_width=2)
      + z('path', '#f4f4f0', d=_poly([P(-26, -14), P(30, -14), P(30, 14), P(-26, 14)]))
      + z('path', '#5b6b7a', d=_poly([P(-40, -8), P(-26, -10), P(-26, 10), P(-40, 8)]))
      + z('path', '#5b6b7a', d=_poly([P(30, -16), P(48, -16), P(48, 16), P(30, 16)]))
      + s('path', d=_line(P(30, -14), P(30, 14)), stroke_width=0.01)
      + z('circle', '#f5b971', cx=136, cy=112, r=9)
      + s('path', d='M64 158 L64 134 M116 158 L116 134', stroke_width=0.01))
ms = ms.replace(s('path', d=_line(P(30, -14), P(30, 14)), stroke_width=0.01), '')
ms = ms.replace(s('path', d='M64 158 L64 134 M116 158 L116 134', stroke_width=0.01), '')
ITEMS['microscope'] = ms

# 7. calculator
ca = (z('rect', '#8fb3e0', x=54, y=30, width=92, height=146, rx=14)
      + s('rect', '#d8eef8', x=66, y=44, width=68, height=34, rx=5)
      + dot(90, 58, 3) + dot(110, 58, 3) + cheeks(83, 117, 66, 5, 3)
      + s('path', d='M96 66 Q100 70 104 66', stroke_width=2.5))
for r in range(4):
    for c in range(4):
        col = '#f5b971' if c == 3 else ('#f07a8a' if (r, c) == (0, 0) else '#f4f4f0')
        ca += s('rect', col, x=66 + c * 18, y=88 + r * 20, width=13, height=14, rx=3, stroke_width=2.5)
ITEMS['calculator'] = ca

# 8. ruler-triangle
rt = (z('path', '#8fc7e8', d='M34 176 L34 58 L146 176Z')
      + s('path', d='M50 160 L50 98 L108 160Z', stroke_width=2.5))
P = _frame(118, 96, -38)
rt += z('path', '#f5d58a', d=_poly([P(-72, -15), P(72, -15), P(72, 15), P(-72, 15)]))
ticks = ''
for i in range(-64, 66, 8):
    L = 11 if i % 32 == 0 else (8 if i % 16 == 0 else 5)
    ticks += _line(P(i, -15), P(i, -15 + L)) + ' '
rt += s('path', d=ticks.strip(), stroke_width=2)
ITEMS['ruler-triangle'] = rt

# 9. student-studying
st = (s('path', d='M150 126 Q170 96 150 70', stroke='#5b6b7a', stroke_width=0.01))
st = (z('path', '#9ccf7a', d='M48 134 Q50 100 82 98 Q114 100 116 134Z')
      + face(82, 68, '#c68642', '#2b2220', 'smile')
      + s('path', d='M150 124 L150 92 L138 70', stroke_width=6)
      + s('path', d='M150 124 L150 92 L138 70', stroke='#5b6b7a', stroke_width=2)
      + z('path', '#f5b971', d='M120 64 Q132 44 156 58 L146 72 Z')
      + s('path', '#ffe27a', d='M136 72 L126 82 M142 76 L138 88 M130 66 L118 72', stroke='#ffc94d', stroke_width=2.5)
      + z('rect', '#d9a66b', x=24, y=130, width=152, height=12, rx=3)
      + s('path', d='M36 142 L36 182 M164 142 L164 182')
      + z('ellipse', '#5b6b7a', cx=150, cy=128, rx=13, ry=4)
      + z('path', '#ffffff', d='M78 130 L88 120 L128 120 L120 130Z')
      + s('path', d='M98 126 L114 126', stroke='#8fc7e8', stroke_width=2)
      + s('path', d='M100 110 L112 92', stroke='#e8735a', stroke_width=4)
      + s('path', d='M100 110 L112 92', stroke_width=0.01)
      + s('path', d='M64 112 Q78 124 104 118', stroke_width=7)
      + s('path', d='M64 112 Q78 124 104 118', stroke='#9ccf7a', stroke_width=2.5)
      + z('circle', '#c68642', cx=106, cy=116, r=7))
st = st.replace(s('path', d='M100 110 L112 92', stroke_width=0.01), '')
st = st.replace(s('path', d='M100 110 L112 92', stroke='#e8735a', stroke_width=4),
                s('path', d='M106 116 L118 98', stroke_width=7) + s('path', d='M106 116 L118 98', stroke='#e8735a', stroke_width=2.5))
# 鉛筆は手より前に
_pen = s('path', d='M106 116 L118 98', stroke_width=7) + s('path', d='M106 116 L118 98', stroke='#e8735a', stroke_width=2.5)
st = st.replace(_pen, '') + _pen
ITEMS['student-studying'] = st

# 10. school-building
sb = (s('path', d='M158 176 L158 36', stroke_width=4)
      + z('path', '#e8735a', d='M158 38 L182 44 L158 52Z') if False else '')
sb = (s('path', d='M156 176 L156 34', stroke_width=4)
      + z('path', '#e8735a', d='M157 36 Q168 32 178 38 L178 56 Q168 50 157 54Z')
      + dot(156, 32, 4.5, OUT)
      + z('rect', '#f5d58a', x=26, y=96, width=112, height=80, rx=2)
      + z('rect', '#f6e0c4', x=62, y=62, width=40, height=40)
      + z('path', '#e8735a', d='M56 66 L82 40 L108 66Z')
      + z('path', '#e8735a', d='M20 100 L82 84 L144 100Z')
      + z('circle', '#ffffff', cx=82, cy=80, r=11)
      + s('path', d='M82 80 L82 73 M82 80 L87 83', stroke_width=2.5)
      + z('rect', '#8b6b4f', x=70, y=142, width=24, height=34, rx=3)
      + s('path', d='M82 142 L82 176', stroke_width=2))
for x in (36, 106):
    for y in (110, 140):
        sb += s('rect', '#8fc7e8', x=x, y=y, width=22, height=18, rx=2, stroke_width=2.5)
sb += s('path', d='M16 178 L184 178', stroke_width=2.5)
ITEMS['school-building'] = sb
