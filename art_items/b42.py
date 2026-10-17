from art import z, s, dot, cheeks, face, OUT, CH
import math

ITEMS = {}


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


def _smile(x, y, w=4):
    return s('path', d=f'M{x-w} {y} Q{x} {y+4} {x+w} {y}', stroke_width=2.5)


def _kao(x, y, gap=10, r=3.5):
    return dot(x - gap, y, r) + dot(x + gap, y, r) + cheeks(x - gap - 7, x + gap + 7, y + 8, 5, 3) + _smile(x, y + 8)


def _pencil(P, L, col, wood='#f6e0c4', w=8):
    """u=0 が後端, u=L が芯先"""
    return (z('path', col, d=_poly([P(0, -w), P(L, -w), P(L, w), P(0, w)]))
            + z('path', wood, d=_poly([P(L, -w), P(L + 18, 0), P(L, w)]))
            + s('path', col, d=_poly([P(L + 11, -3), P(L + 18, 0), P(L + 11, 3)]), stroke_width=2))


# 1. eraser
er = (s('ellipse', '#f6a6b8', cx=150, cy=168, rx=5, ry=3.5, stroke_width=2) + s('ellipse', '#f6a6b8', cx=166, cy=162, rx=4, ry=3, stroke_width=2) + s('ellipse', '#f6a6b8', cx=158, cy=176, rx=3.5, ry=2.5, stroke_width=2)
      + z('rect', '#f6a6b8', x=30, y=70, width=140, height=76, rx=12)
      + z('rect', '#8fb3e0', x=104, y=64, width=60, height=88, rx=4)
      + s('path', d='M114 64 L114 152', stroke_width=2)
      + s('rect', '#ffffff', x=124, y=88, width=30, height=40, rx=4, stroke_width=2.5)
      + _kao(68, 104, 12))
ITEMS['eraser'] = er

# 2. crayons
cr = ''
for i, (c, top) in enumerate((('#e04b5a', 58), ('#ffc94d', 44), ('#7cc4a0', 36), ('#8fb3e0', 48), ('#a98bd0', 62))):
    x = 32 + i * 28
    cr += (z('path', c, d=f'M{x+4} {top+18} L{x+8} {top} Q{x+12} {top-4} {x+16} {top} L{x+20} {top+18}Z')
           + z('rect', c, x=x, y=top + 18, width=24, height=176 - top - 18, rx=3)
           + s('rect', '#ffffff', x=x, y=top + 40, width=24, height=60, stroke_width=2.5)
           + s('path', d=f'M{x+4} {top+52} L{x+20} {top+52} M{x+4} {top+88} L{x+20} {top+88}', stroke=c, stroke_width=3))
cr += dot(94, 112, 3) + dot(106, 112, 3) + cheeks(91, 109, 120, 3, 2) + _smile(100, 119, 3)
ITEMS['crayons'] = cr

# 3. colored-pencils (in a cup)
cp = ''
for ang, col, L in ((-112, '#e04b5a', 92), (-98, '#ffc94d', 104), (-84, '#7cc4a0', 100), (-70, '#8fb3e0', 90), (-124, '#a98bd0', 76), (-58, '#f5b971', 78)):
    P = _frame(100, 168, ang)
    cp += _pencil(P, L, col, w=7)
cp += (z('path', '#f5d58a', d='M56 110 L144 110 L136 180 L64 180Z')
       + s('path', d='M60 124 L140 124', stroke_width=2)
       + _kao(100, 146, 12))
ITEMS['colored-pencils'] = cp

# 4. scissors
sc = ''
for ang_b, ang_h in ((-108, 66), (-72, 114)):
    Pb = _frame(100, 104, ang_b)
    sc += z('path', '#c9d3db', d=_poly([Pb(-8, -8), Pb(36, -9), Pb(78, -1), Pb(80, 0), Pb(-8, 7)]))
for ang_b, ang_h in ((-108, 66), (-72, 114)):
    Ph = _frame(100, 104, ang_h)
    cx, cy = Ph(50, 0)
    sc += (z('path', '#e8735a', d=_poly([Ph(4, -7), Ph(36, -7), Ph(36, 7), Ph(4, 7)]))
           + z('ellipse', '#e8735a', cx=_f(cx), cy=_f(cy), rx=19, ry=17)
           + s('ellipse', '#ffffff', cx=_f(cx), cy=_f(cy), rx=9, ry=8))
sc += z('circle', '#b9a99c', cx=100, cy=104, r=7) + dot(100, 104, 2.5)
ITEMS['scissors'] = sc

# 5. glue (glue stick with cap)
gl = (z('path', '#f4f4f0', d='M68 88 L68 60 Q68 48 90 48 Q112 48 112 60 L112 88Z')
      + z('rect', '#7cc4b0', x=58, y=84, width=64, height=92, rx=8)
      + s('rect', '#ffffff', x=58, y=108, width=64, height=40, stroke_width=2.5)
      + s('path', d='M58 160 L122 160', stroke_width=2)
      + _kao(90, 124, 11)
      + z('path', '#7cc4b0', d='M134 176 L134 122 Q134 112 144 112 L164 112 Q174 112 174 122 L174 176Z')
      + s('path', d='M134 130 L174 130', stroke_width=2))
ITEMS['glue'] = gl

# 6. watercolors
wc = z('rect', '#f4f4f0', x=24, y=92, width=152, height=76, rx=8)
for i, c in enumerate(('#e04b5a', '#ffc94d', '#9ccf7a', '#8fc7e8', '#f6a6b8', '#f5b971', '#7cc4a0', '#a98bd0')):
    x = 34 + (i % 4) * 34
    y = 102 + (i // 4) * 32
    wc += s('rect', c, x=x, y=y, width=28, height=24, rx=5, stroke_width=2.5)
P = _frame(112, 60, -26)
wc += (z('path', '#d9a66b', d=_poly([P(-22, -5), P(56, -4), P(60, 0), P(56, 4), P(-22, 5)]))
       + z('path', '#c9d3db', d=_poly([P(-36, -6), P(-22, -6), P(-22, 6), P(-36, 6)]))
       + z('path', '#8fc7e8', d=f'M{_f(P(-36,-7)[0])} {_f(P(-36,-7)[1])} Q{_f(P(-50,-9)[0])} {_f(P(-50,-9)[1])} {_f(P(-62,0)[0])} {_f(P(-62,0)[1])} Q{_f(P(-50,9)[0])} {_f(P(-50,9)[1])} {_f(P(-36,7)[0])} {_f(P(-36,7)[1])}Z')
       + z('path', '#8fc7e8', d='M44 128 Q40 136 44 140 Q48 136 44 128Z'))
wc = wc.replace(z('path', '#8fc7e8', d='M44 128 Q40 136 44 140 Q48 136 44 128Z'), '')
ITEMS['watercolors'] = wc

# 7. pencil-sharpener
P = _frame(18, 112, 0)
ps = (_pencil(P, 56, '#ffc94d', w=9)
      + z('rect', '#8fc7e8', x=66, y=76, width=80, height=74, rx=10)
      + s('rect', '#c9d3db', x=72, y=70, width=50, height=10, rx=2, stroke_width=2.5)
      + dot(80, 76, 2) + dot(114, 76, 2)
      + s('ellipse', '#5b6b7a', cx=66, cy=112, rx=6, ry=13, stroke_width=2.5)
      + _kao(112, 112, 12)
      + z('path', '#f6e0c4', d='M84 176 Q84 162 96 162 Q104 162 104 170 Q104 176 98 176Z')
      + z('path', '#f6e0c4', d='M112 176 Q114 164 126 166 Q134 168 132 176Z')
      + s('path', d='M88 170 Q94 166 100 172 M118 172 Q122 168 128 172', stroke='#ffc94d', stroke_width=2.5))
ITEMS['pencil-sharpener'] = ps

# 8. pencil-case
P = _frame(70, 104, -100)
pc = _pencil(P, 44, '#e04b5a', w=8)
pc += (z('rect', '#f5d58a', x=96, y=40, width=26, height=66, rx=2)
       + s('path', d='M96 56 L106 56 M96 70 L110 70 M96 84 L106 84 M96 98 L110 98', stroke_width=2))
pc += (z('path', '#a98bd0', d='M28 106 Q28 88 46 88 L154 88 Q172 88 172 106 L168 160 Q166 176 150 176 L50 176 Q34 176 32 160Z')
       + s('path', d='M36 98 L164 98', stroke_width=2.5)
       + ''.join(s('path', d=f'M{x} 95 L{x} 101', stroke_width=2) for x in range(42, 160, 8))
       + z('path', '#c9d3db', d='M152 96 L160 96 L162 120 Q156 126 150 120Z')
       + _kao(100, 134, 14))
ITEMS['pencil-case'] = pc

# 9. drawing-compass
dc = ''
Pl = _frame(100, 44, 106.5)
dc += (z('path', '#c9d3db', d=_poly([Pl(0, -7), Pl(116, -5), Pl(116, 5), Pl(0, 7)]))
       + s('path', d=_line(Pl(116, 0), Pl(134, 0)), stroke_width=3))
Pr = _frame(100, 44, 72.4)
dc += (z('path', '#c9d3db', d=_poly([Pr(0, -7), Pr(82, -5), Pr(82, 5), Pr(0, 7)]))
       + z('path', '#ffc94d', d=_poly([Pr(70, -7), Pr(112, -7), Pr(112, 7), Pr(70, 7)]))
       + z('path', '#f6e0c4', d=_poly([Pr(112, -7), Pr(128, 0), Pr(112, 7)]))
       + z('path', '#5b6b7a', d=_poly([Pr(80, -9), Pr(90, -9), Pr(90, 9), Pr(80, 9)])))
dc += (z('rect', '#e8735a', x=94, y=18, width=12, height=18, rx=3)
       + z('circle', '#e8735a', cx=100, cy=44, r=12) + dot(100, 44, 3)
       + s('path', d='M40 176 Q94 194 150 178', stroke='#8fb3e0', stroke_width=3))
ITEMS['drawing-compass'] = dc

# 10. globe-desk
gd = (z('path', '#c9a36b', d='M94 140 L106 140 L108 164 L92 164Z')
      + z('ellipse', '#8b6b4f', cx=100, cy=170, rx=40, ry=10)
      + z('circle', '#8fc7e8', cx=100, cy=86, r=50)
      + s('path', '#9ccf7a', d='M70 58 Q90 46 104 62 Q100 84 82 84 Q62 80 70 58Z', stroke_width=2.5)
      + s('path', '#9ccf7a', d='M112 96 Q136 88 142 108 Q132 128 116 122 Q104 110 112 96Z', stroke_width=2.5)
      + s('path', '#9ccf7a', d='M62 100 Q78 98 82 112 Q76 124 64 116Z', stroke_width=2.5)
      + s('path', d='M100 28 A58 58 0 0 0 100 144', stroke_width=10)
      + s('path', d='M100 28 A58 58 0 0 0 100 144', stroke='#c9a36b', stroke_width=4)
      + dot(100, 30, 4) + dot(100, 142, 4))
ITEMS['globe-desk'] = gd

# 11. abacus
ab = (z('rect', '#d9a66b', x=26, y=44, width=148, height=120, rx=8)
      + s('rect', '#ffffff', x=38, y=56, width=124, height=96, rx=3))
cols = ('#e04b5a', '#ffc94d', '#7cc4a0', '#8fb3e0', '#a98bd0')
shifts = (3, 1, 4, 2, 0)
for i, (c, n) in enumerate(zip(cols, shifts)):
    y = 66 + i * 19
    ab += s('path', d=f'M38 {y} L162 {y}', stroke_width=2)
    xs = [48 + k * 13 for k in range(n)] + [152 - k * 13 for k in range(5 - n)]
    for x in xs:
        ab += s('ellipse', c, cx=x, cy=y, rx=6.5, ry=8, stroke_width=2.5)
ab += z('rect', '#9a6a3f', x=36, y=164, width=14, height=14, rx=3) + z('rect', '#9a6a3f', x=150, y=164, width=14, height=14, rx=3)
ITEMS['abacus'] = ab

# 12. test-tubes
tt = (z('rect', '#d9a66b', x=34, y=96, width=10, height=80, rx=2)
      + z('rect', '#d9a66b', x=156, y=96, width=10, height=80, rx=2)
      + z('rect', '#d9a66b', x=26, y=164, width=148, height=14, rx=4))
for x, c, ly in ((66, '#f6a6b8', 98), (100, '#8fc7e8', 70), (134, '#9ccf7a', 110)):
    tt += (z('path', '#ffffff', d=f'M{x-12} 40 L{x-12} 140 Q{x-12} 156 {x} 156 Q{x+12} 156 {x+12} 140 L{x+12} 40Z')
           + s('path', c, d=f'M{x-12} {ly} Q{x} {ly+4} {x+12} {ly} L{x+12} 140 Q{x+12} 156 {x} 156 Q{x-12} 156 {x-12} 140Z', stroke_width=2.5)
           + s('rect', '#f4f4f0', x=x - 15, y=34, width=30, height=8, rx=3, stroke_width=2.5)
           + s('circle', '#ffffff', cx=x - 3, cy=ly - 10, r=3, stroke_width=2) + s('circle', '#ffffff', cx=x + 4, cy=ly - 20, r=2, stroke_width=2))
tt += z('rect', '#d9a66b', x=26, y=110, width=148, height=14, rx=4)
tt += _kao(100, 136, 6, 3)
ITEMS['test-tubes'] = tt

# 13. magnet
mg = (z('path', '#e04b5a', d='M50 110 L50 90 A50 50 0 0 1 150 90 L150 110 L120 110 L120 90 A20 20 0 0 0 80 90 L80 110Z')
      + z('rect', '#c9d3db', x=50, y=108, width=30, height=24, rx=2)
      + z('rect', '#c9d3db', x=120, y=108, width=30, height=24, rx=2)
      + dot(86, 54, 3) + dot(114, 54, 3) + cheeks(76, 124, 60, 5, 3) + _smile(100, 60, 4))


def _clip(x, y):
    return s('path', d=f'M{x} {y+4} L{x} {y+34} Q{x} {y+40} {x+6} {y+40} Q{x+12} {y+40} {x+12} {y+34} L{x+12} {y+2} Q{x+12} {y-2} {x+8} {y-2} Q{x+4} {y-2} {x+4} {y+2} L{x+4} {y+30}',
             stroke='#5b6b7a', stroke_width=3)


mg += _clip(59, 140) + _clip(129, 140)
mg += s('path', d='M40 120 L28 126 M40 132 L28 140 M160 120 L172 126 M160 132 L172 140', stroke_width=2.5)
ITEMS['magnet'] = mg

# 14. dictionary
dy = (z('path', '#e04b5a', d='M16 76 Q58 62 100 76 Q142 62 184 76 L184 172 Q142 160 100 176 Q58 160 16 172Z')
      + s('path', '#ffffff', d='M22 70 Q60 56 100 70 L100 166 Q60 152 22 164Z')
      + s('path', '#ffffff', d='M178 70 Q140 56 100 70 L100 166 Q140 152 178 164Z')
      + s('path', d='M22 156 Q60 144 100 158 Q140 144 178 156 M22 148 Q60 136 100 150 Q140 136 178 148', stroke_width=2)
      + s('path', d='M100 70 L100 166'))
for y in (78, 90, 102, 114, 126):
    dy += s('path', d=f'M34 {y+4} Q60 {y-4} 88 {y+6}', stroke='#c9d3db', stroke_width=3)
    dy += s('path', d=f'M112 {y+6} Q140 {y-4} 166 {y+4}', stroke='#c9d3db', stroke_width=3)
for i, c in enumerate(('#ffc94d', '#8fc7e8', '#9ccf7a')):
    dy += z('rect', c, x=178, y=82 + i * 18, width=8, height=12, rx=2)
dy += s('path', '#e04b5a', d='M128 66 L128 40 L134 46 L140 40 L140 66', stroke_width=2.5)
ITEMS['dictionary'] = dy

# 15. school-desk
sd = (z('rect', '#c9d3db', x=36, y=94, width=7, height=82, rx=2)
      + z('rect', '#c9d3db', x=104, y=94, width=7, height=82, rx=2)
      + z('rect', '#c9d3db', x=32, y=94, width=84, height=20, rx=3)
      + z('rect', '#8fc7e8', x=46, y=68, width=40, height=12, rx=2)
      + z('rect', '#d9a66b', x=24, y=80, width=100, height=14, rx=4)
      + z('rect', '#c9d3db', x=124, y=126, width=6, height=50, rx=2)
      + z('rect', '#c9d3db', x=160, y=96, width=6, height=80, rx=2)
      + z('rect', '#d9a66b', x=150, y=70, width=24, height=36, rx=4)
      + z('rect', '#d9a66b', x=114, y=118, width=60, height=12, rx=4)
      + s('path', d='M16 180 L184 180', stroke_width=2.5))
ITEMS['school-desk'] = sd

# 16. blackboard
bb = (s('path', d='M56 150 L44 182 M144 150 L156 182', stroke_width=5)
      + z('rect', '#d9a66b', x=24, y=34, width=152, height=112, rx=5)
      + s('rect', '#7cc4a0', x=33, y=43, width=134, height=94, rx=2)
      + s('circle', cx=68, cy=74, r=12, stroke='#ffffff')
      + s('path', d='M68 54 L68 50 M86 74 L90 74 M50 74 L46 74 M81 61 L84 58 M55 61 L52 58 M81 87 L84 90 M55 87 L52 90', stroke='#ffffff', stroke_width=2.5)
      + s('path', d='M128 58 L133 70 L146 71 L136 79 L139 92 L128 85 L117 92 L120 79 L110 71 L123 70Z', stroke='#ffffff', stroke_width=2.5)
      + s('path', d='M46 118 Q60 104 74 118 Q88 132 102 118 Q116 104 130 118 Q144 132 156 118', stroke='#ffffff', stroke_width=2.5)
      + z('rect', '#9a6a3f', x=28, y=142, width=144, height=10, rx=3)
      + s('rect', '#ffffff', x=48, y=134, width=18, height=7, rx=2, stroke_width=2)
      + s('rect', '#f6a6b8', x=74, y=134, width=14, height=7, rx=2, stroke_width=2)
      + s('rect', '#ffe27a', x=94, y=134, width=12, height=7, rx=2, stroke_width=2)
      + z('rect', '#8fb3e0', x=126, y=128, width=30, height=13, rx=2))
ITEMS['blackboard'] = bb

# 17. school-bell
bl = (s('path', d='M36 92 Q28 108 34 124 M24 84 Q14 108 22 132 M164 92 Q172 108 166 124 M176 84 Q186 108 178 132', stroke_width=2.5)
      + z('ellipse', '#9a6a3f', cx=100, cy=40, rx=12, ry=20)
      + z('rect', '#9a6a3f', x=93, y=56, width=14, height=24, rx=3)
      + z('circle', '#d9a66b', cx=100, cy=166, r=10)
      + z('path', '#ffc94d', d='M56 150 Q60 82 100 78 Q140 82 144 150 Q154 154 154 162 L46 162 Q46 154 56 150Z')
      + s('path', d='M54 148 L146 148', stroke_width=2)
      + _kao(100, 116, 13))
ITEMS['school-bell'] = bl

# 18. school-bus
bs = (z('path', '#ffc94d', d='M20 76 Q20 62 34 62 L140 62 Q150 62 152 72 L156 98 L172 102 Q180 104 180 114 L180 148 L20 148Z')
      + ''.join(s('rect', '#8fc7e8', x=x, y=74, width=20, height=24, rx=3, stroke_width=2.5) for x in (30, 56, 82, 108))
      + s('rect', '#8fc7e8', x=132, y=74, width=18, height=66, rx=3, stroke_width=2.5)
      + s('path', d='M141 74 L141 140', stroke_width=2)
      + s('path', d='M20 112 L132 112 M20 120 L132 120 M150 120 L180 120', stroke_width=2)
      + s('circle', '#ffe27a', cx=172, cy=110, r=4, stroke_width=2)
      + s('rect', '#5b6b7a', x=174, y=134, width=10, height=8, rx=2, stroke_width=2)
      + z('circle', '#5b6b7a', cx=52, cy=150, r=16) + s('circle', '#c9d3db', cx=52, cy=150, r=6, stroke_width=2.5)
      + z('circle', '#5b6b7a', cx=150, cy=150, r=16) + s('circle', '#c9d3db', cx=150, cy=150, r=6, stroke_width=2.5)
      + s('path', d='M14 172 L186 172', stroke_width=2.5))
ITEMS['school-bus'] = bs

# 19. school-lunch
sl = (z('rect', '#c9d3db', x=20, y=46, width=160, height=118, rx=10)
      + z('ellipse', '#ffffff', cx=78, cy=80, rx=46, ry=22)
      + z('ellipse', '#9a6a3f', cx=70, cy=80, rx=24, ry=12)
      + s('path', '#9ccf7a', d='M98 76 Q104 66 112 72 Q116 82 106 88 Q96 86 98 76Z', stroke_width=2.5)
      + s('circle', '#e8735a', cx=110, cy=88, r=5, stroke_width=2)
      + z('rect', '#ffffff', x=140, y=52, width=30, height=46, rx=3)
      + s('rect', '#8fb3e0', x=140, y=70, width=30, height=16, stroke_width=2.5)
      + s('path', d='M162 52 L168 36', stroke='#f6a6b8', stroke_width=4)
      + z('circle', '#8fc7e8', cx=62, cy=128, r=28)
      + s('circle', '#ffffff', cx=62, cy=128, r=21, stroke_width=2.5)
      + z('circle', '#e8735a', cx=128, cy=128, r=28)
      + s('circle', '#f5b971', cx=128, cy=128, r=21, stroke_width=2.5)
      + s('circle', '#9ccf7a', cx=120, cy=122, r=4, stroke_width=2) + s('rect', '#f07a8a', x=130, y=128, width=8, height=8, rx=2, stroke_width=2)
      + s('circle', '#ffffff', cx=134, cy=118, r=3, stroke_width=2))
ITEMS['school-lunch'] = sl

# 20. recorder-flute
P = _frame(96, 106, 124)
rf = (z('path', '#f6e0c4', d=_poly([P(58, -9), P(78, -16), P(84, -16), P(84, 16), P(78, 16), P(58, 9)]))
      + z('path', '#f6e0c4', d=_poly([P(-26, -9), P(60, -9), P(60, 9), P(-26, 9)]))
      + z('path', '#f6e0c4', d=_poly([P(-64, -12), P(-24, -12), P(-24, 12), P(-64, 12)]))
      + z('path', '#d9a66b', d=_poly([P(-84, -6), P(-64, -10), P(-64, 10), P(-84, 6)]))
      + s('path', '#d9a66b', d=_poly([P(-28, -12), P(-22, -12), P(-22, 12), P(-28, 12)]), stroke_width=2.5)
      + s('path', '#5b6b7a', d=_poly([P(-54, -5), P(-46, -5), P(-46, 5), P(-54, 5)]), stroke_width=2))
for u in (-12, 0, 12, 24, 36, 48):
    x, y = P(u, 0)
    rf += dot(_f(x), _f(y), 3.5)
rf += (z('ellipse', '#a98bd0', cx=46, cy=70, rx=9, ry=7) + s('path', d='M54 70 L54 36 Q62 40 66 48', stroke_width=3)
       + z('ellipse', '#a98bd0', cx=150, cy=146, rx=8, ry=6) + s('path', d='M157 146 L157 118', stroke_width=3))
ITEMS['recorder-flute'] = rf
