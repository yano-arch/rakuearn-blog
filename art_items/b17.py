from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def hand(x, y, r=8):
    return z('circle', SK, cx=x, cy=y, r=r)


def arm(d, color):
    return s('path', d=d, stroke_width=10) + s('path', d=d, stroke=color, stroke_width=4)


def small(b, x, y, k):
    return f'<g transform="translate({x} {y}) scale({k})" stroke-width="{3/k:.2f}">{b}</g>'


def glasses(cx, cy):
    return (s('circle', cx=cx-12, cy=cy+2, r=9, stroke_width=2.5) + s('circle', cx=cx+12, cy=cy+2, r=9, stroke_width=2.5)
            + s('path', d=f'M{cx-3} {cy+2} L{cx+3} {cy+2}', stroke_width=2.5))


def tie(cx, top, color):
    return (s('path', '#ffffff', d=f'M{cx-12} {top+2} L{cx} {top+20} L{cx+12} {top+2}Z', stroke_width=2.5)
            + s('path', color, d=f'M{cx-4} {top+6} L{cx+4} {top+6} L{cx+6} {top+34} L{cx} {top+40} L{cx-6} {top+34}Z', stroke_width=2.5))


# 1. pharmacist
ITEMS['pharmacist'] = (
    body('#ffffff', cx=92)
    + s('path', d='M80 138 L92 156 L104 138', stroke_width=2.5)
    + s('rect', '#8fc7e8', x=68, y=160, width=14, height=12, rx=2, stroke_width=2.5)
    + face(92, 98, SK, '#5a4033', 'smile')
    + z('rect', '#e8735a', x=124, y=126, width=34, height=50, rx=6)
    + z('rect', '#f4f4f0', x=127, y=114, width=28, height=14, rx=3)
    + s('rect', '#ffffff', x=130, y=140, width=22, height=22, rx=2, stroke_width=2.5)
    + s('path', d='M141 145 L141 157 M135 151 L147 151', stroke='#7cc4b0', stroke_width=3.5)
    + hand(126, 162)
    + z('rect', '#ffffff', x=150, y=60, width=32, height=14, rx=7, transform='rotate(-35 166 67)')
    + s('path', '#8fc7e8', d='M166 60 L159 60 Q150 60 150 67 Q150 74 159 74 L166 74Z', transform='rotate(-35 166 67)', stroke_width=2.5)
    + z('circle', '#f5d58a', cx=140, cy=42, r=7)
)

# 2. dentist
ITEMS['dentist'] = (
    body('#8fc7e8', cx=122)
    + s('path', d='M110 138 L122 152 L134 138', stroke_width=2.5)
    + face(122, 98, SK, '#2b2220', 'smile')
    + z('path', '#ffffff', d='M30 112 Q30 84 50 86 Q58 90 64 86 Q84 84 84 112 Q82 134 76 156 Q72 168 67 156 L62 138 Q58 132 54 138 L48 156 Q43 168 38 156 Q32 134 30 112Z')
    + dot(48, 110, 3.2) + dot(66, 110, 3.2) + cheeks(40, 74, 119, 5, 3)
    + s('path', d='M52 119 Q57 124 62 119', stroke_width=2.5)
    + s('path', d='M156 166 L170 128', stroke_width=4)
    + z('circle', '#c9d3db', cx=172, cy=120, r=9)
    + hand(156, 166)
)

# 3. veterinarian
ITEMS['veterinarian'] = (
    body('#7cc4b0', top=128)
    + s('path', d='M88 130 L100 142 L112 130', stroke_width=2.5)
    + face(100, 86, SK, '#c9a36b', 'smile')
    + z('ellipse', '#d9a66b', cx=100, cy=176, rx=24, ry=12)
    + z('circle', '#d9a66b', cx=100, cy=152, r=21)
    + z('path', '#9a6a3f', d='M82 140 Q70 156 76 168 Q86 162 88 144Z')
    + z('path', '#9a6a3f', d='M118 140 Q130 156 124 168 Q114 162 112 144Z')
    + dot(93, 152, 3) + dot(107, 152, 3) + f'<ellipse cx="100" cy="160" rx="4.5" ry="3" fill="{OUT}" stroke="none"/>'
    + cheeks(87, 113, 162, 4, 2.5)
    + hand(74, 176) + hand(126, 176)
)

# 4. caregiver
ITEMS['caregiver'] = (
    body('#f6e0c4', cx=64, top=142)
    + s('path', d='M34 150 L30 186', stroke_width=4) + s('path', d='M34 150 Q34 140 44 142', stroke_width=4)
    + face(64, 104, SK, '#e8e1d8', 'smile')
    + s('path', d='M46 96 L56 96 M72 96 L82 96', stroke_width=2)
    + hand(36, 152)
    + body('#f6a6b8', cx=138, top=132)
    + s('path', d='M128 134 L138 146 L148 134', stroke_width=2.5)
    + face(138, 92, SK, '#5a4033', 'smile')
    + arm('M114 156 Q104 152 98 146', '#f6a6b8')
    + hand(96, 146)
)

# 5. nursery-teacher
child = (body('#ffc94d') + face(100, 98, SK, '#2b2220', 'open'))
ITEMS['nursery-teacher'] = (
    body('#f6a6b8', cx=70)
    + z('path', '#f5d58a', d='M50 148 L90 148 L94 186 L46 186Z')
    + s('path', '#ffffff', d='M60 162 L80 162 L78 176 L62 176Z', stroke_width=2.5)
    + face(70, 98, SK, '#5a4033', 'smile')
    + small(child, 82, 56, 0.7)
    + hand(118, 164, 7)
    + s('path', '#ffe27a', d='M170 52 L173 60 L181 61 L175 66 L177 74 L170 70 L163 74 L165 66 L159 61 L167 60Z', stroke_width=2)
)

# 6. librarian
ITEMS['librarian'] = (
    z('circle', '#5a4033', cx=100, cy=58, r=13)
    + body('#7cc4a0')
    + face(100, 98, SK, '#5a4033', 'smile')
    + glasses(100, 98)
    + z('rect', '#e8735a', x=72, y=166, width=56, height=14, rx=2)
    + z('rect', '#8fc7e8', x=76, y=152, width=50, height=14, rx=2)
    + z('rect', '#f5d58a', x=70, y=138, width=54, height=14, rx=2)
    + s('path', d='M80 138 L80 152 M116 152 L116 166 M82 166 L82 180', stroke_width=2)
    + hand(68, 170) + hand(132, 170)
)

# 7. programmer
def monitor(x):
    return (s('rect', '#b9a99c', x=x+31, y=74, width=12, height=16)
            + z('rect', '#5b6b7a', x=x, y=26, width=74, height=50, rx=4)
            + s('rect', '#d8eef8', x=x+6, y=32, width=62, height=38, rx=2, stroke_width=2.5)
            + s('path', d=f'M{x+12} 41 L{x+36} 41 M{x+20} 50 L{x+52} 50 M{x+20} 59 L{x+44} 59', stroke='#7cc4b0', stroke_width=3)
            + s('path', d=f'M{x+40} 41 L{x+56} 41', stroke='#e8735a', stroke_width=3))
ITEMS['programmer'] = (
    monitor(20) + monitor(106)
    + body('#8fb3e0', top=150, bottom=188)
    + face(100, 118, SK, '#2b2220', 'smile')
    + z('rect', '#c9d3db', x=56, y=166, width=88, height=18, rx=3)
    + s('path', d='M66 175 L134 175', stroke_width=2)
    + hand(62, 168) + hand(138, 168)
)

# 8. designer
ITEMS['designer'] = (
    body('#f5d58a', cx=82)
    + face(82, 98, SK, '#2b2220', 'smile')
    + z('ellipse', '#e8735a', cx=78, cy=64, rx=32, ry=11)
    + s('path', d='M80 53 L84 44', stroke_width=4)
    + z('rect', '#5b6b7a', x=118, y=104, width=56, height=76, rx=6, transform='rotate(8 146 142)')
    + s('rect', '#ffffff', x=124, y=111, width=44, height=60, rx=2, transform='rotate(8 146 142)', stroke_width=2.5)
    + s('path', d='M132 150 Q140 126 150 140 Q158 154 162 130', stroke='#f07a8a', stroke_width=4)
    + s('circle', '#8fc7e8', cx=148, cy=124, r=6, stroke_width=2)
    + s('path', d='M120 170 L140 150', stroke_width=9) + s('path', d='M120 170 L140 150', stroke='#8fb3e0', stroke_width=4)
    + hand(118, 170)
)

# 9. photographer
ITEMS['photographer'] = (
    body('#9ccf7a', cx=80)
    + face(80, 98, SK, '#c9a36b', 'smile')
    + s('path', d='M60 136 Q76 170 112 150', stroke='#8b6b4f', stroke_width=4)
    + z('rect', '#5b6b7a', x=126, y=110, width=20, height=12, rx=2)
    + z('rect', '#5b6b7a', x=110, y=118, width=66, height=46, rx=7)
    + s('rect', '#ffe27a', x=158, y=124, width=11, height=7, rx=1.5, stroke_width=2)
    + z('circle', '#c9d3db', cx=140, cy=142, r=15)
    + s('circle', '#8fc7e8', cx=140, cy=142, r=8, stroke_width=2.5)
    + dot(137, 139, 2.5, '#ffffff')
    + hand(112, 154) + hand(174, 158)
    + s('path', d='M164 100 L170 90 M178 106 L188 100 M150 98 L150 88', stroke_width=2.5)
)

# 10. reporter
ITEMS['reporter'] = (
    body('#e8735a', cx=84)
    + s('path', '#ffffff', d='M72 138 L84 156 L96 138Z', stroke_width=2.5)
    + face(84, 98, SK, '#5a4033', 'open')
    + s('path', d='M126 160 L148 128', stroke_width=10) + s('path', d='M126 160 L148 128', stroke='#2b2220', stroke_width=4)
    + z('rect', '#e8735a', x=138, y=128, width=16, height=10, rx=2, transform='rotate(34 146 133)')
    + z('circle', '#c9d3db', cx=154, cy=116, r=13)
    + dot(148, 112, 1.8) + dot(156, 112, 1.8) + dot(152, 118, 1.8) + dot(148, 122, 1.8) + dot(156, 122, 1.8) + dot(160, 117, 1.8) + dot(144, 117, 1.8)
    + hand(124, 162)
    + s('path', d='M170 92 Q178 98 176 106 M176 82 Q190 94 186 110', stroke_width=2.5)
)

# 11. news-anchor
ITEMS['news-anchor'] = (
    z('rect', '#c9d3db', x=22, y=26, width=40, height=30, rx=3)
    + s('circle', '#8fc7e8', cx=42, cy=41, r=9, stroke_width=2)
    + body('#5b6b7a', top=124, bottom=170)
    + tie(100, 124, '#e04b5a')
    + face(100, 86, SK, '#2b2220', 'smile')
    + z('rect', '#8fb3e0', x=24, y=148, width=152, height=36, rx=4)
    + s('path', d='M24 160 L176 160', stroke_width=2.5)
    + z('rect', '#ffffff', x=114, y=136, width=36, height=12, rx=2)
    + hand(78, 148) + hand(122, 144)
    + s('path', d='M58 148 L58 132', stroke_width=3) + z('circle', '#5b6b7a', cx=58, cy=128, r=5)
)

# 12. lawyer
ITEMS['lawyer'] = (
    s('path', d='M44 120 L44 170', stroke_width=4)
    + z('rect', '#8b6b4f', x=30, y=168, width=30, height=10, rx=2)
    + s('path', d='M24 122 L64 116', stroke_width=4) + dot(44, 118, 4.5)
    + s('path', d='M24 122 L18 142 M24 122 L30 142 M64 116 L58 136 M64 116 L70 136', stroke_width=2)
    + z('path', '#f5d58a', d='M14 142 L34 142 Q32 152 24 152 Q16 152 14 142Z')
    + z('path', '#f5d58a', d='M54 136 L74 136 Q72 146 64 146 Q56 146 54 136Z')
    + body('#5b6b7a', cx=104)
    + tie(104, 136, '#e04b5a')
    + face(104, 98, SK, '#2b2220', 'smile')
    + z('rect', '#d9a66b', x=118, y=126, width=46, height=56, rx=3, transform='rotate(6 141 154)')
    + s('rect', '#ffffff', x=124, y=120, width=36, height=50, rx=2, transform='rotate(-4 142 145)', stroke_width=2.5)
    + s('path', d='M130 132 L154 130 M130 142 L154 140 M131 152 L148 151', stroke_width=2)
    + hand(124, 170)
)

# 13. judge
ITEMS['judge'] = (
    z('path', '#5b6b7a', d='M56 186 Q58 134 100 132 Q142 134 144 186Z')
    + z('path', '#ffffff', d='M88 136 L112 136 L108 154 L100 160 L92 154Z')
    + s('path', d='M100 140 L100 158', stroke_width=2)
    + face(100, 96, SK, '#e8e1d8', 'smile')
    + z('rect', '#8b6b4f', x=136, y=170, width=40, height=12, rx=3)
    + s('path', d='M130 166 L150 136', stroke_width=10) + s('path', d='M130 166 L150 136', stroke='#d9a66b', stroke_width=4)
    + z('rect', '#9a6a3f', x=136, y=120, width=40, height=18, rx=4, transform='rotate(34 156 129)')
    + hand(130, 166)
    + s('path', d='M170 112 L180 104 M176 124 L188 122', stroke_width=2.5)
)

# 14. accountant
ITEMS['accountant'] = (
    z('rect', '#ffffff', x=24, y=128, width=38, height=48, rx=2, transform='rotate(-10 43 152)')
    + s('path', d='M32 142 L52 138 M33 152 L54 148 M35 162 L48 160', stroke_width=2, transform='rotate(-10 43 152)')
    + body('#8fb3e0', cx=96)
    + tie(96, 136, '#7cc4b0')
    + face(96, 98, SK, '#5a4033', 'smile')
    + glasses(96, 98)
    + z('rect', '#c9d3db', x=124, y=118, width=44, height=60, rx=6)
    + s('rect', '#9ccf7a', x=131, y=125, width=30, height=13, rx=2, stroke_width=2.5)
    + ''.join(dot(x, y, 3.5, '#5b6b7a') for x in (136, 146, 156) for y in (149, 159, 169))
    + hand(124, 166) + hand(62, 162)
)

# 15. real-estate-agent
ITEMS['real-estate-agent'] = (
    z('rect', '#f5d58a', x=26, y=140, width=36, height=36, rx=2)
    + z('path', '#e8735a', d='M20 144 L44 120 L68 144Z')
    + z('rect', '#8b6b4f', x=39, y=156, width=11, height=20, rx=2)
    + body('#7cc4b0', cx=96)
    + s('path', '#ffffff', d='M84 138 L96 156 L108 138Z', stroke_width=2.5)
    + face(96, 98, SK, '#2b2220', 'smile')
    + arm('M122 150 Q142 136 150 112', '#7cc4b0')
    + z('rect', '#ffc94d', x=150, y=40, width=8, height=50, rx=3)
    + z('rect', '#ffc94d', x=158, y=46, width=12, height=7, rx=1)
    + z('rect', '#ffc94d', x=158, y=58, width=8, height=7, rx=1)
    + z('circle', '#ffc94d', cx=154, cy=96, r=13)
    + s('circle', '#ffffff', cx=154, cy=98, r=4.5, stroke_width=2.5)
    + hand(150, 112)
)

# 16. salesperson
ITEMS['salesperson'] = (
    body('#8fb3e0', cx=86)
    + tie(86, 136, '#e8735a')
    + face(86, 98, SK, '#c9a36b', 'open')
    + z('path', '#ffffff', d='M118 124 L138 118 L158 124 L178 118 L178 166 L158 172 L138 166 L118 172Z')
    + s('path', d='M138 118 L138 166 M158 124 L158 172', stroke_width=2.5)
    + s('circle', '#f6a6b8', cx=128, cy=136, r=6, stroke_width=2)
    + s('path', '#9ccf7a', d='M142 156 L148 140 L154 156Z', stroke_width=2)
    + s('path', d='M162 138 L174 135 M162 146 L174 143 M162 154 L170 152', stroke_width=2)
    + hand(118, 162)
)

# 17. receptionist
ITEMS['receptionist'] = (
    body('#f07a8a', top=126, bottom=160)
    + s('path', '#ffffff', d='M90 128 L100 142 L110 128Z', stroke_width=2.5)
    + face(100, 88, SK, '#5a4033', 'smile')
    + z('rect', '#d9a66b', x=28, y=150, width=144, height=34, rx=3)
    + z('rect', '#f6e0c4', x=22, y=142, width=156, height=12, rx=3)
    + z('rect', '#8b6b4f', x=136, y=134, width=34, height=8, rx=2)
    + z('path', '#ffc94d', d='M140 134 Q140 112 153 112 Q166 112 166 134Z')
    + z('circle', '#ffc94d', cx=153, cy=108, r=4)
    + s('path', d='M140 100 L134 94 M166 100 L172 94 M153 96 L153 88', stroke_width=2.5)
    + hand(76, 140)
    + z('path', '#e8735a', d='M34 142 L56 142 L54 124 L36 124Z')
    + z('path', '#7cc4a0', d='M45 124 Q30 112 34 98 Q46 104 45 124Z')
    + z('path', '#7cc4a0', d='M45 124 Q58 110 56 96 Q44 104 45 124Z')
)

# 18. call-center
ITEMS['call-center'] = (
    body('#7cc4b0', cx=94)
    + s('path', '#ffffff', d='M82 138 L94 154 L106 138Z', stroke_width=2.5)
    + face(94, 98, SK, '#2b2220', 'smile')
    + s('path', d='M60 94 Q58 54 94 54 Q130 54 128 94', stroke_width=9)
    + s('path', d='M60 94 Q58 54 94 54 Q130 54 128 94', stroke='#5b6b7a', stroke_width=4)
    + z('rect', '#5b6b7a', x=52, y=84, width=14, height=24, rx=6)
    + z('rect', '#5b6b7a', x=122, y=84, width=14, height=24, rx=6)
    + s('path', d='M60 108 Q62 122 80 120', stroke_width=3)
    + z('circle', '#5b6b7a', cx=82, cy=120, r=4)
    + z('path', '#ffffff', d='M138 34 L178 34 Q184 34 184 40 L184 60 Q184 66 178 66 L156 66 L146 76 L148 66 L138 66 Q132 66 132 60 L132 40 Q132 34 138 34Z')
    + dot(146, 50, 3) + dot(158, 50, 3) + dot(170, 50, 3)
)

# 19. security-guard
ITEMS['security-guard'] = (
    body('#8fb3e0')
    + tie(100, 136, '#5b6b7a')
    + z('path', '#ffc94d', d='M118 148 L132 148 L132 158 Q132 166 125 170 Q118 166 118 158Z')
    + s('path', d='M66 150 L80 150', stroke='#5b6b7a', stroke_width=4)
    + face(100, 100, SK, '#2b2220', 'smile')
    + z('path', '#5b6b7a', d='M64 80 Q62 44 100 44 Q138 44 136 80Z')
    + z('path', '#5b6b7a', d='M60 80 Q100 70 140 80 Q142 90 132 90 Q100 84 68 90 Q58 90 60 80Z')
    + z('path', '#ffc94d', d='M94 54 L106 54 L106 62 Q106 68 100 70 Q94 68 94 62Z')
)

# 20. janitor
ITEMS['janitor'] = (
    body('#7cc4b0', cx=76)
    + z('path', '#5b6b7a', d='M58 150 L94 150 L98 186 L54 186Z')
    + face(76, 98, SK, '#5a4033', 'smile')
    + z('path', '#e8735a', d='M42 92 Q42 58 76 58 Q110 58 110 92 Q94 74 76 74 Q58 74 42 92Z')
    + z('path', '#8fb3e0', d='M142 146 L180 146 L176 184 L146 184Z')
    + s('path', d='M140 146 L182 146', stroke_width=4)
    + s('path', d='M150 146 Q161 128 172 146', stroke_width=2.5)
    + s('path', d='M126 36 L126 158', stroke_width=10) + s('path', d='M126 36 L126 158', stroke='#d9a66b', stroke_width=4)
    + z('path', '#f4f4f0', d='M112 158 L140 158 L146 182 Q140 186 136 180 Q132 188 126 180 Q120 188 116 180 Q110 186 106 182Z')
    + arm('M100 150 Q114 140 122 128', '#7cc4b0')
    + hand(126, 102) + hand(124, 128)
    + s('circle', cx=34, cy=168, r=5, stroke_width=2) + s('circle', cx=24, cy=156, r=3, stroke_width=2)
)
