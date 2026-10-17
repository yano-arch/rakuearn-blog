from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def bar(d, color, w=10, inner=4):
    """太い棒（外線＋色の芯）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


# 1. bed
ITEMS['bed'] = (
    z('rect', '#d9a66b', x=28, y=64, width=20, height=114, rx=6)
    + s('rect', '#9a6a3f', x=44, y=160, width=8, height=18, rx=2)
    + s('rect', '#9a6a3f', x=160, y=160, width=8, height=18, rx=2)
    + z('rect', '#d9a66b', x=40, y=138, width=136, height=24, rx=4)
    + z('rect', '#ffffff', x=40, y=116, width=134, height=24, rx=6)
    + z('path', '#ffffff', d='M50 116 Q46 96 62 94 L84 94 Q98 96 94 116 Z')
    + z('path', '#8fc7e8', d='M84 146 L84 118 Q86 104 104 104 L168 104 Q178 106 176 118 L176 150 L84 150 Z')
    + s('path', d='M84 120 Q100 114 116 120', stroke_width=2.5)
    + s('circle', '#ffffff', cx=118, cy=128, r=4, stroke='none')
    + s('circle', '#ffffff', cx=142, cy=122, r=4, stroke='none')
    + s('circle', '#ffffff', cx=160, cy=136, r=4, stroke='none')
    + s('circle', '#ffffff', cx=132, cy=140, r=4, stroke='none')
    + s('path', d='M24 180 L180 180', stroke_width=2)
)

# 2. sofa
ITEMS['sofa'] = (
    s('rect', '#8b6b4f', x=40, y=158, width=8, height=18, rx=2)
    + s('rect', '#8b6b4f', x=152, y=158, width=8, height=18, rx=2)
    + z('rect', '#7cc4b0', x=44, y=66, width=112, height=64, rx=16)
    + s('path', d='M100 72 L100 122', stroke_width=2.5)
    + z('rect', '#7cc4b0', x=40, y=118, width=120, height=42, rx=10)
    + s('path', d='M100 122 L100 156', stroke_width=2.5)
    + z('rect', '#7cc4b0', x=22, y=96, width=30, height=66, rx=14)
    + z('rect', '#7cc4b0', x=148, y=96, width=30, height=66, rx=14)
    + z('path', '#f5b971', d='M60 92 Q74 84 92 90 Q98 104 92 120 Q76 126 60 120 Q54 106 60 92 Z')
    + dot(70, 104, 2.5) + dot(84, 104, 2.5) + cheeks(66, 88, 110, 4, 2.5)
    + s('path', d='M74 110 Q77 113 80 110', stroke_width=2)
    + s('path', d='M16 180 L184 180', stroke_width=2)
)

# 3. washing-machine
ITEMS['washing-machine'] = (
    z('rect', '#f4f4f0', x=46, y=30, width=108, height=146, rx=12)
    + s('path', d='M46 60 L154 60')
    + s('rect', '#8fc7e8', x=58, y=40, width=30, height=12, rx=3, stroke_width=2.5)
    + s('circle', '#c9d3db', cx=136, cy=45, r=8)
    + dot(116, 45, 3)
    + z('circle', '#c9d3db', cx=100, cy=116, r=42)
    + s('circle', '#8fc7e8', cx=100, cy=116, r=31)
    + s('path', '#ffffff', d='M70 112 Q78 104 86 112 Q94 120 102 112 Q110 104 118 112 Q124 118 130 114 Q126 104 118 96 Q100 82 82 96 Q74 102 70 112 Z', stroke='none')
    + s('circle', '#ffffff', cx=88, cy=128, r=7, stroke_width=2.5)
    + s('circle', '#ffffff', cx=110, cy=134, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=116, cy=122, r=4, stroke_width=2.5)
    + s('circle', '#ffffff', cx=96, cy=104, r=4, stroke_width=2.5)
    + s('path', d='M84 96 Q92 90 100 90', stroke='#ffffff', stroke_width=3)
    + s('rect', '#b9a99c', x=54, y=176, width=14, height=6, rx=2, stroke_width=2.5)
    + s('rect', '#b9a99c', x=132, y=176, width=14, height=6, rx=2, stroke_width=2.5)
)

# 4. broom-cleaning
ITEMS['broom-cleaning'] = (
    bar('M58 28 L86 116', '#9a6a3f', 11, 5)
    + z('path', '#f5d58a', d='M78 116 L96 110 Q118 136 126 172 Q100 182 72 178 Q66 146 78 116 Z')
    + s('path', d='M86 130 L84 174 M98 128 L102 176 M108 132 L116 172', stroke_width=2)
    + z('path', '#e8735a', d='M74 112 L98 104 L102 118 L78 126 Z')
    + z('rect', '#8fb3e0', x=146, y=110, width=12, height=34, rx=5)
    + z('path', '#8fb3e0', d='M124 146 Q152 136 180 146 L184 180 L120 180 Z')
    + s('path', d='M128 168 L176 168', stroke_width=2)
    + s('circle', '#b9a99c', cx=140, cy=176, r=3, stroke='none')
    + s('circle', '#b9a99c', cx=150, cy=177, r=2, stroke='none')
    + s('circle', '#b9a99c', cx=56, cy=180, r=3, stroke='none')
    + s('circle', '#b9a99c', cx=46, cy=181, r=2, stroke='none')
    + s('path', d='M16 184 L186 184', stroke_width=2)
)

# 5. cooking-pot
ITEMS['cooking-pot'] = (
    s('path', d='M68 50 Q60 42 68 34 Q76 26 68 18', stroke_width=2.5)
    + s('path', d='M132 50 Q124 42 132 34 Q140 26 132 18', stroke_width=2.5)
    + z('rect', '#c9d3db', x=24, y=164, width=152, height=16, rx=4)
    + z('path', '#ffc94d', d='M66 164 Q60 154 66 146 Q72 154 78 148 Q80 158 76 164 Z')
    + z('path', '#ffc94d', d='M94 164 Q88 152 96 144 Q102 152 108 146 Q112 156 106 164 Z')
    + z('path', '#ffc94d', d='M122 164 Q118 154 124 148 Q130 154 136 146 Q140 156 134 164 Z')
    + s('rect', '#5b6b7a', x=56, y=154, width=88, height=8, rx=3, stroke_width=2.5)
    + z('ellipse', '#e8735a', cx=36, cy=104, rx=12, ry=7)
    + z('ellipse', '#e8735a', cx=164, cy=104, rx=12, ry=7)
    + z('rect', '#e8735a', x=44, y=88, width=112, height=62, rx=10)
    + z('path', '#e8735a', d='M40 90 Q46 60 100 58 Q154 60 160 90 Z')
    + z('ellipse', '#f6e0c4', cx=100, cy=52, rx=12, ry=7)
    + dot(88, 116) + dot(112, 116) + cheeks(78, 122, 126, 6, 3.5)
    + s('path', d='M95 124 Q100 129 105 124', stroke_width=2.5)
)

# 6. bathtub
BUB = ''.join(z('circle', '#ffffff', cx=x, cy=y, r=r) for x, y, r in
              ((52, 98, 12), (72, 90, 14), (94, 96, 11), (150, 92, 13), (168, 100, 9)))
ITEMS['bathtub'] = (
    BUB
    + z('ellipse', '#ffe27a', cx=120, cy=96, rx=22, ry=13)
    + s('path', d='M102 92 Q96 82 104 86', stroke_width=2.5)
    + z('circle', '#ffe27a', cx=132, cy=72, r=12)
    + z('path', '#f5b971', d='M143 70 L154 74 L143 78 Z')
    + dot(136, 69, 2.5) + s('ellipse', CH, cx=134, cy=77, rx=4, ry=2.5, stroke='none')
    + s('path', d='M110 96 Q118 104 126 96', stroke_width=2.5)
    + s('path', d='M30 104 L30 60 Q30 46 44 46 L52 46', stroke_width=10)
    + s('path', d='M30 104 L30 60 Q30 46 44 46 L52 46', stroke='#c9d3db', stroke_width=4)
    + z('rect', '#c9d3db', x=50, y=40, width=8, height=14, rx=2)
    + z('path', '#8fc7e8', d='M54 64 Q50 70 54 74 Q58 70 54 64 Z')
    + s('rect', '#b9a99c', x=46, y=162, width=10, height=16, rx=3, stroke_width=2.5)
    + s('rect', '#b9a99c', x=144, y=162, width=10, height=16, rx=3, stroke_width=2.5)
    + z('path', '#f4f4f0', d='M28 108 L172 108 L166 152 Q164 166 148 166 L52 166 Q36 166 34 152 Z')
    + z('rect', '#f4f4f0', x=20, y=102, width=160, height=12, rx=6)
    + s('path', d='M46 128 L154 128', stroke='#8fc7e8', stroke_width=3)
    + s('circle', '#ffffff', cx=170, cy=70, r=5, stroke_width=2)
    + s('circle', '#ffffff', cx=84, cy=66, r=4, stroke_width=2)
)

# 7. house-key
ITEMS['house-key'] = (
    s('circle', cx=56, cy=70, r=28, stroke_width=9)
    + s('circle', cx=56, cy=70, r=28, stroke='#c9d3db', stroke_width=4)
    + s('path', d='M42 96 L40 108', stroke_width=3)
    + z('path', '#f07a8a', d='M40 142 C28 132 22 124 28 116 C33 110 40 113 40 119 C40 113 47 110 52 116 C58 124 52 132 40 142 Z')
    + z('path', '#ffc94d', d='M106 108 L170 108 Q178 108 178 116 L178 118 Q178 124 170 124 L162 124 L162 134 L152 134 L152 124 L144 124 L144 138 L132 138 L132 124 L106 124 Z')
    + z('circle', '#ffc94d', cx=82, cy=116, r=30)
    + s('circle', '#fbf6ee', cx=70, cy=104, r=8)
    + dot(78, 122) + dot(96, 122) + cheeks(72, 102, 130, 5, 3)
    + s('path', d='M83 128 Q87 132 91 128', stroke_width=2.5)
    + s('path', d='M150 92 L156 84 M164 96 L172 90', stroke_width=2.5)
)

# 8. desk-lamp
ITEMS['desk-lamp'] = (
    s('path', '#ffe27a', d='M124 108 L166 94 L188 176 L96 176 Z', stroke='none')
    + s('path', d='M16 178 L188 178', stroke_width=2)
    + z('ellipse', '#5b6b7a', cx=60, cy=168, rx=34, ry=9)
    + bar('M60 164 L44 108 L104 66', '#8fb3e0', 11, 5)
    + z('circle', '#8fb3e0', cx=44, cy=108, r=7)
    + z('path', '#8fb3e0', d='M98 66 Q106 46 128 48 L170 92 Q148 112 122 110 Z')
    + z('ellipse', '#ffe27a', cx=146, cy=102, rx=12, ry=7)
    + s('path', d='M98 158 L136 158 L136 170 L98 170 Z', fill='#e8735a', stroke_width=2.5)
    + s('path', d='M102 150 L132 150 L132 158 L102 158 Z', fill='#9ccf7a', stroke_width=2.5)
    + s('path', d='M178 70 L188 62 M182 100 L194 102 M156 64 L160 52', stroke_width=2.5)
)

# 9. alarm-clock
ITEMS['alarm-clock'] = (
    s('path', d='M72 156 L60 176 M128 156 L140 176', stroke_width=7)
    + z('path', '#ffc94d', d='M40 66 Q42 40 68 38 Z')
    + z('path', '#ffc94d', d='M160 66 Q158 40 132 38 Z')
    + s('path', d='M100 48 L100 36', stroke_width=4)
    + z('ellipse', '#b9a99c', cx=100, cy=34, rx=10, ry=5)
    + z('circle', '#e8735a', cx=100, cy=110, r=58)
    + s('circle', '#ffffff', cx=100, cy=110, r=45)
    + dot(100, 74, 3) + dot(136, 110, 3) + dot(100, 146, 3) + dot(64, 110, 3)
    + s('path', d='M100 110 L100 84', stroke_width=5)
    + s('path', d='M100 110 L124 122', stroke_width=4)
    + dot(100, 110, 5)
    + s('path', d='M24 50 L16 46 M22 66 L12 68 M176 50 L184 46 M178 66 L188 68', stroke_width=2.5)
)

# 10. trash-bins
def bin_(x, color, mark):
    return (z('path', color, d=f'M{x} 92 L{x+44} 92 L{x+40} 176 L{x+4} 176 Z')
            + z('rect', color, x=x - 4, y=80, width=52, height=14, rx=4)
            + s('rect', '#ffffff', x=x + 14, y=72, width=16, height=8, rx=3, stroke_width=2.5)
            + mark)


ITEMS['trash-bins'] = (
    bin_(24, '#8fb3e0',
         s('path', '#ffffff', d='M42 112 L42 106 L50 106 L50 112 Q56 116 56 124 L56 150 Q56 154 52 154 L40 154 Q36 154 36 150 L36 124 Q36 116 42 112 Z', stroke_width=2.5))
    + bin_(78, '#9ccf7a',
           s('rect', '#ffffff', x=89, y=112, width=22, height=38, rx=4, stroke_width=2.5)
           + s('path', d='M89 122 L111 122 M89 140 L111 140', stroke_width=2))
    + bin_(132, '#f5d58a',
           s('path', '#ffffff', d='M142 110 L162 110 L166 116 L166 152 L142 152 Z', stroke_width=2.5)
           + s('path', d='M147 124 L161 124 M147 132 L161 132 M147 140 L157 140', stroke_width=2))
    + s('path', d='M14 180 L188 180', stroke_width=2)
)
