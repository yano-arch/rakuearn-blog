from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def bar(d, color, w=10, inner=4):
    """太い棒（外線＋色の芯）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def kao(x, y, gap=10, r=3, ch=True):
    """点の目＋ほっぺ＋小さな口"""
    o = dot(x - gap, y, r) + dot(x + gap, y, r)
    if ch:
        o += cheeks(x - gap - 8, x + gap + 8, y + 8, 5, 3)
    o += s('path', d=f'M{x-4} {y+7} Q{x} {y+11} {x+4} {y+7}', stroke_width=2.5)
    return o


def drop(x, y, k=1.0, c='#8fc7e8'):
    return s('path', c, d=f'M{x} {y-9*k} Q{x+6*k} {y} {x} {y+4*k} Q{x-6*k} {y} {x} {y-9*k}Z', stroke_width=2)


# 1. iron
ITEMS['iron'] = (
    s('path', d='M40 82 Q34 72 40 62 Q46 52 40 42', stroke_width=2.5)
    + s('path', d='M56 76 Q50 66 56 56 Q62 46 56 36', stroke_width=2.5)
    + z('path', '#e8735a', d='M74 104 Q72 58 100 56 L150 56 Q166 58 166 76 L166 104 L150 104 L150 80 Q150 72 142 72 L104 72 Q90 74 90 104Z')
    + z('path', '#8fc7e8', d='M28 150 Q38 102 96 96 L164 96 Q176 98 176 112 L176 150Z')
    + z('rect', '#c9d3db', x=22, y=148, width=158, height=14, rx=6)
    + s('circle', '#ffffff', cx=150, cy=124, r=9, stroke_width=2.5)
    + kao(108, 122)
    + s('path', d='M24 178 L180 178', stroke_width=2)
)

# 2. hair-dryer
ITEMS['hair-dryer'] = (
    z('path', '#f6a6b8', d='M106 96 L140 96 L134 166 Q124 176 114 166Z')
    + s('rect', '#f07a8a', x=116, y=114, width=14, height=20, rx=4, stroke_width=2.5)
    + s('path', d='M124 172 Q128 188 150 182 Q166 178 172 186', stroke_width=2.5)
    + z('rect', '#e8735a', x=36, y=62, width=24, height=40, rx=5)
    + z('rect', '#f6a6b8', x=52, y=52, width=104, height=56, rx=26)
    + z('circle', '#f07a8a', cx=152, cy=80, r=22)
    + s('circle', '#ffffff', cx=152, cy=80, r=11, stroke_width=2.5)
    + kao(98, 78)
    + s('path', d='M28 70 L16 64 M28 82 L14 82 M28 94 L16 100', stroke_width=2.5)
)

# 3. television
ITEMS['television'] = (
    s('path', d='M100 54 L74 24 M100 54 L128 22', stroke_width=3)
    + dot(74, 24, 5) + dot(128, 22, 5)
    + s('rect', '#9a6a3f', x=60, y=156, width=10, height=22, rx=3)
    + s('rect', '#9a6a3f', x=130, y=156, width=10, height=22, rx=3)
    + z('rect', '#9a6a3f', x=48, y=150, width=104, height=12, rx=5)
    + z('rect', '#5b6b7a', x=26, y=50, width=148, height=104, rx=14)
    + s('rect', '#8fc7e8', x=38, y=62, width=110, height=80, rx=8)
    + s('path', '#9ccf7a', d='M39 126 Q66 104 92 118 Q118 100 147 116 L147 134 Q147 141 140 141 L46 141 Q39 141 39 134Z', stroke_width=2.5)
    + s('circle', '#ffe27a', cx=118, cy=84, r=11, stroke_width=2.5)
    + s('circle', '#c9d3db', cx=162, cy=80, r=5, stroke_width=2.5)
    + s('circle', '#c9d3db', cx=162, cy=98, r=5, stroke_width=2.5)
    + dot(70, 92, 3) + dot(88, 92, 3) + s('path', d='M75 100 Q79 104 83 100', stroke_width=2.5)
)

# 4. ceiling-light
ITEMS['ceiling-light'] = (
    s('path', d='M30 22 L170 22', stroke_width=2)
    + z('rect', '#c9d3db', x=84, y=22, width=32, height=10, rx=4)
    + s('path', d='M100 32 L100 64')
    + s('path', d='M100 132 L100 150 M76 128 L64 144 M124 128 L136 144 M58 116 L40 124 M142 116 L160 124', stroke='#f5b971', stroke_width=5)
    + z('circle', '#ffe27a', cx=100, cy=112, r=16)
    + z('path', '#7cc4b0', d='M50 112 Q52 64 100 62 Q148 64 150 112Z')
    + s('path', d='M50 112 L150 112')
    + kao(100, 88, 12)
    + s('path', d='M100 160 L100 178 M70 156 L60 172 M130 156 L140 172', stroke='#ffc94d', stroke_width=4)
)

# 5. frying-pan
ITEMS['frying-pan'] = (
    z('rect', '#9a6a3f', x=126, y=96, width=58, height=16, rx=8)
    + s('circle', '#fbf6ee', cx=172, cy=104, r=3.5, stroke_width=2)
    + z('circle', '#5b6b7a', cx=78, cy=104, r=54)
    + s('circle', '#c9d3db', cx=78, cy=104, r=44)
    + z('path', '#ffffff', d='M50 100 Q46 72 74 70 Q100 62 108 86 Q120 106 104 126 Q86 142 64 130 Q46 120 50 100Z')
    + z('circle', '#ffc94d', cx=80, cy=100, r=16)
    + dot(74, 98, 2.5) + dot(86, 98, 2.5) + cheeks(69, 91, 104, 3.5, 2.2)
    + s('path', d='M77 104 Q80 107 83 104', stroke_width=2)
    + s('path', d='M34 172 L170 172', stroke_width=2)
)

# 6. cutting-board
ITEMS['cutting-board'] = (
    z('rect', '#d9a66b', x=24, y=76, width=152, height=94, rx=12)
    + s('circle', '#fbf6ee', cx=162, cy=122, r=5, stroke_width=2.5)
    + z('path', '#f5b971', d='M36 140 Q40 124 58 120 L104 112 Q112 120 106 132 L58 150 Q40 154 36 140Z')
    + s('path', d='M58 128 L62 134 M76 120 L80 126 M78 138 L80 142', stroke_width=2)
    + z('path', '#9ccf7a', d='M104 112 Q112 96 126 98 Q120 108 110 116Z')
    + z('path', '#9ccf7a', d='M106 116 Q124 112 130 124 Q118 126 108 122Z')
    + z('circle', '#f5b971', cx=124, cy=148, r=10)
    + s('circle', '#ffe27a', cx=124, cy=148, r=4, stroke_width=2)
    + z('circle', '#f5b971', cx=146, cy=150, r=10)
    + s('circle', '#ffe27a', cx=146, cy=150, r=4, stroke_width=2)
    + z('path', '#f4f4f0', d='M42 86 Q62 58 120 60 L120 86Z')
    + z('rect', '#8b6b4f', x=118, y=62, width=50, height=20, rx=8)
    + dot(130, 72, 2.2) + dot(156, 72, 2.2)
    + s('path', d='M20 182 L180 182', stroke_width=2)
)

# 7. kitchen-utensils
ITEMS['kitchen-utensils'] = (
    s('path', d='M30 26 L170 26', stroke_width=3)
    + s('path', d='M54 26 L54 38 M100 26 L100 38 M146 26 L146 38', stroke_width=2.5)
    # ladle
    + z('rect', '#9a6a3f', x=48, y=38, width=12, height=100, rx=6)
    + s('circle', '#fbf6ee', cx=54, cy=46, r=3, stroke_width=2)
    + z('path', '#c9d3db', d='M30 134 L78 134 Q78 166 54 168 Q30 166 30 134Z')
    # spatula
    + z('rect', '#9a6a3f', x=94, y=38, width=12, height=90, rx=6)
    + s('circle', '#fbf6ee', cx=100, cy=46, r=3, stroke_width=2)
    + z('rect', '#f5b971', x=82, y=122, width=36, height=52, rx=8)
    + dot(93, 142, 2.5) + dot(107, 142, 2.5) + cheeks(88, 112, 148, 3.5, 2.2)
    + s('path', d='M97 148 Q100 151 103 148', stroke_width=2)
    + s('path', d='M92 160 L92 168 M100 160 L100 168 M108 160 L108 168', stroke_width=2.5)
    # whisk
    + s('path', d='M140 96 Q118 150 146 172 Q174 150 152 96', stroke='#b9a99c', stroke_width=7)
    + s('path', d='M140 96 Q118 150 146 172 Q174 150 152 96', stroke_width=2.5)
    + s('path', d='M143 96 Q132 150 146 172 Q160 150 149 96', stroke_width=2.5)
    + s('path', d='M146 100 L146 172', stroke_width=2.5)
    + z('rect', '#9a6a3f', x=139, y=38, width=14, height=62, rx=6)
    + s('circle', '#fbf6ee', cx=146, cy=46, r=3, stroke_width=2)
)

# 8. plates
ITEMS['plates'] = (
    z('path', '#ffffff', d='M30 160 Q30 172 100 172 Q170 172 170 160 L170 154 L30 154Z')
    + s('path', d='M32 160 Q100 168 168 160', stroke='#8fc7e8', stroke_width=3)
    + z('path', '#ffffff', d='M32 146 Q32 158 100 158 Q168 158 168 146 L168 140 L32 140Z')
    + s('path', d='M34 146 Q100 154 166 146', stroke='#8fc7e8', stroke_width=3)
    + z('path', '#ffffff', d='M34 132 Q34 144 100 144 Q166 144 166 132 L166 126 L34 126Z')
    + s('path', d='M36 132 Q100 140 164 132', stroke='#8fc7e8', stroke_width=3)
    + z('ellipse', '#ffffff', cx=100, cy=110, rx=70, ry=26)
    + s('ellipse', '#8fc7e8', cx=100, cy=110, rx=56, ry=19, stroke_width=2.5)
    + s('ellipse', '#ffffff', cx=100, cy=110, rx=44, ry=13, stroke_width=2.5)
    + kao(100, 106, 10, 3)
    + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 9. teapot
ITEMS['teapot'] = (
    s('path', d='M168 66 Q162 56 168 46 Q174 36 168 28', stroke_width=2.5)
    + s('path', d='M184 72 Q178 62 184 52', stroke_width=2.5)
    + z('path', '#7cc4b0', d='M134 118 Q160 112 168 80 L180 84 Q174 132 140 146Z')
    + s('path', d='M56 104 Q24 104 28 132 Q32 154 60 150', stroke_width=12)
    + s('path', d='M56 104 Q24 104 28 132 Q32 154 60 150', stroke='#7cc4b0', stroke_width=5)
    + z('ellipse', '#7cc4b0', cx=96, cy=126, rx=50, ry=46)
    + s('path', d='M50 136 Q96 152 142 136', stroke='#ffffff', stroke_width=5)
    + z('path', '#7cc4b0', d='M62 86 Q96 64 130 86Z')
    + z('circle', '#f5b971', cx=96, cy=68, r=8)
    + kao(96, 116, 12, 3.2)
    + s('path', d='M40 178 L160 178', stroke_width=2)
)

# 10. oven-mitt
ITEMS['oven-mitt'] = (
    z('path', '#e8735a', d='M60 156 L58 90 Q58 40 102 38 Q144 40 144 90 L144 156Z')
    + z('path', '#e8735a', d='M64 122 Q36 112 32 86 Q32 66 48 68 Q60 72 64 94')
    + s('path', d='M70 64 Q76 56 84 54 M120 54 Q130 58 134 66', stroke='#f6a6b8', stroke_width=3)
    + s('circle', '#f6a6b8', cx=78, cy=134, r=4, stroke='none')
    + s('circle', '#f6a6b8', cx=124, cy=132, r=4, stroke='none')
    + s('circle', '#f6a6b8', cx=102, cy=62, r=4, stroke='none')
    + kao(102, 100, 12, 3.2)
    + z('rect', '#f4f4f0', x=52, y=150, width=100, height=30, rx=8)
    + s('path', d='M152 160 Q172 160 170 174 Q166 184 152 176', stroke_width=3)
)

# 11. apron
ITEMS['apron'] = (
    s('path', d='M76 46 Q100 14 124 46', stroke_width=4)
    + s('path', d='M50 98 Q38 100 32 110 M150 98 Q162 100 168 110', stroke_width=4)
    + s('path', d='M32 110 Q22 104 24 116 Q28 122 32 110 M168 110 Q178 104 176 116 Q172 122 168 110', stroke_width=3)
    + z('path', '#f6a6b8', d='M76 44 L124 44 L124 84 Q150 88 152 112 L150 178 L50 178 L48 112 Q50 88 76 84Z')
    + s('path', d='M50 168 Q75 174 100 168 Q125 174 150 168', stroke_width=2.5)
    + s('path', '#f07a8a', d='M100 72 C92 66 88 62 91 57 C94 53 100 55 100 59 C100 55 106 53 109 57 C112 62 108 66 100 72Z', stroke_width=2)
    + z('rect', '#ffffff', x=74, y=118, width=52, height=34, rx=8)
    + s('path', d='M100 118 L100 152', stroke_width=2.5)
)

# 12. toilet
ITEMS['toilet'] = (
    z('rect', '#ffffff', x=56, y=30, width=88, height=64, rx=10)
    + s('rect', '#c9d3db', x=64, y=40, width=18, height=8, rx=3, stroke_width=2.5)
    + kao(100, 64, 12, 3.2)
    + z('path', '#ffffff', d='M46 110 Q48 158 80 166 L80 180 L120 180 L120 166 Q152 158 154 110Z')
    + z('rect', '#8fc7e8', x=38, y=94, width=124, height=18, rx=9)
    + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 13. toothbrush-cup
ITEMS['toothbrush-cup'] = (
    bar('M88 130 L70 56', '#f07a8a', 12, 6)
    + z('rect', '#ffffff', x=56, y=36, width=14, height=26, rx=3, transform='rotate(-14 63 49)')
    + s('path', d='M58 42 L54 43 M59 49 L55 50 M60 56 L56 57', stroke='#8fc7e8', stroke_width=2)
    + bar('M110 130 L134 50', '#9ccf7a', 12, 6)
    + z('rect', '#ffffff', x=134, y=30, width=14, height=26, rx=3, transform='rotate(17 141 43)')
    + bar('M98 130 L102 64', '#f5d58a', 12, 6)
    + z('rect', '#ffffff', x=104, y=46, width=12, height=22, rx=3, transform='rotate(3 110 57)')
    + z('rect', '#8fc7e8', x=58, y=98, width=84, height=80, rx=12)
    + s('path', d='M58 112 L142 112', stroke_width=2.5)
    + kao(100, 138, 12, 3.2)
    + s('path', d='M30 182 L170 182', stroke_width=2)
)

# 14. towel
ITEMS['towel'] = (
    z('rect', '#8fc7e8', x=32, y=138, width=136, height=38, rx=14)
    + s('path', d='M140 138 L140 176', stroke_width=2.5)
    + s('path', d='M50 150 L126 150 M50 164 L126 164', stroke='#ffffff', stroke_width=4)
    + z('rect', '#f6a6b8', x=40, y=102, width=124, height=38, rx=14)
    + s('path', d='M138 102 L138 140', stroke_width=2.5)
    + s('path', d='M56 114 L124 114 M56 128 L124 128', stroke='#ffffff', stroke_width=4)
    + z('rect', '#9ccf7a', x=50, y=66, width=108, height=38, rx=14)
    + s('path', d='M134 66 L134 104', stroke_width=2.5)
    + kao(94, 82, 12, 3)
    + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 15. soap
ITEMS['soap'] = (
    z('path', '#8fc7e8', d='M30 150 L170 150 Q166 176 140 176 L60 176 Q34 176 30 150Z')
    + z('rect', '#f6a6b8', x=44, y=96, width=112, height=62, rx=22)
    + s('path', d='M60 108 Q80 102 100 104', stroke='#ffffff', stroke_width=4)
    + kao(100, 126, 12, 3.2)
    + z('circle', '#ffffff', cx=64, cy=76, r=16)
    + z('circle', '#ffffff', cx=98, cy=60, r=22)
    + z('circle', '#ffffff', cx=134, cy=78, r=14)
    + s('circle', '#ffffff', cx=150, cy=46, r=9, stroke_width=2.5)
    + s('circle', '#ffffff', cx=56, cy=40, r=7, stroke_width=2.5)
    + s('circle', '#ffffff', cx=124, cy=34, r=5, stroke_width=2.5)
    + s('path', d='M90 52 Q94 46 100 46', stroke='#8fc7e8', stroke_width=3)
)

# 16. shampoo
ITEMS['shampoo'] = (
    s('rect', '#c9d3db', x=68, y=44, width=10, height=26, rx=2, stroke_width=2.5)
    + z('path', '#f4f4f0', d='M44 40 L96 40 L96 52 L44 52 Q36 52 36 46 Q36 40 44 40Z')
    + z('rect', '#f4f4f0', x=60, y=64, width=26, height=18, rx=4)
    + z('rect', '#a98bd0', x=42, y=78, width=62, height=102, rx=14)
    + s('rect', '#ffffff', x=52, y=108, width=42, height=48, rx=8, stroke_width=2.5)
    + s('path', '#9ccf7a', d='M73 148 Q60 136 66 120 Q82 128 73 148Z', stroke_width=2)
    + s('path', '#9ccf7a', d='M73 148 Q86 136 82 124 Q72 132 73 148Z', stroke_width=2)
    + z('rect', '#f5d58a', x=122, y=92, width=34, height=18, rx=5)
    + z('rect', '#7cc4b0', x=114, y=106, width=50, height=74, rx=16)
    + kao(139, 136, 10, 3)
    + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 17. shower
ITEMS['shower'] = (
    bar('M40 20 L40 40 Q40 48 48 48 L112 48 L112 64', '#c9d3db', 12, 6)
    + z('path', '#c9d3db', d='M78 94 Q80 64 112 62 Q144 64 146 94Z')
    + z('rect', '#f4f4f0', x=72, y=90, width=80, height=12, rx=6)
    + dot(102, 80, 2.8) + dot(122, 80, 2.8) + cheeks(94, 130, 86, 4, 2.5)
    + s('path', d='M86 112 L72 140 M100 112 L94 146 M112 112 L112 150 M124 112 L130 146 M138 112 L152 140', stroke='#8fc7e8', stroke_width=4)
    + drop(66, 160) + drop(92, 168) + drop(114, 174) + drop(136, 168) + drop(160, 158)
    + drop(80, 152, 0.7) + drop(148, 150, 0.7)
)

# 18. laundry-hanging
ITEMS['laundry-hanging'] = (
    z('rect', '#9a6a3f', x=20, y=34, width=10, height=146, rx=4)
    + z('rect', '#9a6a3f', x=170, y=34, width=10, height=146, rx=4)
    + s('path', d='M26 44 Q100 62 174 44', stroke_width=2.5)
    # t-shirt
    + z('path', '#8fc7e8', d='M44 52 L80 54 L98 70 L88 82 L80 76 L80 128 L44 128 L44 76 L36 82 L28 70Z')
    + s('path', d='M54 52 Q62 62 70 53', stroke_width=2.5)
    # sock
    + z('path', '#f07a8a', d='M106 56 L122 56 L122 100 Q134 104 134 116 Q132 126 116 124 L106 120Z')
    + s('path', d='M106 66 L122 66', stroke='#ffffff', stroke_width=3)
    # towel
    + z('rect', '#f5d58a', x=138, y=52, width=26, height=80, rx=4)
    + s('path', d='M138 118 L164 118', stroke_width=2.5)
    # pins
    + s('rect', '#e8735a', x=48, y=44, width=6, height=14, rx=2, stroke_width=2)
    + s('rect', '#e8735a', x=70, y=46, width=6, height=14, rx=2, stroke_width=2)
    + s('rect', '#e8735a', x=111, y=48, width=6, height=14, rx=2, stroke_width=2)
    + s('rect', '#e8735a', x=148, y=45, width=6, height=14, rx=2, stroke_width=2)
    + dot(56, 98, 2.8) + dot(70, 98, 2.8) + s('path', d='M60 105 Q63 108 66 105', stroke_width=2)
    + s('path', d='M14 180 L186 180', stroke_width=2)
)

# 19. folding-clothes
ITEMS['folding-clothes'] = (
    z('rect', '#8fc7e8', x=36, y=146, width=128, height=32, rx=8)
    + s('path', d='M64 146 L64 178 M136 146 L136 178', stroke_width=2.5)
    + z('rect', '#f5b971', x=42, y=116, width=116, height=32, rx=8)
    + s('path', d='M68 116 L68 148 M132 116 L132 148', stroke_width=2.5)
    + z('rect', '#f6a6b8', x=48, y=86, width=104, height=32, rx=8)
    + s('path', d='M72 86 L72 118 M128 86 L128 118', stroke_width=2.5)
    + z('rect', '#9ccf7a', x=54, y=56, width=92, height=32, rx=8)
    + s('path', d='M76 56 L76 88 M124 56 L124 88', stroke_width=2.5)
    + z('path', '#ffffff', d='M86 56 L100 68 L114 56Z')
    + dot(92, 76, 2.5) + dot(108, 76, 2.5) + cheeks(84, 116, 81, 3.5, 2.2)
    + s('path', d='M98 80 Q100 82 102 80', stroke_width=2)
    + s('path', d='M24 182 L176 182', stroke_width=2)
)

# 20. washing-dishes
ITEMS['washing-dishes'] = (
    bar('M152 108 L152 52 Q152 40 140 40 L124 40 Q116 40 116 50 L116 56', '#c9d3db', 12, 6)
    + s('rect', '#c9d3db', x=144, y=72, width=22, height=8, rx=3, stroke_width=2.5)
    + s('path', d='M116 62 L116 104', stroke='#8fc7e8', stroke_width=6)
    + z('circle', '#ffffff', cx=78, cy=100, r=34)
    + s('circle', '#8fc7e8', cx=78, cy=100, r=22, stroke_width=2.5)
    + dot(70, 98, 2.8) + dot(86, 98, 2.8) + cheeks(62, 94, 105, 4, 2.5)
    + s('path', d='M75 105 Q78 108 81 105', stroke_width=2)
    + z('rect', '#c9d3db', x=24, y=110, width=152, height=66, rx=10)
    + s('rect', '#8fc7e8', x=34, y=118, width=132, height=18, rx=5, stroke_width=2.5)
    + z('rect', '#ffe27a', x=122, y=92, width=34, height=20, rx=5)
    + s('rect', '#9ccf7a', x=122, y=92, width=34, height=7, rx=3, stroke_width=2.5)
    + s('circle', '#ffffff', cx=44, cy=108, r=8, stroke_width=2.5)
    + s('circle', '#ffffff', cx=112, cy=104, r=7, stroke_width=2.5)
    + s('circle', '#ffffff', cx=56, cy=70, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=104, cy=64, r=6, stroke_width=2.5)
    + s('circle', '#ffffff', cx=166, cy=100, r=5, stroke_width=2.5)
)
