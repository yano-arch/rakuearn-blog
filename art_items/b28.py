from art import z, s, dot, cheeks, face, OUT, CH
import re
ITEMS = {}


def mini_face(cx, cy, gap=12, ch=20, r=3.5):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+10, 6, 3.5)
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))


def stick(d, color, w=7):
    return s('path', d=d, stroke_width=w+3) + s('path', d=d, stroke=color, stroke_width=w-3)


def tf(d, sx=1, dx=0, dy=0, mirror=False):
    """transform a path made only of coordinate pairs (M/L/Q/C/Z)"""
    def rep(m):
        x, y = float(m.group(1)), float(m.group(2))
        if mirror:
            x = 200 - x
        return f'{x*sx+dx:g} {y*sx+dy:g}'
    return re.sub(r'(-?\d+(?:\.\d+)?)[ ,](-?\d+(?:\.\d+)?)', rep, d)


def plate(cy=150, rx=80, ry=26, color='#ffffff'):
    return (z('ellipse', color, cx=100, cy=cy, rx=rx, ry=ry)
            + s('ellipse', cx=100, cy=cy-2, rx=rx-18, ry=ry-9, stroke_width=2))


# 1 fried chicken
def drumstick(mirror=False, dx=0, dy=0):
    meat = 'M118 84 Q128 94 120 108 Q104 146 70 148 Q42 146 46 116 Q52 82 96 72 Q110 72 118 84Z'
    bone = 'M112 82 L140 56'
    crumbs = ['M62 104 Q66 98 72 100', 'M84 126 Q90 122 96 126', 'M60 130 Q64 126 70 128', 'M92 96 Q98 92 104 96']
    o = stick(tf(bone, 1, dx, dy, mirror), '#ffffff', 12)
    bx, by = (140, 56)
    if mirror:
        bx = 200 - bx
    o += z('circle', '#ffffff', cx=bx-5 + dx if not mirror else bx+5 + dx, cy=by-4 + dy, r=7)
    o += z('circle', '#ffffff', cx=bx+3 + dx if not mirror else bx-3 + dx, cy=by+4 + dy, r=7)
    o += z('path', '#d9a66b', d=tf(meat, 1, dx, dy, mirror))
    o += ''.join(s('path', d=tf(c, 1, dx, dy, mirror), stroke='#9a6a3f', stroke_width=2.5) for c in crumbs)
    return o


ITEMS['fried-chicken'] = (
    plate(156, 82, 24)
    + z('path', '#9ccf7a', d='M110 150 Q120 118 150 116 Q170 124 168 146 Q150 158 110 150Z')
    + drumstick(True, 4, 6)
    + drumstick(False, -6, 14)
    + z('path', '#ffe27a', d='M140 146 L170 146 Q168 164 155 166 Q142 164 140 146Z')
)

# 2 steak
ITEMS['steak'] = (
    plate(128, 84, 46)
    + z('path', '#9a6a3f', d='M44 118 Q42 90 76 86 Q104 84 118 96 Q136 108 130 130 Q124 156 92 154 Q50 152 44 118Z')
    + s('path', d='M54 104 Q60 96 70 92 Q90 88 104 96', stroke='#ffffff', stroke_width=4)
    + ''.join(s('path', d=f'M{x} {y} L{x+30} {y-22}', stroke='#5a4033', stroke_width=4) for x, y in ((60, 130), (76, 142), (92, 150)))
    + s('path', d='M60 108 L82 98', stroke='#5a4033', stroke_width=4)
    + z('path', '#e8735a', d='M134 112 L172 92 Q180 100 174 112Z')
    + s('path', d='M148 106 L150 111 M160 100 L162 105', stroke_width=2)
    + z('circle', '#7cc4a0', cx=150, cy=132, r=11) + z('circle', '#7cc4a0', cx=166, cy=126, r=9)
    + z('rect', '#9ccf7a', x=153, y=138, width=8, height=14, rx=3)
)

# 3 tacos
def taco(dx):
    o = z('path', '#9a6a3f', d=f'M{dx+30} 112 Q{dx+40} 92 {dx+70} 92 Q{dx+100} 92 {dx+110} 112Z')
    o += z('path', '#9ccf7a', d=f'M{dx+26} 114 Q{dx+30} 98 {dx+42} 102 Q{dx+48} 88 {dx+60} 96 Q{dx+70} 84 {dx+80} 96 Q{dx+92} 88 {dx+98} 102 Q{dx+110} 98 {dx+114} 114Z')
    o += s('circle', '#e04b5a', cx=dx+52, cy=100, r=6, stroke_width=2.5) + s('circle', '#e04b5a', cx=dx+84, cy=100, r=6, stroke_width=2.5)
    o += s('rect', '#ffe27a', x=dx+64, y=94, width=10, height=8, rx=2, stroke_width=2)
    o += z('path', '#f5d58a', d=f'M{dx+22} 112 Q{dx+24} 168 {dx+70} 168 Q{dx+116} 168 {dx+118} 112 Q{dx+100} 128 {dx+70} 128 Q{dx+40} 128 {dx+22} 112Z')
    o += ''.join(dot(dx+x, y, 2.5, '#d9a66b') for x, y in ((46, 144), (66, 154), (90, 146), (78, 138), (56, 158)))
    return o


ITEMS['tacos'] = taco(52) + taco(-8) + s('path', d='M26 178 L178 178', stroke_width=2.5)

# 4 gyoza
def gyoza(cx, cy, fc=False):
    o = z('path', '#f6e0c4', d=f'M{cx-30} {cy+14} Q{cx-34} {cy-26} {cx} {cy-28} Q{cx+34} {cy-26} {cx+30} {cy+14} Q{cx} {cy+20} {cx-30} {cy+14}Z')
    o += s('path', '#f5b971', d=f'M{cx-30} {cy+14} Q{cx} {cy+20} {cx+30} {cy+14} Q{cx+30} {cy+6} {cx+26} {cy+4} Q{cx} {cy+10} {cx-26} {cy+4} Q{cx-30} {cy+6} {cx-30} {cy+14}Z', stroke_width=2.5)
    o += ''.join(s('path', d=f'M{cx+x} {cy-25} Q{cx+x+4} {cy-20} {cx+x+2} {cy-14}', stroke_width=2.5) for x in (-16, -6, 4, 14))
    if fc:
        o += dot(cx-9, cy-4, 3) + dot(cx+9, cy-4, 3) + cheeks(cx-17, cx+17, cy+3, 5, 3) + s('path', d=f'M{cx-4} {cy+2} Q{cx} {cy+6} {cx+4} {cy+2}', stroke_width=2.5)
    return o


ITEMS['gyoza'] = (
    plate(140, 84, 36, '#8fb3e0')
    + gyoza(62, 122) + gyoza(138, 122) + gyoza(100, 140, True)
    + z('ellipse', '#ffffff', cx=160, cy=60, rx=22, ry=10)
    + z('path', '#ffffff', d='M138 60 Q140 80 160 80 Q180 80 182 60Z')
    + s('ellipse', '#9a6a3f', cx=160, cy=60, rx=16, ry=6, stroke_width=2)
)

# 5 bento box
ITEMS['bento-box'] = (
    z('rect', '#e04b5a', x=26, y=44, width=148, height=118, rx=14)
    + s('rect', '#f4f4f0', x=36, y=54, width=128, height=98, rx=8)
    + s('path', d='M98 54 L98 152 M98 104 L164 104', stroke_width=3)
    + z('rect', '#ffffff', x=42, y=60, width=48, height=84, rx=6)
    + dot(66, 102, 8, '#e04b5a')
    + ''.join(s('ellipse', cx=x, cy=y, rx=3, ry=2, stroke_width=1.5) for x, y in ((52, 72), (78, 76), (54, 128), (80, 130), (60, 86), (76, 116)))
    + z('rect', '#ffe27a', x=106, y=62, width=24, height=34, rx=4) + z('rect', '#ffe27a', x=132, y=62, width=24, height=34, rx=4)
    + s('path', d='M110 72 Q118 68 126 72 M136 72 Q144 68 152 72', stroke_width=2)
    + z('path', '#e8735a', d='M106 116 Q110 108 122 110 L136 112 Q144 114 140 124 Q136 132 124 130 L112 128 Q102 126 106 116Z')
    + s('path', d='M114 116 L118 122 M124 116 L128 122', stroke_width=2)
    + z('circle', '#7cc4a0', cx=146, cy=134, r=9) + z('circle', '#7cc4a0', cx=154, cy=124, r=7)
    + z('path', '#9ccf7a', d='M108 134 Q118 128 128 136 Q120 146 108 134Z')
)

# 6 takoyaki
def tako(cx, cy):
    o = z('circle', '#d9a66b', cx=cx, cy=cy, r=17)
    o += s('path', '#8b6b4f', d=f'M{cx-15} {cy-6} Q{cx-12} {cy-17} {cx} {cy-17} Q{cx+12} {cy-17} {cx+15} {cy-6} Q{cx+8} {cy-2} {cx} {cy-4} Q{cx-8} {cy-2} {cx-15} {cy-6}Z', stroke_width=2)
    o += s('path', d=f'M{cx-9} {cy-12} L{cx-3} {cy-8} L{cx+3} {cy-13} L{cx+9} {cy-8}', stroke='#ffffff', stroke_width=2.5)
    o += dot(cx-5, cy-15, 1.8, '#7cc4a0') + dot(cx+7, cy-14, 1.8, '#7cc4a0')
    return o


ITEMS['takoyaki'] = (
    z('path', '#f6e0c4', d='M26 116 L174 116 L158 166 L42 166Z')
    + tako(56, 108) + tako(100, 102) + tako(144, 108)
    + tako(78, 126) + tako(122, 126)
    + s('path', d='M150 104 L170 40', stroke_width=7) + s('path', d='M150 104 L170 40', stroke='#f5d58a', stroke_width=3)
    + z('path', '#f6e0c4', d='M30 140 L170 140 L158 166 L42 166Z')
)

# 7 rice bowl
ITEMS['rice-bowl'] = (
    z('path', '#ffffff', d='M40 104 Q42 50 100 48 Q158 50 160 104Z')
    + ''.join(s('ellipse', cx=x, cy=y, rx=4, ry=2.5, stroke_width=1.5) for x, y in ((80, 66), (104, 60), (124, 70), (66, 86), (92, 80), (118, 88), (142, 90)))
    + z('path', '#8fb3e0', d='M30 100 L170 100 Q168 156 120 164 L80 164 Q32 156 30 100Z')
    + z('rect', '#8fb3e0', x=76, y=162, width=48, height=12, rx=3)
    + mini_face(100, 122, 14, 26)
    + s('path', d='M40 112 Q46 120 52 112 M148 112 Q154 120 160 112', stroke='#ffffff', stroke_width=3)
    + stick('M126 40 L184 74', '#d9a66b', 7) + stick('M118 46 L180 84', '#d9a66b', 7)
)

# 8 miso soup
ITEMS['miso-soup'] = (
    s('path', d='M80 50 Q72 40 80 30 Q88 20 80 10', stroke_width=2.5) + s('path', d='M120 50 Q112 40 120 30 Q128 20 120 10', stroke_width=2.5)
    + z('path', '#e04b5a', d='M28 82 L172 82 Q170 146 124 160 L76 160 Q30 146 28 82Z')
    + z('rect', '#e04b5a', x=72, y=158, width=56, height=14, rx=3)
    + s('ellipse', '#d9a66b', cx=100, cy=84, rx=72, ry=18)
    + s('rect', '#ffffff', x=66, y=76, width=14, height=12, rx=2, stroke_width=2.5)
    + s('rect', '#ffffff', x=110, y=80, width=14, height=12, rx=2, stroke_width=2.5)
    + s('path', '#5b6b7a', d='M86 92 Q94 80 104 88 Q96 96 86 92Z', stroke_width=2)
    + s('path', '#5b6b7a', d='M132 78 Q142 72 148 80 Q140 86 132 78Z', stroke_width=2)
    + ''.join(s('circle', '#9ccf7a', cx=x, cy=y, r=3.5, stroke_width=2) for x, y in ((52, 84), (96, 74), (140, 90), (122, 72)))
    + s('path', d='M48 112 L152 112', stroke='#5b6b7a', stroke_width=3)
)

# 9 shrimp tempura
def tempura(y, dx):
    o = z('path', '#e8735a', d=f'M{dx+150} {y} L{dx+176} {y-16} L{dx+172} {y+2} L{dx+178} {y+16}Z')
    o += z('path', '#f5d58a', d=f'M{dx+30} {y} Q{dx+30} {y-16} {dx+56} {y-18} L{dx+120} {y-14} Q{dx+150} {y-10} {dx+156} {y} Q{dx+150} {y+10} {dx+120} {y+14} L{dx+56} {y+18} Q{dx+30} {y+16} {dx+30} {y}Z')
    o += ''.join(s('path', d=f'M{dx+x} {y-8+(i%2)*10} Q{dx+x+5} {y-12+(i%2)*10} {dx+x+10} {y-8+(i%2)*10}', stroke='#d9a66b', stroke_width=2.5) for i, x in enumerate((46, 66, 86, 106, 126)))
    return o


ITEMS['tempura'] = (
    plate(146, 84, 30, '#5b6b7a')
    + z('path', '#ffffff', d='M40 140 L68 60 L166 78 L146 156Z')
    + tempura(92, -8) + tempura(126, -2)
)

# 10 grilled fish
ITEMS['grilled-fish'] = (
    z('rect', '#f4f4f0', x=18, y=96, width=166, height=72, rx=16)
    + z('path', '#b9a99c', d='M40 128 Q60 96 104 96 Q140 98 150 118 L172 100 L166 128 L172 156 L150 138 Q140 158 104 160 Q60 160 40 128Z')
    + s('path', '#8fb3e0', d='M48 122 Q68 102 104 102 Q132 104 146 120 Q120 112 100 118 Q76 124 48 122Z', stroke_width=2)
    + s('circle', '#ffffff', cx=60, cy=124, r=7, stroke_width=2.5) + dot(61, 124, 3)
    + s('path', d='M78 112 Q74 128 80 146', stroke_width=2.5)
    + ''.join(s('path', d=f'M{x} 132 L{x+8} 120', stroke='#5a4033', stroke_width=4) for x in (98, 114, 130))
    + z('path', '#ffffff', d='M136 88 Q138 72 150 74 Q156 64 166 70 Q178 74 176 88 Q156 94 136 88Z')
    + z('path', '#ffe27a', d='M20 80 L52 72 Q56 92 42 98 Q26 96 20 80Z')
    + s('path', d='M30 80 L42 92 M38 77 L44 92', stroke_width=2)
)

# 11 pancakes
ITEMS['pancakes'] = (
    plate(158, 84, 22)
    + z('path', '#f5b971', d='M38 104 L162 104 L162 148 Q100 162 38 148Z')
    + s('path', d='M38 118 Q100 132 162 118 M38 133 Q100 147 162 133', stroke_width=2.5)
    + z('ellipse', '#f6e0c4', cx=100, cy=104, rx=62, ry=16)
    + z('path', '#9a6a3f', d='M52 100 Q60 88 100 88 Q140 88 148 100 Q150 112 140 116 Q136 136 132 116 Q100 122 72 116 Q68 140 62 116 Q50 112 52 100Z')
    + z('rect', '#ffe27a', x=86, y=78, width=28, height=20, rx=4)
)

# 12 croissant
ITEMS['croissant'] = (
    z('path', '#f5b971', d='M24 132 Q26 114 44 112 Q56 114 60 124 Q50 140 30 142 Q22 140 24 132Z')
    + z('path', '#f5b971', d='M176 132 Q174 114 156 112 Q144 114 140 124 Q150 140 170 142 Q178 140 176 132Z')
    + z('path', '#f5b971', d='M50 128 Q44 96 66 88 Q80 86 86 96 Q86 124 70 138 Q56 140 50 128Z')
    + z('path', '#f5b971', d='M150 128 Q156 96 134 88 Q120 86 114 96 Q114 124 130 138 Q144 140 150 128Z')
    + z('path', '#f5b971', d='M78 132 Q70 80 100 70 Q130 80 122 132 Q100 146 78 132Z')
    + mini_face(100, 104, 10, 16, 3)
)

# 13 toast with butter
ITEMS['toast-butter'] = (
    z('path', '#d9a66b', d='M44 172 L44 92 Q28 84 32 64 Q40 36 100 36 Q160 36 168 64 Q172 84 156 92 L156 172Z')
    + s('path', '#f5d58a', d='M56 162 L56 86 Q44 80 46 66 Q52 48 100 48 Q148 48 154 66 Q156 80 144 86 L144 162Z', stroke_width=2.5)
    + z('path', '#ffe27a', d='M76 76 L118 70 L126 98 L84 106Z')
    + mini_face(100, 128, 14, 24)
)

# 14 cereal with milk
ITEMS['cereal-bowl'] = (
    stick('M128 92 L176 40', '#c9d3db', 9)
    + s('ellipse', '#c9d3db', cx=178, cy=36, rx=10, ry=7)
    + s('ellipse', '#ffffff', cx=100, cy=96, rx=74, ry=20)
    + ''.join(s('circle', c, cx=x, cy=y, r=7, stroke_width=2.5) + dot(x, y, 2, OUT)
              for x, y, c in ((56, 96, '#f5b971'), (78, 88, '#e8735a'), (100, 98, '#ffe27a'), (122, 88, '#f5b971'), (146, 96, '#9ccf7a'), (88, 104, '#f6a6b8'), (114, 106, '#f5b971'), (66, 106, '#ffe27a'), (136, 106, '#e8735a'), (100, 84, '#9ccf7a')))
    + z('path', '#8fc7e8', d='M26 96 Q100 126 174 96 Q170 148 124 160 L76 160 Q30 148 26 96Z')
    + z('rect', '#8fc7e8', x=74, y=158, width=52, height=14, rx=3)
    + mini_face(100, 132, 14, 26)
)

# 15 donut
ITEMS['donut'] = (
    z('path', '#f5b971', fill_rule='evenodd', d='M100 40 Q166 40 166 106 Q166 168 100 168 Q34 168 34 106 Q34 40 100 40Z M100 88 Q84 88 84 104 Q84 120 100 120 Q116 120 116 104 Q116 88 100 88Z')
    + s('path', '#f6a6b8', fill_rule='evenodd', d='M100 46 Q158 44 160 100 Q162 128 150 132 Q140 128 138 140 Q124 152 112 144 Q100 152 88 146 Q76 152 64 140 Q56 128 46 130 Q36 120 40 100 Q42 44 100 46Z M100 82 Q78 82 78 104 Q78 126 100 126 Q122 126 122 104 Q122 82 100 82Z')
    + ''.join(s('path', d=f'M{x} {y} L{x+dx} {y+dy}', stroke=c, stroke_width=4)
              for x, y, dx, dy, c in ((70, 66, 8, -3, '#ffe27a'), (96, 58, 7, 4, '#8fc7e8'), (128, 64, 6, 6, '#9ccf7a'), (146, 92, -2, 8, '#ffffff'), (56, 96, 4, 7, '#8fc7e8'),
                                      (130, 116, 8, 2, '#ffe27a'), (66, 120, 7, -4, '#9ccf7a'), (100, 134, 8, 0, '#ffe27a'), (80, 74, -2, 8, '#ffffff'), (118, 76, 8, -2, '#e8735a')))
)

# 16 cupcake
ITEMS['cupcake'] = (
    z('path', '#8fc7e8', d='M50 112 L150 112 L136 178 L64 178Z')
    + s('path', d='M70 114 L76 176 M90 114 L92 176 M110 114 L108 176 M130 114 L124 176', stroke_width=2.5)
    + z('path', '#f6a6b8', d='M42 116 Q34 100 52 94 Q50 74 74 74 Q76 56 100 56 Q124 56 126 74 Q150 74 148 94 Q166 100 158 116Z')
    + s('path', d='M56 104 Q100 88 144 104 M72 84 Q100 72 128 84', stroke_width=2.5)
    + s('path', d='M100 54 Q102 40 112 34', stroke_width=3)
    + z('circle', '#e04b5a', cx=100, cy=48, r=11)
    + mini_face(100, 140, 13, 22)
)

# 17 strawberry shortcake slice
ITEMS['cake-slice'] = (
    z('path', '#ffffff', d='M36 98 L148 98 L176 70 L96 48Z')
    + z('rect', '#f5d58a', x=36, y=98, width=112, height=74)
    + z('path', '#f5d58a', d='M148 98 L176 70 L176 144 L148 172Z')
    + s('rect', '#ffffff', x=36, y=124, width=112, height=16, stroke_width=2.5)
    + s('path', '#ffffff', d='M148 124 L176 98 L176 112 L148 140Z', stroke_width=2.5)
    + ''.join(s('path', '#e04b5a', d=f'M{x-8} 132 Q{x} 120 {x+8} 132 Q{x} 140 {x-8} 132Z', stroke_width=2) for x in (54, 82, 110, 136))
    + s('path', '#ffffff', d='M36 98 L148 98 L148 108 Q134 114 122 106 Q110 114 98 106 Q86 114 74 106 Q62 114 50 106 Q42 112 36 106Z', stroke_width=2.5)
    + z('path', '#ffffff', d='M88 86 Q84 70 102 66 Q118 70 114 86Z')
    + z('path', '#e04b5a', d='M86 62 Q86 34 102 34 Q118 34 118 62 Q102 74 86 62Z')
    + s('path', '#9ccf7a', d='M92 38 L102 30 L112 38 L102 42Z', stroke_width=2)
    + ''.join(dot(x, y, 1.6, '#ffe27a') for x, y in ((96, 48), (108, 48), (102, 58), (94, 58), (110, 58)))
)

# 18 custard pudding
ITEMS['pudding'] = (
    plate(164, 80, 18, '#8fb3e0')
    + z('path', '#ffe27a', d='M58 160 L70 70 Q100 62 130 70 L142 160 Q100 172 58 160Z')
    + z('path', '#9a6a3f', d='M70 70 Q100 60 130 70 L132 84 Q126 94 122 84 Q112 92 104 86 Q96 100 90 86 Q80 92 76 84 Q72 96 68 86Z')
    + z('path', '#ffffff', d='M84 64 Q80 46 100 44 Q120 46 116 64 Q100 70 84 64Z')
    + z('circle', '#e04b5a', cx=100, cy=36, r=10)
    + s('path', d='M100 26 Q104 16 112 14', stroke_width=2.5)
    + mini_face(100, 122, 14, 24)
)

# 19 macarons
def macaron(cx, cy, c, fill='#ffffff'):
    o = z('path', c, d=f'M{cx-32} {cy+16} Q{cx-34} {cy+6} {cx-30} {cy+4} L{cx+30} {cy+4} Q{cx+34} {cy+6} {cx+32} {cy+16} Q{cx} {cy+24} {cx-32} {cy+16}Z')
    o += s('rect', fill, x=cx-30, y=cy-4, width=60, height=10, rx=4, stroke_width=2.5)
    o += z('path', c, d=f'M{cx-32} {cy-4} Q{cx-34} {cy-26} {cx} {cy-26} Q{cx+34} {cy-26} {cx+32} {cy-4} Q{cx} {cy+2} {cx-32} {cy-4}Z')
    o += s('path', d=f'M{cx-28} {cy-4} Q{cx-24} {cy-8} {cx-20} {cy-4} Q{cx-16} {cy-8} {cx-12} {cy-4} M{cx+12} {cy-4} Q{cx+16} {cy-8} {cx+20} {cy-4} Q{cx+24} {cy-8} {cx+28} {cy-4}', stroke_width=2)
    return o


ITEMS['macarons'] = (
    macaron(100, 76, '#9ccf7a')
    + macaron(64, 136, '#f6a6b8')
    + macaron(136, 136, '#f5d58a')
    + dot(54, 119, 3) + dot(74, 119, 3) + cheeks(46, 82, 125, 5, 3)
    + s('path', d='M60 123 Q64 127 68 123', stroke_width=2.5)
)

# 20 cookies
CHIPS = ((-14, -10), (12, -16), (16, 10), (-10, 14), (0, 0))


def cookie(cx, cy, r):
    return (z('circle', '#d9a66b', cx=cx, cy=cy, r=r)
            + ''.join(s('path', '#8b6b4f', d=f'M{cx+dx*r/36-4} {cy+dy*r/36+2} L{cx+dx*r/36} {cy+dy*r/36-4} L{cx+dx*r/36+4} {cy+dy*r/36+2}Z', stroke_width=2) for dx, dy in CHIPS))


ITEMS['cookies'] = (
    cookie(148, 70, 28)
    + z('path', '#d9a66b', d='M88 58 Q118 58 130 74 Q120 80 126 88 Q136 90 136 100 Q140 106 138 112 Q136 158 88 158 Q38 158 38 108 Q38 58 88 58Z')
    + ''.join(s('path', '#8b6b4f', d=f'M{x-4} {y+2} L{x} {y-4} L{x+4} {y+2}Z', stroke_width=2) for x, y in ((64, 80), (100, 76), (54, 132), (112, 136), (90, 146), (122, 102)))
    + mini_face(86, 108, 14, 24)
    + cookie(150, 150, 26)
)
