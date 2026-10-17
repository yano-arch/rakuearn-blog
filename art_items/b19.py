from art import z, s, dot, cheeks, face, OUT, CH

SKIN = '#ffd9b8'


def tube(d, color, w=6):
    """thick colored line with brown outline"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


def mface(cx, cy, r, hair, mouth='smile'):
    """smaller version of face() with radius r"""
    k = r / 34
    p = lambda dx, dy: f'{cx+dx*k:.1f} {cy+dy*k:.1f}'
    o = z('circle', SKIN, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{p(-34,-2)} Q{p(-32,-36)} {p(0,-35)} Q{p(32,-36)} {p(34,-2)} '
                           f'Q{p(20,-18)} {p(0,-17)} Q{p(-20,-18)} {p(-34,-2)}Z')
    o += dot(cx - 12 * k, cy + 2 * k, 3.5 * k + 0.6) + dot(cx + 12 * k, cy + 2 * k, 3.5 * k + 0.6)
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, 7 * k, 4 * k)
    if mouth == 'smile':
        o += s('path', d=f'M{p(-6,16)} Q{p(0,21)} {p(6,16)}', stroke_width=2.5)
    return o


def sparkle(x, y, r=7, c='#ffe27a'):
    return s('path', c, d=f'M{x} {y-r} Q{x+1.5} {y-1.5} {x+r} {y} Q{x+1.5} {y+1.5} {x} {y+r} '
                          f'Q{x-1.5} {y+1.5} {x-r} {y} Q{x-1.5} {y-1.5} {x} {y-r}Z', stroke_width=2)


def drop(x, y, k=1.0):
    return s('path', '#8fc7e8', d=f'M{x} {y} Q{x-7*k:.1f} {y+10*k:.1f} {x-6*k:.1f} {y+14*k:.1f} '
                                  f'Q{x} {y+20*k:.1f} {x+6*k:.1f} {y+14*k:.1f} Q{x+7*k:.1f} {y+10*k:.1f} {x} {y}Z',
             stroke_width=2.5)


def body(cx, top, bottom, half, color):
    return z('path', color, d=f'M{cx-half} {bottom} Q{cx-half+2} {top+2} {cx} {top} '
                              f'Q{cx+half-2} {top+2} {cx+half} {bottom}Z')


def suit(cx, top, bottom, half):
    """navy suit body with white shirt V and red tie"""
    return (body(cx, top, bottom, half, '#5b6b7a')
            + s('path', '#ffffff', d=f'M{cx-13} {top+1} L{cx} {top+30} L{cx+13} {top+1}Z', stroke_width=2.5)
            + s('path', '#e8735a', d=f'M{cx-4} {top+4} L{cx+4} {top+4} L{cx+6} {top+28} L{cx} {top+36} '
                                     f'L{cx-6} {top+28}Z', stroke_width=2.5))


def cell_person(x, y, bg, shirt, hair):
    cx = x + 20.5
    return (s('rect', bg, x=x, y=y, width=41, height=29, rx=3, stroke_width=2)
            + s('path', shirt, d=f'M{cx-12} {y+29} Q{cx-12} {y+20} {cx} {y+20} Q{cx+12} {y+20} {cx+12} {y+29}Z',
                stroke_width=2)
            + s('circle', SKIN, cx=cx, cy=y + 12, r=8, stroke_width=2)
            + s('path', hair, d=f'M{cx-8} {y+12} Q{cx-8} {y+3} {cx} {y+3} Q{cx+8} {y+3} {cx+8} {y+12} '
                               f'Q{cx} {y+7} {cx-8} {y+12}Z', stroke_width=2)
            + dot(cx - 3, y + 13, 1.5) + dot(cx + 3, y + 13, 1.5))


def stack(x, yb, w, n, h=9):
    o = ''
    for i in range(n):
        dx = (-3, 2, -1, 3, 0, -2)[i % 6]
        o += z('rect', '#ffffff', x=x + dx, y=yb - (i + 1) * h, width=w, height=h, rx=1.5)
    return o


def coin(cx, y, r=26, ry=9, t=10):
    return (z('path', '#ffc94d', d=f'M{cx-r} {y} L{cx-r} {y+t} A{r} {ry} 0 0 0 {cx+r} {y+t} L{cx+r} {y}Z')
            + z('ellipse', '#ffe27a', cx=cx, cy=y, rx=r, ry=ry))


ITEMS = {}

ITEMS['video-call'] = (
    z('rect', '#5b6b7a', x=44, y=44, width=112, height=86, rx=8)
    + s('rect', '#d8eef8', x=53, y=53, width=94, height=68, rx=3)
    + cell_person(56, 56, '#f5d58a', '#e8735a', '#2b2220')
    + cell_person(103, 56, '#9ccf7a', '#8fb3e0', '#c9a36b')
    + cell_person(56, 89, '#f6a6b8', '#7cc4b0', '#5a4033')
    + cell_person(103, 89, '#8fc7e8', '#f5b971', '#e8e1d8')
    + z('path', '#c9d3db', d='M44 134 L156 134 L176 158 Q178 164 172 164 L28 164 Q22 164 24 158Z')
    + s('rect', '#b9a99c', x=84, y=146, width=32, height=10, rx=3, stroke_width=2)
    + s('path', d='M152 34 Q164 28 168 18 M162 42 Q174 40 180 32', stroke_width=2.5)
)

ITEMS['working-from-home'] = (
    s('rect', '#d8eef8', x=130, y=26, width=44, height=44, rx=3)
    + s('path', d='M152 26 L152 70 M130 48 L174 48', stroke_width=2.5)
    + body(100, 112, 160, 40, '#f5b971')
    + face(100, 76, SKIN, '#5a4033', 'smile')
    + z('rect', '#d9a66b', x=22, y=150, width=156, height=14, rx=4)
    + s('path', d='M36 164 L36 182 M164 164 L164 182', stroke_width=5)
    + z('rect', '#c9d3db', x=68, y=116, width=64, height=34, rx=4)
    + s('circle', '#ffffff', cx=100, cy=133, r=4, stroke_width=2)
    + s('path', d='M146 130 Q156 131 156 140 Q156 147 146 146', stroke_width=4)
    + z('rect', '#e8735a', x=140, y=124, width=10, height=26, rx=2) + z('rect', '#e8735a', x=132, y=124, width=20, height=26, rx=4)
    + s('path', d='M138 116 Q134 110 138 104 M146 116 Q142 110 146 104', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M44 132 Q30 120 36 104 Q48 112 48 130Z') + z('path', '#9ccf7a', d='M50 132 Q60 116 56 100 Q44 112 46 130Z')
    + z('path', '#f5d58a', d='M34 130 L62 130 L58 150 L38 150Z')
)


def tired_face(cx, cy):
    o = z('circle', SKIN, cx=cx, cy=cy, r=34)
    o += s('path', '#2b2220', d=f'M{cx-34} {cy-2} Q{cx-32} {cy-36} {cx} {cy-35} Q{cx+32} {cy-36} {cx+34} {cy-2} '
                                f'Q{cx+20} {cy-18} {cx} {cy-17} Q{cx-20} {cy-18} {cx-34} {cy-2}Z')
    o += s('path', d=f'M{cx-18} {cy+2} L{cx-6} {cy+2} M{cx+6} {cy+2} L{cx+18} {cy+2}', stroke_width=3)
    o += s('path', d=f'M{cx-17} {cy+8} Q{cx-12} {cy+11} {cx-7} {cy+8} M{cx+7} {cy+8} Q{cx+12} {cy+11} {cx+17} {cy+8}',
           stroke='#8fb3e0', stroke_width=2.5)
    o += s('path', d=f'M{cx-7} {cy+20} Q{cx-3} {cy+17} {cx} {cy+20} Q{cx+3} {cy+23} {cx+7} {cy+20}', stroke_width=2.5)
    return o


ITEMS['overtime-night'] = (
    z('rect', '#5b6b7a', x=24, y=24, width=66, height=62, rx=4)
    + s('path', '#ffe27a', d='M64 36 Q46 40 48 58 Q52 74 70 72 Q56 66 56 54 Q56 42 64 36Z', stroke_width=2.5)
    + dot(36, 40, 2.2, '#ffe27a') + dot(78, 50, 2.2, '#ffe27a') + dot(40, 72, 2, '#ffe27a')
    + body(120, 122, 160, 38, '#8fb3e0')
    + tired_face(120, 88)
    + z('rect', '#d9a66b', x=22, y=150, width=156, height=14, rx=4)
    + s('path', d='M36 164 L36 182 M164 164 L164 182', stroke_width=5)
    + z('rect', '#c9d3db', x=92, y=118, width=56, height=32, rx=4)
    + tube('M44 150 L44 118 L62 104', '#5b6b7a', 4)
    + z('path', '#ffc94d', d='M54 96 L76 92 L80 112 Q66 116 54 96Z')
    + z('ellipse', '#5b6b7a', cx=44, cy=148, rx=14, ry=5)
    + z('rect', '#ffffff', x=156, y=130, width=16, height=20, rx=3)
)

ITEMS['business-trip'] = (
    s('path', d='M134 110 L134 74 L162 74 L162 110', stroke_width=10)
    + s('path', d='M134 110 L134 74 L162 74 L162 110', stroke='#c9d3db', stroke_width=4)
    + z('rect', '#8fc7e8', x=122, y=104, width=52, height=68, rx=8)
    + s('path', d='M138 112 L138 164 M158 112 L158 164', stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=134, cy=178, r=5) + z('circle', '#5b6b7a', cx=162, cy=178, r=5)
    + suit(76, 124, 182, 34)
    + tube('M104 140 Q120 112 134 80', '#5b6b7a', 10)
    + z('circle', SKIN, cx=136, cy=78, r=9)
    + face(76, 82, SKIN, '#2b2220', 'smile')
)


def glasses(cx, cy):
    return (s('circle', cx=cx - 12, cy=cy + 2, r=8, stroke_width=2.5) + s('circle', cx=cx + 12, cy=cy + 2, r=8, stroke_width=2.5)
            + s('path', d=f'M{cx-4} {cy+2} L{cx+4} {cy+2}', stroke_width=2.5))


ITEMS['job-interview'] = (
    suit(56, 116, 160, 32)
    + face(56, 78, SKIN, '#2b2220', 'smile') + glasses(56, 78)
    + suit(144, 116, 160, 32)
    + face(144, 78, SKIN, '#5a4033', 'smile')
    + drop(176, 60, 0.8)
    + z('rect', '#d9a66b', x=22, y=142, width=156, height=14, rx=4)
    + z('rect', '#d9a66b', x=34, y=156, width=132, height=24, rx=2)
    + z('rect', '#ffffff', x=74, y=132, width=30, height=10, rx=1, transform='rotate(-4 89 137)')
    + s('path', d='M110 140 L130 132', stroke_width=4)
)

ITEMS['new-employee'] = (
    suit(100, 120, 182, 40)
    + s('path', d='M86 122 L96 150 M114 122 L104 150', stroke_width=2.5)
    + z('rect', '#ffffff', x=114, y=144, width=16, height=11, rx=2)
    + s('path', d='M118 150 L126 150', stroke_width=2)
    + face(100, 80, SKIN, '#2b2220', 'smile')
    + drop(144, 52)
    + sparkle(40, 66, 9) + sparkle(160, 110, 8) + sparkle(46, 124, 6, '#f6a6b8')
)

ITEMS['promotion-stairs'] = (
    z('path', '#f5d58a', d='M24 180 L24 156 L60 156 L60 128 L96 128 L96 100 L132 100 L132 72 L172 72 L172 180Z')
    + s('path', d='M60 156 L60 180 M96 128 L96 180 M132 100 L132 180', stroke_width=2)
    + s('path', d='M156 72 L156 28', stroke_width=3.5)
    + z('path', '#e8735a', d='M156 30 L178 38 L156 48Z')
    + body(112, 74, 100, 17, '#7cc4b0')
    + s('path', d='M126 84 L136 70', stroke_width=6) + z('circle', SKIN, cx=137, cy=68, r=5)
    + mface(112, 54, 21, '#5a4033')
    + z('path', '#9ccf7a', d='M34 136 L60 92 L50 88 L76 72 L76 102 L68 98 L44 142Z')
)

PA = 'M40 66 L100 66 L100 84 Q118 78 118 96 Q118 114 100 108 L100 126 L40 126Z'
PB = 'M110 66 L170 66 L170 126 L110 126 L110 108 Q128 114 128 96 Q128 78 110 84Z'
ITEMS['teamwork-puzzle'] = (
    z('path', '#8fc7e8', d=PA)
    + z('path', '#f5b971', d=PB)
    + tube('M30 184 L60 136', '#8fb3e0', 16)
    + tube('M172 184 L148 136', '#9ccf7a', 16)
    + z('circle', SKIN, cx=64, cy=128, r=13)
    + z('circle', SKIN, cx=146, cy=128, r=13)
    + s('path', d='M98 46 L98 34 M112 48 L120 38 M84 48 L76 38', stroke_width=2.5)
)

ITEMS['brainstorming'] = (
    s('path', d='M52 136 L40 182 M132 136 L144 182', stroke_width=5)
    + z('rect', '#ffffff', x=28, y=40, width=128, height=96, rx=6)
    + s('rect', '#c9d3db', x=56, y=136, width=72, height=6, rx=2, stroke_width=2)
    + z('rect', '#f5d58a', x=40, y=52, width=26, height=26, rx=2)
    + z('rect', '#f6a6b8', x=76, y=56, width=26, height=26, rx=2)
    + z('rect', '#9ccf7a', x=40, y=94, width=26, height=26, rx=2)
    + z('rect', '#8fc7e8', x=78, y=96, width=26, height=26, rx=2)
    + z('rect', '#f5b971', x=114, y=92, width=26, height=26, rx=2)
    + s('path', d='M45 62 L60 62 M45 69 L56 69 M81 66 L96 66 M81 73 L92 73 M45 104 L60 104 M45 111 L56 111 '
                  'M83 106 L98 106 M83 113 L94 113 M119 102 L134 102 M119 109 L130 109', stroke_width=2)
    + s('path', d='M66 64 L76 68 M66 106 L78 108 M104 108 L114 104', stroke_width=2, stroke_dasharray='3 4')
    + s('rect', '#b9a99c', x=145, y=58, width=14, height=10, rx=3)
    + z('circle', '#ffe27a', cx=152, cy=42, r=17)
    + s('path', d='M152 16 L152 10 M174 24 L180 18 M130 24 L124 18 M178 42 L186 42', stroke_width=2.5)
)

ITEMS['deadline-hourglass'] = (
    s('path', d='M58 44 L58 158 M142 44 L142 158', stroke_width=7)
    + s('path', d='M58 44 L58 158 M142 44 L142 158', stroke='#9a6a3f', stroke_width=3)
    + z('path', '#d8eef8', d='M66 44 L134 44 Q134 80 106 100 Q134 120 134 158 L66 158 Q66 120 94 100 Q66 80 66 44Z')
    + s('path', '#f5d58a', d='M78 62 L122 62 Q116 82 100 94 Q84 82 78 62Z', stroke_width=2.5)
    + s('path', d='M100 94 L100 140', stroke='#d9a66b', stroke_width=2.5)
    + s('path', '#f5d58a', d='M70 158 Q72 148 84 146 Q100 136 116 146 Q128 148 130 158Z', stroke_width=2.5)
    + z('rect', '#9a6a3f', x=48, y=30, width=104, height=14, rx=5)
    + z('rect', '#9a6a3f', x=48, y=158, width=104, height=14, rx=5)
    + dot(88, 122) + dot(112, 122) + cheeks(80, 120, 131, 5, 3)
    + s('path', d='M80 112 L90 116 M120 112 L110 116', stroke_width=2.5)
    + s('path', d='M92 134 Q96 130 100 134 Q104 138 108 134', stroke_width=2.5)
    + drop(166, 60) + drop(36, 84, 0.8)
)

ITEMS['paperwork-stress'] = (
    face(100, 92, SKIN, '#5a4033', 'o')
    + s('path', d='M84 76 L94 80 M116 76 L106 80', stroke_width=2.5)
    + stack(26, 180, 46, 11)
    + stack(130, 180, 44, 13)
    + stack(74, 180, 52, 5)
    + z('rect', '#ffffff', x=52, y=34, width=24, height=30, rx=1.5, transform='rotate(-20 64 49)')
    + s('path', d='M58 44 L70 40 M60 50 L72 46', stroke_width=2, transform='rotate(-20 64 49)')
    + z('rect', '#ffffff', x=128, y=24, width=24, height=30, rx=1.5, transform='rotate(16 140 39)')
    + s('path', d='M133 34 L147 34 M133 40 L145 40', stroke_width=2, transform='rotate(16 140 39)')
    + drop(30, 72, 0.9)
)

ITEMS['filing-cabinet'] = (
    z('rect', '#f5d58a', x=60, y=36, width=34, height=40, rx=3)
    + z('rect', '#8fb3e0', x=82, y=30, width=34, height=46, rx=3)
    + z('rect', '#f07a8a', x=106, y=40, width=34, height=36, rx=3)
    + z('rect', '#c9d3db', x=48, y=62, width=104, height=116, rx=6)
    + s('path', d='M52 100 L148 100 M52 140 L148 140', stroke_width=2.5)
    + z('rect', '#c9d3db', x=42, y=56, width=116, height=40, rx=5)
    + ''.join(s('rect', '#ffffff', x=88, y=y, width=24, height=8, rx=1.5, stroke_width=2)
              + s('rect', '#5b6b7a', x=86, y=y + 13, width=28, height=7, rx=3.5, stroke_width=2)
              for y in (64, 108, 148))
)

ITEMS['briefcase'] = (
    tube('M80 70 Q80 46 100 46 Q120 46 120 70', '#8b6b4f', 8)
    + z('rect', '#9a6a3f', x=32, y=66, width=136, height=104, rx=12)
    + s('path', d='M32 104 Q100 116 168 104', stroke_width=2.5)
    + z('rect', '#ffc94d', x=56, y=100, width=16, height=16, rx=3)
    + z('rect', '#ffc94d', x=128, y=100, width=16, height=16, rx=3)
    + s('path', d='M42 80 L42 158 M158 80 L158 158', stroke='#f5b971', stroke_width=2, stroke_dasharray='4 5')
)

ITEMS['business-cards'] = (
    tube('M22 176 L54 112', '#5b6b7a', 18)
    + tube('M178 176 L148 142', '#8fb3e0', 18)
    + z('rect', '#ffffff', x=56, y=62, width=60, height=38, rx=3, transform='rotate(-8 86 81)')
    + s('rect', '#7cc4b0', x=64, y=70, width=12, height=12, rx=2, stroke_width=2, transform='rotate(-8 86 81)')
    + s('path', d='M82 74 L106 74 M82 82 L100 82 M66 90 L104 90', stroke_width=2.5, transform='rotate(-8 86 81)')
    + z('circle', SKIN, cx=60, cy=96, r=13)
    + z('rect', '#ffffff', x=86, y=106, width=60, height=38, rx=3, transform='rotate(6 116 125)')
    + s('rect', '#e8735a', x=94, y=114, width=12, height=12, rx=6, stroke_width=2, transform='rotate(6 116 125)')
    + s('path', d='M112 118 L136 118 M112 126 L130 126 M96 134 L134 134', stroke_width=2.5, transform='rotate(6 116 125)')
    + z('circle', SKIN, cx=144, cy=140, r=13)
    + sparkle(150, 66, 9) + sparkle(40, 70, 6, '#f6a6b8')
)

ITEMS['coffee-break'] = (
    s('path', d='M24 176 L176 176', stroke_width=2.5)
    + z('ellipse', '#f4f4f0', cx=86, cy=164, rx=48, ry=10)
    + tube('M116 112 Q144 112 140 132 Q136 148 112 146', '#ffffff', 6)
    + z('path', '#ffffff', d='M48 102 L124 102 Q122 160 86 160 Q50 160 48 102Z')
    + z('ellipse', '#8b6b4f', cx=86, cy=102, rx=38, ry=8)
    + dot(74, 128) + dot(98, 128) + cheeks(64, 108, 137, 5, 3) + s('path', d='M82 136 Q86 140 90 136', stroke_width=2.5)
    + s('path', d='M72 84 Q66 74 72 64 Q78 54 72 44 M96 84 Q90 74 96 64 Q102 54 96 44', stroke_width=2.5)
    + z('circle', '#d9a66b', cx=152, cy=158, r=20)
    + dot(144, 152, 3, '#8b6b4f') + dot(158, 148, 3, '#8b6b4f') + dot(150, 166, 3, '#8b6b4f') + dot(162, 162, 3, '#8b6b4f')
)

ITEMS['signing-contract'] = (
    z('rect', '#ffffff', x=36, y=30, width=100, height=140, rx=4, transform='rotate(-6 86 100)')
    + s('path', d='M52 52 L118 52 M52 66 L120 66 M52 78 L110 78 M52 92 L118 92 M52 104 L100 104',
        stroke='#b9a99c', stroke_width=3, transform='rotate(-6 86 100)')
    + s('path', d='M54 150 L120 150', stroke='#b9a99c', stroke_width=2, stroke_dasharray='3 4', transform='rotate(-6 86 100)')
    + s('path', d='M58 142 Q62 126 68 138 Q72 148 78 132 Q82 122 86 140 Q90 146 100 136 L110 138',
        stroke='#5b6b7a', stroke_width=2.5, transform='rotate(-6 86 100)')
    + tube('M150 134 L182 176', '#8fb3e0', 18)
    + tube('M116 132 L160 82', '#5b6b7a', 7)
    + s('path', OUT, d='M112 140 L114 130 L120 135Z', stroke_width=2)
    + z('circle', SKIN, cx=138, cy=118, r=14)
)

ITEMS['hanko-stamp'] = (
    z('rect', '#ffffff', x=24, y=110, width=76, height=66, rx=3, transform='rotate(-5 62 143)')
    + s('circle', cx=60, cy=144, r=15, stroke='#e04b5a', stroke_width=4)
    + s('circle', cx=60, cy=144, r=8, stroke='#e04b5a', stroke_width=2.5)
    + z('rect', '#5b6b7a', x=128, y=142, width=50, height=32, rx=6)
    + s('rect', '#e04b5a', x=134, y=146, width=38, height=20, rx=3, stroke_width=2)
    + z('path', '#d9a66b', d='M98 44 Q98 30 114 30 Q130 30 130 44 L128 58 Q124 66 126 76 L130 126 L98 126 L102 76 Q104 66 100 58Z')
    + s('rect', '#e04b5a', x=97, y=124, width=34, height=8, rx=2, stroke_width=2.5)
    + dot(114, 40, 3, '#e04b5a')
    + s('path', d='M86 94 L78 90 M84 110 L76 112 M142 94 L150 90', stroke_width=2.5)
)

ITEMS['coin-stack'] = (
    ''.join(coin(68, y) for y in (160, 150, 140, 130, 120, 110, 100))
    + ''.join(coin(128, y) for y in (160, 150, 140, 130))
    + s('ellipse', cx=68, cy=100, rx=17, ry=5.5, stroke='#d9a66b', stroke_width=2.5)
    + s('ellipse', cx=128, cy=130, rx=17, ry=5.5, stroke='#d9a66b', stroke_width=2.5)
    + z('circle', '#ffc94d', cx=146, cy=72, r=22) + s('circle', cx=146, cy=72, r=14, stroke='#d9a66b', stroke_width=2.5)
    + sparkle(110, 48, 8) + sparkle(178, 104, 6) + sparkle(36, 76, 7)
)

ITEMS['wallet'] = (
    z('rect', '#8fb3e0', x=50, y=44, width=70, height=46, rx=5, transform='rotate(-8 85 67)')
    + s('rect', '#ffc94d', x=60, y=54, width=14, height=11, rx=2, stroke_width=2, transform='rotate(-8 85 67)')
    + z('rect', '#f5d58a', x=82, y=52, width=66, height=40, rx=5, transform='rotate(6 115 72)')
    + z('rect', '#9a6a3f', x=30, y=72, width=140, height=94, rx=12)
    + s('rect', x=38, y=80, width=124, height=78, rx=8, stroke='#f5b971', stroke_width=2, stroke_dasharray='4 5')
    + z('path', '#8b6b4f', d='M118 96 L172 96 L172 140 L118 140 Q110 140 110 132 L110 104 Q110 96 118 96Z')
    + z('circle', '#ffc94d', cx=124, cy=118, r=6)
)

ITEMS['credit-card'] = (
    z('rect', '#7cc4b0', x=40, y=44, width=136, height=88, rx=10, transform='rotate(-10 108 88)')
    + z('rect', '#8fb3e0', x=26, y=74, width=144, height=92, rx=10)
    + z('rect', '#ffc94d', x=40, y=104, width=28, height=22, rx=4)
    + s('path', d='M40 115 L52 115 M56 115 L68 115 M54 104 L54 126', stroke_width=2)
    + s('path', d='M80 108 Q84 115 80 122 M88 104 Q94 115 88 126', stroke_width=2.5)
    + ''.join(s('rect', '#ffffff', x=x, y=138, width=24, height=8, rx=4, stroke_width=2) for x in (40, 70, 100, 130))
    + s('circle', '#f5d58a', cx=146, cy=112, r=9, stroke_width=2.5)
)
