import math
from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

def ck(x, y, rx=5, ry=3):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{CH}" stroke="none"/>'

def smile(cx, cy, w=4):
    return s('path', d=f'M{cx-w} {cy} Q{cx} {cy+4} {cx+w} {cy}', stroke_width=2.5)

def tube(d, color, w=10):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)

def mirror(d):
    import re
    toks = re.findall(r'[A-Za-z]|-?\d+(?:\.\d+)?', d)
    out, nums = [], []
    for t in toks:
        if t.isalpha():
            out.append(t)
        else:
            nums.append(t); out.append(None)
    res, i = [], 0
    for t in out:
        if t is not None:
            res.append(t); i = 0
        else:
            v = float(nums.pop(0))
            res.append(f'{200 - v:g}' if i % 2 == 0 else f'{v:g}'); i += 1
    return ' '.join(res)

# 1. seahorse
ITEMS['seahorse'] = (
    tube('M98 142 Q114 172 92 178 Q72 178 78 162 Q84 152 94 160', '#f5b971', 10)
    + z('path', '#f6a6b8', d='M84 40 L80 24 L92 32 L96 20 L104 34Z')
    + z('path', '#f5b971', d='M84 74 Q72 100 84 126 Q92 148 108 144 Q128 136 120 108 Q114 88 108 74Z')
    + z('path', '#f6a6b8', d='M80 96 Q56 98 60 118 Q72 116 80 112Z')
    + s('path', d='M102 98 Q112 102 119 98 M102 112 Q113 116 122 112 M102 126 Q111 130 118 126', stroke_width=2)
    + z('rect', '#f5b971', x=112, y=56, width=36, height=13, rx=6.5)
    + z('circle', '#f5b971', cx=100, cy=60, r=26)
    + dot(106, 55) + ck(106, 68)
    + s('circle', '#ffffff', cx=158, cy=44, r=6, stroke_width=2) + s('circle', '#ffffff', cx=168, cy=28, r=4, stroke_width=2)
)

# 2. sparrow
ITEMS['sparrow'] = (
    s('path', d='M100 156 L98 180 M90 182 L98 180 L106 182 M120 156 L122 180 M114 182 L122 180 L130 182', stroke_width=2.5)
    + z('path', '#9a6a3f', d='M138 126 L176 148 L168 160 L132 146Z')
    + z('ellipse', '#d9a66b', cx=110, cy=124, rx=46, ry=38)
    + s('ellipse', '#f6e0c4', cx=94, cy=138, rx=26, ry=20, stroke='none')
    + z('path', '#9a6a3f', d='M104 110 Q140 98 152 130 Q132 150 106 140 Q96 126 104 110Z')
    + s('path', d='M116 124 Q130 120 140 130 M114 134 Q126 132 134 138', stroke_width=2)
    + z('path', '#5b6b7a', d='M54 84 L34 93 L54 102Z')
    + z('circle', '#d9a66b', cx=78, cy=88, r=30)
    + s('path', '#9a6a3f', d='M48 86 Q50 58 78 58 Q104 58 108 84 Q92 72 76 74 Q60 76 48 86Z')
    + s('ellipse', '#f4f4f0', cx=80, cy=102, rx=17, ry=10, stroke='none')
    + dot(68, 88) + ck(80, 102) + s('path', d='M30 182 L170 182', stroke_width=2)
)

# 3. crow
ITEMS['crow'] = (
    s('path', d='M88 154 L86 180 M78 182 L86 180 L94 182 M106 156 L108 180 M100 182 L108 180 L116 182', stroke_width=3)
    + z('path', '#5b6b7a', d='M60 120 L26 140 L32 152 L66 140Z')
    + z('ellipse', '#5b6b7a', cx=96, cy=124, rx=44, ry=36)
    + z('path', '#5b6b7a', d='M64 112 Q92 100 118 118 Q102 148 66 136Z')
    + s('path', d='M76 124 Q92 120 104 128', stroke_width=2)
    + z('path', '#2b2220', d='M140 78 L178 90 L142 102Z')
    + z('circle', '#5b6b7a', cx=124, cy=86, r=28)
    + s('circle', '#ffffff', cx=132, cy=80, r=7, stroke_width=2) + dot(134, 80, 3.5)
    + ck(128, 98) + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 4. pigeon
ITEMS['pigeon'] = (
    s('path', d='M98 158 L96 178', stroke_width=6) + s('path', d='M98 158 L96 178', stroke='#f07a8a', stroke_width=3)
    + s('path', d='M118 158 L120 178', stroke_width=6) + s('path', d='M118 158 L120 178', stroke='#f07a8a', stroke_width=3)
    + s('path', d='M88 180 L104 180 M112 180 L128 180', stroke_width=3)
    + z('path', '#b9a99c', d='M146 118 L178 132 L172 146 L140 140Z')
    + z('ellipse', '#c9d3db', cx=108, cy=126, rx=48, ry=36)
    + s('path', '#7cc4b0', d='M64 112 Q70 100 84 102 Q92 114 86 126 Q72 130 64 112Z', stroke='none')
    + z('path', '#b9a99c', d='M104 108 Q144 100 156 128 Q138 148 106 140 Q96 124 104 108Z')
    + s('path', '#5b6b7a', d='M120 120 L140 118 L142 124 L122 126Z', stroke_width=1.5)
    + s('path', '#5b6b7a', d='M120 132 L142 130 L144 136 L122 138Z', stroke_width=1.5)
    + z('path', '#b9a99c', d='M58 80 L42 88 L58 94Z')
    + z('circle', '#c9d3db', cx=76, cy=86, r=24)
    + s('ellipse', '#ffffff', cx=58, cy=82, rx=4, ry=3, stroke='none')
    + s('circle', '#f5b971', cx=72, cy=82, r=5.5, stroke_width=2) + dot(72, 82, 2.5) + ck(80, 96)
)

# 5. eagle
EW = 'M80 104 Q60 62 30 64 Q20 70 30 78 Q18 84 28 92 Q18 100 32 104 Q24 114 40 116 Q36 126 52 124 Q56 134 80 132Z'
ITEMS['eagle'] = (
    z('path', '#9a6a3f', d=EW) + z('path', '#9a6a3f', d=mirror(EW))
    + s('path', d='M66 96 Q50 90 40 94 M70 112 Q56 108 48 114 M134 96 Q150 90 160 94 M130 112 Q144 108 152 114', stroke_width=2)
    + z('path', '#f4f4f0', d='M88 156 L78 180 L122 180 L112 156Z')
    + s('path', d='M92 162 L90 178 M100 162 L100 178 M108 162 L110 178', stroke_width=2)
    + z('ellipse', '#9a6a3f', cx=100, cy=128, rx=30, ry=36)
    + z('ellipse', '#ffc94d', cx=88, cy=162, rx=8, ry=6) + z('ellipse', '#ffc94d', cx=112, cy=162, rx=8, ry=6)
    + z('circle', '#f4f4f0', cx=100, cy=72, r=28)
    + dot(88, 70) + dot(112, 70)
    + s('path', d='M80 60 L92 64 M120 60 L108 64', stroke_width=3)
    + cheeks(80, 120, 84, 5, 3)
    + z('path', '#ffc94d', d='M90 78 L110 78 Q110 92 102 98 Q100 92 96 90 Q90 86 90 78Z')
)

# 6. flamingo
NECK = 'M94 96 Q66 86 78 64 Q88 48 72 42'
ITEMS['flamingo'] = (
    s('path', d='M114 116 L114 178', stroke_width=7) + s('path', d='M114 116 L114 178', stroke='#f07a8a', stroke_width=3)
    + s('path', d='M122 116 L136 144 L116 150', stroke_width=7) + s('path', d='M122 116 L136 144 L116 150', stroke='#f07a8a', stroke_width=3)
    + tube(NECK, '#f6a6b8', 9)
    + z('path', '#f6a6b8', d='M84 96 Q90 72 122 74 Q150 76 172 86 Q160 92 160 100 Q148 122 116 122 Q88 122 84 96Z')
    + s('path', '#f07a8a', d='M106 92 Q130 80 154 92 Q134 108 106 102Z', stroke_width=2.5)
    + z('path', '#f4f4f0', d='M60 36 L44 42 Q40 52 46 60 Q50 50 62 46Z')
    + s('path', '#5b6b7a', d='M44 42 Q40 52 46 60 Q47 52 50 46Z', stroke_width=2)
    + z('circle', '#f6a6b8', cx=68, cy=40, r=13)
    + dot(68, 37, 3) + ck(74, 46, 4, 2.5)
    + z('ellipse', '#8fc7e8', cx=116, cy=178, rx=34, ry=5)
)

# 7. parrot
ITEMS['parrot'] = (
    z('path', '#8fb3e0', d='M108 134 L126 180 L110 180 L94 138Z')
    + z('path', '#e8735a', d='M100 134 L104 180 L92 180 L90 138Z')
    + z('rect', '#9a6a3f', x=28, y=138, width=148, height=12, rx=6)
    + z('ellipse', '#e04b5a', cx=104, cy=110, rx=30, ry=34)
    + z('path', '#ffc94d', d='M110 92 Q142 98 136 132 Q122 146 108 136Z')
    + s('path', '#8fb3e0', d='M118 122 Q136 124 132 136 Q120 146 110 138Z', stroke_width=2.5)
    + z('ellipse', '#b9a99c', cx=96, cy=142, rx=6, ry=5) + z('ellipse', '#b9a99c', cx=114, cy=142, rx=6, ry=5)
    + z('circle', '#e04b5a', cx=94, cy=66, r=28)
    + s('ellipse', '#f4f4f0', cx=86, cy=68, rx=14, ry=12, stroke='none')
    + dot(86, 66) + ck(96, 82)
    + z('path', '#f4f4f0', d='M74 54 Q48 52 50 78 Q54 72 62 74 L76 74Z')
    + s('path', '#5b6b7a', d='M62 74 Q60 84 70 84 L76 74Z', stroke_width=2.5)
)

# 8. peacock (open tail)
def fan():
    cx, cy, r, R = 100, 132, 76, 86
    n = 8
    pts = [(cx + r * math.cos(math.pi - math.pi * i / n), cy - r * math.sin(math.pi * i / n)) for i in range(n + 1)]
    d = f'M{cx} {cy} L{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(n):
        a = math.pi - math.pi * (i + .5) / n
        d += f' Q{cx + R * math.cos(a):.1f} {cy - R * math.sin(a):.1f} {pts[i+1][0]:.1f} {pts[i+1][1]:.1f}'
    o = z('path', '#7cc4b0', d=d + 'Z')
    spots = [(62, math.radians(a)) for a in range(16, 170, 25)] + [(36, math.radians(a)) for a in (32, 72, 108, 148)]
    for rr, a in spots:
        x, y = cx + rr * math.cos(a), cy - rr * math.sin(a)
        o += s('path', d=f'M{cx} {cy} L{x:.1f} {y:.1f}', stroke_width=1.5)
    for rr, a in spots:
        x, y = cx + rr * math.cos(a), cy - rr * math.sin(a)
        o += s('ellipse', '#9ccf7a', cx=f'{x:.1f}', cy=f'{y:.1f}', rx=9, ry=10, stroke_width=2)
        o += s('circle', '#8fb3e0', cx=f'{x:.1f}', cy=f'{y:.1f}', r=6, stroke='none') + dot(round(x, 1), round(y, 1), 3, '#5b6b7a')
    return o
ITEMS['peacock'] = (
    fan()
    + s('path', d='M94 164 L92 180 M86 180 L98 180 M106 164 L108 180 M102 180 L114 180', stroke_width=3)
    + z('path', '#8fb3e0', d='M100 92 Q84 120 82 146 Q84 168 100 168 Q116 168 118 146 Q116 120 100 92Z')
    + s('path', d='M92 52 L100 66 L108 52 M100 48 L100 66', stroke_width=2)
    + dot(92, 52, 3.5, '#8fb3e0') + dot(100, 48, 3.5, '#8fb3e0') + dot(108, 52, 3.5, '#8fb3e0')
    + z('circle', '#8fb3e0', cx=100, cy=82, r=17)
    + dot(94, 80, 3) + dot(106, 80, 3) + ck(88, 89, 4, 2.5) + ck(112, 89, 4, 2.5)
    + z('path', '#f5d58a', d='M96 86 L104 86 L100 93Z')
)

# 9. swan
ITEMS['swan'] = (
    tube('M94 140 Q64 128 70 98 Q74 72 86 60', '#f4f4f0', 11)
    + z('path', '#f4f4f0', d='M72 140 Q76 112 112 112 Q140 112 158 92 Q172 112 164 134 Q152 160 112 160 Q76 160 72 140Z')
    + s('path', '#ffffff', d='M100 130 Q124 112 154 114 Q142 140 110 144Z', stroke_width=2.5)
    + z('path', '#f5b971', d='M76 50 L52 58 L76 64Z')
    + s('path', '#5b6b7a', d='M76 50 L68 53 L68 61 L76 64Z', stroke='none')
    + z('circle', '#f4f4f0', cx=86, cy=56, r=14)
    + dot(84, 53, 3) + ck(90, 62, 4, 2.5)
    + z('path', '#8fc7e8', d='M26 158 Q38 150 50 158 Q62 166 74 158 Q86 150 98 158 Q110 166 122 158 Q134 150 146 158 Q158 166 174 158 L174 178 L26 178Z')
)

# 10. hummingbird at a flower
PET = ''.join(z('circle', '#f6a6b8', cx=round(58 + 15 * math.cos(math.radians(a)), 1), cy=round(124 + 15 * math.sin(math.radians(a)), 1), r=12) for a in range(-90, 270, 72))
ITEMS['hummingbird'] = (
    s('path', d='M58 136 Q62 160 58 182', stroke_width=3)
    + z('path', '#9ccf7a', d='M60 164 Q80 148 92 156 Q80 172 60 164Z')
    + PET + z('circle', '#ffe27a', cx=58, cy=124, r=9)
    + z('path', '#ffffff', d='M136 88 Q146 52 176 46 Q170 78 146 94Z')
    + z('path', '#7cc4b0', d='M146 106 L176 130 L164 138 L138 114Z')
    + z('ellipse', '#7cc4b0', cx=128, cy=100, rx=28, ry=18, transform='rotate(28 128 100)')
    + s('ellipse', '#f4f4f0', cx=122, cy=108, rx=12, ry=8, transform='rotate(28 122 108)', stroke='none')
    + z('path', '#c9d3db', d='M124 90 Q114 50 140 32 Q148 62 136 92Z')
    + s('path', d='M110 40 L116 50 M154 30 L152 40 M182 60 L172 62', stroke_width=2)
    + s('path', d='M94 84 L66 114', stroke_width=3)
    + z('circle', '#7cc4b0', cx=106, cy=78, r=16)
    + s('path', '#e04b5a', d='M98 92 Q108 98 118 88 Q116 84 110 86 Q102 90 98 92Z', stroke='none')
    + dot(101, 74, 3) + ck(108, 84, 4, 2.5)
)

# 11. woodpecker on a tree
ITEMS['woodpecker'] = (
    z('rect', '#9a6a3f', x=36, y=24, width=48, height=158, rx=6)
    + s('path', d='M50 40 Q46 60 52 80 M70 100 Q74 120 68 140 M48 150 Q52 164 48 176', stroke_width=2)
    + s('ellipse', '#3b2f2a', cx=60, cy=114, rx=8, ry=11, stroke='none')
    + z('path', '#5b6b7a', d='M114 138 L104 176 L118 176 L126 138Z')
    + s('path', d='M104 142 L90 146 M104 150 L90 156', stroke_width=3)
    + z('ellipse', '#5b6b7a', cx=118, cy=116, rx=24, ry=34)
    + s('ellipse', '#f4f4f0', cx=108, cy=122, rx=11, ry=22, stroke='none')
    + dot(128, 108, 3, '#f4f4f0') + dot(134, 118, 3, '#f4f4f0') + dot(128, 128, 3, '#f4f4f0')
    + z('path', '#e04b5a', d='M128 58 L146 56 L134 70Z')
    + z('path', '#b9a99c', d='M96 70 L84 76 L96 82Z')
    + z('circle', '#f4f4f0', cx=114, cy=74, r=22)
    + s('path', '#e04b5a', d='M92 72 Q94 52 114 52 Q134 52 136 72 Q124 62 114 62 Q102 62 92 72Z')
    + dot(106, 74, 3) + ck(114, 84, 4, 2.5)
    + z('rect', '#d9a66b', x=92, y=56, width=6, height=4, transform='rotate(-30 95 58)')
    + z('rect', '#d9a66b', x=94, y=94, width=6, height=4, transform='rotate(30 97 96)')
    + s('path', d='M88 62 L92 66 M88 90 L92 86', stroke_width=2)
)

# 12. butterfly
UW = 'M98 98 Q62 38 34 58 Q22 92 60 106 Q84 110 98 106Z'
LW = 'M98 110 Q64 108 52 132 Q54 162 80 154 Q96 142 98 118Z'
ITEMS['butterfly'] = (
    z('path', '#f5b971', d=UW) + z('path', '#f5b971', d=mirror(UW))
    + z('path', '#f6a6b8', d=LW) + z('path', '#f6a6b8', d=mirror(LW))
    + s('circle', '#ffffff', cx=56, cy=76, r=8, stroke_width=2) + s('circle', '#ffffff', cx=144, cy=76, r=8, stroke_width=2)
    + s('circle', '#ffe27a', cx=74, cy=134, r=6, stroke_width=2) + s('circle', '#ffe27a', cx=126, cy=134, r=6, stroke_width=2)
    + z('ellipse', '#8b6b4f', cx=100, cy=122, rx=8, ry=32)
    + s('path', d='M94 66 Q86 46 76 40 M106 66 Q114 46 124 40', stroke_width=2.5)
    + dot(76, 40, 4) + dot(124, 40, 4)
    + z('circle', '#f5d58a', cx=100, cy=80, r=15)
    + dot(94, 79, 2.8) + dot(106, 79, 2.8) + ck(89, 86, 4, 2.5) + ck(111, 86, 4, 2.5) + smile(100, 86, 3)
)

# 13. ladybug
ITEMS['ladybug'] = (
    s('path', d='M56 104 L36 96 M52 128 L30 130 M58 152 L40 166 M144 104 L164 96 M148 128 L170 130 M142 152 L160 166', stroke_width=3)
    + s('path', d='M92 40 Q88 28 78 26 M108 40 Q112 28 122 26', stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=100, cy=62, r=26)
    + z('circle', '#e04b5a', cx=100, cy=120, r=50)
    + s('path', d='M100 72 L100 170', stroke_width=2.5)
    + dot(76, 102, 8) + dot(124, 102, 8) + dot(70, 134, 8) + dot(130, 134, 8) + dot(88, 156, 7) + dot(112, 156, 7)
    + s('ellipse', '#ffffff', cx=78, cy=84, rx=7, ry=3.5, stroke='none', transform='rotate(-30 78 84)')
    + s('circle', '#ffffff', cx=90, cy=52, r=5.5, stroke='none') + s('circle', '#ffffff', cx=110, cy=52, r=5.5, stroke='none')
    + dot(91, 53, 2.8) + dot(109, 53, 2.8) + ck(82, 62, 4, 2.5) + ck(118, 62, 4, 2.5)
    + s('path', d='M96 62 Q100 66 104 62', stroke='#ffffff', stroke_width=2)
)

# 14. honey bee
ITEMS['bee'] = (
    s('path', d='M92 150 L88 162 M110 152 L110 164 M128 148 L132 160', stroke_width=3)
    + z('path', '#5b6b7a', d='M152 110 L172 116 L152 124Z')
    + z('ellipse', '#ffe27a', cx=110, cy=116, rx=46, ry=36)
    + s('path', '#5b6b7a', d='M103 81 L117 81 L117 151 L103 151Z', stroke='none')
    + s('path', '#5b6b7a', d='M127 83 L141 90 L141 142 L127 149Z', stroke='none')
    + s('ellipse', cx=110, cy=116, rx=46, ry=36)
    + z('ellipse', '#ffffff', cx=104, cy=70, rx=15, ry=24, transform='rotate(-20 104 70)')
    + z('ellipse', '#ffffff', cx=128, cy=74, rx=13, ry=21, transform='rotate(22 128 74)')
    + s('path', d='M56 84 Q50 66 42 58 M72 82 Q74 64 80 54', stroke_width=2.5) + dot(42, 58, 4) + dot(80, 54, 4)
    + z('circle', '#ffe27a', cx=64, cy=106, r=25)
    + dot(56, 104) + dot(72, 104) + ck(48, 114, 5, 3) + ck(80, 114, 5, 3) + smile(64, 116, 4)
)

# 15. ant carrying a crumb
ITEMS['ant'] = (
    s('path', d='M92 138 L80 162 L74 176 M100 140 L102 160 L98 176 M108 138 L122 160 L128 176', stroke_width=3)
    + s('path', d='M150 154 L160 170', stroke_width=3)
    + s('path', d='M86 124 L72 86 M98 124 L100 86', stroke_width=3)
    + z('ellipse', '#9a6a3f', cx=142, cy=136, rx=28, ry=22)
    + z('ellipse', '#9a6a3f', cx=102, cy=132, rx=17, ry=11)
    + z('path', '#f5d58a', d='M50 72 Q44 50 66 44 Q82 34 100 44 Q116 54 110 72 Q104 90 80 88 Q56 90 50 72Z')
    + dot(70, 58, 3, '#d9a66b') + dot(92, 54, 2.5, '#d9a66b') + dot(84, 72, 3, '#d9a66b') + dot(62, 76, 2.5, '#d9a66b')
    + s('path', d='M54 104 Q42 98 34 106 M60 100 Q52 90 40 92', stroke_width=2.5)
    + z('circle', '#9a6a3f', cx=68, cy=118, r=21)
    + dot(60, 114, 3.5) + dot(76, 114, 3.5) + ck(54, 124, 4, 2.5) + ck(82, 124, 4, 2.5) + smile(68, 126, 3)
    + s('path', d='M124 90 L130 82 M134 98 L144 94', stroke_width=2)
)

# 16. dragonfly
def wing(cx, cy, rx, ry, rot):
    return (z('ellipse', '#ffffff', cx=cx, cy=cy, rx=rx, ry=ry, transform=f'rotate({rot} {cx} {cy})')
            + s('path', d=f'M{cx-rx+6} {cy} L{cx+rx-6} {cy}', transform=f'rotate({rot} {cx} {cy})', stroke_width=1.5, stroke='#8fc7e8'))
ITEMS['dragonfly'] = (
    wing(64, 76, 38, 11, -12) + wing(66, 100, 34, 10, 14)
    + wing(136, 76, 38, 11, 12) + wing(134, 100, 34, 10, -14)
    + z('rect', '#7cc4b0', x=93, y=92, width=14, height=86, rx=7)
    + s('path', d='M93 112 L107 112 M93 128 L107 128 M93 144 L107 144 M93 160 L107 160', stroke_width=2)
    + z('ellipse', '#7cc4b0', cx=100, cy=86, rx=12, ry=14)
    + z('circle', '#7cc4b0', cx=100, cy=58, r=18)
    + z('circle', '#8fc7e8', cx=87, cy=50, r=9) + z('circle', '#8fc7e8', cx=113, cy=50, r=9)
    + dot(88, 51, 3.5) + dot(112, 51, 3.5) + ck(88, 64, 4, 2.5) + ck(112, 64, 4, 2.5) + smile(100, 66, 3)
)

# 17. rhinoceros beetle
ITEMS['rhinoceros-beetle'] = (
    s('path', d='M92 138 L80 166 L70 174 M118 146 L118 172 L108 178 M146 140 L158 166 L168 172', stroke_width=3)
    + z('ellipse', '#8b6b4f', cx=124, cy=118, rx=48, ry=32)
    + s('path', d='M86 112 Q120 92 168 106', stroke_width=2)
    + s('ellipse', '#d9a66b', cx=126, cy=96, rx=18, ry=4, stroke='none', transform='rotate(-6 126 96)')
    + z('path', '#8b6b4f', d='M76 98 Q66 84 56 86 Q62 92 66 104Z')
    + z('ellipse', '#8b6b4f', cx=80, cy=114, rx=22, ry=20)
    + z('path', '#8b6b4f', d='M46 124 Q34 96 40 64 Q42 54 48 54 Q46 64 52 68 Q54 60 60 62 Q50 92 62 120Z')
    + z('ellipse', '#8b6b4f', cx=54, cy=128, rx=16, ry=13)
    + s('ellipse', '#d9a66b', cx=78, cy=104, rx=8, ry=3, stroke='none')
    + dot(50, 126, 3) + ck(56, 134, 4, 2.5)
)

# 18. stag beetle
MAND = 'M86 64 Q62 52 72 28 Q82 20 90 28 Q80 32 80 42 L86 42 Q86 52 94 60Z'
ITEMS['stag-beetle'] = (
    s('path', d='M72 110 L50 98 L44 84 M70 134 L46 138 L36 150 M76 156 L58 170 L56 180 M128 110 L150 98 L156 84 M130 134 L154 138 L164 150 M124 156 L142 170 L144 180', stroke_width=3)
    + s('path', d='M80 70 L68 70 L62 62 M120 70 L132 70 L138 62', stroke_width=2)
    + z('path', '#9a6a3f', d=MAND) + z('path', '#9a6a3f', d=mirror(MAND))
    + z('ellipse', '#8b6b4f', cx=100, cy=136, rx=34, ry=40)
    + s('path', d='M100 104 L100 176', stroke_width=2.5)
    + s('ellipse', '#d9a66b', cx=84, cy=124, rx=4, ry=12, stroke='none')
    + z('ellipse', '#8b6b4f', cx=100, cy=94, rx=30, ry=15)
    + z('ellipse', '#8b6b4f', cx=100, cy=70, rx=24, ry=14)
    + dot(91, 68, 3) + dot(109, 68, 3) + ck(84, 74, 4, 2.5) + ck(116, 74, 4, 2.5) + smile(100, 75, 3)
)

# 19. caterpillar on a leaf
SEG = [(52, 128), (68, 120), (84, 108), (100, 100), (116, 102), (132, 110)]
ITEMS['caterpillar'] = (
    z('path', '#9ccf7a', d='M26 154 Q36 72 118 52 Q160 42 178 46 Q172 112 122 150 Q78 178 26 154Z')
    + s('path', d='M30 152 Q100 112 174 50 M70 130 Q66 108 74 92 M110 98 Q108 78 118 64 M100 108 Q120 116 140 112', stroke_width=2)
    + ''.join(s('path', d=f'M{x-4} {y+10} L{x-6} {y+16} M{x+4} {y+10} L{x+6} {y+16}', stroke_width=2.5) for x, y in SEG)
    + ''.join(z('circle', '#7cc4b0', cx=x, cy=y, r=13) + dot(x, y - 3, 3.5, '#f5d58a') for x, y in SEG)
    + s('path', d='M146 82 L140 66 M160 82 L166 66', stroke_width=2.5) + dot(140, 66, 3.5) + dot(166, 66, 3.5)
    + z('circle', '#7cc4b0', cx=152, cy=98, r=18)
    + dot(145, 96, 3) + dot(159, 96, 3) + ck(140, 104, 4, 2.5) + ck(164, 104, 4, 2.5) + smile(152, 106, 3)
)

# 20. snail
def spiral(cx, cy):
    pts = []
    for i in range(0, 101):
        t = i / 100 * 2.2 * 2 * math.pi
        r = 4 + 30 * i / 100
        pts.append(f'{cx + r * math.cos(t):.1f} {cy + r * math.sin(t):.1f}')
    return 'M' + ' L'.join(pts)
ITEMS['snail'] = (
    z('path', '#f6e0c4', d='M34 174 Q32 156 56 152 L150 152 Q176 156 174 174Z')
    + z('circle', '#f5b971', cx=124, cy=112, r=42)
    + s('path', d=spiral(124, 112), stroke_width=2.5)
    + s('path', d='M64 94 L56 64 M80 94 L88 64', stroke_width=3) + dot(56, 64, 5.5) + dot(88, 64, 5.5)
    + z('path', '#f6e0c4', d='M50 164 L52 114 Q54 92 72 92 Q90 94 88 114 L86 160Z')
    + dot(64, 114, 3) + dot(80, 114, 3) + ck(58, 124, 4, 2.5) + ck(86, 124, 4, 2.5) + smile(72, 126, 3)
)
