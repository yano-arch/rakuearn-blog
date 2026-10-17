from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

SK = '#ffd9b8'


def hd(cx, cy, hair, mouth='smile', r=34, eyes='dot', style=''):
    """Head scaled from art.face(); eyes: dot / happy / tight / worried."""
    k = r / 34
    f = lambda v: round(v * k, 1)
    o = ''
    if style == 'long':
        o += z('path', hair, d=f'M{cx-f(36)} {cy-f(4)} Q{cx-f(40)} {cy+f(30)} {cx-f(30)} {cy+f(38)} L{cx+f(30)} {cy+f(38)} Q{cx+f(40)} {cy+f(30)} {cx+f(36)} {cy-f(4)}Z')
    if style == 'bun':
        o += z('circle', hair, cx=cx, cy=cy - f(36), r=f(13))
    o += z('circle', SK, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{cx-r} {cy-f(2)} Q{cx-f(32)} {cy-f(36)} {cx} {cy-f(35)} Q{cx+f(32)} {cy-f(36)} {cx+r} {cy-f(2)} Q{cx+f(20)} {cy-f(18)} {cx} {cy-f(17)} Q{cx-f(20)} {cy-f(18)} {cx-r} {cy-f(2)}Z')
    ex, ey = f(12), cy + f(2)
    if eyes == 'dot':
        o += dot(cx - ex, ey, max(3, f(3.5))) + dot(cx + ex, ey, max(3, f(3.5)))
    elif eyes == 'happy':
        for x in (cx - ex, cx + ex):
            o += s('path', d=f'M{x-f(5)} {ey+f(2)} Q{x} {ey-f(5)} {x+f(5)} {ey+f(2)}', stroke_width=2.5)
    elif eyes == 'tight':
        o += s('path', d=f'M{cx-ex-f(5)} {ey-f(4)} L{cx-ex+f(3)} {ey} L{cx-ex-f(5)} {ey+f(4)}', stroke_width=2.5)
        o += s('path', d=f'M{cx+ex+f(5)} {ey-f(4)} L{cx+ex-f(3)} {ey} L{cx+ex+f(5)} {ey+f(4)}', stroke_width=2.5)
    elif eyes == 'angry':
        o += dot(cx - ex, ey + 1, max(3, f(3.5))) + dot(cx + ex, ey + 1, max(3, f(3.5)))
        o += s('path', d=f'M{cx-ex-f(7)} {ey-f(10)} L{cx-ex+f(5)} {ey-f(5)} M{cx+ex+f(7)} {ey-f(10)} L{cx+ex-f(5)} {ey-f(5)}', stroke_width=2.5)
    elif eyes == 'worried':
        o += dot(cx - ex, ey, max(3, f(3.5))) + dot(cx + ex, ey, max(3, f(3.5)))
        o += s('path', d=f'M{cx-ex-f(6)} {ey-f(7)} L{cx-ex+f(4)} {ey-f(11)} M{cx+ex+f(6)} {ey-f(7)} L{cx+ex-f(4)} {ey-f(11)}', stroke_width=2.5)
    o += cheeks(cx - f(20), cx + f(20), cy + f(13), f(7), f(4))
    my = cy + f(16)
    if mouth == 'smile':
        o += s('path', d=f'M{cx-f(6)} {my} Q{cx} {my+f(5)} {cx+f(6)} {my}', stroke_width=2.5)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{cx-f(8)} {my-f(2)} Q{cx} {my+f(12)} {cx+f(8)} {my-f(2)}Z', stroke_width=2.5)
    elif mouth == 'o':
        o += f'<circle cx="{cx}" cy="{cy+f(18)}" r="{f(4)}" fill="#c0504d" stroke-width="2.5"/>'
    elif mouth == 'wavy':
        o += s('path', d=f'M{cx-f(8)} {my+f(2)} Q{cx-f(4)} {my-f(2)} {cx} {my+f(2)} Q{cx+f(4)} {my+f(6)} {cx+f(8)} {my+f(2)}', stroke_width=2.5)
    return o


def body(cx, top, col, w=34, bot=184):
    return z('path', col, d=f'M{cx-w} {bot} Q{cx-w+2} {top} {cx} {top-2} Q{cx+w-2} {top} {cx+w} {bot}Z')


def arm(d, col, w=7):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=col, stroke_width=w)


def hand(x, y, r=8):
    return z('circle', SK, cx=x, cy=y, r=r)


def drop(x, y, c='#8fc7e8', k=1):
    return s('path', c, d=f'M{x} {y-8*k} Q{x+6*k} {y} {x} {y+4*k} Q{x-6*k} {y} {x} {y-8*k}Z', stroke_width=2)


def heart(x, y, c='#f07a8a', k=1):
    return z('path', c, d=f'M{x} {y+12*k} C{x-10*k} {y+4*k} {x-14*k} {y-4*k} {x-8*k} {y-9*k} C{x-4*k} {y-12*k} {x} {y-8*k} {x} {y-5*k} C{x} {y-8*k} {x+4*k} {y-12*k} {x+8*k} {y-9*k} C{x+14*k} {y-4*k} {x+10*k} {y+4*k} {x} {y+12*k}Z')


def spark(x, y, l=7):
    return s('path', d=f'M{x} {y-l} L{x} {y+l} M{x-l} {y} L{x+l} {y}', stroke_width=2.5)


# 1. drinking water
ITEMS['person-drinking-water'] = (
    body(86, 126, '#8fc7e8')
    + hd(86, 80, '#5a4033', 'smile', eyes='happy')
    + arm('M108 146 Q134 144 128 120', '#8fc7e8')
    + z('rect', '#f4f4f0', x=105, y=83, width=22, height=34, rx=3, transform='rotate(-30 116 100)')
    + s('rect', '#8fc7e8', x=107, y=99, width=18, height=16, rx=2, stroke='none', transform='rotate(-30 116 100)')
    + hand(127, 116)
    + drop(150, 70, '#8fc7e8', 0.8)
)

# 2. brushing teeth
ITEMS['person-brushing-teeth'] = (
    body(88, 126, '#f6a6b8')
    + s('circle', '#f6a6b8', cx=72, cy=150, r=3, stroke='none') + s('circle', '#f6a6b8', cx=100, cy=162, r=3, stroke='none')
    + hd(88, 80, '#2b2220', 'open', eyes='dot')
    + arm('M112 146 Q148 146 146 112', '#f6a6b8')
    + z('rect', '#8fc7e8', x=92, y=95, width=60, height=8, rx=4)
    + z('rect', '#ffffff', x=84, y=91, width=16, height=8, rx=2)
    + hand(146, 102, 9)
    + s('circle', '#ffffff', cx=70, cy=110, r=5, stroke_width=2) + s('circle', '#ffffff', cx=60, cy=100, r=3.5, stroke_width=2)
    + s('circle', '#ffffff', cx=112, cy=114, r=4, stroke_width=2) + s('circle', '#ffffff', cx=62, cy=118, r=3, stroke_width=2)
)

# 3. washing face
ITEMS['person-washing-face'] = (
    body(100, 124, '#7cc4b0')
    + arm('M72 140 Q62 124 66 106', '#7cc4b0') + arm('M128 140 Q138 124 134 106', '#7cc4b0')
    + hd(100, 80, '#5a4033', 'o', eyes='tight')
    + hand(67, 96, 10) + hand(133, 96, 10)
    + z('ellipse', '#f4f4f0', cx=100, cy=136, rx=64, ry=10)
    + z('path', '#f4f4f0', d='M36 136 Q40 180 100 180 Q160 180 164 136Z')
    + s('ellipse', '#8fc7e8', cx=100, cy=138, rx=50, ry=5, stroke_width=2)
    + drop(48, 70) + drop(152, 70) + drop(58, 44, k=0.8) + drop(142, 44, k=0.8) + drop(40, 100, k=0.7) + drop(160, 100, k=0.7)
)

# 4. getting dressed (pulling a sweater over the head)
SW = '#f07a8a'
ITEMS['person-getting-dressed'] = (
    body(100, 138, '#f4f4f0')
    + arm('M72 150 Q58 110 62 72', SW, 12) + arm('M128 150 Q142 110 138 72', SW, 12)
    + hd(100, 96, '#2b2220', 'o', eyes='dot')
    + z('path', SW, d='M58 80 Q100 92 142 80 L146 48 Q100 30 54 48Z')
    + s('path', d='M64 84 L62 74 M76 87 L75 77 M88 89 L88 79 M100 90 L100 80 M112 89 L112 79 M124 87 L125 77 M136 84 L138 74', stroke_width=2)
    + hand(58, 70, 9) + hand(142, 70, 9)
)

# 5. morning stretch
ITEMS['person-morning-stretch'] = (
    body(100, 138, '#8fb3e0')
    + s('circle', '#ffffff', cx=84, cy=158, r=3.5, stroke='none') + s('circle', '#ffffff', cx=112, cy=152, r=3.5, stroke='none')
    + s('circle', '#ffffff', cx=100, cy=172, r=3.5, stroke='none') + s('circle', '#ffffff', cx=122, cy=174, r=3.5, stroke='none')
    + arm('M74 150 Q54 110 64 56', '#8fb3e0', 10) + arm('M126 150 Q146 110 136 56', '#8fb3e0', 10)
    + hd(100, 100, '#c9a36b', 'o', eyes='happy')
    + hand(64, 50, 9) + hand(136, 50, 9)
    + spark(36, 70) + spark(164, 70) + spark(100, 32, 6)
)

# 6. commuter holding a train hand strap
ITEMS['person-train-strap'] = (
    z('rect', '#c9d3db', x=24, y=24, width=152, height=8, rx=4)
    + z('rect', '#f4f4f0', x=46, y=30, width=9, height=20, rx=2) + s('circle', cx=50, cy=60, r=10, stroke_width=4)
    + body(90, 150, '#5b6b7a')
    + s('path', '#ffffff', d='M78 150 L90 168 L102 150Z', stroke_width=2.5)
    + s('path', d='M66 156 L116 184', stroke='#8b6b4f', stroke_width=5)
    + arm('M112 160 Q142 130 142 86', '#5b6b7a', 10)
    + z('rect', '#f4f4f0', x=137, y=30, width=9, height=22, rx=2)
    + s('circle', cx=141, cy=64, r=11, stroke_width=4)
    + hd(90, 108, '#2b2220', 'smile', eyes='dot')
    + hand(141, 77, 9)
)

# 7. riding a bicycle
FR = '#e8735a'
ITEMS['person-riding-bicycle'] = (
    z('circle', '#5b6b7a', cx=52, cy=148, r=28) + s('circle', '#f4f4f0', cx=52, cy=148, r=19)
    + z('circle', '#5b6b7a', cx=150, cy=148, r=28) + s('circle', '#f4f4f0', cx=150, cy=148, r=19)
    + dot(52, 148, 4) + dot(150, 148, 4)
    + arm('M52 148 L94 148 L84 112 L52 148 M84 112 L136 110 L94 148 M136 110 L150 148', FR, 5)
    + s('path', d='M134 112 L130 96 L142 94', stroke_width=5)
    + z('ellipse', '#5b6b7a', cx=82, cy=106, rx=12, ry=5)
    + arm('M86 104 Q108 108 112 124 Q106 136 98 148', '#5b6b7a', 11)
    + z('ellipse', '#9ccf7a', cx=96, cy=84, rx=20, ry=26, transform='rotate(25 96 84)')
    + arm('M104 74 Q120 84 132 96', '#9ccf7a', 8)
    + hd(102, 50, '#5a4033', 'smile', r=25, eyes='dot')
    + hand(134, 96, 7) + z('ellipse', '#5b6b7a', cx=100, cy=150, rx=8, ry=4)
)

# 8. wearing a face mask
ITEMS['person-wearing-mask'] = (
    body(100, 126, '#7cc4b0')
    + hd(100, 82, '#5a4033', 'smile', eyes='happy')
    + s('path', d='M78 94 Q68 90 67 82 M78 112 Q68 108 67 96 M122 94 Q132 90 133 82 M122 112 Q132 108 133 96', stroke_width=2)
    + z('path', '#ffffff', d='M76 92 Q100 86 124 92 L122 112 Q100 122 78 112Z')
    + s('path', d='M82 100 Q100 96 118 100 M82 107 Q100 104 118 107', stroke_width=2)
)

# 9. person in a wheelchair
ITEMS['person-wheelchair'] = (
    s('path', d='M58 82 L62 144 M58 82 L46 80', stroke_width=5)
    + z('ellipse', '#f5b971', cx=86, cy=114, rx=24, ry=30)
    + arm('M96 138 L132 140 L136 168', '#8fb3e0', 12)
    + z('ellipse', '#8b6b4f', cx=142, cy=170, rx=10, ry=5)
    + s('path', d='M80 146 L132 150 L140 176', stroke_width=4)
    + z('circle', '#c9d3db', cx=80, cy=148, r=32) + s('circle', '#f4f4f0', cx=80, cy=148, r=24)
    + s('path', d='M80 124 L80 172 M56 148 L104 148 M63 131 L97 165 M97 131 L63 165', stroke_width=2) + dot(80, 148, 5)
    + z('circle', '#5b6b7a', cx=146, cy=176, r=6)
    + arm('M100 100 Q124 96 134 72', '#f5b971', 9)
    + hd(86, 62, '#2b2220', 'open', r=30, eyes='dot')
    + hand(136, 66, 9)
)

# 10. giving flowers
ITEMS['person-giving-flowers'] = (
    body(72, 126, '#8fb3e0')
    + hd(72, 80, '#c9a36b', 'smile', eyes='happy', style='long')
    + z('path', '#7cc4a0', d='M132 112 Q118 98 112 104 Q118 116 132 112Z') + z('path', '#7cc4a0', d='M150 108 Q166 92 172 100 Q164 112 150 108Z')
    + z('circle', '#f6a6b8', cx=126, cy=92, r=11) + z('circle', '#ffe27a', cx=160, cy=88, r=11)
    + z('circle', '#f07a8a', cx=142, cy=80, r=12)
    + dot(126, 92, 3.5, '#ffc94d') + dot(160, 88, 3.5, '#e8735a') + dot(142, 80, 4, '#ffc94d')
    + z('path', '#8fc7e8', d='M116 100 L168 100 L144 164Z')
    + arm('M94 146 Q116 146 132 140', '#8fb3e0', 9)
    + hand(138, 138, 9)
)

# 11. receiving a gift
ITEMS['person-receiving-gift'] = (
    body(100, 118, '#f6a6b8')
    + hd(100, 74, '#5a4033', 'open', eyes='happy', style='bun')
    + z('rect', '#9ccf7a', x=70, y=128, width=60, height=48, rx=3)
    + s('rect', '#f07a8a', x=94, y=128, width=12, height=48, stroke_width=2.5)
    + z('rect', '#9ccf7a', x=64, y=120, width=72, height=14, rx=3)
    + s('rect', '#f07a8a', x=94, y=120, width=12, height=14, stroke_width=2.5)
    + z('path', '#f07a8a', d='M100 120 Q84 100 80 112 Q82 122 100 120Z') + z('path', '#f07a8a', d='M100 120 Q116 100 120 112 Q118 122 100 120Z')
    + hand(68, 154, 9) + hand(132, 154, 9)
    + spark(40, 112) + spark(160, 112) + spark(46, 52, 5) + spark(156, 50, 5)
)

# 12. apologizing with hands pressed together
ITEMS['person-apologizing'] = (
    body(100, 124, '#9ccf7a')
    + hd(100, 80, '#2b2220', 'wavy', eyes='tight')
    + drop(142, 58, '#8fc7e8', 1.1)
    + arm('M70 150 Q80 160 94 150', '#9ccf7a', 9) + arm('M130 150 Q120 160 106 150', '#9ccf7a', 9)
    + z('ellipse', SK, cx=95, cy=134, rx=7, ry=18) + z('ellipse', SK, cx=105, cy=134, rx=7, ry=18)
    + s('path', d='M45 70 L36 66 M46 82 L36 84 M155 82 L164 84', stroke_width=2.5)
)

# 13. one person whispering to another
ITEMS['people-whispering'] = (
    body(140, 130, '#7cc4b0', w=30)
    + hd(140, 94, '#2b2220', 'o', r=29, eyes='dot')
    + body(62, 126, '#f5b971', w=30)
    + hd(62, 90, '#9a6a3f', 'smile', r=29, eyes='happy', style='long')
    + arm('M80 144 Q100 138 96 116', '#f5b971', 8)
    + z('ellipse', SK, cx=96, cy=104, rx=7, ry=11)
    + s('path', d='M104 92 Q108 98 104 104 M108 86 Q115 98 108 110', stroke_width=2.5)
)

# 14. two people arguing
ITEMS['people-arguing'] = (
    body(52, 136, '#8fb3e0', w=28)
    + hd(52, 104, '#5a4033', 'open', r=26, eyes='angry')
    + body(148, 136, '#f6a6b8', w=28)
    + hd(148, 104, '#2b2220', 'open', r=26, eyes='angry', style='bun')
    + arm('M72 150 Q82 146 82 130', '#8fb3e0', 8) + hand(82, 126, 8)
    + arm('M128 150 Q118 146 118 130', '#f6a6b8', 8) + hand(118, 126, 8)
    + z('path', '#c9d3db', d='M68 58 Q62 38 82 36 Q90 22 108 30 Q128 24 132 42 Q144 56 126 62 L82 62 Q66 66 68 58Z')
    + s('path', d='M80 50 Q84 38 92 46 Q98 54 104 42 Q110 32 116 46 Q120 54 124 46', stroke_width=2.5)
    + s('path', d='M88 92 L96 100 L92 104 L102 112 M112 92 L104 100 L108 104', stroke='#e8735a', stroke_width=3)
)

# 15. two people shaking hands to make up
ITEMS['people-making-up'] = (
    body(54, 122, '#9ccf7a', w=30)
    + hd(54, 84, '#5a4033', 'smile', r=27, eyes='happy')
    + body(146, 122, '#f5d58a', w=30)
    + hd(146, 84, '#c9a36b', 'smile', r=27, eyes='happy', style='long')
    + arm('M74 140 Q86 146 96 142', '#9ccf7a', 9) + arm('M126 140 Q114 146 104 142', '#f5d58a', 9)
    + z('ellipse', SK, cx=96, cy=142, rx=10, ry=8) + z('ellipse', SK, cx=104, cy=143, rx=10, ry=8)
    + heart(100, 56, k=1.1)
)

# 16. volunteer picking up litter
ITEMS['person-volunteer-cleanup'] = (
    body(80, 112, '#9ccf7a')
    + s('path', '#ffe27a', d='M64 112 L64 184 M96 112 L96 184', stroke='#ffe27a', stroke_width=6)
    + hd(80, 70, '#2b2220', 'smile', r=32, eyes='dot')
    + s('path', d='M120 130 L160 168 M126 128 L164 164', stroke_width=7)
    + s('path', d='M120 130 L160 168 M126 128 L164 164', stroke='#c9d3db', stroke_width=3)
    + z('rect', '#e8735a', x=148, y=166, width=26, height=12, rx=4)
    + arm('M106 128 Q118 124 122 128', '#9ccf7a', 9) + hand(124, 128, 8)
    + z('path', '#c9d3db', d='M34 140 Q20 182 44 182 Q68 182 54 140Z')
    + s('path', d='M38 140 L44 132 L50 140', stroke_width=2.5)
    + arm('M56 130 Q48 132 44 134', '#9ccf7a', 9) + hand(44, 134, 8)
)

# 17. putting a coin into a donation box
ITEMS['person-donation'] = (
    body(64, 116, '#8fb3e0', w=32)
    + hd(64, 72, '#5a4033', 'smile', r=32, eyes='happy', style='bun')
    + z('rect', '#d9a66b', x=104, y=122, width=64, height=58, rx=4)
    + z('rect', '#9a6a3f', x=100, y=112, width=72, height=12, rx=3)
    + s('rect', OUT, x=122, y=116, width=28, height=4, rx=2, stroke='none')
    + heart(136, 148, k=1.1)
    + arm('M88 132 Q112 112 130 90', '#8fb3e0', 9)
    + z('circle', '#ffc94d', cx=137, cy=102, r=7)
    + hand(132, 86, 8)
    + s('path', d='M152 94 L158 90 M154 104 L161 104', stroke_width=2.5)
)

# 18. voting at a ballot box
ITEMS['person-voting'] = (
    body(100, 104, '#f5b971')
    + hd(100, 58, '#2b2220', 'smile', r=32, eyes='dot')
    + z('rect', '#8fb3e0', x=50, y=124, width=100, height=56, rx=4)
    + z('rect', '#5b6b7a', x=44, y=114, width=112, height=14, rx=3)
    + s('rect', OUT, x=84, y=118, width=34, height=5, rx=2, stroke='none')
    + z('rect', '#ffffff', x=91, y=96, width=20, height=24, rx=2)
    + s('path', d='M95 104 L99 108 L106 100', stroke='#e8735a', stroke_width=2.5)
    + arm('M128 122 Q130 104 112 98', '#f5b971', 9)
    + hand(110, 98, 8)
)

# 19. three people waiting in line
ITEMS['people-queue'] = (
    body(52, 98, '#f5d58a', w=22, bot=150)
    + hd(52, 74, '#c9a36b', 'smile', r=22, eyes='dot', style='bun')
    + body(98, 116, '#7cc4b0', w=26, bot=166)
    + hd(98, 88, '#2b2220', 'smile', r=25, eyes='dot')
    + body(148, 136, '#f07a8a', w=30, bot=184)
    + hd(148, 104, '#5a4033', 'smile', r=28, eyes='dot', style='long')
    + s('path', d='M30 152 L74 152 M72 168 L124 168 M118 186 L178 186', stroke_width=2.5)
)

# 20. lost person holding an open map
ITEMS['person-lost-map'] = (
    body(100, 108, '#7cc4b0')
    + hd(100, 66, '#5a4033', 'wavy', r=32, eyes='worried')
    + drop(140, 48, '#8fc7e8', 1.1)
    + s('path', d='M154 38 Q154 28 164 28 Q174 28 174 38 Q174 46 164 46 Q158 46 158 40 Q158 34 164 34 Q168 34 168 38', stroke_width=2.5)
    + z('path', '#f5d58a', d='M48 122 L82 130 L118 122 L152 130 L152 178 L118 170 L82 178 L48 170Z')
    + s('path', d='M82 130 L82 178 M118 122 L118 170', stroke_width=2)
    + s('path', '#9ccf7a', d='M56 136 Q72 132 74 146 Q66 156 56 150Z', stroke_width=2)
    + s('path', d='M100 128 Q94 150 104 172', stroke='#8fc7e8', stroke_width=4)
    + s('path', d='M60 162 L76 158 M86 152 L96 144 M110 140 L124 148 M130 152 L140 142', stroke='#e8735a', stroke_width=2.5)
    + s('circle', '#e04b5a', cx=142, cy=140, r=5, stroke_width=2)
    + hand(50, 126, 8) + hand(150, 126, 8)
)
