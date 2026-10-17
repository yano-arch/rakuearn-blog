from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def mf(cx, cy, gap=12, ch=20, r=3.5):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+10, 6, 3.5)
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))


def stick(d, color, w=7):
    return s('path', d=d, stroke_width=w+3) + s('path', d=d, stroke=color, stroke_width=w-3)


def egg_d(cx, t, b, w):
    h = b-t; m = t+0.62*h
    return (f'M{cx} {t} C{cx+0.6*w:.1f} {t} {cx+w} {m-0.3*h:.1f} {cx+w} {m:.1f} '
            f'C{cx+w} {b-0.05*h:.1f} {cx+0.55*w:.1f} {b} {cx} {b} '
            f'C{cx-0.55*w:.1f} {b} {cx-w} {b-0.05*h:.1f} {cx-w} {m:.1f} '
            f'C{cx-w} {m-0.3*h:.1f} {cx-0.6*w:.1f} {t} {cx} {t}Z')


def blob(cx, cy, rx, ry, n, amp, rot=0):
    pts = []
    for i in range(n):
        a = 2*math.pi*i/n+rot
        pts.append((cx+rx*math.cos(a), cy+ry*math.sin(a)))
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f} '
    for i in range(n):
        a = 2*math.pi*(i+0.5)/n+rot
        k = 1+amp
        p = pts[(i+1) % n]
        d += f'Q{cx+rx*k*math.cos(a):.1f} {cy+ry*k*math.sin(a):.1f} {p[0]:.1f} {p[1]:.1f} '
    return d+'Z'


# 1 eggs
ITEMS['egg'] = (
    s('path', d='M30 178 L170 178', stroke_width=2.5)
    + z('path', '#f6e0c4', d=egg_d(136, 86, 174, 32))
    + z('path', '#ffffff', d=egg_d(80, 48, 174, 44))
    + s('path', d='M62 76 Q56 88 56 100', stroke='#f4f4f0', stroke_width=4)
    + mf(80, 124, 13, 24))

# 2 cheese wedge
ITEMS['cheese'] = (
    z('path', '#ffe27a', d='M38 106 L64 58 L162 102 L162 106Z')
    + z('rect', '#ffc94d', x=38, y=104, width=124, height=62, rx=4)
    + s('ellipse', '#f5b971', cx=70, cy=86, rx=8, ry=5, stroke_width=2)
    + s('ellipse', '#f5b971', cx=104, cy=94, rx=6, ry=3.5, stroke_width=2)
    + s('circle', '#f5b971', cx=56, cy=126, r=7, stroke_width=2)
    + s('circle', '#f5b971', cx=146, cy=146, r=9, stroke_width=2)
    + s('circle', '#f5b971', cx=142, cy=118, r=5, stroke_width=2)
    + s('circle', '#f5b971', cx=60, cy=154, r=4, stroke_width=2)
    + mf(100, 128, 13, 24))

# 3 honey jar with dipper
ITEMS['honey-jar'] = (
    stick('M112 72 L162 30', '#d9a66b', 9)
    + z('ellipse', '#d9a66b', cx=164, cy=28, rx=9, ry=9)
    + z('rect', '#ffc94d', x=44, y=72, width=104, height=104, rx=26)
    + z('rect', '#d9a66b', x=50, y=62, width=92, height=18, rx=6)
    + z('path', '#ffc94d', d='M54 80 L138 80 L138 96 Q134 104 130 96 L130 90 Q124 88 118 92 L118 108 Q113 116 108 108 L108 92 Q96 88 84 92 L84 100 Q79 108 74 100 L74 92 Q62 90 54 92Z')
    + s('ellipse', '#f6e0c4', cx=96, cy=134, rx=32, ry=24, stroke_width=2.5)
    + mf(96, 128, 11, 20))

# 4 jam jar
ITEMS['jam-jar'] = (
    z('rect', '#e04b5a', x=54, y=80, width=92, height=96, rx=16)
    + z('path', '#f6a6b8', d='M44 84 Q46 56 100 54 Q154 56 156 84 L148 96 L138 88 L126 98 L114 88 L100 98 L86 88 L74 98 L62 88 L52 96Z')
    + ''.join(dot(x, y, 3, '#ffffff') for x, y in ((70, 68), (92, 64), (114, 64), (134, 70), (80, 80), (104, 78), (126, 82), (58, 80), (144, 82)))
    + s('path', d='M50 88 Q100 102 150 88', stroke='#e8735a', stroke_width=4)
    + z('circle', '#ffffff', cx=100, cy=136, r=26)
    + mf(100, 132, 10, 17)
    + s('path', d='M62 112 Q60 128 62 146', stroke='#f6a6b8', stroke_width=4))

# 5 salt and pepper shakers
def shaker(cx, body, speck):
    o = z('rect', body, x=cx-26, y=84, width=52, height=90, rx=16)
    o += z('path', '#c9d3db', d=f'M{cx-24} 88 Q{cx-24} 52 {cx} 50 Q{cx+24} 52 {cx+24} 88Z')
    o += ''.join(dot(cx+dx, dy, 2.2) for dx, dy in ((-8, 66), (0, 62), (8, 66), (-4, 74), (4, 74)))
    o += ''.join(dot(cx+dx, dy, 1.6, speck) for dx, dy in ((-16, 102), (14, 104), (-12, 158), (16, 156), (0, 164)))
    return o + mf(cx, 124, 9, 15, 3.2)
ITEMS['salt-pepper'] = (
    s('path', d='M28 180 L172 180', stroke_width=2.5)
    + shaker(68, '#ffffff', '#c9d3db') + shaker(132, '#b9a99c', '#5b6b7a'))

# 6 sushi rolls (maki)
def maki(cx, cy, fill):
    o = z('path', '#5b6b7a', d=f'M{cx-26} {cy} L{cx-26} {cy+24} A26 12 0 0 0 {cx+26} {cy+24} L{cx+26} {cy}Z')
    o += z('ellipse', '#5b6b7a', cx=cx, cy=cy, rx=26, ry=13)
    o += s('ellipse', '#ffffff', cx=cx, cy=cy, rx=19, ry=8.5, stroke_width=2)
    o += s('ellipse', fill, cx=cx-3, cy=cy, rx=6, ry=4, stroke_width=2)
    o += s('ellipse', '#9ccf7a', cx=cx+6, cy=cy+1, rx=4, ry=3, stroke_width=2)
    return o
ITEMS['nori-roll'] = (
    z('rect', '#d9a66b', x=26, y=138, width=148, height=26, rx=6)
    + z('rect', '#9a6a3f', x=40, y=162, width=16, height=12, rx=2) + z('rect', '#9a6a3f', x=144, y=162, width=16, height=12, rx=2)
    + maki(76, 82, '#e8735a') + maki(124, 82, '#e04b5a')
    + maki(52, 112, '#ffc94d') + maki(100, 112, '#e8735a') + maki(148, 112, '#e04b5a'))

# 7 two rice balls on a plate
def oni(cx, t, mood):
    o = z('path', '#ffffff', d=f'M{cx} {t} Q{cx+8} {t} {cx+32} {t+56} Q{cx+42} {t+86} {cx+20} {t+88} L{cx-20} {t+88} Q{cx-42} {t+86} {cx-32} {t+56} Q{cx-8} {t} {cx} {t}Z')
    o += z('rect', '#5b6b7a', x=cx-16, y=t+64, width=32, height=26, rx=3)
    return o + mf(cx, t+44, 9, 16, 3)
ITEMS['onigiri-set'] = (
    z('ellipse', '#8fc7e8', cx=100, cy=152, rx=82, ry=24)
    + s('ellipse', 'none', cx=100, cy=150, rx=62, ry=14, stroke_width=2)
    + oni(64, 58, 0) + oni(136, 58, 1)
    + z('path', '#ffe27a', d='M86 160 Q100 150 114 160 Q100 168 86 160Z'))

# 8 udon noodles
ITEMS['udon'] = (
    s('path', d='M74 40 Q68 30 74 20 M100 36 Q94 26 100 16', stroke='#b9a99c', stroke_width=3)
    + stick('M118 70 L176 24', '#d9a66b', 7) + stick('M128 78 L180 40', '#d9a66b', 7)
    + z('ellipse', '#f5d58a', cx=100, cy=98, rx=74, ry=22)
    + ''.join(s('path', d=d, stroke_width=9) + s('path', d=d, stroke='#ffffff', stroke_width=5) for d in (
        'M50 100 Q70 90 90 100 Q108 108 120 96', 'M58 108 Q80 100 98 110 Q116 116 134 106',
        'M122 74 Q118 86 124 98', 'M132 80 Q128 92 136 104'))
    + z('ellipse', '#ffffff', cx=72, cy=90, rx=14, ry=8)
    + s('path', d='M64 90 Q72 84 80 90', stroke='#f6a6b8', stroke_width=3)
    + ''.join(s('circle', '#9ccf7a', cx=x, cy=y, r=3.5, stroke_width=2) for x, y in ((100, 88), (110, 92), (88, 106), (150, 100), (144, 92)))
    + z('path', '#e8735a', d='M24 100 Q100 128 176 100 Q172 168 100 170 Q28 168 24 100Z')
    + mf(100, 130, 12, 22))

# 9 fried rice
ITEMS['fried-rice'] = (
    z('ellipse', '#ffffff', cx=100, cy=150, rx=82, ry=26)
    + s('ellipse', 'none', cx=100, cy=148, rx=64, ry=16, stroke_width=2)
    + z('path', '#f5d58a', d='M42 146 Q44 72 100 68 Q156 72 158 146 Q100 156 42 146Z')
    + ''.join(s('circle', '#9ccf7a', cx=x, cy=y, r=4, stroke_width=2) for x, y in ((70, 92), (126, 84), (140, 126), (58, 130), (98, 80)))
    + ''.join(s('rect', '#e8735a', x=x, y=y, width=7, height=7, rx=1, stroke_width=2) for x, y in ((86, 86), (136, 106), (64, 112), (116, 138)))
    + ''.join(s('ellipse', '#ffe27a', cx=x, cy=y, rx=6, ry=4, stroke_width=2) for x, y in ((112, 78), (54, 108), (146, 140), (78, 140)))
    + z('path', '#ffffff', d='M150 120 L176 60 Q182 52 186 60 L178 70 L160 128Z')
    + mf(100, 110, 12, 20))

# 10 dumpling soup
def dump(cx, cy):
    o = z('path', '#f4f4f0', d=f'M{cx-20} {cy+4} Q{cx-16} {cy-16} {cx} {cy-16} Q{cx+16} {cy-16} {cx+20} {cy+4} Q{cx} {cy+10} {cx-20} {cy+4}Z')
    o += s('path', d=f'M{cx-8} {cy-14} Q{cx-6} {cy-8} {cx-8} {cy-4} M{cx} {cy-16} L{cx} {cy-6} M{cx+8} {cy-14} Q{cx+6} {cy-8} {cx+8} {cy-4}', stroke_width=2)
    return o
ITEMS['dumpling-soup'] = (
    s('path', d='M80 46 Q74 36 80 26 M104 42 Q98 32 104 22 M128 46 Q122 36 128 26', stroke='#b9a99c', stroke_width=3)
    + z('ellipse', '#f5d58a', cx=100, cy=96, rx=74, ry=22)
    + dump(66, 96) + dump(104, 88) + dump(134, 102)
    + ''.join(s('circle', '#9ccf7a', cx=x, cy=y, r=3.5, stroke_width=2) for x, y in ((86, 104), (92, 90), (128, 86), (150, 92), (48, 96)))
    + z('path', '#8fc7e8', d='M24 100 Q100 128 176 100 Q172 168 100 170 Q28 168 24 100Z')
    + mf(100, 130, 12, 22))

# 11 whole pizza
ITEMS['pizza-whole'] = (
    z('circle', '#d9a66b', cx=100, cy=100, r=74)
    + z('circle', '#ffe27a', cx=100, cy=100, r=60)
    + s('path', d='M100 40 L100 160 M48 70 L152 130 M48 130 L152 70', stroke='#f5b971', stroke_width=3)
    + ''.join(s('circle', '#e04b5a', cx=x, cy=y, r=9, stroke_width=2.5) for x, y in ((80, 64), (126, 66), (64, 104), (136, 104), (84, 140), (122, 138), (100, 96)))
    + ''.join(s('path', '#9ccf7a', d=f'M{x} {y} Q{x+6} {y-8} {x+12} {y} Q{x+6} {y+6} {x} {y}Z', stroke_width=2) for x, y in ((100, 70), (70, 84), (120, 88), (98, 124), (138, 122), (58, 124))))

# 12 burrito
ITEMS['burrito'] = '<g transform="rotate(-18 100 110)">' + (
    z('rect', '#f5d58a', x=64, y=56, width=76, height=124, rx=30)
    + z('ellipse', '#ffffff', cx=102, cy=58, rx=36, ry=16)
    + s('circle', '#9a6a3f', cx=90, cy=56, r=5, stroke_width=2) + s('circle', '#9a6a3f', cx=114, cy=62, r=5, stroke_width=2)
    + s('path', '#9ccf7a', d='M76 56 Q84 44 94 50 Q88 58 76 56Z', stroke_width=2)
    + s('path', '#9ccf7a', d='M112 46 Q124 42 130 52 Q120 54 112 46Z', stroke_width=2)
    + s('rect', '#e04b5a', x=98, y=52, width=8, height=7, rx=1, stroke_width=2)
    + s('path', d='M66 84 Q100 96 138 80', stroke_width=2.5)
    + z('path', '#c9d3db', d='M64 128 L74 120 L84 128 L94 120 L104 128 L114 120 L124 128 L134 120 L140 126 L140 150 Q140 182 102 182 Q64 182 64 150Z')
    + mf(102, 100, 11, 20)) + '</g>'

# 13 meat skewers
def skewer(y):
    o = s('path', d=f'M14 {y} L186 {y}', stroke_width=6) + s('path', d=f'M14 {y} L186 {y}', stroke='#d9a66b', stroke_width=2.5)
    for i, c in enumerate(('#9a6a3f', '#9ccf7a', '#9a6a3f', '#e04b5a', '#9a6a3f')):
        x = 34+i*28
        if c == '#e04b5a':
            o += z('circle', c, cx=x+13, cy=y, r=14)
        elif c == '#9ccf7a':
            o += z('rect', c, x=x+3, y=y-15, width=21, height=30, rx=5)
        else:
            o += z('rect', c, x=x, y=y-17, width=27, height=34, rx=9)
    return o
ITEMS['kebab'] = '<g transform="rotate(-20 100 100)">' + skewer(76) + skewer(130) + '</g>'

# 14 pretzel
PZ = 'M64 150 C74 122 120 104 132 74 C142 46 178 56 174 94 C170 142 128 170 100 170 C72 170 30 142 26 94 C22 56 58 46 68 74'
PZ2 = 'M68 74 C80 104 124 122 136 150'
ITEMS['pretzel'] = (
    '<g transform="translate(4 4)">' + s('path', d=PZ+' '+PZ2, stroke='#d9a66b', stroke_width=17) + '</g>'
    + s('path', d=PZ, stroke_width=24) + s('path', d=PZ, stroke='#d9a66b', stroke_width=17)
    + s('path', d=PZ2, stroke_width=24) + s('path', d=PZ2, stroke='#d9a66b', stroke_width=17)
    + s('path', d='M66 76 C78 104 122 122 134 148', stroke='#d9a66b', stroke_width=17)
    + ''.join(s('rect', '#ffffff', x=x, y=y, width=5, height=4, rx=1, stroke_width=1.5) for x, y in ((44, 96), (60, 58), (150, 62), (164, 104), (100, 164), (130, 152), (72, 152), (96, 112), (120, 86))))

# 15 bagel
ITEMS['bagel'] = (
    z('path', '#d9a66b', d='M100 36 A64 60 0 1 1 99.9 36Z M100 80 A20 18 0 1 0 100.1 80Z', fill_rule='evenodd')
    + s('path', d='M54 70 Q66 50 92 46', stroke='#f5b971', stroke_width=5)
    + ''.join(s('ellipse', '#ffffff', cx=x, cy=y, rx=3.5, ry=2, stroke_width=1.5, transform=f'rotate({r} {x} {y})') for x, y, r in (
        (100, 52, 10), (124, 58, -20), (146, 74, 30), (70, 66, -30), (56, 92, 20), (150, 100, -10), (80, 84, 40), (122, 84, -40), (72, 124, 15), (130, 124, -15)))
    + mf(100, 132, 12, 22))

# 16 waffle
WC = ''.join(s('rect', '#d9a66b', x=58+i*24, y=60+j*24, width=16, height=16, rx=3, stroke_width=2) for i in range(4) for j in range(4))
ITEMS['waffle'] = (
    z('ellipse', '#ffffff', cx=100, cy=158, rx=82, ry=22)
    + '<g transform="rotate(-6 100 104)">' + z('rect', '#f5b971', x=48, y=48, width=104, height=104, rx=14) + WC + '</g>'
    + z('path', '#9a6a3f', d='M70 74 Q100 60 130 72 Q138 80 132 96 Q130 110 124 100 L122 90 Q112 98 104 92 L102 116 Q96 124 92 114 L90 92 Q80 96 76 90 L74 102 Q66 106 66 96Z')
    + z('rect', '#ffe27a', x=86, y=62, width=28, height=20, rx=4))

# 17 fruit pie (top view, lattice)
def chord(x0, r):
    h = math.sqrt(r*r-(x0-100)**2)
    return h
LT = ''
for dx in (-30, 0, 30):
    h = chord(100+dx, 56)
    LT += stick(f'M{100+dx} {100-h:.1f} L{100+dx} {100+h:.1f}', '#f5b971', 12)
for dy in (-30, 0, 30):
    h = chord(100+dy, 56)
    LT += stick(f'M{100-h:.1f} {100+dy} L{100+h:.1f} {100+dy}', '#f5b971', 12)
ITEMS['pie'] = (
    z('path', '#f5b971', d=blob(100, 100, 72, 72, 16, 0.08))
    + z('circle', '#e04b5a', cx=100, cy=100, r=56)
    + ''.join(dot(x, y, 3, '#f07a8a') for x, y in ((84, 84), (116, 116), (84, 116), (116, 84), (68, 100), (132, 100), (100, 68), (100, 132)))
    + LT
    + s('circle', 'none', cx=100, cy=100, r=56, stroke_width=3))

# 18 yogurt with fruit
ITEMS['yogurt'] = (
    stick('M128 84 L168 30', '#c9d3db', 8)
    + z('ellipse', '#c9d3db', cx=170, cy=28, rx=10, ry=7, transform='rotate(-50 170 28)')
    + z('path', '#ffffff', d='M30 102 Q36 70 70 74 Q84 58 104 66 Q124 56 140 72 Q170 72 170 102Z')
    + z('path', '#e04b5a', d='M64 88 Q56 72 70 70 Q76 64 82 72 Q92 76 80 90 Q72 96 64 88Z')
    + dot(70, 80, 1.6, '#ffe27a') + dot(76, 84, 1.6, '#ffe27a')
    + z('circle', '#ffe27a', cx=104, cy=80, r=9) + dot(104, 80, 1.8, '#d9a66b')
    + z('circle', '#ffe27a', cx=122, cy=88, r=8) + dot(122, 88, 1.8, '#d9a66b')
    + ''.join(z('circle', '#8fb3e0', cx=x, cy=y, r=6) for x, y in ((90, 92), (142, 86), (48, 94)))
    + ''.join(s('rect', '#d9a66b', x=x, y=y, width=6, height=5, rx=1.5, stroke_width=1.5) for x, y in ((56, 98), (112, 96), (134, 98), (92, 74)))
    + z('path', '#f6a6b8', d='M26 102 L174 102 Q170 170 100 172 Q30 170 26 102Z')
    + mf(100, 132, 12, 22))

# 19 mixed nuts in a bowl
def almond(cx, cy, r):
    return z('path', '#d9a66b', d=f'M{cx} {cy-16} Q{cx+14} {cy} {cx} {cy+14} Q{cx-14} {cy} {cx} {cy-16}Z', transform=f'rotate({r} {cx} {cy})')
def peanut(cx, cy, r):
    return z('path', '#f5d58a', d=f'M{cx-18} {cy} Q{cx-18} {cy-11} {cx-8} {cy-10} Q{cx} {cy-6} {cx+8} {cy-10} Q{cx+18} {cy-11} {cx+18} {cy} Q{cx+18} {cy+11} {cx+8} {cy+10} Q{cx} {cy+6} {cx-8} {cy+10} Q{cx-18} {cy+11} {cx-18} {cy}Z', transform=f'rotate({r} {cx} {cy})')
def cashew(cx, cy, r):
    return z('path', '#f6e0c4', d=f'M{cx-14} {cy-8} Q{cx-20} {cy+12} {cx} {cy+12} Q{cx+18} {cy+10} {cx+16} {cy-8} Q{cx+8} {cy-10} {cx+6} {cy-2} Q{cx} {cy+4} {cx-6} {cy-2} Q{cx-8} {cy-10} {cx-14} {cy-8}Z', transform=f'rotate({r} {cx} {cy})')
def walnut(cx, cy):
    return (z('circle', '#d9a66b', cx=cx, cy=cy, r=17)
            + s('path', d=f'M{cx} {cy-14} Q{cx-4} {cy} {cx} {cy+14} M{cx-10} {cy-6} Q{cx-6} {cy} {cx-10} {cy+6} M{cx+10} {cy-6} Q{cx+6} {cy} {cx+10} {cy+6}', stroke_width=2))
ITEMS['nuts'] = (
    walnut(70, 84) + almond(100, 70, 30) + peanut(130, 82, -20)
    + cashew(48, 100, 10) + almond(152, 98, -40) + walnut(112, 98) + cashew(82, 104, -10)
    + z('path', '#8fc7e8', d='M28 108 L172 108 Q168 168 100 170 Q32 168 28 108Z')
    + mf(100, 134, 12, 22)
    + peanut(44, 178, 15) + almond(162, 172, 70))

# 20 cotton candy
ITEMS['cotton-candy'] = (
    z('path', '#ffffff', d='M84 126 L116 126 L104 184 L96 184Z')
    + s('path', d='M88 140 L112 140 M92 158 L108 158', stroke='#8fb3e0', stroke_width=3)
    + z('path', '#f6a6b8', d=blob(100, 80, 54, 50, 11, 0.16, 0.3))
    + s('path', d='M64 62 Q74 52 86 56 M120 52 Q134 52 140 64 M128 108 Q140 104 146 94', stroke='#f4f4f0', stroke_width=3)
    + mf(100, 84, 13, 24))
