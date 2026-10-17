from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}
SK = '#ffd9b8'

def hair_path(cx, cy, r):
    k = r / 34
    return (f'M{cx-r} {cy-2*k} Q{cx-32*k} {cy-36*k} {cx} {cy-35*k} Q{cx+32*k} {cy-36*k} {cx+r} {cy-2*k} '
            f'Q{cx+20*k} {cy-18*k} {cx} {cy-17*k} Q{cx-20*k} {cy-18*k} {cx-r} {cy-2*k}Z')

def eyes(cx, cy, r, closed=False, dy=0):
    k = r / 34
    ex = 12 * k; ey = cy + 2 * k + dy
    if closed:
        return s('path', d=f'M{cx-ex-5*k} {ey} Q{cx-ex} {ey+5*k} {cx-ex+5*k} {ey} M{cx+ex-5*k} {ey} Q{cx+ex} {ey+5*k} {cx+ex+5*k} {ey}', stroke_width=2.5)
    return dot(cx - ex, ey, max(2.6, 3.5 * k)) + dot(cx + ex, ey, max(2.6, 3.5 * k))

def mouth(cx, cy, r, kind='smile'):
    k = r / 34
    if kind == 'smile':
        return s('path', d=f'M{cx-6*k} {cy+16*k} Q{cx} {cy+21*k} {cx+6*k} {cy+16*k}', stroke_width=2.5)
    if kind == 'open':
        return s('path', '#c0504d', d=f'M{cx-8*k} {cy+14*k} Q{cx} {cy+28*k} {cx+8*k} {cy+14*k}Z', stroke_width=2.5)
    if kind == 'o':
        return f'<circle cx="{cx}" cy="{cy+18*k}" r="{4*k}" fill="#c0504d" stroke-width="2.5"/>'
    return ''

def hd(cx, cy, r, hair, m='smile', closed=False, dy=0, hair_on=True):
    k = r / 34
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    if hair_on:
        o += s('path', hair, d=hair_path(cx, cy, r))
    o += eyes(cx, cy, r, closed, dy) + cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k + dy, 7 * k, 4 * k)
    o += mouth(cx, cy + dy, r, m)
    return o

def long_hair(cx, cy, r, col):
    # back hair behind head (draw before head)
    return z('path', col, d=f'M{cx-r-4} {cy+r*0.9} Q{cx-r-8} {cy-r*1.1} {cx} {cy-r-4} Q{cx+r+8} {cy-r*1.1} {cx+r+4} {cy+r*0.9} Q{cx} {cy+r*0.7} {cx-r-4} {cy+r*0.9}Z')

def bun(cx, cy, r, col):
    return z('circle', col, cx=cx, cy=cy - r - 6, r=r * 0.42)

def bald(cx, cy, r, col='#e8e1d8'):
    # side tufts for grandpa
    return (s('path', col, d=f'M{cx-r+1} {cy+4} Q{cx-r-6} {cy-14} {cx-r+10} {cy-r*0.6} Q{cx-r+12} {cy-6} {cx-r+1} {cy+4}Z', stroke_width=2.5)
            + s('path', col, d=f'M{cx+r-1} {cy+4} Q{cx+r+6} {cy-14} {cx+r-10} {cy-r*0.6} Q{cx+r-12} {cy-6} {cx+r-1} {cy+4}Z', stroke_width=2.5))

def body(cx, top, bottom, col, hw=34):
    return z('path', col, d=f'M{cx-hw} {bottom} Q{cx-hw+2} {top+2} {cx} {top} Q{cx+hw-2} {top+2} {cx+hw} {bottom}Z')

def arm(d, col, w=9):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 5)

def hand(x, y, r=7):
    return z('circle', SK, cx=x, cy=y, r=r)

def ground(y=186, x1=28, x2=172):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2.5)

def heart(x, y, k=1.0, col='#f07a8a'):
    return s('path', col, d=f'M{x} {y+12*k} C{x-5*k} {y+8*k} {x-8*k} {y+4*k} {x-5*k} {y} C{x-2*k} {y-3*k} {x} {y-1*k} {x} {y+2*k} C{x} {y-1*k} {x+2*k} {y-3*k} {x+5*k} {y} C{x+8*k} {y+4*k} {x+5*k} {y+8*k} {x} {y+12*k}Z', stroke_width=2)

def glasses(cx, cy, r):
    k = r / 34
    ey = cy + 2 * k
    return (s('circle', cx=cx - 12 * k, cy=ey, r=9 * k, stroke_width=2.2) + s('circle', cx=cx + 12 * k, cy=ey, r=9 * k, stroke_width=2.2)
            + s('path', d=f'M{cx-3*k} {ey-1} Q{cx} {ey-3*k} {cx+3*k} {ey-1}', stroke_width=2.2))

def mustache(cx, y, w=10, col='#e8e1d8'):
    return s('path', col, d=f'M{cx} {y} Q{cx-w*0.6} {y-4} {cx-w} {y+2} Q{cx-w*0.5} {y+6} {cx} {y+2} Q{cx+w*0.5} {y+6} {cx+w} {y+2} Q{cx+w*0.6} {y-4} {cx} {y}Z', stroke_width=2)

# 1. grandpa with cane
ITEMS['grandpa-cane'] = (
    ground(186, 40, 166)
    + z('ellipse', '#8b6b4f', cx=84, cy=182, rx=12, ry=6) + z('ellipse', '#8b6b4f', cx=114, cy=182, rx=12, ry=6)
    + body(98, 132, 180, '#9a6a3f', 36)
    + s('path', '#f6e0c4', d='M88 134 L98 152 L108 134Z', stroke_width=2.5)
    + dot(98, 162, 3) + dot(98, 174, 3)
    + s('path', d='M148 186 L148 120 Q148 106 136 106 Q126 106 126 116', stroke_width=11)
    + s('path', d='M148 186 L148 120 Q148 106 136 106 Q126 106 126 116', stroke='#d9a66b', stroke_width=5)
    + arm('M124 150 Q136 140 146 130', '#9a6a3f', 10)
    + hand(148, 128, 8)
    + hd(98, 88, 34, None, m='', closed=True, hair_on=False)
    + bald(98, 88, 34)
    + glasses(98, 88, 34)
    + mustache(98, 104, 12)
    + s('path', d='M94 112 Q98 115 102 112', stroke_width=2.5)
)

# 2. grandparents couple
ITEMS['grandparents-couple'] = (
    body(62, 122, 184, '#7cc4b0', 30)
    + s('path', '#f6e0c4', d='M54 124 L62 138 L70 124Z', stroke_width=2.5)
    + body(140, 122, 184, '#f6a6b8', 30)
    + s('path', '#ffffff', d='M130 124 L140 134 L150 124Z', stroke_width=2.5)
    + arm('M86 150 Q100 158 114 150', '#f6a6b8', 9)
    + hd(62, 90, 28, None, m='', closed=True, hair_on=False)
    + bald(62, 90, 28)
    + mustache(62, 104, 10)
    + s('path', d='M58 111 Q62 114 66 111', stroke_width=2.5)
    + bun(140, 90, 28, '#e8e1d8')
    + hd(140, 90, 28, '#e8e1d8', m='smile', closed=True)
    + glasses(140, 90, 28)
    + heart(101, 46, 1.4)
)

# 3. family of three
ITEMS['family-three'] = (
    body(48, 104, 184, '#8fb3e0', 26)
    + long_hair(152, 74, 24, '#5a4033')
    + body(152, 104, 184, '#f6a6b8', 26)
    + arm('M64 150 Q76 156 84 150', '#8fb3e0', 9) + arm('M136 150 Q124 156 116 150', '#f6a6b8', 9)
    + body(100, 146, 184, '#ffe27a', 20)
    + hand(82, 152, 6) + hand(118, 152, 6)
    + hd(48, 74, 24, '#2b2220')
    + hd(152, 74, 24, '#5a4033')
    + hd(100, 122, 22, '#5a4033', m='open')
)

# 4. mother holding baby
ITEMS['mother-holding-baby'] = (
    long_hair(100, 70, 32, '#2b2220')
    + body(100, 104, 186, '#7cc4b0', 42)
    + z('ellipse', '#f6e0c4', cx=104, cy=146, rx=38, ry=22, transform='rotate(-12 104 146)')
    + z('circle', SK, cx=82, cy=136, r=17)
    + s('path', d='M80 120 Q78 114 84 114', stroke_width=2.5)
    + eyes(82, 134, 17, closed=True) + cheeks(72, 92, 142, 4, 2.5)
    + s('path', d='M80 145 Q82 147 84 145', stroke_width=2)
    + arm('M64 138 Q70 172 110 166 Q134 162 142 148', '#7cc4b0', 10)
    + hand(142, 144, 7)
    + hd(100, 70, 32, '#2b2220', closed=True)
    + heart(146, 64, 1.0) + heart(162, 88, 0.7)
)

# 5. father piggyback
ITEMS['father-piggyback'] = (
    body(130, 92, 140, '#f07a8a', 24)
    + hd(130, 66, 24, '#c9a36b', m='open')
    + body(92, 132, 188, '#8fc7e8', 38)
    + arm('M150 128 Q166 142 170 160', '#5b6b7a', 11)
    + z('ellipse', '#e8735a', cx=172, cy=164, rx=9, ry=6)
    + arm('M66 150 Q74 132 112 126', '#8fc7e8', 10)
    + arm('M124 150 Q140 146 150 132', '#8fc7e8', 10)
    + hand(150, 130, 8)
    + hd(90, 100, 30, '#2b2220')
    + arm('M124 104 Q128 120 120 130', '#f07a8a', 9) + hand(119, 131, 7)
)

# 6. siblings holding hands
ITEMS['siblings-holding-hands'] = (
    ground(186, 30, 170)
    + z('ellipse', '#8b6b4f', cx=52, cy=182, rx=10, ry=6) + z('ellipse', '#8b6b4f', cx=78, cy=182, rx=10, ry=6)
    + z('ellipse', '#e8735a', cx=124, cy=182, rx=9, ry=5) + z('ellipse', '#e8735a', cx=146, cy=182, rx=9, ry=5)
    + body(64, 120, 178, '#8fc7e8', 28)
    + body(136, 132, 178, '#f6a6b8', 24)
    + arm('M86 150 Q100 160 114 154', '#8fc7e8', 9)
    + hand(100, 158, 7)
    + hd(64, 86, 30, '#5a4033', m='open')
    + s('path', d='M96 70 Q92 66 96 64', stroke_width=0)
    + z('ellipse', '#5a4033', cx=136 - 30, cy=96, rx=7, ry=12)
    + z('ellipse', '#5a4033', cx=136 + 30, cy=96, rx=7, ry=12)
    + hd(136, 104, 26, '#5a4033')
)

# 7. couple holding hands
ITEMS['couple-holding-hands'] = (
    body(62, 120, 184, '#8fb3e0', 30)
    + long_hair(138, 88, 26, '#c9a36b')
    + body(138, 120, 184, '#f5b971', 30)
    + arm('M86 150 Q100 162 114 150', '#8fb3e0', 9)
    + hand(100, 158, 7)
    + hd(62, 86, 28, '#2b2220')
    + hd(138, 88, 26, '#c9a36b')
    + heart(100, 46, 1.5) + heart(78, 30, 0.8) + heart(124, 30, 0.8)
)

# 8. friends high five
ITEMS['friends-high-five'] = (
    arm('M76 130 Q88 90 96 58', '#ffe27a', 10) + arm('M124 130 Q112 90 104 58', '#7cc4b0', 10)
    + z('circle', SK, cx=94, cy=52, r=9) + z('circle', SK, cx=106, cy=52, r=9)
    + s('path', d='M100 22 L100 32 M80 30 L86 38 M120 30 L114 38 M74 48 L82 50 M126 48 L118 50', stroke_width=2.5)
    + body(56, 132, 186, '#ffe27a', 30)
    + body(144, 132, 186, '#7cc4b0', 30)
    + hd(54, 102, 28, '#5a4033', m='open')
    + hd(146, 102, 28, '#2b2220', m='open')
)

# 9. child drawing with crayons
ITEMS['child-drawing'] = (
    body(100, 116, 160, '#f5d58a', 34)
    + hd(100, 82, 32, '#5a4033', dy=4)
    + z('rect', '#d9a66b', x=26, y=140, width=148, height=16, rx=3)
    + s('path', d='M40 156 L40 186 M160 156 L160 186', stroke_width=6)
    + s('path', '#ffffff', d='M52 142 L62 120 L148 120 L156 142Z', stroke_width=2.5)
    + s('circle', '#ffc94d', cx=78, cy=129, r=5, stroke_width=2)
    + s('path', d='M92 134 Q100 124 108 132 Q114 126 122 132', stroke='#e04b5a', stroke_width=3)
    + arm('M120 128 Q128 124 132 126', '#f5d58a', 9)
    + s('rect', '#8fb3e0', x=128, y=110, width=6, height=22, rx=2, stroke_width=2, transform='rotate(25 131 121)')
    + hand(132, 126, 7)
    + s('rect', '#9ccf7a', x=58, y=146, width=20, height=5, rx=2, stroke_width=1.5)
    + s('rect', '#f07a8a', x=84, y=146, width=20, height=5, rx=2, stroke_width=1.5)
)

# 10. girl with big hair ribbon
ITEMS['girl-hair-ribbon'] = (
    z('ellipse', '#5a4033', cx=64, cy=108, rx=10, ry=16) + z('ellipse', '#5a4033', cx=136, cy=108, rx=10, ry=16)
    + body(100, 136, 186, '#f6a6b8', 34)
    + s('path', '#ffffff', d='M88 138 Q94 148 100 140 Q106 148 112 138Z', stroke_width=2.5)
    + hd(100, 98, 34, '#5a4033')
    + z('path', '#f07a8a', d='M100 60 Q76 38 66 52 Q66 68 100 60Z')
    + z('path', '#f07a8a', d='M100 60 Q124 38 134 52 Q134 68 100 60Z')
    + z('circle', '#f07a8a', cx=100, cy=60, r=8)
)

# 11. teen with headphones
ITEMS['teen-headphones'] = (
    body(100, 136, 186, '#5b6b7a', 36)
    + s('path', d='M88 138 L88 170 M112 138 L112 170', stroke='#f4f4f0', stroke_width=3)
    + hd(100, 96, 34, '#2b2220', closed=True)
    + s('path', d='M64 94 Q62 50 100 50 Q138 50 136 94', stroke_width=11)
    + s('path', d='M64 94 Q62 50 100 50 Q138 50 136 94', stroke='#e8735a', stroke_width=5)
    + z('rect', '#e8735a', x=56, y=84, width=16, height=28, rx=7)
    + z('rect', '#e8735a', x=128, y=84, width=16, height=28, rx=7)
    + s('path', '#3b2f2a', d='M160 54 L160 34 L172 30 L172 50', stroke_width=2.5)
    + dot(156, 56, 5) + dot(168, 52, 5)
    + s('path', d='M36 50 L36 34 L44 38', stroke_width=2.5) + dot(32, 52, 5)
)

# 12. person reading a book
ITEMS['person-reading-book'] = (
    body(100, 128, 186, '#8fc7e8', 38)
    + hd(100, 86, 34, '#5a4033', closed=True, dy=6)
    + z('path', '#f4f4f0', d='M100 134 Q80 124 56 130 L60 176 Q82 170 100 180Z')
    + z('path', '#f4f4f0', d='M100 134 Q120 124 144 130 L140 176 Q118 170 100 180Z')
    + s('path', d='M68 144 Q80 140 92 144 M68 154 Q80 150 92 154 M108 144 Q120 140 132 144 M108 154 Q120 150 132 154', stroke_width=2)
    + s('path', '#e8735a', d='M54 128 L50 132 L56 182 Q80 174 100 184 Q120 174 144 182 L150 132 L146 128 L140 176 Q118 170 100 180 Q82 170 60 176Z', stroke_width=2.5)
    + hand(56, 156, 8) + hand(144, 156, 8)
)

# 13. person writing a letter at desk
ITEMS['person-writing-letter'] = (
    body(96, 116, 156, '#9ccf7a', 34)
    + hd(96, 80, 32, '#2b2220', dy=5)
    + z('rect', '#d9a66b', x=26, y=140, width=148, height=16, rx=3)
    + s('path', d='M40 156 L40 186 M160 156 L160 186', stroke_width=6)
    + s('path', '#ffffff', d='M58 140 L66 114 L126 114 L132 140Z', stroke_width=2.5)
    + s('path', d='M72 122 L118 122 M70 128 L120 128 M68 134 L104 134', stroke_width=1.8)
    + s('path', '#f07a8a', d='M150 120 L176 120 L176 138 L150 138Z', stroke_width=2.5)
    + s('path', d='M150 120 L163 130 L176 120', stroke_width=2)
    + s('path', d='M122 98 L108 132', stroke_width=7) + s('path', d='M122 98 L108 132', stroke='#ffc94d', stroke_width=3)
    + arm('M126 124 Q120 130 116 128', '#9ccf7a', 9)
    + hand(114, 126, 7)
)

# 14. person on phone call
ITEMS['person-phone-call'] = (
    body(96, 134, 186, '#e8735a', 36)
    + arm('M120 152 Q144 140 138 108', '#e8735a', 10)
    + hd(96, 92, 34, '#5a4033', m='open')
    + z('rect', '#5b6b7a', x=124, y=72, width=16, height=34, rx=4, transform='rotate(12 132 89)')
    + hand(136, 104, 8)
    + s('path', d='M152 66 Q160 74 158 86 M162 56 Q174 72 170 92', stroke_width=2.5)
)

# 15. person taking a selfie
ITEMS['person-selfie'] = (
    body(88, 138, 186, '#f6a6b8', 36)
    + arm('M110 150 Q140 120 146 76', '#f6a6b8', 10)
    + hd(86, 100, 34, '#c9a36b', m='open')
    + z('rect', '#5b6b7a', x=136, y=34, width=26, height=44, rx=5, transform='rotate(14 149 56)')
    + s('rect', '#d8eef8', x=141, y=40, width=16, height=28, rx=2, stroke_width=2, transform='rotate(14 149 56)')
    + hand(146, 76, 8)
    + s('path', d='M54 122 L48 98 M58 120 L58 96', stroke_width=7)
    + s('path', d='M54 122 L48 98 M58 120 L58 96', stroke=SK, stroke_width=3)
    + z('circle', SK, cx=56, cy=126, r=8)
    + s('path', d='M168 26 L176 18 M174 38 L184 36', stroke_width=2.5)
)

# 16. person with umbrella in rain
def drop(x, y, k=1.0):
    return s('path', '#8fc7e8', d=f'M{x} {y} Q{x-5*k} {y+9*k} {x} {y+12*k} Q{x+5*k} {y+9*k} {x} {y}Z', stroke_width=2)
ITEMS['person-umbrella-rain'] = (
    drop(30, 40) + drop(170, 52) + drop(26, 112) + drop(176, 128) + drop(40, 160, 0.8) + drop(166, 170, 0.8)
    + body(100, 132, 184, '#ffe27a', 34)
    + s('path', d='M100 140 L100 176', stroke_width=2.5) + dot(92, 152, 2.5) + dot(92, 166, 2.5)
    + s('path', d='M120 50 L120 140 Q120 150 112 150', stroke_width=4)
    + hd(98, 96, 30, '#2b2220')
    + z('path', '#8fc7e8', d='M44 62 Q48 18 120 18 Q186 20 190 62 Q178 54 166 62 Q154 54 142 62 Q130 54 118 62 Q106 54 94 62 Q80 54 68 62 Q56 54 44 62Z')
    + s('path', d='M118 18 L118 10', stroke_width=4)
    + s('path', d='M118 20 Q106 34 106 60 M118 20 Q150 30 154 60', stroke_width=2)
    + arm('M124 146 Q126 132 120 124', '#ffe27a', 9)
    + hand(120, 120, 8)
)

# 17. person walking a small dog
ITEMS['person-walking-dog'] = (
    ground(186, 26, 176)
    + arm('M64 150 Q58 166 54 178', '#5b6b7a', 11) + arm('M82 150 Q90 166 96 178', '#5b6b7a', 11)
    + z('ellipse', '#8b6b4f', cx=50, cy=181, rx=10, ry=5) + z('ellipse', '#8b6b4f', cx=100, cy=181, rx=10, ry=5)
    + body(72, 104, 156, '#7cc4b0', 30)
    + s('path', d='M98 132 Q130 170 144 146', stroke='#e04b5a', stroke_width=2.5)
    + arm('M90 120 Q98 128 98 132', '#7cc4b0', 9) + hand(98, 132, 7)
    + hd(70, 70, 30, '#5a4033')
    + s('path', d='M174 150 Q184 140 180 132', stroke_width=3)
    + z('ellipse', '#f5b971', cx=152, cy=164, rx=24, ry=14)
    + s('path', d='M136 174 L136 182 M148 176 L148 182 M160 176 L160 182 M170 174 L170 182', stroke_width=5)
    + z('circle', '#f5b971', cx=138, cy=144, r=16)
    + z('path', '#d9a66b', d='M124 134 Q116 148 124 156 Q130 148 130 136Z')
    + z('path', '#d9a66b', d='M150 134 Q158 148 150 156 Q144 148 144 136Z')
    + s('rect', '#e04b5a', x=128, y=156, width=20, height=5, rx=2, stroke_width=1.5)
    + dot(132, 144, 2.5) + dot(144, 144, 2.5) + f'<ellipse cx="138" cy="150" rx="3" ry="2.2" fill="{OUT}" stroke="none"/>'
    + cheeks(127, 149, 151, 3.5, 2)
)

# 18. person carrying shopping bags
def bag(x, y, w, h, col, hcol=OUT):
    return (s('path', d=f'M{x+w*0.3} {y} Q{x+w*0.3} {y-14} {x+w/2} {y-14} Q{x+w*0.7} {y-14} {x+w*0.7} {y}', stroke_width=3)
            + z('rect', col, x=x, y=y, width=w, height=h, rx=3))
ITEMS['person-shopping-bags'] = (
    body(100, 134, 186, '#8fb3e0', 34)
    + bag(26, 140, 34, 40, '#f5b971') + bag(140, 144, 32, 36, '#9ccf7a')
    + s('rect', '#f07a8a', x=36, y=154, width=14, height=10, rx=2, stroke_width=2)
    + arm('M72 148 Q56 140 44 128', '#8fb3e0', 10) + arm('M128 148 Q144 140 156 132', '#8fb3e0', 10)
    + hand(43, 127, 8) + hand(157, 131, 8)
    + hd(100, 94, 34, '#5a4033', m='open')
)

# 19. person pushing a shopping cart
ITEMS['person-shopping-cart'] = (
    ground(188, 24, 178)
    + body(60, 116, 176, '#f5b971', 28)
    + s('path', d='M50 176 L50 184 M70 176 L70 184', stroke_width=7)
    + z('path', '#f4f4f0', d='M98 100 L176 100 L166 148 L108 148Z')
    + s('path', '#9ccf7a', d='M114 100 Q114 84 128 84 Q142 84 142 100Z', stroke_width=2.5)
    + s('rect', '#f07a8a', x=144, y=78, width=18, height=22, rx=3, stroke_width=2.5)
    + z('path', '#f4f4f0', d='M98 100 L176 100 L166 148 L108 148Z')
    + s('path', d='M117 112 L164 112 M114 124 L161 124 M112 136 L159 136 M124 100 L126 148 M144 100 L142 148', stroke_width=2)
    + s('path', d='M98 100 L90 86 L80 86 M110 148 L106 164 L168 164', stroke_width=4)
    + z('circle', '#5b6b7a', cx=114, cy=174, r=7) + z('circle', '#5b6b7a', cx=158, cy=174, r=7)
    + arm('M76 136 Q84 104 82 88', '#f5b971', 9) + hand(82, 86, 7)
    + hd(58, 84, 30, '#2b2220')
)

# 20. person eating a meal
ITEMS['person-eating-meal'] = (
    body(100, 118, 160, '#e8735a', 36)
    + s('path', '#ffffff', d='M78 122 Q100 152 122 122 Q100 128 78 122Z', stroke_width=2.5)
    + hd(100, 82, 32, '#5a4033', m='open')
    + z('rect', '#d9a66b', x=24, y=146, width=152, height=14, rx=3)
    + s('path', d='M40 160 L40 188 M160 160 L160 188', stroke_width=6)
    + z('ellipse', '#ffffff', cx=96, cy=140, rx=40, ry=9)
    + s('path', '#f5d58a', d='M74 138 Q80 124 96 124 Q112 124 118 138Z', stroke_width=2.5)
    + dot(88, 130, 3, '#e04b5a') + dot(104, 128, 3, '#9ccf7a')
    + s('path', d='M144 140 L124 106', stroke_width=8) + s('path', d='M144 140 L124 106', stroke='#c9d3db', stroke_width=3)
    + s('path', '#c9d3db', d='M118 96 L130 103 L126 110 L116 104Z', stroke_width=2.5)
    + s('path', d='M118 96 L122 86 M122 98 L127 89 M126 101 L132 92', stroke_width=2.5)
    + hand(144, 140, 8)
    + heart(160, 50, 1.0) + heart(36, 72, 0.8)
)
