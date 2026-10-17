from math import cos, sin, pi
from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186, w=36):
    return z('path', fill, d=f'M{cx-w} {bottom} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bottom}Z')


def hand(x, y, c=SK, r=8):
    return z('circle', c, cx=x, cy=y, r=r)


def tube(d, color, w=6):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def sface(cx, cy, r, skin, hair, mouth='smile'):
    """smaller version of art.face (r = head radius)"""
    k = r / 34
    f = lambda v: f'{v:.1f}'
    o = z('circle', skin, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=(f'M{f(cx-34*k)} {f(cy-2*k)} Q{f(cx-32*k)} {f(cy-36*k)} {cx} {f(cy-35*k)} '
                            f'Q{f(cx+32*k)} {f(cy-36*k)} {f(cx+34*k)} {f(cy-2*k)} Q{f(cx+20*k)} {f(cy-18*k)} {cx} {f(cy-17*k)} '
                            f'Q{f(cx-20*k)} {f(cy-18*k)} {f(cx-34*k)} {f(cy-2*k)}Z'))
    dr = max(2.6, 3.5 * k)
    o += dot(cx - 12 * k, cy + 2 * k, dr) + dot(cx + 12 * k, cy + 2 * k, dr)
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, 7 * k, 4 * k)
    if mouth == 'smile':
        o += s('path', d=f'M{f(cx-6*k)} {f(cy+16*k)} Q{cx} {f(cy+21*k)} {f(cx+6*k)} {f(cy+16*k)}', stroke_width=2.5)
    else:
        o += s('path', '#c0504d', d=f'M{f(cx-7*k)} {f(cy+14*k)} Q{cx} {f(cy+27*k)} {f(cx+7*k)} {f(cy+14*k)}Z', stroke_width=2.2)
    return o


def tie(cx, y, c='#e8735a', k=1.0):
    return z('path', c, d=f'M{cx-4*k} {y} L{cx+4*k} {y} L{cx+6*k} {y+20*k} L{cx} {y+27*k} L{cx-6*k} {y+20*k}Z')


def gear_d(cx, cy, R, r, n=8):
    pts = []
    for i in range(n):
        a = 2 * pi * i / n
        w = pi / n * 0.55
        for ang, rad in ((a - w * 1.25, r), (a - w * 0.7, R), (a + w * 0.7, R), (a + w * 1.25, r)):
            pts.append(f'{cx + rad * cos(ang):.1f} {cy + rad * sin(ang):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


# 1. factory-worker: goggles on forehead, big gloves, carrying a box
HR = '#2b2220'
ITEMS['factory-worker'] = (
    body('#8fb3e0')
    + s('path', '#7c9bd0', d='M80 186 L80 156 L120 156 L120 186Z', stroke_width=2.5)
    + s('path', d='M82 156 L78 140 M118 156 L122 140', stroke_width=2.5)
    + face(100, 100, SK, HR, 'smile')
    + s('path', d='M66 80 Q100 70 134 80', stroke='#5b6b7a', stroke_width=6)
    + z('rect', '#8fc7e8', x=74, y=66, width=22, height=17, rx=7)
    + z('rect', '#8fc7e8', x=104, y=66, width=22, height=17, rx=7)
    + s('path', d='M96 74 L104 74', stroke_width=3)
    + s('path', d='M78 71 L84 69', stroke='#ffffff', stroke_width=2.5)
    + s('path', d='M108 71 L114 69', stroke='#ffffff', stroke_width=2.5)
    + z('rect', '#d9a66b', x=68, y=146, width=64, height=38, rx=3)
    + s('path', d='M68 156 L132 156 M100 146 L100 156', stroke_width=2.5)
    + z('path', '#f5b971', d='M54 160 Q52 146 64 146 Q76 148 74 162 Q72 172 62 172 Q54 170 54 160Z')
    + z('path', '#f5b971', d='M146 160 Q148 146 136 146 Q124 148 126 162 Q128 172 138 172 Q146 170 146 160Z')
)

# 2. mechanic: wrench raised, big tire beside
HR = '#5a4033'
ITEMS['mechanic'] = (
    z('circle', '#5b6b7a', cx=50, cy=150, r=30)
    + s('circle', '#c9d3db', cx=50, cy=150, r=14)
    + dot(50, 150, 4)
    + s('path', d='M34 128 L38 136 M66 128 L62 136 M24 156 L32 154 M76 156 L68 154', stroke='#ffffff', stroke_width=2)
    + body('#7cc4b0', cx=118)
    + s('path', d='M118 140 L118 186', stroke_width=2.5)
    + s('rect', '#ffffff', x=124, y=152, width=12, height=10, rx=2, stroke_width=2)
    + face(118, 100, SK, HR, 'open')
    + z('path', '#e8735a', d='M84 88 Q84 60 118 60 Q152 60 152 88Z')
    + z('path', '#e8735a', d='M84 84 L60 90 Q56 92 60 94 L86 92Z')
    + s('path', d='M150 154 Q160 140 158 124', stroke_width=12)
    + s('path', d='M150 154 Q160 140 158 124', stroke='#7cc4b0', stroke_width=6)
    + z('rect', '#c9d3db', x=153, y=74, width=11, height=44, rx=4)
    + z('path', '#c9d3db', d='M147 80 Q142 62 150 52 L154 64 L164 64 L167 52 Q176 62 170 80Z')
    + hand(158, 118)
    + s('path', d='M172 98 L180 96 M174 112 L182 114', stroke_width=2.5)
)

# 3. astronaut
HR = '#5a4033'
ITEMS['astronaut'] = (
    s('path', '#ffe27a', d='M34 44 L37 52 L45 54 L37 57 L34 65 L31 57 L23 54 L31 52Z', stroke_width=2)
    + s('path', '#ffe27a', d='M166 120 L168 126 L174 128 L168 130 L166 136 L164 130 L158 128 L164 126Z', stroke_width=2)
    + dot(160, 40, 3, '#ffe27a') + dot(40, 120, 3, '#ffe27a')
    + z('rect', '#c9d3db', x=60, y=128, width=80, height=50, rx=10)
    + z('path', '#f4f4f0', d='M58 186 Q58 136 100 134 Q142 136 142 186Z')
    + z('rect', '#8fb3e0', x=82, y=150, width=36, height=22, rx=4)
    + dot(92, 158, 3.5, '#e04b5a') + dot(104, 158, 3.5, '#ffc94d') + s('path', d='M88 166 L112 166', stroke_width=2)
    + z('circle', '#f4f4f0', cx=100, cy=90, r=50)
    + s('circle', '#d8eef8', cx=100, cy=92, r=40, stroke_width=2.5)
    + face(100, 96, SK, HR, 'open')
    + s('path', d='M70 72 Q76 58 92 54', stroke='#ffffff', stroke_width=5)
    + z('rect', '#c9d3db', x=144, y=80, width=10, height=22, rx=4)
)

# 4. archaeologist: safari hat, brush and bone
HR = '#9a6a3f'
ITEMS['archaeologist'] = (
    body('#f5d58a')
    + s('path', d='M88 138 L100 150 L112 138', stroke_width=2.5)
    + s('rect', '#f5d58a', x=74, y=156, width=16, height=14, rx=2, stroke_width=2.5)
    + face(100, 102, SK, HR, 'smile')
    + z('path', '#d9a66b', d='M70 80 Q70 48 100 46 Q130 48 130 80Z')
    + s('rect', '#8b6b4f', x=70, y=70, width=60, height=8, stroke_width=2.5)
    + z('ellipse', '#d9a66b', cx=100, cy=81, rx=54, ry=10)
    + z('rect', '#f4f4f0', x=44, y=164, width=58, height=12, rx=6)
    + z('circle', '#f4f4f0', cx=42, cy=163, r=7) + z('circle', '#f4f4f0', cx=42, cy=177, r=7)
    + z('circle', '#f4f4f0', cx=104, cy=163, r=7) + z('circle', '#f4f4f0', cx=104, cy=177, r=7)
    + s('rect', '#f4f4f0', x=44, y=164, width=58, height=12, stroke='none')
    + s('path', d='M44 164 L102 164 M44 176 L102 176', stroke_width=3)
    + s('path', d='M140 150 L160 116', stroke_width=9)
    + s('path', d='M140 150 L160 116', stroke='#9a6a3f', stroke_width=4)
    + z('path', '#f5b971', d='M154 120 L166 126 L176 104 Q172 96 164 98Z')
    + s('path', d='M166 100 L163 106 M170 102 L167 108', stroke_width=1.8)
    + hand(140, 152)
)

# 5. architect: blueprint roll under arm, glasses
HR = '#2b2220'
ITEMS['architect'] = (
    body('#f4f4f0')
    + s('path', d='M88 138 L100 150 L112 138', stroke_width=2.5)
    + z('path', '#5b6b7a', d='M64 186 Q66 146 86 140 L90 186Z')
    + z('path', '#5b6b7a', d='M136 186 Q134 146 114 140 L110 186Z')
    + face(100, 98, SK, HR, 'smile')
    + s('circle', cx=88, cy=100, r=8, stroke_width=2) + s('circle', cx=112, cy=100, r=8, stroke_width=2)
    + s('path', d='M96 100 L104 100', stroke_width=2)
    + z('rect', '#8fc7e8', x=40, y=146, width=124, height=20, rx=4, transform='rotate(-22 100 156)')
    + s('path', d='M66 167 L62 155 M84 160 L80 148 M120 146 L116 134 M138 139 L134 127', stroke='#ffffff', stroke_width=2,
        transform='')
    + z('ellipse', '#d8eef8', cx=158, cy=133, rx=6, ry=11, transform='rotate(-22 158 133)')
    + s('circle', cx=158, cy=133, r=3, stroke_width=2)
    + hand(86, 166) + hand(116, 152)
)

# 6. engineer: white hard hat and a gear
HR = '#5a4033'
ITEMS['engineer'] = (
    body('#8fb3e0', cx=88)
    + s('path', d='M76 138 L88 150 L100 138', stroke_width=2.5)
    + s('rect', '#ffe27a', x=56, y=160, width=64, height=7, stroke_width=2)
    + face(88, 102, SK, HR, 'smile')
    + z('path', '#f4f4f0', d='M54 86 Q54 50 88 48 Q122 50 122 86Z')
    + s('path', d='M88 50 L88 84', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=46, y=82, width=84, height=9, rx=4)
    + z('path', '#c9d3db', d=gear_d(148, 128, 30, 23, 8))
    + s('circle', '#f4f4f0', cx=148, cy=128, r=9)
    + s('path', d='M150 46 L150 60 M144 52 L156 52', stroke='#ffc94d', stroke_width=3)
    + s('path', d='M178 70 L178 80 M173 75 L183 75', stroke='#ffc94d', stroke_width=3)
    + hand(122, 150) + hand(150, 162)
)

# 7. translator: headset, two speech bubbles with different "languages"
HR = '#2b2220'
ITEMS['translator'] = (
    z('path', '#8fc7e8', d='M22 36 Q22 24 34 24 L74 24 Q86 24 86 36 L86 58 Q86 70 74 70 L50 70 L38 82 L40 70 L34 70 Q22 70 22 58Z')
    + s('path', d='M34 40 Q40 34 46 40 Q52 46 58 40 Q64 34 70 40 M34 54 Q40 48 46 54 Q52 60 58 54', stroke_width=2.5)
    + z('path', '#f6a6b8', d='M114 36 Q114 24 126 24 L166 24 Q178 24 178 36 L178 58 Q178 70 166 70 L160 70 L162 82 L150 70 L126 70 Q114 70 114 58Z')
    + s('rect', '#ffffff', x=126, y=36, width=10, height=10, rx=1, stroke_width=2)
    + s('circle', '#ffffff', cx=152, cy=41, r=5, stroke_width=2)
    + s('path', '#ffffff', d='M160 46 L166 36 L172 46Z', stroke_width=2)
    + s('path', d='M126 58 L166 58', stroke_width=2.5)
    + s('path', d='M90 44 L106 44 M100 38 L106 44 L100 50', stroke_width=3)
    + body('#9ccf7a', top=146, bottom=190)
    + face(100, 116, SK, HR, 'smile')
    + s('path', d='M64 116 Q64 76 100 76 Q136 76 136 116', stroke='#5b6b7a', stroke_width=5)
    + z('rect', '#5b6b7a', x=58, y=106, width=12, height=22, rx=5)
    + z('rect', '#5b6b7a', x=130, y=106, width=12, height=22, rx=5)
    + s('path', d='M64 128 Q68 140 86 140', stroke_width=2.5)
    + dot(88, 140, 3.5)
)

# 8. tour-guide: small flag raised
HR = '#c9a36b'
ITEMS['tour-guide'] = (
    body('#e8735a', cx=90)
    + s('path', d='M78 138 L90 150 L102 138', stroke_width=2.5)
    + s('rect', '#ffffff', x=66, y=156, width=18, height=14, rx=2, stroke_width=2)
    + face(90, 104, SK, HR, 'open')
    + z('path', '#f5d58a', d='M58 88 Q58 58 90 58 Q122 58 122 88Z')
    + z('path', '#f5d58a', d='M118 84 L144 90 Q148 92 144 94 L118 92Z')
    + s('path', d='M120 154 Q138 140 140 120', stroke_width=12)
    + s('path', d='M120 154 Q138 140 140 120', stroke='#e8735a', stroke_width=6)
    + s('path', d='M146 130 L146 30', stroke_width=4)
    + z('path', '#ffe27a', d='M148 32 L182 44 L148 58Z')
    + dot(146, 28, 4)
    + hand(144, 118)
)

# 9. hotel-concierge: pillbox cap, uniform, service bell
HR = '#5a4033'
ITEMS['hotel-concierge'] = (
    body('#e04b5a', cx=92)
    + s('path', d='M80 138 L92 150 L104 138', stroke_width=2.5)
    + dot(84, 160, 3, '#ffc94d') + dot(84, 174, 3, '#ffc94d') + dot(100, 160, 3, '#ffc94d') + dot(100, 174, 3, '#ffc94d')
    + face(92, 102, SK, HR, 'smile')
    + z('rect', '#e04b5a', x=70, y=48, width=40, height=24, rx=4)
    + s('rect', '#ffc94d', x=70, y=62, width=40, height=7, stroke_width=2)
    + z('rect', '#d9a66b', x=112, y=168, width=70, height=10, rx=3)
    + z('path', '#ffc94d', d='M120 168 Q120 140 147 140 Q174 140 174 168Z')
    + s('path', d='M147 140 L147 133', stroke_width=3) + dot(147, 131, 4)
    + s('path', d='M130 158 Q132 150 140 147', stroke='#ffffff', stroke_width=3)
    + hand(122, 152)
    + s('path', d='M150 120 L148 112 M162 122 L168 116 M136 122 L130 116', stroke_width=2.5)
)

# 10. sushi-chef: headband, white coat, sushi on a board
HR = '#2b2220'
ITEMS['sushi-chef'] = (
    body('#ffffff')
    + s('path', d='M86 138 L104 160', stroke_width=2.5)
    + s('path', '#5b6b7a', d='M72 186 L72 168 L128 168 L128 186Z', stroke_width=2.5)
    + face(100, 98, SK, HR, 'smile')
    + z('rect', '#f4f4f0', x=64, y=72, width=72, height=11, rx=5)
    + s('path', d='M80 75 L84 82 M94 74 L98 82 M108 74 L112 82 M122 74 L126 82', stroke_width=1.8)
    + z('path', '#f4f4f0', d='M132 76 L146 68 L144 80Z')
    + z('rect', '#d9a66b', x=58, y=150, width=84, height=14, rx=3)
    + z('ellipse', '#ffffff', cx=80, cy=146, rx=13, ry=7)
    + z('path', '#f5b971', d='M66 144 Q68 134 80 134 Q94 134 94 144 Q80 140 66 144Z')
    + s('path', d='M74 137 L78 141 M82 136 L86 140', stroke='#ffffff', stroke_width=1.8)
    + z('ellipse', '#ffffff', cx=118, cy=146, rx=13, ry=7)
    + z('path', '#e8735a', d='M104 144 Q106 134 118 134 Q132 134 132 144 Q118 140 104 144Z')
    + s('rect', '#5b6b7a', x=114, y=133, width=8, height=16, stroke_width=2)
    + hand(52, 158) + hand(148, 158)
)

# 11. video-creator: ring light with phone on tripod, person waving
HR = '#5a4033'
ITEMS['video-creator'] = (
    s('path', d='M54 104 L54 158 M54 158 L36 184 M54 158 L54 184 M54 158 L72 184', stroke_width=4)
    + tube('M54 42 A30 30 0 1 1 53.9 42', '#ffe27a', 9)
    + z('rect', '#5b6b7a', x=45, y=56, width=18, height=32, rx=4)
    + s('rect', '#d8eef8', x=48, y=60, width=12, height=22, rx=1, stroke_width=1.5)
    + dot(80, 34, 5, '#e04b5a')
    + body('#f6a6b8', cx=132)
    + face(132, 102, SK, HR, 'open')
    + s('path', d='M160 150 Q172 128 172 108', stroke_width=12)
    + s('path', d='M160 150 Q172 128 172 108', stroke='#f6a6b8', stroke_width=6)
    + hand(172, 102)
    + s('path', d='M180 84 L184 78 M186 96 L192 94', stroke_width=2.5)
)

# 12. tailor: measuring tape around neck, scissors
HR = '#e8e1d8'
ITEMS['tailor'] = (
    z('circle', HR, cx=100, cy=58, r=11)
    + body('#7cc4b0')
    + face(100, 98, SK, HR, 'smile')
    + s('circle', cx=88, cy=100, r=8, stroke_width=2) + s('circle', cx=112, cy=100, r=8, stroke_width=2)
    + s('path', d='M96 100 L104 100', stroke_width=2)
    + z('path', '#ffe27a', d='M78 134 Q100 146 122 134 L126 186 L116 186 L112 146 Q100 150 88 146 L84 186 L74 186Z')
    + s('path', d='M77 150 L81 150 M77 160 L83 160 M76 170 L80 170 M76 180 L82 180 M119 150 L123 150 M117 160 L123 160 M120 170 L124 170 M118 180 L124 180', stroke_width=1.8)
    + z('circle', '#f07a8a', cx=44, cy=158, r=14)
    + s('path', d='M40 146 L36 136 M48 146 L52 136 M44 145 L44 134', stroke_width=2)
    + dot(36, 135, 3, '#8fc7e8') + dot(52, 135, 3, '#ffe27a') + dot(44, 133, 3, '#9ccf7a')
    + s('path', d='M144 146 L176 118 M144 146 L180 132', stroke='#5b6b7a', stroke_width=5)
    + s('circle', '#e8735a', cx=136, cy=144, r=6, stroke_width=2.5)
    + s('circle', '#e8735a', cx=140, cy=156, r=6, stroke_width=2.5)
)

# 13. beekeeper: hat with veil, honeycomb frame, bees
def bee(x, y):
    return (s('ellipse', '#ffffff', cx=x - 3, cy=y - 7, rx=4, ry=5, stroke_width=1.8)
            + s('ellipse', '#ffffff', cx=x + 4, cy=y - 7, rx=4, ry=5, stroke_width=1.8)
            + s('ellipse', '#ffc94d', cx=x, cy=y, rx=8, ry=6, stroke_width=2)
            + s('path', d=f'M{x-2} {y-5} L{x-2} {y+5} M{x+3} {y-5} L{x+3} {y+5}', stroke_width=2))


def hexd(cx, cy, r):
    return 'M' + ' L'.join(f'{cx + r * cos(pi / 3 * i):.1f} {cy + r * sin(pi / 3 * i):.1f}' for i in range(6)) + 'Z'


HR = '#5a4033'
_comb = ''.join(s('path', '#ffc94d', d=hexd(x, y, 7), stroke_width=1.8)
                for x, y in ((122, 146), (134, 139), (134, 153), (146, 146), (158, 139), (158, 153), (122, 160), (146, 160), (170, 146)))
ITEMS['beekeeper'] = (
    body('#f4f4f0', cx=92)
    + s('path', d='M92 138 L92 186', stroke_width=2.5)
    + face(92, 104, SK, HR, 'smile')
    + s('path', d='M54 82 L50 138 M130 82 L134 138 M54 82 L130 82', stroke_width=2)
    + s('path', d='M52 96 L132 96 M51 110 L133 110 M50 124 L134 124', stroke='#b9a99c', stroke_width=1.5)
    + s('path', d='M66 84 L64 136 M80 84 L80 136 M92 84 L92 136 M104 84 L104 136 M118 84 L120 136', stroke='#b9a99c', stroke_width=1.5)
    + s('path', d='M50 138 Q92 146 134 138', stroke_width=2)
    + z('path', '#f4f4f0', d='M66 76 Q66 46 92 46 Q118 46 118 76Z')
    + z('ellipse', '#f4f4f0', cx=92, cy=80, rx=46, ry=8)
    + z('rect', '#d9a66b', x=110, y=128, width=70, height=44, rx=3)
    + s('rect', '#f6e0c4', x=116, y=133, width=58, height=34, stroke_width=2)
    + _comb
    + hand(110, 150) + hand(180, 150)
    + bee(40, 60) + bee(160, 54) + bee(36, 150)
)

# 14. zookeeper: cap, bucket of food
HR = '#2b2220'
ITEMS['zookeeper'] = (
    body('#9ccf7a')
    + s('path', d='M88 138 L100 150 L112 138', stroke_width=2.5)
    + s('rect', '#9ccf7a', x=112, y=156, width=16, height=14, rx=2, stroke_width=2.5)
    + face(100, 100, SK, HR, 'open')
    + z('path', '#7cc4a0', d='M66 84 Q66 52 100 52 Q134 52 134 84Z')
    + z('path', '#7cc4a0', d='M68 82 Q100 74 132 82 Q136 92 100 90 Q64 92 68 82Z')
    + s('path', d='M40 146 Q58 112 76 146', stroke_width=3)
    + z('path', '#f5b971', d='M44 140 L38 118 L48 124 L52 140Z')
    + s('path', d='M42 118 L38 108 M42 118 L48 110', stroke='#7cc4a0', stroke_width=3)
    + z('circle', '#e04b5a', cx=64, cy=138, r=9)
    + z('path', '#ffe27a', d='M54 140 Q52 124 60 118 Q58 130 62 140Z')
    + z('path', '#c9d3db', d='M36 140 L80 140 L74 180 L42 180Z')
    + s('path', d='M38 152 L78 152', stroke_width=2)
    + hand(64, 152)
)

# 15. lifeguard: visor, whistle, ring buoy
HR = '#c9a36b'
_buoy = z('circle', '#ffffff', cx=142, cy=146, r=32) + s('circle', '#fbf6ee', cx=142, cy=146, r=15)
for a in (45, 135, 225, 315):
    r1, r2, w = 16, 31, 0.3
    p = [(142 + r * cos((a + d) * pi / 180), 146 + r * sin((a + d) * pi / 180)) for r, d in ((r1, -20), (r2, -12), (r2, 12), (r1, 20))]
    _buoy += s('path', '#e04b5a', d='M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in p) + 'Z', stroke_width=2)
_buoy += s('circle', cx=142, cy=146, r=32) + s('circle', cx=142, cy=146, r=15)
ITEMS['lifeguard'] = (
    body('#e04b5a', cx=84)
    + face(84, 100, SK, HR, 'smile')
    + z('path', '#ffe27a', d='M50 78 Q84 64 118 78 L132 82 Q134 88 126 88 L52 86Z')
    + s('path', d='M72 136 L84 154 L96 136', stroke_width=2.5)
    + z('rect', '#c9d3db', x=78, y=154, width=16, height=9, rx=4)
    + _buoy
    + hand(112, 140) + hand(118, 168)
)

# 16. park-ranger: campaign hat, badge, pine trees
def pine(x, y, h):
    return (z('rect', '#8b6b4f', x=x - 4, y=y - 10, width=8, height=12)
            + z('path', '#7cc4a0', d=f'M{x} {y-h} L{x+18} {y-h*0.45} L{x+9} {y-h*0.45} L{x+20} {y-10} L{x-20} {y-10} L{x-9} {y-h*0.45} L{x-18} {y-h*0.45}Z'))


HR = '#5a4033'
ITEMS['park-ranger'] = (
    pine(38, 184, 82) + pine(164, 184, 70)
    + body('#f5d58a')
    + s('path', d='M88 138 L100 150 L112 138', stroke_width=2.5)
    + s('path', '#ffc94d', d='M120 154 L122 159 L127 159 L123 162 L125 167 L120 164 L115 167 L117 162 L113 159 L118 159Z', stroke_width=1.8)
    + s('rect', '#f5d58a', x=74, y=154, width=16, height=14, rx=2, stroke_width=2.5)
    + z('path', '#7cc4a0', d='M80 138 L120 138 L116 146 L84 146Z')
    + face(100, 100, SK, HR, 'smile')
    + z('path', '#9a6a3f', d='M74 76 Q76 52 86 46 Q93 44 100 54 Q107 44 114 46 Q124 52 126 76Z')
    + s('rect', '#8b6b4f', x=74, y=68, width=52, height=8, stroke_width=2.5)
    + z('ellipse', '#9a6a3f', cx=100, cy=78, rx=56, ry=9)
)

# 17. business-meeting: three people behind a table
def suit_person(cx, cy, r, hair, suit, tie_c, mouth='smile', bottom=134):
    w = r * 1.15
    top = cy + r * 0.9
    return (body(suit, cx=cx, top=top, bottom=bottom, w=w)
            + s('path', '#ffffff', d=f'M{cx-r*0.35:.1f} {top+1:.1f} L{cx} {top+r*0.45:.1f} L{cx+r*0.35:.1f} {top+1:.1f}Z', stroke_width=2)
            + tie(cx, top + r * 0.15, tie_c, r / 34)
            + sface(cx, cy, r, SK, hair, mouth))


ITEMS['business-meeting'] = (
    suit_person(48, 88, 22, '#2b2220', '#5b6b7a', '#e8735a', bottom=142)
    + suit_person(152, 88, 22, '#c9a36b', '#8fb3e0', '#f5d58a', bottom=142)
    + suit_person(100, 72, 24, '#5a4033', '#7cc4b0', '#f07a8a', 'open', bottom=142)
    + z('rect', '#d9a66b', x=18, y=132, width=164, height=16, rx=4)
    + z('rect', '#9a6a3f', x=28, y=148, width=144, height=10)
    + s('path', d='M36 158 L36 184 M164 158 L164 184', stroke_width=5)
    + z('path', '#c9d3db', d='M84 106 L116 106 L118 130 L82 130Z')
    + s('rect', '#c9d3db', x=72, y=129, width=56, height=5, rx=2, stroke_width=2)
    + s('rect', '#ffffff', x=30, y=124, width=24, height=10, rx=1, stroke_width=2, transform='rotate(-8 42 129)')
    + s('rect', '#ffffff', x=146, y=124, width=24, height=10, rx=1, stroke_width=2, transform='rotate(8 158 129)')
    + z('path', '#f4f4f0', d='M134 118 L144 118 L143 130 L135 130Z')
)

# 18. presentation: board with chart, presenter pointing
HR = '#2b2220'
ITEMS['presentation'] = (
    s('path', d='M40 128 L30 182 M92 128 L102 182 M66 128 L66 182', stroke_width=4)
    + z('rect', '#ffffff', x=20, y=40, width=92, height=88, rx=4)
    + s('rect', '#8fc7e8', x=34, y=96, width=12, height=20, stroke_width=2.5)
    + s('rect', '#7cc4b0', x=52, y=84, width=12, height=32, stroke_width=2.5)
    + s('rect', '#f5d58a', x=70, y=70, width=12, height=46, stroke_width=2.5)
    + s('rect', '#f6a6b8', x=88, y=56, width=12, height=60, stroke_width=2.5)
    + s('path', d='M30 116 L104 116', stroke_width=2.5)
    + s('path', d='M36 82 L56 70 L72 74 L98 48', stroke='#e8735a', stroke_width=3)
    + body('#8fb3e0', cx=142)
    + s('path', '#ffffff', d='M130 137 L142 150 L154 137Z', stroke_width=2)
    + tie(142, 140, '#e8735a')
    + face(142, 98, SK, HR, 'open')
    + s('path', d='M116 152 L84 88', stroke_width=6)
    + s('path', d='M116 152 L84 88', stroke='#d9a66b', stroke_width=2)
    + hand(116, 152)
)

# 19. handshake-deal
ITEMS['handshake-deal'] = (
    s('path', '#ffe27a', d='M100 30 L104 40 L114 42 L104 46 L100 56 L96 46 L86 42 L96 40Z', stroke_width=2)
    + dot(78, 40, 3, '#ffc94d') + dot(124, 38, 3, '#ffc94d')
    + suit_person(52, 86, 28, '#2b2220', '#5b6b7a', '#e8735a', bottom=186)
    + suit_person(148, 86, 28, '#c9a36b', '#8fb3e0', '#f5d58a', bottom=186)
    + s('path', d='M74 142 Q88 148 96 140', stroke_width=14)
    + s('path', d='M74 142 Q88 148 96 140', stroke='#5b6b7a', stroke_width=8)
    + s('path', d='M126 142 Q112 148 104 140', stroke_width=14)
    + s('path', d='M126 142 Q112 148 104 140', stroke='#8fb3e0', stroke_width=8)
    + z('ellipse', SK, cx=96, cy=138, rx=11, ry=9)
    + z('ellipse', SK, cx=105, cy=134, rx=11, ry=9)
    + s('path', d='M98 128 Q103 132 102 140', stroke_width=2)
)

# 20. business-team: three people, center in front
ITEMS['business-team'] = (
    suit_person(52, 78, 26, '#5a4033', '#7cc4b0', '#f5d58a', bottom=186)
    + suit_person(148, 78, 26, '#c9a36b', '#8fb3e0', '#e8735a', bottom=186)
    + suit_person(100, 102, 30, '#2b2220', '#5b6b7a', '#f07a8a', 'open', bottom=190)
)
