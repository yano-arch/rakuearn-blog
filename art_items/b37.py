from art import z, s, dot, cheeks, face, OUT, CH
import math

ITEMS = {}


def bar(d, color, w=12, inner=6):
    """太い棒（外線＋色の芯）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def mini_face(x, y, r=2.5):
    return (dot(x - 7, y, r) + dot(x + 7, y, r) + cheeks(x - 12, x + 12, y + 6, 4, 2.5)
            + s('path', d=f'M{x-3} {y+5} Q{x} {y+8} {x+3} {y+5}', stroke_width=2))


# 1. mopping
ITEMS['mopping'] = (
    z('path', '#7cc4b0', d='M36 180 Q38 128 66 126 Q94 128 96 180Z')
    + bar('M110 36 L124 166', '#d9a66b', 10, 4)
    + z('path', '#f4f4f0', d='M104 162 L144 162 L148 180 L100 180Z')
    + s('path', d='M110 166 L108 178 M118 166 L117 178 M126 166 L126 178 M134 166 L135 178 M141 166 L143 178', stroke_width=2)
    + bar('M84 140 L118 118', '#7cc4b0') + bar('M88 154 L121 140', '#7cc4b0')
    + z('circle', '#ffd9b8', cx=118, cy=118, r=7) + z('circle', '#ffd9b8', cx=121, cy=141, r=7)
    + face(66, 76, '#ffd9b8', '#5a4033', 'smile')
    + z('path', '#8fc7e8', d='M148 138 L178 138 L174 180 L152 180Z')
    + s('ellipse', '#ffffff', cx=163, cy=138, rx=15, ry=4, stroke_width=2.5)
    + s('path', d='M150 140 Q163 112 176 140', stroke_width=2.5)
    + s('path', d='M150 32 L150 44 M144 38 L156 38 M170 58 L170 66 M166 62 L174 62', stroke_width=2.5)
    + s('path', d='M24 182 L180 182', stroke_width=2)
)

# 2. window-cleaning
ITEMS['window-cleaning'] = (
    z('rect', '#f4f4f0', x=88, y=26, width=88, height=118, rx=4)
    + s('rect', '#8fc7e8', x=98, y=36, width=68, height=98, rx=2)
    + s('path', d='M132 36 L132 134 M98 85 L166 85')
    + s('path', d='M106 50 L120 42 M106 62 L126 48 M140 98 L156 90', stroke='#ffffff', stroke_width=4)
    + s('path', d='M154 44 L154 58 M147 51 L161 51', stroke='#ffffff', stroke_width=3)
    + z('rect', '#d9a66b', x=82, y=142, width=100, height=10, rx=3)
    + z('path', '#e8735a', d='M36 102 L36 84 Q36 78 44 78 L74 78 L80 88 L62 92 L62 102Z')
    + s('path', d='M50 102 L44 120', stroke_width=5)
    + z('rect', '#ffffff', x=40, y=100, width=26, height=16, rx=3)
    + z('rect', '#8fc7e8', x=30, y=114, width=46, height=66, rx=10)
    + s('rect', '#ffffff', x=38, y=132, width=30, height=28, rx=4, stroke_width=2.5)
    + dot(46, 142, 2.5) + dot(60, 142, 2.5) + cheeks(42, 64, 149, 3.5, 2.2)
    + s('path', d='M50 148 Q53 151 56 148', stroke_width=2)
    + dot(88, 82, 3, '#8fc7e8') + dot(96, 74, 3, '#8fc7e8') + dot(96, 90, 3, '#8fc7e8') + dot(104, 82, 3, '#8fc7e8')
    + s('circle', '#ffffff', cx=88, cy=82, r=3, stroke_width=1.5) + s('circle', '#ffffff', cx=96, cy=74, r=3, stroke_width=1.5)
    + s('circle', '#ffffff', cx=96, cy=90, r=3, stroke_width=1.5) + s('circle', '#ffffff', cx=104, cy=82, r=3, stroke_width=1.5)
)

# 3. taking-out-trash
ITEMS['taking-out-trash'] = (
    z('rect', '#9a6a3f', x=26, y=26, width=84, height=154, rx=3)
    + s('rect', '#8b6b4f', x=38, y=40, width=60, height=50, rx=3, stroke_width=2.5)
    + s('rect', '#8b6b4f', x=38, y=104, width=60, height=62, rx=3, stroke_width=2.5)
    + z('circle', '#ffc94d', cx=96, cy=104, r=6)
    + z('path', '#c9d3db', d='M110 180 Q86 180 88 152 Q92 122 122 112 L136 112 Q166 122 170 152 Q172 180 148 180Z')
    + z('path', '#c9d3db', d='M128 114 Q112 96 118 88 Q126 86 130 106Z')
    + z('path', '#c9d3db', d='M130 114 Q146 96 140 88 Q132 86 128 106Z')
    + s('ellipse', '#c9d3db', cx=129, cy=113, rx=9, ry=5)
    + s('path', d='M106 140 Q112 152 108 166 M150 132 Q156 146 154 160', stroke_width=2)
    + s('path', d='M16 182 L184 182', stroke_width=2)
)

# 4. grocery-bag
ITEMS['grocery-bag'] = (
    z('path', '#9ccf7a', d='M62 96 Q52 50 66 26 Q74 50 78 96Z')
    + z('path', '#7cc4a0', d='M70 96 Q74 46 90 30 Q88 60 84 96Z')
    + z('rect', '#f4f4f0', x=68, y=70, width=14, height=30, rx=3)
    + z('rect', '#f5b971', x=104, y=36, width=26, height=64, rx=13, transform='rotate(14 117 68)')
    + s('path', d='M110 52 L124 48 M108 64 L122 60 M108 76 L122 72', stroke_width=2.5, transform='rotate(14 117 68)')
    + z('path', '#e8735a', d='M132 98 L146 56 L156 98Z')
    + z('path', '#9ccf7a', d='M146 58 Q138 42 144 36 Q150 46 148 56 Q156 40 164 44 Q156 52 148 58Z')
    + z('path', '#d9a66b', d='M50 92 L150 92 L158 180 L42 180Z')
    + s('path', '#f6e0c4', d='M50 92 L150 92 L148 108 L52 108Z', stroke_width=2.5)
    + dot(88, 136) + dot(112, 136) + cheeks(78, 122, 146, 6, 3.5)
    + s('path', d='M94 146 Q100 152 106 146', stroke_width=2.5)
    + s('path', d='M30 182 L170 182', stroke_width=2)
)

# 5. door
ITEMS['door'] = (
    z('rect', '#f6e0c4', x=44, y=22, width=112, height=156, rx=4)
    + z('rect', '#7cc4b0', x=56, y=34, width=88, height=144, rx=3)
    + s('path', '#8fc7e8', d='M74 76 L74 64 Q74 46 100 46 Q126 46 126 64 L126 76Z', stroke_width=2.5)
    + s('path', d='M100 46 L100 76', stroke_width=2)
    + s('rect', x=70, y=90, width=60, height=32, rx=3, stroke_width=2.5)
    + s('rect', x=70, y=132, width=60, height=34, rx=3, stroke_width=2.5)
    + z('circle', '#ffc94d', cx=132, cy=118, r=6)
    + z('path', '#ffe27a', d='M162 60 L176 60 L174 82 L164 82Z')
    + s('path', d='M169 48 L169 60', stroke_width=2.5)
    + z('rect', '#e8735a', x=40, y=172, width=120, height=10, rx=4)
)

# 6. intercom
ITEMS['intercom'] = (
    z('rect', '#f4f4f0', x=62, y=28, width=76, height=148, rx=16)
    + s('circle', '#5b6b7a', cx=100, cy=54, r=12)
    + s('circle', '#8fc7e8', cx=100, cy=54, r=5, stroke='none')
    + s('path', d='M80 80 L120 80 M80 90 L120 90 M80 100 L120 100', stroke_width=2.5)
    + z('circle', '#8fc7e8', cx=100, cy=140, r=20)
    + dot(93, 138, 2.5) + dot(107, 138, 2.5) + cheeks(88, 112, 145, 3.5, 2.2)
    + s('path', d='M97 145 Q100 148 103 145', stroke_width=2)
    + s('path', d='M148 70 Q158 84 148 98 M158 60 Q174 84 158 108', stroke_width=3)
    + s('path', d='M52 70 Q42 84 52 98 M42 60 Q26 84 42 108', stroke_width=3)
)

# 7. mailbox
ITEMS['mailbox'] = (
    z('rect', '#8b6b4f', x=88, y=114, width=20, height=66, rx=2)
    + z('path', '#8fc7e8', d='M36 118 L36 76 Q36 52 60 52 L134 52 Q158 52 158 76 L158 118Z')
    + s('rect', '#5b6b7a', x=66, y=64, width=62, height=8, rx=4, stroke_width=2.5)
    + z('rect', '#ffffff', x=78, y=34, width=40, height=34, rx=2)
    + s('path', d='M78 34 L98 52 L118 34', stroke_width=2.5)
    + dot(82, 92) + dot(112, 92) + cheeks(74, 120, 101, 6, 3.5)
    + s('path', d='M92 100 Q97 105 102 100', stroke_width=2.5)
    + s('rect', '#b9a99c', x=158, y=64, width=6, height=46, rx=2, stroke_width=2.5)
    + z('rect', '#e04b5a', x=158, y=56, width=20, height=14, rx=2)
    + s('path', d='M40 182 L160 182', stroke_width=2)
)

# 8. umbrella-stand
def umb(x, lean, color):
    tx, ty = x + lean, 54
    hx, hy = x + lean * 1.3, 44
    return (z('path', color, d=f'M{x-14} 114 Q{x-12} 78 {tx} {ty} Q{x+12} 78 {x+14} 114Z')
            + s('path', d=f'M{x} 112 Q{x+lean*0.4} 80 {tx} {ty}', stroke_width=2)
            + s('path', d=f'M{tx} {ty} L{hx} {hy}', stroke_width=4)
            + bar(f'M{hx} {hy} L{hx} {hy-6} Q{hx} {hy-16} {hx+9} {hy-16} Q{hx+18} {hy-16} {hx+18} {hy-8}', '#9a6a3f', 10, 4))


ITEMS['umbrella-stand'] = (
    umb(78, -10, '#e8735a') + umb(118, 8, '#9ccf7a') + umb(98, -2, '#f5d58a')
    + z('rect', '#8fb3e0', x=60, y=104, width=80, height=74, rx=6)
    + s('path', d='M60 120 L140 120 M60 164 L140 164', stroke_width=2.5)
    + dot(88, 140) + dot(112, 140) + cheeks(80, 120, 149, 6, 3.5)
    + s('path', d='M94 148 Q100 153 106 148', stroke_width=2.5)
    + s('path', d='M40 182 L160 182', stroke_width=2)
)

# 9. slippers
def slipper(x):
    return (z('ellipse', '#f6e0c4', cx=x, cy=110, rx=27, ry=66)
            + z('path', '#f6a6b8', d=f'M{x-27} 96 Q{x-28} 46 {x} 44 Q{x+28} 46 {x+27} 96 Q{x} 108 {x-27} 96Z')
            + mini_face(x, 74))


ITEMS['slippers'] = slipper(70) + slipper(128)

# 10. shoes-entrance
def sneaker(x, y, c):
    return (z('path', c, d=f'M{x} {y} L{x} {y-26} Q{x} {y-32} {x+8} {y-32} L{x+20} {y-30} Q{x+26} {y-20} {x+38} {y-16} Q{x+52} {y-12} {x+52} {y-2} L{x+52} {y} Z')
            + s('rect', '#ffffff', x=x - 2, y=y - 4, width=58, height=8, rx=4, stroke_width=2.5)
            + s('path', d=f'M{x+16} {y-24} L{x+22} {y-18} M{x+22} {y-26} L{x+28} {y-20}', stroke_width=2))


ITEMS['shoes-entrance'] = (
    z('rect', '#f6e0c4', x=22, y=36, width=156, height=40)
    + z('rect', '#d9a66b', x=22, y=72, width=156, height=22, rx=2)
    + s('path', d='M60 44 L60 72 M110 44 L110 72 M150 44 L150 72', stroke_width=2)
    + s('rect', '#c9d3db', x=22, y=98, width=156, height=82, stroke_width=2.5)
    + s('path', d='M74 98 L74 180 M126 98 L126 180 M22 138 L178 138', stroke='#ffffff', stroke_width=2)
    + sneaker(34, 146, '#e8735a') + sneaker(44, 166, '#e8735a')
    + sneaker(104, 146, '#8fc7e8') + sneaker(114, 166, '#8fc7e8')
)

# 11. picture-frame
ITEMS['picture-frame'] = (
    s('path', d='M62 62 L100 30 L138 62', stroke_width=2.5) + dot(100, 30, 4.5)
    + z('rect', '#d9a66b', x=34, y=58, width=132, height=112, rx=4)
    + s('rect', '#8fc7e8', x=48, y=72, width=104, height=84, rx=2)
    + s('circle', '#ffe27a', cx=128, cy=92, r=9, stroke_width=2.5)
    + s('path', '#9ccf7a', d='M48 156 L48 134 L76 104 L96 126 L118 100 L152 134 L152 156Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M68 113 L76 104 L84 113 Q76 116 68 113Z', stroke_width=2)
    + s('path', '#ffffff', d='M110 109 L118 100 L126 109 Q118 112 110 109Z', stroke_width=2)
)

# 12. wall-clock
ticks = ''
for i in range(12):
    a = math.radians(i * 30)
    r1, r2 = (44, 54) if i % 3 == 0 else (48, 54)
    ticks += s('path', d=f'M{100+r1*math.sin(a):.1f} {104-r1*math.cos(a):.1f} L{100+r2*math.sin(a):.1f} {104-r2*math.cos(a):.1f}',
               stroke_width=3 if i % 3 == 0 else 2)
ITEMS['wall-clock'] = (
    s('path', d='M100 32 L100 22', stroke_width=3) + dot(100, 20, 4)
    + z('circle', '#f5b971', cx=100, cy=104, r=72)
    + s('circle', '#ffffff', cx=100, cy=104, r=60)
    + ticks
    + s('path', d='M100 104 L80 88', stroke_width=5)
    + s('path', d='M100 104 L130 76', stroke_width=3.5)
    + s('circle', '#e8735a', cx=100, cy=104, r=5, stroke_width=2.5)
    + dot(86, 122, 3) + dot(114, 122, 3) + cheeks(78, 122, 130, 5, 3)
    + s('path', d='M96 130 Q100 134 104 130', stroke_width=2.2)
)

# 13. candle
ITEMS['candle'] = (
    z('ellipse', '#f5d58a', cx=100, cy=168, rx=56, ry=12)
    + z('rect', '#f6a6b8', x=76, y=82, width=48, height=86, rx=5)
    + s('path', '#ffffff', d='M76 90 Q76 82 82 82 L118 82 Q124 82 124 90 L124 98 Q118 104 114 96 Q108 112 102 96 Q96 104 90 96 Q84 108 76 98Z', stroke_width=2.5)
    + s('path', d='M100 82 L100 70', stroke_width=2.5)
    + z('path', '#ffc94d', d='M100 72 Q84 56 100 30 Q116 56 100 72Z')
    + s('path', '#e8735a', d='M100 68 Q93 60 100 48 Q107 60 100 68Z', stroke='none')
    + s('path', d='M66 46 L74 52 M134 46 L126 52 M100 18 L100 14 M70 70 L62 72 M130 70 L138 72', stroke_width=2.5)
    + dot(91, 128) + dot(109, 128) + cheeks(84, 116, 136, 5, 3)
    + s('path', d='M96 136 Q100 140 104 136', stroke_width=2.5)
)

# 14. toolbox
ITEMS['toolbox'] = (
    bar('M72 92 L72 68 Q72 60 80 60 L120 60 Q128 60 128 68 L128 92', '#5b6b7a', 12, 6)
    + z('rect', '#e8735a', x=32, y=100, width=136, height=76, rx=6)
    + z('rect', '#e8735a', x=28, y=86, width=144, height=24, rx=5)
    + z('rect', '#ffc94d', x=90, y=102, width=20, height=16, rx=3)
    + s('path', d='M40 128 L160 128', stroke_width=2)
    + dot(70, 146) + dot(130, 146) + cheeks(58, 142, 154, 6, 3.5)
    + s('path', d='M94 152 Q100 158 106 152', stroke_width=2.5)
    + s('path', d='M22 182 L178 182', stroke_width=2)
)

# 15. hammer
ROT = 'rotate(35 100 120)'
ITEMS['hammer'] = (
    z('rect', '#f5d58a', x=112, y=160, width=66, height=20, rx=3)
    + s('path', d='M134 160 L134 136 M156 160 L156 140', stroke_width=4)
    + s('rect', '#c9d3db', x=126, y=131, width=16, height=6, rx=2, stroke_width=2.5)
    + s('rect', '#c9d3db', x=148, y=135, width=16, height=6, rx=2, stroke_width=2.5)
    + z('rect', '#d9a66b', x=91, y=72, width=18, height=104, rx=7, transform=ROT)
    + s('rect', '#e8735a', x=91, y=138, width=18, height=38, rx=7, transform=ROT, stroke_width=2.5)
    + z('path', '#c9d3db', d='M74 54 L126 54 Q140 54 146 46 L148 64 Q140 82 126 80 L74 80Z', transform=ROT)
    + z('rect', '#c9d3db', x=60, y=50, width=18, height=34, rx=3, transform=ROT)
    + s('path', d='M24 182 L180 182', stroke_width=2)
)

# 16. ladder
def lx(y, top, bot):
    return top + (bot - top) * (y - 40) / 138


rungs = ''
for y in (70, 100, 130, 160):
    rungs += bar(f'M{lx(y,74,48):.1f} {y} L{lx(y,126,152):.1f} {y}', '#f5d58a', 11, 5)
ITEMS['ladder'] = (
    bar('M126 42 L170 178', '#b9a99c', 12, 6)
    + rungs
    + bar('M74 40 L48 178', '#f5d58a', 14, 8) + bar('M126 40 L152 178', '#f5d58a', 14, 8)
    + z('rect', '#e8735a', x=64, y=28, width=72, height=18, rx=5)
    + s('path', d='M30 182 L178 182', stroke_width=2)
)

# 17. flashlight
ITEMS['flashlight'] = (
    s('path', '#ffe27a', d='M128 74 L180 50 L180 156 L128 132Z', stroke='none')
    + s('path', d='M140 68 L178 52 M140 138 L178 154', stroke_width=2.5)
    + z('rect', '#8fb3e0', x=24, y=86, width=82, height=36, rx=10)
    + z('path', '#c9d3db', d='M102 82 L126 68 L126 140 L102 126Z')
    + s('ellipse', '#ffffff', cx=127, cy=104, rx=6, ry=36, stroke_width=2.5)
    + z('rect', '#e8735a', x=56, y=78, width=20, height=10, rx=3)
    + s('path', d='M38 92 L38 116 M46 92 L46 116', stroke_width=2)
    + dot(70, 102, 3) + dot(88, 102, 3) + cheeks(64, 94, 110, 4, 2.5)
    + s('path', d='M76 110 Q79 113 82 110', stroke_width=2)
)

# 18. emergency-bag
ITEMS['emergency-bag'] = (
    bar('M80 54 Q80 34 100 34 Q120 34 120 54', '#5b6b7a', 11, 5)
    + z('rect', '#f5b971', x=40, y=50, width=104, height=128, rx=28)
    + s('path', d='M40 84 L144 84', stroke_width=2.5)
    + z('rect', '#e8735a', x=56, y=112, width=72, height=56, rx=12)
    + s('rect', '#ffe27a', x=56, y=124, width=72, height=10, stroke_width=2.5)
    + s('path', d='M64 112 L120 112', stroke_width=2)
    + dot(80, 98, 3) + dot(104, 98, 3) + cheeks(72, 112, 105, 4.5, 2.5)
    + s('path', d='M89 104 Q92 107 95 104', stroke_width=2)
    + z('rect', '#8fc7e8', x=146, y=120, width=28, height=58, rx=7)
    + z('rect', '#ffffff', x=152, y=110, width=16, height=12, rx=2)
    + s('path', d='M146 140 L174 140 M146 160 L174 160', stroke_width=2)
    + s('path', d='M24 182 L180 182', stroke_width=2)
)

# 19. moving-boxes
def box(x, y, w, h):
    cx = x + w / 2
    return (z('rect', '#d9a66b', x=x, y=y, width=w, height=h, rx=2)
            + s('rect', '#f5d58a', x=cx - 7, y=y, width=14, height=22, stroke_width=2.5)
            + s('path', d=f'M{x} {y+8} L{cx-7} {y+8} M{cx+7} {y+8} L{x+w} {y+8}', stroke_width=2))


ITEMS['moving-boxes'] = (
    box(102, 104, 72, 74)
    + box(28, 112, 76, 66)
    + box(60, 46, 80, 64)
    + dot(88, 84, 3) + dot(112, 84, 3) + cheeks(80, 120, 92, 5, 3)
    + s('path', d='M96 92 Q100 96 104 92', stroke_width=2.2)
    + s('path', d='M54 160 L54 140 M48 146 L54 140 L60 146', stroke_width=2.5)
    + s('path', d='M74 160 L74 140 M68 146 L74 140 L80 146', stroke_width=2.5)
    + s('path', d='M18 182 L182 182', stroke_width=2)
)

# 20. apartment
wins = ''
for row in range(4):
    y = 44 + row * 28
    for col in range(3):
        x = 60 + col * 28
        wins += s('rect', '#8fc7e8', x=x, y=y, width=20, height=16, rx=2, stroke_width=2.5)
    wins += s('path', d=f'M56 {y+22} L144 {y+22}', stroke_width=2)
ITEMS['apartment'] = (
    s('path', d='M166 180 L166 150', stroke_width=4)
    + z('circle', '#9ccf7a', cx=166, cy=138, r=16)
    + s('path', d='M34 180 L34 158', stroke_width=4)
    + z('circle', '#7cc4a0', cx=34, cy=148, r=13)
    + z('rect', '#f6e0c4', x=50, y=30, width=100, height=150, rx=2)
    + z('rect', '#e8735a', x=44, y=24, width=112, height=12, rx=3)
    + wins
    + z('rect', '#8b6b4f', x=88, y=152, width=24, height=28, rx=2)
    + s('rect', '#8fc7e8', x=62, y=156, width=16, height=14, rx=2, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=122, y=156, width=16, height=14, rx=2, stroke_width=2.5)
    + s('path', d='M18 182 L182 182', stroke_width=2)
)
