from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def fluff_d(cx, cy, rx, ry, n=12, bump=1.18, rot=0):
    """もこもこ（波形）の楕円パス"""
    pts = []
    for i in range(n + 1):
        a = (rot + i * 360 / n) * pi / 180
        pts.append((cx + rx * cos(a), cy + ry * sin(a)))
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(n):
        a = (rot + (i + 0.5) * 360 / n) * pi / 180
        qx, qy = cx + rx * bump * cos(a), cy + ry * bump * sin(a)
        d += f' Q{qx:.1f} {qy:.1f} {pts[i + 1][0]:.1f} {pts[i + 1][1]:.1f}'
    return d + 'Z'


def spikes_d(cx, cy, rx, ry, a0, a1, n, out=1.28, back=(0, 0)):
    """ハリネズミの針（a0→a1 度の範囲にギザギザ）"""
    d = ''
    for i in range(n + 1):
        a = (a0 + (a1 - a0) * i / n) * pi / 180
        x, y = cx + rx * cos(a), cy + ry * sin(a)
        d += (f'M{x:.1f} {y:.1f}' if i == 0 else f' L{x:.1f} {y:.1f}')
        if i < n:
            am = (a0 + (a1 - a0) * (i + 0.5) / n) * pi / 180
            d += f' L{cx + rx * out * cos(am):.1f} {cy + ry * out * sin(am):.1f}'
    return d + f' Q{back[0]} {back[1]} ' + d.split(' ')[0][1:] + ' ' + d.split(' ')[1] + 'Z'


def nose(x, y, rx=5, ry=3.5):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{OUT}" stroke="none"/>'


def wmouth(cx, cy):
    return s('path', d=f'M{cx-6} {cy} Q{cx-3} {cy+4} {cx} {cy} Q{cx+3} {cy+4} {cx+6} {cy}', stroke_width=2.5)


# 1. shiba inu
OR = '#f5b971'; CR = '#f6e0c4'
ITEMS['shiba-dog'] = (
    z('circle', OR, cx=144, cy=118, r=16) + s('circle', CR, cx=144, cy=118, r=6, stroke_width=2.5)
    + z('ellipse', OR, cx=100, cy=144, rx=38, ry=36)
    + s('ellipse', CR, cx=100, cy=150, rx=20, ry=24, stroke='none')
    + z('ellipse', CR, cx=86, cy=178, rx=11, ry=7) + z('ellipse', CR, cx=114, cy=178, rx=11, ry=7)
    + z('path', OR, d='M70 74 L72 38 L98 58Z') + z('path', OR, d='M130 74 L128 38 L102 58Z')
    + s('path', CR, d='M76 64 L77 48 L88 57Z', stroke='none') + s('path', CR, d='M124 64 L123 48 L112 57Z', stroke='none')
    + z('circle', OR, cx=100, cy=86, r=33)
    + s('path', CR, d='M70 96 Q76 84 100 90 Q124 84 130 96 Q126 118 100 119 Q74 118 70 96Z', stroke='none')
    + dot(88, 74, 3, CR) + dot(112, 74, 3, CR)
    + dot(88, 84) + dot(112, 84) + cheeks(76, 124, 100, 6, 3.5)
    + nose(100, 96) + wmouth(100, 101)
)

# 2. poodle
PB = '#d9a66b'
ITEMS['poodle'] = (
    z('path', PB, d=fluff_d(100, 146, 36, 30, 12))
    + z('path', PB, d=fluff_d(84, 178, 12, 7, 6)) + z('path', PB, d=fluff_d(116, 178, 12, 7, 6))
    + z('path', PB, d=fluff_d(64, 102, 14, 24, 8)) + z('path', PB, d=fluff_d(136, 102, 14, 24, 8))
    + z('path', PB, d=fluff_d(100, 54, 24, 16, 9))
    + z('path', PB, d=fluff_d(100, 88, 30, 28, 14, 1.12))
    + z('path', '#f07a8a', d='M100 44 L84 36 L84 52Z') + z('path', '#f07a8a', d='M100 44 L116 36 L116 52Z')
    + z('circle', '#f07a8a', cx=100, cy=44, r=5)
    + dot(89, 86) + dot(111, 86) + cheeks(80, 120, 98, 6, 3.5)
    + nose(100, 97) + wmouth(100, 102)
)

# 3. dachshund (side view, facing right)
DB = '#9a6a3f'; DE = '#8b6b4f'
ITEMS['dachshund'] = (
    thick('M42 112 Q30 104 28 90', DB, 10, 5)
    + z('rect', DB, x=48, y=124, width=14, height=36, rx=6) + z('rect', DB, x=114, y=124, width=14, height=36, rx=6)
    + z('ellipse', DB, cx=88, cy=118, rx=54, ry=24)
    + z('rect', DB, x=66, y=128, width=14, height=34, rx=6) + z('rect', DB, x=130, y=128, width=14, height=34, rx=6)
    + s('path', d='M80 134 Q96 140 112 134', stroke_width=2)
    + z('ellipse', DB, cx=168, cy=104, rx=14, ry=11)
    + z('circle', DB, cx=146, cy=90, r=24)
    + dot(176, 99, 4.5)
    + z('ellipse', DE, cx=134, cy=102, rx=10, ry=19, transform='rotate(15 134 102)')
    + dot(154, 86) + s('ellipse', CH, cx=158, cy=100, rx=5, ry=3, stroke='none')
    + s('path', d='M162 110 Q168 114 174 110', stroke_width=2.5)
    + s('path', d='M30 166 L176 166', stroke_width=2)
)

# 4. corgi (side body, face front, facing left)
WH = '#f4f4f0'
ITEMS['corgi'] = (
    z('ellipse', WH, cx=150, cy=118, rx=16, ry=18)
    + z('rect', WH, x=118, y=130, width=16, height=30, rx=7) + z('rect', WH, x=70, y=130, width=16, height=30, rx=7)
    + z('ellipse', OR, cx=110, cy=122, rx=48, ry=28)
    + s('path', WH, d='M68 128 Q100 156 140 136 Q130 150 100 150 Q76 148 68 128Z', stroke='none')
    + z('rect', WH, x=84, y=134, width=16, height=28, rx=7) + z('rect', WH, x=132, y=134, width=16, height=28, rx=7)
    + z('path', OR, d='M42 72 L36 30 L68 56Z') + z('path', OR, d='M90 70 L100 30 L70 54Z')
    + s('path', '#f6a6b8', d='M45 64 L42 42 L59 56Z', stroke='none') + s('path', '#f6a6b8', d='M86 63 L93 42 L77 55Z', stroke='none')
    + z('circle', OR, cx=66, cy=86, r=30)
    + s('path', WH, d='M66 66 Q60 80 44 92 Q46 114 66 115 Q86 114 88 92 Q72 80 66 66Z', stroke='none')
    + dot(55, 86) + dot(77, 86) + cheeks(45, 87, 98, 5.5, 3.5)
    + nose(66, 96, 4.5, 3.2) + wmouth(66, 101)
    + s('path', d='M40 166 L166 166', stroke_width=2)
)

# 5. golden retriever (sitting, tongue out)
GD = '#f5d58a'; GE = '#f5b971'
ITEMS['golden-retriever'] = (
    s('path', d='M134 166 Q166 160 168 128', stroke_width=14) + s('path', d='M134 166 Q166 160 168 128', stroke=GD, stroke_width=8)
    + z('ellipse', GD, cx=100, cy=144, rx=40, ry=38)
    + s('path', d='M88 124 Q92 132 88 140 M100 128 Q104 136 100 144 M112 124 Q116 132 112 140', stroke_width=2.5)
    + z('ellipse', GD, cx=84, cy=180, rx=12, ry=7) + z('ellipse', GD, cx=116, cy=180, rx=12, ry=7)
    + z('circle', GD, cx=100, cy=84, r=34)
    + z('path', GE, d='M70 66 Q50 82 56 116 Q72 116 78 98 Q80 80 70 66Z')
    + z('path', GE, d='M130 66 Q150 82 144 116 Q128 116 122 98 Q120 80 130 66Z')
    + s('ellipse', '#f6e0c4', cx=100, cy=98, rx=16, ry=12, stroke='none')
    + dot(88, 82) + dot(112, 82) + cheeks(78, 122, 96, 6, 3.5)
    + nose(100, 93) + s('path', d='M92 100 Q96 104 100 100 Q104 104 108 100', stroke_width=2.5)
    + z('path', '#f07a8a', d='M94 102 L106 102 L106 110 Q100 118 94 110Z')
)

# 6. bulldog
BF = '#f6e0c4'; BP = '#d9a66b'
ITEMS['bulldog'] = (
    z('ellipse', BF, cx=100, cy=146, rx=48, ry=32)
    + s('ellipse', BP, cx=124, cy=140, rx=14, ry=12, stroke='none')
    + z('ellipse', BF, cx=70, cy=176, rx=15, ry=8) + z('ellipse', BF, cx=130, cy=176, rx=15, ry=8)
    + z('path', BP, d='M60 72 L54 50 L80 62Z') + z('path', BP, d='M140 72 L146 50 L120 62Z')
    + z('ellipse', BF, cx=100, cy=94, rx=44, ry=36)
    + s('ellipse', BP, cx=82, cy=84, rx=13, ry=12, stroke='none')
    + s('path', d='M88 68 Q100 64 112 68 M92 74 Q100 71 108 74', stroke_width=2.5)
    + z('path', BF, d='M78 104 Q78 128 100 128 Q122 128 122 104Z')
    + s('path', WH, d='M88 112 L92 104 L96 112Z', stroke_width=2) + s('path', WH, d='M104 112 L108 104 L112 112Z', stroke_width=2)
    + z('path', BF, d='M74 104 Q74 92 100 98 Q126 92 126 104 Q120 116 100 108 Q80 116 74 104Z')
    + dot(82, 86) + dot(118, 86) + cheeks(66, 134, 100, 6, 3.5)
    + nose(100, 98, 7, 4.5)
)

# 7. cat sleeping (curled up on a cushion)
GR = '#b9a99c'
ITEMS['cat-sleeping'] = (
    z('ellipse', '#8fb3e0', cx=100, cy=160, rx=72, ry=18)
    + z('ellipse', GR, cx=110, cy=136, rx=54, ry=32)
    + s('path', d='M110 106 Q114 116 108 124 M128 108 Q132 118 126 126 M146 116 Q148 124 142 130', stroke_width=2.5)
    + thick('M160 140 Q160 168 120 168 Q90 168 72 160', GR, 14, 8)
    + z('path', GR, d='M52 116 L50 88 L72 102Z') + z('path', GR, d='M90 108 L96 82 L74 96Z')
    + s('path', '#f6a6b8', d='M55 108 L54 95 L65 102Z', stroke='none')
    + z('ellipse', GR, cx=72, cy=130, rx=28, ry=24)
    + s('path', d='M58 128 Q63 132 68 128 M76 128 Q81 132 86 128', stroke_width=2.5)
    + cheeks(56, 90, 138, 5.5, 3.2)
    + s('path', '#f6a6b8', d='M69 136 L75 136 L72 139Z', stroke_width=1.5)
    + s('circle', '#d8eef8', cx=50, cy=146, r=7, stroke_width=2)
)

# 8. black cat (sitting, tail up)
BK = '#5b6b7a'; LT = '#e8e1d8'
ITEMS['black-cat'] = (
    s('path', d='M128 168 Q164 162 160 126 Q156 96 172 84', stroke_width=14)
    + s('path', d='M128 168 Q164 162 160 126 Q156 96 172 84', stroke=BK, stroke_width=8)
    + z('ellipse', BK, cx=100, cy=144, rx=36, ry=36)
    + z('ellipse', BK, cx=86, cy=178, rx=11, ry=7) + z('ellipse', BK, cx=114, cy=178, rx=11, ry=7)
    + z('path', BK, d='M70 76 L70 40 L98 58Z') + z('path', BK, d='M130 76 L130 40 L102 58Z')
    + s('path', '#f6a6b8', d='M76 64 L76 50 L88 58Z', stroke='none') + s('path', '#f6a6b8', d='M124 64 L124 50 L112 58Z', stroke='none')
    + z('circle', BK, cx=100, cy=88, r=32)
    + s('ellipse', '#ffe27a', cx=87, cy=86, rx=7, ry=8, stroke_width=2) + s('ellipse', '#ffe27a', cx=113, cy=86, rx=7, ry=8, stroke_width=2)
    + s('ellipse', OUT, cx=87, cy=86, rx=2.2, ry=5.5, stroke='none') + s('ellipse', OUT, cx=113, cy=86, rx=2.2, ry=5.5, stroke='none')
    + cheeks(76, 124, 101, 6, 3.5)
    + s('path', '#f6a6b8', d='M96 97 L104 97 L100 101Z', stroke='none')
    + s('path', d='M94 103 Q97 107 100 103 Q103 107 106 103', stroke=LT, stroke_width=2.5)
    + s('path', d='M66 94 L54 91 M66 100 L54 102 M134 94 L146 91 M134 100 L146 102', stroke=LT, stroke_width=2)
)

# 9. kitten playing with yarn
YB = '#8fb3e0'
ITEMS['kitten-yarn'] = (
    s('path', d='M128 168 Q100 176 82 170 Q64 164 52 172', stroke=YB, stroke_width=3)
    + s('path', d='M42 150 Q30 132 40 118', stroke_width=13) + s('path', d='M42 150 Q30 132 40 118', stroke=WH, stroke_width=7)
    + z('ellipse', WH, cx=76, cy=146, rx=32, ry=28)
    + z('ellipse', WH, cx=64, cy=172, rx=10, ry=6)
    + z('path', WH, d='M52 80 L52 50 L74 66Z') + z('path', OR, d='M104 80 L104 50 L82 66Z')
    + s('path', '#f6a6b8', d='M57 72 L57 60 L66 66Z', stroke='none')
    + z('circle', WH, cx=78, cy=92, r=28)
    + s('path', OR, d='M84 66 Q104 68 105 92 Q96 84 84 66Z', stroke='none')
    + dot(68, 92) + dot(90, 92) + cheeks(59, 99, 103, 5.5, 3.2)
    + s('path', '#f6a6b8', d='M75 100 L81 100 L78 103Z', stroke='none')
    + s('path', '#c0504d', d='M72 106 Q78 116 84 106Z', stroke_width=2)
    + z('circle', YB, cx=142, cy=150, r=26)
    + s('path', d='M120 140 Q142 128 164 142 M118 154 Q142 142 166 156 M126 168 Q146 156 164 166 M134 126 Q150 146 140 174', stroke='#5b6b7a', stroke_width=2)
    + thick('M92 138 Q106 130 116 128', WH, 15, 9)
    + z('ellipse', WH, cx=120, cy=128, rx=10, ry=8, transform='rotate(-20 120 128)')
    + s('path', d='M118 122 L120 130 M124 121 L126 129', stroke_width=1.8)
)

# 10. guinea pig (side view, facing left)
GB = '#d9a66b'
ITEMS['guinea-pig'] = (
    z('ellipse', '#f6a6b8', cx=72, cy=164, rx=9, ry=5) + z('ellipse', '#f6a6b8', cx=130, cy=164, rx=9, ry=5)
    + z('path', WH, d='M40 126 Q40 82 92 80 Q160 80 166 128 Q166 162 110 162 L70 162 Q40 160 40 126Z')
    + s('path', GB, d='M112 81 Q160 82 166 128 Q166 162 120 162 Q128 120 112 81Z', stroke='none')
    + s('path', GB, d='M58 92 Q74 82 88 84 Q92 104 80 116 Q62 118 56 100Z', stroke='none')
    + s('path', d='M40 126 Q40 82 92 80 Q160 80 166 128 Q166 162 110 162 L70 162 Q40 160 40 126Z')
    + z('path', '#8b6b4f', d='M80 84 Q78 66 92 68 Q100 76 94 88Z')
    + s('path', '#f6a6b8', d='M84 82 Q84 72 91 73 Q95 78 92 84Z', stroke='none')
    + dot(68, 104, 4) + s('ellipse', CH, cx=62, cy=120, rx=6, ry=3.5, stroke='none')
    + dot(42, 122, 3.5, '#f07a8a')
    + s('path', d='M44 130 Q49 134 54 130', stroke_width=2.5)
    + s('path', d='M46 124 L32 120 M46 128 L32 132', stroke_width=1.8)
)

# 11. budgie parakeet on a branch
ITEMS['parakeet'] = (
    z('path', '#8fb3e0', d='M92 146 L96 186 L104 186 L108 146Z')
    + z('ellipse', '#9ccf7a', cx=100, cy=118, rx=32, ry=40)
    + z('ellipse', '#7cc4a0', cx=70, cy=122, rx=12, ry=28, transform='rotate(12 70 122)')
    + z('ellipse', '#7cc4a0', cx=130, cy=122, rx=12, ry=28, transform='rotate(-12 130 122)')
    + s('path', d='M64 108 Q70 104 74 108 M64 120 Q70 116 76 120 M66 132 Q72 128 76 132', stroke_width=2)
    + s('path', d='M126 108 Q130 104 136 108 M124 120 Q130 116 136 120 M124 132 Q128 128 134 132', stroke_width=2)
    + z('rect', '#9a6a3f', x=30, y=154, width=140, height=12, rx=6)
    + s('path', '#f6a6b8', d='M86 152 Q86 162 92 162 M114 152 Q114 162 108 162', stroke_width=3)
    + z('circle', '#ffe27a', cx=100, cy=72, r=30)
    + s('path', d='M80 54 Q86 50 92 54 M108 54 Q114 50 120 54', stroke_width=2)
    + dot(88, 72) + dot(112, 72) + cheeks(76, 124, 86, 5.5, 3.5)
    + s('path', '#8fb3e0', d='M93 78 Q100 72 107 78Z', stroke_width=2)
    + z('path', '#f5b971', d='M93 80 Q100 76 107 80 Q104 92 100 94 Q96 92 93 80Z')
    + dot(90, 98, 2.5) + dot(100, 101, 2.5) + dot(110, 98, 2.5)
)

# 12. turtle (side view, facing right)
TG = '#9ccf7a'; TS = '#7cc4a0'
ITEMS['turtle'] = (
    z('path', TG, d='M40 134 L26 128 L40 124Z')
    + z('ellipse', TG, cx=60, cy=150, rx=14, ry=12) + z('ellipse', TG, cx=128, cy=150, rx=14, ry=12)
    + z('path', TG, d='M140 132 Q146 108 158 102 L164 120 Q154 130 148 140Z')
    + z('circle', TG, cx=158, cy=98, r=22)
    + dot(152, 94) + dot(168, 94) + cheeks(146, 172, 104, 5, 3)
    + s('path', d='M155 106 Q160 110 165 106', stroke_width=2.5)
    + z('path', TS, d='M34 136 Q38 66 94 64 Q150 66 152 136Z')
    + s('path', '#9ccf7a', d='M78 96 L94 86 L110 96 L110 114 L94 124 L78 114Z', stroke_width=2.5)
    + s('path', d='M78 96 L60 90 M110 96 L128 90 M78 114 L56 122 M110 114 L132 122 M94 86 L94 66 M94 124 L94 136', stroke_width=2.5)
    + z('rect', '#f5d58a', x=28, y=132, width=130, height=12, rx=6)
)

# 13. hedgehog (side view, facing left)
HB = '#9a6a3f'; HF = '#f6e0c4'
ITEMS['hedgehog'] = (
    z('ellipse', HF, cx=82, cy=166, rx=9, ry=6) + z('ellipse', HF, cx=130, cy=166, rx=9, ry=6)
    + z('path', HF, d='M40 140 Q46 112 80 104 L120 110 Q150 130 146 150 Q130 164 90 164 Q50 162 40 140Z')
    + z('path', HB, d=spikes_d(110, 128, 50, 40, -170, 20, 11, 1.3, back=(90, 150)))
    + s('path', d='M110 92 Q118 100 114 110 M132 104 Q138 112 132 120', stroke_width=2)
    + dot(36, 138, 4.5)
    + dot(62, 128) + s('ellipse', CH, cx=64, cy=142, rx=6, ry=3.5, stroke='none')
    + s('path', d='M46 148 Q51 152 56 148', stroke_width=2.5)
)

# 14. gecko lizard (top view)
LG = '#9ccf7a'
ITEMS['lizard'] = (
    thick('M100 128 Q100 160 124 166 Q150 172 160 150', LG, 16, 10)
    + thick('M88 86 Q70 84 62 70', LG, 12, 7) + thick('M112 86 Q130 84 138 70', LG, 12, 7)
    + thick('M88 120 Q70 124 62 142', LG, 12, 7) + thick('M112 120 Q130 124 138 142', LG, 12, 7)
    + ''.join(s('circle', LG, cx=x, cy=y, r=4, stroke_width=2) for x, y in
              [(56, 66), (62, 61), (68, 66), (132, 66), (138, 61), (144, 66),
               (56, 146), (62, 151), (68, 146), (132, 146), (138, 151), (144, 146)])
    + z('ellipse', LG, cx=100, cy=104, rx=20, ry=32)
    + dot(94, 98, 3, '#f5d58a') + dot(106, 112, 3, '#f5d58a') + dot(95, 122, 2.5, '#f5d58a') + dot(108, 92, 2.5, '#f5d58a')
    + z('ellipse', LG, cx=100, cy=60, rx=24, ry=20)
    + dot(88, 56, 4) + dot(112, 56, 4) + cheeks(82, 118, 66, 5, 3)
    + s('path', d='M92 66 Q100 72 108 66', stroke_width=2.5)
)

# 15. dairy cow
ITEMS['cow'] = (
    z('ellipse', WH, cx=100, cy=146, rx=42, ry=34)
    + s('path', BK, d='M66 130 Q74 120 86 128 Q88 142 74 146 Q64 142 66 130Z', stroke='none')
    + s('path', BK, d='M118 150 Q128 140 138 148 Q138 164 124 166 Q114 160 118 150Z', stroke='none')
    + z('ellipse', WH, cx=78, cy=178, rx=14, ry=7) + z('ellipse', WH, cx=122, cy=178, rx=14, ry=7)
    + z('path', '#f5d58a', d='M80 60 Q72 44 78 36 Q86 46 90 56Z') + z('path', '#f5d58a', d='M120 60 Q128 44 122 36 Q114 46 110 56Z')
    + z('ellipse', WH, cx=60, cy=78, rx=16, ry=8, transform='rotate(20 60 78)')
    + z('ellipse', WH, cx=140, cy=78, rx=16, ry=8, transform='rotate(-20 140 78)')
    + z('ellipse', WH, cx=100, cy=86, rx=32, ry=32)
    + s('path', BK, d='M106 56 Q124 56 130 74 Q120 84 108 74 Q102 64 106 56Z', stroke='none')
    + dot(88, 82) + dot(114, 82) + cheeks(76, 126, 94, 5.5, 3.5)
    + z('ellipse', '#f6a6b8', cx=100, cy=106, rx=24, ry=14)
    + nose(92, 104, 3, 4) + nose(108, 104, 3, 4)
    + s('path', d='M94 112 Q100 116 106 112', stroke_width=2.5)
    + z('circle', '#ffc94d', cx=100, cy=130, r=8)
    + dot(100, 133, 2)
)

# 16. pink pig
PK = '#f6a6b8'
ITEMS['pig'] = (
    s('path', d='M136 140 Q152 138 150 128 Q146 120 140 128 Q138 136 150 140 Q158 140 160 132', stroke_width=3)
    + z('ellipse', PK, cx=100, cy=144, rx=40, ry=34)
    + z('ellipse', PK, cx=82, cy=178, rx=11, ry=7) + z('ellipse', PK, cx=118, cy=178, rx=11, ry=7)
    + z('path', PK, d='M68 68 L64 38 L94 54Z') + z('path', PK, d='M132 68 L136 38 L106 54Z')
    + s('path', '#f07a8a', d='M70 60 L68 46 L84 54Z', stroke='none') + s('path', '#f07a8a', d='M130 60 L132 46 L116 54Z', stroke='none')
    + z('circle', PK, cx=100, cy=88, r=34)
    + dot(86, 80) + dot(114, 80) + cheeks(74, 126, 94, 6, 3.5)
    + z('ellipse', '#f07a8a', cx=100, cy=98, rx=15, ry=11)
    + nose(95, 98, 2.5, 4) + nose(105, 98, 2.5, 4)
    + s('path', d='M94 113 Q100 118 106 113', stroke_width=2.5)
)

# 17. fluffy sheep (side view, facing left)
ITEMS['sheep'] = (
    z('rect', BK, x=70, y=136, width=12, height=36, rx=5) + z('rect', BK, x=128, y=136, width=12, height=36, rx=5)
    + z('rect', BK, x=84, y=138, width=12, height=36, rx=5) + z('rect', BK, x=142, y=136, width=12, height=34, rx=5)
    + z('path', WH, d=fluff_d(114, 116, 54, 36, 14, 1.14))
    + z('ellipse', '#f6e0c4', cx=48, cy=96, rx=14, ry=7, transform='rotate(20 48 96)')
    + z('ellipse', '#f6e0c4', cx=66, cy=104, rx=22, ry=26)
    + z('path', WH, d=fluff_d(70, 80, 18, 10, 7, 1.25))
    + z('ellipse', '#f6e0c4', cx=90, cy=90, rx=14, ry=7, transform='rotate(-20 90 90)')
    + dot(58, 102) + dot(76, 102) + cheeks(52, 82, 114, 5, 3)
    + s('path', d='M62 120 Q67 124 72 120', stroke_width=2.5)
)

# 18. horse (side view, facing left)
HO = '#d9a66b'; HM = '#8b6b4f'
ITEMS['horse'] = (
    s('path', HM, d='M150 100 Q174 110 170 150 Q160 140 156 150 Q150 128 146 112Z')
    + z('rect', HO, x=78, y=118, width=13, height=50, rx=5) + z('rect', HO, x=134, y=118, width=13, height=50, rx=5)
    + z('rect', HM, x=76, y=164, width=17, height=10, rx=3) + z('rect', HM, x=132, y=164, width=17, height=10, rx=3)
    + z('path', HO, d='M74 108 L60 62 L88 52 L104 96Z')
    + z('ellipse', HO, cx=116, cy=110, rx=44, ry=26)
    + z('rect', HO, x=92, y=122, width=13, height=46, rx=5) + z('rect', HO, x=148, y=118, width=13, height=50, rx=5)
    + z('rect', HM, x=90, y=164, width=17, height=10, rx=3) + z('rect', HM, x=146, y=164, width=17, height=10, rx=3)
    + z('path', HO, d='M66 42 L70 26 L80 40Z') + z('path', HO, d='M78 40 L86 26 L90 42Z')
    + z('path', HO, d='M84 50 Q80 34 66 38 Q48 44 36 70 Q32 84 46 86 Q60 86 70 70 Q86 64 84 50Z')
    + s('path', HM, d='M84 40 Q94 44 92 56 Q100 64 98 74 Q106 82 104 96 Q96 80 90 70 Q86 56 80 46Z', stroke_width=2.5)
    + s('path', HM, d='M64 38 Q70 32 78 38 Q72 46 64 38Z', stroke_width=2)
    + dot(66, 56) + s('ellipse', CH, cx=60, cy=68, rx=5.5, ry=3.5, stroke='none')
    + dot(40, 76, 2.5)
    + s('path', d='M42 82 Q47 84 52 80', stroke_width=2.5)
)

# 19. goat (side view, facing right)
ITEMS['goat'] = (
    thick('M54 104 Q44 96 46 86', WH, 10, 5)
    + z('rect', WH, x=60, y=120, width=11, height=46, rx=5) + z('rect', WH, x=112, y=120, width=11, height=46, rx=5)
    + z('rect', '#8b6b4f', x=58, y=162, width=15, height=9, rx=3) + z('rect', '#8b6b4f', x=110, y=162, width=15, height=9, rx=3)
    + z('path', WH, d='M116 104 L128 74 L148 80 L134 112Z')
    + z('ellipse', WH, cx=94, cy=114, rx=42, ry=24)
    + z('rect', WH, x=74, y=122, width=11, height=44, rx=5) + z('rect', WH, x=124, y=120, width=11, height=46, rx=5)
    + z('rect', '#8b6b4f', x=72, y=162, width=15, height=9, rx=3) + z('rect', '#8b6b4f', x=122, y=162, width=15, height=9, rx=3)
    + thick('M136 58 Q124 36 108 40', '#b9a99c', 11, 6) + thick('M144 58 Q138 34 122 32', '#b9a99c', 11, 6)
    + z('ellipse', WH, cx=122, cy=70, rx=14, ry=6, transform='rotate(20 122 70)')
    + z('path', WH, d='M152 104 L150 124 L162 106Z')
    + z('path', WH, d='M126 70 Q126 52 142 52 Q156 54 164 80 Q170 98 160 104 Q148 108 140 92 Q128 86 126 70Z')
    + dot(144, 70) + s('ellipse', CH, cx=150, cy=84, rx=5, ry=3, stroke='none')
    + dot(164, 92, 2.5)
    + s('path', d='M154 98 Q159 101 164 98', stroke_width=2.5)
)

# 20. hen (side view, facing left)
RD = '#e04b5a'
ITEMS['hen'] = (
    s('path', d='M98 156 L96 178 M96 178 L86 182 M96 178 L100 184 M118 156 L120 178 M120 178 L110 182 M120 178 L126 184',
      stroke='#f5b971', stroke_width=5)
    + z('path', WH, d='M128 112 Q136 70 152 56 Q152 74 160 66 Q160 84 170 80 Q166 96 176 98 Q168 116 150 120Z')
    + z('path', WH, d='M58 100 Q60 156 108 160 Q156 160 160 118 Q150 100 128 104 Q100 108 92 92Z')
    + z('path', RD, d='M54 56 Q52 42 62 44 Q64 32 74 38 Q80 30 86 42 Q92 46 84 56Z')
    + z('circle', WH, cx=72, cy=74, r=24)
    + z('path', '#ffc94d', d='M50 70 L34 78 L50 84Z')
    + z('path', RD, d='M50 86 Q44 98 52 102 Q60 98 56 86Z')
    + dot(64, 70) + s('ellipse', CH, cx=70, cy=84, rx=5.5, ry=3.5, stroke='none')
    + z('path', WH, d='M96 122 Q118 110 140 122 Q132 146 108 142 Q96 136 96 122Z')
    + s('path', d='M106 130 Q118 124 130 128 M108 138 Q120 132 130 136', stroke_width=2)
)
