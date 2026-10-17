from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def mini_face(cx, cy, gap=12, ch=20, r=3.5, cr=(6, 3.5)):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+10, cr[0], cr[1])
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))


def tiny_face(cx, cy):
    return (dot(cx-7, cy, 2.6)+dot(cx+7, cy, 2.6)+cheeks(cx-12, cx+12, cy+6, 4, 2.5)
            + s('path', d=f'M{cx-3} {cy+5} Q{cx} {cy+8} {cx+3} {cy+5}', stroke_width=2))


def leaf(d, color='#9ccf7a'):
    return z('path', color, d=d)


# 1 strawberry
ITEMS['strawberry'] = (
    z('path', '#e04b5a', d='M100 62 Q150 52 158 90 Q160 128 104 176 Q100 180 96 176 Q40 128 42 90 Q50 52 100 62Z')
    + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.2" ry="3.4" fill="#ffe27a" stroke="none"/>'
              for x, y in ((66, 88), (134, 88), (58, 112), (142, 112), (74, 140), (126, 140), (100, 160), (86, 82), (114, 82), (100, 148)))
    + leaf('M100 70 L66 62 L84 54 L74 38 L96 48 L100 30 L104 48 L126 38 L116 54 L134 62Z')
    + mini_face(100, 108, 14, 26))

# 2 grapes
G = [(100, 150), (86, 126), (114, 126), (72, 102), (100, 102), (128, 102), (60, 78), (86, 78), (114, 78), (140, 78)]
ITEMS['grapes'] = (
    s('path', d='M100 64 Q100 46 110 32', stroke_width=5)
    + leaf('M104 52 Q120 26 154 34 Q140 62 104 52Z')
    + ''.join(z('circle', '#a98bd0', cx=x, cy=y, r=16) + s('path', d=f'M{x-8} {y-6} Q{x-6} {y-10} {x-2} {y-11}', stroke='#ffffff', stroke_width=2.5)
              for x, y in G)
    + tiny_face(100, 104))

# 3 orange
ITEMS['orange'] = (
    z('circle', '#f5b971', cx=100, cy=112, r=60)
    + s('path', d='M100 54 L100 42', stroke_width=5)
    + leaf('M102 48 Q120 26 150 36 Q134 60 102 48Z')
    + ''.join(dot(x, y, 1.6, '#e8735a') for x, y in ((62, 98), (70, 140), (138, 98), (130, 142), (80, 72), (122, 72), (100, 160)))
    + s('path', d='M62 112 Q60 96 68 84', stroke='#ffffff', stroke_width=4)
    + mini_face(100, 114, 14, 26))

# 4 lemon
ITEMS['lemon'] = (
    z('path', '#ffe27a', d='M30 110 Q28 102 38 98 Q54 58 100 56 Q146 58 162 98 Q172 102 170 110 Q168 116 160 120 Q146 162 100 164 Q54 162 40 120 Q32 116 30 110Z')
    + leaf('M104 60 Q118 34 150 38 Q136 66 104 60Z')
    + s('path', d='M54 104 Q56 86 68 76', stroke='#ffffff', stroke_width=4)
    + mini_face(100, 108, 14, 26))

# 5 watermelon slice
def half(r, cy=62):
    return f'M{100-r} {cy} L{100+r} {cy} A{r} {r} 0 0 1 {100-r} {cy}Z'
ITEMS['watermelon'] = (
    z('path', '#7cc4a0', d=half(80))
    + s('path', '#f4f4f0', d=half(70), stroke_width=2.5)
    + s('path', '#f07a8a', d=half(62), stroke_width=2.5)
    + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="4" fill="{OUT}" stroke="none" transform="rotate({a} {x} {y})"/>'
              for x, y, a in ((56, 76, 20), (144, 76, -20), (70, 100, 30), (130, 100, -30), (90, 116, 10), (110, 116, -10), (100, 70, 0)))
    + mini_face(100, 86, 14, 24))

# 6 peach
ITEMS['peach'] = (
    leaf('M98 62 Q74 34 50 46 Q66 70 98 62Z')
    + leaf('M102 62 Q126 34 150 46 Q134 70 102 62Z', '#7cc4a0')
    + z('path', '#f6a6b8', d='M100 66 Q62 50 46 96 Q36 144 82 168 Q100 176 118 168 Q164 144 154 96 Q138 50 100 66Z')
    + s('path', d='M100 68 Q84 100 92 132', stroke_width=2.5)
    + s('path', d='M60 104 Q60 88 70 78', stroke='#ffffff', stroke_width=4)
    + mini_face(112, 122, 12, 22))

# 7 cherries
ITEMS['cherries'] = (
    s('path', d='M68 128 Q78 76 108 40', stroke_width=4)
    + s('path', d='M134 120 Q128 76 108 40', stroke_width=4)
    + leaf('M108 42 Q130 20 158 32 Q138 56 108 42Z')
    + z('circle', '#e04b5a', cx=66, cy=146, r=28)
    + z('circle', '#e04b5a', cx=136, cy=138, r=28)
    + s('path', d='M50 140 Q50 130 58 126', stroke='#ffffff', stroke_width=3.5)
    + s('path', d='M120 132 Q120 122 128 118', stroke='#ffffff', stroke_width=3.5)
    + tiny_face(68, 150) + tiny_face(138, 142))

# 8 pineapple
def clip_line(x0, y0, dx, dy, cx, cy, rx, ry):
    # intersection of line p = (x0,y0)+t(dx,dy) with ellipse
    a = (dx/rx)**2 + (dy/ry)**2
    b = 2*((x0-cx)*dx/rx**2 + (y0-cy)*dy/ry**2)
    c = ((x0-cx)/rx)**2 + ((y0-cy)/ry)**2 - 1
    disc = b*b - 4*a*c
    if disc <= 0:
        return ''
    t1 = (-b - math.sqrt(disc))/(2*a); t2 = (-b + math.sqrt(disc))/(2*a)
    return f'M{x0+t1*dx:.1f} {y0+t1*dy:.1f} L{x0+t2*dx:.1f} {y0+t2*dy:.1f}'
PCX, PCY, PRX, PRY = 100, 128, 42, 50
hatch = ''.join(s('path', d=clip_line(PCX+k, PCY, 1, sg, PCX, PCY, PRX-4, PRY-4), stroke='#d9a66b', stroke_width=2.5)
                for k in range(-90, 91, 22) for sg in (1, -1))
ITEMS['pineapple'] = (
    leaf('M100 90 L66 56 L84 62 L76 32 L94 54 L100 22 L106 54 L124 32 L116 62 L134 56Z', '#7cc4a0')
    + z('ellipse', '#ffc94d', cx=PCX, cy=PCY, rx=PRX, ry=PRY)
    + hatch
    + s('ellipse', '#ffc94d', cx=100, cy=132, rx=24, ry=14, stroke='none')
    + mini_face(100, 126, 12, 20))

# 9 melon (net melon)
ITEMS['melon'] = (
    z('circle', '#9ccf7a', cx=100, cy=114, r=60)
    + ''.join(s('path', d=d, stroke='#f4f4f0', stroke_width=2.5) for d in (
        'M70 62 Q56 92 64 118 Q70 146 62 166', 'M100 56 Q90 84 98 102', 'M130 62 Q144 92 136 118 Q130 146 138 166',
        'M46 100 Q70 92 82 100', 'M118 100 Q130 92 154 100', 'M50 142 Q66 134 76 142', 'M124 142 Q134 134 150 142',
        'M100 148 Q92 160 100 172'))
    + s('path', d='M100 56 L100 36', stroke_width=6)
    + s('path', d='M86 36 L114 36', stroke_width=6)
    + s('path', d='M86 36 L114 36', stroke='#9ccf7a', stroke_width=2)
    + s('ellipse', '#9ccf7a', cx=100, cy=126, rx=30, ry=16, stroke='none')
    + mini_face(100, 118, 14, 24))

# 10 kiwi (whole + cut)
seeds = ''.join(f'<ellipse cx="{124+22*math.cos(a):.1f}" cy="{126+22*math.sin(a):.1f}" rx="1.8" ry="3.4" fill="{OUT}" stroke="none" '
                f'transform="rotate({math.degrees(a)+90:.0f} {124+22*math.cos(a):.1f} {126+22*math.sin(a):.1f})"/>'
                for a in [i*math.pi/7 for i in range(14)])
ITEMS['kiwi'] = (
    z('ellipse', '#d9a66b', cx=72, cy=88, rx=44, ry=36)
    + ''.join(s('path', d=f'M{x} {y} l3 -2', stroke='#9a6a3f', stroke_width=2) for x, y in ((48, 76), (60, 64), (92, 66), (100, 84), (46, 98), (66, 110)))
    + mini_face(72, 86, 12, 22)
    + z('circle', '#d9a66b', cx=124, cy=126, r=48)
    + s('circle', '#9ccf7a', cx=124, cy=126, r=40, stroke_width=2.5)
    + ''.join(s('path', d=f'M{124+16*math.cos(a):.1f} {126+16*math.sin(a):.1f} L{124+34*math.cos(a):.1f} {126+34*math.sin(a):.1f}',
                stroke='#f4f4f0', stroke_width=1.5) for a in [i*math.pi/7+0.22 for i in range(14)])
    + s('ellipse', '#f4f4f0', cx=124, cy=126, rx=13, ry=10, stroke_width=2.5)
    + seeds)

# 11 pear
ITEMS['pear'] = (
    s('path', d='M100 54 Q100 38 108 28', stroke_width=5)
    + leaf('M104 44 Q122 22 152 30 Q136 54 104 44Z')
    + z('path', '#f5d58a', d='M100 50 Q120 50 122 76 Q124 98 144 118 Q162 142 150 164 Q134 184 100 182 Q66 184 50 164 Q38 142 56 118 Q76 98 78 76 Q80 50 100 50Z')
    + s('path', d='M62 132 Q62 118 72 108', stroke='#ffffff', stroke_width=4)
    + ''.join(dot(x, y, 1.6, '#d9a66b') for x, y in ((86, 80), (114, 90), (70, 158), (134, 156), (100, 170)))
    + mini_face(100, 136, 14, 26))

# 12 mango
ITEMS['mango'] = (
    z('path', '#ffc94d', d='M48 92 Q70 46 122 50 Q170 56 170 106 Q170 158 118 168 Q66 176 46 138 Q36 116 48 92Z')
    + s('path', '#e8735a', d='M52 92 Q72 52 120 54 Q140 56 152 66 Q118 66 96 84 Q74 102 50 110Z', stroke='none')
    + s('path', d='M48 92 Q70 46 122 50 Q170 56 170 106 Q170 158 118 168 Q66 176 46 138 Q36 116 48 92Z')
    + s('path', d='M64 56 L56 44', stroke_width=5)
    + leaf('M58 48 Q48 22 20 30 Q32 56 58 48Z')
    + mini_face(112, 116, 14, 24))

# 13 blueberries
def calyx(x, y, r=7):
    pts = ' '.join(f'M{x} {y} L{x+r*math.cos(a):.1f} {y+r*math.sin(a):.1f}' for a in [i*2*math.pi/5 - math.pi/2 for i in range(5)])
    return s('circle', '#5b6b7a', cx=x, cy=y, r=r-1, stroke_width=2) + s('path', d=pts, stroke='#c9d3db', stroke_width=1.6)
ITEMS['blueberries'] = (
    z('circle', '#8fb3e0', cx=66, cy=96, r=30) + calyx(66, 80)
    + z('circle', '#8fb3e0', cx=136, cy=92, r=30) + calyx(136, 76)
    + leaf('M100 66 Q104 36 132 30 Q130 58 100 66Z')
    + z('circle', '#8fb3e0', cx=100, cy=134, r=38) + calyx(100, 110, 8)
    + s('path', d='M74 128 Q74 116 82 108', stroke='#ffffff', stroke_width=4)
    + mini_face(100, 138, 13, 22))

# 14 avocado half
ITEMS['avocado'] = (
    z('path', '#7cc4a0', d='M100 30 Q128 30 134 64 Q138 90 154 110 Q172 140 154 166 Q134 186 100 184 Q66 186 46 166 Q28 140 46 110 Q62 90 66 64 Q72 30 100 30Z')
    + s('path', '#f5d58a', d='M100 42 Q119 42 124 70 Q128 94 144 114 Q158 140 144 160 Q128 176 100 175 Q72 176 56 160 Q42 140 56 114 Q72 94 76 70 Q81 42 100 42Z', stroke_width=2.5)
    + z('circle', '#d9a66b', cx=100, cy=138, r=26)
    + s('path', d='M86 126 Q90 120 96 118', stroke='#ffffff', stroke_width=3)
    + mini_face(100, 138, 10, 17, 3, (4.5, 3)))

# 15 persimmon
ITEMS['persimmon'] = (
    z('ellipse', '#e8735a', cx=100, cy=118, rx=66, ry=54)
    + s('path', d='M54 112 Q56 96 66 86', stroke='#ffffff', stroke_width=4)
    + leaf('M100 72 Q74 52 50 66 Q68 82 100 72Z M100 72 Q126 52 150 66 Q132 82 100 72Z M100 72 Q76 78 70 96 Q92 96 100 72Z M100 72 Q124 78 130 96 Q108 96 100 72Z')
    + s('rect', '#9a6a3f', x=96, y=60, width=8, height=12, rx=2)
    + mini_face(100, 124, 14, 26))

# 16 carrot
ITEMS['carrot'] = (
    leaf('M98 72 Q78 50 72 26 Q94 34 100 70Z')
    + leaf('M100 72 Q98 44 108 20 Q120 44 104 72Z', '#7cc4a0')
    + leaf('M102 72 Q118 46 142 36 Q134 64 104 74Z')
    + z('path', '#e8735a', d='M64 72 Q100 60 136 72 Q130 124 104 176 Q100 182 96 176 Q70 124 64 72Z')
    + ''.join(s('path', d=d, stroke_width=2.5) for d in ('M78 116 L87 116', 'M111 132 L119 132', 'M88 154 L95 154'))
    + mini_face(100, 94, 12, 20))

# 17 tomato
ITEMS['tomato'] = (
    z('path', '#e04b5a', d='M100 64 Q154 58 164 104 Q168 150 124 168 Q100 176 76 168 Q32 150 36 104 Q46 58 100 64Z')
    + s('path', d='M58 102 Q58 88 70 80', stroke='#ffffff', stroke_width=4)
    + leaf('M100 72 L74 84 L84 70 L62 62 L88 62 L84 46 L100 58 L116 46 L112 62 L138 62 L116 70 L126 84Z', '#7cc4a0')
    + s('path', d='M100 60 Q100 46 106 38', stroke_width=5)
    + mini_face(100, 114, 14, 26))

# 18 broccoli
ITEMS['broccoli'] = (
    z('path', '#9ccf7a', d='M80 112 Q86 140 78 176 Q100 184 122 176 Q114 140 120 112Z')
    + z('circle', '#7cc4a0', cx=62, cy=92, r=26)
    + z('circle', '#7cc4a0', cx=138, cy=92, r=26)
    + z('circle', '#7cc4a0', cx=100, cy=66, r=32)
    + z('circle', '#7cc4a0', cx=80, cy=104, r=24)
    + z('circle', '#7cc4a0', cx=120, cy=104, r=24)
    + ''.join(s('path', d=f'M{x-5} {y} Q{x} {y-6} {x+5} {y}', stroke_width=2) for x, y in ((92, 56), (110, 64), (56, 88), (144, 86), (78, 100), (122, 100)))
    + mini_face(100, 144, 9, 15, 3, (4.5, 3)))

# 19 cabbage
ITEMS['cabbage'] = (
    z('circle', '#9ccf7a', cx=100, cy=112, r=58)
    + s('path', d='M54 82 Q70 52 100 54 Q84 66 80 92', stroke_width=2.5)
    + s('path', d='M146 82 Q130 52 100 54 Q116 66 120 92', stroke_width=2.5)
    + leaf('M100 172 Q44 170 36 120 Q34 92 48 76 Q60 136 100 172Z', '#7cc4a0')
    + leaf('M100 172 Q156 170 164 120 Q166 92 152 76 Q140 136 100 172Z', '#7cc4a0')
    + s('path', d='M100 56 L100 80', stroke='#f4f4f0', stroke_width=3)
    + s('path', d='M64 72 Q72 82 70 98', stroke='#f4f4f0', stroke_width=3)
    + s('path', d='M136 72 Q128 82 130 98', stroke='#f4f4f0', stroke_width=3)
    + mini_face(100, 118, 14, 26))

# 20 onion
ON = 'M100 32 Q104 62 140 84 Q172 108 158 146 Q142 174 100 174 Q58 174 42 146 Q28 108 60 84 Q96 62 100 32Z'
ITEMS['onion'] = (
    ''.join(s('path', d=f'M{x} 172 Q{x+dx} 182 {x+2*dx} 186', stroke_width=2.5) for x, dx in ((86, -6), (96, -2), (104, 2), (114, 6)))
    + z('path', '#f5d58a', d=ON)
    + s('path', d='M100 34 Q74 70 72 120 Q74 152 86 172', stroke='#d9a66b', stroke_width=2.5)
    + s('path', d='M100 34 Q126 70 128 120 Q126 152 114 172', stroke='#d9a66b', stroke_width=2.5)
    + s('path', d='M96 30 Q100 18 108 14', stroke_width=4)
    + s('ellipse', '#f5d58a', cx=100, cy=128, rx=26, ry=16, stroke='none')
    + mini_face(100, 120, 14, 26))
