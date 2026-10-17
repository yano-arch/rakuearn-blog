from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

ITEMS['car'] = (
    z('path', '#e8735a', d='M30 146 L30 126 Q30 108 50 106 L62 106 Q72 70 102 70 Q132 70 142 106 L156 108 Q172 110 172 128 L172 146Z')
    + s('path', '#8fc7e8', d='M72 106 Q80 82 98 81 L98 106Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M106 106 L106 81 Q124 82 132 106Z', stroke_width=2.5)
    + s('path', d='M102 112 L102 140', stroke_width=2.5) + s('path', d='M110 120 L118 120', stroke_width=2.5)
    + s('circle', '#ffe27a', cx=164, cy=120, r=5, stroke_width=2.5)
    + s('rect', '#f4f4f0', x=26, y=128, width=8, height=10, rx=2, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=66, cy=148, r=17) + s('circle', '#c9d3db', cx=66, cy=148, r=7, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=138, cy=148, r=17) + s('circle', '#c9d3db', cx=138, cy=148, r=7, stroke_width=2.5)
    + s('path', d='M24 172 L178 172', stroke_width=2))

ITEMS['bus'] = (
    z('rect', '#ffc94d', x=24, y=56, width=152, height=98, rx=14)
    + s('rect', '#8fc7e8', x=34, y=70, width=24, height=72, rx=3, stroke_width=2.5)
    + s('path', d='M46 72 L46 140', stroke_width=2)
    + ''.join(s('rect', '#8fc7e8', x=x, y=70, width=20, height=28, rx=3, stroke_width=2.5) for x in (68, 94, 120, 146))
    + s('rect', '#e8735a', x=58, y=110, width=118, height=8, stroke_width=2)
    + s('circle', '#ffe27a', cx=30, cy=136, r=4, stroke_width=2)
    + z('circle', '#5b6b7a', cx=82, cy=156, r=16) + s('circle', '#c9d3db', cx=82, cy=156, r=6, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=146, cy=156, r=16) + s('circle', '#c9d3db', cx=146, cy=156, r=6, stroke_width=2.5)
    + s('path', d='M22 174 L178 174', stroke_width=2))

ITEMS['train'] = (
    z('path', '#f4f4f0', d='M30 136 L30 86 Q30 72 44 72 L116 72 Q166 74 180 136Z')
    + s('path', '#8fb3e0', d='M30 112 L170 112 Q175 122 178 130 L30 130Z', stroke_width=2.5)
    + s('path', '#5b6b7a', d='M128 80 Q154 84 166 104 L136 104 Q130 92 128 80Z', stroke_width=2.5)
    + ''.join(s('rect', '#8fc7e8', x=x, y=82, width=16, height=16, rx=3, stroke_width=2.5) for x in (40, 62, 84, 106))
    + s('rect', '#5b6b7a', x=34, y=136, width=134, height=8, rx=2, stroke_width=2.5)
    + ''.join(z('circle', '#5b6b7a', cx=x, cy=148, r=7) for x in (50, 70, 130, 150))
    + s('path', d='M20 160 L180 160', stroke_width=3)
    + ''.join(s('path', d=f'M{x} 160 L{x-4} 170', stroke_width=2.5) for x in (36, 66, 96, 126, 156)))

frame = 'M58 138 L98 138 L88 94 M58 138 L88 94 L132 96 M98 138 L132 96 L144 138'
ITEMS['bicycle'] = (
    s('circle', '#f4f4f0', cx=62, cy=142, r=26, stroke='none') + s('circle', '#f4f4f0', cx=148, cy=142, r=26, stroke='none')
    + s('circle', cx=58, cy=138, r=30, stroke_width=7) + s('circle', cx=144, cy=138, r=30, stroke_width=7)
    + ''.join(s('path', d=f'M{cx-21} {138-21} L{cx+21} {138+21} M{cx-21} {138+21} L{cx+21} {138-21} M{cx} 108 L{cx} 168', stroke_width=1.5) for cx in (58, 144))
    + s('path', d=frame, stroke_width=9) + s('path', d=frame, stroke='#e8735a', stroke_width=4)
    + s('path', d='M132 96 L128 80 L144 76', stroke_width=4)
    + z('ellipse', '#5b6b7a', cx=86, cy=88, rx=14, ry=5)
    + z('circle', '#c9d3db', cx=98, cy=138, r=8) + dot(58, 138, 4) + dot(144, 138, 4))

ITEMS['ship'] = (
    s('path', d='M100 62 L100 40 L122 50 L100 56', stroke_width=2.5)
    + z('rect', '#f5d58a', x=106, y=60, width=20, height=32, rx=2) + s('rect', '#e8735a', x=106, y=64, width=20, height=8, stroke_width=2)
    + z('rect', '#f4f4f0', x=56, y=88, width=88, height=34, rx=4)
    + ''.join(dot(x, 104, 5, '#8fc7e8') for x in (74, 94, 114, 132))
    + z('path', '#e8735a', d='M28 120 L172 120 L152 158 L48 158Z')
    + s('path', '#ffffff', d='M36 132 L166 132 L162 140 L40 140Z', stroke_width=2)
    + z('path', '#8fc7e8', d='M22 160 Q36 150 50 160 Q64 170 78 160 Q92 150 106 160 Q120 170 134 160 Q148 150 162 160 Q172 166 178 162 L178 182 L22 182Z')
    + s('path', d='M40 172 Q48 168 56 172 M110 174 Q118 170 126 174', stroke_width=2))

hd = 'M84 62 L84 30 L116 30 L116 62'
ITEMS['suitcase'] = (
    s('path', d=hd, stroke_width=9) + s('path', d=hd, stroke='#c9d3db', stroke_width=4)
    + z('rect', '#7cc4b0', x=50, y=60, width=100, height=108, rx=12)
    + s('path', d='M72 70 L72 158 M128 70 L128 158', stroke_width=2.5)
    + z('circle', '#ffe27a', cx=100, cy=92, r=12)
    + s('rect', '#f6a6b8', x=82, y=124, width=24, height=16, rx=3, stroke_width=2.5, transform='rotate(-12 94 132)')
    + s('path', '#ffffff', d='M114 118 L117 126 L125 126 L119 131 L121 139 L114 134 L107 139 L109 131 L103 126 L111 126Z', stroke_width=2)
    + z('circle', '#5b6b7a', cx=66, cy=174, r=7) + z('circle', '#5b6b7a', cx=134, cy=174, r=7))

ITEMS['map-pin'] = (
    z('path', '#f6e0c4', d='M32 72 L74 60 L74 160 L32 172Z')
    + z('path', '#f5d58a', d='M74 60 L126 72 L126 172 L74 160Z')
    + z('path', '#f6e0c4', d='M126 72 L168 60 L168 160 L126 172Z')
    + s('path', '#9ccf7a', d='M38 100 Q56 88 68 104 Q62 126 44 122 Q36 112 38 100Z', stroke_width=2.5)
    + s('path', '#9ccf7a', d='M134 126 Q150 112 162 124 Q160 146 142 148 Q132 140 134 126Z', stroke_width=2.5)
    + s('path', d='M50 150 Q80 140 92 150 Q104 160 126 140 Q138 128 146 106', stroke_width=2.5, stroke_dasharray='5 6')
    + z('path', '#e04b5a', d='M110 126 Q86 92 86 70 A24 24 0 1 1 134 70 Q134 92 110 126Z')
    + s('circle', '#ffffff', cx=110, cy=70, r=9, stroke_width=2.5))

ITEMS['camera'] = (
    z('rect', '#5b6b7a', x=56, y=52, width=36, height=22, rx=4)
    + z('rect', '#e8735a', x=128, y=56, width=20, height=12, rx=3)
    + z('rect', '#f5b971', x=32, y=68, width=136, height=96, rx=14)
    + s('path', '#9a6a3f', d='M32 104 L168 104 L168 134 L32 134Z', stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=100, cy=118, r=34)
    + s('circle', '#8fc7e8', cx=100, cy=118, r=20, stroke_width=2.5)
    + dot(93, 111, 5, '#ffffff')
    + s('rect', '#ffe27a', x=142, y=78, width=16, height=12, rx=2, stroke_width=2.5))

fl = 'M152 158 Q132 140 144 120 Q146 132 152 132 Q150 114 162 104 Q160 122 170 134 Q176 148 158 160Z'
ITEMS['camping-tent'] = (
    z('path', '#9ccf7a', d='M26 168 L76 58 L126 168Z')
    + s('path', '#5b6b7a', d='M76 90 L60 168 L92 168Z', stroke_width=2.5)
    + s('path', d='M76 58 L70 46 M76 58 L84 44', stroke_width=2.5)
    + z('path', '#ffc94d', d=fl)
    + s('path', '#e8735a', d='M156 158 Q148 148 154 138 Q158 146 160 140 Q166 150 162 158Z', stroke_width=2)
    + z('rect', '#9a6a3f', x=134, y=158, width=48, height=10, rx=5, transform='rotate(-10 158 163)')
    + z('rect', '#d9a66b', x=134, y=158, width=48, height=10, rx=5, transform='rotate(10 158 163)')
    + s('path', d='M22 176 L180 176', stroke_width=2)
    + s('path', '#ffe27a', d='M150 46 L153 54 L161 55 L155 60 L157 68 L150 64 L143 68 L145 60 L139 55 L147 54Z', stroke_width=2)
    + dot(120, 40, 3) + dot(176, 82, 2.5))

ITEMS['hot-air-balloon'] = (
    z('ellipse', '#ffffff', cx=44, cy=150, rx=22, ry=10) + z('ellipse', '#ffffff', cx=160, cy=60, rx=20, ry=9)
    + z('path', '#f07a8a', d='M100 26 C152 26 164 80 136 108 L118 128 L82 128 L64 108 C36 80 48 26 100 26Z')
    + s('path', '#ffe27a', d='M100 26 C120 40 124 98 112 128 L88 128 C76 98 80 40 100 26Z', stroke_width=2.5)
    + s('path', d='M54 70 Q100 86 146 70', stroke_width=2.5)
    + s('path', d='M84 128 L88 148 M116 128 L112 148 M100 128 L100 148', stroke_width=2)
    + z('rect', '#d9a66b', x=84, y=146, width=32, height=24, rx=3)
    + s('path', d='M84 156 L116 156', stroke_width=2)
    + z('ellipse', '#ffffff', cx=150, cy=166, rx=24, ry=10))
