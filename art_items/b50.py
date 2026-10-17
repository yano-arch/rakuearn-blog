from math import sin, cos, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def thick(d, color, w=9, inner=4.5):
    """太い色線（外側こげ茶＋内側色）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def star_d(cx, cy, R, r, rot=-90):
    pts = []
    for i in range(10):
        a = (rot + i * 36) * pi / 180
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr * cos(a):.1f} {cy + rr * sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


def sparkle(x, y, r=7, w=2.5):
    return s('path', d=f'M{x} {y-r} L{x} {y+r} M{x-r} {y} L{x+r} {y}', stroke_width=w)


def ring_d(cx, cy, R, r):
    return (f'M{cx-R} {cy} A{R} {R} 0 1 0 {cx+R} {cy} A{R} {R} 0 1 0 {cx-R} {cy}Z '
            f'M{cx-r} {cy} A{r} {r} 0 1 0 {cx+r} {cy} A{r} {r} 0 1 0 {cx-r} {cy}Z')


def mini_face(cx, cy, gap=12, cg=20, r=3.5):
    return (dot(cx - gap, cy, r) + dot(cx + gap, cy, r) + cheeks(cx - cg, cx + cg, cy + 9, 6, 3.5)
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))


# 1. halloween ghost
ITEMS['halloween-ghost'] = (
    z('ellipse', '#ffffff', cx=50, cy=118, rx=12, ry=8, transform='rotate(-30 50 118)')
    + z('ellipse', '#ffffff', cx=150, cy=118, rx=12, ry=8, transform='rotate(30 150 118)')
    + z('path', '#ffffff', d='M56 170 L56 94 Q56 40 100 40 Q144 40 144 94 L144 170 '
        'Q133 180 122 170 Q111 160 100 170 Q89 180 78 170 Q67 160 56 170Z')
    + dot(86, 96, 4.5) + dot(114, 96, 4.5) + cheeks(74, 126, 110)
    + s('ellipse', '#c0504d', cx=100, cy=118, rx=6, ry=8, stroke_width=2.5)
    + z('path', '#ffe27a', d=star_d(160, 50, 11, 5)) + z('path', '#ffe27a', d=star_d(38, 66, 8, 3.5))
)

# 2. witch hat
ITEMS['witch-hat'] = (
    z('ellipse', '#7a5ea8', cx=100, cy=150, rx=74, ry=20)
    + z('path', '#a98bd0', d='M62 150 L90 76 Q100 46 136 40 Q118 58 116 78 L138 150 Q100 160 62 150Z')
    + z('path', '#ffc94d', d='M70 128 Q100 134 130 128 L136 144 Q100 152 64 144Z')
    + s('rect', '#ffe27a', x=92, y=128, width=16, height=18, rx=2, stroke_width=2.5)
    + s('rect', '#a98bd0', x=97, y=133, width=6, height=8, rx=1, stroke_width=2)
    + z('path', '#ffe27a', d=star_d(46, 62, 11, 5)) + z('path', '#ffe27a', d=star_d(160, 90, 9, 4))
    + sparkle(158, 40, 6)
)


# 3. trick or treat candy pail
def candy(cx, cy, col, ang=0):
    t = f'rotate({ang} {cx} {cy})'
    return (s('path', col, d=f'M{cx-10} {cy} L{cx-22} {cy-8} L{cx-22} {cy+8}Z', transform=t, stroke_width=2.5)
            + s('path', col, d=f'M{cx+10} {cy} L{cx+22} {cy-8} L{cx+22} {cy+8}Z', transform=t, stroke_width=2.5)
            + z('ellipse', col, cx=cx, cy=cy, rx=13, ry=10, transform=t))


ITEMS['trick-or-treat'] = (
    s('path', d='M52 104 Q100 18 148 104', stroke_width=4)
    + z('ellipse', '#e8735a', cx=100, cy=104, rx=50, ry=13)
    + s('path', d='M120 100 L132 56', stroke_width=7) + s('path', d='M120 100 L132 56', stroke='#ffffff', stroke_width=3)
    + z('circle', '#f6a6b8', cx=134, cy=50, r=13)
    + s('path', d='M134 42 Q142 50 134 58 Q126 50 134 42', stroke_width=2)
    + candy(76, 94, '#8fc7e8', -20) + candy(104, 88, '#ffe27a', 10)
    + z('path', '#f5b971', d='M50 104 Q50 178 100 178 Q150 178 150 104 Q100 124 50 104Z')
    + s('path', OUT, d='M74 130 L84 118 L94 130Z', stroke_width=2) + s('path', OUT, d='M106 130 L116 118 L126 130Z', stroke_width=2)
    + cheeks(68, 132, 140, 7, 4)
    + s('path', OUT, d='M80 146 Q100 166 120 146 Q100 154 80 146Z', stroke_width=2.5)
)

# 4. halloween bat and moon
ITEMS['halloween-bat'] = (
    z('circle', '#ffe27a', cx=112, cy=86, r=56)
    + s('circle', '#f5d58a', cx=140, cy=64, r=8, stroke='none') + s('circle', '#f5d58a', cx=86, cy=60, r=5, stroke='none')
    + z('path', '#7a5ea8', d='M86 110 Q66 82 30 92 Q42 102 38 116 Q52 108 60 122 Q70 112 84 128Z')
    + z('path', '#7a5ea8', d='M114 110 Q134 82 170 92 Q158 102 162 116 Q148 108 140 122 Q130 112 116 128Z')
    + z('path', '#a98bd0', d='M84 98 L80 74 L92 88 L108 88 L120 74 L116 98Z')
    + z('ellipse', '#a98bd0', cx=100, cy=116, rx=22, ry=26)
    + dot(91, 108) + dot(109, 108) + cheeks(84, 116, 118, 5, 3)
    + s('path', '#ffffff', d='M94 124 L96 130 L98 124Z', stroke_width=1.5) + s('path', '#ffffff', d='M102 124 L104 130 L106 124Z', stroke_width=1.5)
    + s('path', d='M92 123 L108 123', stroke_width=2.5)
    + z('path', '#ffe27a', d=star_d(40, 152, 9, 4)) + z('path', '#ffe27a', d=star_d(160, 160, 7, 3))
)

# 5. santa
ITEMS['santa'] = (
    z('path', '#e04b5a', d='M54 186 Q56 134 100 132 Q144 134 146 186Z')
    + z('circle', '#ffd9b8', cx=100, cy=94, r=32)
    + z('path', '#ffffff', d='M66 96 Q62 146 100 152 Q138 146 134 96 Q128 112 100 112 Q72 112 66 96Z')
    + dot(88, 92) + dot(112, 92) + cheeks(78, 122, 102, 6, 3.5)
    + s('path', '#ffffff', d='M100 106 Q88 100 82 110 Q92 114 100 108 Q108 114 118 110 Q112 100 100 106Z', stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=100, cy=101, r=5, stroke_width=2.5)
    + s('path', '#c0504d', d='M95 120 Q100 126 105 120Z', stroke_width=2)
    + z('path', '#e04b5a', d='M68 76 Q72 34 110 34 Q140 38 152 70 L142 74 Q132 56 120 54 Q132 64 132 76Z')
    + z('rect', '#ffffff', x=62, y=66, width=76, height=15, rx=7.5)
    + z('circle', '#ffffff', cx=150, cy=78, r=9)
    + s('rect', OUT, x=56, y=166, width=88, height=8, stroke='none')
    + s('rect', '#ffc94d', x=92, y=162, width=16, height=16, rx=2, stroke_width=2.5)
)

# 6. reindeer
ITEMS['reindeer'] = (
    thick('M82 66 Q70 46 58 30 M70 50 Q56 50 46 42 M76 58 Q78 44 74 34', '#9a6a3f', 10, 5.5)
    + thick('M118 66 Q130 46 142 30 M130 50 Q144 50 154 42 M124 58 Q122 44 126 34', '#9a6a3f', 10, 5.5)
    + z('ellipse', '#d9a66b', cx=104, cy=148, rx=40, ry=32)
    + z('ellipse', '#d9a66b', cx=82, cy=178, rx=11, ry=6) + z('ellipse', '#d9a66b', cx=124, cy=178, rx=11, ry=6)
    + s('ellipse', '#f6e0c4', cx=104, cy=154, rx=20, ry=16, stroke='none')
    + z('ellipse', '#d9a66b', cx=66, cy=80, rx=14, ry=8, transform='rotate(-25 66 80)')
    + z('ellipse', '#d9a66b', cx=134, cy=80, rx=14, ry=8, transform='rotate(25 134 80)')
    + z('circle', '#d9a66b', cx=100, cy=94, r=32)
    + z('ellipse', '#f6e0c4', cx=100, cy=112, rx=17, ry=12)
    + dot(88, 92) + dot(112, 92) + cheeks(78, 122, 102, 6, 3.5)
    + s('ellipse', '#5a4033', cx=100, cy=106, rx=7, ry=5.5, stroke_width=2.5)
    + s('path', d='M94 116 Q100 121 106 116', stroke_width=2.5)
)

# 7. wreath
_lv = ''
for i in range(12):
    a = i * 30 * pi / 180
    x, y = 100 + 46 * cos(a), 98 + 46 * sin(a)
    col = '#9ccf7a' if i % 2 else '#7cc4a0'
    _lv += s('ellipse', col, cx=round(x, 1), cy=round(y, 1), rx=13, ry=7,
             transform=f'rotate({i*30+60} {x:.1f} {y:.1f})', stroke_width=2.5)
_bry = ''.join(s('circle', '#5a4033', cx=round(100 + 46 * cos(a * pi / 180), 1), cy=round(98 + 46 * sin(a * pi / 180), 1), r=5, stroke_width=2)
               for a in (200, 250, 300, 345, 20, 160))
ITEMS['wreath'] = (
    z('path', '#7cc4a0', d=ring_d(100, 98, 64, 30), fill_rule='evenodd')
    + _lv + _bry
    + z('path', '#e04b5a', d='M100 146 Q78 124 68 140 Q70 158 100 146Z')
    + z('path', '#e04b5a', d='M100 146 Q122 124 132 140 Q130 158 100 146Z')
    + z('path', '#e04b5a', d='M96 148 L82 178 L92 174 L98 182 L102 150Z')
    + z('path', '#e04b5a', d='M104 148 L118 178 L108 174 L102 182 L98 150Z')
    + z('circle', '#e04b5a', cx=100, cy=146, r=8)
)

# 8. stocking
ITEMS['stocking'] = (
    s('path', d='M128 42 Q138 24 146 30 Q152 36 144 42', stroke_width=7) + s('path', d='M128 42 Q138 24 146 30 Q152 36 144 42', stroke='#e04b5a', stroke_width=3)
    + s('path', d='M122 60 L132 26 Q136 16 144 20', stroke_width=9) + s('path', d='M122 60 L132 26 Q136 16 144 20', stroke='#ffffff', stroke_width=5)
    + s('path', d='M126 46 L129 40 M128 36 L131 30', stroke='#e04b5a', stroke_width=4)
    + z('path', '#e04b5a', d='M76 70 L130 70 L130 124 Q130 140 118 150 L94 170 Q74 186 58 170 Q46 154 62 142 L76 132Z')
    + s('path', '#9ccf7a', d='M130 124 Q130 140 118 150 L104 162 Q100 138 130 124Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M76 162 Q70 174 62 172 Q50 162 58 150 Q70 150 76 162Z', stroke='none')
    + s('path', d='M76 162 Q70 174 62 172', stroke_width=2.5)
    + s('circle', '#ffffff', cx=96, cy=100, r=4, stroke='none') + s('circle', '#ffffff', cx=114, cy=114, r=4, stroke='none')
    + s('circle', '#ffffff', cx=92, cy=130, r=4, stroke='none') + s('circle', '#ffffff', cx=112, cy=88, r=4, stroke='none')
    + z('rect', '#ffffff', x=68, y=46, width=70, height=28, rx=8)
)

# 9. gingerbread man
ITEMS['gingerbread'] = (
    z('path', '#d9a66b', d='M78 86 L48 94 Q34 100 40 114 Q46 122 60 118 L76 112 L72 148 L62 164 Q56 178 70 180 Q80 180 84 170 L100 146 '
      'L116 170 Q120 180 130 180 Q144 178 138 164 L128 148 L124 112 L140 118 Q154 122 160 114 Q166 100 152 94 L122 86Z')
    + z('circle', '#d9a66b', cx=100, cy=60, r=30)
    + s('path', d='M46 100 Q50 104 46 108 Q50 112 46 114', stroke='#ffffff', stroke_width=3)
    + s('path', d='M154 100 Q150 104 154 108 Q150 112 154 114', stroke='#ffffff', stroke_width=3)
    + s('path', d='M62 168 Q68 172 74 168 Q78 172 82 168', stroke='#ffffff', stroke_width=3)
    + s('path', d='M118 168 Q122 172 126 168 Q132 172 138 168', stroke='#ffffff', stroke_width=3)
    + dot(89, 58) + dot(111, 58) + cheeks(79, 121, 68, 6, 3.5)
    + s('path', d='M92 72 Q100 78 108 72', stroke='#ffffff', stroke_width=3.5)
    + s('circle', '#e04b5a', cx=100, cy=100, r=6, stroke_width=2.5)
    + s('circle', '#9ccf7a', cx=100, cy=118, r=6, stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=100, cy=136, r=6, stroke_width=2.5)
)


# 10. christmas candle with holly
def holly(cx, cy, ang):
    d = (f'M{cx} {cy} Q{cx-6} {cy-8} {cx-4} {cy-16} Q{cx-10} {cy-18} {cx-10} {cy-24} '
         f'Q{cx-2} {cy-26} {cx} {cy-34} Q{cx+2} {cy-26} {cx+10} {cy-24} Q{cx+10} {cy-18} {cx+4} {cy-16} '
         f'Q{cx+6} {cy-8} {cx} {cy}Z')
    return z('path', '#7cc4a0', d=d, transform=f'rotate({ang} {cx} {cy})') + s('path', d=f'M{cx} {cy} L{cx} {cy-28}', transform=f'rotate({ang} {cx} {cy})', stroke_width=2)


ITEMS['christmas-candle'] = (
    z('path', '#ffc94d', d='M100 66 Q86 50 100 28 Q114 50 100 66Z')
    + s('path', '#ffe27a', d='M100 62 Q94 54 100 44 Q106 54 100 62Z', stroke='none')
    + s('path', d='M100 66 L100 74', stroke_width=3)
    + z('rect', '#e04b5a', x=76, y=74, width=48, height=92, rx=4)
    + s('path', '#ffffff', d='M76 80 Q76 74 82 74 L118 74 Q124 74 124 80 L124 92 Q120 98 116 92 L116 86 Q112 82 108 88 L108 100 Q104 106 100 100 L100 86 Q94 82 90 88 Q86 94 82 88 L82 84 Q78 82 76 86Z', stroke_width=2.5)
    + z('ellipse', '#f5d58a', cx=100, cy=170, rx=64, ry=12)
    + holly(86, 166, -60) + holly(114, 166, 60) + holly(70, 170, -84) + holly(130, 170, 84)
    + s('circle', '#e04b5a', cx=94, cy=160, r=6, stroke_width=2.5) + s('circle', '#e04b5a', cx=106, cy=160, r=6, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=100, cy=150, r=6, stroke_width=2.5)
    + dot(92, 120) + dot(108, 120) + cheeks(84, 116, 129, 5, 3) + s('path', d='M96 128 Q100 132 104 128', stroke_width=2.5)
)

# 11. snow globe
_snow = ''.join(s('circle', '#ffffff', cx=x, cy=y, r=3.5, stroke_width=1.5)
                for x, y in ((70, 64), (92, 46), (128, 58), (140, 84), (60, 92), (112, 70), (82, 78), (146, 106), (54, 112)))
ITEMS['snow-globe'] = (
    z('circle', '#d8eef8', cx=100, cy=90, r=62)
    + s('path', '#ffffff', d='M44 118 Q100 104 156 118 L144 140 L56 140Z', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M118 116 L134 84 L150 116Z') + s('rect', '#8b6b4f', x=131, y=116, width=6, height=8, stroke_width=2)
    + z('circle', '#ffffff', cx=94, cy=116, r=15)
    + z('circle', '#ffffff', cx=94, cy=90, r=11)
    + dot(90, 88, 2.2) + dot(98, 88, 2.2) + s('path', '#f5b971', d='M94 92 L104 94 L94 96Z', stroke_width=1.5)
    + s('path', d='M84 98 Q94 104 104 98', stroke='#e04b5a', stroke_width=4)
    + dot(94, 112, 2.2) + dot(94, 121, 2.2)
    + _snow
    + s('path', d='M66 50 Q74 40 86 38', stroke='#ffffff', stroke_width=5)
    + z('path', '#9a6a3f', d='M60 140 L140 140 L154 180 L46 180Z')
    + s('path', '#e04b5a', d='M54 158 L146 158 L150 168 L50 168Z', stroke_width=2.5)
)

# 12. red lantern
ITEMS['lunar-new-year-lantern'] = (
    s('path', d='M100 22 L100 50', stroke_width=3)
    + thick('M100 158 L100 168', '#ffc94d', 7, 3)
    + z('path', '#ffc94d', d='M92 168 L108 168 L114 184 L86 184Z')
    + s('path', d='M94 172 L92 184 M100 172 L100 184 M106 172 L108 184', stroke_width=2)
    + z('ellipse', '#e04b5a', cx=100, cy=106, rx=64, ry=50)
    + s('path', d='M100 56 L100 156')
    + s('path', d='M78 58 Q60 106 78 154 M122 58 Q140 106 122 154', stroke_width=2.5)
    + s('path', d='M58 66 Q30 106 58 146 M142 66 Q170 106 142 146', stroke_width=2.5)
    + z('rect', '#ffc94d', x=74, y=46, width=52, height=14, rx=4)
    + z('rect', '#ffc94d', x=74, y=150, width=52, height=14, rx=4)
    + s('rect', '#e04b5a', x=86, y=94, width=28, height=28, rx=6, stroke='none')
    + dot(90, 104) + dot(110, 104) + cheeks(80, 120, 114, 6, 3.5)
    + s('path', d='M95 113 Q100 118 105 113', stroke_width=2.5)
)

# 13. red envelope
ITEMS['red-envelope'] = (
    z('rect', '#e04b5a', x=56, y=32, width=82, height=134, rx=8)
    + s('path', '#f07a8a', d='M56 40 Q56 32 64 32 L130 32 Q138 32 138 40 L138 52 Q97 92 56 52Z', stroke_width=3)
    + z('circle', '#ffc94d', cx=97, cy=76, r=16)
    + s('path', d='M97 66 L97 86 M87 76 L107 76', stroke='#e04b5a', stroke_width=3)
    + s('circle', '#e04b5a', cx=97, cy=76, r=5, stroke_width=2)
    + s('path', d='M70 120 L124 120 M70 146 L124 146', stroke='#ffc94d', stroke_width=3)
    + s('path', d='M74 133 L80 127 L86 133 L80 139Z M94 133 L100 127 L106 133 L100 139Z M114 133 L120 127 L126 133 L120 139Z', stroke='#ffc94d', stroke_width=2.5)
    + z('circle', '#ffc94d', cx=148, cy=150, r=18) + s('rect', '#fbf6ee', x=142, y=144, width=12, height=12, rx=1, stroke_width=2.5)
    + z('circle', '#ffc94d', cx=126, cy=166, r=14) + s('rect', '#fbf6ee', x=121, y=161, width=10, height=10, rx=1, stroke_width=2.5)
    + sparkle(160, 46, 7) + sparkle(38, 86, 6)
)

# 14. wedding couple
_H = 'M100 32 C94 27 90 23 93 19 C96 16 100 18 100 21 C100 18 104 16 107 19 C110 23 106 27 100 32Z'
ITEMS['wedding-couple'] = (
    z('path', '#ffffff', d='M44 62 Q26 116 32 166 Q48 158 56 140 L70 64Z')
    + z('path', '#ffffff', d='M30 184 Q38 128 66 120 Q92 126 100 184Z')
    + s('path', d='M54 140 Q66 146 80 140', stroke_width=2.5)
    + z('path', '#5b6b7a', d='M102 184 Q104 128 134 120 Q162 128 166 184Z')
    + s('path', '#ffffff', d='M124 122 L134 146 L144 122 Q134 118 124 122Z', stroke_width=2.5)
    + s('path', OUT, d='M126 128 L134 132 L126 136Z M142 128 L134 132 L142 136Z', stroke_width=2)
    + face(66, 84, '#ffd9b8', '#5a4033', 'smile')
    + s('circle', '#f6a6b8', cx=46, cy=58, r=6, stroke_width=2.5) + s('circle', '#ffffff', cx=58, cy=50, r=6, stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=72, cy=48, r=6, stroke_width=2.5)
    + face(134, 84, '#ffd9b8', '#2b2220', 'smile')
    + z('circle', '#ffd9b8', cx=100, cy=158, r=9)
    + z('path', '#f07a8a', d=_H)
)

# 15. wedding cake
ITEMS['wedding-cake'] = (
    z('rect', '#ffffff', x=46, y=132, width=108, height=44, rx=5)
    + s('path', '#f6a6b8', d='M46 136 L154 136 L154 142 Q145 150 136 142 Q127 150 118 142 Q109 150 100 142 Q91 150 82 142 Q73 150 64 142 Q55 150 46 142Z', stroke_width=2.5)
    + z('rect', '#ffffff', x=62, y=96, width=76, height=36, rx=5)
    + s('path', '#f6a6b8', d='M62 100 L138 100 L138 106 Q128 114 119 106 Q110 114 100 106 Q90 114 81 106 Q72 114 62 106Z', stroke_width=2.5)
    + z('rect', '#ffffff', x=76, y=64, width=48, height=32, rx=5)
    + s('path', '#f6a6b8', d='M76 68 L124 68 L124 74 Q112 82 100 74 Q88 82 76 74Z', stroke_width=2.5)
    + ''.join(s('circle', '#f4f4f0', cx=x, cy=162, r=4, stroke_width=2) for x in (62, 82, 100, 118, 138))
    + ''.join(s('circle', '#f4f4f0', cx=x, cy=120, r=3.5, stroke_width=2) for x in (76, 92, 108, 124))
    + s('circle', '#f07a8a', cx=56, cy=126, r=6, stroke_width=2.5) + s('circle', '#f07a8a', cx=146, cy=126, r=6, stroke_width=2.5)
    + z('path', '#f07a8a', d='M90 62 C80 52 76 46 80 40 C84 34 90 37 90 42 C90 37 96 34 100 40 C104 46 100 52 90 62Z')
    + z('path', '#f6a6b8', d='M110 62 C100 52 96 46 100 40 C104 34 110 37 110 42 C110 37 116 34 120 40 C124 46 120 52 110 62Z')
    + s('path', d='M32 180 L168 180', stroke_width=2.5)
)

# 16. wedding rings
ITEMS['wedding-rings'] = (
    z('path', '#c9d3db', d=ring_d(124, 116, 38, 28), fill_rule='evenodd')
    + z('path', '#ffc94d', d=ring_d(80, 116, 38, 28), fill_rule='evenodd')
    + z('path', '#8fc7e8', d='M68 78 L74 68 L86 68 L92 78 L80 92Z')
    + s('path', d='M68 78 L92 78 M74 68 L80 78 L86 68 M80 78 L80 92', stroke_width=2)
    + sparkle(106, 52, 7) + sparkle(46, 60, 5) + sparkle(160, 64, 6)
    + z('path', '#f07a8a', d='M150 172 C142 165 138 160 141 155 C144 151 150 153 150 157 C150 153 156 151 159 155 C162 160 158 165 150 172Z')
)


# 17. bridal bouquet
def flower(cx, cy, col, r=13):
    o = ''
    for i in range(5):
        a = (i * 72 - 90) * pi / 180
        o += s('circle', col, cx=round(cx + r * 0.75 * cos(a), 1), cy=round(cy + r * 0.75 * sin(a), 1), r=r * 0.62, stroke_width=2.5)
    return o + s('circle', '#ffe27a', cx=cx, cy=cy, r=r * 0.38, stroke_width=2)


ITEMS['bouquet'] = (
    z('ellipse', '#9ccf7a', cx=62, cy=82, rx=16, ry=8, transform='rotate(-35 62 82)')
    + z('ellipse', '#9ccf7a', cx=140, cy=80, rx=16, ry=8, transform='rotate(35 140 80)')
    + z('ellipse', '#7cc4a0', cx=100, cy=44, rx=8, ry=14)
    + z('circle', '#9ccf7a', cx=100, cy=86, r=40)
    + flower(78, 72, '#f6a6b8') + flower(116, 64, '#ffffff') + flower(100, 96, '#f07a8a')
    + flower(124, 98, '#f6a6b8', 11) + flower(76, 104, '#ffffff', 11) + flower(96, 58, '#f07a8a', 10)
    + z('path', '#ffffff', d='M68 118 L132 118 L108 180 L92 180Z')
    + s('path', d='M84 124 L96 176 M116 124 L104 176', stroke_width=2)
    + z('path', '#f6a6b8', d='M100 136 Q80 120 76 134 Q80 148 100 136Z')
    + z('path', '#f6a6b8', d='M100 136 Q120 120 124 134 Q120 148 100 136Z')
    + s('path', '#f6a6b8', d='M98 138 L88 166 L96 162 L100 138Z', stroke_width=2.5)
    + s('path', '#f6a6b8', d='M102 138 L112 166 L104 162 L100 138Z', stroke_width=2.5)
    + s('circle', '#f07a8a', cx=100, cy=136, r=6, stroke_width=2.5)
)


# 18. champagne toast
def flute(cx, cy, ang):
    t = f'rotate({ang} {cx} {cy})'
    return (s('path', d=f'M{cx} {cy-8} L{cx} {cy+32}', transform=t, stroke_width=4)
            + z('ellipse', '#f4f4f0', cx=cx, cy=cy + 34, rx=17, ry=5, transform=t)
            + z('path', '#f4f4f0', d=f'M{cx-15} {cy-66} L{cx+15} {cy-66} Q{cx+15} {cy-10} {cx} {cy-6} Q{cx-15} {cy-10} {cx-15} {cy-66}Z', transform=t)
            + s('path', '#ffe27a', d=f'M{cx-14.5} {cy-50} L{cx+14.5} {cy-50} Q{cx+14} {cy-12} {cx} {cy-9} Q{cx-14} {cy-12} {cx-14.5} {cy-50}Z', transform=t, stroke_width=2)
            + s('circle', '#ffffff', cx=cx - 3, cy=cy - 26, r=2.5, transform=t, stroke='none')
            + s('circle', '#ffffff', cx=cx + 4, cy=cy - 36, r=2, transform=t, stroke='none')
            + s('circle', '#ffffff', cx=cx - 2, cy=cy - 42, r=1.8, transform=t, stroke='none'))


ITEMS['champagne-toast'] = (
    flute(66, 140, 16) + flute(134, 140, -16)
    + s('path', d='M100 46 L100 34 M86 52 L78 42 M114 52 L122 42', stroke_width=3)
    + z('path', '#ffe27a', d=star_d(44, 52, 9, 4)) + z('path', '#ffe27a', d=star_d(158, 48, 8, 3.5))
    + s('circle', '#f6a6b8', cx=40, cy=96, r=4, stroke_width=2) + s('circle', '#8fc7e8', cx=162, cy=94, r=4, stroke_width=2)
)


# 19. party hats
def hat(bx1, bx2, by, tx, ty, col, deco):
    o = z('path', col, d=f'M{bx1} {by} L{tx} {ty} L{bx2} {by} Q{(bx1+bx2)/2} {by+10} {bx1} {by}Z')
    o += deco
    o += s('path', '#ffffff', d=f'M{bx1} {by} Q{(bx1+bx2)/2} {by+10} {bx2} {by}', stroke='none')
    o += s('path', d=f'M{bx1} {by} Q{(bx1+bx2)/2} {by+12} {bx2} {by}', stroke='#ffe27a', stroke_width=5)
    o += z('circle', '#ffe27a', cx=tx, cy=ty, r=9)
    return o


ITEMS['party-hats'] = (
    hat(96, 166, 168, 140, 52, '#8fc7e8',
        s('path', d='M118 96 L150 100 M110 124 L156 130 M102 152 L162 160', stroke='#ffffff', stroke_width=6)
        )
    + hat(32, 104, 172, 60, 52, '#f07a8a',
          s('circle', '#ffe27a', cx=60, cy=92, r=4.5, stroke_width=2) + s('circle', '#ffffff', cx=50, cy=120, r=4.5, stroke_width=2)
          + s('circle', '#8fc7e8', cx=74, cy=124, r=4.5, stroke_width=2) + s('circle', '#ffe27a', cx=62, cy=148, r=4.5, stroke_width=2)
          + s('circle', '#ffffff', cx=86, cy=156, r=4.5, stroke_width=2) + s('circle', '#8fc7e8', cx=42, cy=154, r=4.5, stroke_width=2))
    + s('rect', '#9ccf7a', x=94, y=40, width=8, height=5, rx=1, transform='rotate(30 98 42)', stroke_width=1.5)
    + s('rect', '#ffc94d', x=30, y=34, width=8, height=5, rx=1, transform='rotate(-20 34 36)', stroke_width=1.5)
    + s('rect', '#a98bd0', x=170, y=96, width=8, height=5, rx=1, transform='rotate(40 174 98)', stroke_width=1.5)
    + s('rect', '#f6a6b8', x=166, y=40, width=8, height=5, rx=1, transform='rotate(-30 170 42)', stroke_width=1.5)
    + dot(98, 76, 3, '#f07a8a') + dot(24, 100, 3, '#8fc7e8') + dot(170, 150, 3, '#ffc94d')
)


# 20. bunting flags
def bunting(x1, x2, y, sag, cols, n):
    o = s('path', d=f'M{x1} {y} Q{(x1+x2)/2} {y+2*sag} {x2} {y}', stroke_width=3)
    flags = ''
    def pt(t):
        cx, cy = (x1 + x2) / 2, y + 2 * sag
        return ((1-t)**2*x1 + 2*(1-t)*t*cx + t*t*x2, (1-t)**2*y + 2*(1-t)*t*cy + t*t*y)
    w = 1 / n
    for i in range(n):
        ta, tb = (i + 0.12) * w, (i + 0.88) * w
        (ax, ay), (bx, by) = pt(ta), pt(tb)
        mx, my = (ax + bx) / 2, (ay + by) / 2
        flags += z('path', cols[i % len(cols)], d=f'M{ax:.1f} {ay:.1f} L{bx:.1f} {by:.1f} L{mx:.1f} {my+30:.1f}Z')
    return flags + o


ITEMS['bunting'] = (
    bunting(28, 172, 40, 18, ['#f07a8a', '#ffe27a', '#8fc7e8', '#9ccf7a', '#a98bd0'], 6)
    + bunting(28, 172, 112, 16, ['#8fc7e8', '#f5b971', '#f6a6b8', '#7cc4a0', '#ffe27a'], 6)
    + dot(28, 40, 4) + dot(172, 40, 4) + dot(28, 112, 4) + dot(172, 112, 4)
)
