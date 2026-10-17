from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def hand(x, y, r=8, c=SK):
    return z('circle', c, cx=x, cy=y, r=r)


def arm(d, color, w=14):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=w - 6)


def peak_cap(cx, cy, crown, band, visor='#2b2220'):
    return (z('path', crown, d=f'M{cx-30} {cy-26} L{cx-42} {cy-48} Q{cx} {cy-64} {cx+42} {cy-48} L{cx+30} {cy-26}Z')
            + z('rect', band, x=cx - 32, y=cy - 34, width=64, height=11, rx=3)
            + z('path', visor, d=f'M{cx-32} {cy-24} Q{cx} {cy-8} {cx+32} {cy-24} Q{cx} {cy-18} {cx-32} {cy-24}Z'))


def soft_cap(cx, cy, color, brim=None):
    brim = brim or color
    return (z('path', color, d=f'M{cx-35} {cy-12} Q{cx-34} {cy-48} {cx} {cy-48} Q{cx+34} {cy-48} {cx+35} {cy-12}Z')
            + z('path', brim, d=f'M{cx-38} {cy-14} Q{cx} {cy+2} {cx+38} {cy-14} Q{cx} {cy-22} {cx-38} {cy-14}Z'))


def bow_tie(cx, cy, c):
    return s('path', c, d=f'M{cx} {cy} L{cx-11} {cy-7} L{cx-11} {cy+7}Z M{cx} {cy} L{cx+11} {cy-7} L{cx+11} {cy+7}Z', stroke_width=2.5)


def tie(cx, top, c):
    return s('path', c, d=f'M{cx-5} {top} L{cx+5} {top} L{cx+4} {top+6} L{cx+7} {top+30} L{cx} {top+38} L{cx-7} {top+30} L{cx-4} {top+6}Z', stroke_width=2.5)


def collar_v(cx, top, c='#ffffff'):
    return s('path', c, d=f'M{cx-14} {top} L{cx} {top+26} L{cx+14} {top}Z', stroke_width=2.5)


# 1. police officer saluting
HR = '#2b2220'
ITEMS['police-officer'] = (
    body('#5b6b7a')
    + collar_v(100, 137, '#8fb3e0') + tie(100, 140, '#2b2220')
    + s('path', '#ffe27a', d='M118 150 L130 150 L130 160 Q124 166 118 160Z', stroke_width=2.5)
    + face(100, 100, SK, HR, 'smile')
    + peak_cap(100, 100, '#5b6b7a', '#2b2220')
    + s('path', '#ffe27a', d='M100 46 L104 54 L100 60 L96 54Z', stroke_width=2)
    + arm('M72 154 Q46 134 54 82', '#5b6b7a')
    + hand(60, 76, 9)
)

# 2. pilot
HR = '#5a4033'
ITEMS['pilot'] = (
    body('#5b6b7a')
    + collar_v(100, 137) + tie(100, 140, '#5b6b7a')
    + s('path', d='M66 160 L80 160 M64 168 L80 168', stroke='#ffe27a', stroke_width=3)
    + s('path', d='M134 160 L120 160 M136 168 L120 168', stroke='#ffe27a', stroke_width=3)
    + face(100, 100, SK, HR, 'smile')
    + peak_cap(100, 100, '#ffffff', '#5b6b7a')
    + s('path', '#ffe27a', d='M86 70 Q93 64 100 70 Q107 64 114 70 Q107 74 100 72 Q93 74 86 70Z', stroke_width=2)
    + z('path', '#f4f4f0', d='M140 40 Q140 34 150 34 L180 34 Q188 36 190 40 Q188 44 180 46 L150 46 Q140 46 140 40Z')
    + z('path', '#8fc7e8', d='M162 40 L150 56 L158 56 L172 40Z')
    + s('path', '#8fc7e8', d='M146 36 L142 26 L148 26 L154 34Z', stroke_width=2.5)
    + s('path', d='M120 52 L132 46 M118 62 L130 58', stroke_width=2)
)

# 3. flight attendant
HR = '#2b2220'
ITEMS['flight-attendant'] = (
    z('circle', HR, cx=74, cy=78, r=12)
    + body('#8fb3e0', cx=88)
    + s('path', d='M88 140 L88 186', stroke_width=2.5)
    + dot(82, 160, 2.5) + dot(82, 174, 2.5)
    + face(88, 100, SK, HR, 'smile')
    + z('path', '#8fb3e0', d='M70 70 Q72 56 88 56 Q104 56 106 70Z')
    + s('path', d='M70 70 L106 70', stroke='#e8735a', stroke_width=3)
    + z('path', '#e8735a', d='M70 134 Q88 144 106 134 L104 142 Q88 150 72 142Z')
    + z('path', '#e8735a', d='M98 140 L114 152 L106 158 Z')
    + z('path', '#e8735a', d='M98 140 L112 136 L110 146Z')
    + s('path', d='M150 120 L150 94 L166 94 L166 120', stroke_width=4)
    + z('rect', '#f5b971', x=134, y=118, width=48, height=56, rx=6)
    + s('path', d='M146 126 L146 166 M170 126 L170 166', stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=144, cy=180, r=5) + z('circle', '#5b6b7a', cx=172, cy=180, r=5)
    + arm('M118 156 Q134 120 150 96', '#8fb3e0', 12)
    + hand(152, 96)
)

# 4. train conductor with whistle
HR = '#5a4033'
ITEMS['train-conductor'] = (
    body('#5b6b7a')
    + collar_v(100, 137) + tie(100, 140, '#e04b5a')
    + dot(86, 162, 3, '#ffe27a') + dot(86, 176, 3, '#ffe27a')
    + face(100, 100, SK, HR, 'smile')
    + peak_cap(100, 100, '#5b6b7a', '#e04b5a')
    + s('path', d='M110 128 Q124 140 120 152', stroke='#e04b5a', stroke_width=2)
    + z('rect', '#c9d3db', x=100, y=112, width=24, height=12, rx=5)
    + dot(116, 118, 3, '#5b6b7a')
    + arm('M128 156 Q150 140 134 124', '#5b6b7a')
    + hand(132, 122)
    + s('path', d='M144 104 L156 96 M148 116 L162 114 M146 128 L158 132', stroke_width=2.5)
)

# 5. bus driver at the wheel
HR = '#2b2220'
ITEMS['bus-driver'] = (
    z('rect', '#8fc7e8', x=26, y=30, width=148, height=100, rx=10)
    + s('path', d='M26 70 L174 70', stroke='#ffffff', stroke_width=0)
    + body('#8fb3e0', top=126)
    + collar_v(100, 127) + tie(100, 130, '#5b6b7a')
    + face(100, 88, SK, HR, 'smile')
    + peak_cap(100, 88, '#8fb3e0', '#5b6b7a')
    + s('circle', cx=100, cy=158, r=34, stroke_width=13)
    + s('circle', cx=100, cy=158, r=34, stroke='#5b6b7a', stroke_width=7)
    + s('path', d='M66 158 L134 158 M100 158 L100 190', stroke_width=7)
    + z('circle', '#5b6b7a', cx=100, cy=158, r=10)
    + hand(68, 140, 9) + hand(132, 140, 9)
)

# 6. taxi driver with cap
HR = '#2b2220'
ITEMS['taxi-driver'] = (
    z('rect', '#e8735a', x=140, y=56, width=26, height=14, rx=4)
    + z('path', '#ffe27a', d='M108 112 L120 74 Q122 68 130 68 L176 68 Q184 68 186 74 L186 168 L108 168Z')
    + s('path', '#8fc7e8', d='M124 106 L132 80 L172 80 L172 106Z', stroke_width=2.5)
    + s('path', d='M110 132 L186 132', stroke_width=2.5)
    + s('rect', '#2b2220', x=148, y=140, width=14, height=5, rx=2, stroke_width=0)
    + z('circle', '#5b6b7a', cx=164, cy=170, r=14) + s('circle', '#c9d3db', cx=164, cy=170, r=5, stroke_width=2)
    + body('#5b6b7a', cx=70)
    + collar_v(70, 137) + tie(70, 140, '#e8735a')
    + face(70, 100, SK, HR, 'smile')
    + peak_cap(70, 100, '#5b6b7a', '#2b2220')
    + arm('M98 156 Q116 150 120 128', '#5b6b7a')
    + hand(120, 124, 9, '#ffffff')
)

# 7. mail carrier with letter bag
HR = '#5a4033'
ITEMS['mail-carrier'] = (
    body('#8fb3e0')
    + s('path', d='M74 144 L130 178', stroke='#8b6b4f', stroke_width=8)
    + face(100, 100, SK, HR, 'smile')
    + soft_cap(100, 100, '#e8735a')
    + z('path', '#d9a66b', d='M112 150 L170 150 L170 182 Q170 186 166 186 L116 186 Q112 186 112 182Z')
    + z('path', '#d9a66b', d='M110 150 L172 150 L170 166 Q141 172 112 166Z')
    + z('rect', '#ffffff', x=40, y=118, width=40, height=28, rx=3)
    + s('path', d='M40 120 L60 134 L80 120', stroke_width=2.5)
    + hand(70, 150)
)

# 8. carpenter with saw and plank
HR = '#2b2220'
ITEMS['carpenter'] = (
    body('#f5d58a')
    + s('path', '#8b6b4f', d='M76 150 L124 150 L126 186 L74 186Z', stroke_width=2.5)
    + face(100, 96, SK, HR, 'smile')
    + z('path', '#f6e0c4', d='M66 74 Q100 62 134 74 L134 84 Q100 72 66 84Z')
    + z('path', '#f6e0c4', d='M134 76 L148 66 L150 80Z')
    + z('rect', '#d9a66b', x=22, y=164, width=156, height=16, rx=2)
    + s('path', d='M40 172 L56 172 M120 170 L140 170', stroke='#9a6a3f', stroke_width=2)
    + z('path', '#c9d3db', d='M132 102 L172 110 L130 168 L112 156Z')
    + s('path', d='M132 102 L128 106 L130 110 L126 114 L128 118 L124 122 L126 126 L122 130 L124 134 L120 138 L122 142 L118 146 L120 150 L114 154', stroke_width=2)
    + z('path', '#9a6a3f', d='M150 88 L184 96 L176 116 L146 106Z')
    + s('path', '#f6e0c4', d='M156 96 L174 100 L170 108 L154 104Z', stroke_width=2)
    + hand(162, 112)
)

# 9. electrician with tools and cable
HR = '#5a4033'
ITEMS['electrician'] = (
    body('#8fb3e0')
    + z('rect', '#d9a66b', x=66, y=164, width=68, height=12, rx=2)
    + s('rect', '#5b6b7a', x=74, y=160, width=10, height=22, rx=2, stroke_width=2.5)
    + s('rect', '#e04b5a', x=114, y=158, width=8, height=24, rx=2, stroke_width=2.5)
    + face(100, 100, SK, HR, 'smile')
    + z('path', '#ffe27a', d='M64 84 Q64 52 100 50 Q136 52 136 84Z')
    + s('path', d='M100 52 L100 82', stroke_width=2.5)
    + z('path', '#ffe27a', d='M56 84 Q100 76 144 84 Q146 92 138 92 L62 92 Q54 92 56 84Z')
    + s('path', d='M150 150 Q190 120 160 100 Q130 84 150 64 Q164 52 174 60', stroke_width=9)
    + s('path', d='M150 150 Q190 120 160 100 Q130 84 150 64 Q164 52 174 60', stroke='#e8735a', stroke_width=4)
    + z('rect', '#f4f4f0', x=168, y=48, width=16, height=20, rx=3)
    + s('path', d='M172 48 L172 40 M180 48 L180 40', stroke_width=3)
    + hand(146, 152)
    + s('path', d='M32 120 L60 140', stroke_width=7) + s('path', d='M32 120 L60 140', stroke='#e04b5a', stroke_width=2)
    + s('path', d='M24 104 L32 120 L40 106', stroke_width=3)
    + hand(58, 142)
)

# 10. plumber with wrench and pipe
HR = '#5a4033'
ITEMS['plumber'] = (
    body('#f5d58a')
    + s('path', '#7cc4b0', d='M76 186 L76 152 L124 152 L124 186Z')
    + s('path', d='M78 152 L82 138 M122 152 L118 138', stroke_width=3)
    + face(100, 100, SK, HR, 'smile')
    + soft_cap(100, 100, '#7cc4b0')
    + z('path', '#c9d3db', d='M20 70 L48 70 L48 120 L36 120 L36 82 L20 82Z')
    + z('rect', '#b9a99c', x=30, y=116, width=24, height=10, rx=2)
    + z('path', '#8fc7e8', d='M42 134 Q36 144 42 148 Q48 144 42 134Z')
    + z('path', '#8fc7e8', d='M42 156 Q37 164 42 168 Q47 164 42 156Z')
    + s('path', d='M130 160 L164 112', stroke_width=12) + s('path', d='M130 160 L164 112', stroke='#c9d3db', stroke_width=6)
    + z('path', '#c9d3db', d='M154 112 Q150 94 166 90 L170 100 L162 104 L170 112 L180 104 Q182 120 166 120Z')
    + hand(132, 158)
)

# 11. house painter with roller and bucket
HR = '#2b2220'
ITEMS['house-painter'] = (
    z('rect', '#f5d58a', x=18, y=30, width=36, height=126, rx=4)
    + body('#ffffff', cx=104)
    + s('path', '#ffffff', d='M82 186 L82 150 L126 150 L126 186Z', stroke_width=2.5)
    + dot(90, 166, 4, '#8fc7e8') + dot(116, 176, 3, '#f6a6b8') + dot(112, 160, 3, '#8fc7e8')
    + face(104, 100, SK, HR, 'smile')
    + soft_cap(104, 100, '#ffffff')
    + s('path', d='M74 154 L54 58', stroke_width=5)
    + s('path', d='M54 58 L44 58 L44 44', stroke_width=4)
    + z('rect', '#8fc7e8', x=26, y=30, width=36, height=16, rx=6)
    + hand(74, 154)
    + z('path', '#c9d3db', d='M142 146 L176 146 L172 184 L146 184Z')
    + s('path', d='M142 146 Q159 128 176 146', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M142 146 L176 146 L175 154 Q166 160 159 152 Q152 160 143 154Z', stroke_width=2)
)

# 12. gardener with shears and hedge
HR = '#5a4033'
ITEMS['gardener'] = (
    z('path', '#7cc4a0', d='M20 184 L20 100 Q20 80 40 82 Q48 64 66 74 Q82 70 86 88 Q90 100 86 120 L86 184Z')
    + s('path', d='M34 108 Q38 102 44 106 M58 98 Q62 92 68 96 M40 140 Q44 134 50 138 M66 128 Q70 122 76 126 M36 166 Q40 160 46 164 M62 160 Q66 154 72 158', stroke_width=2)
    + body('#f5b971', cx=124)
    + s('path', '#9ccf7a', d='M102 150 L146 150 L148 186 L100 186Z', stroke_width=2.5)
    + face(124, 100, SK, HR, 'smile')
    + z('ellipse', '#f5d58a', cx=124, cy=74, rx=50, ry=10)
    + z('path', '#f5d58a', d='M98 74 Q98 46 124 46 Q150 46 150 74Z')
    + s('path', '#e8735a', d='M99 66 Q124 60 149 66 L150 72 Q124 66 98 72Z', stroke_width=2)
    + s('path', d='M110 156 L74 128 M110 160 L76 144', stroke_width=7)
    + s('path', d='M110 156 L74 128 M110 160 L76 144', stroke='#c9d3db', stroke_width=2.5)
    + s('path', d='M110 156 L134 168 M110 160 L132 176', stroke_width=8)
    + s('path', d='M110 156 L134 168 M110 160 L132 176', stroke='#e04b5a', stroke_width=3)
    + hand(136, 170)
    + s('path', '#9ccf7a', d='M58 120 Q66 116 64 108 Q56 112 58 120Z', stroke_width=2)
)

# 13. fisherman holding a fish
HR = '#2b2220'
ITEMS['fisherman'] = (
    body('#ffe27a')
    + face(100, 96, SK, HR, 'open')
    + z('path', '#ffe27a', d='M66 80 Q66 50 100 48 Q134 50 134 80Z')
    + z('path', '#ffe27a', d='M56 78 Q100 70 144 78 Q156 90 148 94 Q100 84 52 94 Q44 90 56 78Z')
    + z('path', '#8fc7e8', d='M36 150 Q60 124 104 128 Q136 132 150 148 L176 130 L172 154 L178 176 L150 160 Q128 178 96 176 Q56 174 36 150Z')
    + s('path', d='M120 132 Q128 152 118 172', stroke_width=2.5)
    + dot(54, 146, 3.5) + s('path', d='M40 154 L48 156', stroke_width=2.5)
    + s('path', d='M74 140 Q80 136 86 140 M86 156 Q92 152 98 156', stroke='#5b6b7a', stroke_width=2)
    + hand(76, 172) + hand(132, 162)
)

# 14. baker holding a tray of bread
HR = '#c9a36b'
ITEMS['baker'] = (
    body('#ffffff')
    + face(100, 100, SK, HR, 'smile')
    + z('path', '#ffffff', d='M72 70 Q54 52 72 40 Q80 26 100 32 Q120 26 128 40 Q146 52 128 70Z')
    + z('rect', '#ffffff', x=70, y=62, width=60, height=12, rx=3)
    + z('ellipse', '#d9a66b', cx=66, cy=146, rx=22, ry=12)
    + s('path', d='M56 140 L60 150 M66 138 L70 148 M76 140 L80 150', stroke='#9a6a3f', stroke_width=2.5)
    + z('ellipse', '#f5b971', cx=108, cy=144, rx=18, ry=14)
    + s('path', d='M100 138 Q108 134 116 138', stroke='#9a6a3f', stroke_width=2.5)
    + z('path', '#d9a66b', d='M130 152 Q132 126 150 128 Q168 126 168 152Z')
    + s('path', d='M140 140 L144 134 M150 140 L154 134 M160 142 L162 136', stroke='#9a6a3f', stroke_width=2.5)
    + z('rect', '#b9a99c', x=34, y=154, width=144, height=10, rx=3)
    + hand(44, 168) + hand(166, 168)
)

# 15. barista making a latte
HR = '#2b2220'
ITEMS['barista'] = (
    body('#f4f4f0', cx=88)
    + s('path', '#8b6b4f', d='M66 152 L110 152 L112 186 L64 186Z', stroke_width=2.5)
    + s('path', d='M70 152 L74 138 M106 152 L102 138', stroke='#8b6b4f', stroke_width=3)
    + face(88, 100, SK, HR, 'smile')
    + s('path', HR, d='M60 92 Q56 72 70 70 Q58 82 62 96Z', stroke_width=2)
    + z('path', '#ffffff', d='M120 132 L160 132 L156 172 Q140 180 124 172Z')
    + s('path', d='M159 140 Q174 142 172 154 Q170 164 157 162', stroke_width=3)
    + s('ellipse', '#d9a66b', cx=140, cy=134, rx=19, ry=5, stroke_width=2.5)
    + s('path', '#ffffff', d='M140 138 C136 135 133 132 136 130 C138 129 140 130 140 132 C140 130 142 129 144 130 C147 132 144 135 140 138Z', stroke_width=1.5)
    + z('path', '#c9d3db', d='M118 72 L150 72 L152 104 Q146 110 136 108 L116 112 L122 100Z')
    + s('path', d='M150 78 Q164 82 158 98', stroke_width=3)
    + s('path', d='M118 110 Q124 122 132 130', stroke='#ffffff', stroke_width=5)
    + s('path', d='M118 110 Q124 122 132 130', stroke_width=0)
    + hand(154, 92)
)

# 16. waiter carrying a tray
HR = '#5a4033'
ITEMS['waiter'] = (
    body('#ffffff', cx=88)
    + s('path', '#2b2220', d='M58 186 Q60 146 74 140 L88 170 L102 140 Q116 146 118 186Z', stroke_width=2.5)
    + bow_tie(88, 140, '#e04b5a')
    + face(88, 100, SK, HR, 'smile')
    + s('path', d='M112 156 Q138 150 142 96', stroke_width=14)
    + s('path', d='M112 156 Q138 150 142 96', stroke='#ffffff', stroke_width=8)
    + hand(142, 92)
    + z('ellipse', '#c9d3db', cx=142, cy=84, rx=34, ry=7)
    + z('path', '#ffffff', d='M124 54 L148 54 L146 76 Q136 80 126 76Z')
    + s('path', d='M147 60 Q158 62 156 70 Q154 74 146 72', stroke_width=2.5)
    + s('path', d='M130 46 Q126 40 130 34 M140 46 Q136 40 140 34', stroke_width=2)
    + s('rect', '#ffffff', x=40, y=148, width=18, height=26, rx=2, stroke_width=2.5)
)

# 17. cashier at a register
HR = '#5a4033'
ITEMS['cashier'] = (
    body('#7cc4b0', cx=70, top=122, bottom=170)
    + face(70, 86, SK, HR, 'smile')
    + z('rect', '#c9d3db', x=104, y=110, width=64, height=48, rx=6)
    + z('rect', '#5b6b7a', x=116, y=66, width=40, height=30, rx=4)
    + s('rect', '#8fc7e8', x=121, y=71, width=30, height=20, rx=2, stroke_width=2)
    + s('path', d='M136 96 L136 110', stroke_width=5)
    + ''.join(dot(x, y, 3.5, '#5b6b7a') for x in (118, 130, 142, 154) for y in (122, 134))
    + s('rect', '#ffffff', x=114, y=144, width=44, height=8, rx=2, stroke_width=2)
    + z('rect', '#d9a66b', x=20, y=158, width=164, height=26, rx=3)
    + hand(98, 132)
    + s('path', d='M78 140 Q90 140 96 134', stroke_width=0)
)

# 18. shop clerk bowing behind a counter
HR = '#2b2220'
ITEMS['shop-clerk'] = (
    z('path', '#f6a6b8', d='M60 150 Q62 108 100 102 Q138 108 140 150Z')
    + z('circle', SK, cx=100, cy=106, r=32)
    + s('path', HR, d='M68 104 Q66 70 100 68 Q134 70 132 104 Q116 92 100 92 Q84 92 68 104Z')
    + s('path', d='M84 114 Q89 118 94 114 M106 114 Q111 118 116 114', stroke_width=2.5)
    + cheeks(80, 120, 124, 6, 3.5)
    + s('path', d='M96 128 Q100 131 104 128', stroke_width=2.5)
    + s('path', d='M54 86 Q50 78 52 70 M146 86 Q150 78 148 70 M44 98 Q38 92 36 84 M156 98 Q162 92 164 84', stroke_width=2.5)
    + z('rect', '#d9a66b', x=24, y=146, width=152, height=38, rx=3)
    + s('path', d='M24 156 L176 156', stroke_width=2.5)
    + hand(88, 150, 8) + hand(112, 150, 8)
    + z('path', '#9ccf7a', d='M150 146 L150 130 Q150 122 158 122 Q166 122 166 130 L166 146Z')
)

# 19. hairdresser with scissors and comb
HR = '#c9a36b'
ITEMS['hairdresser'] = (
    z('path', HR, d='M64 100 Q58 136 70 142 L130 142 Q142 136 136 100Z')
    + body('#f4f4f0')
    + s('path', '#5b6b7a', d='M76 150 L124 150 L126 186 L74 186Z', stroke_width=2.5)
    + s('path', d='M78 150 L84 138 M122 150 L116 138', stroke='#5b6b7a', stroke_width=3)
    + face(100, 100, SK, HR, 'smile')
    + hand(146, 150)
    + s('path', d='M150 124 L178 74', stroke_width=7) + s('path', d='M150 124 L178 74', stroke='#c9d3db', stroke_width=3)
    + s('path', d='M150 124 L186 86', stroke_width=7) + s('path', d='M150 124 L186 86', stroke='#c9d3db', stroke_width=3)
    + s('path', d='M150 124 L140 140 M150 124 L156 142', stroke_width=4)
    + s('circle', '#e8735a', cx=138, cy=146, r=7, stroke_width=3) + s('circle', '#e8735a', cx=158, cy=148, r=7, stroke_width=3)
    + s('circle', '#ffffff', cx=138, cy=146, r=2.5, stroke_width=2) + s('circle', '#ffffff', cx=158, cy=148, r=2.5, stroke_width=2)
    + dot(150, 124, 3)
    + z('rect', '#8fc7e8', x=24, y=96, width=40, height=12, rx=3)
    + s('path', d='M30 108 L30 120 M37 108 L37 120 M44 108 L44 120 M51 108 L51 120 M58 108 L58 120', stroke_width=2.5)
    + hand(64, 124)
)

# 20. florist holding a flower bucket
HR = '#5a4033'
FL = '#7cc4a0'


def flower(x, y, c, r=9):
    return z('circle', c, cx=x, cy=y, r=r) + dot(x, y, 3.5, '#ffe27a')


ITEMS['florist'] = (
    body('#f6e0c4', cx=76)
    + s('path', FL, d='M54 152 L98 152 L100 186 L52 186Z', stroke_width=2.5)
    + face(76, 100, SK, HR, 'smile')
    + s('path', HR, d='M42 98 Q36 130 48 136 Q50 116 46 100Z', stroke_width=2.5)
    + s('path', d='M128 132 L120 92 M138 132 L138 84 M148 132 L158 90 M134 132 L130 72 M144 132 L148 74', stroke='#7cc4a0', stroke_width=3)
    + flower(120, 90, '#f6a6b8') + flower(160, 88, '#f07a8a') + flower(138, 80, '#ffe27a', 8)
    + flower(128, 68, '#e04b5a') + flower(150, 70, '#f6a6b8')
    + z('path', '#9ccf7a', d='M112 104 Q118 94 126 100 Q120 108 112 104Z')
    + z('path', '#9ccf7a', d='M166 104 Q160 94 152 100 Q158 108 166 104Z')
    + z('path', '#c9d3db', d='M110 126 L168 126 L162 182 L116 182Z')
    + s('path', d='M112 140 L166 140', stroke_width=2.5)
    + hand(110, 152)
)
