import math
from art import z, s, dot, cheeks, face, OUT, CH


def tube(d, color, w=6):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def seg(x1, y1, x2, y2, w, color):
    """rounded bar from (x1,y1) to (x2,y2) with offset fill"""
    L = math.hypot(x2 - x1, y2 - y1)
    a = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return z('rect', color, x=f'{x1 - w/2:.1f}', y=f'{y1 - w/2:.1f}', width=f'{L + w:.1f}', height=w,
             rx=w / 2, transform=f'rotate({a:.1f} {x1} {y1})')


def phone(x, y, w, h, body='#5b6b7a', screen='#d8eef8'):
    return (z('rect', body, x=x, y=y, width=w, height=h, rx=12)
            + s('rect', screen, x=x + 7, y=y + 14, width=w - 14, height=h - 30, rx=4)
            + dot(x + w / 2, y + h - 8, 3, screen))


ITEMS = {}

# 1 solar panel
rays = ' '.join(f'M{52 + 30*math.cos(math.radians(a)):.0f} {48 + 30*math.sin(math.radians(a)):.0f} '
                f'L{52 + 40*math.cos(math.radians(a)):.0f} {48 + 40*math.sin(math.radians(a)):.0f}'
                for a in range(0, 360, 45))
ITEMS['solar-panel'] = (
    s('path', d=rays, stroke_width=3)
    + z('circle', '#ffc94d', cx=52, cy=48, r=22)
    + dot(45, 47, 2.6) + dot(59, 47, 2.6) + cheeks(40, 64, 54, 4, 2.5)
    + s('path', d='M49 54 Q52 57 55 54', stroke_width=2)
    + s('path', d='M92 150 L86 178 M136 150 L142 178', stroke_width=5)
    + z('path', '#8fb3e0', d='M78 88 L176 88 L162 150 L46 150Z')
    + s('path', d='M102.5 88 L75 150 M127 88 L104 150 M151.5 88 L133 150 M62 119 L169 119', stroke_width=2.5)
    + s('path', d='M86 94 L92 94 M110 94 L116 94', stroke='#ffffff', stroke_width=3)
    + s('path', d='M30 180 L170 180', stroke_width=2.5)
)

# 2 EV charging
ITEMS['ev-charging'] = (
    tube('M152 126 Q140 150 128 128', '#5b6b7a', 5)
    + z('path', '#7cc4b0', d='M20 150 L20 126 Q22 114 36 112 L50 110 L66 90 Q70 86 78 86 L104 86 '
                             'Q112 86 116 92 L126 110 Q132 112 132 122 L132 150Z')
    + s('path', '#d8eef8', d='M71 94 L88 94 L88 110 L58 110Z', stroke_width=2.5)
    + s('path', '#d8eef8', d='M94 94 L106 94 Q110 94 112 98 L118 110 L94 110Z', stroke_width=2.5)
    + dot(28, 124, 4, '#ffe27a')
    + z('rect', '#5b6b7a', x=124, y=120, width=10, height=12, rx=2)
    + z('circle', '#5b6b7a', cx=46, cy=152, r=14) + s('circle', '#c9d3db', cx=46, cy=152, r=5)
    + z('circle', '#5b6b7a', cx=108, cy=152, r=14) + s('circle', '#c9d3db', cx=108, cy=152, r=5)
    + z('rect', '#c9d3db', x=146, y=58, width=34, height=118, rx=8)
    + s('rect', '#ffffff', x=152, y=68, width=22, height=30, rx=3, stroke_width=2.5)
    + s('path', '#ffc94d', d='M166 71 L157 84 L163 84 L159 95 L169 80 L163 80Z', stroke_width=2)
    + s('path', d='M14 176 L186 176', stroke_width=2.5)
)

# 3 online shopping
ITEMS['online-shopping'] = (
    phone(46, 26, 84, 150)
    + s('path', d='M60 70 L70 70 L76 82', stroke_width=3)
    + z('path', '#ffc94d', d='M74 82 L120 82 L112 116 L82 116Z')
    + s('path', d='M80 98 L116 98 M90 82 L93 116 M104 82 L102 116', stroke_width=2)
    + dot(86, 126, 5) + dot(108, 126, 5)
    + s('rect', '#f07a8a', x=62, y=142, width=52, height=10, rx=5, stroke_width=2.5)
    + s('path', d='M146 128 Q148 104 159 104 Q170 104 172 128', stroke_width=3.5)
    + z('path', '#f07a8a', d='M138 124 L180 124 L176 176 L142 176Z')
    + dot(152, 148, 2.6) + dot(166, 148, 2.6) + s('path', d='M156 156 Q159 159 162 156', stroke_width=2)
)

# 4 mobile payment
ITEMS['mobile-payment'] = (
    z('rect', '#5b6b7a', x=30, y=76, width=74, height=104, rx=10)
    + s('rect', '#d8eef8', x=40, y=86, width=54, height=36, rx=4)
    + s('path', d='M56 104 L64 112 L80 94', stroke='#7cc4a0', stroke_width=4)
    + ''.join(dot(x, y, 4, '#c9d3db') for x in (50, 67, 84) for y in (138, 154))
    + s('path', d='M108 70 Q116 62 124 70 M100 62 Q116 46 132 62', stroke_width=3)
    + z('rect', '#8fb3e0', x=120, y=36, width=50, height=92, rx=9, transform='rotate(-18 145 82)')
    + s('rect', '#ffffff', x=126, y=46, width=38, height=66, rx=3, transform='rotate(-18 145 82)', stroke_width=2.5)
    + dot(140, 76, 3) + dot(154, 72, 3) + cheeks(133, 162, 82, 4, 2.5)
    + s('path', d='M143 86 Q149 89 153 84', stroke_width=2)
)

# 5 GPS phone
ITEMS['gps-phone'] = (
    z('rect', '#5b6b7a', x=56, y=40, width=88, height=140, rx=12)
    + s('rect', '#f6e0c4', x=63, y=54, width=74, height=110, rx=4)
    + s('path', d='M63 120 Q90 112 100 130 Q110 148 137 140', stroke='#8fc7e8', stroke_width=7)
    + s('path', d='M63 84 L137 96 M86 54 L80 164 M120 54 L126 164', stroke='#ffffff', stroke_width=6)
    + s('rect', '#9ccf7a', x=96, y=140, width=18, height=18, rx=4, stroke_width=2)
    + dot(100, 172, 3, '#d8eef8')
    + z('path', '#e04b5a', d='M100 108 C88 90 74 80 74 62 A26 26 0 0 1 126 62 C126 80 112 90 100 108Z')
    + s('circle', '#ffffff', cx=100, cy=62, r=10)
)

# 6 smart home
ITEMS['smart-home'] = (
    s('path', d='M80 38 Q100 20 120 38 M88 46 Q100 36 112 46', stroke_width=3.5)
    + dot(100, 54, 4)
    + z('rect', '#f5d58a', x=40, y=110, width=96, height=66)
    + z('path', '#8fb3e0', d='M28 110 L88 62 L148 110Z')
    + z('rect', '#8b6b4f', x=52, y=130, width=24, height=46, rx=3)
    + z('rect', '#ffe27a', x=90, y=120, width=32, height=28, rx=3)
    + s('path', d='M106 120 L106 148 M90 134 L122 134', stroke_width=2)
    + dot(70, 154, 2.5)
    + z('rect', '#7cc4b0', x=148, y=118, width=32, height=58, rx=7)
    + s('rect', '#d8eef8', x=153, y=126, width=22, height=38, rx=3, stroke_width=2)
    + s('path', d='M158 140 Q164 134 170 140 M161 146 Q164 143 167 146', stroke_width=2)
    + s('path', d='M150 104 Q160 94 170 104', stroke_width=2.5)
    + s('path', d='M20 176 L186 176', stroke_width=2.5)
)

# 7 SD card
ITEMS['sd-card'] = (
    z('path', '#8fb3e0', d='M64 30 L124 30 L144 50 L144 170 Q144 176 138 176 L62 176 Q56 176 56 170 L56 38 Q56 30 64 30Z')
    + ''.join(s('rect', '#ffc94d', x=x, y=38, width=9, height=22, rx=2, stroke_width=2) for x in (66, 81, 96, 111))
    + z('rect', '#ffffff', x=68, y=94, width=64, height=66, rx=6)
    + dot(88, 124, 3.5) + dot(112, 124, 3.5) + cheeks(80, 120, 134, 5, 3)
    + s('path', d='M95 134 Q100 139 105 134', stroke_width=2.5)
)

# 8 floppy disk
ITEMS['save-disk'] = (
    z('path', '#8fb3e0', d='M40 34 L146 34 L168 56 L168 160 Q168 168 160 168 L40 168 Q32 168 32 160 L32 42 Q32 34 40 34Z')
    + z('rect', '#c9d3db', x=62, y=34, width=74, height=44, rx=3)
    + s('rect', '#5b6b7a', x=112, y=42, width=14, height=28, rx=2, stroke_width=2.5)
    + z('rect', '#ffffff', x=52, y=100, width=96, height=68, rx=4)
    + s('path', d='M64 120 L136 120 M64 136 L136 136 M64 152 L112 152', stroke='#b9a99c', stroke_width=2.5)
)

# 9 cursor click
ITEMS['cursor-click'] = (
    z('rect', '#7cc4b0', x=34, y=52, width=96, height=40, rx=20)
    + s('path', d='M82 34 L82 24 M56 44 L48 36 M108 44 L116 36 M44 112 L36 120', stroke_width=3)
    + z('path', '#ffffff', d='M82 72 L82 170 L104 150 L118 180 L136 172 L122 142 L152 140Z')
)

# 10 loading
ld = ''
for i in range(8):
    a = math.radians(-90 + i * 45)
    r = 13 - i * 0.8
    col = '#8fb3e0' if i < 4 else '#c9d3db'
    ld += z('circle', col, cx=f'{98 + 46*math.cos(a):.1f}', cy=f'{82 + 46*math.sin(a):.1f}', r=f'{r:.1f}')
ITEMS['loading'] = (
    ld
    + z('rect', '#f4f4f0', x=34, y=152, width=130, height=22, rx=11)
    + s('rect', '#7cc4b0', x=34, y=152, width=78, height=22, rx=11)
)

# 11 warning
ITEMS['error-warning'] = (
    z('path', '#ffc94d', d='M88 40 Q100 22 112 40 L172 146 Q180 164 160 164 L40 164 Q20 164 28 146Z')
    + s('path', d='M100 72 L100 118', stroke_width=14)
    + dot(100, 142, 8)
)

# 12 folder
ITEMS['folder'] = (
    z('path', '#f5b971', d='M30 62 Q30 52 40 52 L80 52 L92 66 L162 66 Q170 66 170 74 L170 168 L30 168Z')
    + z('rect', '#f4f4f0', x=56, y=42, width=96, height=74, rx=3, transform='rotate(6 104 80)')
    + z('rect', '#ffffff', x=44, y=48, width=96, height=74, rx=3, transform='rotate(-4 92 84)')
    + s('path', d='M58 66 L118 62 M59 78 L126 74', stroke='#b9a99c', stroke_width=2.5)
    + z('path', '#ffc94d', d='M22 98 Q22 90 30 90 L172 90 Q180 90 179 98 L170 166 Q169 174 160 174 L40 174 Q32 174 31 166Z')
)

# 13 trash
ITEMS['trash-delete'] = (
    z('rect', '#5b6b7a', x=82, y=34, width=36, height=18, rx=5)
    + z('path', '#8fb3e0', d='M50 70 L150 70 L140 172 Q139 178 132 178 L68 178 Q61 178 60 172Z')
    + s('path', d='M78 90 L82 158 M100 90 L100 158 M122 90 L118 158', stroke_width=3)
    + z('rect', '#5b6b7a', x=38, y=50, width=124, height=20, rx=6)
)

# 14 photo
ITEMS['photo-gallery'] = (
    z('rect', '#f6a6b8', x=52, y=34, width=118, height=96, rx=6, transform='rotate(8 111 82)')
    + z('rect', '#ffffff', x=26, y=66, width=128, height=106, rx=6)
    + s('rect', '#8fc7e8', x=36, y=76, width=108, height=86, rx=3)
    + s('circle', '#ffc94d', cx=120, cy=98, r=11, stroke_width=2.5)
    + s('path', '#9ccf7a', d='M36 162 L70 112 L94 144 L110 124 L144 162Z', stroke_width=2.5)
)

# 15 microphone
ITEMS['microphone'] = (
    s('path', d='M100 134 L100 166', stroke_width=8)
    + z('ellipse', '#5b6b7a', cx=100, cy=172, rx=42, ry=9)
    + tube('M58 84 Q58 134 100 134 Q142 134 142 84', '#5b6b7a', 6)
    + z('rect', '#c9d3db', x=72, y=26, width=56, height=96, rx=28)
    + s('path', d='M80 46 L120 46 M76 60 L124 60 M74 74 L126 74', stroke_width=2.5)
    + s('rect', '#5b6b7a', x=72, y=86, width=56, height=10, stroke_width=2.5)
    + dot(88, 106, 3) + dot(112, 106, 3) + cheeks(80, 120, 113, 4, 2.5)
    + s('path', d='M96 111 Q100 115 104 111', stroke_width=2)
)

# 16 game console
ITEMS['game-console'] = (
    z('rect', '#f07a8a', x=22, y=58, width=156, height=88, rx=30)
    + s('rect', '#5b6b7a', x=62, y=68, width=76, height=64, rx=5)
    + s('rect', '#d8eef8', x=68, y=74, width=64, height=52, rx=3, stroke_width=2)
    + s('path', '#9ccf7a', d='M68 116 Q84 100 100 116 Q114 106 132 116 L132 126 L68 126Z', stroke_width=2)
    + s('circle', '#ffc94d', cx=118, cy=88, r=6, stroke_width=2)
    + s('path', '#5b6b7a', d='M38 96 L46 96 L46 88 L54 88 L54 96 L62 96 L62 104 L54 104 L54 112 L46 112 L46 104 L38 104Z', stroke_width=2)
    + s('circle', '#ffe27a', cx=152, cy=94, r=7, stroke_width=2.5)
    + s('circle', '#7cc4b0', cx=164, cy=108, r=7, stroke_width=2.5)
)

# 17 webcam
ITEMS['webcam'] = (
    s('path', d='M100 128 L100 150', stroke_width=8)
    + z('path', '#c9d3db', d='M70 150 L130 150 L140 174 L60 174Z')
    + z('rect', '#5b6b7a', x=36, y=44, width=128, height=86, rx=40)
    + z('circle', '#c9d3db', cx=100, cy=87, r=30)
    + s('circle', '#2b2220', cx=100, cy=87, r=17)
    + dot(94, 81, 5, '#ffffff')
    + dot(146, 66, 4.5, '#9ccf7a')
)

# 18 cloud computing
ITEMS['cloud-computing'] = (
    s('path', d='M60 108 L44 150 M100 112 L100 150 M140 108 L156 150 M58 160 L86 160 M114 160 L142 160', stroke_width=3)
    + z('path', '#8fc7e8', d='M54 116 Q26 116 28 92 Q30 70 54 72 Q58 38 92 38 Q118 38 128 60 '
                             'Q144 50 158 60 Q170 70 164 84 Q180 90 176 104 Q172 116 152 116Z')
    + dot(88, 82, 3.5) + dot(112, 82, 3.5) + cheeks(78, 122, 92, 6, 3.5)
    + s('path', d='M94 92 Q100 98 106 92', stroke_width=2.5)
    + z('rect', '#f5b971', x=30, y=146, width=28, height=28, rx=7)
    + z('rect', '#7cc4b0', x=86, y=146, width=28, height=28, rx=7)
    + z('rect', '#f07a8a', x=142, y=146, width=28, height=28, rx=7)
)

# 19 robot arm
ITEMS['robot-arm'] = (
    z('rect', '#d9a66b', x=136, y=146, width=40, height=30, rx=3)
    + s('path', d='M136 158 L176 158', stroke_width=2)
    + seg(66, 142, 100, 74, 22, '#ffc94d')
    + seg(100, 74, 154, 92, 18, '#ffc94d')
    + z('rect', '#5b6b7a', x=146, y=98, width=16, height=14, rx=3)
    + s('path', d='M146 112 L144 134 M162 112 L164 134', stroke_width=6)
    + s('path', d='M146 112 L144 134 M162 112 L164 134', stroke='#c9d3db', stroke_width=2)
    + z('circle', '#5b6b7a', cx=100, cy=74, r=12) + s('circle', '#c9d3db', cx=100, cy=74, r=4, stroke_width=2)
    + z('circle', '#5b6b7a', cx=154, cy=92, r=10)
    + z('path', '#f5b971', d='M42 164 Q42 136 66 136 Q90 136 90 164Z')
    + z('circle', '#5b6b7a', cx=66, cy=142, r=12) + s('circle', '#c9d3db', cx=66, cy=142, r=4, stroke_width=2)
    + z('rect', '#5b6b7a', x=30, y=162, width=72, height=14, rx=4)
    + s('path', d='M20 176 L186 176', stroke_width=2.5)
)

# 20 smartphone
icons = ''
cols = ['#f07a8a', '#ffc94d', '#7cc4b0', '#8fb3e0', '#a98bd0', '#9ccf7a', '#f5b971', '#e8735a', '#8fc7e8']
for i, c in enumerate(cols):
    icons += s('rect', c, x=74 + (i % 3) * 19, y=52 + (i // 3) * 20, width=13, height=13, rx=3, stroke_width=2)
ITEMS['smartphone'] = (
    phone(62, 28, 76, 148)
    + s('rect', '#5b6b7a', x=88, y=34, width=24, height=4, rx=2, stroke_width=1.5)
    + icons
    + s('rect', '#ffffff', x=74, y=118, width=52, height=20, rx=4, stroke_width=2)
)
