from art import z, s, dot, cheeks, face, OUT, CH

SK = '#ffd9b8'

ITEMS = {}


def tube(d, color, w=6):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def hand(x, y, r=8):
    return z('circle', SK, cx=x, cy=y, r=r)


def box(x, y, w, h, fill='#d9a66b'):
    return (z('rect', fill, x=x, y=y, width=w, height=h, rx=2)
            + s('path', d=f'M{x+w/2} {y} L{x+w/2} {y+h*0.45}', stroke='#f5d58a', stroke_width=3))


def little_face(cx, cy, k=1.0):
    return (dot(cx - 9 * k, cy, 3 * k) + dot(cx + 9 * k, cy, 3 * k)
            + cheeks(cx - 16 * k, cx + 16 * k, cy + 8 * k, 5 * k, 3 * k)
            + s('path', d=f'M{cx-4*k} {cy+8*k} Q{cx} {cy+12*k} {cx+4*k} {cy+8*k}', stroke_width=2.5))


# 1. storefront
ITEMS['storefront'] = (
    z('rect', '#f6e0c4', x=44, y=72, width=112, height=104)
    + z('rect', '#e8735a', x=36, y=56, width=128, height=20, rx=4)
    + ''.join(z('path', '#e8735a' if i % 2 == 0 else '#ffffff', d=f'M{38+i*31} 80 L{69+i*31} 80 L{69+i*31} 100 Q{53.5+i*31} 116 {38+i*31} 100Z')
              for i in range(4))
    + z('rect', '#8fc7e8', x=56, y=120, width=46, height=36, rx=3)
    + s('path', d='M79 120 L79 156', stroke_width=2.5)
    + s('path', '#7cc4a0', d='M60 156 Q60 144 68 144 Q74 144 74 156Z', stroke_width=2)
    + z('rect', '#8b6b4f', x=114, y=118, width=32, height=58, rx=3)
    + dot(139, 148, 3)
    + s('path', d='M28 176 L172 176', stroke_width=3)
)

# 2. startup-rocket
ITEMS['startup-rocket'] = (
    z('path', '#ffc94d', d='M88 118 Q100 150 112 118Z')
    + s('path', '#e8735a', d='M93 118 Q100 136 107 118Z', stroke_width=2)
    + z('path', '#e8735a', d='M84 92 L70 116 L86 112Z')
    + z('path', '#e8735a', d='M116 92 L130 116 L114 112Z')
    + z('path', '#f4f4f0', d='M100 24 Q124 46 120 112 L80 112 Q76 46 100 24Z')
    + z('circle', '#8fc7e8', cx=100, cy=66, r=11)
    + s('path', d='M86 96 L114 96', stroke_width=2.5)
    + s('path', d='M54 60 L48 54 M146 60 L152 54 M52 84 L44 84 M148 84 L156 84', stroke_width=2.5)
    + z('rect', '#5b6b7a', x=56, y=128, width=88, height=34, rx=6)
    + s('rect', '#d8eef8', x=63, y=134, width=74, height=24, rx=3)
    + s('path', '#ffc94d', d='M92 134 Q100 150 108 134Z', stroke='none')
    + z('path', '#c9d3db', d='M48 164 L152 164 L166 178 L34 178Z')
)

# 3. target-goal
ITEMS['target-goal'] = (
    z('circle', '#e8735a', cx=92, cy=108, r=64)
    + s('circle', '#ffffff', cx=92, cy=108, r=48)
    + s('circle', '#e8735a', cx=92, cy=108, r=32)
    + s('circle', '#ffffff', cx=92, cy=108, r=17)
    + s('circle', '#e8735a', cx=92, cy=108, r=6)
    + s('path', d='M94 106 L156 44', stroke_width=9)
    + s('path', d='M94 106 L156 44', stroke='#9a6a3f', stroke_width=4)
    + z('path', '#7cc4b0', d='M150 50 L148 30 L160 20 L162 38Z')
    + z('path', '#7cc4b0', d='M150 50 L170 52 L180 40 L162 38Z')
    + s('path', d='M58 52 L48 42 M42 74 L30 70', stroke_width=2.5)
)

# 4. strategy-chess
_board = ''
for r in range(3):
    for c in range(6):
        if (r + c) % 2 == 0:
            x0 = 40 + c * 20
            _board += s('path', '#8b6b4f', d=f'M{x0} {150+r*10} L{x0+20} {150+r*10} L{x0+20} {160+r*10} L{x0} {160+r*10}Z', stroke='none')
ITEMS['strategy-chess'] = (
    z('rect', '#f6e0c4', x=36, y=146, width=128, height=34, rx=4)
    + s('rect', '#f6e0c4', x=40, y=150, width=120, height=26, stroke_width=2)
    + _board
    + s('rect', x=40, y=150, width=120, height=26, stroke_width=2)
    # rook (dark)
    + z('path', '#5b6b7a', d='M62 66 L62 50 L72 50 L72 58 L80 58 L80 50 L90 50 L90 58 L98 58 L98 50 L108 50 L108 66Z')
    + z('path', '#5b6b7a', d='M68 70 L102 70 L106 136 L64 136Z')
    + z('rect', '#5b6b7a', x=56, y=132, width=58, height=14, rx=4)
    + little_face(85, 98, 0.8)
    # pawn (light)
    + z('path', '#f4f4f0', d='M126 96 L150 96 L156 136 L120 136Z')
    + z('rect', '#f4f4f0', x=114, y=132, width=48, height=14, rx=4)
    + z('ellipse', '#f4f4f0', cx=138, cy=96, rx=18, ry=6)
    + z('circle', '#f4f4f0', cx=138, cy=78, r=15)
    + little_face(138, 112, 0.7)
)

# 5. falling-chart
ITEMS['falling-chart'] = (
    z('rect', '#7cc4b0', x=50, y=64, width=22, height=106, rx=3)
    + z('rect', '#8fc7e8', x=82, y=94, width=22, height=76, rx=3)
    + z('rect', '#f5d58a', x=114, y=122, width=22, height=48, rx=3)
    + z('rect', '#f6a6b8', x=146, y=148, width=22, height=22, rx=3)
    + s('path', d='M36 30 L36 172 L180 172', stroke_width=3.5)
    + tube('M48 42 L84 66 L106 60 L148 108', '#e8735a', 6)
    + z('path', '#e8735a', d='M166 128 L134 122 L160 98Z')
    + dot(152, 160, 2.5) + dot(162, 160, 2.5)
    + s('path', d='M153 167 Q157 163 161 167', stroke_width=2)
    + s('path', '#8fc7e8', d='M170 140 Q166 146 170 150 Q174 146 170 140Z', stroke_width=2)
)

# 6. pie-chart
ITEMS['pie-chart'] = (
    z('path', '#8fc7e8', d='M92 108 L92 44 A64 64 0 1 0 154 124Z')
    + z('path', '#f5d58a', d='M92 108 L154 124 A64 64 0 0 0 128 55Z')
    + z('path', '#e8735a', d='M100 98 L136 46 A62 62 0 0 0 100 34Z')
    + s('path', d='M92 108 L46 140', stroke_width=3)
    + s('path', '#9ccf7a', d='M92 108 L46 140 A64 64 0 0 0 92 172Z', stroke_width=3)
    + dot(70, 100, 3.5) + dot(88, 100, 3.5) + cheeks(62, 96, 110, 5, 3)
    + s('path', d='M74 112 Q79 117 84 112', stroke_width=2.5)
)

# 7. megaphone
ITEMS['megaphone'] = (
    z('rect', '#5b6b7a', x=62, y=118, width=16, height=40, rx=5, transform='rotate(-14 70 138)')
    + z('rect', '#e8735a', x=30, y=86, width=28, height=34, rx=6)
    + z('path', '#f4f4f0', d='M54 90 L136 50 Q148 102 136 158 L54 116Z')
    + z('ellipse', '#e8735a', cx=137, cy=104, rx=11, ry=54)
    + s('path', '#e8735a', d='M54 90 L54 116 L70 124 L70 82Z', stroke_width=2.5)
    + s('path', d='M160 76 Q170 104 160 132', stroke_width=3.5)
    + s('path', d='M172 62 Q186 104 172 146', stroke_width=3.5)
)

# 8. customer-support
ITEMS['customer-support'] = (
    z('path', '#8fc7e8', d='M30 44 Q30 32 42 32 L108 32 Q120 32 120 44 L120 70 Q120 82 108 82 L58 82 L42 96 L46 82 L42 82 Q30 82 30 70Z')
    + dot(56, 57, 4) + dot(75, 57, 4) + dot(94, 57, 4)
    + z('path', '#f6a6b8', d='M128 66 Q128 56 138 56 L164 56 Q174 56 174 66 L174 82 Q174 92 164 92 L160 92 L162 104 L150 92 L138 92 Q128 92 128 82Z')
    + s('path', '#f07a8a', d='M151 84 C146 80 142 76 145 72 C148 69 151 71 151 74 C151 71 154 69 157 72 C160 76 156 80 151 84Z', stroke_width=2)
    + tube('M64 156 Q64 104 106 104 Q148 104 148 156', '#5b6b7a', 7)
    + z('rect', '#7cc4b0', x=52, y=140, width=24, height=36, rx=10)
    + z('rect', '#7cc4b0', x=136, y=140, width=24, height=36, rx=10)
    + s('path', d='M64 172 Q72 188 98 186', stroke_width=4)
    + z('ellipse', '#5b6b7a', cx=104, cy=186, rx=9, ry=5)
)

# 9. delivery-truck
ITEMS['delivery-truck'] = (
    z('rect', '#f4f4f0', x=24, y=62, width=96, height=88, rx=6)
    + box(40, 92, 30, 26) + box(76, 98, 28, 20, '#f5b971') + box(54, 72, 26, 20, '#f5b971')
    + s('rect', x=24, y=62, width=96, height=88, rx=6)
    + z('path', '#8fb3e0', d='M120 88 L154 88 Q164 88 168 100 L176 118 L176 150 L120 150Z')
    + z('path', '#d8eef8', d='M130 96 L152 96 Q158 96 161 104 L166 118 L130 118Z')
    + s('rect', '#ffc94d', x=170, y=128, width=8, height=8, rx=2, stroke_width=2)
    + z('circle', '#5b6b7a', cx=52, cy=154, r=15) + s('circle', '#c9d3db', cx=52, cy=154, r=6)
    + z('circle', '#5b6b7a', cx=148, cy=154, r=15) + s('circle', '#c9d3db', cx=148, cy=154, r=6)
    + s('path', d='M14 106 L4 106 M18 122 L8 122', stroke_width=2.5)
)

# 10. warehouse-boxes
ITEMS['warehouse-boxes'] = (
    z('rect', '#8fb3e0', x=34, y=30, width=10, height=148, rx=2)
    + z('rect', '#8fb3e0', x=156, y=30, width=10, height=148, rx=2)
    + box(52, 48, 34, 26) + box(92, 54, 26, 20, '#f5b971') + box(122, 44, 30, 30)
    + box(50, 98, 26, 26, '#f5b971') + box(80, 90, 40, 34) + box(124, 102, 28, 22, '#f5b971')
    + box(54, 140, 40, 34) + box(100, 150, 24, 24, '#f5b971') + box(128, 144, 24, 30)
    + z('rect', '#e8735a', x=36, y=74, width=128, height=9, rx=2)
    + z('rect', '#e8735a', x=36, y=124, width=128, height=9, rx=2)
    + little_face(68, 158, 0.6)
)

# 11. factory-conveyor
ITEMS['factory-conveyor'] = (
    z('rect', '#5b6b7a', x=48, y=142, width=10, height=36) + z('rect', '#5b6b7a', x=142, y=142, width=10, height=36)
    + z('rect', '#c9d3db', x=22, y=124, width=156, height=22, rx=11)
    + ''.join(s('circle', '#b9a99c', cx=x, cy=135, r=6, stroke_width=2.5) for x in (36, 64, 92, 120, 148, 164))
    + box(30, 94, 32, 30) + box(84, 88, 36, 36, '#f5b971') + box(140, 98, 28, 26)
    + little_face(102, 112, 0.6)
    + z('path', '#8fc7e8', d='M76 34 L124 34 L124 50 L112 60 L88 60 L76 50Z')
    + s('path', d='M100 22 L100 34 M88 60 L84 74 M112 60 L116 74', stroke_width=4)
    + s('path', d='M178 108 L190 108 M174 96 L184 90', stroke_width=2.5)
)

# 12. office-building
_win = ''
for r in range(6):
    for c in range(3):
        _win += s('rect', '#d8eef8', x=70 + c * 22, y=46 + r * 18, width=14, height=11, rx=2, stroke_width=2)
ITEMS['office-building'] = (
    z('rect', '#c9d3db', x=128, y=88, width=40, height=88)
    + ''.join(s('rect', '#ffe27a', x=138, y=100 + r * 18, width=20, height=10, rx=2, stroke_width=2) for r in range(4))
    + z('rect', '#c9d3db', x=32, y=110, width=30, height=66)
    + ''.join(s('rect', '#ffe27a', x=40, y=120 + r * 16, width=14, height=9, rx=2, stroke_width=2) for r in range(3))
    + z('rect', '#8fb3e0', x=60, y=30, width=78, height=146, rx=3)
    + z('rect', '#5b6b7a', x=56, y=24, width=86, height=10, rx=3)
    + _win
    + z('rect', '#8b6b4f', x=88, y=156, width=22, height=20, rx=2)
    + s('path', d='M99 156 L99 176', stroke_width=2)
    + s('path', d='M22 176 L178 176', stroke_width=3)
)

# 13. office-desk
ITEMS['office-desk'] = (
    z('rect', '#d9a66b', x=40, y=128, width=12, height=50)
    + z('rect', '#d9a66b', x=118, y=128, width=46, height=50, rx=2)
    + s('path', d='M122 152 L160 152', stroke_width=2.5) + dot(141, 140, 2.5) + dot(141, 164, 2.5)
    + z('rect', '#d9a66b', x=30, y=118, width=144, height=12, rx=3)
    + z('rect', '#5b6b7a', x=88, y=100, width=16, height=18)
    + z('rect', '#5b6b7a', x=74, y=112, width=44, height=8, rx=3)
    + z('rect', '#5b6b7a', x=56, y=46, width=80, height=58, rx=6)
    + s('rect', '#8fc7e8', x=63, y=53, width=66, height=44, rx=3)
    + s('path', d='M72 66 L112 66 M72 76 L102 76 M72 86 L108 86', stroke='#ffffff', stroke_width=3)
    + z('path', '#7cc4a0', d='M154 96 Q136 88 140 70 Q156 76 154 96Z')
    + z('path', '#9ccf7a', d='M156 96 Q170 84 166 64 Q150 74 156 96Z')
    + z('path', '#e8735a', d='M144 94 L166 94 L162 118 L148 118Z')
    + z('rect', '#f4f4f0', x=34, y=108, width=34, height=10, rx=2)
)

# 14. office-chair
ITEMS['office-chair'] = (
    s('path', d='M100 150 L60 170 M100 150 L140 170 M100 150 L100 176', stroke_width=7)
    + s('path', d='M100 150 L60 170 M100 150 L140 170 M100 150 L100 176', stroke='#5b6b7a', stroke_width=3)
    + z('circle', '#5b6b7a', cx=58, cy=174, r=6) + z('circle', '#5b6b7a', cx=142, cy=174, r=6) + z('circle', '#5b6b7a', cx=100, cy=180, r=6)
    + z('rect', '#c9d3db', x=94, y=124, width=12, height=28)
    + z('rect', '#8fb3e0', x=66, y=34, width=68, height=72, rx=22)
    + s('path', d='M80 52 Q100 46 120 52', stroke='#ffffff', stroke_width=3)
    + z('rect', '#5b6b7a', x=94, y=102, width=12, height=14)
    + z('rect', '#5b6b7a', x=50, y=90, width=12, height=30, rx=4)
    + z('rect', '#5b6b7a', x=138, y=90, width=12, height=30, rx=4)
    + z('rect', '#8fb3e0', x=54, y=110, width=92, height=20, rx=10)
)

# 15. time-card
# card sticking out of the slot (drawn on top, above the slot)
ITEMS['time-card'] = (
    z('rect', '#c9d3db', x=46, y=56, width=108, height=124, rx=12)
    + z('rect', '#f5d58a', x=76, y=18, width=48, height=54, rx=3)
    + s('path', d='M84 32 L116 32 M84 42 L116 42 M84 52 L108 52', stroke_width=2.5)
    + s('rect', '#5b6b7a', x=68, y=66, width=64, height=10, rx=4, stroke_width=2.5)
    + z('circle', '#ffffff', cx=100, cy=118, r=26)
    + ''.join(dot(100 + 20 * dx, 118 + 20 * dy, 2.5) for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
    + s('path', d='M100 118 L100 104 M100 118 L111 124', stroke_width=3.5)
    + dot(100, 118, 3.5)
    + s('rect', '#e8735a', x=62, y=154, width=76, height=16, rx=6, stroke_width=2.5)
    + dot(78, 162, 4, '#ffe27a') + dot(122, 162, 4, '#9ccf7a')
)

# 16. payday-envelope
def coin(x, y, r=14):
    return z('circle', '#ffc94d', cx=x, cy=y, r=r) + s('circle', cx=x, cy=y, r=r - 5, stroke_width=2)

ITEMS['payday-envelope'] = (
    z('rect', '#f4f4f0', x=52, y=28, width=86, height=132, rx=6)
    + s('path', d='M52 52 L138 52', stroke_width=2.5)
    + z('rect', '#9ccf7a', x=66, y=16, width=56, height=30, rx=3)
    + s('circle', cx=94, cy=31, r=8, stroke_width=2)
    + dot(82, 96) + dot(108, 96) + cheeks(72, 118, 106, 6, 3.5)
    + s('path', d='M88 104 Q95 112 102 104', stroke_width=2.5)
    + s('path', d='M74 130 L116 130 M74 140 L104 140', stroke_width=2.5)
    + coin(142, 176) + coin(160, 156)
    + coin(48, 176, 12)
    + s('path', d='M164 120 L172 112 M176 132 L186 130 M156 112 L156 102', stroke_width=2.5)
)

# 17. retirement-bouquet
ITEMS['retirement-bouquet'] = (
    body('#8fb3e0', cx=96)
    + s('path', d='M86 138 L96 152 L106 138', stroke_width=2.5)
    + face(96, 96, SK, '#e8e1d8', 'smile')
    + z('path', '#9ccf7a', d='M118 182 L134 120 L160 120 L148 182Z')
    + z('circle', '#f6a6b8', cx=136, cy=112, r=12)
    + z('circle', '#ffe27a', cx=158, cy=108, r=12)
    + z('circle', '#f07a8a', cx=148, cy=90, r=12)
    + z('circle', '#ffffff', cx=166, cy=126, r=9)
    + dot(136, 112, 3, '#f07a8a') + dot(158, 108, 3, '#f5b971') + dot(148, 90, 3, '#e04b5a')
    + z('path', '#e8735a', d='M126 150 L156 150 L152 162 L128 162Z')
    + hand(130, 160)
    + s('path', '#f07a8a', d='M40 52 C35 48 32 44 35 40 C38 37 40 39 40 42 C40 39 42 37 45 40 C48 44 45 48 40 52Z', stroke_width=2)
    + s('path', d='M150 42 L156 34 M164 52 L174 48', stroke_width=2.5)
)

# 18. award-certificate
ITEMS['award-certificate'] = (
    z('rect', '#d9a66b', x=26, y=40, width=148, height=112, rx=6)
    + s('rect', '#f4f4f0', x=38, y=52, width=124, height=88, rx=2)
    + s('path', d='M66 70 L134 70', stroke_width=4)
    + s('path', d='M58 88 L142 88 M58 100 L130 100 M58 112 L110 112', stroke_width=2.5)
    + z('path', '#e8735a', d='M128 128 L120 176 L132 168 L140 178 L144 132Z')
    + z('path', '#8fb3e0', d='M146 128 L148 178 L156 168 L168 174 L158 128Z')
    + z('circle', '#ffc94d', cx=142, cy=124, r=20)
    + s('circle', '#ffe27a', cx=142, cy=124, r=12, stroke_width=2)
    + s('path', '#ffc94d', d='M142 116 L144.8 121.6 L151 122.4 L146.5 126.6 L147.6 132.8 L142 129.8 L136.4 132.8 L137.5 126.6 L133 122.4 L139.2 121.6Z', stroke_width=1.8)
)

# 19. it-support
ITEMS['it-support'] = (
    z('rect', '#5b6b7a', x=104, y=62, width=74, height=56, rx=6)
    + s('rect', '#8fc7e8', x=111, y=69, width=60, height=42, rx=3)
    + s('path', d='M128 82 L134 88 M134 82 L128 88 M148 82 L154 88 M154 82 L148 88', stroke_width=2.5)
    + s('path', d='M133 102 Q141 96 149 102', stroke_width=2.5)
    + z('rect', '#5b6b7a', x=134, y=118, width=14, height=20)
    + z('rect', '#c9d3db', x=104, y=136, width=78, height=10, rx=3)
    + body('#7cc4b0', cx=70, top=132, bottom=186)
    + s('path', d='M62 134 L62 186', stroke_width=2.5)
    + face(70, 94, SK, '#5a4033', 'smile')
    + s('path', d='M98 162 L120 130', stroke_width=11)
    + s('path', d='M98 162 L120 130', stroke='#c9d3db', stroke_width=6)
    + s('path', '#c9d3db', d='M114 128 Q112 116 122 114 L120 124 L128 126 L130 116 Q138 124 128 134 Z', stroke_width=2.5)
    + hand(98, 162)
    + s('path', d='M178 40 L184 32 M186 54 L194 52', stroke_width=2.5)
)

# 20. event-staff
ITEMS['event-staff'] = (
    body('#f5b971', cx=92)
    + face(92, 98, SK, '#2b2220', 'smile')
    + z('path', '#e8735a', d='M58 84 Q58 54 92 54 Q126 54 126 84Z')
    + z('path', '#e8735a', d='M118 78 L150 80 Q154 86 146 88 L118 86Z')
    + s('circle', '#e8735a', cx=92, cy=54, r=4, stroke_width=2)
    + s('rect', '#ffffff', x=70, y=150, width=20, height=14, rx=2, stroke_width=2.5)
    + z('rect', '#9a6a3f', x=112, y=126, width=46, height=58, rx=4)
    + s('rect', '#ffffff', x=118, y=134, width=34, height=44, rx=2, stroke_width=2.5)
    + z('rect', '#c9d3db', x=124, y=120, width=22, height=10, rx=2)
    + s('path', d='M124 146 L128 150 L134 142 M138 147 L148 147 M124 162 L128 166 L134 158 M138 163 L148 163', stroke_width=2)
    + hand(114, 164)
)
