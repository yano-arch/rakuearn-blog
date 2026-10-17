from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

def arm(d, col, w=9):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 5)

def head(cx, cy, skin, hair):
    o = z('circle', skin, cx=cx, cy=cy, r=34)
    o += s('path', hair, d=f'M{cx-34} {cy-2} Q{cx-32} {cy-36} {cx} {cy-35} Q{cx+32} {cy-36} {cx+34} {cy-2} Q{cx+20} {cy-18} {cx} {cy-17} Q{cx-20} {cy-18} {cx-34} {cy-2}Z')
    return o

def body(cx, top, bottom, col, hw=34):
    return z('path', col, d=f'M{cx-hw} {bottom} Q{cx-hw+2} {top+2} {cx} {top} Q{cx+hw-2} {top+2} {cx+hw} {bottom}Z')

def drop(x, y, k=1.0, col='#8fc7e8'):
    return z('path', col, d=f'M{x} {y} Q{x-6*k} {y+10*k} {x} {y+14*k} Q{x+6*k} {y+10*k} {x} {y}Z', stroke_width=2.5)

# 1. jumping with joy
ITEMS['person-jumping-joy'] = (
    arm('M80 122 Q60 100 48 62', '#f5b971') + arm('M120 122 Q140 100 152 62', '#f5b971')
    + z('circle', '#ffd9b8', cx=46, cy=56, r=9) + z('circle', '#ffd9b8', cx=154, cy=56, r=9)
    + arm('M88 146 Q80 160 72 170', '#5b6b7a') + arm('M112 146 Q120 160 128 170', '#5b6b7a')
    + z('ellipse', '#8b6b4f', cx=68, cy=172, rx=9, ry=6) + z('ellipse', '#8b6b4f', cx=132, cy=172, rx=9, ry=6)
    + body(100, 112, 152, '#f5b971', 30)
    + face(100, 76, '#ffd9b8', '#5a4033', 'open')
    + s('path', d='M74 188 Q100 182 126 188', stroke_width=2.5)
    + s('path', d='M28 30 L28 40 M23 35 L33 35 M172 30 L172 40 M167 35 L177 35', stroke_width=2.5))

# 2. thinking
ITEMS['person-thinking'] = (
    body(88, 136, 186, '#8fc7e8')
    + head(88, 92, '#ffd9b8', '#2b2220')
    + dot(76, 94) + dot(100, 94) + cheeks(68, 108, 105)
    + s('path', d='M74 112 L84 110')
    + s('path', d='M70 80 L80 78 M96 76 L106 80', stroke_width=2.5)
    + arm('M104 178 Q124 156 108 132', '#8fc7e8')
    + z('circle', '#ffd9b8', cx=106, cy=126, r=10)
    + s('path', d='M140 40 Q140 22 155 22 Q170 22 170 36 Q170 46 158 52 L158 62', stroke_width=12)
    + s('path', d='M140 40 Q140 22 155 22 Q170 22 170 36 Q170 46 158 52 L158 62', stroke='#f5b971', stroke_width=6)
    + z('circle', '#f5b971', cx=158, cy=78, r=6))

# 3. crying
ITEMS['person-crying'] = (
    body(100, 136, 186, '#f6a6b8')
    + head(100, 92, '#ffd9b8', '#c9a36b')
    + s('path', d='M80 86 L93 82 M107 82 L120 86', stroke_width=2.5)
    + s('path', d='M83 95 Q88 91 93 95 M107 95 Q112 91 117 95', stroke_width=2.5)
    + cheeks(80, 120, 106)
    + s('path', d='M92 116 Q100 109 108 116')
    + drop(84, 100, 1.1) + drop(116, 100, 1.1)
    + drop(54, 120, 1.0) + drop(146, 120, 1.0) + drop(40, 146, 0.8) + drop(160, 146, 0.8))

# 4. angry
ITEMS['person-angry'] = (
    z('path', '#f4f4f0', d='M46 40 Q36 40 38 30 Q36 18 50 20 Q56 10 66 18 Q78 18 74 30 Q76 40 64 40Z') + s('path', d='M72 62 Q64 56 70 50 Q76 44 68 40', stroke_width=2.5)
    + z('path', '#f4f4f0', d='M136 40 Q126 40 128 30 Q126 18 140 20 Q146 10 156 18 Q168 18 164 30 Q166 40 154 40Z') + s('path', d='M128 62 Q136 56 130 50 Q124 44 132 40', stroke_width=2.5)
    + arm('M72 150 Q56 160 50 146', '#9ccf7a') + arm('M128 150 Q144 160 150 146', '#9ccf7a')
    + body(100, 136, 186, '#9ccf7a')
    + z('circle', '#ffd9b8', cx=48, cy=142, r=9) + z('circle', '#ffd9b8', cx=152, cy=142, r=9)
    + head(100, 94, '#ffd9b8', '#5a4033')
    + s('path', d='M78 84 L94 90 M122 84 L106 90', stroke_width=3)
    + dot(88, 98) + dot(112, 98)
    + f'<ellipse cx="78" cy="108" rx="9" ry="5" fill="#f07a8a" stroke="none"/><ellipse cx="122" cy="108" rx="9" ry="5" fill="#f07a8a" stroke="none"/>'
    + s('path', d='M92 116 Q100 110 108 116'))

# 5. surprised
ITEMS['person-surprised'] = (
    body(100, 136, 186, '#f5d58a')
    + arm('M78 150 Q60 140 58 118', '#f5d58a') + arm('M122 150 Q140 140 142 118', '#f5d58a')
    + face(100, 92, '#ffd9b8', '#2b2220', 'o')
    + z('circle', '#ffd9b8', cx=58, cy=112, r=9) + z('circle', '#ffd9b8', cx=142, cy=112, r=9)
    + s('path', d='M100 46 L100 34 M72 52 L64 42 M128 52 L136 42 M56 70 L44 64 M144 70 L156 64', stroke_width=3))

# 6. thumbs up
ITEMS['person-thumbs-up'] = (
    body(92, 136, 186, '#e8735a')
    + arm('M116 160 Q140 150 146 116', '#e8735a')
    + face(92, 92, '#ffd9b8', '#2b2220', 'smile')
    + z('rect', '#ffd9b8', x=138, y=82, width=11, height=26, rx=5.5)
    + z('rect', '#ffd9b8', x=136, y=102, width=26, height=24, rx=9)
    + s('path', d='M149 110 L160 110 M149 118 L160 118', stroke_width=2)
    + s('path', d='M168 70 L168 80 M163 75 L173 75 M174 96 L182 92', stroke_width=2.5))

# 7. sleeping under a blanket
ITEMS['person-sleeping'] = (
    z('ellipse', '#f4f4f0', cx=96, cy=78, rx=58, ry=24)
    + head(96, 80, '#ffd9b8', '#c9a36b')
    + s('path', d='M80 84 Q86 89 92 84 M100 84 Q106 89 112 84', stroke_width=2.5)
    + cheeks(76, 116, 94, 6, 3.5)
    + s('path', d='M92 100 Q96 103 100 100', stroke_width=2.5)
    + z('path', '#8fb3e0', d='M40 182 L40 116 Q40 108 50 108 L144 108 Q154 108 154 116 L154 182Z')
    + s('path', '#ffffff', d='M40 120 L154 120 L154 116 Q154 108 144 108 L50 108 Q40 108 40 116Z', stroke_width=3)
    + dot(70, 146, 4, '#ffffff') + dot(100, 160, 4, '#ffffff') + dot(128, 140, 4, '#ffffff') + dot(84, 172, 4, '#ffffff') + dot(134, 170, 4, '#ffffff')
    + s('path', d='M140 52 L152 52 L140 64 L152 64', stroke_width=2.5)
    + s('path', d='M158 30 L174 30 L158 46 L174 46', stroke_width=3))

# 8. bowing politely
ITEMS['person-bowing-thanks'] = (
    z('rect', '#5b6b7a', x=118, y=128, width=24, height=50, rx=6)
    + z('ellipse', '#8b6b4f', cx=126, cy=180, rx=16, ry=6)
    + z('ellipse', '#7cc4b0', cx=112, cy=116, rx=40, ry=26, transform='rotate(35 112 116)')
    + arm('M92 104 Q92 124 98 140', '#7cc4b0')
    + z('circle', '#ffd9b8', cx=98, cy=146, r=8)
    + z('circle', '#ffd9b8', cx=64, cy=98, r=30)
    + s('path', '#2b2220', d='M80 124 A30 30 0 1 0 38 83 Q52 104 80 124Z')
    + s('path', d='M48 108 Q53 113 58 108', stroke_width=2.5)
    + f'<ellipse cx="60" cy="119" rx="6" ry="3.5" fill="{CH}" stroke="none"/>'
    + s('path', d='M148 70 Q160 80 160 96 M162 60 Q178 76 176 100', stroke_width=2.5))

# 9. smiling grandma
ITEMS['grandma-smiling'] = (
    body(100, 136, 186, '#b9a99c')
    + s('path', '#f4f4f0', d='M92 138 L100 152 L108 138Z', stroke_width=2.5)
    + dot(100, 162, 3.5) + dot(100, 176, 3.5)
    + z('circle', '#e8e1d8', cx=100, cy=52, r=15)
    + head(100, 92, '#ffd9b8', '#e8e1d8')
    + s('path', d='M83 94 Q88 99 93 94 M107 94 Q112 99 117 94', stroke_width=2.5)
    + s('circle', cx=88, cy=95, r=10, stroke_width=2.5) + s('circle', cx=112, cy=95, r=10, stroke_width=2.5)
    + s('path', d='M98 94 Q100 91 102 94', stroke_width=2.5)
    + cheeks(76, 124, 108, 6, 3.5)
    + s('path', d='M94 110 Q100 116 106 110'))

# 10. baby crawling
ITEMS['baby-crawling'] = (
    s('path', d='M28 182 L176 182', stroke_width=2.5)
    + z('rect', '#8fc7e8', x=86, y=140, width=18, height=40, rx=9)
    + z('ellipse', '#8fc7e8', cx=146, cy=166, rx=24, ry=14)
    + z('ellipse', '#8fc7e8', cx=118, cy=136, rx=46, ry=28)
    + z('ellipse', '#ffd9b8', cx=168, cy=176, rx=9, ry=6)
    + z('ellipse', '#ffd9b8', cx=94, cy=178, rx=10, ry=6)
    + z('circle', '#ffd9b8', cx=64, cy=104, r=34)
    + s('path', d='M58 72 Q56 58 66 56 Q74 58 68 64 Q64 66 64 62', stroke_width=3)
    + dot(52, 106) + dot(76, 106) + cheeks(44, 84, 117)
    + s('path', d='M58 120 Q64 125 70 120'))
