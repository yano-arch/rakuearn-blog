from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def limb(d, color, w=10):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=w - 5)


def mini_face(cx, cy, sp=10, ch=8):
    return (dot(cx - sp, cy, 3) + dot(cx + sp, cy, 3) + cheeks(cx - sp - ch, cx + sp + ch, cy + 8, 5, 3)
            + s('path', d=f'M{cx-4} {cy+7} Q{cx} {cy+11} {cx+4} {cy+7}', stroke_width=2.5))


def note(x, y, c='#a98bd0'):
    return (s('path', d=f'M{x+7} {y} L{x+7} {y-20} L{x+15} {y-16}', stroke_width=2.5)
            + s('ellipse', c, cx=x + 2, cy=y, rx=6, ry=4.5, stroke_width=2.5))


def sparkle(x, y, r=8, c='#ffe27a'):
    return s('path', c, d=f'M{x} {y-r} Q{x+2} {y-2} {x+r} {y} Q{x+2} {y+2} {x} {y+r} Q{x-2} {y+2} {x-r} {y} Q{x-2} {y-2} {x} {y-r}Z', stroke_width=2)


# 1. origami crane
ITEMS['origami-crane'] = (
    z('path', '#f07a8a', d='M78 118 L58 30 L112 108Z')
    + z('path', '#f07a8a', d='M96 108 L160 40 L128 120Z')
    + z('path', '#f6a6b8', d='M58 124 L100 104 L142 124 L100 150Z')
    + z('path', '#f6a6b8', d='M72 122 L44 74 L36 78 L48 72 L62 126Z')
    + z('path', '#f6a6b8', d='M132 124 L172 86 L150 128Z')
    + s('path', d='M100 104 L100 150 M58 124 L142 124', stroke_width=2)
    + s('path', d='M30 178 Q100 168 170 178', stroke_width=2.5)
)

# 2. calligraphy
ITEMS['calligraphy'] = (
    z('rect', '#ffffff', x=34, y=96, width=104, height=80, rx=3)
    + s('path', OUT, d='M52 126 Q70 108 92 118 Q108 126 104 142 Q100 158 118 154 Q112 164 96 158 Q86 150 92 132 Q88 124 74 124 Q62 126 52 126Z', stroke_width=2)
    + z('rect', '#5b6b7a', x=146, y=150, width=30, height=26, rx=5)
    + s('ellipse', '#2b2220', cx=161, cy=158, rx=9, ry=4, stroke_width=2)
    + z('path', '#d9a66b', d='M168 30 L176 36 L132 104 L124 98Z')
    + z('path', '#2b2220', d='M124 98 L132 104 Q126 120 114 128 Q116 112 124 98Z')
    + s('path', d='M128 92 L137 98', stroke_width=3)
)

# 3. flower arranging
ITEMS['flower-arranging'] = (
    s('path', d='M100 128 L100 74 M100 128 Q86 96 66 70 M100 128 Q116 98 140 76', stroke='#7cc4a0', stroke_width=4)
    + z('path', '#9ccf7a', d='M100 112 Q78 106 74 90 Q94 92 100 112Z')
    + z('path', '#9ccf7a', d='M104 106 Q124 100 128 86 Q108 88 104 106Z')
    + ''.join(z('circle', '#f6a6b8', cx=66 + dx, cy=64 + dy, r=8) for dx, dy in ((-9, 0), (9, 0), (0, -9), (0, 9)))
    + dot(66, 64, 5, '#ffc94d')
    + ''.join(z('circle', '#ffe27a', cx=100 + dx, cy=60 + dy, r=9) for dx, dy in ((-10, 0), (10, 0), (0, -10), (0, 10)))
    + dot(100, 60, 6, '#e8735a')
    + ''.join(z('circle', '#f07a8a', cx=142 + dx, cy=70 + dy, r=8) for dx, dy in ((-9, 0), (9, 0), (0, -9), (0, 9)))
    + dot(142, 70, 5, '#ffc94d')
    + z('path', '#8fb3e0', d='M70 128 L130 128 Q140 128 136 140 L128 176 L72 176 L64 140 Q60 128 70 128Z')
    + dot(88, 150) + dot(112, 150) + cheeks(80, 120, 159, 5, 3) + s('path', d='M96 158 Q100 162 104 158', stroke_width=2.5)
    + s('path', d='M40 180 L160 180', stroke_width=2.5)
)

# 4. baking cookies
ck = lambda x, y: (z('circle', '#d9a66b', cx=x, cy=y, r=17) + dot(x - 6, y - 5, 2.6, '#8b6b4f')
                   + dot(x + 6, y + 1, 2.6, '#8b6b4f') + dot(x - 2, y + 8, 2.6, '#8b6b4f'))
ITEMS['baking'] = (
    z('rect', '#c9d3db', x=30, y=104, width=140, height=74, rx=6)
    + s('rect', x=38, y=112, width=124, height=58, rx=4, stroke_width=2)
    + ck(62, 128) + ck(138, 128) + ck(62, 156) + ck(138, 156)
    + z('circle', '#d9a66b', cx=100, cy=142, r=21) + mini_face(100, 140, 8, 6)
    + z('rect', '#f6e0c4', x=50, y=50, width=100, height=26, rx=13)
    + z('rect', '#d9a66b', x=26, y=56, width=26, height=14, rx=6)
    + z('rect', '#d9a66b', x=148, y=56, width=26, height=14, rx=6)
    + s('path', d='M100 24 Q94 32 100 38 M116 26 Q110 34 116 40 M84 26 Q78 34 84 40', stroke_width=2.5)
)

# 5. pour-over coffee
ITEMS['coffee-dripper'] = (
    z('path', '#8fc7e8', d='M78 120 L122 120 Q142 140 138 168 Q134 180 120 180 L80 180 Q66 180 62 168 Q58 140 78 120Z')
    + s('path', '#8b6b4f', d='M64 152 L136 152 Q138 168 134 172 Q130 178 120 178 L80 178 Q70 178 66 172 Q62 166 64 152Z', stroke_width=2)
    + z('path', '#8fc7e8', d='M138 136 Q156 140 150 160 Q146 168 136 166')
    + z('rect', '#ffffff', x=64, y=112, width=72, height=10, rx=4)
    + z('path', '#ffffff', d='M62 76 L138 76 L114 112 L86 112Z')
    + s('path', d='M80 86 L91 104 M120 86 L109 104', stroke_width=2)
    + s('path', d='M100 114 L100 140', stroke='#8b6b4f', stroke_width=4)
    + z('path', '#c9d3db', d='M30 40 Q30 28 50 28 Q70 28 70 40 L72 66 L28 66Z')
    + s('path', d='M68 52 Q90 52 96 64', stroke_width=7) + s('path', d='M68 52 Q90 52 96 64', stroke='#c9d3db', stroke_width=2)
    + s('path', d='M32 38 Q18 46 30 58', stroke_width=3) + s('rect', '#5b6b7a', x=44, y=22, width=12, height=6, rx=2, stroke_width=2)
    + s('path', d='M97 66 Q98 70 97 76', stroke='#8b6b4f', stroke_width=2.5)
)

# 6. tea ceremony
ITEMS['tea-ceremony'] = (
    z('ellipse', '#e8735a', cx=100, cy=170, rx=68, ry=10)
    + z('path', '#5b6b7a', d='M44 120 L136 120 Q134 166 90 168 Q46 166 44 120Z')
    + s('ellipse', '#9ccf7a', cx=90, cy=120, rx=46, ry=10)
    + s('path', d='M74 120 Q84 116 96 122', stroke='#7cc4a0', stroke_width=2)
    + dot(76, 144) + dot(104, 144) + cheeks(66, 114, 153, 5, 3) + s('path', d='M86 152 Q90 156 94 152', stroke_width=2.5)
    + z('path', '#f5d58a', d='M146 108 Q140 140 152 156 L172 156 Q184 140 178 108Z')
    + s('path', d='M152 112 Q150 136 158 154 M162 110 L162 154 M172 112 Q174 136 166 154', stroke_width=2)
    + z('rect', '#d9a66b', x=154, y=154, width=16, height=14, rx=3)
    + s('path', d='M88 92 Q82 80 90 70 M104 92 Q98 80 106 70', stroke='#b9a99c', stroke_width=2.5)
)

# 7. model train
ITEMS['model-train'] = (
    s('path', d='M20 170 L180 170 M20 178 L180 178', stroke_width=2.5)
    + ''.join(s('rect', '#9a6a3f', x=x, y=166, width=8, height=16, rx=1, stroke_width=2) for x in range(24, 180, 18))
    + z('rect', '#8fb3e0', x=18, y=114, width=44, height=40, rx=4)
    + s('rect', '#ffffff', x=26, y=122, width=12, height=12, rx=2, stroke_width=2.5) + s('rect', '#ffffff', x=42, y=122, width=12, height=12, rx=2, stroke_width=2.5)
    + s('path', d='M62 146 L72 146', stroke_width=4)
    + z('rect', '#e8735a', x=72, y=116, width=72, height=38, rx=6)
    + z('rect', '#e8735a', x=124, y=88, width=36, height=66, rx=4)
    + z('rect', '#5b6b7a', x=118, y=80, width=48, height=10, rx=3)
    + s('rect', '#ffffff', x=132, y=98, width=20, height=16, rx=2, stroke_width=2.5)
    + z('rect', '#5b6b7a', x=84, y=96, width=14, height=22, rx=2)
    + z('rect', '#ffc94d', x=60, y=122, width=14, height=14, rx=4)
    + ''.join(z('circle', '#5b6b7a', cx=x, cy=158, r=10) + dot(x, 158, 3, '#c9d3db') for x in (88, 114, 140))
    + ''.join(z('circle', '#5b6b7a', cx=x, cy=158, r=8) for x in (30, 50))
    + z('circle', '#ffffff', cx=96, cy=74, r=8) + z('circle', '#ffffff', cx=84, cy=60, r=11) + z('circle', '#ffffff', cx=66, cy=46, r=14)
    + dot(94, 132, 3) + dot(110, 132, 3) + cheeks(88, 116, 140, 5, 3)
)

# 8. kite
ITEMS['kite'] = (
    z('ellipse', '#ffffff', cx=48, cy=140, rx=22, ry=9) + z('ellipse', '#ffffff', cx=160, cy=160, rx=18, ry=8)
    + s('path', d='M100 132 Q86 156 104 170 Q120 182 108 194', stroke_width=2.5)
    + z('path', '#f07a8a', d='M96 146 L104 152 L96 158Z') + z('path', '#f07a8a', d='M110 166 L104 174 L112 178Z')
    + s('path', d='M120 92 Q150 120 170 186', stroke_width=2)
    + z('path', '#ffc94d', d='M100 24 L144 74 L100 132 L56 74Z')
    + s('path', '#f07a8a', d='M100 24 L144 74 L100 74Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M100 74 L56 74 L100 132Z', stroke_width=2.5)
    + dot(88, 82) + dot(112, 82) + cheeks(80, 120, 92, 5, 3) + s('path', d='M95 92 Q100 97 105 92', stroke_width=2.5)
)

# 9. telescope
ITEMS['telescope'] = (
    s('path', d='M96 112 L64 180 M104 112 L136 180 M100 112 L100 180', stroke_width=5)
    + s('path', d='M96 112 L64 180 M104 112 L136 180 M100 112 L100 180', stroke='#9a6a3f', stroke_width=1)
    + z('path', '#8fb3e0', d='M56 128 L132 70 L146 88 L70 146Z')
    + z('path', '#5b6b7a', d='M128 64 L152 46 L170 70 L146 88Z')
    + z('path', '#5b6b7a', d='M50 132 L60 124 L74 142 L64 150Z')
    + s('circle', '#c9d3db', cx=100, cy=108, r=7, stroke_width=2.5)
    + z('path', '#ffe27a', d='M60 30 A22 22 0 1 0 84 62 A18 18 0 1 1 60 30Z')
    + sparkle(150, 120, 8) + sparkle(176, 30, 7) + sparkle(110, 34, 6) + sparkle(30, 92, 6)
)

# 10. woodworking tools
ITEMS['woodworking'] = (
    z('rect', '#d9a66b', x=26, y=140, width=148, height=30, rx=3)
    + s('path', d='M40 150 Q70 146 100 152 Q130 158 160 152 M50 162 Q80 158 120 163', stroke='#9a6a3f', stroke_width=2)
    + z('path', '#c9d3db', d='M78 112 L168 52 L176 64 L96 128Z')
    + s('path', d='M96 128 L100 120 L104 122 L108 114 L112 116 L116 108 L120 110 L124 102 L128 104 L132 96 L136 98 L140 90 L144 92 L148 84 L152 86 L156 78 L160 80 L164 72 L168 74 L172 66', stroke_width=1.5)
    + z('path', '#e8735a', d='M56 100 Q66 88 80 98 L96 128 Q82 138 70 130Z')
    + s('ellipse', '#fbf6ee', cx=74, cy=113, rx=6, ry=9, stroke_width=2.5)
    + z('rect', '#9a6a3f', x=28, y=56, width=14, height=72, rx=5)
    + z('rect', '#5b6b7a', x=16, y=38, width=50, height=20, rx=4)
    + s('path', d='M66 42 Q76 44 76 52 L66 54', stroke_width=2.5)
)

# 11. ballerina
ITEMS['ballet'] = (
    limb('M92 140 L84 180', SK) + limb('M108 140 L130 172', SK)
    + z('ellipse', '#f6a6b8', cx=82, cy=182, rx=7, ry=4) + z('ellipse', '#f6a6b8', cx=134, cy=174, rx=7, ry=4)
    + limb('M84 110 Q58 96 46 66', SK) + limb('M116 110 Q142 96 154 66', SK)
    + z('circle', SK, cx=46, cy=62, r=7) + z('circle', SK, cx=154, cy=62, r=7)
    + z('path', '#f6a6b8', d='M84 100 L116 100 L114 136 L86 136Z')
    + z('path', '#f6a6b8', d='M48 140 Q60 124 100 126 Q140 124 152 140 Q140 146 130 142 Q120 150 110 144 Q100 152 90 144 Q80 150 70 142 Q60 146 48 140Z')
    + z('circle', '#5a4033', cx=100, cy=32, r=11)
    + face(100, 68, SK, '#5a4033', 'smile')
    + s('path', '#f07a8a', d='M92 34 Q100 26 108 34', stroke_width=2.5)
)

# 12. magic hat and wand
ITEMS['magic-hat'] = (
    z('ellipse', '#5b6b7a', cx=96, cy=112, rx=52, ry=13)
    + s('ellipse', '#2b2220', cx=96, cy=112, rx=40, ry=8, stroke_width=2)
    + z('path', '#ffffff', d='M82 80 Q70 40 80 30 Q92 36 92 76Z') + z('path', '#ffffff', d='M110 76 Q110 36 124 32 Q132 44 118 80Z')
    + s('path', '#f6a6b8', d='M84 70 Q78 46 82 38 Q88 44 88 68Z', stroke_width=2) + s('path', '#f6a6b8', d='M113 68 Q114 44 122 40 Q126 48 117 70Z', stroke_width=2)
    + z('circle', '#ffffff', cx=98, cy=92, r=22)
    + mini_face(98, 90, 8, 6)
    + z('path', '#5b6b7a', d='M60 114 Q96 126 132 114 L128 166 Q96 178 64 166Z')
    + s('path', '#e04b5a', d='M62 136 Q96 146 131 136 L130 150 Q96 160 63 150Z', stroke_width=2.5)
    + s('path', d='M44 112 Q96 136 148 112', stroke_width=3)
    + z('path', '#2b2220', d='M140 162 L170 118 L178 124 L148 168Z')
    + s('path', '#ffffff', d='M164 126 L170 118 L178 124 L172 132Z', stroke_width=2.5)
    + sparkle(160, 94, 9) + sparkle(182, 104, 5) + sparkle(148, 76, 5) + sparkle(36, 74, 7)
)

# 13. aquarium tank
ITEMS['aquarium-tank'] = (
    z('rect', '#8fc7e8', x=28, y=56, width=144, height=110, rx=6)
    + s('path', d='M28 74 Q46 68 64 74 Q82 80 100 74 Q118 68 136 74 Q154 80 172 74', stroke='#ffffff', stroke_width=2.5)
    + s('path', '#d9a66b', d='M30 150 Q60 142 100 148 Q140 154 170 146 L170 164 L30 164Z', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M48 148 Q38 120 50 96 Q58 120 56 148Z') + z('path', '#9ccf7a', d='M60 148 Q70 122 62 104 Q50 126 54 148Z')
    + z('path', '#9ccf7a', d='M150 150 Q142 126 152 112 Q162 128 156 150Z')
    + z('path', '#f5b971', d='M90 112 Q100 94 124 102 L138 92 L136 120 L124 112 Q102 128 90 112Z')
    + dot(102, 108, 3) + s('ellipse', CH, cx=109, cy=115, rx=4, ry=2.5, stroke='none')
    + z('path', '#f07a8a', d='M126 140 Q120 130 108 134 L100 128 L100 146 L108 140 Q120 146 126 140Z') + dot(119, 137, 2.5)
    + s('circle', '#ffffff', cx=86, cy=96, r=4, stroke_width=2) + s('circle', '#ffffff', cx=80, cy=84, r=3, stroke_width=2)
    + z('rect', '#5b6b7a', x=22, y=48, width=156, height=12, rx=3)
    + z('rect', '#5b6b7a', x=36, y=166, width=128, height=12, rx=3)
)

# 14. DJ turntable
ITEMS['dj'] = (
    body('#a98bd0', top=96, bottom=140)
    + face(100, 70, SK, '#2b2220', 'open')
    + s('path', d='M64 70 Q64 26 100 26 Q136 26 136 70', stroke_width=8) + s('path', d='M64 70 Q64 26 100 26 Q136 26 136 70', stroke='#e04b5a', stroke_width=3)
    + z('rect', '#e04b5a', x=58, y=58, width=14, height=26, rx=6) + z('rect', '#e04b5a', x=128, y=58, width=14, height=26, rx=6)
    + z('rect', '#5b6b7a', x=22, y=124, width=156, height=54, rx=6)
    + z('ellipse', '#2b2220', cx=58, cy=150, rx=28, ry=17) + s('ellipse', '#f07a8a', cx=58, cy=150, rx=8, ry=5, stroke_width=2)
    + z('ellipse', '#2b2220', cx=142, cy=150, rx=28, ry=17) + s('ellipse', '#ffc94d', cx=142, cy=150, rx=8, ry=5, stroke_width=2)
    + s('rect', '#c9d3db', x=92, y=136, width=16, height=34, rx=2, stroke_width=2) + s('path', d='M96 146 L104 146 M96 158 L104 158', stroke_width=2.5)
    + z('circle', SK, cx=66, cy=136, r=9) + z('circle', SK, cx=134, cy=136, r=9)
    + note(20, 70) + note(168, 52, '#8fc7e8')
)

# 15. ukulele
ITEMS['ukulele'] = (
    z('rect', '#9a6a3f', x=92, y=40, width=16, height=70, rx=2)
    + z('path', '#8b6b4f', d='M88 22 L112 22 L110 44 L90 44Z')
    + dot(86, 28, 3.5, '#c9d3db') + dot(86, 38, 3.5, '#c9d3db') + dot(114, 28, 3.5, '#c9d3db') + dot(114, 38, 3.5, '#c9d3db')
    + z('path', '#f5b971', d='M100 92 Q74 86 72 112 Q72 124 80 130 Q58 140 62 164 Q68 184 100 184 Q132 184 138 164 Q142 140 120 130 Q128 124 128 112 Q126 86 100 92Z')
    + z('rect', '#9a6a3f', x=92, y=60, width=16, height=60, rx=2)
    + s('circle', '#5b6b7a', cx=100, cy=134, r=11)
    + z('rect', '#8b6b4f', x=84, y=162, width=32, height=8, rx=2)
    + s('path', d='M96 44 L96 166 M100 44 L100 166 M104 44 L104 166', stroke='#f4f4f0', stroke_width=1.2)
    + s('path', d='M92 72 L108 72 M92 86 L108 86 M92 100 L108 100', stroke_width=1.5)
    + dot(80, 152, 3) + dot(120, 152, 3) + cheeks(72, 128, 160, 5, 3)
    + note(28, 90) + note(150, 76, '#f07a8a')
)

# 16. saxophone
ITEMS['saxophone'] = (
    s('path', d='M88 44 Q86 28 66 30 L52 34', stroke_width=11) + s('path', d='M88 44 Q86 28 66 30 L52 34', stroke='#ffc94d', stroke_width=6)
    + z('rect', '#2b2220', x=40, y=28, width=14, height=12, rx=3)
    + z('path', '#ffc94d', d='M80 40 L96 40 L104 138 Q106 156 120 154 Q132 150 132 124 L126 98 L164 92 L150 124 Q144 176 116 178 Q84 178 84 146Z')
    + z('ellipse', '#f5d58a', cx=145, cy=95, rx=19, ry=6)
    + s('ellipse', '#d9a66b', cx=145, cy=95, rx=12, ry=3, stroke_width=2)
    + ''.join(s('circle', '#f4f4f0', cx=x, cy=y, r=4.5, stroke_width=2) for x, y in ((90, 64), (91, 82), (93, 100), (95, 118)))
    + s('path', d='M86 136 Q96 150 104 138', stroke_width=2)
    + dot(108, 162, 3) + dot(126, 160, 3) + cheeks(100, 134, 168, 4.5, 2.5)
    + note(150, 54) + note(30, 120, '#8fc7e8') + note(170, 150, '#f07a8a')
)

# 17. knitting
ITEMS['knitting'] = (
    s('path', d='M120 150 Q150 170 168 140 Q178 122 160 112', stroke='#f07a8a', stroke_width=7) + s('path', d='M120 150 Q150 170 168 140 Q178 122 160 112', stroke='#f6a6b8', stroke_width=2)
    + z('rect', '#8fb3e0', x=126, y=72, width=48, height=42, rx=4)
    + s('path', d='M134 82 L140 90 L146 82 M146 82 L152 90 L158 82 M158 82 L164 90 L170 82 M134 96 L140 104 L146 96 M146 96 L152 104 L158 96 M158 96 L164 104 L170 96', stroke_width=2)
    + z('circle', '#f6a6b8', cx=82, cy=128, r=48)
    + s('path', d='M42 104 Q80 96 118 120 M36 128 Q78 116 126 142 M44 152 Q82 140 116 162 M60 88 Q52 126 70 172 M94 82 Q112 124 100 174', stroke='#f07a8a', stroke_width=2.5)
    + dot(70, 128) + dot(96, 128) + cheeks(60, 106, 138, 6, 3.5) + s('path', d='M78 138 Q83 143 88 138', stroke_width=2.5)
    + s('path', d='M48 34 L150 70', stroke_width=8) + s('path', d='M48 34 L150 70', stroke='#c9d3db', stroke_width=3)
    + s('path', d='M150 34 L132 74', stroke_width=8) + s('path', d='M150 34 L132 74', stroke='#c9d3db', stroke_width=3)
    + z('circle', '#e8735a', cx=44, cy=32, r=7) + z('circle', '#e8735a', cx=152, cy=30, r=7)
)

# 18. person with camera
ITEMS['camera-hobby'] = (
    body('#7cc4b0')
    + face(100, 90, SK, '#5a4033', 'smile')
    + s('path', d='M72 108 L66 142 M128 108 L134 142', stroke='#e8735a', stroke_width=4)
    + z('rect', '#5b6b7a', x=58, y=136, width=84, height=46, rx=6)
    + z('rect', '#5b6b7a', x=72, y=128, width=22, height=10, rx=2)
    + s('rect', '#ffe27a', x=124, y=142, width=10, height=6, rx=1.5, stroke_width=2)
    + z('circle', '#c9d3db', cx=100, cy=159, r=17) + s('circle', '#2b2220', cx=100, cy=159, r=9, stroke_width=2.5)
    + dot(96, 155, 2.5, '#ffffff')
    + z('circle', SK, cx=56, cy=160, r=9) + z('circle', SK, cx=144, cy=160, r=9)
    + sparkle(150, 46, 8) + sparkle(168, 70, 5)
)

# 19. bird watching
ITEMS['bird-watching'] = (
    body('#9ccf7a', cx=78, top=136)
    + face(78, 104, SK, '#2b2220', 'smile')
    + z('path', '#d9a66b', d='M40 86 Q44 56 78 56 Q112 56 116 86Z') + z('rect', '#d9a66b', x=30, y=80, width=96, height=10, rx=5)
    + z('rect', '#5b6b7a', x=58, y=96, width=18, height=26, rx=5) + z('rect', '#5b6b7a', x=82, y=96, width=18, height=26, rx=5)
    + s('rect', '#5b6b7a', x=74, y=104, width=10, height=8, stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=67, cy=99, r=5, stroke_width=2) + s('circle', '#8fc7e8', cx=91, cy=99, r=5, stroke_width=2)
    + z('circle', SK, cx=62, cy=128, r=8) + z('circle', SK, cx=96, cy=128, r=8)
    + s('path', d='M120 70 L182 60 M160 63 L172 48', stroke='#9a6a3f', stroke_width=5)
    + z('path', '#9ccf7a', d='M172 50 Q180 38 186 44 Q182 54 172 50Z')
    + z('ellipse', '#8fc7e8', cx=150, cy=50, rx=16, ry=13)
    + z('path', '#8fc7e8', d='M136 52 L122 46 L128 58Z')
    + z('path', '#ffc94d', d='M164 44 L172 46 L164 50Z')
    + dot(156, 44, 2.5) + s('ellipse', CH, cx=154, cy=52, rx=4, ry=2.5, stroke='none')
    + s('path', d='M146 63 L146 67 M152 63 L152 67', stroke_width=2)
    + note(160, 100, '#f07a8a')
)

# 20. vegetable garden planter
ITEMS['gardening-hobby'] = (
    s('path', d='M64 112 L64 66 M100 112 L100 56 M136 112 L136 70', stroke='#7cc4a0', stroke_width=4)
    + z('path', '#9ccf7a', d='M64 92 Q44 86 42 70 Q60 72 64 92Z') + z('path', '#9ccf7a', d='M64 82 Q84 74 84 60 Q66 64 64 82Z')
    + z('circle', '#e04b5a', cx=56, cy=104, r=9) + z('circle', '#e04b5a', cx=74, cy=100, r=8)
    + z('path', '#7cc4a0', d='M100 104 Q78 90 84 60 Q100 76 100 104Z') + z('path', '#9ccf7a', d='M100 104 Q122 88 118 54 Q100 74 100 104Z')
    + z('path', '#9ccf7a', d='M136 110 Q120 96 124 78 Q136 90 136 110Z') + z('path', '#9ccf7a', d='M136 110 Q152 96 150 80 Q138 90 136 110Z')
    + z('rect', '#9a6a3f', x=30, y=108, width=140, height=14, rx=3)
    + z('rect', '#d9a66b', x=34, y=120, width=132, height=56, rx=3)
    + s('path', d='M34 138 L166 138 M34 158 L166 158', stroke='#9a6a3f', stroke_width=2)
    + dot(88, 146) + dot(112, 146) + cheeks(80, 120, 155, 5, 3) + s('path', d='M96 154 Q100 158 104 154', stroke_width=2.5)
    + sparkle(160, 40, 7) + sparkle(36, 44, 5)
)
