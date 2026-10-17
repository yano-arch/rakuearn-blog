from art import z, s, dot, cheeks, face, OUT, CH
import math, random


def tube(d, color, w=6):
    """thick colored line with brown outline"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def ring(x, y, w, h, r, c, t=14, cover=False):
    """rounded-rect chain link drawn as a band; colored band shifted 4px, outlines in place"""
    band = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="{c}" stroke-width="{t}"/>'
    o = ''
    if cover:
        o += band
    o += f'<g transform="translate(4 4)">{band}</g>'
    o += s('rect', x=x - t / 2, y=y - t / 2, width=w + t, height=h + t, rx=r + t / 2)
    o += s('rect', x=x + t / 2, y=y + t / 2, width=w - t, height=h - t, rx=r - t / 2)
    return o


def poly(pts):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


def rot(pts, ang, cx=100, cy=100):
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)
    return [(cx + (x - cx) * ca - (y - cy) * sa, cy + (x - cx) * sa + (y - cy) * ca) for x, y in pts]


def rrect(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


ITEMS = {}

# 1 link-chain
ITEMS['link-chain'] = (
    ring(30, 65, 90, 50, 25, '#8fb3e0')
    + ring(80, 85, 90, 50, 25, '#f5b971', cover=True)
    + '<clipPath id="b40lk"><circle cx="122" cy="85" r="16"/></clipPath>'
    + f'<g clip-path="url(#b40lk)">{ring(30, 65, 90, 50, 25, "#8fb3e0", cover=True)}</g>'
)

# 2 qr-code
def _qr():
    o = z('rect', '#ffffff', x=36, y=36, width=128, height=128, rx=12)
    x0 = y0 = 52; m = 8; n = 12
    def finder(fx, fy):
        return (s('rect', OUT, x=fx, y=fy, width=24, height=24, rx=3, stroke='none')
                + s('rect', '#ffffff', x=fx + 4, y=fy + 4, width=16, height=16, rx=2, stroke='none')
                + s('rect', OUT, x=fx + 8, y=fy + 8, width=8, height=8, rx=1, stroke='none'))
    rnd = random.Random(40)
    for i in range(n):
        for j in range(n):
            if (i < 4 and j < 4) or (i >= n - 4 and j < 4) or (i < 4 and j >= n - 4):
                continue
            if rnd.random() < 0.5:
                o += s('rect', OUT, x=x0 + i * m, y=y0 + j * m, width=m, height=m, stroke='none')
    o += finder(x0, y0) + finder(x0 + 72, y0) + finder(x0, y0 + 72)
    o += s('rect', '#7cc4b0', x=x0 + 72, y=y0 + 72, width=24, height=24, rx=4, stroke_width=2.5)
    return o

ITEMS['qr-code'] = _qr()

# 3 barcode
def _barcode():
    o = z('rect', '#ffffff', x=30, y=52, width=140, height=96, rx=10)
    widths = [3, 1, 2, 1, 3, 2, 1, 1, 3, 1, 2, 3, 1, 2, 1, 1, 3, 2, 1, 3, 1, 2]
    x = 48
    for k, w in enumerate(widths):
        bw = w * 1.9
        if k % 2 == 0:
            o += s('rect', OUT, x=round(x, 1), y=66, width=round(bw, 1), height=68, stroke='none')
        x += bw + 2.2
    o += s('path', d='M22 100 L178 100', stroke='#e04b5a', stroke_width=4)
    return o

ITEMS['barcode'] = _barcode()

# 4 password-key
ITEMS['password-key'] = (
    z('rect', '#ffc94d', x=82, y=66, width=86, height=16, rx=5)
    + z('rect', '#ffc94d', x=146, y=80, width=12, height=20, rx=3)
    + z('rect', '#ffc94d', x=126, y=80, width=12, height=14, rx=3)
    + z('circle', '#ffc94d', cx=62, cy=74, r=30)
    + s('circle', '#ffffff', cx=54, cy=74, r=9)
    + z('rect', '#ffffff', x=30, y=122, width=140, height=44, rx=12)
    + ''.join(dot(x, 144, 6) for x in (56, 78, 100, 122))
    + s('path', d='M144 132 L144 156', stroke='#e8735a', stroke_width=3.5)
)

# 5 fingerprint
def _finger():
    o = z('circle', '#8fc7e8', cx=100, cy=100, r=68)
    o += z('ellipse', '#f6e0c4', cx=100, cy=104, rx=46, ry=56)
    cx, cy = 100, 96
    for k, (rx, ry, l, r) in enumerate([(8, 10, 1.6, 0.8), (17, 20, 1.4, 1.8), (26, 30, 1.4, 1.1),
                                         (35, 40, 0.8, 0.9)]):
        o += s('path', d=f'M{cx-rx} {cy+ry*l} L{cx-rx} {cy} A{rx} {ry} 0 0 1 {cx+rx} {cy} L{cx+rx} {cy+ry*r}',
               stroke='#9a6a3f', stroke_width=4.5)
    return o

ITEMS['fingerprint'] = _finger()

# 6 face-scan
ITEMS['face-scan'] = (
    z('path', '#8fb3e0', d='M58 162 Q60 136 100 134 Q140 136 142 162Z')
    + face(100, 98, '#ffd9b8', '#5a4033', 'smile')
    + tube('M34 62 L34 38 L58 38', '#7cc4b0', 6)
    + tube('M166 62 L166 38 L142 38', '#7cc4b0', 6)
    + tube('M34 138 L34 162 L58 162', '#7cc4b0', 6)
    + tube('M166 138 L166 162 L142 162', '#7cc4b0', 6)
    + s('path', d='M48 84 L152 84', stroke='#7cc4b0', stroke_width=4)
)

# 7 shield
ITEMS['shield'] = (
    z('path', '#8fb3e0', d='M100 30 Q128 46 158 46 Q162 124 100 172 Q38 124 42 46 Q72 46 100 30Z')
    + s('path', '#8fc7e8', d='M100 46 Q122 58 144 58 Q144 116 100 154 Q56 116 56 58 Q78 58 100 46Z', stroke='none')
    + tube('M74 100 L94 120 L130 80', '#ffffff', 10)
)

# 8 virus-alert
def _virus():
    o = z('path', '#ffc94d', d='M92 36 Q100 24 108 36 L174 156 Q180 170 164 170 L36 170 Q20 170 26 156Z')
    cx, cy = 100, 130
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        x1, y1 = cx + 22 * math.cos(a), cy + 22 * math.sin(a)
        x2, y2 = cx + 31 * math.cos(a), cy + 31 * math.sin(a)
        o += s('path', d=f'M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}', stroke_width=3)
        o += s('circle', '#9ccf7a', cx=round(x2, 1), cy=round(y2, 1), r=4.5, stroke_width=2.5)
    o += z('circle', '#9ccf7a', cx=cx, cy=cy, r=22)
    o += dot(92, 127, 3) + dot(108, 127, 3) + cheeks(86, 114, 135, 4, 2.5)
    o += s('path', d='M95 140 Q100 136 105 140', stroke_width=2.5)
    return o

ITEMS['virus-alert'] = _virus()

# 9 spam-mail
ITEMS['spam-mail'] = (
    z('rect', '#f4f4f0', x=26, y=62, width=126, height=92, rx=8)
    + s('path', d='M28 152 L76 112 M150 152 L102 112')
    + z('path', '#f6e0c4', d='M30 66 L89 116 L148 66Z')
    + z('circle', '#e04b5a', cx=146, cy=62, r=26)
    + s('rect', '#ffffff', x=142.5, y=46, width=7, height=20, rx=3.5, stroke='none')
    + dot(146, 75, 4, '#ffffff')
    + s('path', d='M178 92 L186 98 M176 40 L184 34', stroke_width=2.5)
)

# 10 notification-bell
ITEMS['notification-bell'] = (
    z('circle', '#ffc94d', cx=100, cy=160, r=11)
    + z('circle', '#ffc94d', cx=100, cy=48, r=8)
    + z('path', '#ffc94d', d='M58 144 Q66 132 66 102 Q66 58 100 56 Q134 58 134 102 Q134 132 142 144Z')
    + z('rect', '#ffc94d', x=48, y=140, width=104, height=14, rx=7)
    + dot(88, 104) + dot(112, 104) + cheeks(80, 120, 116, 6, 3.5)
    + s('path', d='M94 116 Q100 121 106 116', stroke_width=2.5)
    + z('circle', '#e04b5a', cx=138, cy=60, r=15)
    + s('path', d='M40 72 Q32 86 38 102 M164 98 Q170 110 166 124', stroke_width=3)
)

# 11 chat-bubbles
ITEMS['chat-bubbles'] = (
    z('path', '#8fc7e8', d='M48 32 L110 32 Q132 32 132 54 L132 76 Q132 98 110 98 L66 98 L42 118 L48 98 '
                         'Q26 98 26 76 L26 54 Q26 32 48 32Z')
    + dot(60, 65, 5) + dot(79, 65, 5) + dot(98, 65, 5)
    + z('path', '#f5d58a', d='M90 94 L152 94 Q174 94 174 116 L174 138 Q174 160 152 160 L152 160 L158 180 '
                          'L134 160 L90 160 Q68 160 68 138 L68 116 Q68 94 90 94Z')
    + s('path', d='M86 118 L156 118 M86 136 L136 136', stroke_width=4)
)

# 12 play-button
ITEMS['play-button'] = (
    z('rect', '#5b6b7a', x=26, y=40, width=148, height=104, rx=14)
    + z('circle', '#ffffff', cx=100, cy=92, r=30)
    + z('path', '#e8735a', d='M90 76 Q90 72 94 74 L118 89 Q121 92 118 95 L94 110 Q90 112 90 108Z')
    + s('path', d='M30 166 L170 166', stroke_width=9) + s('path', d='M30 166 L170 166', stroke='#c9d3db', stroke_width=4)
    + tube('M30 166 L96 166', '#e8735a', 4)
    + z('circle', '#ffffff', cx=96, cy=166, r=8)
)

# 13 live-stream
ITEMS['live-stream'] = (
    z('path', '#c9d3db', d='M126 100 L170 76 Q176 74 176 80 L176 140 Q176 146 170 144 L126 120Z')
    + z('rect', '#8fb3e0', x=26, y=70, width=108, height=82, rx=16)
    + z('circle', '#e04b5a', cx=52, cy=96, r=10)
    + s('rect', '#ffffff', x=74, y=86, width=44, height=20, rx=5, stroke_width=2.5)
    + z('circle', '#f4f4f0', cx=78, cy=128, r=10) + z('circle', '#f4f4f0', cx=104, cy=128, r=10)
    + s('path', d='M40 56 Q52 44 64 56 M30 48 Q52 26 74 48', stroke='#e04b5a', stroke_width=4)
)

# 14 thumbs-up-like
ITEMS['thumbs-up-like'] = (
    z('rect', '#8fb3e0', x=34, y=96, width=30, height=76, rx=6)
    + z('path', '#ffd9b8', d='M64 100 L82 100 Q96 88 98 66 Q100 42 116 44 Q132 48 126 74 L122 94 L146 94 '
                          'Q160 96 158 110 Q156 120 152 122 Q162 128 154 140 Q160 150 150 156 Q154 168 140 170 L64 170Z')
    + s('path', d='M152 122 L126 122 M154 140 L128 140 M150 156 L128 156', stroke_width=2.5)
    + dot(50, 158, 3.5, '#ffffff')
    + s('path', d='M150 52 L160 42 M160 70 L174 66 M138 36 L140 26', stroke_width=3)
)

# 15 comment
ITEMS['comment'] = (
    z('path', '#f5d58a', d='M60 36 L140 36 Q172 36 172 68 L172 112 Q172 144 140 144 L84 144 L52 172 L58 144 '
                          'Q28 144 28 112 L28 68 Q28 36 60 36Z')
    + dot(70, 90, 8) + dot(100, 90, 8) + dot(130, 90, 8)
)

# 16 database
ITEMS['database'] = (
    z('path', '#8fb3e0', d='M46 54 L46 150 A54 17 0 0 0 154 150 L154 54Z')
    + s('path', d='M46 86 A54 17 0 0 0 154 86 M46 118 A54 17 0 0 0 154 118')
    + z('ellipse', '#8fc7e8', cx=100, cy=54, rx=54, ry=17)
    + dot(134, 90, 5, '#9ccf7a') + dot(134, 122, 5, '#9ccf7a') + dot(134, 154, 5, '#ffc94d')
    + s('path', d='M62 92 L96 98 M62 124 L96 130 M62 156 L96 162', stroke_width=3)
)

# 17 satellite
def _sat():
    A = -30
    o = ''
    # connecting rod
    o += s('path', d=poly(rot([(70, 98), (130, 98), (130, 102), (70, 102)], A)), stroke_width=3)
    for px in (26, 128):
        o += z('path', '#8fb3e0', d=poly(rot(rrect(px, 82, 46, 36), A)))
        for gx in (px + 15.3, px + 30.7):
            a, b = rot([(gx, 82), (gx, 118)], A)
            o += s('path', d=f'M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}', stroke_width=2.5)
        a, b = rot([(px, 100), (px + 46, 100)], A)
        o += s('path', d=f'M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}', stroke_width=2.5)
    # dish on top of body
    a, b = rot([(100, 76), (100, 62)], A)
    o += s('path', d=f'M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f}', stroke_width=3)
    d1, d2, d3 = rot([(84, 66), (100, 52), (116, 66)], A)
    c1, c2 = rot([(100, 84)], A)[0], rot([(100, 76)], A)[0]
    o += z('path', '#f4f4f0', d=f'M{d1[0]:.1f} {d1[1]:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {d3[0]:.1f} {d3[1]:.1f}Z')
    o += z('path', '#f5d58a', d=poly(rot(rrect(78, 76, 44, 48), A)))
    o += dot(*[round(v, 1) for v in rot([(92, 98)], A)[0]], 3.5) + dot(*[round(v, 1) for v in rot([(108, 98)], A)[0]], 3.5)
    ch = rot([(87, 108), (113, 108)], A)
    o += ''.join(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="5" ry="3" fill="{CH}" stroke="none"/>' for x, y in ch)
    m1, m2, m3 = rot([(96, 108), (100, 112), (104, 108)], A)
    o += s('path', d=f'M{m1[0]:.1f} {m1[1]:.1f} Q{m2[0]:.1f} {m2[1]:.1f} {m3[0]:.1f} {m3[1]:.1f}', stroke_width=2.5)
    o += s('path', d='M44 70 Q46 52 60 44 M34 66 Q36 38 58 30', stroke_width=3)
    o += dot(160, 40, 3, '#ffc94d') + dot(40, 46, 2.5, '#ffc94d') + dot(168, 150, 3, '#ffc94d')
    return o

ITEMS['satellite'] = _sat()

# 18 antenna-tower
ITEMS['antenna-tower'] = (
    s('path', d='M92 84 L108 84 M86 106 L114 106 M80 130 L120 130 M74 154 L126 154', stroke_width=3)
    + s('path', d='M92 84 L114 106 L80 130 L126 154 M108 84 L86 106 L120 130 L74 154', stroke_width=3)
    + tube('M100 60 L68 176', '#e8735a', 6)
    + tube('M100 60 L132 176', '#e8735a', 6)
    + z('circle', '#ffc94d', cx=100, cy=54, r=10)
    + s('path', d='M76 40 Q68 54 76 68 M124 40 Q132 54 124 68', stroke_width=3.5)
    + s('path', d='M62 30 Q48 54 62 78 M138 30 Q152 54 138 78', stroke_width=3.5)
    + s('path', d='M48 176 L152 176', stroke_width=3)
)

# 19 charging-cable
ITEMS['charging-cable'] = (
    tube('M126 108 C126 178 52 74 52 128', '#f4f4f0', 6)
    + z('rect', '#c9d3db', x=116, y=28, width=20, height=20, rx=3)
    + z('rect', '#ffffff', x=106, y=44, width=40, height=62, rx=10)
    + z('path', '#ffc94d', d='M130 56 L114 78 L124 78 L120 96 L138 72 L128 72 L132 56Z')
    + z('rect', '#5b6b7a', x=34, y=124, width=36, height=34, rx=8)
    + z('rect', '#c9d3db', x=40, y=156, width=24, height=20, rx=2)
    + s('rect', OUT, x=46, y=162, width=12, height=6, rx=1, stroke='none')
    + s('path', d='M154 40 L164 34 M156 60 L168 60 M96 36 L90 28', stroke_width=2.5)
)

# 20 power-plug
ITEMS['power-plug'] = (
    z('rect', '#f4f4f0', x=112, y=46, width=64, height=96, rx=14)
    + s('rect', OUT, x=129, y=74, width=7, height=20, rx=2.5, stroke='none')
    + s('rect', OUT, x=152, y=74, width=7, height=20, rx=2.5, stroke='none')
    + cheeks(124, 164, 106, 5, 3)
    + s('path', d='M138 108 Q144 114 150 108', stroke_width=2.5)
    + tube('M48 96 Q24 98 28 132 Q32 168 84 168', '#5b6b7a', 6)
    + z('rect', '#c9d3db', x=86, y=80, width=18, height=7, rx=2)
    + z('rect', '#c9d3db', x=86, y=105, width=18, height=7, rx=2)
    + z('rect', '#8fb3e0', x=46, y=70, width=42, height=54, rx=10)
    + s('path', d='M96 52 L102 44 M84 50 L84 40 M106 132 L114 140', stroke_width=2.5)
)
