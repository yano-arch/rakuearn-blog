from art import z, s, dot, cheeks, face, OUT, CH

def heart(cx, by, k=1.0):
    """bottom point at (cx, by); k = scale (k=1 -> about 40 wide, 36 tall)"""
    p = lambda dx, dy: f'{cx+dx*k:.1f} {by+dy*k:.1f}'
    return (f'M{p(0,0)} C{p(-12,-10)} {p(-20,-18)} {p(-14,-28)} C{p(-8,-36)} {p(0,-31)} {p(0,-24)} '
            f'C{p(0,-31)} {p(8,-36)} {p(14,-28)} C{p(20,-18)} {p(12,-10)} {p(0,0)}Z')

def tube(d, color, w=6):
    """thick colored line with brown outline"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)

ITEMS = {}

ITEMS['laptop'] = (
    z('rect', '#5b6b7a', x=44, y=44, width=112, height=86, rx=8)
    + s('rect', '#d8eef8', x=53, y=53, width=94, height=68, rx=3)
    + z('rect', '#ffffff', x=66, y=64, width=64, height=44, rx=3)
    + s('rect', '#8fc7e8', x=66, y=64, width=64, height=11, rx=3, stroke_width=2.5)
    + dot(73, 69.5, 2.2, '#e8735a') + dot(80, 69.5, 2.2, '#ffc94d') + dot(87, 69.5, 2.2, '#9ccf7a')
    + s('path', d='M74 86 L118 86 M74 96 L104 96', stroke_width=2.5)
    + z('path', '#c9d3db', d='M44 134 L156 134 L176 158 Q178 164 172 164 L28 164 Q22 164 24 158Z')
    + s('rect', '#b9a99c', x=84, y=146, width=32, height=10, rx=3, stroke_width=2)
)

ITEMS['email-envelope'] = (
    z('rect', '#f4f4f0', x=34, y=56, width=132, height=94, rx=8)
    + s('path', d='M36 148 L86 106 M164 148 L114 106')
    + z('path', '#f6e0c4', d='M38 60 L100 112 L162 60Z')
    + z('path', '#f07a8a', d=heart(100, 124, 0.8))
    + s('path', d='M152 38 L158 30 M168 46 L178 42 M140 34 L140 26', stroke_width=2.5)
)

ITEMS['cloud-upload'] = (
    z('path', '#8fc7e8', d='M54 150 Q24 150 26 122 Q28 98 54 100 Q56 62 92 60 Q120 58 130 84 '
                         'Q144 72 160 82 Q172 92 166 108 Q182 114 178 132 Q174 150 152 150Z')
    + z('path', '#ffffff', d='M100 78 L128 108 L112 108 L112 140 L88 140 L88 108 L72 108Z')
)

ITEMS['robot'] = (
    tube('M68 136 Q50 144 44 158', '#8fb3e0')
    + tube('M132 136 Q150 144 156 158', '#8fb3e0')
    + z('circle', '#c9d3db', cx=43, cy=162, r=8) + z('circle', '#c9d3db', cx=157, cy=162, r=8)
    + z('rect', '#8fb3e0', x=66, y=120, width=68, height=56, rx=16)
    + z('circle', '#ffe27a', cx=100, cy=146, r=9)
    + s('path', d='M100 52 L100 36')
    + z('circle', '#f07a8a', cx=100, cy=30, r=8)
    + z('rect', '#7cc4b0', x=48, y=74, width=14, height=26, rx=5)
    + z('rect', '#7cc4b0', x=138, y=74, width=14, height=26, rx=5)
    + z('rect', '#c9d3db', x=58, y=50, width=84, height=68, rx=22)
    + dot(86, 82, 4) + dot(114, 82, 4) + cheeks(76, 124, 94, 6, 3.5)
    + s('path', d='M93 98 Q100 104 107 98', stroke_width=2.5)
)

ITEMS['magnifying-glass'] = (
    z('rect', '#9a6a3f', x=133, y=112, width=22, height=64, rx=10, transform='rotate(-45 144 144)')
    + z('rect', '#5b6b7a', x=113, y=110, width=20, height=16, rx=4, transform='rotate(-45 123 118)')
    + z('circle', '#f5b971', cx=86, cy=86, r=50)
    + s('circle', '#d8eef8', cx=86, cy=86, r=37)
    + s('path', d='M62 80 Q66 64 82 60', stroke='#ffffff', stroke_width=6)
)

ITEMS['padlock'] = (
    tube('M68 100 L68 72 Q68 38 100 38 Q132 38 132 72 L132 100', '#c9d3db', 11)
    + z('rect', '#ffc94d', x=48, y=92, width=104, height=84, rx=14)
    + s('circle', OUT, cx=100, cy=126, r=9, stroke='none')
    + s('path', OUT, d='M95 128 L105 128 L108 150 L92 150Z', stroke='none')
)

ITEMS['battery-charging'] = (
    z('rect', '#5b6b7a', x=158, y=86, width=16, height=30, rx=4)
    + z('rect', '#f4f4f0', x=28, y=62, width=132, height=78, rx=12)
    + s('rect', '#9ccf7a', x=38, y=72, width=96, height=58, rx=5, stroke_width=2.5)
    + z('path', '#ffe27a', d='M104 52 L70 106 L94 106 L84 152 L124 94 L100 94 L112 52Z')
)

ITEMS['wifi-signal'] = (
    tube('M60 86 A56 56 0 0 1 140 86', '#7cc4b0', 7)
    + tube('M73 100 A38 38 0 0 1 127 100', '#7cc4b0', 7)
    + tube('M86 114 A20 20 0 0 1 114 114', '#7cc4b0', 7)
    + z('circle', '#7cc4b0', cx=100, cy=124, r=6)
    + s('path', d='M66 146 L58 120 M134 146 L142 120', stroke_width=5)
    + z('rect', '#8fb3e0', x=44, y=142, width=112, height=34, rx=10)
    + dot(66, 159, 4, '#9ccf7a') + dot(80, 159, 4, '#9ccf7a') + dot(94, 159, 4, '#ffc94d')
    + s('path', d='M116 159 L140 159', stroke_width=2.5)
)

ITEMS['growth-chart'] = (
    z('rect', '#8fc7e8', x=52, y=138, width=22, height=32, rx=3)
    + z('rect', '#7cc4b0', x=84, y=116, width=22, height=54, rx=3)
    + z('rect', '#f5d58a', x=116, y=92, width=22, height=78, rx=3)
    + z('rect', '#f6a6b8', x=148, y=66, width=22, height=104, rx=3)
    + s('path', d='M36 30 L36 172 L180 172', stroke_width=3.5)
    + tube('M46 122 L82 96 L104 104 L148 52', '#e8735a', 6)
    + z('path', '#e8735a', d='M164 34 L160 66 L136 46Z')
)

_grid = ''
for r in range(4):
    for c in range(5):
        x, y = 52 + c * 22, 92 + r * 20
        if (r, c) == (1, 3):
            continue
        _grid += s('rect', '#f6e0c4', x=x, y=y, width=14, height=13, rx=2, stroke_width=1.8)

ITEMS['calendar'] = (
    z('rect', '#ffffff', x=38, y=52, width=124, height=126, rx=10)
    + z('path', '#e8735a', d='M38 84 L38 62 Q38 52 48 52 L152 52 Q162 52 162 62 L162 84Z')
    + z('rect', '#b9a99c', x=62, y=36, width=10, height=28, rx=5)
    + z('rect', '#b9a99c', x=128, y=36, width=10, height=28, rx=5)
    + _grid
    + s('circle', cx=125, cy=118, r=14, stroke='#e04b5a', stroke_width=3)
    + s('path', '#f07a8a', d=heart(125, 125, 0.42), stroke_width=2)
)
