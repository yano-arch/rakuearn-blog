from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def thick(d, color, w=10, inner=5):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def mini(cx, cy, r, hair, mouth='smile'):
    """小さめの顔（face() の縮小版）"""
    k = r / 34
    def f(v): return round(v, 1)
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=(f'M{f(cx-r)} {f(cy-2*k)} Q{f(cx-32*k)} {f(cy-36*k)} {cx} {f(cy-35*k)} '
                            f'Q{f(cx+32*k)} {f(cy-36*k)} {f(cx+r)} {f(cy-2*k)} Q{f(cx+20*k)} {f(cy-18*k)} {cx} {f(cy-17*k)} '
                            f'Q{f(cx-20*k)} {f(cy-18*k)} {f(cx-r)} {f(cy-2*k)}Z'))
    o += dot(f(cx-12*k), f(cy+2*k), 3) + dot(f(cx+12*k), f(cy+2*k), 3) + cheeks(f(cx-20*k), f(cx+20*k), f(cy+13*k), 5, 3)
    if mouth == 'smile':
        o += s('path', d=f'M{f(cx-5*k)} {f(cy+16*k)} Q{cx} {f(cy+21*k)} {f(cx+5*k)} {f(cy+16*k)}', stroke_width=2.5)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{f(cx-7*k)} {f(cy+14*k)} Q{cx} {f(cy+27*k)} {f(cx+7*k)} {f(cy+14*k)}Z', stroke_width=2.5)
    return o


def body(cx, top, bottom, col, hw=30):
    return z('path', col, d=f'M{cx-hw} {bottom} Q{cx-hw+2} {top+2} {cx} {top} Q{cx+hw-2} {top+2} {cx+hw} {bottom}Z')


def drop(x, y, k=1.0, col='#8fc7e8'):
    return z('path', col, d=f'M{x} {y} Q{x-6*k} {y+10*k} {x} {y+14*k} Q{x+6*k} {y+10*k} {x} {y}Z', stroke_width=2.5)


def ground(y, x1=24, x2=178):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2.5)


def star_d(cx, cy, R, r, rot=-90):
    pts = []
    for i in range(10):
        a = (rot + i * 36) * pi / 180
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


# 1 dumbbell (curl)
def db(cx, cy, col='#e8735a'):
    return (s('rect', '#5b6b7a', x=cx-22, y=cy-3, width=44, height=6, rx=2, stroke_width=2.5)
            + z('rect', col, x=cx-25, y=cy-16, width=11, height=32, rx=3)
            + z('rect', col, x=cx+14, y=cy-16, width=11, height=32, rx=3))


ITEMS['dumbbell'] = (
    body(80, 132, 182, '#7cc4b0', 34)
    + thick('M56 146 Q50 162 54 174', SK, 13, 7)
    + thick('M104 146 L146 146 L146 104', SK, 13, 7)
    + db(146, 92)
    + z('circle', SK, cx=146, cy=100, r=8)
    + face(80, 86, SK, '#5a4033', 'smile')
    + drop(124, 54) + drop(30, 70, 0.8)
    + s('path', d='M168 120 L176 116 M166 132 L176 132', stroke_width=2.5)
)

# 2 push-ups
ITEMS['push-ups'] = (
    ground(178)
    + thick('M128 140 L174 168', '#5b6b7a', 18, 12)
    + z('ellipse', '#8fb3e0', cx=172, cy=170, rx=8, ry=6)
    + z('ellipse', '#f07a8a', cx=100, cy=130, rx=40, ry=17, transform='rotate(16 100 130)')
    + thick('M80 128 L80 170', SK, 13, 7)
    + z('ellipse', SK, cx=82, cy=172, rx=10, ry=5)
    + z('circle', SK, cx=52, cy=112, r=24)
    + s('path', '#2b2220', d='M30 104 Q34 84 56 88 Q72 92 74 106 Q62 98 52 100 Q40 100 30 104Z')
    + dot(44, 116, 3) + dot(60, 116, 3) + cheeks(38, 66, 124, 5, 3)
    + s('path', d='M48 128 Q52 132 56 128', stroke_width=2.5)
    + drop(66, 70) + drop(84, 82, 0.8)
    + s('path', d='M110 94 L112 84 M124 100 L130 92', stroke_width=2.5)
)

# 3 jump rope
ITEMS['jump-rope'] = (
    s('path', d='M46 118 Q30 196 100 188 Q170 196 154 118', stroke='#f07a8a', stroke_width=4)
    + thick('M90 150 L86 168', SK, 12, 6) + thick('M110 150 L114 168', SK, 12, 6)
    + z('ellipse', '#e8735a', cx=84, cy=170, rx=10, ry=6) + z('ellipse', '#e8735a', cx=116, cy=170, rx=10, ry=6)
    + body(100, 102, 154, '#ffc94d', 26)
    + thick('M80 118 Q60 124 50 118', SK, 12, 6) + thick('M120 118 Q140 124 150 118', SK, 12, 6)
    + z('rect', '#8fb3e0', x=40, y=106, width=10, height=22, rx=4, transform='rotate(-20 45 117)')
    + z('rect', '#8fb3e0', x=150, y=106, width=10, height=22, rx=4, transform='rotate(20 155 117)')
    + face(100, 68, SK, '#2b2220', 'open')
    + s('path', d='M70 184 L60 184 M140 184 L130 184', stroke_width=2.5)
    + s('path', d='M30 176 L24 174 M170 176 L176 174', stroke_width=2.5)
)

# 4 marathon finish
ITEMS['marathon-finish'] = (
    z('rect', '#c9d3db', x=24, y=104, width=8, height=76, rx=3) + z('rect', '#c9d3db', x=166, y=104, width=8, height=76, rx=3)
    + thick('M88 152 L80 180', '#5b6b7a', 13, 7) + thick('M112 152 L120 180', '#5b6b7a', 13, 7)
    + thick('M78 116 Q60 90 56 58', SK, 13, 7) + thick('M122 116 Q140 90 144 58', SK, 13, 7)
    + z('circle', SK, cx=56, cy=54, r=9) + z('circle', SK, cx=144, cy=54, r=9)
    + body(100, 108, 160, '#e8735a', 28)
    + s('rect', '#ffffff', x=88, y=128, width=24, height=18, rx=2, stroke_width=2.5)
    + s('path', d='M30 128 Q46 120 58 132 Q66 140 72 130', stroke='#e04b5a', stroke_width=6)
    + s('path', d='M128 130 Q136 142 146 132 Q158 120 170 128', stroke='#e04b5a', stroke_width=6)
    + face(100, 76, SK, '#5a4033', 'open')
    + s('path', d='M34 44 L26 38 M30 66 L22 66 M166 44 L174 38 M170 66 L178 66', stroke_width=2.5)
)

# 5 relay baton
ITEMS['relay-baton'] = (
    z('path', '#8fc7e8', d='M24 168 L60 132 L80 152 L44 186Z')
    + z('path', '#f07a8a', d='M176 32 L140 70 L120 50 L156 24Z')
    + z('rect', '#ffc94d', x=62, y=92, width=76, height=18, rx=8, transform='rotate(-35 100 101)')
    + s('path', d='M74 112 L80 128 M120 74 L126 90', stroke_width=2.5)
    + z('circle', SK, cx=78, cy=128, r=17)
    + s('path', d='M66 120 Q74 116 84 122 M66 128 Q74 124 86 130', stroke_width=2.5)
    + z('circle', SK, cx=124, cy=74, r=17)
    + s('path', d='M134 82 Q126 86 116 80 M134 74 Q126 78 114 72', stroke_width=2.5)
    + s('path', d='M30 104 L52 104 M24 118 L48 118 M150 112 L174 112 M154 126 L176 126', stroke_width=2.5)
)

# 6 high jump
ITEMS['high-jump'] = (
    z('rect', '#8fb3e0', x=28, y=150, width=144, height=30, rx=8)
    + z('rect', '#c9d3db', x=36, y=96, width=8, height=56, rx=2) + z('rect', '#c9d3db', x=156, y=96, width=8, height=56, rx=2)
    + thick('M120 84 L150 62 L170 78', '#5b6b7a', 14, 8)
    + thick('M78 90 L62 62', SK, 12, 6)
    + z('path', '#f07a8a', d='M64 96 Q90 60 128 76 Q132 92 120 96 Q96 90 70 108Z')
    + z('rect', '#ffc94d', x=30, y=116, width=140, height=7, rx=3)
    + mini(50, 94, 22, '#2b2220', 'open')
    + s('path', d='M178 92 L170 98 M180 108 L172 108', stroke_width=2.5)
)

# 7 hurdles
ITEMS['hurdles'] = (
    ground(180)
    + z('rect', '#f4f4f0', x=70, y=136, width=8, height=44, rx=2) + z('rect', '#f4f4f0', x=140, y=136, width=8, height=44, rx=2)
    + z('rect', '#f4f4f0', x=60, y=132, width=98, height=14, rx=2)
    + s('rect', '#e04b5a', x=72, y=132, width=12, height=14, stroke_width=0) + s('rect', '#e04b5a', x=98, y=132, width=12, height=14, stroke_width=0)
    + s('rect', '#e04b5a', x=124, y=132, width=12, height=14, stroke_width=0)
    + s('rect', x=60, y=132, width=98, height=14, rx=2)
    + thick('M86 120 Q66 128 50 112', '#5b6b7a', 14, 8)
    + thick('M110 118 L150 112 L172 112', '#5b6b7a', 14, 8)
    + thick('M80 96 L58 84', SK, 12, 6) + thick('M118 96 L140 80', SK, 12, 6)
    + body(98, 88, 128, '#7cc4b0', 24)
    + face(98, 60, SK, '#5a4033', 'smile')
    + s('path', d='M30 92 L44 92 M26 104 L42 104', stroke_width=2.5)
)

# 8 gymnastics (rhythmic ribbon)
ITEMS['gymnastics'] = (
    s('path', d='M150 34 Q184 50 168 82 Q150 110 120 100 Q90 92 70 118 Q50 144 64 170 Q74 184 96 176',
      stroke='#f07a8a', stroke_width=6)
    + thick('M106 170 L104 182', SK, 12, 6)
    + thick('M108 146 Q132 156 150 140', SK, 12, 6)
    + z('path', '#a98bd0', d='M84 154 Q82 116 100 112 Q118 116 116 154Z')
    + thick('M88 122 Q68 112 56 92', SK, 12, 6)
    + thick('M112 122 Q130 100 138 70', SK, 11, 6)
    + s('path', d='M140 74 L150 34', stroke='#8b6b4f', stroke_width=4)
    + z('circle', SK, cx=138, cy=72, r=7)
    + z('circle', '#5a4033', cx=100, cy=40, r=10)
    + face(100, 78, SK, '#5a4033', 'smile')
    + s('circle', '#f6a6b8', cx=100, cy=48, r=5, stroke_width=2)
)

# 9 archery
ITEMS['archery'] = (
    thick('M92 140 L64 182', '#8b6b4f', 12, 6) + thick('M108 140 L136 182', '#8b6b4f', 12, 6)
    + z('circle', '#f4f4f0', cx=96, cy=96, r=62)
    + s('circle', '#8fc7e8', cx=96, cy=96, r=48) + s('circle', '#f07a8a', cx=96, cy=96, r=33)
    + s('circle', '#ffe27a', cx=96, cy=96, r=18)
    + s('path', d='M96 96 L160 46', stroke_width=7) + s('path', d='M96 96 L160 46', stroke='#8b6b4f', stroke_width=2)
    + z('path', '#e8735a', d='M150 54 L156 34 L166 40 L162 48Z')
    + z('path', '#e8735a', d='M152 56 L172 52 L170 62 L160 60Z')
    + s('path', d='M82 92 L72 86 M88 110 L80 118 M104 82 L106 72', stroke_width=2.5)
)

# 10 bowling
def pin(cx, base):
    d = (f'M{cx-10} {base} Q{cx-17} {base-30} {cx-13} {base-50} Q{cx-6} {base-62} {cx-6} {base-70} '
         f'Q{cx-13} {base-82} {cx} {base-88} Q{cx+13} {base-82} {cx+6} {base-70} Q{cx+6} {base-62} {cx+13} {base-50} '
         f'Q{cx+17} {base-30} {cx+10} {base}Z')
    return (z('path', '#ffffff', d=d)
            + s('path', d=f'M{cx-7} {base-60} Q{cx} {base-57} {cx+7} {base-60}', stroke='#e04b5a', stroke_width=3)
            + s('path', d=f'M{cx-8} {base-54} Q{cx} {base-51} {cx+8} {base-54}', stroke='#e04b5a', stroke_width=3))


ITEMS['bowling'] = (
    pin(134, 162) + pin(112, 176) + pin(156, 176)
    + z('circle', '#8fb3e0', cx=64, cy=144, r=34)
    + dot(56, 128, 5) + dot(72, 128, 5) + dot(64, 142, 5.5)
    + s('path', d='M24 176 L50 176 M30 186 L44 186', stroke_width=2.5)
    + s('path', d='M128 50 L120 40 M146 48 L148 36 M162 54 L172 44', stroke_width=2.5)
)

# 11 climbing
def hold(cx, cy, col, r=8):
    return z('path', col, d=f'M{cx-r} {cy} Q{cx-r} {cy-r} {cx} {cy-r} Q{cx+r+2} {cy-r+2} {cx+r} {cy+2} Q{cx+r-2} {cy+r} {cx} {cy+r-2} Q{cx-r} {cy+r} {cx-r} {cy}Z', stroke_width=2.5)


ITEMS['climbing'] = (
    z('rect', '#f5d58a', x=26, y=24, width=148, height=154, rx=8)
    + hold(40, 120, '#9ccf7a') + hold(156, 110, '#8fc7e8') + hold(40, 160, '#e8735a') + hold(158, 166, '#a98bd0')
    + hold(150, 36, '#f07a8a') + hold(96, 38, '#ffc94d')
    + s('path', d='M100 26 L100 132', stroke='#e8735a', stroke_width=4)
    + thick('M88 150 L72 166', '#5b6b7a', 14, 8) + thick('M112 150 L130 160', '#5b6b7a', 14, 8)
    + hold(66, 172, '#7cc4b0', 7) + hold(136, 162, '#ffc94d', 7)
    + z('ellipse', '#8fb3e0', cx=70, cy=168, rx=10, ry=6) + z('ellipse', '#8fb3e0', cx=132, cy=158, rx=10, ry=6)
    + thick('M80 118 Q62 92 58 62', SK, 12, 6) + thick('M120 118 Q140 92 146 64', SK, 12, 6)
    + hold(56, 56, '#7cc4b0') + hold(148, 60, '#e04b5a')
    + z('circle', SK, cx=58, cy=62, r=8) + z('circle', SK, cx=146, cy=66, r=8)
    + body(100, 110, 154, '#e8735a', 24)
    + s('rect', '#ffe27a', x=78, y=134, width=44, height=8, rx=3, stroke_width=2.5)
    + face(100, 84, SK, '#2b2220', 'smile')
)

# 12 horse riding
ITEMS['horse-riding'] = (
    ground(182)
    + s('path', '#9a6a3f', d='M150 116 Q176 120 172 160 Q162 140 150 132Z')
    + thick('M78 140 L72 178', '#d9a66b', 14, 8) + thick('M136 140 L144 178', '#d9a66b', 14, 8)
    + thick('M90 142 L88 178', '#d9a66b', 14, 8) + thick('M124 142 L126 178', '#d9a66b', 14, 8)
    + z('ellipse', '#d9a66b', cx=108, cy=126, rx=46, ry=26)
    + z('path', '#d9a66b', d='M66 118 Q56 92 50 70 L74 64 Q82 92 92 110Z')
    + z('ellipse', '#d9a66b', cx=50, cy=72, rx=24, ry=14, transform='rotate(-25 50 72)')
    + z('path', '#d9a66b', d='M60 56 L64 42 L70 58Z')
    + s('path', '#9a6a3f', d='M68 56 Q80 70 86 92 Q90 104 96 112 Q80 106 74 88 Q70 72 62 60Z', stroke_width=2.5)
    + dot(48, 66, 3) + dot(34, 80, 2) + cheeks(52, 52, 80, 5, 3)
    + s('path', d='M32 84 Q36 88 42 86', stroke_width=2)
    + z('path', '#e8735a', d='M92 104 Q108 98 128 104 L126 116 Q108 112 94 116Z')
    + thick('M112 112 L114 140', '#8fb3e0', 13, 7)
    + body(110, 70, 112, '#7cc4b0', 18)
    + thick('M100 88 L76 76', SK, 10, 5)
    + s('path', d='M74 76 Q62 74 54 82', stroke_width=2)
    + mini(112, 54, 20, '#5a4033', 'smile')
    + z('path', '#5b6b7a', d='M90 50 Q92 28 112 28 Q132 28 134 50 Q112 42 90 50Z')
)

# 13 rowing (front view)
ITEMS['rowing'] = (
    z('path', '#8fc7e8', d='M24 156 Q44 148 62 156 Q80 164 100 156 Q120 148 138 156 Q156 164 176 156 L176 180 L24 180Z')
    + body(100, 104, 148, '#ffc94d', 30)
    + z('path', '#e8735a', d='M44 134 L156 134 Q150 168 100 170 Q50 168 44 134Z')
    + s('path', d='M54 146 L146 146', stroke_width=2.5)
    + s('path', d='M74 126 L34 164', stroke_width=9) + s('path', d='M74 126 L34 164', stroke='#d9a66b', stroke_width=4)
    + s('path', d='M126 126 L166 164', stroke_width=9) + s('path', d='M126 126 L166 164', stroke='#d9a66b', stroke_width=4)
    + z('ellipse', '#d9a66b', cx=34, cy=166, rx=7, ry=12, transform='rotate(45 34 166)')
    + z('ellipse', '#d9a66b', cx=166, cy=166, rx=7, ry=12, transform='rotate(-45 166 166)')
    + thick('M84 116 L74 124', SK, 12, 6) + thick('M116 116 L126 124', SK, 12, 6)
    + z('circle', SK, cx=74, cy=124, r=8) + z('circle', SK, cx=126, cy=124, r=8)
    + face(100, 74, SK, '#2b2220', 'smile')
)

# 14 scuba diver
ITEMS['diving'] = (
    s('circle', '#8fc7e8', cx=46, cy=58, r=6, stroke_width=2.5) + s('circle', '#8fc7e8', cx=38, cy=40, r=4.5, stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=48, cy=26, r=3.5, stroke_width=2)
    + thick('M124 108 L156 98', '#5b6b7a', 16, 10) + thick('M124 118 L158 124', '#5b6b7a', 16, 10)
    + z('path', '#f5b971', d='M156 94 L180 80 L176 104 L160 104Z')
    + z('path', '#f5b971', d='M158 118 L180 116 L172 140 L156 130Z')
    + z('rect', '#ffc94d', x=84, y=80, width=50, height=18, rx=9)
    + z('ellipse', '#5b6b7a', cx=104, cy=110, rx=36, ry=17)
    + thick('M80 116 L50 130', '#5b6b7a', 13, 7) + z('circle', SK, cx=48, cy=130, r=7)
    + z('circle', SK, cx=60, cy=96, r=24)
    + s('path', '#5b6b7a', d='M36 92 Q38 70 60 70 Q82 70 84 92 Q60 82 36 92Z')
    + z('rect', '#8fc7e8', x=42, y=86, width=36, height=18, rx=8)
    + dot(52, 95, 3) + dot(68, 95, 3)
    + cheeks(44, 76, 110, 4.5, 2.5)
    + z('rect', '#c9d3db', x=54, y=110, width=12, height=8, rx=3)
    + s('path', d='M66 114 Q78 120 86 104', stroke_width=2.5)
    + z('path', '#f5b971', d='M132 160 Q146 148 160 160 Q146 172 132 160Z') + z('path', '#f5b971', d='M134 160 L122 152 L122 168Z')
    + dot(152, 158, 2)
)

# 15 ice hockey
ITEMS['ice-hockey'] = (
    z('ellipse', '#c9d3db', cx=100, cy=166, rx=76, ry=16)
    + z('path', '#d9a66b', d='M56 30 L70 24 L126 146 L168 146 Q178 148 176 160 L122 162 Q112 160 112 150Z')
    + s('path', '#5b6b7a', d='M56 30 L70 24 L80 46 L66 52Z', stroke_width=2.5)
    + s('path', '#f4f4f0', d='M136 146 L152 146 L152 161 L136 161Z', stroke_width=2.5)
    + z('ellipse', '#5b6b7a', cx=66, cy=162, rx=20, ry=8)
    + s('rect', '#5b6b7a', x=46, y=150, width=40, height=12, stroke_width=0)
    + s('path', d='M46 150 L46 162 M86 150 L86 162', stroke_width=3)
    + s('ellipse', '#5b6b7a', cx=66, cy=150, rx=20, ry=8)
    + s('path', d='M30 140 L40 140 M28 152 L38 150 M100 120 L94 112', stroke_width=2.5)
)

# 16 cricket
ITEMS['cricket'] = (
    z('rect', '#f6e0c4', x=126, y=74, width=9, height=100, rx=3) + z('rect', '#f6e0c4', x=142, y=74, width=9, height=100, rx=3)
    + z('rect', '#f6e0c4', x=158, y=74, width=9, height=100, rx=3)
    + z('rect', '#f6e0c4', x=124, y=66, width=22, height=7, rx=3) + z('rect', '#f6e0c4', x=148, y=66, width=22, height=7, rx=3)
    + z('rect', '#5b6b7a', x=84, y=20, width=12, height=44, rx=5, transform='rotate(30 90 42)')
    + z('path', '#f5d58a', d='M74 52 L102 68 L60 142 Q54 150 44 144 L34 138 Q28 130 34 122Z')
    + s('path', d='M86 76 L56 128', stroke_width=2.5)
    + z('circle', '#e04b5a', cx=104, cy=160, r=18)
    + s('path', d='M96 144 Q108 160 96 176', stroke='#f4f4f0', stroke_width=2.5)
    + s('path', d='M98 148 L103 147 M99 154 L104 153 M100 160 L105 160 M99 166 L104 167 M98 172 L103 173', stroke='#f4f4f0', stroke_width=2)
    + s('path', d='M120 140 L128 134 M122 156 L132 156', stroke_width=2.5)
)

# 17 cheerleader
def pompom(cx, cy, col, r=20):
    o = ''
    for i in range(8):
        a = i * pi / 4
        o += s('circle', col, cx=round(cx + r * 0.6 * cos(a), 1), cy=round(cy + r * 0.6 * sin(a), 1), r=r * 0.5, stroke_width=2.5)
    return o + s('circle', col, cx=cx, cy=cy, r=r * 0.5, stroke_width=2.5)


ITEMS['cheerleader'] = (
    z('path', '#5a4033', d='M126 52 Q154 60 146 96 Q138 82 128 74Z')
    + thick('M92 160 L90 178', SK, 12, 6) + thick('M108 160 L110 178', SK, 12, 6)
    + z('ellipse', '#f4f4f0', cx=88, cy=180, rx=9, ry=5) + z('ellipse', '#f4f4f0', cx=112, cy=180, rx=9, ry=5)
    + thick('M82 116 Q62 90 48 62', SK, 12, 6) + thick('M118 116 Q138 90 152 62', SK, 12, 6)
    + z('path', '#8fb3e0', d='M74 162 L82 132 L118 132 L126 162Z')
    + s('path', d='M88 136 L84 160 M100 136 L100 162 M112 136 L116 160', stroke_width=2.5)
    + z('path', '#e04b5a', d='M80 136 Q82 108 100 106 Q118 108 120 136Z')
    + s('path', '#ffffff', d='M88 108 L100 122 L112 108', stroke_width=2.5)
    + pompom(46, 56, '#ffc94d', 18) + pompom(154, 56, '#ffc94d', 18)
    + face(100, 74, SK, '#5a4033', 'open')
    + z('path', '#f07a8a', d='M100 40 L112 32 L112 48Z M100 40 L88 32 L88 48Z')
)

# 18 referee
ITEMS['referee'] = (
    body(100, 116, 182, '#f4f4f0', 36)
    + s('path', d='M76 128 L76 180 M92 120 L92 182 M108 120 L108 182 M124 128 L124 180', stroke_width=5)
    + s('path', d='M66 182 Q68 120 100 118 Q132 120 134 182Z')
    + thick('M126 132 Q146 112 152 72', '#f4f4f0', 15, 9)
    + z('circle', SK, cx=152, cy=66, r=9)
    + z('rect', '#ffe27a', x=146, y=26, width=22, height=30, rx=3, transform='rotate(12 157 41)')
    + face(84, 80, SK, '#2b2220', 'o')
    + z('path', '#c9d3db', d='M78 96 L92 94 Q104 94 104 104 Q104 112 94 112 Q86 112 86 104 L78 104Z')
    + s('path', d='M86 106 Q70 118 76 128', stroke_width=2)
    + s('path', d='M110 92 L118 88 M112 104 L122 106 M108 114 L114 120', stroke_width=2.5)
)

# 19 stopwatch
ticks = ''.join(
    s('path', d=f'M{100 + 42*cos(i*pi/6):.1f} {110 + 42*sin(i*pi/6):.1f} L{100 + 48*cos(i*pi/6):.1f} {110 + 48*sin(i*pi/6):.1f}', stroke_width=2.5)
    for i in range(12))
ITEMS['stopwatch'] = (
    z('rect', '#8fb3e0', x=90, y=30, width=20, height=12, rx=3)
    + z('rect', '#8fb3e0', x=94, y=40, width=12, height=12)
    + z('rect', '#8fb3e0', x=140, y=50, width=14, height=10, rx=3, transform='rotate(45 147 55)')
    + z('circle', '#8fb3e0', cx=100, cy=110, r=64)
    + s('circle', '#ffffff', cx=100, cy=110, r=52)
    + ticks
    + s('path', '#f07a8a', d='M100 110 L100 80 A30 30 0 0 1 126 95Z', stroke_width=0)
    + s('path', d='M100 110 L124 92', stroke='#e04b5a', stroke_width=4)
    + dot(100, 110, 5)
    + s('path', d='M28 74 L18 70 M24 92 L14 92 M172 74 L182 70', stroke_width=2.5)
)

# 20 medals
def medal(cx, cy, r, col, rib):
    return (z('path', rib, d=f'M{cx-r} {cy-r-44} L{cx-r+16} {cy-r-44} L{cx+6} {cy-r+6} L{cx-8} {cy-r+6}Z')
            + z('path', rib, d=f'M{cx+r} {cy-r-44} L{cx+r-16} {cy-r-44} L{cx-6} {cy-r+6} L{cx+8} {cy-r+6}Z')
            + z('circle', col, cx=cx, cy=cy, r=r)
            + s('circle', cx=cx, cy=cy, r=r - 7, stroke_width=2)
            + s('path', '#ffffff', d=star_d(cx, cy, r * 0.45, r * 0.2), stroke_width=2))


ITEMS['medals'] = (
    medal(48, 132, 22, '#c9d3db', '#8fb3e0')
    + medal(152, 136, 22, '#d9a66b', '#7cc4b0')
    + medal(100, 114, 30, '#ffc94d', '#e8735a')
    + s('path', d='M64 40 L58 32 M136 40 L142 32 M100 30 L100 22', stroke_width=2.5)
)
