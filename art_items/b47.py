from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}


def waves(y, x0=24, x1=176, step=24, sw=2.5):
    d = f'M{x0} {y}'
    x = x0
    while x < x1:
        d += f' Q{x + step / 4} {y - 6} {x + step / 2} {y} Q{x + 3 * step / 4} {y + 6} {x + step} {y}'
        x += step
    return s('path', d=d, stroke_width=sw)


# 1 picnic
ITEMS['picnic'] = (
    z('path', '#f07a8a', d='M24 176 L54 120 L148 120 L176 176Z')
    + s('path', '#ffffff', d='M47 133 L152 133 L158 145 L41 145Z', stroke='none')
    + s('path', '#ffffff', d='M34 157 L165 157 L170 166 L30 166Z', stroke='none')
    + ''.join(s('path', d=f'M{a} 120 L{b} 176', stroke='#ffffff', stroke_width=7) for a, b in ((78, 64), (101, 100), (124, 136)))
    + s('path', d='M24 176 L54 120 L148 120 L176 176Z')
    + s('path', d='M70 104 Q70 56 100 56 Q130 56 130 104', stroke_width=7)
    + s('path', d='M70 104 Q70 56 100 56 Q130 56 130 104', stroke='#d9a66b', stroke_width=3)
    + z('path', '#d9a66b', d='M58 100 L142 100 L134 152 L66 152Z')
    + s('path', d='M62 117 L138 117 M64 134 L136 134 M86 100 L88 152 M114 100 L112 152', stroke_width=2)
    + z('rect', '#9a6a3f', x=54, y=92, width=92, height=12, rx=4)
    + z('circle', '#e04b5a', cx=152, cy=148, r=12) + s('path', d='M152 136 Q154 130 158 128', stroke_width=2.5)
    + z('path', '#9ccf7a', d='M154 134 Q164 126 168 134 Q160 140 154 134Z'))

# 2 barbecue
ITEMS['barbecue'] = (
    s('path', d='M80 148 L64 182 M120 148 L136 182 M100 150 L100 182', stroke_width=4)
    + z('circle', '#5b6b7a', cx=64, cy=182, r=5) + z('circle', '#5b6b7a', cx=136, cy=182, r=5)
    + z('path', '#e8735a', d='M44 100 L156 100 Q154 154 100 154 Q46 154 44 100Z')
    + s('path', d='M38 100 L162 100', stroke_width=4)
    + z('rect', '#e8735a', x=80, y=76, width=30, height=18, rx=8)
    + s('path', d='M86 82 L92 88 M96 82 L102 88', stroke='#9a6a3f', stroke_width=2.5)
    + z('rect', '#f07a8a', x=116, y=80, width=36, height=14, rx=7)
    + z('rect', '#d9a66b', x=50, y=80, width=26, height=14, rx=7)
    + s('path', d='M58 82 L58 92 M66 82 L66 92', stroke='#9a6a3f', stroke_width=2)
    + s('path', d='M74 66 Q66 56 74 46 Q82 36 74 26', stroke='#b9a99c', stroke_width=3)
    + s('path', d='M110 64 Q102 54 110 44 Q118 34 110 24', stroke='#b9a99c', stroke_width=3)
    + s('path', d='M140 68 Q134 60 140 52', stroke='#b9a99c', stroke_width=3)
    + s('circle', '#c9d3db', cx=100, cy=127, r=6, stroke_width=2.5))

# 3 japanese castle
ITEMS['japanese-castle'] = (
    z('path', '#b9a99c', d='M40 182 Q52 160 50 140 L150 140 Q148 160 160 182Z')
    + s('path', d='M64 152 L136 152 M58 168 L142 168 M80 140 L76 182 M120 140 L124 182', stroke_width=2)
    + z('rect', '#f4f4f0', x=58, y=112, width=84, height=28)
    + z('path', '#5b6b7a', d='M38 116 Q60 110 70 98 L130 98 Q140 110 162 116Z')
    + z('rect', '#f4f4f0', x=70, y=82, width=60, height=16)
    + z('path', '#5b6b7a', d='M52 86 Q72 80 80 68 L120 68 Q128 80 148 86Z')
    + z('rect', '#f4f4f0', x=82, y=54, width=36, height=14)
    + z('path', '#5b6b7a', d='M66 58 Q84 52 88 34 L112 34 Q116 52 134 58Z')
    + s('path', '#ffc94d', d='M88 34 Q84 26 90 22 Q92 28 96 30Z', stroke_width=2)
    + s('path', '#ffc94d', d='M112 34 Q116 26 110 22 Q108 28 104 30Z', stroke_width=2)
    + ''.join(s('rect', '#5b6b7a', x=x, y=120, width=10, height=12, rx=1, stroke_width=2) for x in (68, 90, 110, 128))
    + ''.join(s('rect', '#5b6b7a', x=x, y=85, width=8, height=9, rx=1, stroke_width=2) for x in (82, 96, 110))
    + s('path', d='M30 182 L170 182', stroke_width=2))

# 4 european castle
crenel = lambda x, y, w: ''.join(z('rect', '#c9d3db', x=x + i * (w / 3), y=y, width=w / 3 - 4, height=10) for i in range(3))
ITEMS['european-castle'] = (
    z('rect', '#c9d3db', x=60, y=98, width=80, height=80)
    + ''.join(z('rect', '#c9d3db', x=x, y=88, width=12, height=12) for x in (62, 82, 106, 126))
    + z('rect', '#c9d3db', x=30, y=82, width=34, height=96) + z('rect', '#c9d3db', x=136, y=82, width=34, height=96)
    + z('path', '#8fb3e0', d='M26 84 L47 36 L68 84Z') + z('path', '#8fb3e0', d='M132 84 L153 36 L174 84Z')
    + s('path', d='M47 36 L47 24 M153 36 L153 24', stroke_width=2.5)
    + s('path', '#f07a8a', d='M47 24 L60 28 L47 32Z', stroke_width=2)
    + s('path', '#f07a8a', d='M153 24 L166 28 L153 32Z', stroke_width=2)
    + z('path', '#8b6b4f', d='M84 178 L84 146 Q84 128 100 128 Q116 128 116 146 L116 178Z')
    + s('path', d='M92 132 L92 178 M100 128 L100 178 M108 132 L108 178', stroke_width=2)
    + s('path', '#5b6b7a', d='M41 112 Q41 102 47 102 Q53 102 53 112 L53 124 L41 124Z', stroke_width=2)
    + s('path', '#5b6b7a', d='M147 112 Q147 102 153 102 Q159 102 159 112 L159 124 L147 124Z', stroke_width=2)
    + s('path', '#5b6b7a', d='M94 112 Q94 104 100 104 Q106 104 106 112 L106 118 L94 118Z', stroke_width=2)
    + s('path', d='M20 180 L180 180', stroke_width=2))

# 5 pagoda
def tier(y, hw, bw):
    return (z('rect', '#f5d58a', x=100 - bw, y=y - 16, width=2 * bw, height=16)
            + s('rect', '#e8735a', x=94, y=y - 14, width=12, height=12, stroke_width=2)
            + z('path', '#5b6b7a', d=f'M{100 - hw} {y + 4} Q{100 - hw + 14} {y - 2} {100 - hw + 22} {y - 10} L{100 + hw - 22} {y - 10} Q{100 + hw - 14} {y - 2} {100 + hw} {y + 4}Z'))
ITEMS['pagoda'] = (
    s('path', d='M100 44 L100 20', stroke_width=4)
    + ''.join(s('circle', '#ffc94d', cx=100, cy=y, r=3.5, stroke_width=2) for y in (24, 32, 40))
    + z('rect', '#e8735a', x=62, y=150, width=76, height=30)
    + s('rect', '#8b6b4f', x=90, y=158, width=20, height=22, stroke_width=2.5)
    + z('path', '#5b6b7a', d='M30 154 Q46 148 54 138 L146 138 Q154 148 170 154Z')
    + z('rect', '#f5d58a', x=70, y=122, width=60, height=16) + s('rect', '#e8735a', x=94, y=124, width=12, height=12, stroke_width=2)
    + z('path', '#5b6b7a', d='M38 126 Q52 120 60 110 L140 110 Q148 120 162 126Z')
    + z('rect', '#f5d58a', x=76, y=96, width=48, height=14) + s('rect', '#e8735a', x=94, y=98, width=12, height=10, stroke_width=2)
    + z('path', '#5b6b7a', d='M46 100 Q58 94 66 86 L134 86 Q142 94 154 100Z')
    + z('rect', '#f5d58a', x=82, y=72, width=36, height=14) + s('rect', '#e8735a', x=94, y=74, width=12, height=10, stroke_width=2)
    + z('path', '#5b6b7a', d='M54 76 Q64 70 72 62 L128 62 Q136 70 146 76Z')
    + z('rect', '#f5d58a', x=88, y=50, width=24, height=12)
    + z('path', '#5b6b7a', d='M62 54 Q72 48 78 42 L122 42 Q128 48 138 54Z')
    + s('path', d='M24 182 L176 182', stroke_width=2))

# 6 torii
ITEMS['torii'] = (
    z('path', '#9ccf7a', d='M20 182 Q60 164 100 168 Q140 164 180 182Z')
    + z('rect', '#e8735a', x=56, y=64, width=14, height=112, rx=2) + z('rect', '#e8735a', x=130, y=64, width=14, height=112, rx=2)
    + z('rect', '#5b6b7a', x=52, y=164, width=22, height=12, rx=2) + z('rect', '#5b6b7a', x=126, y=164, width=22, height=12, rx=2)
    + z('rect', '#e8735a', x=40, y=84, width=120, height=12, rx=2)
    + z('rect', '#e8735a', x=94, y=60, width=12, height=24)
    + z('path', '#e8735a', d='M30 54 Q100 64 170 54 L174 42 Q100 54 26 42Z')
    + z('path', '#5b6b7a', d='M24 42 Q100 54 176 42 L180 32 Q100 44 20 32Z'))

# 7 lighthouse
ITEMS['lighthouse'] = (
    s('path', d='M140 50 L178 40 M140 62 L180 66 M60 50 L22 40 M60 62 L20 66', stroke='#ffc94d', stroke_width=4)
    + z('path', '#f4f4f0', d='M74 166 L82 76 L118 76 L126 166Z')
    + s('path', '#e8735a', d='M80 100 L120 100 L122 122 L78 122Z', stroke_width=2.5)
    + s('path', '#e8735a', d='M76 144 L124 144 L126 166 L74 166Z', stroke_width=2.5)
    + s('path', d='M74 166 L82 76 L118 76 L126 166Z')
    + s('path', '#8b6b4f', d='M94 166 L94 152 Q100 146 106 152 L106 166Z', stroke_width=2.5)
    + z('rect', '#5b6b7a', x=74, y=70, width=52, height=8, rx=2)
    + z('rect', '#ffe27a', x=84, y=48, width=32, height=22, rx=3)
    + s('path', d='M94 48 L94 70 M106 48 L106 70', stroke_width=2)
    + z('path', '#e8735a', d='M80 50 Q100 26 120 50Z') + dot(100, 30, 3.5)
    + z('path', '#8fc7e8', d='M20 176 Q40 168 60 168 L140 168 Q160 168 180 176 L180 186 L20 186Z')
    + waves(178, 30, 170, 28, 2))

# 8 windmill
ITEMS['windmill'] = (
    z('path', '#9ccf7a', d='M20 182 Q100 160 180 182Z')
    + z('path', '#f5d58a', d='M70 176 L80 84 L120 84 L130 176Z')
    + s('path', '#8b6b4f', d='M92 176 L92 156 Q100 146 108 156 L108 176Z', stroke_width=2.5)
    + s('rect', '#8fc7e8', x=93, y=112, width=14, height=16, rx=3, stroke_width=2.5)
    + z('path', '#e8735a', d='M74 88 Q76 56 100 54 Q124 56 126 88Z')
    + ''.join(z('path', '#f4f4f0', d=d) for d in (
        'M100 70 L56 26 L44 38 L88 82Z', 'M100 70 L144 26 L156 38 L112 82Z',
        'M100 70 L144 114 L156 102 L112 58Z', 'M100 70 L56 114 L44 102 L88 58Z'))
    + s('path', d='M56 26 L88 58 M144 26 L112 58 M144 114 L112 82 M56 114 L88 82', stroke_width=2)
    + z('circle', '#8b6b4f', cx=100, cy=70, r=7))

# 9 bridge
ITEMS['bridge'] = (
    z('path', '#8fc7e8', d='M20 150 L180 150 L180 182 L20 182Z')
    + waves(168, 40, 160, 30, 2)
    + z('path', '#d9a66b', d='M20 110 L180 110 L180 160 L162 160 Q162 128 130 128 Q100 128 100 160 L100 160 Q100 128 70 128 Q38 128 38 160 L20 160Z')
    + s('path', d='M20 124 L180 124', stroke_width=2)
    + ''.join(s('path', d=f'M{x} 110 L{x} 124', stroke_width=2) for x in (40, 60, 80, 100, 120, 140, 160))
    + z('rect', '#e8735a', x=16, y=86, width=168, height=24, rx=3)
    + ''.join(s('rect', '#f5d58a', x=x, y=72, width=10, height=14, rx=2, stroke_width=2) for x in (24, 66, 124, 166))
    + s('path', d='M34 78 L66 78 M76 78 L124 78 M134 78 L166 78', stroke_width=3)
    + z('ellipse', '#ffffff', cx=56, cy=40, rx=22, ry=9) + z('ellipse', '#ffffff', cx=146, cy=48, rx=18, ry=8))

# 10 pyramid
ITEMS['pyramid'] = (
    z('circle', '#ffc94d', cx=150, cy=46, r=18)
    + z('path', '#f5d58a', d='M20 170 L76 66 L132 170Z')
    + s('path', '#d9a66b', d='M76 66 L132 170 L96 170Z', stroke_width=3)
    + s('path', d='M48 118 L104 118 M34 144 L118 144 M62 92 L90 92', stroke_width=2)
    + z('path', '#f5d58a', d='M112 170 L148 104 L184 170Z')
    + s('path', '#d9a66b', d='M148 104 L184 170 L160 170Z', stroke_width=3)
    + s('path', d='M130 138 L166 138', stroke_width=2)
    + z('path', '#f6e0c4', d='M16 172 Q100 160 184 172 L184 184 L16 184Z')
    + s('path', d='M40 178 Q48 174 56 178 M120 178 Q128 174 136 178', stroke_width=2))

# 11 cruise ship
ITEMS['cruise-ship'] = (
    z('rect', '#e8735a', x=110, y=44, width=18, height=26, rx=3) + s('rect', '#5b6b7a', x=110, y=44, width=18, height=6, stroke_width=2)
    + z('rect', '#e8735a', x=134, y=50, width=16, height=20, rx=3) + s('rect', '#5b6b7a', x=134, y=50, width=16, height=6, stroke_width=2)
    + z('rect', '#f4f4f0', x=60, y=68, width=96, height=22, rx=4)
    + z('rect', '#f4f4f0', x=40, y=88, width=128, height=24, rx=4)
    + ''.join(s('rect', '#8fc7e8', x=x, y=74, width=10, height=10, rx=2, stroke_width=2) for x in (70, 88, 106, 124, 140))
    + ''.join(s('rect', '#8fc7e8', x=x, y=94, width=10, height=10, rx=2, stroke_width=2) for x in (50, 68, 86, 104, 122, 140, 154))
    + z('path', '#5b6b7a', d='M22 112 L180 112 L164 148 L38 148Z')
    + s('path', '#f4f4f0', d='M26 120 L177 120 L174 126 L28 126Z', stroke_width=2)
    + ''.join(dot(x, 136, 3.5, '#f4f4f0') for x in (60, 82, 104, 126, 148))
    + z('path', '#8fc7e8', d='M14 150 Q56 144 100 150 Q144 144 186 150 L186 184 L14 184Z')
    + waves(166, 26, 174, 30, 2.5))

# 12 world trip
ITEMS['world-trip'] = (
    z('circle', '#8fc7e8', cx=100, cy=104, r=56)
    + s('path', '#9ccf7a', d='M70 72 Q90 60 104 76 Q100 96 80 94 Q62 90 70 72Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M114 108 Q140 98 146 120 Q136 144 118 138 Q106 124 114 108Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M60 116 Q76 114 82 128 Q74 142 62 134Z', stroke_width=2.5)
    + s('ellipse', cx=100, cy=104, rx=84, ry=30, stroke_width=2.5, stroke_dasharray='6 8', transform='rotate(-18 100 104)')
    + z('path', '#e8735a', d='M150 44 L140 26 L150 25 L166 42Z', transform='rotate(-20 158 46)')
    + z('ellipse', '#f4f4f0', cx=158, cy=46, rx=26, ry=9, transform='rotate(-20 158 46)')
    + z('path', '#e8735a', d='M138 46 L132 34 L140 34 L148 44Z', transform='rotate(-20 158 46)')
    + z('path', '#e8735a', d='M152 50 L144 70 L154 70 L166 50Z', transform='rotate(-20 158 46)')
    + ''.join(dot(x, y, 2.5, '#8fc7e8') for x, y in ((160, 44), (168, 41), (176, 38))))

# 13 duffel bag
ITEMS['duffel-bag'] = (
    s('path', d='M74 88 Q74 50 100 50 Q126 50 126 88', stroke_width=8)
    + s('path', d='M74 88 Q74 50 100 50 Q126 50 126 88', stroke='#9a6a3f', stroke_width=3)
    + z('path', '#7cc4b0', d='M46 86 L154 86 Q182 86 182 130 Q182 172 154 172 L46 172 Q18 172 18 130 Q18 86 46 86Z')
    + s('ellipse', '#f5d58a', cx=40, cy=130, rx=14, ry=36, stroke_width=2.5)
    + s('ellipse', '#f5d58a', cx=160, cy=130, rx=14, ry=36, stroke_width=2.5)
    + s('path', d='M52 98 L148 98', stroke_width=2.5) + s('path', d='M56 98 L144 98', stroke='#f4f4f0', stroke_width=1, stroke_dasharray='3 3')
    + s('rect', '#f5d58a', x=138, y=94, width=8, height=14, rx=2, stroke_width=2)
    + z('rect', '#9a6a3f', x=82, y=86, width=10, height=30, rx=2) + z('rect', '#9a6a3f', x=108, y=86, width=10, height=30, rx=2)
    + s('rect', '#7cc4b0', x=70, y=128, width=60, height=28, rx=4, stroke_width=2.5))

# 14 tourist photo
ITEMS['tourist-photo'] = (
    z('path', '#f5b971', d='M60 186 Q62 130 100 128 Q138 130 140 186Z')
    + face(100, 84, '#ffd9b8', '#5a4033', 'open')
    + z('ellipse', '#f5d58a', cx=100, cy=56, rx=54, ry=10)
    + z('path', '#f5d58a', d='M74 56 Q74 26 100 26 Q126 26 126 56Z')
    + s('path', '#e8735a', d='M74 50 Q100 56 126 50 L126 56 Q100 62 74 56Z', stroke_width=2.5)
    + s('path', d='M78 146 L86 128 M122 146 L114 128', stroke_width=2.5)
    + z('rect', '#5b6b7a', x=72, y=140, width=56, height=36, rx=6)
    + s('rect', '#5b6b7a', x=82, y=134, width=16, height=8, rx=2, stroke_width=2.5)
    + z('circle', '#c9d3db', cx=100, cy=158, r=12) + s('circle', '#8fb3e0', cx=100, cy=158, r=6, stroke_width=2)
    + z('circle', '#ffd9b8', cx=70, cy=160, r=9) + z('circle', '#ffd9b8', cx=130, cy=160, r=9)
    + s('path', d='M150 136 L160 128 M154 148 L168 146 M146 124 L150 112', stroke='#ffc94d', stroke_width=3))

# 15 road trip
ITEMS['road-trip'] = (
    z('path', '#9ccf7a', d='M18 96 Q60 60 100 86 Q140 54 182 90 L182 182 L18 182Z')
    + s('path', '#b9a99c', d='M96 92 Q118 100 112 110 Q96 126 60 136 Q20 148 40 182 L104 182 Q86 156 112 140 Q140 124 134 108 Q130 98 104 92Z', stroke_width=2.5)
    + s('path', d='M100 98 Q112 104 106 112 M88 124 Q64 134 58 146 M60 160 L62 172', stroke='#f4f4f0', stroke_width=3)
    + s('circle', '#7cc4a0', cx=150, cy=140, r=14, stroke_width=2.5) + s('path', d='M150 154 L150 168', stroke_width=3)
    + z('path', '#e8735a', d='M48 150 L48 140 Q48 132 56 131 L62 131 Q66 118 80 118 Q94 118 98 131 L104 132 Q110 134 110 142 L110 150Z')
    + s('path', '#8fc7e8', d='M68 131 Q71 123 78 123 L78 131Z', stroke_width=2)
    + s('path', '#8fc7e8', d='M84 131 L84 123 Q91 123 93 131Z', stroke_width=2)
    + z('circle', '#5b6b7a', cx=62, cy=152, r=7) + z('circle', '#5b6b7a', cx=96, cy=152, r=7)
    + z('rect', '#f5d58a', x=60, y=110, width=34, height=8, rx=3)
    + z('ellipse', '#ffffff', cx=50, cy=44, rx=20, ry=8) + z('circle', '#ffc94d', cx=150, cy=40, r=14))

# 16 tunnel
ITEMS['tunnel'] = (
    z('path', '#9ccf7a', d='M18 160 Q22 70 100 50 Q178 70 182 160Z')
    + s('circle', '#7cc4a0', cx=60, cy=82, r=10, stroke_width=2.5) + s('circle', '#7cc4a0', cx=144, cy=80, r=10, stroke_width=2.5)
    + z('path', '#c9d3db', d='M50 160 L50 124 Q50 82 100 82 Q150 82 150 124 L150 160Z')
    + s('path', '#3b2f2a', d='M64 160 L64 126 Q64 96 100 96 Q136 96 136 126 L136 160Z', stroke_width=2.5)
    + s('path', '#ffe27a', d='M92 160 L92 140 Q92 132 100 132 Q108 132 108 140 L108 160Z', stroke='none')
    + ''.join(dot(x, 112, 3, '#ffe27a') for x in (80, 100, 120))
    + z('path', '#b9a99c', d='M70 160 L130 160 L170 184 L30 184Z')
    + s('path', d='M100 164 L100 170 M100 176 L100 184', stroke='#f4f4f0', stroke_width=3))

# 17 highway
ITEMS['highway'] = (
    z('path', '#9ccf7a', d='M18 94 L182 94 L182 182 L18 182Z')
    + s('path', '#b9a99c', d='M90 94 L110 94 L172 182 L28 182Z', stroke_width=3)
    + s('path', d='M100 98 L100 106 M100 116 L100 130 M100 142 L100 162 M100 172 L100 182', stroke='#f4f4f0', stroke_width=4)
    + s('path', d='M94 94 L46 182 M106 94 L154 182', stroke='#ffe27a', stroke_width=2.5)
    + z('path', '#8fc7e8', d='M18 94 Q40 70 64 84 Q90 58 116 82 Q144 60 182 88 L182 94 L18 94Z')
    + s('path', d='M150 182 L150 108 L176 108', stroke_width=3)
    + z('rect', '#7cc4a0', x=150, y=100, width=30, height=16, rx=3)
    + z('rect', '#e8735a', x=108, y=140, width=26, height=22, rx=6)
    + s('rect', '#8fc7e8', x=112, y=144, width=18, height=8, rx=2, stroke_width=2)
    + z('rect', '#5b6b7a', x=106, y=160, width=8, height=8, rx=2) + z('rect', '#5b6b7a', x=128, y=160, width=8, height=8, rx=2)
    + z('rect', '#8fb3e0', x=86, y=108, width=14, height=12, rx=4))

# 18 train window
ITEMS['train-window'] = (
    z('rect', '#c9d3db', x=24, y=30, width=152, height=128, rx=14)
    + s('rect', '#8fc7e8', x=38, y=44, width=124, height=100, rx=10, stroke_width=2.5)
    + s('circle', '#ffc94d', cx=136, cy=66, r=10, stroke_width=2.5)
    + s('path', '#ffffff', d='M58 70 Q60 62 70 64 Q76 56 86 62 Q94 64 92 70Z', stroke_width=2)
    + s('path', '#9ccf7a', d='M38 120 L68 82 L92 110 L112 90 L162 128 L162 134 Q162 144 152 144 L48 144 Q38 144 38 134Z', stroke_width=2.5)
    + s('path', '#7cc4a0', d='M38 128 Q100 118 162 132 L162 134 Q162 144 152 144 L48 144 Q38 144 38 134Z', stroke_width=2.5)
    + s('path', d='M100 44 L100 144', stroke_width=3)
    + z('rect', '#8b6b4f', x=30, y=156, width=140, height=12, rx=3)
    + z('path', '#f4f4f0', d='M126 134 L146 134 L143 156 L129 156Z')
    + s('path', '#d9a66b', d='M127 142 L145 142 L143 156 L129 156Z', stroke_width=2)
    + z('rect', '#e8735a', x=52, y=146, width=34, height=10, rx=3))

# 19 ferry
ITEMS['ferry'] = (
    z('rect', '#f4f4f0', x=88, y=62, width=60, height=34, rx=4)
    + ''.join(s('rect', '#8fc7e8', x=x, y=70, width=12, height=10, rx=2, stroke_width=2) for x in (96, 114, 132))
    + z('rect', '#e8735a', x=126, y=40, width=14, height=22, rx=3)
    + z('rect', '#f5d58a', x=40, y=84, width=26, height=14, rx=5) + s('rect', '#8fc7e8', x=44, y=87, width=10, height=5, rx=1, stroke_width=1.5)
    + z('rect', '#8fb3e0', x=62, y=84, width=22, height=14, rx=5)
    + z('path', '#f4f4f0', d='M20 96 L180 96 L166 136 L34 136Z')
    + s('path', '#8fb3e0', d='M24 106 L177 106 L174 116 L27 116Z', stroke_width=2.5)
    + ''.join(dot(x, 126, 3.5, '#8fc7e8') for x in (56, 80, 104, 128, 152))
    + z('path', '#8fc7e8', d='M14 138 Q56 132 100 138 Q144 132 186 138 L186 182 L14 182Z')
    + waves(156, 26, 174, 30, 2.5) + s('path', d='M50 170 Q60 164 70 170 M120 172 Q130 166 140 172', stroke_width=2)
    + z('ellipse', '#ffffff', cx=50, cy=44, rx=20, ry=8))

# 20 rental car key
ITEMS['rental-car-key'] = (
    z('circle', '#c9d3db', cx=58, cy=58, r=26) + s('circle', '#ffffff', cx=58, cy=58, r=16, stroke_width=2.5)
    + z('path', '#c9d3db', d='M118 118 L168 168 L160 176 L150 166 L144 172 L138 166 L132 172 L108 128Z')
    + s('path', d='M126 132 L158 164', stroke_width=2)
    + z('rect', '#5b6b7a', x=62, y=70, width=60, height=86, rx=26, transform='rotate(-45 92 113)')
    + s('circle', '#e8735a', cx=80, cy=100, r=8, stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=100, cy=120, r=8, stroke_width=2.5)
    + s('circle', '#f4f4f0', cx=88, cy=124, r=4, stroke_width=2)
    + z('path', '#f5d58a', d='M28 116 L56 102 L72 132 L44 146Z') + s('circle', '#ffffff', cx=50, cy=114, r=4, stroke_width=2)
    + s('path', d='M50 114 Q42 90 50 78', stroke_width=2))
