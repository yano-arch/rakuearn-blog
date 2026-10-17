from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

GLASS = '#d8eef8'


def mini_face(cx, cy, gap=10, ch=17, r=3.2, k=1.0):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+9*k, 5.5*k, 3.2*k)
            + s('path', d=f'M{cx-4.5} {cy+8} Q{cx} {cy+12.5} {cx+4.5} {cy+8}', stroke_width=2.5))


def stick(d, color, w=7):
    return s('path', d=d, stroke_width=w+3) + s('path', d=d, stroke=color, stroke_width=w-3)


def fill_only(d, color):
    return f'<path d="{d}" fill="{color}" stroke="none"/>'


def steam(xs, y0=40, h=22):
    return ''.join(s('path', d=f'M{x} {y0+h} Q{x-7} {y0+h*0.66} {x} {y0+h*0.33} Q{x+7} {y0} {x} {y0-h*0.33}', stroke_width=2.5) for x in xs)


# 1 chocolate bar
choc = ''.join(s('path', d=f'M{x} 40 L{x} 120', stroke_width=2) for x in (88, 112))
choc += ''.join(s('path', d=f'M64 {y} L136 {y}', stroke_width=2) for y in (64, 92))
ITEMS['chocolate-bar'] = (
    z('rect', '#9a6a3f', x=62, y=32, width=76, height=100, rx=5)
    + choc
    + s('path', '#c9d3db', d='M58 116 L64 108 L72 116 L80 108 L88 116 L96 108 L104 116 L112 108 L120 116 L128 108 L136 116 L142 110 L142 124 L58 124Z', stroke_width=2.5)
    + z('path', '#e04b5a', d='M56 120 L144 120 L144 176 Q144 180 140 180 L60 180 Q56 180 56 176Z')
    + s('path', d='M56 168 L144 168', stroke='#f5d58a', stroke_width=4)
    + mini_face(100, 140)
)

# 2 candy
def candy(cx, cy, col, stripe, rot):
    o = (z('path', col, d=f'M{cx-30} {cy} L{cx-54} {cy-18} Q{cx-50} {cy} {cx-54} {cy+18}Z')
         + z('path', col, d=f'M{cx+30} {cy} L{cx+54} {cy-18} Q{cx+50} {cy} {cx+54} {cy+18}Z')
         + z('ellipse', col, cx=cx, cy=cy, rx=34, ry=26)
         + ''.join(s('path', d=f'M{cx+dx-8} {cy-22} Q{cx+dx+4} {cy} {cx+dx-8} {cy+22}', stroke=stripe, stroke_width=4) for dx in (-12, 8)))
    return f'<g transform="rotate({rot} {cx} {cy})">{o}</g>'
ITEMS['candy'] = (
    candy(92, 74, '#f6a6b8', '#ffffff', -14)
    + candy(108, 140, '#ffe27a', '#f5b971', 10)
    + mini_face(108, 136, 9, 15, 3)
)

# 3 lollipop
swirl = 'M100 78 Q108 78 108 70 Q106 60 96 62 Q84 66 86 80 Q90 96 106 94 Q124 90 122 72 Q118 50 96 48 Q72 50 70 76 Q72 104 102 108 Q132 106 136 76'
ITEMS['lollipop'] = (
    stick('M100 118 L100 186', '#ffffff', 9)
    + z('circle', '#f6a6b8', cx=100, cy=76, r=48)
    + s('path', d=swirl, stroke='#ffffff', stroke_width=7)
    + s('path', d=swirl, stroke='#f07a8a', stroke_width=0)
    + s('circle', cx=100, cy=76, r=48)
    + z('path', '#8fc7e8', d='M100 136 L80 124 L80 148Z') + z('path', '#8fc7e8', d='M100 136 L120 124 L120 148Z')
    + s('circle', '#8fc7e8', cx=100, cy=136, r=5, stroke_width=2.5)
)

# 4 popcorn
def puff(x, y, r):
    return z('circle', '#ffffff', cx=x, cy=y, r=r) + dot(x+r*0.3, y+r*0.2, r*0.28, '#f5d58a')
pops = [(64, 92, 13), (136, 92, 13), (80, 78, 14), (120, 78, 14), (100, 70, 15), (90, 54, 12), (112, 52, 12), (72, 62, 10), (130, 62, 10), (100, 40, 10)]
box = 'M56 98 L144 98 L132 182 L68 182Z'
stripes = ''.join(fill_only(f'M{56+i*17.6} 98 L{56+i*17.6+17.6/2*2} 98 L{68+i*12.8+12.8} 182 L{68+i*12.8} 182Z', '#e04b5a') for i in (0, 2, 4))
ITEMS['popcorn'] = (
    ''.join(puff(*p) for p in sorted(pops, key=lambda p: p[1]))
    + z('path', '#ffffff', d=box) + stripes + s('path', d=box)
    + z('rect', '#ffffff', x=86, y=124, width=28, height=26, rx=6)
    + dot(94, 134, 2.8) + dot(106, 134, 2.8) + s('path', d='M96 141 Q100 145 104 141', stroke_width=2.2)
)

# 5 dango
ITEMS['dango'] = (
    stick('M100 22 L100 188', '#d9a66b', 8)
    + z('circle', '#9ccf7a', cx=100, cy=146, r=26)
    + z('circle', '#ffffff', cx=100, cy=100, r=26)
    + z('circle', '#f6a6b8', cx=100, cy=54, r=26)
    + mini_face(100, 54, 9, 15, 3) + mini_face(100, 100, 9, 15, 3) + mini_face(100, 146, 9, 15, 3)
)

# 6 taiyaki
ITEMS['taiyaki'] = (
    z('path', '#d9a66b', d='M138 100 L172 70 Q166 100 172 132Z')
    + z('path', '#d9a66b', d='M28 102 Q40 60 92 58 Q136 58 146 100 Q136 142 92 144 Q40 144 28 102Z')
    + z('path', '#d9a66b', d='M84 60 Q100 40 120 52 Q112 58 108 64Z')
    + s('path', d='M62 76 Q76 102 62 128', stroke_width=2.5)
    + ''.join(s('path', d=f'M{x} {y} Q{x+8} {y+6} {x+16} {y}', stroke_width=2.2) for x, y in ((80, 90), (100, 90), (120, 92), (90, 106), (110, 106), (80, 120), (100, 120)))
    + dot(46, 94, 4) + cheeks(50, 50, 108, 5, 3)
    + s('path', d='M32 112 Q38 116 42 112', stroke_width=2.5)
)

# 7 mochi
def mochi(cx, cy, rx, ry, col):
    return z('path', col, d=f'M{cx-rx} {cy} Q{cx-rx} {cy-ry*2} {cx} {cy-ry*2} Q{cx+rx} {cy-ry*2} {cx+rx} {cy} Q{cx} {cy+8} {cx-rx} {cy}Z')
ITEMS['mochi'] = (
    z('ellipse', '#8fb3e0', cx=100, cy=160, rx=80, ry=22)
    + s('ellipse', cx=100, cy=158, rx=60, ry=13, stroke_width=2)
    + mochi(64, 156, 34, 22, '#f6a6b8')
    + mochi(136, 156, 34, 22, '#9ccf7a')
    + mochi(100, 150, 42, 36, '#ffffff')
    + mini_face(100, 112, 11, 19)
)

# 8 shaved ice
ITEMS['shaved-ice'] = (
    z('rect', GLASS, x=78, y=162, width=44, height=14, rx=4)
    + z('rect', GLASS, x=92, y=146, width=16, height=20)
    + z('path', '#ffffff', d='M50 106 Q48 34 100 30 Q152 34 150 106Z')
    + z('path', '#f07a8a', d='M56 70 Q60 32 100 30 Q140 32 144 70 Q138 80 132 72 Q126 88 118 74 Q110 84 102 74 Q94 90 86 74 Q78 84 72 72 Q64 84 56 70Z')
    + z('path', GLASS, d='M42 104 L158 104 Q154 148 100 150 Q46 148 42 104Z')
    + s('path', d='M54 116 Q60 130 72 136', stroke='#ffffff', stroke_width=4)
    + stick('M128 60 L162 22', '#f5d58a', 6)
    + mini_face(100, 122, 10, 18)
)

# 9 parfait
def lx(y): return 60 + 12*(y-56)/84
def layer(y0, y1, col):
    return fill_only(f'M{lx(y0)} {y0} L{200-lx(y0)} {y0} L{200-lx(y1)} {y1} L{lx(y1)} {y1}Z', col)
glass = 'M60 56 L140 56 L128 140 Q100 150 72 140Z'
ITEMS['parfait'] = (
    z('ellipse', GLASS, cx=100, cy=176, rx=30, ry=8)
    + z('rect', GLASS, x=94, y=140, width=12, height=34)
    + z('path', GLASS, d=glass)
    + layer(72, 92, '#f6a6b8') + layer(92, 106, '#ffffff') + layer(106, 124, '#9a6a3f') + fill_only('M70.3 124 L129.7 124 L128 140 Q100 150 72 140Z', '#f5d58a')
    + s('path', d=glass)
    + z('rect', '#f5b971', x=116, y=20, width=12, height=44, rx=3)
    + z('path', '#ffffff', d='M56 62 Q52 46 70 46 Q74 32 92 38 Q100 24 112 36 Q130 32 132 46 Q148 46 144 62Z')
    + s('path', d='M100 28 Q104 14 112 8', stroke_width=2.5)
    + z('circle', '#e04b5a', cx=98, cy=30, r=10)
    + z('path', '#e04b5a', d='M66 48 Q62 34 74 36 Q84 38 78 50Z')
    + mini_face(100, 104, 10, 18)
)

# 10 crepe
ITEMS['crepe'] = (
    z('path', '#f5d58a', d='M48 84 Q50 64 72 70 Q100 56 128 70 Q150 64 152 84 L100 186Z')
    + z('circle', '#ffffff', cx=78, cy=64, r=16) + z('circle', '#ffffff', cx=122, cy=64, r=16) + z('circle', '#ffffff', cx=100, cy=56, r=18)
    + z('path', '#e04b5a', d='M70 66 Q64 44 80 44 Q94 46 86 66Z') + s('path', d='M74 44 L80 36 L86 44', stroke='#9ccf7a', stroke_width=3.5)
    + z('circle', '#ffe27a', cx=124, cy=58, r=11) + s('circle', '#f6e0c4', cx=124, cy=58, r=4, stroke_width=2)
    + s('path', d='M54 90 Q100 110 146 90', stroke_width=2.5)
    + s('path', d='M92 84 Q96 92 104 86 Q110 96 116 88', stroke='#9a6a3f', stroke_width=5)
    + z('path', '#f4f4f0', d='M68 126 L132 126 L100 186Z')
    + s('path', d='M78 140 L122 140 M86 156 L114 156', stroke='#8fc7e8', stroke_width=3)
    + mini_face(100, 106, 10, 18, 3)
)

# 11 green tea
ITEMS['green-tea'] = (
    z('ellipse', '#d9a66b', cx=100, cy=166, rx=58, ry=12)
    + z('path', '#7cc4a0', d='M54 82 L146 82 Q146 140 124 160 L76 160 Q54 140 54 82Z')
    + s('ellipse', '#9ccf7a', cx=100, cy=82, rx=46, ry=10)
    + s('path', d='M56 120 Q100 128 144 120', stroke='#f4f4f0', stroke_width=4)
    + steam((82, 100, 118), 38, 22)
    + mini_face(100, 104, 12, 22)
)

# 12 milk carton
ITEMS['milk'] = (
    z('path', '#c9d3db', d='M130 70 L154 54 L154 166 L130 182Z')
    + z('rect', '#ffffff', x=56, y=70, width=74, height=112, rx=2)
    + z('path', '#8fc7e8', d='M56 70 L80 30 L106 30 L130 70Z')
    + z('path', '#8fb3e0', d='M106 30 L130 16 L154 54 L130 70Z')
    + z('rect', '#f4f4f0', x=78, y=20, width=30, height=10, rx=1)
    + s('rect', '#8fc7e8', x=56, y=150, width=74, height=32, stroke_width=3)
    + s('ellipse', '#5b6b7a', cx=72, cy=136, rx=6, ry=4, stroke='none') + s('ellipse', '#5b6b7a', cx=116, cy=134, rx=5, ry=7, stroke='none')
    + mini_face(93, 108, 11, 19)
)

# 13 orange juice
oj_glass = 'M58 52 L142 52 L132 182 L68 182Z'
ITEMS['orange-juice'] = (
    stick('M112 120 L136 22', '#f07a8a', 8)
    + z('path', GLASS, d=oj_glass)
    + fill_only('M61.1 80 L138.9 80 L132 182 L68 182Z', '#ffc94d')
    + s('path', d='M61 80 L139 80', stroke_width=2.5)
    + s('path', d=oj_glass)
    + stick('M112 120 L120 80', '#f07a8a', 8)
    + z('circle', '#f5b971', cx=58, cy=50, r=22)
    + s('circle', '#ffe27a', cx=58, cy=50, r=15, stroke_width=2)
    + ''.join(s('path', d=f'M58 50 L{58+15*c} {50+15*sn}', stroke_width=1.6) for c, sn in ((1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7)))
    + dot(84, 152, 2) + dot(110, 106, 2.5, '#ffffff') + dot(90, 168, 2.5, '#ffffff')
    + mini_face(100, 128, 10, 18)
)

# 14 soda
bottle = 'M88 22 L112 22 L112 50 Q140 70 140 104 L140 172 Q140 184 128 184 L72 184 Q60 184 60 172 L60 104 Q60 70 88 50Z'
ITEMS['soda'] = (
    z('path', '#7cc4b0', d=bottle)
    + s('path', d='M70 100 Q72 76 92 62', stroke='#ffffff', stroke_width=4)
    + z('rect', '#e04b5a', x=84, y=14, width=32, height=14, rx=3)
    + z('rect', '#f5d58a', x=60, y=112, width=80, height=40)
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=r, stroke_width=1.8) for x, y, r in ((78, 166, 4), (120, 168, 3), (110, 92, 4), (88, 84, 3)))
    + mini_face(100, 126, 11, 19)
)

# 15 bubble tea
cup = 'M56 68 L144 68 L132 184 L68 184Z'
ITEMS['bubble-tea'] = (
    stick('M108 70 L124 14', '#f07a8a', 13)
    + z('path', GLASS, d=cup)
    + fill_only('M57.5 82 L142.5 82 L132 184 L68 184Z', '#d9a66b')
    + s('path', d='M58 82 L142 82', stroke_width=2.5)
    + ''.join(dot(x, y, 6, '#5a4033') for x, y in ((78, 172), (94, 176), (110, 174), (124, 170), (86, 160), (102, 162), (118, 158), (74, 156)))
    + s('path', d=cup)
    + z('path', '#ffffff', d='M50 70 Q50 40 100 38 Q150 40 150 70Z')
    + z('rect', '#ffffff', x=46, y=64, width=108, height=10, rx=4)
    + stick('M108 70 L114 46', '#f07a8a', 13)
    + mini_face(100, 110, 11, 19)
)

# 16 beer
ITEMS['beer'] = (
    s('path', d='M140 82 Q176 82 176 116 Q176 150 140 150', stroke_width=16) + s('path', d='M140 82 Q176 82 176 116 Q176 150 140 150', stroke='#f6e0c4', stroke_width=10)
    + z('rect', '#ffc94d', x=46, y=62, width=96, height=120, rx=8)
    + ''.join(s('path', d=f'M{x} 84 L{x} 168', stroke='#f5d58a', stroke_width=5) for x in (66, 122))
    + z('path', '#ffffff', d='M40 72 Q34 50 56 50 Q60 32 80 38 Q94 22 110 36 Q128 28 136 44 Q154 46 148 66 Q150 84 136 80 Q134 94 124 86 Q116 76 108 78 L48 82 Q38 82 40 72Z')
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=3, stroke_width=1.6) for x, y in ((80, 160), (110, 150), (96, 172)))
    + mini_face(94, 116, 11, 19)
)

# 17 wine
ITEMS['wine'] = (
    z('ellipse', GLASS, cx=88, cy=180, rx=34, ry=8)
    + z('rect', GLASS, x=83, y=114, width=10, height=64)
    + z('path', GLASS, d='M48 24 L128 24 Q136 64 124 92 Q110 120 88 120 Q66 120 52 92 Q40 64 48 24Z')
    + fill_only('M45 66 L131 66 Q130 80 124 92 Q110 120 88 120 Q66 120 52 92 Q46 80 45 66Z', '#e04b5a')
    + s('path', d='M45 66 Q88 72 131 66', stroke_width=2.5)
    + s('path', d='M48 24 L128 24 Q136 64 124 92 Q110 120 88 120 Q66 120 52 92 Q40 64 48 24Z')
    + s('path', d='M58 36 Q54 52 58 62', stroke='#ffffff', stroke_width=4)
    + s('path', d='M152 118 Q152 108 158 102', stroke_width=3)
    + ''.join(z('circle', '#8fb3e0', cx=x, cy=y, r=8) for x, y in ((144, 128), (160, 128), (152, 142), (136, 142), (168, 142), (144, 156), (160, 156), (152, 170)))
    + z('path', '#9ccf7a', d='M156 110 Q172 98 180 112 Q168 120 156 110Z')
    + mini_face(88, 86, 10, 17)
)

# 18 water bottle
wb = 'M86 40 L114 40 L114 52 Q136 62 136 84 L136 170 Q136 184 122 184 L78 184 Q64 184 64 170 L64 84 Q64 62 86 52Z'
ITEMS['water-bottle'] = (
    z('path', GLASS, d=wb)
    + fill_only('M64.2 92 L135.8 92 L136 170 Q136 184 122 184 L78 184 Q64 184 64 170Z', '#8fc7e8')
    + s('path', d='M64 92 L136 92', stroke_width=2.5)
    + s('path', d=wb)
    + s('path', d='M64 160 L136 160 M64 170 L136 170', stroke_width=2)
    + z('rect', '#8fb3e0', x=82, y=20, width=36, height=22, rx=4)
    + s('path', d='M90 24 L90 38 M100 24 L100 38 M110 24 L110 38', stroke_width=2)
    + z('rect', '#ffffff', x=64, y=104, width=72, height=44)
    + s('path', d='M74 82 Q72 66 84 60', stroke='#ffffff', stroke_width=4)
    + z('path', '#8fc7e8', d='M162 104 Q172 118 162 124 Q152 118 162 104Z')
    + z('path', '#8fc7e8', d='M40 132 Q48 144 40 150 Q32 144 40 132Z')
    + mini_face(100, 120, 11, 19)
)

# 19 smoothie
sg = 'M58 64 L142 64 L130 184 L70 184Z'
ITEMS['smoothie'] = (
    stick('M106 70 L132 14 L146 14', '#9ccf7a', 9)
    + z('path', '#f6a6b8', d=sg)
    + z('path', '#f6a6b8', d='M52 66 Q56 40 80 46 Q100 30 120 46 Q144 40 148 66Z')
    + s('path', d='M66 70 Q72 60 80 64', stroke='#ffffff', stroke_width=3)
    + stick('M106 70 L114 52', '#9ccf7a', 9)
    + z('path', '#e04b5a', d='M38 56 Q34 30 54 30 Q72 32 62 58 Q52 68 38 56Z')
    + s('path', d='M44 32 L52 22 L58 32', stroke='#9ccf7a', stroke_width=3.5)
    + dot(48, 44, 1.6, '#ffe27a') + dot(56, 40, 1.6, '#ffe27a') + dot(52, 52, 1.6, '#ffe27a')
    + z('circle', '#9ccf7a', cx=146, cy=60, r=16) + s('circle', '#f4f4f0', cx=146, cy=60, r=5, stroke_width=1.5)
    + s('path', d='M64 150 L136 150', stroke='#f07a8a', stroke_width=5)
    + mini_face(100, 108, 11, 19)
)

# 20 hot chocolate
ITEMS['hot-chocolate'] = (
    s('path', d='M140 96 Q174 96 174 124 Q174 152 136 152', stroke_width=16) + s('path', d='M140 96 Q174 96 174 124 Q174 152 136 152', stroke='#f07a8a', stroke_width=10)
    + z('path', '#f07a8a', d='M40 82 L148 82 L140 168 Q138 182 124 182 L64 182 Q50 182 48 168Z')
    + s('ellipse', '#9a6a3f', cx=94, cy=82, rx=54, ry=12)
    + z('rect', '#ffffff', x=62, y=64, width=20, height=18, rx=4)
    + z('rect', '#f6a6b8', x=86, y=60, width=20, height=18, rx=4)
    + z('rect', '#ffffff', x=108, y=66, width=20, height=18, rx=4)
    + steam((76, 98, 120), 22, 22)
    + s('path', d='M50 158 L144 158', stroke='#ffffff', stroke_width=4)
    + mini_face(94, 120, 12, 22)
)
