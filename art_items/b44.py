from art import z, s, dot, cheeks, face, OUT, CH
import math

ITEMS = {}
SK = '#ffd9b8'


def _f(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def _frame(cx, cy, deg):
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


def sface(cx, cy, r, hair, mouth='smile', skin=SK):
    k = r / 34
    def X(d): return _f(cx + d * k)
    def Y(d): return _f(cy + d * k)
    o = z('circle', skin, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{X(-34)} {Y(-2)} Q{X(-32)} {Y(-36)} {X(0)} {Y(-35)} Q{X(32)} {Y(-36)} {X(34)} {Y(-2)} '
           f'Q{X(20)} {Y(-18)} {X(0)} {Y(-17)} Q{X(-20)} {Y(-18)} {X(-34)} {Y(-2)}Z')
    o += dot(cx - 12 * k, cy + 2 * k, 3.2) + dot(cx + 12 * k, cy + 2 * k, 3.2)
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, 6, 3.5)
    if mouth == 'smile':
        o += s('path', d=f'M{X(-6)} {Y(16)} Q{X(0)} {Y(21)} {X(6)} {Y(16)}', stroke_width=2.5)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{X(-8)} {Y(14)} Q{X(0)} {Y(28)} {X(8)} {Y(14)}Z', stroke_width=2.5)
    else:
        o += f'<circle cx="{_f(cx)}" cy="{_f(cy + 18 * k)}" r="3.5" fill="#c0504d" stroke-width="2.5"/>'
    return o


def body(cx, top, bot, color, w=34):
    return z('path', color, d=f'M{cx-w} {bot} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bot}Z')


def arm(a, b, color, hand=SK, r=8):
    d = f'M{a[0]} {a[1]} L{b[0]} {b[1]}'
    return (s('path', d=d, stroke_width=12) + s('path', d=d, stroke=color, stroke_width=6)
            + z('circle', hand, cx=b[0], cy=b[1], r=r))


def glasses(cx, cy, r=8, gap=12):
    return (s('circle', cx=cx - gap, cy=cy, r=r, stroke_width=2.5) + s('circle', cx=cx + gap, cy=cy, r=r, stroke_width=2.5)
            + s('path', d=f'M{cx-gap+r} {cy} L{cx+gap-r} {cy}', stroke_width=2.5))


def face_dots(cx, cy, k=1.0):
    return (dot(cx - 10 * k, cy) + dot(cx + 10 * k, cy) + cheeks(cx - 17 * k, cx + 17 * k, cy + 9 * k, 5, 3)
            + s('path', d=f'M{_f(cx-4*k)} {_f(cy+8*k)} Q{cx} {_f(cy+12*k)} {_f(cx+4*k)} {_f(cy+8*k)}', stroke_width=2.5))


# 1. tutor
t = (body(58, 124, 168, '#8fc7e8', 28) + sface(58, 98, 28, '#2b2220', 'o')
     + body(142, 108, 168, '#9ccf7a', 32) + sface(142, 76, 31, '#5a4033', 'smile') + glasses(142, 77, 7, 11)
     + z('rect', '#d9a66b', x=22, y=150, width=156, height=30, rx=4)
     + z('path', '#ffffff', d='M54 156 L62 134 L100 140 L100 162Z') + z('path', '#ffffff', d='M100 162 L100 140 L134 134 L142 156Z')
     + s('path', d='M68 142 L92 146 M66 149 L90 153 M108 146 L128 142 M110 153 L132 149', stroke='#8fc7e8', stroke_width=2)
     + arm((122, 120), (112, 146), '#9ccf7a', r=7))
ITEMS['tutor'] = t

# 2. study-group
sg = (body(100, 102, 150, '#f5b971', 28) + sface(100, 74, 27, '#5a4033', 'smile')
      + body(48, 118, 160, '#8fc7e8', 26) + sface(48, 92, 26, '#2b2220', 'o')
      + body(152, 118, 160, '#f6a6b8', 26) + sface(152, 92, 26, '#c9a36b', 'smile')
      + z('rect', '#d9a66b', x=22, y=140, width=156, height=40, rx=5)
      + z('path', '#ffffff', d='M64 168 L70 148 L100 152 L100 172Z') + z('path', '#ffffff', d='M100 172 L100 152 L130 148 L136 168Z')
      + s('path', d='M74 156 L94 159 M72 162 L94 165 M106 159 L126 156 M106 165 L128 162', stroke='#8fc7e8', stroke_width=2)
      + z('circle', SK, cx=72, cy=146, r=7) + z('circle', SK, cx=128, cy=146, r=7)
      + z('rect', '#ffc94d', x=146, y=158, width=26, height=7, rx=2))
ITEMS['study-group'] = sg

# 3. highlighters
hl = ''
for cx, cy, deg, c in ((58, 104, -100, '#f6a6b8'), (100, 98, -90, '#ffe27a'), (142, 104, -80, '#9ccf7a')):
    P = _frame(cx, cy, deg)
    hl += (z('path', c, d=_poly([P(-62, -10), P(-50, -15), P(30, -15), P(30, 15), P(-50, 15), P(-62, 10)]))
           + s('path', '#ffffff', d=_poly([P(-36, -7), P(18, -7), P(18, 7), P(-36, 7)]), stroke_width=2)
           + z('path', c, d=_poly([P(28, -17), P(58, -17), P(64, -10), P(64, 10), P(58, 17), P(28, 17)]))
           + s('path', d=_line(P(34, -10), P(60, -10)), stroke_width=2.5))
hl += f'<g>{dot(93, 80, 3)}{dot(107, 80, 3)}</g>' + cheeks(88, 112, 88, 4, 2.5) + s('path', d='M97 88 Q100 91 103 88', stroke_width=2)
hl += (s('path', d='M36 176 L74 176', stroke='#f6a6b8', stroke_width=9) + s('path', d='M82 176 L120 176', stroke='#ffe27a', stroke_width=9)
       + s('path', d='M128 176 L166 176', stroke='#9ccf7a', stroke_width=9))
ITEMS['highlighters'] = hl

# 4. bookmark
bm = (s('path', d='M120 40 Q128 26 140 30', stroke_width=2.5)
      + z('path', '#e04b5a', d='M140 30 Q148 34 146 46 L136 46 Q134 34 140 30Z')
      + z('rect', '#f5d58a', x=108, y=34, width=24, height=46, rx=3) + s('circle', '#ffffff', cx=120, cy=42, r=3.5, stroke_width=2)
      + z('rect', '#f4f4f0', x=62, y=60, width=94, height=116, rx=4)
      + s('path', d='M152 70 L152 168 M146 66 L146 172', stroke='#b9a99c', stroke_width=2)
      + z('rect', '#8fb3e0', x=46, y=54, width=98, height=124, rx=6)
      + s('path', d='M60 54 L60 178', stroke_width=2.5)
      + s('rect', '#ffffff', x=74, y=74, width=56, height=24, rx=4, stroke_width=2.5)
      + face_dots(102, 128))
ITEMS['bookmark'] = bm

# 5. teacher-grading
tg = (body(100, 106, 150, '#f6a6b8', 36) + face(100, 70, SK, '#5a4033', 'smile')
      + z('rect', '#d9a66b', x=20, y=132, width=160, height=48, rx=5)
      + z('rect', '#ffffff', x=28, y=150, width=42, height=24, rx=2) + z('rect', '#ffffff', x=30, y=144, width=42, height=24, rx=2)
      + z('rect', '#ffffff', x=26, y=138, width=42, height=24, rx=2)
      + z('rect', '#ffffff', x=80, y=138, width=50, height=38, rx=2)
      + s('path', d='M86 148 L90 152 L96 144 M86 162 L90 166 L96 158', stroke='#e04b5a', stroke_width=2.5)
      + s('path', d='M102 148 L122 148 M102 162 L122 162', stroke='#b9a99c', stroke_width=2)
      + s('path', d='M128 168 L148 140', stroke_width=9) + s('path', d='M128 168 L148 140', stroke='#e04b5a', stroke_width=4)
      + z('circle', SK, cx=148, cy=140, r=8))
ITEMS['teacher-grading'] = tg

# 6. principal
pr = (body(100, 102, 150, '#5b6b7a', 38)
      + s('path', '#ffffff', d='M88 104 L100 128 L112 104Z', stroke_width=2.5)
      + z('path', '#e04b5a', d='M96 108 L104 108 L106 128 L100 134 L94 128Z')
      + face(100, 66, SK, '#e8e1d8', 'smile') + glasses(100, 68, 8, 12)
      + s('path', '#e8e1d8', d='M90 79 Q100 74 110 79 Q104 83 100 80 Q96 83 90 79Z', stroke_width=2)
      + s('path', d='M110 122 L124 104', stroke_width=3) + z('ellipse', '#5b6b7a', cx=127, cy=99, rx=6, ry=8)
      + z('rect', '#9a6a3f', x=40, y=122, width=120, height=12, rx=3)
      + z('path', '#d9a66b', d='M50 134 L150 134 L140 180 L60 180Z')
      + s('circle', '#f5d58a', cx=100, cy=156, r=10, stroke_width=2.5)
      + z('circle', SK, cx=62, cy=122, r=8) + z('circle', SK, cx=138, cy=122, r=8))
ITEMS['principal'] = pr

# 7. school-gate
gt = (z('circle', '#7cc4a0', cx=40, cy=104, r=18) + z('circle', '#7cc4a0', cx=160, cy=104, r=18)
      + z('rect', '#f6e0c4', x=86, y=28, width=28, height=34, rx=2) + s('circle', '#ffffff', cx=100, cy=44, r=9)
      + s('path', d='M100 44 L100 38 M100 44 L104 46', stroke_width=2)
      + z('rect', '#f6e0c4', x=44, y=60, width=112, height=72, rx=2)
      + s('path', '#e8735a', d='M40 60 L160 60 L156 52 L44 52Z', stroke_width=2.5)
      + ''.join(s('rect', '#8fc7e8', x=x, y=y, width=14, height=12, rx=2, stroke_width=2.5) for x in (54, 76, 110, 132) for y in (70, 94))
      + s('rect', '#8b6b4f', x=90, y=108, width=20, height=24, rx=2, stroke_width=2.5)
      + z('rect', '#9ccf7a', x=22, y=132, width=156, height=48, rx=3)
      + s('path', '#f5d58a', d='M90 132 L110 132 L130 180 L70 180Z', stroke_width=2.5)
      + s('path', d='M46 140 L82 140 M46 176 L82 176 ' + ' '.join(f'M{x} 140 L{x} 176' for x in (52, 60, 68, 76)), stroke_width=3)
      + s('path', d='M154 140 L120 140 M154 176 L120 176 ' + ' '.join(f'M{x} 140 L{x} 176' for x in (126, 134, 142, 150)), stroke_width=3)
      + z('rect', '#b9a99c', x=24, y=118, width=22, height=62, rx=2) + z('rect', '#b9a99c', x=20, y=110, width=30, height=10, rx=2)
      + z('rect', '#b9a99c', x=154, y=118, width=22, height=62, rx=2) + z('rect', '#b9a99c', x=150, y=110, width=30, height=10, rx=2))
ITEMS['school-gate'] = gt

# 8. clay
cl = (z('rect', '#8fb3e0', x=24, y=128, width=150, height=48, rx=8)
      + z('rect', '#e8735a', x=34, y=126, width=44, height=20, rx=5) + z('rect', '#9ccf7a', x=38, y=106, width=38, height=20, rx=5)
      + z('rect', '#ffe27a', x=42, y=86, width=32, height=20, rx=5)
      + s('path', d='M98 104 L92 88 M108 104 L114 88', stroke_width=2.5) + dot(92, 87, 3.5) + dot(114, 87, 3.5)
      + z('path', '#f5b971', d='M90 148 Q86 104 103 102 Q120 104 118 134 L160 134 Q174 140 166 150Z')
      + z('circle', '#a98bd0', cx=136, cy=112, r=26)
      + s('path', d='M136 112 Q144 110 142 118 Q134 126 126 116 Q124 102 138 100 Q156 102 152 120', stroke_width=2.5)
      + dot(98, 116, 3) + dot(110, 116, 3) + cheeks(94, 114, 123, 4, 2.5) + s('path', d='M101 123 Q104 126 107 123', stroke_width=2)
      + z('path', '#f6a6b8', d='M40 162 Q60 154 80 162 Q96 168 112 160 L113 168 Q96 176 80 170 Q60 162 40 170Z'))
ITEMS['clay'] = cl

# 9. origami-class
og = ''
for cx, cy, deg, c in ((64, 150, -14, '#8fc7e8'), (136, 152, 16, '#9ccf7a'), (100, 156, 2, '#ffe27a')):
    P = _frame(cx, cy, deg)
    og += z('path', c, d=_poly([P(-26, -20), P(26, -20), P(26, 20), P(-26, 20)]))
og += (z('path', '#f6a6b8', d='M98 122 L122 40 L128 120Z')
       + z('path', '#f07a8a', d='M126 126 L160 72 L114 120Z')
       + z('path', '#f07a8a', d='M76 126 L48 72 L88 120Z')
       + z('path', '#f07a8a', d='M48 72 L38 86 L54 82Z')
       + z('path', '#f07a8a', d='M60 128 L100 110 L140 128 L100 146Z')
       + z('path', '#f6a6b8', d='M90 126 L80 44 L114 122Z')
       + s('path', d='M60 128 L140 128', stroke_width=2))
ITEMS['origami-class'] = og


def note(x, y):
    return (f'<ellipse cx="{x}" cy="{y}" rx="6" ry="4.5" fill="{OUT}" stroke="none" transform="rotate(-20 {x} {y})"/>'
            + s('path', d=f'M{x+5} {y-1} L{x+5} {y-24} Q{x+12} {y-18} {x+14} {y-12}', stroke_width=2.5))


# 10. piano-class
pn = (z('rect', '#9a6a3f', x=34, y=52, width=116, height=112, rx=4)
      + z('rect', '#9a6a3f', x=28, y=44, width=128, height=12, rx=3)
      + s('rect', '#ffffff', x=60, y=62, width=64, height=30, rx=2, stroke_width=2.5)
      + s('path', d='M66 72 L118 72 M66 82 L118 82', stroke='#b9a99c', stroke_width=1.5)
      + z('rect', '#8b6b4f', x=28, y=98, width=128, height=10, rx=2)
      + z('rect', '#ffffff', x=30, y=108, width=124, height=22, rx=2)
      + s('path', d=' '.join(f'M{x} 108 L{x} 130' for x in range(41, 154, 11)), stroke_width=2)
      + ''.join(s('rect', OUT, x=x - 3, y=108, width=7, height=13, stroke_width=1) for x in (41, 52, 74, 85, 96, 118, 129, 140))
      + s('rect', '#8b6b4f', x=50, y=136, width=84, height=22, rx=3, stroke_width=2.5)
      + z('rect', '#9a6a3f', x=40, y=164, width=10, height=16, rx=2) + z('rect', '#9a6a3f', x=134, y=164, width=10, height=16, rx=2)
      + note(166, 76) + note(170, 128))
ITEMS['piano-class'] = pn

# 11. pe-class
pe = (z('rect', SK, x=78, y=154, width=12, height=18, rx=4) + z('rect', SK, x=106, y=154, width=12, height=18, rx=4)
      + z('ellipse', '#f4f4f0', cx=82, cy=174, rx=11, ry=6) + z('ellipse', '#f4f4f0', cx=114, cy=174, rx=11, ry=6)
      + z('path', '#e04b5a', d='M64 140 L132 140 L134 160 L104 160 L98 152 L92 160 L62 160Z')
      + body(98, 104, 146, '#ffffff', 36)
      + arm((68, 122), (50, 138), '#ffffff')
      + face(98, 70, SK, '#2b2220', 'open')
      + s('path', d='M65 56 Q98 44 131 56', stroke='#e04b5a', stroke_width=7)
      + z('circle', '#e8735a', cx=152, cy=112, r=24)
      + s('path', d='M130 104 Q152 116 174 104 M146 88 Q140 112 148 136', stroke_width=2.5)
      + arm((126, 124), (136, 124), '#ffffff')
      + s('path', d='M152 74 L158 66 M168 80 L176 74 M136 76 L136 68', stroke_width=2.5)
      + s('path', d='M30 182 L170 182', stroke_width=2))
ITEMS['pe-class'] = pe

# 12. swimming-class
cap1 = z('path', '#e8735a', d='M32 92 Q30 56 66 56 Q102 56 100 92 Q66 72 32 92Z')
cap2 = z('path', '#ffe27a', d='M102 100 Q100 64 136 64 Q172 64 170 100 Q136 80 102 100Z')
sw = (face(66, 94, SK, '#2b2220', 'open') + cap1
      + s('circle', '#8fc7e8', cx=54, cy=70, r=6, stroke_width=2.5) + s('circle', '#8fc7e8', cx=78, cy=70, r=6, stroke_width=2.5)
      + s('path', d='M60 70 L72 70', stroke_width=2.5)
      + face(136, 100, SK, '#5a4033', 'smile') + cap2
      + z('path', '#8fc7e8', d='M22 126 Q38 118 54 126 Q70 134 86 126 Q102 118 118 126 Q134 134 150 126 Q166 118 178 126 L178 176 Q178 180 174 180 L26 180 Q22 180 22 176Z')
      + s('path', d='M24 160 L176 160', stroke_width=2.5)
      + ''.join(s('circle', '#e8735a' if i % 2 == 0 else '#ffffff', cx=x, cy=160, r=7, stroke_width=2.5) for i, x in enumerate(range(34, 176, 18)))
      + s('path', d='M40 140 Q50 136 60 140 M120 144 Q130 140 140 144', stroke='#ffffff', stroke_width=2.5)
      + s('path', '#ffffff', d='M30 112 Q26 104 30 98 Q34 104 30 112Z', stroke_width=2)
      + s('path', '#ffffff', d='M172 108 Q168 100 172 94 Q176 100 172 108Z', stroke_width=2))
ITEMS['swimming-class'] = sw

# 13. lunch-time-kids
ln = (body(58, 110, 150, '#8fc7e8', 32) + face(58, 74, SK, '#2b2220', 'open')
      + body(142, 110, 150, '#f6a6b8', 32) + face(142, 74, SK, '#c9a36b', 'smile')
      + z('rect', '#d9a66b', x=20, y=136, width=160, height=44, rx=5)
      + z('rect', '#c9d3db', x=26, y=144, width=66, height=30, rx=4) + z('rect', '#c9d3db', x=108, y=144, width=66, height=30, rx=4)
      + z('path', '#ffffff', d='M32 154 L58 154 Q58 170 45 170 Q32 170 32 154Z') + z('path', '#f5b971', d='M62 154 L86 154 Q86 170 74 170 Q62 170 62 154Z')
      + z('path', '#ffffff', d='M114 154 L140 154 Q140 170 127 170 Q114 170 114 154Z') + z('path', '#f5b971', d='M144 154 L168 154 Q168 170 156 170 Q144 170 144 154Z')
      + z('rect', '#ffffff', x=92, y=118, width=16, height=24, rx=2) + z('path', '#8fc7e8', d='M92 118 L96 108 L104 108 L108 118Z')
      + s('path', d='M36 132 L40 110', stroke_width=3) + z('ellipse', '#c9d3db', cx=41, cy=106, rx=5, ry=7)
      + z('circle', SK, cx=36, cy=134, r=8)
      + z('circle', SK, cx=164, cy=134, r=8))
ITEMS['lunch-time-kids'] = ln

# 14. ruler
P = _frame(100, 104, -30)
ru = (z('path', '#8fc7e8', d=_poly([P(-74, -20), P(74, -20), P(74, 20), P(-74, 20)]))
      + s('path', d=' '.join(_line(P(u, -20), P(u, -20 + (12 if (u + 64) % 32 == 0 else 7))) for u in range(-64, 66, 8)), stroke_width=2)
      + s('circle', '#ffffff', cx=_f(P(64, 8)[0]), cy=_f(P(64, 8)[1]), r=4, stroke_width=2))
c = P(-6, 6)
ru += face_dots(c[0], c[1] - 2, 0.9)
ITEMS['ruler'] = ru

# 15. notebook-stack
nk = ''
for i, (col, off) in enumerate((('#e8735a', 0), ('#8fc7e8', 6), ('#9ccf7a', -4), ('#f6a6b8', 4))):
    x = 34 + off; y = 162 - 16 * i
    nk += (z('rect', col, x=x, y=y, width=128, height=16, rx=3)
           + s('rect', '#ffffff', x=x + 8, y=y + 5, width=116, height=6, rx=1, stroke_width=1.5))
nk += (z('path', '#ffc94d', d='M38 114 L166 114 L150 72 L56 72Z')
       + s('path', d='M42 114 L60 72', stroke_width=2.5)
       + s('rect', '#ffffff', x=88, y=82, width=40, height=18, rx=3, stroke_width=2.5)
       + s('path', d='M94 89 L122 89 M94 94 L114 94', stroke='#b9a99c', stroke_width=1.5))
P = _frame(150, 70, -160)
nk += (z('path', '#e04b5a', d=_poly([P(-30, -5), P(26, -5), P(26, 5), P(-30, 5)]))
       + z('path', '#f6e0c4', d=_poly([P(26, -5), P(38, 0), P(26, 5)])))
ITEMS['notebook-stack'] = nk

# 16. backpack-yellow-cover
bp = (s('path', d='M86 48 Q86 30 100 30 Q114 30 114 48', stroke_width=6) + s('path', d='M86 48 Q86 30 100 30 Q114 30 114 48', stroke='#e04b5a', stroke_width=2)
      + z('rect', '#e04b5a', x=48, y=46, width=104, height=134, rx=22)
      + z('path', '#ffe27a', d='M42 64 Q42 42 64 42 L136 42 Q158 42 158 64 L158 150 Q100 164 42 150Z')
      + s('path', '#f4f4f0', d='M42 120 Q100 128 158 120 L158 132 Q100 140 42 132Z', stroke_width=2.5)
      + z('rect', '#5b6b7a', x=92, y=152, width=16, height=18, rx=4)
      + dot(86, 88) + dot(114, 88) + cheeks(78, 122, 98, 6, 3.5) + s('path', d='M94 98 Q100 104 106 98', stroke_width=2.5)
      + ''.join(s('path', '#8fc7e8', d=f'M{x} {y} Q{x-5} {y+10} {x} {y+12} Q{x+5} {y+10} {x} {y}Z', stroke_width=2)
                for x, y in ((28, 40), (172, 56), (26, 110), (174, 126), (30, 160))))
ITEMS['backpack-yellow-cover'] = bp

# 17. stopwatch-class
P = _frame(100, 98, -45)
st = (z('rect', '#d9a66b', x=20, y=150, width=160, height=30, rx=4)
      + z('path', '#5b6b7a', d=_poly([P(50, -6), P(62, -6), P(62, 6), P(50, 6)]))
      + z('rect', '#5b6b7a', x=95, y=36, width=10, height=12) + z('rect', '#5b6b7a', x=88, y=26, width=24, height=12, rx=4)
      + z('circle', '#8fc7e8', cx=100, cy=98, r=52)
      + s('circle', '#ffffff', cx=100, cy=98, r=40)
      + s('path', d=' '.join(_line((100 + 34 * math.cos(a), 98 + 34 * math.sin(a)), (100 + (28 if k % 3 == 0 else 31) * math.cos(a), 98 + (28 if k % 3 == 0 else 31) * math.sin(a)))
                             for k, a in ((k, math.radians(k * 30)) for k in range(12))), stroke_width=2)
      + s('path', d='M100 98 L100 70', stroke='#e04b5a', stroke_width=3) + s('path', d='M100 98 L118 106', stroke_width=3)
      + dot(100, 98, 4)
      + s('path', d='M150 168 L174 160', stroke_width=7) + s('path', d='M150 168 L174 160', stroke='#ffc94d', stroke_width=3))
ITEMS['stopwatch-class'] = st

# 18. art-class
ac = (z('path', '#d9a66b', d='M44 180 L54 180 L104 34 L96 34Z') + z('path', '#d9a66b', d='M156 180 L146 180 L96 34 L104 34Z')
      + z('rect', '#d9a66b', x=95, y=120, width=10, height=60)
      + z('rect', '#ffffff', x=46, y=44, width=108, height=84, rx=2)
      + s('rect', '#8fc7e8', x=54, y=52, width=92, height=68, stroke_width=2)
      + s('path', '#9ccf7a', d='M54 104 Q78 84 100 100 Q122 86 146 98 L146 120 L54 120Z', stroke_width=2)
      + s('circle', '#ffc94d', cx=124, cy=72, r=10, stroke_width=2)
      + s('path', '#f6a6b8', d='M74 98 Q70 90 76 88 Q82 90 78 98 Z', stroke_width=2)
      + z('rect', '#9a6a3f', x=38, y=128, width=124, height=10, rx=3)
      + z('path', '#f6e0c4', d='M118 160 Q120 140 146 142 Q176 144 176 162 Q174 178 150 178 Q130 178 132 170 Q140 164 128 164 Q118 166 118 160Z')
      + dot(140, 152, 4.5, '#e04b5a') + dot(156, 150, 4.5, '#8fc7e8') + dot(166, 162, 4.5, '#ffc94d') + dot(152, 168, 4.5, '#9ccf7a'))
ITEMS['art-class'] = ac

# 19. calligraphy-set
cg = (z('rect', '#5b6b7a', x=30, y=60, width=72, height=116, rx=12)
      + s('rect', '#c9d3db', x=40, y=88, width=52, height=78, rx=8, stroke_width=2.5)
      + s('path', OUT, d='M40 92 Q40 70 66 70 Q92 70 92 92 Q66 86 40 92Z', stroke_width=2.5)
      + z('rect', '#2b2220', x=52, y=116, width=26, height=44, rx=3)
      + s('rect', '#f5d58a', x=56, y=124, width=18, height=14, rx=2, stroke_width=2))
P = _frame(146, 104, 112)
cg += (z('path', '#f5d58a', d=_poly([P(-72, -6), P(24, -6), P(24, 6), P(-72, 6)]))
       + s('path', d=_line(P(-40, -6), P(-40, 6)) + ' ' + _line(P(-8, -6), P(-8, 6)), stroke_width=2.5)
       + z('path', '#f4f4f0', d=f'M{_f(P(24,-8)[0])} {_f(P(24,-8)[1])} Q{_f(P(44,-12)[0])} {_f(P(44,-12)[1])} {_f(P(54,-4)[0])} {_f(P(54,-4)[1])} '
                                 f'L{_f(P(54,4)[0])} {_f(P(54,4)[1])} Q{_f(P(44,12)[0])} {_f(P(44,12)[1])} {_f(P(24,8)[0])} {_f(P(24,8)[1])}Z')
       + s('path', '#2b2220', d=f'M{_f(P(50,-6)[0])} {_f(P(50,-6)[1])} Q{_f(P(66,-4)[0])} {_f(P(66,-4)[1])} {_f(P(72,0)[0])} {_f(P(72,0)[1])} '
                                f'Q{_f(P(66,4)[0])} {_f(P(66,4)[1])} {_f(P(50,6)[0])} {_f(P(50,6)[1])}Z', stroke_width=2.5))
cg += s('path', '#2b2220', d='M124 172 Q120 166 124 162 Q128 166 124 172Z', stroke_width=2)
ITEMS['calligraphy-set'] = cg

# 20. chalk-eraser
ce = (z('path', '#8fb3e0', d='M30 84 L130 84 L156 60 L56 60Z')
      + s('path', d='M62 78 L132 78 M70 70 L140 70', stroke_width=2)
      + z('path', '#8fb3e0', d='M130 84 L156 60 L156 104 L130 128Z')
      + z('rect', '#8fb3e0', x=30, y=84, width=100, height=30)
      + z('path', '#5b6b7a', d='M30 114 L130 114 L130 128 L30 128Z') + s('path', '#5b6b7a', d='M130 114 L156 90 L156 104 L130 128Z')
      + dot(68, 98) + dot(92, 98) + cheeks(60, 100, 106, 5, 3) + s('path', d='M76 106 Q80 110 84 106', stroke_width=2.5)
      + z('rect', '#ffffff', x=34, y=146, width=60, height=14, rx=7)
      + z('rect', '#f6a6b8', x=104, y=142, width=56, height=14, rx=7)
      + z('rect', '#ffe27a', x=70, y=164, width=58, height=14, rx=7)
      + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=r, stroke_width=1.5) for x, y, r in ((166, 132, 3), (172, 120, 2.5), (24, 140, 2.5), (160, 172, 3))))
ITEMS['chalk-eraser'] = ce
