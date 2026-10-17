from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def hand(x, y, skin, r=8):
    return z('circle', skin, cx=x, cy=y, r=r)


# 1. doctor
SK = '#ffd9b8'; HR = '#2b2220'
ITEMS['doctor'] = (
    z('path', HR, d='M66 96 Q60 140 74 146 L126 146 Q140 140 134 96Z')
    + body('#ffffff')
    + s('path', '#8fc7e8', d='M88 138 L100 158 L112 138Z', stroke_width=2.5)
    + s('path', d='M88 138 L96 176 M112 138 L104 176', stroke_width=2.5)
    + s('rect', '#f4f4f0', x=110, y=160, width=16, height=12, rx=2, stroke_width=2.5)
    + face(100, 98, SK, HR, 'smile')
    + s('path', d='M80 136 Q78 164 92 168', stroke='#5b6b7a', stroke_width=4)
    + s('path', d='M120 136 Q122 164 108 168', stroke='#5b6b7a', stroke_width=4)
    + s('path', d='M92 168 Q100 172 108 168', stroke='#5b6b7a', stroke_width=4)
    + z('circle', '#c9d3db', cx=100, cy=176, r=7)
)

# 2. nurse
SK = '#ffd9b8'; HR = '#2b2220'
ITEMS['nurse'] = (
    body('#8fc7e8')
    + s('path', d='M88 138 L100 152 L112 138', stroke_width=2.5)
    + s('rect', '#8fc7e8', x=72, y=158, width=16, height=14, rx=2, stroke_width=2.5)
    + face(100, 98, SK, HR, 'smile')
    + z('rect', '#d9a66b', x=110, y=140, width=38, height=46, rx=4)
    + s('rect', '#ffffff', x=115, y=148, width=28, height=33, rx=2, stroke_width=2.5)
    + s('path', d='M120 158 L138 158 M120 166 L138 166 M120 174 L132 174', stroke_width=2)
    + z('rect', '#b9a99c', x=121, y=135, width=16, height=8, rx=2)
    + hand(110, 166, SK)
)

# 3. chef
SK = '#ffd9b8'; HR = '#c9a36b'
ITEMS['chef'] = (
    body('#ffffff', cx=92)
    + s('path', d='M92 140 L92 186', stroke_width=2.5)
    + dot(82, 156, 3) + dot(82, 172, 3) + dot(102, 156, 3) + dot(102, 172, 3)
    + face(92, 100, SK, HR, 'open')
    + z('path', '#e8735a', d='M78 136 L106 136 L96 148 L88 148Z')
    + z('path', '#ffffff', d='M70 64 Q52 44 72 32 Q80 16 92 24 Q104 16 112 32 Q132 44 114 64Z')
    + z('rect', '#ffffff', x=68, y=58, width=48, height=14, rx=3)
    + s('path', d='M83 38 L83 56 M101 38 L101 56', stroke_width=2)
    + s('path', d='M126 158 L148 140', stroke_width=9)
    + s('path', d='M126 158 L148 140', stroke='#8b6b4f', stroke_width=4)
    + z('path', '#5b6b7a', d='M140 136 Q138 120 162 116 Q184 116 184 128 Q182 140 160 142 Q144 142 140 136Z')
    + s('ellipse', '#ffffff', cx=162, cy=128, rx=11, ry=7, stroke_width=2)
    + dot(162, 128, 4.5, '#ffc94d')
    + hand(126, 160, SK)
)

# 4. teacher
SK = '#ffd9b8'; HR = '#e8e1d8'
ITEMS['teacher'] = (
    s('path', d='M36 120 L28 180 M88 120 L96 180', stroke_width=4)
    + z('rect', '#8b6b4f', x=22, y=58, width=82, height=66, rx=4)
    + s('rect', '#7cc4a0', x=29, y=65, width=68, height=52, rx=2, stroke_width=2.5)
    + s('circle', cx=46, cy=84, r=9, stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M66 96 L76 76 L86 96Z', stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M38 106 Q48 100 58 106 Q68 112 78 106', stroke='#ffffff', stroke_width=2.5)
    + z('circle', HR, cx=138, cy=60, r=12)
    + body('#f6a6b8', cx=138)
    + s('path', d='M138 140 L138 186', stroke_width=2.5)
    + face(138, 98, SK, HR, 'smile')
    + s('circle', cx=126, cy=100, r=8, stroke_width=2) + s('circle', cx=150, cy=100, r=8, stroke_width=2)
    + s('path', d='M134 100 L142 100', stroke_width=2)
    + s('path', d='M112 152 L76 104', stroke_width=6)
    + s('path', d='M112 152 L76 104', stroke='#d9a66b', stroke_width=2)
    + hand(112, 152, SK)
)

# 5. firefighter
SK = '#ffd9b8'; HR = '#9a6a3f'
ITEMS['firefighter'] = (
    z('path', HR, d='M64 104 Q56 132 66 142 Q76 132 72 104Z')
    + body('#f5b971')
    + s('rect', '#ffe27a', x=66, y=164, width=68, height=7, stroke_width=2.5)
    + s('path', d='M100 140 L100 186', stroke_width=2.5)
    + face(100, 102, SK, HR, 'smile')
    + z('path', '#e04b5a', d='M64 86 Q64 48 100 46 Q136 48 136 86Z')
    + s('path', d='M100 48 L100 84', stroke_width=2.5)
    + s('path', '#ffe27a', d='M92 58 L108 58 L108 70 Q100 78 92 70Z', stroke_width=2.5)
    + z('path', '#e04b5a', d='M54 86 Q100 78 146 86 Q148 94 140 94 L60 94 Q52 94 54 86Z')
    + s('path', d='M34 186 Q34 152 66 158 Q104 166 128 150', stroke_width=13)
    + s('path', d='M34 186 Q34 152 66 158 Q104 166 128 150', stroke='#ffc94d', stroke_width=7)
    + z('path', '#b9a99c', d='M124 142 L150 124 L158 136 L132 154Z')
    + hand(130, 152, SK)
    + z('path', '#8fc7e8', d='M160 112 Q166 104 168 98 Q172 106 170 112 Q166 118 160 112Z')
    + z('path', '#8fc7e8', d='M172 128 Q178 122 182 118 Q184 126 180 130 Q176 134 172 128Z')
    + z('path', '#8fc7e8', d='M150 98 Q154 90 156 86 Q160 92 158 98 Q154 102 150 98Z')
)

# 6. farmer
SK = '#ffd9b8'; HR = '#5a4033'
ITEMS['farmer'] = (
    body('#e8735a')
    + s('path', '#8fb3e0', d='M78 186 L78 150 L122 150 L122 186Z')
    + s('path', d='M80 150 L84 138 M120 150 L116 138', stroke_width=3)
    + face(100, 100, SK, HR, 'smile')
    + z('path', '#f5d58a', d='M74 72 Q74 40 100 40 Q126 40 126 72Z')
    + s('rect', '#e8735a', x=74, y=60, width=52, height=8, stroke_width=2.5)
    + z('ellipse', '#f5d58a', cx=100, cy=74, rx=56, ry=11)
    + z('path', '#9ccf7a', d='M80 154 L74 132 L86 140 L90 128 L96 152Z')
    + z('circle', '#e04b5a', cx=106, cy=150, r=11)
    + s('path', '#7cc4a0', d='M100 140 L106 143 L112 140 L108 137Z', stroke_width=2)
    + z('path', '#f5b971', d='M118 156 L132 128 Q136 126 136 132 L126 158Z')
    + s('path', '#9ccf7a', d='M134 128 L140 118 M134 128 L144 124', stroke_width=2.5)
    + z('path', '#d9a66b', d='M66 154 L134 154 L126 186 L74 186Z')
    + s('path', d='M70 166 L130 166 M72 176 L128 176', stroke_width=2)
    + hand(66, 160, SK) + hand(134, 160, SK)
)

# 7. construction-worker
SK = '#ffd9b8'; HR = '#2b2220'
ITEMS['construction-worker'] = (
    body('#8fb3e0')
    + s('path', '#f5b971', d='M64 186 Q66 146 88 138 L90 186Z')
    + s('path', '#f5b971', d='M136 186 Q134 146 112 138 L110 186Z')
    + s('rect', '#ffe27a', x=67, y=164, width=22, height=7, stroke_width=2)
    + s('rect', '#ffe27a', x=111, y=164, width=22, height=7, stroke_width=2)
    + face(100, 102, SK, HR, 'open')
    + z('path', '#ffc94d', d='M66 86 Q66 50 100 48 Q134 50 134 86Z')
    + s('path', d='M100 50 L100 84', stroke_width=2.5)
    + z('rect', '#ffc94d', x=58, y=82, width=84, height=9, rx=4)
    + s('path', d='M128 154 L146 140', stroke_width=12)
    + s('path', d='M128 154 L146 140', stroke='#8fb3e0', stroke_width=6)
    + z('rect', '#c9d3db', x=145, y=86, width=11, height=50, rx=4)
    + z('path', '#c9d3db', d='M139 92 Q134 74 142 64 L146 76 L156 76 L159 64 Q168 74 162 92Z')
    + hand(150, 138, SK)
)

# 8. office-worker-laptop
SK = '#ffd9b8'; HR = '#2b2220'
ITEMS['office-worker-laptop'] = (
    body('#ffffff', cx=80, top=128, bottom=180)
    + s('path', d='M66 130 L80 140 L94 130', stroke_width=2.5)
    + z('path', '#e8735a', d='M76 138 L84 138 L87 160 L80 168 L73 160Z')
    + face(80, 90, SK, HR, 'smile')
    + z('rect', '#d9a66b', x=26, y=176, width=150, height=10, rx=3)
    + z('path', '#c9d3db', d='M154 168 L168 112 Q170 106 175 108 L178 110 L166 168Z')
    + s('path', '#ffffff', d='M160 160 L171 118', stroke_width=2)
    + z('rect', '#b9a99c', x=104, y=166, width=64, height=8, rx=2)
    + hand(116, 162, SK) + hand(138, 162, SK)
    + s('path', d='M112 148 L108 142 M127 146 L127 139 M142 148 L146 142', stroke_width=2.5)
    + z('path', '#8fc7e8', d='M34 156 L50 156 L48 176 L36 176Z')
    + s('path', d='M50 160 Q58 164 49 170', stroke_width=2.5)
)

# 9. delivery-person
SK = '#ffd9b8'; HR = '#5a4033'
ITEMS['delivery-person'] = (
    body('#7cc4b0')
    + face(100, 100, SK, HR, 'smile')
    + z('path', '#7cc4b0', d='M66 84 Q66 52 100 52 Q134 52 134 84Z')
    + dot(100, 54, 4)
    + z('path', '#7cc4b0', d='M68 82 Q100 74 132 82 Q136 92 100 90 Q64 92 68 82Z')
    + z('rect', '#d9a66b', x=66, y=138, width=68, height=46, rx=3)
    + s('rect', '#f5d58a', x=93, y=138, width=14, height=46, stroke_width=2)
    + s('path', d='M66 150 L93 150 M107 150 L134 150', stroke_width=2)
    + hand(66, 164, SK) + hand(134, 164, SK)
)

# 10. scientist
SK = '#ffd9b8'; HR = '#2b2220'
ITEMS['scientist'] = (
    z('circle', HR, cx=70, cy=90, r=14) + z('circle', HR, cx=130, cy=90, r=14)
    + z('circle', HR, cx=74, cy=116, r=12) + z('circle', HR, cx=126, cy=116, r=12)
    + body('#ffffff')
    + s('path', '#9ccf7a', d='M90 138 L100 156 L110 138Z', stroke_width=2.5)
    + s('path', d='M90 138 L96 176 M110 138 L104 176', stroke_width=2.5)
    + face(100, 98, SK, HR, 'o')
    + s('path', d='M66 98 L80 98 M120 98 L134 98', stroke='#5b6b7a', stroke_width=4)
    + s('rect', '#d8eef8', x=78, y=90, width=20, height=16, rx=6, stroke_width=2.5)
    + s('rect', '#d8eef8', x=102, y=90, width=20, height=16, rx=6, stroke_width=2.5)
    + dot(88, 100) + dot(112, 100)
    + s('path', d='M98 98 L102 98', stroke_width=2.5)
    + z('path', '#ffffff', d='M146 106 L146 128 L128 162 Q126 168 132 168 L172 168 Q178 168 176 162 L158 128 L158 106Z')
    + s('path', '#f07a8a', d='M137 146 L167 146 L176 162 Q178 168 172 168 L132 168 Q126 168 128 162Z', stroke_width=2.5)
    + s('rect', '#ffffff', x=142, y=100, width=20, height=7, rx=2, stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=150, cy=88, r=5, stroke_width=2)
    + s('circle', '#9ccf7a', cx=160, cy=74, r=6, stroke_width=2)
    + s('circle', '#8fc7e8', cx=148, cy=60, r=4, stroke_width=2)
    + s('circle', '#ffffff', cx=146, cy=158, r=3, stroke_width=1.5)
    + s('circle', '#ffffff', cx=158, cy=154, r=2.5, stroke_width=1.5)
    + hand(132, 150, SK)
)
