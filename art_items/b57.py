from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186, w=36):
    return z('path', fill, d=f'M{cx-w} {bottom} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bottom}Z')


def hand(x, y, r=8):
    return z('circle', SK, cx=x, cy=y, r=r)


def hair(cx, cy, c):
    return s('path', c, d=f'M{cx-34} {cy-2} Q{cx-32} {cy-36} {cx} {cy-35} Q{cx+32} {cy-36} {cx+34} {cy-2} Q{cx+20} {cy-18} {cx} {cy-17} Q{cx-20} {cy-18} {cx-34} {cy-2}Z')


def calm_face(cx, cy, hr, mouth='smile'):
    """目を閉じた顔（眠り・リラックス）"""
    o = z('circle', SK, cx=cx, cy=cy, r=34) + hair(cx, cy, hr)
    o += s('path', d=f'M{cx-18} {cy+2} Q{cx-12} {cy+7} {cx-6} {cy+2} M{cx+6} {cy+2} Q{cx+12} {cy+7} {cx+18} {cy+2}', stroke_width=2.5)
    o += cheeks(cx - 20, cx + 20, cy + 13)
    if mouth == 'smile':
        o += s('path', d=f'M{cx-6} {cy+16} Q{cx} {cy+21} {cx+6} {cy+16}')
    else:
        o += s('ellipse', '#c0504d', cx=cx, cy=cy + 18, rx=3, ry=2.5, stroke_width=2)
    return o


def drop(x, y, r=6, c='#8fc7e8', sw=2.5):
    return s('path', c, d=f'M{x} {y-2.2*r} Q{x+r} {y-0.6*r} {x+r} {y} A{r} {r} 0 0 1 {x-r} {y} Q{x-r} {y-0.6*r} {x} {y-2.2*r}Z', stroke_width=sw)


def zdrop(x, y, r, c):
    return z('path', c, d=f'M{x} {y-2.2*r} Q{x+r} {y-0.6*r} {x+r} {y} A{r} {r} 0 0 1 {x-r} {y} Q{x-r} {y-0.6*r} {x} {y-2.2*r}Z')


def sparkle(x, y, r=7, c='#ffe27a'):
    return s('path', c, d=f'M{x} {y-r} Q{x+1.5} {y-1.5} {x+r} {y} Q{x+1.5} {y+1.5} {x} {y+r} Q{x-1.5} {y+1.5} {x-r} {y} Q{x-1.5} {y-1.5} {x} {y-r}Z', stroke_width=2)


def heart(cx, cy, k=1.0):
    def p(x, y):
        return f'{cx + x*k:.1f} {cy + y*k:.1f}'
    return f'M{p(0,14)} C{p(-12,4)} {p(-20,-4)} {p(-14,-12)} C{p(-8,-20)} {p(0,-15)} {p(0,-8)} C{p(0,-15)} {p(8,-20)} {p(14,-12)} C{p(20,-4)} {p(12,4)} {p(0,14)}Z'


# 1. eye-drops
ITEMS['eye-drops'] = (
    z('path', '#ffffff', d='M40 150 Q100 104 160 150 Q100 192 40 150Z')
    + z('circle', '#8fc7e8', cx=100, cy=148, r=19)
    + dot(100, 148, 8) + dot(106, 142, 3, '#ffffff')
    + s('path', d='M58 134 L52 124 M80 122 L77 111 M100 118 L100 107 M120 122 L123 111 M142 134 L148 124', stroke_width=2.5)
    + z('path', '#f4f4f0', d='M78 26 L122 26 Q126 26 126 32 L126 64 L74 64 L74 32 Q74 26 78 26Z')
    + s('rect', '#8fc7e8', x=74, y=36, width=52, height=18, stroke_width=2.5)
    + z('path', '#8fc7e8', d='M80 64 L120 64 L112 78 L88 78Z')
    + z('path', '#8fc7e8', d='M94 78 L106 78 L102 92 L98 92Z')
    + zdrop(100, 106, 5, '#8fc7e8')
    + dot(92, 44, 2.5) + dot(108, 44, 2.5) + s('path', d='M96 48 Q100 51 104 48', stroke_width=2)
)

# 2. eyeglasses
ITEMS['eyeglasses'] = (
    s('path', d='M34 92 L26 70 Q24 62 32 62', stroke_width=5)
    + s('path', d='M166 92 L174 70 Q176 62 168 62', stroke_width=5)
    + z('circle', '#8fb3e0', cx=64, cy=108, r=34)
    + z('circle', '#8fb3e0', cx=136, cy=108, r=34)
    + s('circle', '#d8eef8', cx=64, cy=108, r=26, stroke_width=2.5)
    + s('circle', '#d8eef8', cx=136, cy=108, r=26, stroke_width=2.5)
    + s('path', d='M98 100 Q100 90 102 100', stroke_width=5)
    + s('path', d='M50 98 Q54 90 62 88 M122 98 Q126 90 134 88', stroke='#ffffff', stroke_width=4)
    + s('path', d='M52 106 L56 102 M124 106 L128 102', stroke='#ffffff', stroke_width=4)
    + sparkle(160, 52, 9) + sparkle(42, 156, 7)
)

# 3. broken-leg
ITEMS['broken-leg'] = (
    s('path', d='M58 118 L48 184 M142 118 L152 184', stroke_width=7)
    + s('path', d='M58 118 L48 184 M142 118 L152 184', stroke='#c9d3db', stroke_width=3)
    + s('path', d='M48 114 L70 118 M130 118 L152 114', stroke_width=6)
    + s('rect', '#5b6b7a', x=78, y=136, width=18, height=40, stroke_width=3)
    + z('ellipse', '#8b6b4f', cx=86, cy=178, rx=12, ry=6)
    + z('path', '#ffffff', d='M104 132 L130 132 L130 156 Q140 158 140 166 Q140 172 132 172 L110 172 Q104 172 104 166Z')
    + s('path', d='M106 144 L128 144 M106 156 L126 156', stroke='#b9a99c', stroke_width=2)
    + body('#7cc4b0', top=104, bottom=146, w=34)
    + face(100, 70, SK, '#5a4033', 'o')
    + drop(142, 52, 5)
    + hand(56, 132) + hand(144, 132)
)

# 4. x-ray
ITEMS['x-ray'] = (
    z('rect', '#5b6b7a', x=34, y=42, width=132, height=118, rx=8)
    + s('rect', '#7a8a99', x=44, y=52, width=112, height=98, rx=4, stroke_width=2)
    + z('rect', '#c9d3db', x=84, y=32, width=32, height=14, rx=3)
    + z('path', '#f4f4f0', d='M70 90 L130 90 A14 14 0 1 1 152 96 Q148 101 152 106 A14 14 0 1 1 130 112 L70 112 A14 14 0 1 1 48 106 Q52 101 48 96 A14 14 0 1 1 70 90Z')
    + dot(90, 100, 3) + dot(110, 100, 3) + cheeks(82, 118, 106, 5, 3)
    + s('path', d='M96 106 Q100 109 104 106', stroke_width=2)
    + s('path', d='M80 172 L120 172 M100 160 L100 172', stroke_width=4)
)

# 5. blood-pressure
ITEMS['blood-pressure'] = (
    s('path', d='M56 144 Q56 120 80 126 Q104 132 110 122', stroke='#5b6b7a', stroke_width=5)
    + z('rect', '#f4f4f0', x=94, y=40, width=78, height=86, rx=10)
    + s('rect', '#d8eef8', x=104, y=50, width=58, height=38, rx=4, stroke_width=2.5)
    + s('path', '#f07a8a', d=heart(120, 68, 0.6), stroke_width=2)
    + s('path', d='M132 64 L154 64 M132 74 L148 74', stroke_width=3)
    + z('circle', '#8fc7e8', cx=118, cy=106, r=8) + z('circle', '#9ccf7a', cx=146, cy=106, r=8)
    + z('rect', SK, x=24, y=150, width=96, height=28, rx=14)
    + hand(126, 164, 11)
    + z('rect', '#8fb3e0', x=38, y=142, width=40, height=44, rx=6)
    + s('path', d='M46 150 L70 150 M46 178 L70 178', stroke_width=2)
)

# 6. heart-health
ITEMS['heart-health'] = (
    z('path', '#f07a8a', d='M100 170 C62 144 34 116 42 82 C50 50 88 48 100 74 C112 48 150 50 158 82 C166 116 138 144 100 170Z')
    + s('path', d='M64 70 Q70 62 80 62', stroke='#ffffff', stroke_width=4)
    + dot(86, 96) + dot(114, 96) + cheeks(72, 128, 108)
    + s('path', d='M94 108 Q100 113 106 108')
    + s('path', d='M24 134 L62 134 L72 116 L84 152 L96 124 L104 134 L176 134', stroke_width=4)
)

# 7. lungs
L_LOBE = 'M92 76 Q62 62 48 100 Q38 150 58 168 Q80 176 92 158Z'
R_LOBE = 'M108 76 Q138 62 152 100 Q162 150 142 168 Q120 176 108 158Z'
ITEMS['lungs'] = (
    z('path', '#f6a6b8', d=L_LOBE) + z('path', '#f6a6b8', d=R_LOBE)
    + z('rect', '#f4f4f0', x=94, y=26, width=12, height=56, rx=5)
    + s('path', d='M94 38 L106 38 M94 50 L106 50 M94 62 L106 62', stroke_width=2)
    + s('path', d='M100 80 L82 100 M100 80 L118 100', stroke_width=5)
    + dot(64, 120, 3) + dot(80, 120, 3) + cheeks(58, 86, 128, 5, 3)
    + s('path', d='M68 128 Q72 132 76 128', stroke_width=2.5)
    + dot(120, 120, 3) + dot(136, 120, 3) + cheeks(114, 142, 128, 5, 3)
    + s('path', d='M124 128 Q128 132 132 128', stroke_width=2.5)
)

# 8. brain
ITEMS['brain'] = (
    z('path', '#f6a6b8', d='M100 50 Q82 34 64 48 Q40 46 40 72 Q24 92 40 112 Q38 138 64 140 Q78 158 100 148 Q122 158 136 140 Q162 138 160 112 Q176 92 160 72 Q160 46 136 48 Q118 34 100 50Z')
    + s('path', d='M100 50 Q94 62 100 72 Q106 82 100 92', stroke_width=2.5)
    + s('path', d='M62 62 Q74 64 72 76 M140 64 Q126 66 128 78 M50 92 Q60 88 64 96 M150 92 Q140 88 136 96', stroke_width=2.5)
    + dot(86, 110) + dot(114, 110) + cheeks(72, 128, 121, 6, 3.5)
    + s('path', d='M94 120 Q100 126 106 120')
    + sparkle(160, 30, 9) + sparkle(36, 34, 7) + sparkle(178, 152, 6)
)

# 9. tooth
ITEMS['tooth'] = (
    z('path', '#ffffff', d='M58 64 Q58 38 82 40 Q92 42 100 48 Q108 42 118 40 Q142 38 142 64 Q144 96 134 122 Q128 172 116 172 Q106 170 104 144 Q100 132 96 144 Q94 170 84 172 Q72 172 66 122 Q56 96 58 64Z')
    + s('path', d='M70 60 Q72 50 82 50', stroke='#8fc7e8', stroke_width=4)
    + dot(88, 94) + dot(112, 94) + cheeks(74, 126, 106, 6, 3.5)
    + s('path', d='M94 106 Q100 112 106 106')
    + sparkle(160, 50, 10, '#8fc7e8') + sparkle(40, 140, 8, '#8fc7e8') + sparkle(166, 126, 6, '#ffe27a')
)

# 10. weight-scale
ITEMS['weight-scale'] = (
    z('rect', '#8fc7e8', x=38, y=50, width=124, height=124, rx=22)
    + z('path', '#ffffff', d='M74 88 Q74 62 100 62 Q126 62 126 88Z')
    + s('path', d='M80 84 L84 80 M90 74 L92 70 M100 72 L100 67 M110 74 L108 70 M120 84 L116 80', stroke_width=2)
    + s('path', d='M100 88 L112 72', stroke='#e04b5a', stroke_width=3)
    + dot(100, 88, 3)
    + z('ellipse', '#c9d3db', cx=76, cy=134, rx=17, ry=26)
    + z('ellipse', '#c9d3db', cx=124, cy=134, rx=17, ry=26)
)

# 11. height-measure
ITEMS['height-measure'] = (
    z('rect', '#f5d58a', x=132, y=26, width=24, height=158, rx=3)
    + s('path', d='M132 44 L144 44 M132 58 L140 58 M132 72 L144 72 M132 86 L140 86 M132 100 L144 100 M132 114 L140 114 M132 128 L144 128 M132 142 L140 142 M132 156 L144 156 M132 170 L140 170', stroke_width=2)
    + body('#f6a6b8', cx=88, top=120, bottom=186, w=34)
    + face(88, 82, SK, '#c9a36b', 'smile')
    + z('rect', '#e8735a', x=72, y=38, width=90, height=9, rx=3)
    + s('path', d='M40 60 L40 104 M32 68 L40 58 L48 68', stroke_width=3)
)

# 12. healthy-plate
ITEMS['healthy-plate'] = (
    z('circle', '#f4f4f0', cx=100, cy=104, r=70)
    + s('circle', cx=100, cy=104, r=56, stroke='#c9d3db', stroke_width=2.5)
    + s('path', d='M78 102 L74 84 M78 102 L82 84', stroke_width=3)
    + z('path', '#7cc4a0', d='M60 84 Q58 66 72 66 Q76 54 88 62 Q100 62 96 76 Q100 90 86 88 Q78 94 60 84Z')
    + z('path', '#f6a6b8', d='M112 56 Q140 56 146 82 Q148 94 136 94 L112 94 Q104 76 112 56Z')
    + s('path', d='M120 64 Q130 72 128 90 M132 64 Q140 74 140 88', stroke='#ffffff', stroke_width=3)
    + z('path', '#ffffff', d='M82 108 Q90 110 98 128 Q102 140 92 142 L64 142 Q54 140 58 128 Q68 108 82 108Z')
    + s('rect', '#5b6b7a', x=68, y=128, width=24, height=14, stroke_width=2.5)
    + z('circle', '#e04b5a', cx=124, cy=126, r=11) + z('circle', '#e04b5a', cx=142, cy=114, r=9)
    + s('path', d='M122 116 L126 112 M140 106 L144 102', stroke='#7cc4a0', stroke_width=3)
    + z('path', '#ffc94d', d='M108 146 Q116 134 130 146 Q120 152 108 146Z')
)

# 13. good-sleep
ITEMS['good-sleep'] = (
    z('rect', '#d9a66b', x=26, y=110, width=12, height=72, rx=3)
    + z('rect', '#d9a66b', x=162, y=140, width=12, height=42, rx=3)
    + z('rect', '#f4f4f0', x=34, y=118, width=58, height=26, rx=12)
    + calm_face(70, 112, '#5a4033', 'o')
    + z('path', '#8fb3e0', d='M58 142 Q60 128 84 130 L168 130 Q174 130 174 138 L174 170 L52 170 Q48 156 58 142Z')
    + s('path', d='M86 146 L168 146', stroke='#ffffff', stroke_width=3)
    + z('path', '#ffe27a', d='M146 26 Q124 34 126 56 Q130 76 152 78 Q136 66 138 50 Q138 34 146 26Z')
    + sparkle(172, 44, 8) + sparkle(110, 34, 6) + sparkle(168, 92, 5)
)

# 14. mental-health
ITEMS['mental-health'] = (
    s('circle', cx=100, cy=112, r=76, stroke='#9ccf7a', stroke_width=2.5, stroke_dasharray='4 9')
    + z('ellipse', '#a98bd0', cx=100, cy=168, rx=54, ry=14)
    + body('#a98bd0', top=112, bottom=170, w=38)
    + calm_face(100, 76, '#2b2220')
    + z('path', '#f07a8a', d=heart(100, 140, 1.1))
    + hand(84, 150) + hand(116, 150)
    + z('path', '#9ccf7a', d='M38 66 Q30 50 44 44 Q52 58 38 66Z')
    + z('path', '#9ccf7a', d='M158 62 Q162 46 176 50 Q170 66 158 62Z')
    + sparkle(36, 120, 6, '#f6a6b8') + sparkle(166, 120, 6, '#f6a6b8')
)

# 15. back-pain
ITEMS['back-pain'] = (
    z('path', '#8fb3e0', d='M62 186 Q60 128 96 120 Q132 124 132 186Z')
    + z('circle', SK, cx=92, cy=80, r=34) + hair(92, 80, '#2b2220')
    + s('path', d='M74 78 L82 82 L74 86 M110 78 L102 82 L110 86', stroke_width=2.5)
    + cheeks(72, 112, 95)
    + s('path', d='M84 100 Q88 96 92 100 Q96 104 100 100', stroke_width=2.5)
    + drop(128, 54, 5)
    + hand(128, 160, 9)
    + s('path', d='M152 150 L164 144 L158 156 L172 152 M150 172 L162 176 M148 132 L156 122', stroke='#e04b5a', stroke_width=3)
)

# 16. eye-strain
ITEMS['eye-strain'] = (
    body('#7cc4b0', top=118, bottom=170, w=40)
    + z('circle', SK, cx=100, cy=80, r=34) + hair(100, 80, '#5a4033')
    + s('path', d='M80 82 L96 82 M104 82 L120 82', stroke_width=3)
    + s('path', d='M82 82 Q88 88 94 82 M106 82 Q112 88 118 82', stroke_width=2)
    + s('path', d='M82 92 Q88 95 94 92 M106 92 Q112 95 118 92', stroke='#a98bd0', stroke_width=2)
    + cheeks(78, 122, 98, 6, 3)
    + s('path', d='M94 104 Q100 101 106 104', stroke_width=2.5)
    + s('path', d='M66 44 Q72 38 66 32 M134 34 Q128 28 134 22 M146 50 Q152 44 146 38', stroke='#a98bd0', stroke_width=2.5)
    + z('path', '#c9d3db', d='M48 122 L152 122 Q156 122 156 126 L156 168 L44 168 L44 126 Q44 122 48 122Z')
    + dot(100, 145, 6, '#f4f4f0')
    + z('rect', '#b9a99c', x=34, y=168, width=132, height=10, rx=4)
)

# 17. heatstroke
SUN = (z('circle', '#ffc94d', cx=46, cy=46, r=20)
       + s('path', d='M46 14 L46 6 M70 22 L76 16 M78 46 L86 46 M22 22 L16 16 M14 46 L6 46 M70 70 L76 76 M22 70 L16 76', stroke_width=3))
ITEMS['heatstroke'] = (
    SUN
    + body('#f5d58a', cx=110, top=136, bottom=186, w=36)
    + z('circle', SK, cx=110, cy=98, r=34) + hair(110, 98, '#2b2220')
    + s('path', d='M90 100 Q94 94 98 100 Q94 106 90 100 M122 100 Q126 94 130 100 Q126 106 122 100', stroke_width=2)
    + s('ellipse', '#f07a8a', cx=88, cy=112, rx=9, ry=5, stroke='none')
    + s('ellipse', '#f07a8a', cx=132, cy=112, rx=9, ry=5, stroke='none')
    + s('path', d='M102 118 Q106 114 110 118 Q114 122 118 118', stroke_width=2.5)
    + drop(80, 74, 5) + drop(146, 82, 5) + drop(152, 118, 4)
    + s('path', d='M158 40 Q164 46 158 52 Q152 58 158 64 M176 52 Q182 58 176 64 Q170 70 176 76', stroke='#e8735a', stroke_width=3)
    + s('path', d='M36 170 Q42 164 48 170 Q54 176 60 170', stroke='#e8735a', stroke_width=3)
)

# 18. sunscreen
ITEMS['sunscreen'] = (
    z('rect', '#ffc94d', x=82, y=30, width=36, height=24, rx=5)
    + z('rect', '#ffffff', x=68, y=52, width=64, height=124, rx=16)
    + s('rect', '#8fc7e8', x=68, y=118, width=64, height=34, stroke_width=2.5)
    + s('circle', '#ffc94d', cx=100, cy=84, r=11, stroke_width=2.5)
    + s('path', d='M100 66 L100 61 M100 102 L100 107 M82 84 L77 84 M118 84 L123 84 M87 71 L84 68 M113 71 L116 68 M87 97 L84 100 M113 97 L116 100', stroke_width=2.5)
    + dot(92, 132, 3) + dot(108, 132, 3) + cheeks(84, 116, 140, 5, 3)
    + s('path', d='M96 140 Q100 144 104 140', stroke_width=2.5)
    + z('path', '#ffffff', d='M138 178 Q136 164 150 164 Q148 154 160 154 Q170 158 164 166 Q176 168 172 178Z')
    + z('circle', '#ffc94d', cx=164, cy=44, r=12)
    + s('path', d='M164 22 L164 26 M164 62 L164 66 M142 44 L146 44 M182 44 L186 44', stroke_width=2.5)
)

# 19. vitamins
ITEMS['vitamins'] = (
    z('rect', '#d9a66b', x=50, y=62, width=64, height=114, rx=12)
    + z('rect', '#ffffff', x=54, y=40, width=56, height=26, rx=5)
    + s('path', d='M62 46 L62 60 M72 46 L72 60 M82 46 L82 60 M92 46 L92 60 M102 46 L102 60', stroke_width=2)
    + s('rect', '#ffffff', x=56, y=94, width=52, height=50, rx=4, stroke_width=2.5)
    + s('path', '#ffc94d', d='M70 128 L84 114 A7 7 0 0 1 94 124 L80 138Z', stroke_width=2)
    + s('path', '#e8735a', d='M70 128 A7 7 0 0 0 80 138Z', stroke_width=2)
    + s('path', '#e8735a', d='M70 128 L80 138 L77 141 A7 7 0 0 1 67 131Z', stroke_width=2)
    + z('circle', '#f5b971', cx=148, cy=150, r=24)
    + s('path', d='M148 126 Q150 118 156 114', stroke_width=3)
    + z('path', '#9ccf7a', d='M150 124 Q162 110 172 120 Q160 130 150 124Z')
    + dot(140, 150, 3) + dot(156, 150, 3) + cheeks(134, 162, 158, 5, 3)
    + s('path', d='M144 158 Q148 162 152 158', stroke_width=2.5)
    + z('rect', '#ffc94d', x=118, y=82, width=30, height=14, rx=7)
    + s('path', d='M133 82 L133 96', stroke_width=2)
    + z('circle', '#e8735a', cx=140, cy=110, r=7)
)

# 20. hydration
ITEMS['hydration'] = (
    body('#8fc7e8', cx=90, top=128, bottom=186, w=36)
    + face(88, 90, SK, '#c9a36b', 'smile')
    + '<g transform="rotate(-28 96 104)">'
    + z('path', '#d8eef8', d='M92 96 L124 96 L119 150 L97 150Z')
    + s('path', '#8fc7e8', d='M94 116 L122 116 L119 150 L97 150Z', stroke_width=2.5)
    + s('path', d='M102 124 L102 142', stroke='#ffffff', stroke_width=3)
    + '</g>'
    + hand(128, 140, 9)
    + zdrop(166, 60, 8, '#8fc7e8') + zdrop(40, 56, 6, '#8fc7e8')
    + sparkle(160, 108, 6, '#8fc7e8')
)
