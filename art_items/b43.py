from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def _n(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def head(cx, cy, r, hair, mouth='smile'):
    """face() を縮小したもの"""
    k = r / 34
    N = _n
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    if hair:
        o += s('path', hair, d=(f'M{N(cx-r)} {N(cy-2*k)} Q{N(cx-32*k)} {N(cy-36*k)} {N(cx)} {N(cy-35*k)} '
                                f'Q{N(cx+32*k)} {N(cy-36*k)} {N(cx+r)} {N(cy-2*k)} Q{N(cx+20*k)} {N(cy-18*k)} {N(cx)} {N(cy-17*k)} '
                                f'Q{N(cx-20*k)} {N(cy-18*k)} {N(cx-r)} {N(cy-2*k)}Z'))
    er = max(2.6, 3.5 * k)
    o += dot(cx - 12 * k, cy + 2 * k, er) + dot(cx + 12 * k, cy + 2 * k, er)
    o += cheeks(N(cx - 20 * k), N(cx + 20 * k), N(cy + 13 * k), N(7 * k), N(4 * k))
    if mouth == 'smile':
        o += s('path', d=f'M{N(cx-6*k)} {N(cy+16*k)} Q{N(cx)} {N(cy+21*k)} {N(cx+6*k)} {N(cy+16*k)}', stroke_width=2.5)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{N(cx-8*k)} {N(cy+14*k)} Q{N(cx)} {N(cy+28*k)} {N(cx+8*k)} {N(cy+14*k)}Z', stroke_width=2.5)
    else:
        o += f'<circle cx="{N(cx)}" cy="{N(cy+18*k)}" r="{N(max(3,4*k))}" fill="#c0504d" stroke-width="2.5"/>'
    return o


def body(cx, top, w, bottom, color):
    return z('path', color, d=f'M{cx-w} {bottom} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bottom}Z')


def arm(d, color):
    return s('path', d=d, stroke_width=8) + s('path', d=d, stroke=color, stroke_width=3)


def hand(x, y, r=6):
    return z('circle', SK, cx=x, cy=y, r=r)


def star(cx, cy, R, c='#ffe27a', w=2.5):
    import math
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = R if i % 2 == 0 else R * 0.45
        pts.append(f'{_n(cx + rr*math.cos(a))} {_n(cy + rr*math.sin(a))}')
    return s('path', c, d='M' + ' L'.join(pts) + 'Z', stroke_width=w)


def sparkle(cx, cy, r, c='#ffe27a'):
    q = r * 0.3
    return s('path', c, d=f'M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r}Z', stroke_width=2)


def heart(cx, cy, k, c):
    return s('path', c, d=(f'M{cx} {_n(cy+9*k)} C{_n(cx-5*k)} {_n(cy+5*k)} {_n(cx-9*k)} {_n(cy+1*k)} {_n(cx-6*k)} {_n(cy-4*k)} '
                           f'C{_n(cx-3*k)} {_n(cy-7*k)} {cx} {_n(cy-5*k)} {cx} {_n(cy-2*k)} C{cx} {_n(cy-5*k)} {_n(cx+3*k)} {_n(cy-7*k)} {_n(cx+6*k)} {_n(cy-4*k)} '
                           f'C{_n(cx+9*k)} {_n(cy+1*k)} {_n(cx+5*k)} {_n(cy+5*k)} {cx} {_n(cy+9*k)}Z'), stroke_width=2.5)


# 1. classroom-hands
o = ''
kids = ((46, '#5a4033', '#8fc7e8', -1, 'smile'), (100, '#2b2220', '#f6a6b8', 1, 'open'), (154, '#c9a36b', '#9ccf7a', 1, 'smile'))
for cx, hair, col, side, m in kids:
    sx = cx + side * 15
    hx = cx + side * 22
    o += arm(f'M{sx} 136 Q{hx + side*4} 100 {hx} 66', col) + hand(hx, 62)
    o += body(cx, 122, 24, 168, col) + head(cx, 106, 19, hair, m)
o += z('rect', '#d9a66b', x=26, y=150, width=150, height=14, rx=3)
o += s('path', d='M40 164 L40 180 M162 164 L162 180')
ITEMS['classroom-hands'] = o

# 2. test-paper
o = (z('rect', '#ffffff', x=40, y=28, width=110, height=148, rx=4)
     + s('rect', '#f4f4f0', x=52, y=38, width=56, height=14, rx=2, stroke_width=2))
for y in (72, 98, 124, 150):
    o += (s('path', d=f'M80 {y} L136 {y}', stroke='#c9d3db', stroke_width=4)
          + f'<circle cx="62" cy="{y}" r="9" fill="none" stroke="#e04b5a" stroke-width="3.5"/>')
o += f'<path d="M132 46 Q118 46 120 36 Q124 26 136 30 Q146 36 140 48 Q132 58 120 52" fill="none" stroke="#e04b5a" stroke-width="3.5"/>'
o += ('<g transform="rotate(32 152 128)">'
      + z('rect', '#ffc94d', x=144, y=86, width=16, height=66, rx=1)
      + z('path', '#f6e0c4', d='M144 152 L160 152 L152 170Z')
      + s('path', '#5b6b7a', d='M149.5 162 L154.5 162 L152 170Z', stroke_width=2)
      + z('rect', '#f6a6b8', x=144, y=74, width=16, height=12, rx=3)
      + '</g>')
ITEMS['test-paper'] = o

# 3. homework
o = (body(100, 114, 40, 172, '#f5b971') + face(100, 78, SK, '#5a4033', 'smile')
     + s('path', d='M36 168 L36 182 M164 168 L164 182')
     + z('path', '#d9a66b', d='M34 136 L166 136 L178 160 L22 160Z')
     + z('rect', '#9a6a3f', x=22, y=160, width=156, height=10, rx=2)
     + z('path', '#ffffff', d='M62 156 L66 140 Q84 136 100 142 L100 156 Q82 152 62 156Z')
     + z('path', '#ffffff', d='M138 156 L134 140 Q116 136 100 142 L100 156 Q118 152 138 156Z')
     + s('path', d='M72 146 Q84 143 94 147 M70 151 Q82 148 94 152 M106 147 Q116 143 128 146', stroke='#8fc7e8', stroke_width=2)
     + hand(78, 140)
     + '<g transform="rotate(35 128 132)">' + z('rect', '#e8735a', x=124, y=110, width=8, height=30, rx=1)
     + s('path', '#f6e0c4', d='M124 140 L132 140 L128 148Z', stroke_width=2) + '</g>'
     + hand(126, 140))
ITEMS['homework'] = o

# 4. studying-late
o = (z('rect', '#5b6b7a', x=24, y=26, width=64, height=56, rx=4)
     + s('path', d='M56 26 L56 82 M24 54 L88 54', stroke_width=3)
     + s('path', '#ffe27a', d='M44 32 Q30 40 38 50 Q46 54 52 46 Q42 46 44 32Z', stroke_width=2)
     + sparkle(72, 40, 5) + sparkle(36, 70, 4) + sparkle(76, 70, 4)
     + sparkle(170, 34, 6) + sparkle(150, 52, 4)
     + body(114, 130, 38, 176, '#8fb3e0') + face(114, 94, SK, '#2b2220', 'o')
     + s('path', d='M98 96 Q102 99 106 96 M122 96 Q126 99 130 96', stroke_width=2.5)
     + s('path', d='M45 116 L45 148', stroke_width=4)
     + z('path', '#7cc4b0', d='M34 96 L56 96 L64 118 L26 118Z')
     + z('rect', '#d9a66b', x=22, y=148, width=156, height=16, rx=3)
     + z('ellipse', '#7cc4b0', cx=45, cy=148, rx=14, ry=5)
     + z('path', '#ffffff', d='M84 150 Q98 138 114 146 Q130 138 144 150Z')
     + z('rect', '#e8735a', x=152, y=128, width=18, height=20, rx=3)
     + s('path', d='M170 132 Q178 138 170 144', stroke_width=3)
     + s('path', d='M156 122 Q153 116 158 112 M164 122 Q161 116 166 112', stroke_width=2))
o = o.replace(dot(102, 96) + dot(126, 96), '')
ITEMS['studying-late'] = o

# 5. entrance-ceremony
o = s('path', d='M182 40 Q150 34 120 40 M150 36 Q140 50 128 60', stroke='#8b6b4f', stroke_width=7)
for cx, cy, r in ((128, 34, 16), (150, 30, 18), (172, 38, 14), (124, 58, 13), (170, 60, 12), (40, 44, 13), (58, 32, 15), (30, 30, 10)):
    o += z('circle', '#f6a6b8', cx=cx, cy=cy, r=r)
for cx, cy in ((150, 30), (124, 58), (58, 32)):
    o += f'<circle cx="{cx}" cy="{cy}" r="3" fill="#f07a8a" stroke="none"/>'
o += s('path', d='M22 52 Q34 44 46 46', stroke='#8b6b4f', stroke_width=6)
o = o.replace(s('path', d='M22 52 Q34 44 46 46', stroke='#8b6b4f', stroke_width=6), '')
o += (z('rect', '#e04b5a', x=58, y=134, width=84, height=40, rx=10)
      + body(100, 136, 34, 182, '#5b6b7a')
      + s('path', d='M78 140 L78 180 M122 140 L122 180', stroke='#e04b5a', stroke_width=6)
      + s('path', '#ffffff', d='M90 138 L100 154 L110 138Z', stroke_width=2.5)
      + face(100, 102, SK, '#2b2220', 'open'))
for a in range(5):
    import math
    t = math.radians(-90 + a * 72)
    o += f'<circle cx="{_n(110 + 6*math.cos(t))}" cy="{_n(160 + 6*math.sin(t))}" r="4.5" fill="#f6a6b8" stroke-width="2"/>'
o += '<circle cx="110" cy="160" r="2.5" fill="#ffe27a" stroke="none"/>'
for x, y, rot in ((34, 96, 20), (164, 100, -30), (48, 136, 50), (156, 140, 10), (90, 52, -20), (176, 82, 40)):
    o += f'<ellipse cx="{x}" cy="{y}" rx="6" ry="3.5" transform="rotate({rot} {x} {y})" fill="#f6a6b8" stroke-width="2"/>'
ITEMS['entrance-ceremony'] = o


# 6. graduation-ceremony
def grad(cx, cy, hair, mouth, dip):
    r = 25
    o = body(cx, cy + 22, 32, 182, '#5b6b7a')
    o += s('path', '#ffffff', d=f'M{cx-10} {cy+24} L{cx} {cy+38} L{cx+10} {cy+24}Z', stroke_width=2.5)
    o += head(cx, cy, r, hair, mouth)
    o += z('path', '#5b6b7a', d=f'M{cx-19} {cy-14} L{cx-19} {cy-25} L{cx+19} {cy-25} L{cx+19} {cy-14} Q{cx} {cy-19} {cx-19} {cy-14}Z')
    o += z('path', '#5b6b7a', d=f'M{cx-36} {cy-28} L{cx} {cy-40} L{cx+36} {cy-28} L{cx} {cy-17}Z')
    o += s('path', d=f'M{cx} {cy-29} Q{cx+22} {cy-26} {cx+26} {cy-12}', stroke='#ffc94d', stroke_width=3)
    o += f'<circle cx="{cx+26}" cy="{cy-9}" r="3.5" fill="#ffc94d" stroke-width="2"/>'
    o += dot(cx, cy - 29, 3)
    return o


o = grad(62, 96, '#2b2220', 'smile', 0) + grad(138, 96, '#c9a36b', 'open', 0)
o += ('<g transform="rotate(-20 64 150)">' + z('rect', '#f4f4f0', x=42, y=144, width=44, height=12, rx=6)
      + s('rect', '#e04b5a', x=60, y=144, width=7, height=12, stroke_width=2) + '</g>'
      + hand(56, 156) + hand(76, 148))
o += (arm('M150 128 Q166 108 168 88', '#5b6b7a') + '<g transform="rotate(70 168 70)">'
      + z('rect', '#f4f4f0', x=148, y=64, width=40, height=12, rx=6)
      + s('rect', '#e04b5a', x=164, y=64, width=7, height=12, stroke_width=2) + '</g>' + hand(168, 86))
ITEMS['graduation-ceremony'] = o

# 7. school-uniform
o = (z('rect', SK, x=82, y=156, width=11, height=14) + z('rect', SK, x=107, y=156, width=11, height=14)
     + z('ellipse', '#8b6b4f', cx=86, cy=174, rx=11, ry=5) + z('ellipse', '#8b6b4f', cx=114, cy=174, rx=11, ry=5)
     + z('path', '#8fb3e0', d='M68 134 L132 134 L144 160 L56 160Z')
     + s('path', d='M80 136 L74 160 M93 136 L91 160 M107 136 L109 160 M120 136 L126 160', stroke_width=2)
     + z('rect', '#8b6b4f', x=134, y=120, width=36, height=28, rx=5)
     + s('path', d='M144 120 Q152 108 160 120', stroke_width=3)
     + body(100, 94, 36, 142, '#5b6b7a')
     + s('path', '#ffffff', d='M86 96 L100 122 L114 96Z', stroke_width=2.5)
     + s('path', d='M86 96 L96 132 M114 96 L104 132', stroke_width=2.5)
     + z('path', '#e04b5a', d='M100 108 L86 100 L86 116Z') + z('path', '#e04b5a', d='M100 108 L114 100 L114 116Z')
     + s('circle', '#e04b5a', cx=100, cy=108, r=4, stroke_width=2.5)
     + dot(100, 130, 2.5) + hand(140, 120) + hand(64, 132)
     + face(100, 58, SK, '#5a4033', 'smile'))
ITEMS['school-uniform'] = o


# 8. field-trip
def cap_kid(cx, cy, r, hair, cap, mouth):
    o = head(cx, cy, r, hair, mouth)
    o += z('path', cap, d=f'M{cx-r+1} {cy-5} Q{cx-r} {cy-r-6} {cx} {cy-r-6} Q{cx+r} {cy-r-6} {cx+r-1} {cy-5}Z')
    o += z('path', cap, d=f'M{cx-r-2} {cy-5} Q{cx} {cy-11} {cx+r+12} {cy-5} Q{cx} {cy+1} {cx-r-2} {cy-5}Z')
    return o


o = (z('rect', '#ffc94d', x=26, y=36, width=150, height=66, rx=12)
     + ''.join(z('rect', '#8fc7e8', x=x, y=46, width=24, height=22, rx=3) for x in (38, 70, 102, 134))
     + s('path', d='M26 80 L176 80', stroke_width=2.5)
     + z('circle', '#5b6b7a', cx=52, cy=102, r=11) + z('circle', '#5b6b7a', cx=150, cy=102, r=11))
for cx, hair, cap, shirt, bag, m in ((66, '#2b2220', '#e8735a', '#9ccf7a', '#8fb3e0', 'open'), (136, '#5a4033', '#8fb3e0', '#f6a6b8', '#e8735a', 'smile')):
    o += z('rect', bag, x=cx - 30, y=140, width=60, height=36, rx=10)
    o += body(cx, 136, 26, 182, shirt)
    o += s('path', d=f'M{cx-16} 140 L{cx-16} 178 M{cx+16} 140 L{cx+16} 178', stroke=bag, stroke_width=5)
    o += cap_kid(cx, 118, 24, hair, cap, m)
o += arm('M88 160 Q98 166 104 160', '#9ccf7a') + arm('M114 160 Q106 166 100 160', '#f6a6b8') + hand(101, 160, 6)
ITEMS['field-trip'] = o

# 9. library
o = z('rect', '#d9a66b', x=26, y=24, width=148, height=110, rx=4) + s('rect', '#9a6a3f', x=34, y=32, width=132, height=94, stroke_width=2.5)
cols = ['#e8735a', '#8fc7e8', '#9ccf7a', '#f5d58a', '#a98bd0', '#f6a6b8', '#7cc4b0', '#8fb3e0']
for bottom, hs in ((62, (24, 20, 26, 22, 18, 24, 26, 20, 22, 24, 20)), (94, (22, 26, 20, 24, 26, 18, 22, 26, 20, 24, 22)), (126, (26, 22, 24, 20, 26, 24, 22, 18, 26, 20, 24))):
    x = 36
    for i, h in enumerate(hs):
        w = 10 + (i * 3 + bottom) % 4
        if x + w > 164:
            break
        o += s('rect', cols[(i + bottom // 32) % len(cols)], x=x, y=bottom - min(h, 27), width=w, height=min(h, 27), stroke_width=2.5)
        x += w + 1
    o += s('path', d=f'M34 {bottom+1} L166 {bottom+1}', stroke_width=4)
o += (z('rect', '#8b6b4f', x=22, y=148, width=156, height=12, rx=3)
      + s('path', d='M34 160 L34 182 M166 160 L166 182', stroke_width=4)
      + z('path', '#ffffff', d='M62 148 Q78 134 98 142 L98 148Z') + z('path', '#ffffff', d='M98 148 L98 142 Q118 134 134 148Z')
      + s('path', d='M98 142 L98 148', stroke_width=2.5)
      + z('rect', '#e8735a', x=140, y=138, width=32, height=10, rx=2) + z('rect', '#8fc7e8', x=144, y=128, width=26, height=10, rx=2))
ITEMS['library'] = o


# 10. toy-blocks
def cube(x, y, sz, d, front, top, side):
    return (z('path', top, d=f'M{x} {y} L{x+d} {y-d} L{x+sz+d} {y-d} L{x+sz} {y}Z')
            + z('path', side, d=f'M{x+sz} {y} L{x+sz+d} {y-d} L{x+sz+d} {y+sz-d} L{x+sz} {y+sz}Z')
            + z('rect', front, x=x, y=y, width=sz, height=sz))


o = (cube(32, 126, 46, 12, '#e8735a', '#f5b971', '#e8735a') + s('circle', '#ffffff', cx=55, cy=149, r=12, stroke_width=2.5)
     + cube(90, 126, 46, 12, '#8fc7e8', '#c9d3db', '#8fb3e0') + star(113, 150, 15, '#ffe27a')
     + cube(62, 76, 46, 12, '#ffe27a', '#f5d58a', '#ffc94d') + heart(85, 98, 1.6, '#f07a8a')
     + z('path', '#9ccf7a', d='M146 172 L178 172 L162 138Z')
     + z('path', '#7cc4a0', d='M150 124 L170 124 L170 136 L150 136Z')
     + s('path', d='M24 172 L180 172', stroke_width=2.5))
o = o.replace(z('path', '#7cc4a0', d='M150 124 L170 124 L170 136 L150 136Z'), '')
ITEMS['toy-blocks'] = o

# 11. math-shapes
o = (z('circle', '#8fc7e8', cx=62, cy=66, r=34)
     + dot(52, 66) + dot(72, 66) + cheeks(44, 80, 76, 5, 3) + s('path', d='M57 76 Q62 81 67 76', stroke_width=2.5)
     + z('path', '#f5b971', d='M134 30 L176 104 L92 104Z')
     + dot(124, 80) + dot(144, 80) + cheeks(116, 152, 90, 5, 3) + s('path', d='M129 90 Q134 95 139 90', stroke_width=2.5)
     + z('rect', '#9ccf7a', x=64, y=114, width=64, height=64, rx=3)
     + dot(86, 144) + dot(106, 144) + cheeks(78, 114, 154, 5, 3) + s('path', '#c0504d', d='M90 154 Q96 166 102 154Z', stroke_width=2.5)
     + sparkle(28, 132, 7) + sparkle(162, 150, 8, '#f6a6b8') + sparkle(160, 124, 4, '#8fc7e8'))
ITEMS['math-shapes'] = o

# 12. science-experiment
FL = 'M90 54 L90 92 L50 164 Q46 176 60 176 L140 176 Q154 176 150 164 L110 92 L110 54Z'
o = (z('path', '#ffffff', d=FL)
     + s('path', '#9ccf7a', d='M68 126 Q84 120 100 126 Q116 132 132 126 L150 164 Q154 176 140 176 L60 176 Q46 176 50 164Z', stroke_width=2.5)
     + s('path', d=FL)
     + z('rect', '#c9d3db', x=84, y=46, width=32, height=10, rx=3)
     + s('circle', '#ffffff', cx=78, cy=164, r=4, stroke_width=2) + s('circle', '#ffffff', cx=122, cy=140, r=3, stroke_width=2)
     + s('circle', '#ffffff', cx=130, cy=160, r=5, stroke_width=2)
     + s('circle', '#9ccf7a', cx=96, cy=34, r=6, stroke_width=2.5) + s('circle', '#9ccf7a', cx=110, cy=24, r=4, stroke_width=2.5)
     + s('circle', '#9ccf7a', cx=86, cy=20, r=3.5, stroke_width=2.5)
     + dot(90, 148) + dot(110, 148) + cheeks(80, 120, 158, 6, 3.5) + s('path', '#c0504d', d='M94 156 Q100 168 106 156Z', stroke_width=2.5)
     + z('rect', '#f4f4f0', x=154, y=84, width=16, height=86, rx=8)
     + s('path', '#f6a6b8', d='M155.5 130 L168.5 130 L168.5 162 Q168.5 168.5 162 168.5 Q155.5 168.5 155.5 162Z', stroke_width=0)
     + s('rect', d='', x=154, y=84, width=16, height=86, rx=8)
     + s('rect', '#c9d3db', x=150, y=78, width=24, height=8, rx=3, stroke_width=2.5)
     + z('rect', '#f4f4f0', x=30, y=104, width=16, height=66, rx=8)
     + s('path', '#8fc7e8', d='M31.5 134 L44.5 134 L44.5 162 Q44.5 168.5 38 168.5 Q31.5 168.5 31.5 162Z', stroke_width=0)
     + s('rect', x=30, y=104, width=16, height=66, rx=8)
     + s('rect', '#c9d3db', x=26, y=98, width=24, height=8, rx=3, stroke_width=2.5))
o = o.replace(s('rect', d='', x=154, y=84, width=16, height=86, rx=8), s('rect', x=154, y=84, width=16, height=86, rx=8))
ITEMS['science-experiment'] = o

# 13. plant-observation
o = (body(70, 124, 34, 180, '#f5b971') + face(70, 80, SK, '#2b2220', 'o')
     + '<g transform="rotate(-8 84 148)">' + z('rect', '#ffffff', x=62, y=128, width=46, height=38, rx=3)
     + s('path', d='M70 140 L100 140 M70 148 L100 148 M70 156 L92 156', stroke='#8fc7e8', stroke_width=2.5)
     + s('path', d='M62 128 L62 166', stroke='#e8735a', stroke_width=4) + '</g>'
     + hand(60, 150) + hand(106, 146)
     + s('path', d='M152 140 Q148 118 154 98', stroke_width=3)
     + z('path', '#9ccf7a', d='M152 120 Q130 116 128 98 Q148 98 152 120Z')
     + z('path', '#7cc4a0', d='M154 104 Q160 82 178 82 Q176 102 154 104Z')
     + z('path', '#e8735a', d='M130 146 L174 146 L168 178 L136 178Z') + z('rect', '#e8735a', x=126, y=138, width=52, height=12, rx=3)
     + dot(145, 160, 3) + dot(159, 160, 3) + cheeks(139, 165, 167, 4, 2.5)
     + sparkle(116, 92, 6) + sparkle(178, 120, 4))
ITEMS['plant-observation'] = o

# 14. bug-catching
o = (s('path', d='M120 56 L104 180', stroke_width=10) + s('path', d='M120 56 L104 180', stroke='#d9a66b', stroke_width=4)
     + z('path', '#ffffff', d='M112 48 Q108 92 136 108 Q166 100 168 48Z')
     + s('path', d='M120 60 Q124 88 136 106 M136 52 L136 108 M152 58 Q150 88 136 106 M114 72 Q140 80 166 70 M120 90 Q138 96 158 88', stroke='#c9d3db', stroke_width=2)
     + s('path', d='M112 48 Q108 92 136 108 Q166 100 168 48')
     + s('ellipse', cx=140, cy=46, rx=28, ry=10, stroke_width=4)
     + s('path', d='M44 104 Q60 88 76 104', stroke_width=3)
     + z('rect', '#f4f4f0', x=30, y=116, width=60, height=58, rx=3)
     + z('ellipse', '#9a6a3f', cx=60, cy=152, rx=12, ry=15) + s('path', d='M60 138 L60 166 M48 146 L42 140 M72 146 L78 140 M48 158 L42 164 M72 158 L78 164 M56 138 L52 128 M64 138 L68 128', stroke_width=2.5)
     + ''.join(s('path', d=f'M{x} 118 L{x} 172', stroke='#7cc4b0', stroke_width=2.5) for x in (40, 50, 70, 80))
     + s('rect', x=30, y=116, width=60, height=58, rx=3)
     + z('rect', '#7cc4b0', x=26, y=104, width=68, height=14, rx=4)
     + z('path', '#f6a6b8', d='M158 146 Q136 120 142 114 Q154 110 160 140Z')
     + z('path', '#f6a6b8', d='M162 146 Q184 120 178 114 Q166 110 160 140Z')
     + z('path', '#ffe27a', d='M158 150 Q142 166 148 172 Q156 174 160 154Z') + z('path', '#ffe27a', d='M162 150 Q178 166 172 172 Q164 174 160 154Z')
     + z('ellipse', '#5b6b7a', cx=160, cy=146, rx=4, ry=14)
     + s('path', d='M158 133 Q154 124 150 120 M162 133 Q166 124 170 120', stroke_width=2))
ITEMS['bug-catching'] = o

# 15. world-map
o = (z('rect', '#8fc7e8', x=24, y=46, width=152, height=110, rx=4)
     + s('path', d='M74 46 L74 156 M126 46 L126 156', stroke='#ffffff', stroke_width=2)
     + s('path', '#9ccf7a', d='M34 64 Q48 52 70 58 Q78 66 66 78 Q60 90 52 96 Q44 86 40 78 Q30 74 34 64Z', stroke_width=2.5)
     + s('path', '#9ccf7a', d='M58 104 Q72 102 76 114 Q72 130 64 144 Q58 130 56 116Z', stroke_width=2.5)
     + s('path', '#9ccf7a', d='M94 60 Q106 54 114 62 Q108 72 98 72Z', stroke_width=2.5)
     + s('path', '#9ccf7a', d='M92 80 Q110 76 116 88 Q114 106 104 128 Q96 118 94 102 Q86 92 92 80Z', stroke_width=2.5)
     + s('path', '#9ccf7a', d='M118 58 Q144 50 164 60 Q168 74 154 84 Q146 96 136 90 Q124 84 120 72Z', stroke_width=2.5)
     + s('path', '#9ccf7a', d='M142 120 Q156 112 166 120 Q164 134 150 134 Q140 130 142 120Z', stroke_width=2.5)
     + s('path', '#ffffff', d='M70 30 L130 30 L130 46', stroke_width=0)
     + s('path', d='M100 30 L100 46', stroke_width=0)
     + s('path', d='M140 64 L140 54', stroke_width=3) + z('circle', '#e04b5a', cx=140, cy=50, r=7)
     + s('path', d='M86 156 L82 172 M114 156 L118 172', stroke='#ffffff', stroke_width=0))
o = o.replace(s('path', '#ffffff', d='M70 30 L130 30 L130 46', stroke_width=0), '').replace(s('path', d='M100 30 L100 46', stroke_width=0), '').replace(s('path', d='M86 156 L82 172 M114 156 L118 172', stroke='#ffffff', stroke_width=0), '')
o = (s('path', d='M70 46 L100 26 L130 46', stroke_width=2.5) + dot(100, 26, 4, '#e8735a') + o)
ITEMS['world-map'] = o


# 16. kindergarten-kids
def kinder(cx, cy, r, hair, mouth):
    o = head(cx, cy, r, hair, mouth)
    o += z('path', '#ffe27a', d=f'M{cx-r+2} {cy-6} Q{cx-r} {cy-r-8} {cx} {cy-r-8} Q{cx+r} {cy-r-8} {cx+r-2} {cy-6}Z')
    o += z('ellipse', '#ffe27a', cx=cx, cy=cy - 6, rx=r + 8, ry=5)
    return o


o = (z('rect', SK, x=52, y=154, width=9, height=14) + z('rect', SK, x=66, y=154, width=9, height=14)
     + z('ellipse', '#e8735a', cx=56, cy=172, rx=8, ry=4) + z('ellipse', '#e8735a', cx=72, cy=172, rx=8, ry=4)
     + arm('M50 128 Q34 112 32 94', '#8fc7e8') + hand(32, 90)
     + body(64, 112, 26, 158, '#8fc7e8') + kinder(64, 86, 24, '#2b2220', 'open')
     + z('rect', SK, x=128, y=150, width=9, height=18) + z('rect', SK, x=144, y=150, width=9, height=18)
     + z('ellipse', '#8fb3e0', cx=132, cy=172, rx=8, ry=4) + z('ellipse', '#8fb3e0', cx=150, cy=172, rx=8, ry=4)
     + body(140, 110, 26, 156, '#8fc7e8') + kinder(140, 84, 24, '#5a4033', 'smile')
     + arm('M118 132 Q108 138 102 132', '#8fc7e8') + hand(100, 130)
     + arm('M160 128 Q172 120 176 108', '#8fc7e8') + hand(176, 104)
     + z('circle', '#e8735a', cx=96, cy=160, r=15)
     + s('path', d='M82 156 Q96 150 110 156 M84 166 Q96 172 108 166', stroke='#ffffff', stroke_width=3)
     + s('path', d='M24 176 L180 176', stroke_width=2.5))
ITEMS['kindergarten-kids'] = o

# 17. kindergarten-hat
o = (s('path', d='M110 120 Q118 50 176 34', stroke_width=7) + s('path', d='M110 120 Q118 50 176 34', stroke='#8fc7e8', stroke_width=2)
     + z('path', '#8fc7e8', d='M98 118 L172 118 L172 158 Q172 176 154 176 L116 176 Q98 176 98 158Z')
     + z('path', '#8fb3e0', d='M96 116 L174 116 L174 132 Q135 156 96 132Z')
     + z('circle', '#ffe27a', cx=135, cy=144, r=6)
     + heart(118, 160, 1.0, '#f6a6b8')
     + s('path', d='M40 94 Q74 140 128 96', stroke_width=2)
     + z('ellipse', '#ffe27a', cx=84, cy=88, rx=58, ry=15)
     + z('path', '#ffe27a', d='M44 88 Q44 38 84 36 Q124 38 124 88 Q84 96 44 88Z')
     + s('path', d='M46 76 Q84 84 122 76', stroke='#ffc94d', stroke_width=5)
     + s('path', d='M46 76 Q84 84 122 76', stroke_width=0))
o = o.replace(s('path', d='M46 76 Q84 84 122 76', stroke_width=0), '')
ITEMS['kindergarten-hat'] = o

# 18. university-campus
o = (z('rect', '#f6e0c4', x=42, y=82, width=116, height=66)
     + z('rect', '#8b6b4f', x=88, y=108, width=24, height=40, rx=2)
     + ''.join(z('rect', '#ffffff', x=x, y=84, width=12, height=62) for x in (46, 66, 122, 142))
     + z('rect', '#f4f4f0', x=32, y=70, width=136, height=14, rx=2)
     + z('path', '#f4f4f0', d='M32 70 L100 32 L168 70Z')
     + s('circle', '#8fc7e8', cx=100, cy=56, r=8, stroke_width=2.5)
     + z('rect', '#c9d3db', x=36, y=146, width=128, height=12)
     + z('rect', '#c9d3db', x=28, y=158, width=144, height=14)
     + s('path', d='M100 30 L100 18', stroke_width=0))
o = o.replace(s('path', d='M100 30 L100 18', stroke_width=0), '')
o = (z('circle', '#9ccf7a', cx=36, cy=110, r=14) + z('circle', '#9ccf7a', cx=166, cy=110, r=14)) + o
o = (s('path', d='M36 124 L36 146 M166 124 L166 146', stroke='#8b6b4f', stroke_width=5)) + o
ITEMS['university-campus'] = o

# 19. lecture-hall
o = (z('rect', '#ffffff', x=46, y=24, width=108, height=50, rx=3)
     + s('path', d='M60 64 L60 52 M60 64 L72 64', stroke_width=2)
     + s('rect', '#8fc7e8', x=62, y=48, width=8, height=16, stroke_width=2) + s('rect', '#9ccf7a', x=74, y=40, width=8, height=24, stroke_width=2)
     + s('rect', '#f5b971', x=86, y=52, width=8, height=12, stroke_width=2)
     + s('path', d='M106 42 L140 42 M106 52 L136 52 M106 62 L128 62', stroke='#c9d3db', stroke_width=3)
     + body(166, 92, 13, 112, '#7cc4b0') + head(166, 80, 12, '#5a4033', 'open')
     + arm('M156 100 Q146 90 146 78', '#7cc4b0') + hand(146, 74, 5)
     + z('rect', '#8b6b4f', x=152, y=102, width=26, height=16, rx=2))
hairs = ['#2b2220', '#5a4033', '#c9a36b', '#e8e1d8', '#5a4033']
for y, r, xs, row in ((126, 10, (44, 72, 100, 128, 156), 'M24 134 Q100 118 178 134 L178 144 Q100 128 24 144Z'),
                      (160, 13, (42, 82, 122, 160), 'M22 168 Q100 152 178 168 L178 180 Q100 164 22 180Z')):
    for i, x in enumerate(xs):
        dy = abs(x - 100) * 0.2
        o += z('circle', hairs[(i + r) % len(hairs)], cx=x, cy=_n(y - 12 + dy), r=r)
    o += z('path', '#e8735a', d=row)
ITEMS['lecture-hall'] = o

# 20. online-class
o = (z('rect', '#5b6b7a', x=34, y=30, width=132, height=96, rx=8)
     + s('rect', '#d8eef8', x=42, y=38, width=116, height=80, rx=3, stroke_width=2.5)
     + s('path', '#f5b971', d='M56 118 Q58 96 82 94 Q106 96 108 118Z', stroke_width=2.5)
     + head(82, 74, 20, '#5a4033', 'open')
     + arm('M102 108 Q110 98 108 84', '#f5b971') + hand(108, 80, 5)
     + s('rect', '#f6e0c4', x=120, y=44, width=32, height=22, rx=2, stroke_width=2)
     + s('rect', '#f6e0c4', x=120, y=70, width=32, height=22, rx=2, stroke_width=2)
     + s('rect', '#f6e0c4', x=120, y=96, width=32, height=20, rx=2, stroke_width=2)
     + s('circle', SK, cx=136, cy=57, r=6, stroke_width=2) + s('path', '#2b2220', d='M130 55 Q136 46 142 55Z', stroke_width=1.5)
     + s('circle', SK, cx=136, cy=83, r=6, stroke_width=2) + s('path', '#c9a36b', d='M130 81 Q136 72 142 81Z', stroke_width=1.5)
     + s('circle', SK, cx=136, cy=109, r=6, stroke_width=2) + s('path', '#5b6b7a', d='M130 107 Q136 98 142 107Z', stroke_width=1.5)
     + z('path', '#c9d3db', d='M34 126 L166 126 L180 146 L22 146Z')
     + s('path', d='M86 136 L114 136', stroke_width=2.5)
     + z('rect', '#8fb3e0', x=32, y=156, width=44, height=22, rx=3) + s('path', d='M54 156 L54 178', stroke_width=2)
     + '<g transform="rotate(-25 130 166)">' + z('rect', '#ffc94d', x=112, y=162, width=40, height=8, rx=1)
     + s('path', '#f6e0c4', d='M112 162 L104 166 L112 170Z', stroke_width=2) + '</g>'
     + sparkle(28, 40, 5, '#8fc7e8') + sparkle(176, 62, 5))
ITEMS['online-class'] = o
