from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

def mini_face(cx, cy, gap=12, ch=20, r=3.5):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+10, 6, 3.5)
            + s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5))

def stick(d, color, w=7):
    return s('path', d=d, stroke_width=w+3) + s('path', d=d, stroke=color, stroke_width=w-3)

# 1 rice ball
ITEMS['rice-ball'] = (
    z('path', '#ffffff', d='M100 36 Q114 36 150 116 Q166 160 132 164 L68 164 Q34 160 50 116 Q86 36 100 36Z')
    + z('rect', '#5b6b7a', x=76, y=128, width=48, height=40, rx=4)
    + mini_face(100, 100, 14, 26))

# 2 hamburger
ITEMS['hamburger'] = (
    z('rect', '#f5b971', x=46, y=144, width=108, height=28, rx=12)
    + z('rect', '#8b6b4f', x=40, y=124, width=120, height=22, rx=10)
    + z('path', '#ffe27a', d='M42 116 L158 116 L156 128 L140 126 L126 140 L114 126 L74 126 L62 140 L50 126 L42 128Z')
    + z('path', '#9ccf7a', d='M38 108 Q46 124 58 114 Q68 126 80 114 Q90 126 100 114 Q110 126 120 114 Q132 126 142 114 Q154 124 162 108Z')
    + z('path', '#f5b971', d='M42 110 Q44 50 100 48 Q156 50 158 110Z')
    + ''.join(s('ellipse', '#ffffff', cx=x, cy=y, rx=4, ry=2.5, stroke_width=1.5) for x, y in ((76,74),(100,64),(124,74),(88,90),(114,88),(64,94),(138,94)))
)

# 3 pizza slice
ITEMS['pizza-slice'] = (
    z('path', '#ffe27a', d='M50 50 L150 50 L104 170 Q100 176 96 170Z')
    + s('circle', '#e04b5a', cx=80, cy=76, r=10, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=120, cy=80, r=10, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=100, cy=112, r=9, stroke_width=2.5)
    + s('circle', '#e04b5a', cx=99, cy=146, r=7, stroke_width=2.5)
    + z('rect', '#d9a66b', x=40, y=36, width=120, height=22, rx=11)
)

# 4 sushi
def nigiri(cx, fish, stripe):
    o = z('ellipse', '#ffffff', cx=cx, cy=128, rx=28, ry=17)
    o += z('path', fish, d=f'M{cx-34} 122 Q{cx-34} 96 {cx} 98 Q{cx+34} 96 {cx+34} 120 Q{cx} 130 {cx-34} 122Z')
    if stripe:
        o += ''.join(s('path', d=f'M{cx+dx} 101 Q{cx+dx+6} 112 {cx+dx+2} 124', stroke='#ffffff', stroke_width=3) for dx in (-18, -4, 10))
    return o
ITEMS['sushi'] = (
    z('ellipse', '#8fb3e0', cx=100, cy=148, rx=80, ry=28)
    + s('ellipse', 'none', cx=100, cy=146, rx=62, ry=18, stroke_width=2)
    + nigiri(64, '#f5b971', True) + nigiri(136, '#e04b5a', False)
)

# 5 apple
ITEMS['apple'] = (
    s('path', d='M100 70 Q100 50 108 38', stroke_width=5)
    + z('path', '#e04b5a', d='M100 70 Q80 54 62 62 Q36 76 42 116 Q50 162 82 170 Q92 174 100 168 Q108 174 118 170 Q150 162 158 116 Q164 76 138 62 Q120 54 100 70Z')
    + z('path', '#9ccf7a', d='M106 52 Q120 30 146 36 Q132 60 106 52Z')
    + s('path', d='M66 84 Q60 94 60 106', stroke='#ffffff', stroke_width=4)
    + mini_face(100, 116, 14, 26))

# 6 banana bunch
BN = 'M60 58 Q66 156 166 116 Q170 108 162 104 Q150 112 132 114 Q84 118 78 56Z'
ITEMS['banana'] = '<g transform="translate(4 24)">' + (
    ''.join(z('path', '#ffe27a', d=BN, transform=f'rotate({r} 66 56)') for r in (-26, -13, 0, 13))
    + ''.join(s('path', '#8b6b4f', d='M162 104 Q168 108 166 116', transform=f'rotate({r} 66 56)', stroke_width=2.5) for r in (-26, -13, 0, 13))
    + z('rect', '#9ccf7a', x=56, y=32, width=20, height=30, rx=5, transform='rotate(-20 66 46)')
) + '</g>'

# 7 coffee cup
ITEMS['coffee-cup'] = (
    s('path', d='M80 70 Q70 58 80 48 Q90 38 80 26', stroke_width=3)
    + s('path', d='M102 72 Q92 58 102 48 Q112 38 102 26', stroke_width=3)
    + s('path', d='M124 70 Q114 58 124 48 Q134 38 124 26', stroke_width=3)
    + z('ellipse', '#f4f4f0', cx=100, cy=166, rx=72, ry=14)
    + stick('M138 104 Q172 100 168 124 Q164 144 134 140', '#8fc7e8', 11)
    + z('path', '#8fc7e8', d='M50 88 L150 88 Q150 162 100 162 Q50 162 50 88Z')
    + s('ellipse', '#8b6b4f', cx=100, cy=88, rx=50, ry=10)
    + mini_face(100, 120, 14, 26))

# 8 ice cream
ITEMS['ice-cream'] = (
    z('path', '#d9a66b', d='M68 110 L132 110 L102 182 Q100 186 98 182Z')
    + s('path', d='M78 122 L114 158 M92 116 L122 140 M122 120 L88 156 M108 116 L80 140', stroke_width=2)
    + z('path', '#7cc4b0', d='M70 76 Q66 34 100 32 Q134 34 130 76 Q100 86 70 76Z')
    + z('path', '#f6a6b8', d='M64 112 Q60 72 100 70 Q140 72 136 112 Q128 124 118 112 Q110 126 100 114 Q90 126 82 112 Q72 124 64 112Z')
    + dot(100, 30, 9, '#e04b5a') + s('circle', 'none', cx=100, cy=30, r=9)
    + s('path', d='M100 21 Q102 12 110 10', stroke_width=2.5)
    + mini_face(100, 94, 13, 24))

# 9 bread
ITEMS['bread'] = (
    z('path', '#f5b971', d='M30 132 Q30 72 100 70 Q170 72 170 132 Q170 160 144 160 L56 160 Q30 160 30 132Z')
    + s('path', d='M58 98 Q66 84 80 80', stroke='#f6e0c4', stroke_width=6)
    + s('path', d='M86 92 Q96 78 112 76', stroke='#f6e0c4', stroke_width=6)
    + s('path', d='M120 92 Q130 82 144 84', stroke='#f6e0c4', stroke_width=6)
    + mini_face(100, 124, 14, 26)
    + s('path', d='M24 172 L176 172', stroke_width=2.5))

# 10 noodle bowl
ITEMS['noodle-bowl'] = (
    s('path', d='M84 76 Q76 64 84 54 Q92 44 84 34', stroke_width=3)
    + s('path', d='M104 72 Q96 60 104 50 Q112 40 104 30', stroke_width=3)
    + z('rect', '#5b6b7a', x=42, y=60, width=24, height=36, rx=2, transform='rotate(-14 54 80)')
    + z('path', '#e8735a', d='M30 100 L170 100 Q166 170 100 172 Q34 170 30 100Z')
    + s('path', d='M42 132 Q100 148 158 132', stroke='#ffffff', stroke_width=4)
    + s('ellipse', '#f5d58a', cx=100, cy=100, rx=70, ry=16)
    + s('path', d='M48 104 Q56 96 64 104 Q72 112 80 104 M96 108 Q104 100 112 108 Q120 116 128 108 M136 104 Q144 96 152 104', stroke_width=2.5)
    + z('ellipse', '#ffffff', cx=76, cy=96, rx=16, ry=10)
    + s('circle', '#ffc94d', cx=76, cy=96, r=5.5, stroke_width=2)
    + z('ellipse', '#d9a66b', cx=114, cy=94, rx=14, ry=8)
    + s('circle', '#9ccf7a', cx=96, cy=92, r=3, stroke_width=1.5) + s('circle', '#9ccf7a', cx=134, cy=100, r=3, stroke_width=1.5)
    + s('circle', '#9ccf7a', cx=60, cy=102, r=3, stroke_width=1.5)
    + stick('M92 100 L162 32', '#d9a66b', 7) + stick('M104 102 L172 42', '#d9a66b', 7)
)
