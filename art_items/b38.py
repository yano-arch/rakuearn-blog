from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def bar(d, color, w=10, inner=4):
    """太い棒（外線＋色の芯）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def ground(x1=20, x2=180, y=180):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2)


# 1. desk-chair
ITEMS['desk-chair'] = (
    s('rect', '#9a6a3f', x=164, y=104, width=10, height=74, rx=2)
    + z('rect', '#d9a66b', x=110, y=104, width=46, height=74, rx=3)
    + s('path', d='M110 128 L156 128 M110 152 L156 152', stroke_width=2.5)
    + dot(133, 116, 3) + dot(133, 140, 3) + dot(133, 164, 3)
    + z('rect', '#d9a66b', x=70, y=92, width=114, height=14, rx=3)
    + z('ellipse', '#5b6b7a', cx=160, cy=88, rx=14, ry=5)
    + bar('M160 86 L146 58 L164 42', '#5b6b7a', 8, 3)
    + z('path', '#ffe27a', d='M156 36 L178 48 L170 60 L150 50 Z')
    + z('rect', '#8fc7e8', x=96, y=80, width=36, height=10, rx=2)
    + z('rect', '#f07a8a', x=100, y=70, width=30, height=10, rx=2)
    + bar('M50 130 L50 162', '#5b6b7a', 9, 3)
    + s('path', d='M26 174 L50 162 L74 174 M50 162 L50 176', stroke_width=4)
    + s('circle', '#5b6b7a', cx=26, cy=176, r=4, stroke_width=2) + s('circle', '#5b6b7a', cx=74, cy=176, r=4, stroke_width=2)
    + s('circle', '#5b6b7a', cx=50, cy=177, r=4, stroke_width=2)
    + bar('M42 112 L42 126', '#5b6b7a', 8, 3)
    + z('rect', '#7cc4b0', x=24, y=62, width=40, height=54, rx=12)
    + z('rect', '#7cc4b0', x=20, y=118, width=62, height=14, rx=6)
    + ground(16, 184, 182)
)

# 2. houseplant
ITEMS['houseplant'] = (
    s('path', d='M100 128 L70 84 M100 128 L132 78 M100 128 L96 52 M100 128 L56 112 M100 128 L148 108', stroke_width=3)
    + z('path', '#7cc4a0', d='M100 126 Q52 124 30 92 Q70 74 100 126 Z')
    + s('path', d='M94 120 Q66 104 44 94', stroke_width=2)
    + z('path', '#7cc4a0', d='M100 124 Q150 122 172 88 Q130 72 100 124 Z')
    + s('path', d='M106 118 Q134 104 158 90', stroke_width=2)
    + z('path', '#9ccf7a', d='M100 122 Q56 96 62 50 Q100 64 100 122 Z')
    + s('path', d='M98 114 Q78 88 70 60', stroke_width=2)
    + z('path', '#9ccf7a', d='M100 120 Q146 96 144 46 Q104 62 100 120 Z')
    + s('path', d='M104 112 Q124 88 136 58', stroke_width=2)
    + z('path', '#7cc4a0', d='M100 118 Q80 74 100 28 Q122 74 100 118 Z')
    + s('path', d='M100 110 L100 42', stroke_width=2)
    + z('path', '#f4f4f0', d='M68 138 L132 138 L124 180 L76 180 Z')
    + z('rect', '#f4f4f0', x=60, y=126, width=80, height=16, rx=4)
    + s('path', d='M72 154 L128 154', stroke='#7cc4b0', stroke_width=5)
    + s('path', d='M72 154 L128 154', stroke_width=1.5)
)

# 3. air-purifier
ITEMS['air-purifier'] = (
    z('rect', '#f4f4f0', x=62, y=48, width=76, height=128, rx=16)
    + s('rect', '#c9d3db', x=72, y=56, width=56, height=18, rx=5, stroke_width=2.5)
    + s('path', d='M80 60 L80 70 M90 60 L90 70 M100 60 L100 70 M110 60 L110 70 M120 60 L120 70', stroke_width=2)
    + dot(84, 86, 4, '#9ccf7a') + s('rect', '#8fc7e8', x=94, y=82, width=30, height=8, rx=4, stroke_width=2)
    + s('rect', '#c9d3db', x=74, y=100, width=52, height=62, rx=8, stroke_width=2.5)
    + ''.join(dot(x, y, 2.5) for x in (84, 95, 106, 117) for y in (110, 122, 134, 146))
    + s('path', d='M54 40 Q60 30 70 36 Q78 42 86 34', stroke='#8fc7e8', stroke_width=5)
    + s('path', d='M54 40 Q60 30 70 36 Q78 42 86 34', stroke_width=1.5)
    + s('path', d='M114 34 Q122 26 130 32 Q138 38 146 30', stroke='#8fc7e8', stroke_width=5)
    + s('path', d='M114 34 Q122 26 130 32 Q138 38 146 30', stroke_width=1.5)
    + z('path', '#9ccf7a', d='M158 72 Q160 54 176 52 Q176 70 158 72 Z')
    + z('path', '#9ccf7a', d='M30 92 Q28 74 44 70 Q46 88 30 92 Z')
    + s('rect', '#b9a99c', x=70, y=176, width=60, height=5, rx=2, stroke_width=2)
)

# 4. humidifier
ITEMS['humidifier'] = (
    z('circle', '#ffffff', cx=100, cy=44, r=13)
    + z('circle', '#ffffff', cx=80, cy=36, r=10)
    + z('circle', '#ffffff', cx=120, cy=34, r=11)
    + z('rect', '#f4f4f0', x=90, y=60, width=20, height=14, rx=4)
    + z('path', '#8fc7e8', d='M62 134 Q60 76 100 72 Q140 76 138 134 Z')
    + s('path', d='M66 108 Q83 102 100 108 Q117 114 134 108', stroke_width=2)
    + dot(88, 116) + dot(112, 116) + cheeks(78, 122, 125, 6, 3.5)
    + s('path', d='M95 124 Q100 129 105 124', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=54, y=132, width=92, height=44, rx=14)
    + s('circle', '#9ccf7a', cx=100, cy=154, r=8, stroke_width=2.5)
    + dot(76, 154, 3) + dot(124, 154, 3)
    + ground(40, 160, 182)
)

# 5. dishwasher
ITEMS['dishwasher'] = (
    z('rect', '#f4f4f0', x=44, y=30, width=112, height=114, rx=8)
    + s('path', d='M44 54 L156 54')
    + dot(118, 42, 3.5, '#9ccf7a') + dot(132, 42, 3) + dot(144, 42, 3)
    + s('rect', '#8fc7e8', x=56, y=37, width=40, height=10, rx=3, stroke_width=2)
    + s('rect', '#c9d3db', x=54, y=62, width=92, height=80, rx=4)
    + s('path', d='M58 92 L142 92 M58 132 L142 132', stroke_width=2.5)
    + z('rect', '#f6a6b8', x=64, y=74, width=14, height=16, rx=3)
    + z('rect', '#8fc7e8', x=86, y=74, width=14, height=16, rx=3)
    + z('rect', '#ffffff', x=108, y=78, width=28, height=12, rx=3)
    + z('ellipse', '#ffffff', cx=70, cy=114, rx=7, ry=20)
    + z('ellipse', '#8fc7e8', cx=88, cy=114, rx=7, ry=20)
    + z('ellipse', '#ffffff', cx=106, cy=114, rx=7, ry=20)
    + z('ellipse', '#f5d58a', cx=124, cy=114, rx=7, ry=20)
    + z('path', '#f4f4f0', d='M44 144 L156 144 L174 176 L26 176 Z')
    + s('path', d='M78 160 L122 160', stroke_width=5)
    + s('circle', '#ffffff', cx=150, cy=72, r=4, stroke_width=2)
    + s('circle', '#ffffff', cx=56, cy=104, r=3, stroke_width=2)
)

# 6. sewing-kit
ITEMS['sewing-kit'] = (
    z('path', '#f07a8a', d='M34 118 L42 66 Q44 58 52 58 L148 58 Q156 58 158 66 L166 118 Z')
    + s('path', '#f6a6b8', d='M48 110 L54 72 L146 72 L152 110 Z', stroke_width=2.5)
    + z('rect', '#d9a66b', x=48, y=86, width=28, height=6, rx=2)
    + z('rect', '#8fb3e0', x=52, y=92, width=20, height=26)
    + s('path', d='M52 100 L72 100 M52 108 L72 108', stroke_width=1.5)
    + z('rect', '#d9a66b', x=82, y=92, width=28, height=6, rx=2)
    + z('rect', '#ffe27a', x=86, y=98, width=20, height=22)
    + s('path', d='M86 106 L106 106 M86 114 L106 114', stroke_width=1.5)
    + s('path', d='M128 98 L122 76 M138 96 L142 72 M148 100 L158 82', stroke_width=2)
    + dot(122, 75, 4, '#8fc7e8') + dot(142, 71, 4, '#ffc94d') + dot(158, 81, 4, '#9ccf7a')
    + z('ellipse', '#e04b5a', cx=138, cy=110, rx=22, ry=16)
    + s('path', d='M138 96 L138 124 M124 102 Q130 112 124 120 M152 102 Q146 112 152 120', stroke_width=2)
    + z('rect', '#f6a6b8', x=28, y=118, width=144, height=58, rx=8)
    + s('path', d='M28 132 L172 132', stroke_width=2.5)
    + z('rect', '#f5d58a', x=88, y=126, width=24, height=14, rx=3)
    + s('path', d='M46 156 L74 156', stroke_width=2)
    + s('path', d='M120 150 Q136 170 156 154 Q170 144 164 164', stroke='#8fb3e0', stroke_width=3)
    + s('path', d='M108 160 L156 146', stroke_width=2.5)
    + s('ellipse', 'none', cx=154, cy=146.5, rx=3, ry=1.5, stroke_width=1.5)
)

# 7. ironing-board
ITEMS['ironing-board'] = (
    bar('M64 116 L140 178', '#c9d3db', 9, 3)
    + bar('M136 116 L60 178', '#c9d3db', 9, 3)
    + s('path', d='M50 180 L72 180 M128 180 L150 180', stroke_width=5)
    + z('path', '#8fb3e0', d='M24 100 Q24 92 32 92 L148 92 Q184 94 184 104 Q184 114 148 116 L32 116 Q24 116 24 108 Z')
    + ''.join(dot(x, y, 2.5, '#ffffff') for x, y in ((40, 100), (58, 108), (76, 100), (94, 108), (148, 100), (166, 106), (130, 108)))
    + z('path', '#f5d58a', d='M88 90 L92 74 Q94 66 104 66 L140 66 Q156 68 164 90 Z')
    + s('path', d='M88 84 L162 84', stroke_width=2)
    + bar('M104 66 Q104 48 116 48 L138 48 Q146 50 148 66', '#5b6b7a', 9, 3)
    + dot(126, 76, 3, '#e8735a')
    + s('path', d='M166 72 Q160 64 166 56 Q172 48 166 40', stroke_width=2.5)
    + s('path', d='M178 76 Q172 68 178 60', stroke_width=2.5)
    + bar('M88 76 Q70 66 74 44 Q78 30 64 26', '#5b6b7a', 6, 2)
)

# 8. coat-rack
ITEMS['coat-rack'] = (
    s('path', d='M100 168 L68 180 M100 168 L132 180 M100 168 L100 180', stroke_width=6)
    + s('path', d='M100 168 L68 180 M100 168 L132 180 M100 168 L100 180', stroke='#9a6a3f', stroke_width=2)
    + bar('M100 40 L100 170', '#9a6a3f', 11, 5)
    + bar('M100 56 Q80 52 76 42 M100 56 Q120 52 124 42', '#9a6a3f', 7, 2)
    + z('circle', '#9a6a3f', cx=100, cy=34, r=7)
    + z('path', '#e8735a', d='M76 46 Q90 50 92 64 L102 148 Q80 154 50 148 L58 64 Q62 50 76 46 Z')
    + z('path', '#d9a66b', d='M76 46 Q66 52 64 64 L76 92 L88 64 Q86 52 76 46 Z')
    + s('path', d='M76 92 L78 146', stroke_width=2.5)
    + dot(84, 104, 3) + dot(84, 120, 3) + dot(84, 136, 3)
    + s('path', d='M58 116 L72 116', stroke_width=2.5)
    + z('path', '#5b6b7a', d='M112 60 Q112 40 128 40 Q144 40 144 60 Z')
    + s('path', d='M112 54 L144 54', stroke='#e8735a', stroke_width=5)
    + z('ellipse', '#5b6b7a', cx=128, cy=61, rx=24, ry=6)
    + z('path', '#f5d58a', d='M116 70 L126 70 L130 128 L120 130 Z')
    + s('path', d='M121 122 L131 120 M120 114 L130 112', stroke_width=2)
)

# 9. storage-boxes
ITEMS['storage-boxes'] = (
    z('rect', '#d9a66b', x=26, y=116, width=74, height=60, rx=3)
    + s('path', d='M26 128 L100 128', stroke_width=2.5)
    + s('rect', '#f6e0c4', x=46, y=140, width=34, height=20, rx=2, stroke_width=2.5)
    + s('rect', '#9a6a3f', x=52, y=118, width=22, height=6, rx=3, stroke_width=2)
    + z('rect', '#8fc7e8', x=106, y=124, width=68, height=52, rx=6)
    + z('rect', '#7cc4b0', x=102, y=114, width=76, height=14, rx=4)
    + s('rect', '#ffffff', x=118, y=138, width=44, height=10, rx=5, stroke_width=2.5)
    + s('path', d='M114 160 L166 160', stroke_width=2)
    + z('rect', '#f5d58a', x=52, y=64, width=88, height=52, rx=3)
    + z('rect', '#f5b971', x=48, y=52, width=96, height=16, rx=3)
    + s('rect', '#9a6a3f', x=84, y=84, width=24, height=7, rx=3.5, stroke_width=2)
    + s('rect', '#f6e0c4', x=70, y=96, width=52, height=12, rx=2, stroke_width=2)
    + ground(16, 184, 180)
)

# 10. garden-hose
_coil = ''.join(
    s('ellipse', cx=84, cy=136, rx=rx, ry=ry, stroke_width=13)
    + s('ellipse', cx=84, cy=136, rx=rx, ry=ry, stroke='#7cc4a0', stroke_width=7)
    for rx, ry in ((56, 36), (40, 26), (24, 16))
)
ITEMS['garden-hose'] = (
    _coil
    + bar('M138 128 Q156 118 150 96 Q146 80 128 70', '#7cc4a0', 13, 7)
    + z('path', '#ffc94d', d='M134 76 L116 64 Q110 58 116 52 L120 50 Q126 46 132 52 L144 68 Z')
    + bar('M140 72 L150 80', '#5b6b7a', 8, 3)
    + z('rect', '#e8735a', x=112, y=42, width=12, height=14, rx=3)
    + ''.join(z('circle', '#8fc7e8', cx=x, cy=y, r=r) for x, y, r in ((98, 36, 5), (84, 28, 4), (86, 46, 4), (70, 38, 3.5), (100, 52, 3.5), (72, 54, 3)))
    + ground(20, 180, 180)
)

# 11. key-holder
def _key(x, top, color, h=36):
    return (s('path', d=f'M{x} {top - 12} L{x} {top - 4}', stroke_width=2.5)
            + s('circle', cx=x, cy=top, r=6, stroke_width=2.5)
            + z('circle', color, cx=x, cy=top + 16, r=12)
            + s('circle', '#fbf6ee', cx=x, cy=top + 14, r=3.5, stroke_width=2)
            + z('path', color, d=f'M{x - 4} {top + 27} L{x + 4} {top + 27} L{x + 4} {top + 27 + h} L{x - 4} {top + 27 + h} Z')
            + s('path', color, d=f'M{x + 4} {top + 27 + h - 16} L{x + 12} {top + 27 + h - 16} L{x + 12} {top + 27 + h - 10} L{x + 8} {top + 27 + h - 10} L{x + 8} {top + 27 + h - 4} L{x + 4} {top + 27 + h - 4}', stroke_width=2.5))


ITEMS['key-holder'] = (
    z('path', '#d9a66b', d='M32 96 L32 62 L100 30 L168 62 L168 96 Z')
    + s('circle', '#8fc7e8', cx=100, cy=60, r=9, stroke_width=2.5)
    + s('path', d='M100 51 L100 69 M91 60 L109 60', stroke_width=2)
    + s('path', d='M40 74 L160 74', stroke_width=2)
    + s('path', d='M56 96 L56 104 Q56 110 62 108 M100 96 L100 104 Q100 110 106 108 M144 96 L144 104 Q144 110 150 108', stroke_width=3)
    + _key(56, 116, '#ffc94d')
    + _key(100, 116, '#c9d3db', 30)
    + _key(144, 116, '#8fb3e0')
)

# 12. light-switch
ITEMS['light-switch'] = (
    z('rect', '#f4f4f0', x=44, y=40, width=84, height=124, rx=12)
    + s('circle', cx=86, cy=50, r=3, stroke_width=2) + s('circle', cx=86, cy=154, r=3, stroke_width=2)
    + s('rect', '#c9d3db', x=62, y=62, width=48, height=80, rx=6, stroke_width=2.5)
    + z('path', '#ffffff', d='M66 66 L106 66 L106 98 L66 106 Z')
    + z('path', '#ffffff', d='M66 108 L106 100 L106 138 L66 138 Z')
    + dot(86, 84, 3.5, '#9ccf7a')
    + z('rect', '#ffd9b8', x=96, y=112, width=58, height=16, rx=8)
    + z('path', '#ffd9b8', d='M140 108 Q166 104 176 120 Q180 146 156 152 Q136 152 134 134 Z')
    + s('path', d='M146 130 Q156 132 162 128 M146 142 Q156 144 162 140', stroke_width=2)
    + z('circle', '#ffe27a', cx=158, cy=52, r=14)
    + s('rect', '#b9a99c', x=152, y=66, width=12, height=8, rx=2, stroke_width=2.5)
    + s('path', d='M158 30 L158 26 M176 40 L181 36 M140 40 L135 36 M180 56 L185 56', stroke_width=2.5)
)

# 13. power-strip
ITEMS['power-strip'] = (
    s('path', d='M24 118 Q10 140 30 152 Q50 162 48 176', stroke_width=7)
    + s('path', d='M24 118 Q10 140 30 152 Q50 162 48 176', stroke='#f4f4f0', stroke_width=2)
    + z('rect', '#f4f4f0', x=24, y=98, width=154, height=40, rx=10)
    + ''.join(s('rect', '#c9d3db', x=x, y=106, width=24, height=24, rx=6, stroke_width=2.5)
              + s('path', d=f'M{x + 8} {y0} L{x + 8} {y0 + 8} M{x + 16} {y0} L{x + 16} {y0 + 8}', stroke_width=2.5)
              for x, y0 in ((34, 114), (64, 114), (124, 114)))
    + z('rect', '#e04b5a', x=154, y=108, width=14, height=20, rx=3)
    + s('path', d='M106 98 Q108 70 120 54 Q134 36 128 22', stroke_width=7)
    + s('path', d='M106 98 Q108 70 120 54 Q134 36 128 22', stroke='#5b6b7a', stroke_width=2)
    + z('rect', '#5b6b7a', x=92, y=96, width=28, height=34, rx=5)
    + s('path', d='M98 122 L114 122', stroke='#c9d3db', stroke_width=2)
)

# 14. smoke-alarm
ITEMS['smoke-alarm'] = (
    s('path', d='M20 34 L180 34', stroke_width=2.5)
    + z('rect', '#c9d3db', x=72, y=34, width=56, height=10, rx=2)
    + z('circle', '#f4f4f0', cx=100, cy=100, r=56)
    + s('circle', cx=100, cy=100, r=42, stroke_width=2.5)
    + s('path', d='M64 88 L80 88 M120 88 L136 88 M62 100 L78 100 M122 100 L138 100 M64 112 L80 112 M120 112 L136 112', stroke_width=2.5)
    + z('circle', '#c9d3db', cx=100, cy=100, r=14)
    + dot(100, 74, 4, '#e04b5a')
    + s('path', d='M32 80 Q24 100 32 120 M22 72 Q10 100 22 128', stroke_width=2.5)
    + s('path', d='M168 80 Q176 100 168 120 M178 72 Q190 100 178 128', stroke_width=2.5)
    + s('path', '#c9d3db', d='M92 180 Q80 172 88 164 Q78 154 92 150 Q100 144 108 152 Q120 150 116 162 Q124 172 110 176 Q102 184 92 180 Z', stroke_width=2.5)
)

# 15. fire-extinguisher
ITEMS['fire-extinguisher'] = (
    bar('M114 58 Q154 58 150 104 L150 140', '#5b6b7a', 10, 4)
    + z('path', '#5b6b7a', d='M144 138 L156 138 L154 164 L146 164 Z')
    + z('rect', '#c9d3db', x=88, y=54, width=26, height=20, rx=3)
    + bar('M88 50 L58 38', '#5b6b7a', 9, 3)
    + bar('M90 58 L62 58', '#5b6b7a', 9, 3)
    + s('circle', '#ffe27a', cx=82, cy=44, r=5, stroke_width=2)
    + z('circle', '#ffffff', cx=122, cy=48, r=8)
    + s('path', d='M122 48 L126 44', stroke_width=2)
    + z('path', '#e04b5a', d='M72 100 Q72 70 101 70 Q130 70 130 100 L130 172 Q130 178 124 178 L78 178 Q72 178 72 172 Z')
    + s('rect', '#f4f4f0', x=82, y=110, width=38, height=40, rx=4, stroke_width=2.5)
    + s('path', d='M90 122 L112 122 M90 132 L112 132 M90 142 L104 142', stroke_width=2)
    + s('path', d='M72 164 L130 164', stroke_width=2.5)
)

# 16. bath-towel-robe
ITEMS['bath-towel-robe'] = (
    s('path', d='M100 42 L100 32 Q100 24 107 24 Q114 24 112 32', stroke_width=3)
    + z('path', '#8fc7e8', d='M74 46 L126 46 L160 66 L180 108 L160 118 L146 96 L148 178 L52 178 L54 96 L40 118 L20 108 L40 66 Z')
    + z('path', '#ffffff', d='M74 46 Q86 50 100 46 Q114 50 126 46 L118 76 L100 126 L82 76 Z')
    + s('path', d='M86 58 L100 116 M114 58 L100 112', stroke_width=2.5)
    + s('path', d='M100 116 L130 176', stroke_width=2.5)
    + z('rect', '#ffffff', x=26, y=104, width=20, height=14, rx=4)
    + z('rect', '#ffffff', x=154, y=104, width=20, height=14, rx=4)
    + z('rect', '#ffffff', x=54, y=120, width=94, height=12, rx=4)
    + z('path', '#ffffff', d='M88 130 L80 162 L90 164 L96 132 Z')
    + z('path', '#ffffff', d='M100 130 L104 160 L114 158 L108 130 Z')
    + z('ellipse', '#ffffff', cx=98, cy=126, rx=9, ry=8)
    + s('rect', '#8fc7e8', x=62, y=142, width=18, height=20, rx=3, stroke_width=2.5)
)

# 17. bunk-bed
ITEMS['bunk-bed'] = (
    z('rect', '#d9a66b', x=28, y=32, width=12, height=148, rx=3)
    + z('rect', '#d9a66b', x=160, y=40, width=12, height=140, rx=3)
    + s('path', d='M40 48 L120 48 M40 60 L120 60', stroke_width=5)
    + s('path', d='M40 48 L120 48 M40 60 L120 60', stroke='#d9a66b', stroke_width=1.5)
    + z('ellipse', '#ffffff', cx=56, cy=72, rx=14, ry=8)
    + z('rect', '#8fc7e8', x=70, y=66, width=90, height=16, rx=6)
    + dot(92, 74, 2.5, '#ffffff') + dot(116, 74, 2.5, '#ffffff') + dot(140, 74, 2.5, '#ffffff')
    + z('rect', '#d9a66b', x=34, y=82, width=134, height=14, rx=3)
    + z('ellipse', '#ffffff', cx=56, cy=140, rx=14, ry=8)
    + z('rect', '#f5d58a', x=70, y=134, width=90, height=16, rx=6)
    + dot(92, 142, 2.5, '#ffffff') + dot(116, 142, 2.5, '#ffffff') + dot(140, 142, 2.5, '#ffffff')
    + z('rect', '#d9a66b', x=34, y=150, width=134, height=14, rx=3)
    + s('path', d='M130 50 L130 180 M150 50 L150 180', stroke_width=7)
    + s('path', d='M130 50 L130 180 M150 50 L150 180', stroke='#9a6a3f', stroke_width=2)
    + s('path', d='M130 104 L150 104 M130 124 L150 124 M130 70 L150 70', stroke_width=4)
    + ground(16, 184, 182)
)

# 18. baby-crib
ITEMS['baby-crib'] = (
    bar('M156 70 L156 36 Q156 28 148 28 L104 28', '#d9a66b', 8, 3)
    + s('path', d='M104 28 L104 36 M84 38 L124 38', stroke_width=2.5)
    + s('path', d='M84 38 L84 50 M124 38 L124 46 M104 38 L104 54', stroke_width=2)
    + z('circle', '#ffe27a', cx=84, cy=56, r=6)
    + z('path', '#f6a6b8', d='M118 48 L130 48 Q132 56 124 58 Q116 56 118 48 Z')
    + z('circle', '#8fc7e8', cx=104, cy=60, r=6)
    + z('rect', '#ffffff', x=38, y=112, width=124, height=20, rx=4)
    + z('ellipse', '#ffffff', cx=58, cy=104, rx=14, ry=8)
    + z('path', '#f6a6b8', d='M78 112 Q78 98 92 98 L150 98 Q160 98 160 112 Z')
    + ''.join(s('path', d=f'M{x} 82 L{x} 150', stroke_width=3) for x in range(48, 160, 14))
    + z('rect', '#f5d58a', x=26, y=60, width=12, height=118, rx=4)
    + z('rect', '#f5d58a', x=162, y=60, width=12, height=118, rx=4)
    + z('rect', '#f5d58a', x=34, y=76, width=132, height=10, rx=3)
    + z('rect', '#f5d58a', x=34, y=146, width=132, height=10, rx=3)
    + ground(16, 184, 182)
)

# 19. pet-bed
ITEMS['pet-bed'] = (
    z('ellipse', '#8fb3e0', cx=96, cy=126, rx=74, ry=40)
    + z('ellipse', '#f6e0c4', cx=96, cy=122, rx=54, ry=22)
    + z('path', '#8fb3e0', d='M22 126 Q22 168 96 170 Q170 168 170 126 Q166 146 96 148 Q26 146 22 126 Z')
    + z('path', '#ffffff', d='M70 118 L108 112 Q112 104 118 108 Q122 112 118 116 Q124 118 120 124 Q116 128 110 122 L72 128 Q68 136 62 132 Q58 128 62 124 Q56 120 60 116 Q64 112 70 118 Z')
    + dot(62, 156, 3, '#ffffff') + dot(56, 150, 2, '#ffffff') + dot(62, 148, 2, '#ffffff') + dot(68, 150, 2, '#ffffff')
    + dot(130, 156, 3, '#ffffff') + dot(124, 150, 2, '#ffffff') + dot(130, 148, 2, '#ffffff') + dot(136, 150, 2, '#ffffff')
    + z('circle', '#e04b5a', cx=162, cy=166, r=13)
    + s('path', d='M150 162 Q162 156 174 162 M152 172 Q162 178 172 172', stroke='#ffffff', stroke_width=3)
    + ground(16, 184, 180)
)

# 20. doormat
ITEMS['doormat'] = (
    z('rect', '#8b6b4f', x=58, y=26, width=84, height=96, rx=3)
    + s('rect', '#9a6a3f', x=68, y=36, width=64, height=34, rx=2, stroke_width=2.5)
    + s('rect', '#9a6a3f', x=68, y=78, width=64, height=36, rx=2, stroke_width=2.5)
    + z('circle', '#ffc94d', cx=128, cy=76, r=5)
    + s('path', d='M20 122 L180 122', stroke_width=2.5)
    + z('path', '#d9a66b', d='M44 132 L156 132 L176 176 L24 176 Z')
    + s('path', '#9a6a3f', d='M54 140 L146 140 L160 168 L40 168 Z', stroke_width=2.5)
    + s('path', '#f5b971', d='M60 146 L140 146 L150 162 L50 162 Z', stroke='none')
    + s('path', '#e8735a', d='M100 160 C92 155 88 152 90 148 C92 145 98 146 100 149 C102 146 108 145 110 148 C112 152 108 155 100 160 Z', stroke_width=2)
    + s('path', '#9ccf7a', d='M70 154 Q78 146 86 154 Q78 160 70 154 Z', stroke_width=2)
    + s('path', '#9ccf7a', d='M114 154 Q122 146 130 154 Q122 160 114 154 Z', stroke_width=2)
)
