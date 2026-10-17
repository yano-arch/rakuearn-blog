from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def mf(cx, cy, gap=12, ch=20, r=3.5, crx=6, cry=3.5):
    return (dot(cx-gap, cy, r)+dot(cx+gap, cy, r)+cheeks(cx-ch, cx+ch, cy+9, crx, cry)
            + s('path', d=f'M{cx-5} {cy+8} Q{cx} {cy+13} {cx+5} {cy+8}', stroke_width=2.5))


def stick(d, color, w=7):
    return s('path', d=d, stroke_width=w+3) + s('path', d=d, stroke=color, stroke_width=w-3)


def scallop(cx, cy, r, n, bump, start=0.0):
    pts = []
    for i in range(n + 1):
        a = start + 2*math.pi*i/n
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(n):
        a = start + 2*math.pi*(i+0.5)/n
        qx, qy = cx + (r+bump)*math.cos(a), cy + (r+bump)*math.sin(a)
        d += f' Q{qx:.1f} {qy:.1f} {pts[i+1][0]:.1f} {pts[i+1][1]:.1f}'
    return d + 'Z'


# 1 potato
ITEMS['potato'] = (
    z('path', '#d9a66b', d='M36 112 Q32 60 96 54 Q162 48 166 104 Q170 160 106 164 Q40 168 36 112Z')
    + ''.join(s('path', d=f'M{x-4} {y} Q{x} {y+3} {x+4} {y}', stroke='#9a6a3f', stroke_width=2.5)
              for x, y in ((62, 86), (138, 80), (58, 132), (146, 136), (100, 148)))
    + mf(102, 104, 14, 26))

# 2 eggplant
ITEMS['eggplant'] = (
    z('path', '#7a5ea8', d='M84 66 Q56 92 56 134 Q56 178 100 178 Q144 178 144 134 Q144 92 116 66Z')
    + s('path', d='M74 112 Q68 132 76 152', stroke='#c9d3db', stroke_width=5)
    + stick('M100 56 Q100 40 108 30', '#7cc4a0', 8)
    + z('path', '#7cc4a0', d='M66 76 Q80 54 100 54 Q120 54 134 76 Q120 70 114 88 Q106 72 100 90 Q94 72 86 88 Q80 70 66 76Z'))

# 3 cucumber
ITEMS['cucumber'] = (
    z('rect', '#7cc4a0', x=30, y=82, width=140, height=36, rx=18, transform='rotate(-32 100 100)')
    + ''.join(s('path', d=f'M{x} {y} l3 -3', stroke_width=2.5) for x, y in ((62, 122), (84, 114), (108, 98), (130, 86), (78, 132), (104, 120), (126, 104)))
    + z('path', '#ffe27a', d='M160 54 Q170 40 178 48 Q176 58 166 60Z')
    + z('circle', '#7cc4a0', cx=58, cy=62, r=26)
    + s('circle', '#9ccf7a', cx=58, cy=62, r=19, stroke_width=2)
    + ''.join(s('ellipse', '#f4f4f0', cx=58+9*math.cos(a), cy=62+9*math.sin(a), rx=2.5, ry=2.5, stroke_width=1.5)
              for a in [i*math.pi/3 for i in range(6)]))

# 4 corn
ITEMS['corn'] = (
    z('ellipse', '#ffe27a', cx=100, cy=94, rx=32, ry=64)
    + ''.join(s('circle', '#ffc94d', cx=100+dx, cy=y, r=5.5, stroke_width=1.5)
              for y in range(46, 150, 13) for dx in ((-17, 0, 17) if 50 < y < 140 else (-8, 8)))
    + z('path', '#9ccf7a', d='M100 182 Q50 168 54 100 Q74 124 98 150Z')
    + z('path', '#7cc4a0', d='M100 182 Q150 168 146 100 Q126 124 102 150Z')
    + s('path', d='M100 180 L100 168', stroke_width=6))

# 5 green pepper
ITEMS['green-pepper'] = (
    z('path', '#9ccf7a', d='M100 66 Q60 52 48 86 Q40 132 64 166 Q82 182 100 168 Q118 182 136 166 Q160 132 152 86 Q140 52 100 66Z')
    + s('path', d='M100 74 Q94 120 100 166', stroke_width=2.5)
    + s('path', d='M66 92 Q60 116 66 140', stroke='#ffffff', stroke_width=5)
    + stick('M100 64 Q100 44 114 34', '#7cc4b0', 9)
    + z('path', '#7cc4b0', d='M80 70 Q100 52 120 70 Q100 80 80 70Z'))

# 6 mushroom
ITEMS['mushroom'] = (
    z('path', '#f6e0c4', d='M74 108 Q68 160 78 176 L122 176 Q132 160 126 108Z')
    + z('path', '#e8735a', d='M28 112 Q30 40 100 36 Q170 40 172 112 Q100 126 28 112Z')
    + s('circle', '#ffffff', cx=70, cy=72, r=11, stroke_width=2)
    + s('circle', '#ffffff', cx=118, cy=56, r=9, stroke_width=2)
    + s('circle', '#ffffff', cx=140, cy=92, r=8, stroke_width=2)
    + s('circle', '#ffffff', cx=98, cy=96, r=7, stroke_width=2)
    + s('circle', '#ffffff', cx=50, cy=100, r=5, stroke_width=2)
    + mf(100, 140, 10, 16, 3.2, 5, 3))

# 7 garlic
ITEMS['garlic'] = (
    z('path', '#f4f4f0', d='M100 34 Q98 66 70 82 Q34 104 42 142 Q52 178 100 178 Q148 178 158 142 Q166 104 130 82 Q102 66 100 34Z')
    + s('path', d='M86 72 Q60 110 74 172 M114 72 Q140 110 126 172', stroke_width=2.5)
    + s('path', d='M92 176 L88 186 M100 178 L100 188 M108 176 L112 186', stroke_width=2.5)
    + mf(100, 128, 12, 18, 3.2, 5, 3))

# 8 daikon radish
ITEMS['daikon-radish'] = (
    z('path', '#9ccf7a', d='M98 72 Q66 50 64 22 Q90 30 100 70Z')
    + z('path', '#7cc4a0', d='M102 72 Q134 50 138 24 Q110 32 100 70Z')
    + z('path', '#9ccf7a', d='M100 72 Q86 40 100 18 Q114 40 100 72Z')
    + z('path', '#ffffff', d='M70 74 Q66 132 94 178 Q100 186 106 178 Q134 132 130 74 Q100 64 70 74Z')
    + s('path', '#9ccf7a', d='M72 76 Q100 68 128 76 L128 88 Q100 82 72 88Z', stroke='none')
    + s('path', d='M82 140 L88 140 M114 152 L120 152', stroke_width=2)
    + mf(100, 108, 11, 17, 3.2, 5, 3))

# 9 lettuce
ITEMS['lettuce'] = (
    z('path', '#7cc4a0', d=scallop(100, 104, 64, 11, 14, -math.pi/2))
    + z('path', '#9ccf7a', d=scallop(100, 110, 36, 7, 9, -math.pi/2))
    + s('path', d='M100 168 L100 146 M100 146 Q76 130 68 104 M100 146 Q124 130 132 104', stroke_width=2.5)
    + s('path', d='M56 70 Q72 84 76 112 M144 70 Q128 84 124 112', stroke_width=2.5))

# 10 sweet potato
ITEMS['sweet-potato'] = '<g transform="rotate(-12 100 108)">' + (
    s('path', d='M26 112 L18 116 M176 98 L184 93', stroke_width=3)
    + z('path', '#f07a8a', d='M24 112 Q56 52 120 56 Q170 60 178 100 Q164 146 112 152 Q50 160 24 112Z')
    + s('path', d='M58 82 Q52 98 58 114 M152 78 Q158 96 150 116', stroke_width=2.5)
    + mf(108, 104, 14, 26)) + '</g>'

# 11 pea pod
ITEMS['pea-pod'] = (
    s('path', d='M24 94 Q12 86 18 74 Q24 66 32 72', stroke_width=3)
    + z('path', '#7cc4b0', d='M24 94 Q100 58 178 90 Q160 116 100 118 Q40 116 24 94Z')
    + ''.join(z('circle', '#9ccf7a', cx=x, cy=100, r=16) + dot(x-5, 100, 2.4) + dot(x+5, 100, 2.4)
              + cheeks(x-9, x+9, 106, 3.5, 2.2) for x in (56, 89, 122, 153 - 2))
    + z('path', '#7cc4a0', d='M22 94 Q38 152 100 154 Q162 152 180 88 Q154 122 100 122 Q46 122 22 94Z'))

# 12 curry rice
ITEMS['curry-rice'] = (
    stick('M140 92 L176 44', '#c9d3db', 8)
    + z('ellipse', '#8fc7e8', cx=100, cy=128, rx=80, ry=44)
    + s('ellipse', 'none', cx=100, cy=126, rx=64, ry=32, stroke_width=2)
    + z('path', '#d9a66b', d='M92 104 Q130 90 160 106 Q178 128 160 148 Q130 162 92 154 Q82 128 92 104Z')
    + z('path', '#ffffff', d='M38 124 Q40 88 84 86 Q114 88 112 120 Q106 150 64 150 Q38 146 38 124Z')
    + s('rect', '#e8735a', x=118, y=110, width=12, height=10, rx=2, stroke_width=2)
    + s('rect', '#ffe27a', x=140, y=124, width=13, height=11, rx=2, stroke_width=2)
    + s('rect', '#ffe27a', x=112, y=136, width=11, height=10, rx=2, stroke_width=2)
    + s('rect', '#e8735a', x=140, y=106, width=9, height=8, rx=2, stroke_width=2)
    + s('path', d='M58 108 l4 2 M74 100 l4 -1 M60 128 l4 1 M84 116 l3 3', stroke_width=2))

# 13 fried egg
ITEMS['fried-egg'] = (
    z('path', '#ffffff', d='M40 100 Q30 60 70 50 Q100 30 134 48 Q172 58 168 100 Q176 140 142 156 Q110 176 76 160 Q34 150 40 100Z')
    + z('circle', '#ffc94d', cx=104, cy=102, r=30)
    + s('path', d='M88 86 Q94 80 102 80', stroke='#ffffff', stroke_width=4)
    + mf(104, 104, 11, 18, 3.2, 5, 3))

# 14 omurice
ITEMS['omurice'] = (
    z('ellipse', '#8fc7e8', cx=100, cy=136, rx=82, ry=36)
    + z('path', '#ffe27a', d='M34 134 Q36 76 100 70 Q164 76 166 134 Q100 152 34 134Z')
    + z('path', '#e04b5a', d='M100 124 C82 112 72 102 78 90 C84 82 96 84 100 94 C104 84 116 82 122 90 C128 102 118 112 100 124Z')
    + s('path', d='M54 112 Q58 98 66 90', stroke='#ffffff', stroke_width=4)
    + z('path', '#9ccf7a', d='M140 112 Q146 100 156 104 Q154 116 140 112Z'))

# 15 spaghetti
ITEMS['spaghetti'] = (
    z('ellipse', '#ffffff', cx=100, cy=138, rx=82, ry=34)
    + s('ellipse', 'none', cx=100, cy=136, rx=66, ry=24, stroke_width=2)
    + z('path', '#f5d58a', d='M42 134 Q44 84 100 78 Q156 84 158 134 Q100 150 42 134Z')
    + s('path', d='M54 124 Q70 96 96 112 Q120 128 146 104 M60 136 Q82 116 104 132 Q126 144 150 124 M70 104 Q86 90 104 98', stroke_width=2)
    + z('path', '#e04b5a', d='M70 92 Q70 66 100 64 Q132 66 132 92 Q120 104 100 100 Q80 106 70 92Z')
    + z('path', '#9ccf7a', d='M100 72 Q108 60 118 66 Q112 78 100 72Z')
    + stick('M140 116 L166 40', '#c9d3db', 8)
    + s('path', d='M160 46 L168 22 M166 48 L174 24 M172 50 L180 26', stroke_width=3))

# 16 salad bowl
ITEMS['salad-bowl'] = (
    z('path', '#7cc4a0', d='M34 106 Q30 80 50 78 Q54 58 76 64 Q86 46 104 56 Q122 44 132 62 Q156 58 154 80 Q172 84 166 106Z')
    + z('path', '#9ccf7a', d='M54 106 Q50 88 66 86 Q72 72 88 78 Q100 66 112 78 Q126 72 132 86 Q148 88 144 106Z')
    + z('circle', '#e04b5a', cx=78, cy=94, r=12)
    + z('circle', '#e04b5a', cx=128, cy=90, r=11)
    + z('circle', '#7cc4a0', cx=104, cy=86, r=11)
    + s('circle', '#9ccf7a', cx=104, cy=86, r=7, stroke_width=1.5)
    + z('path', '#8fc7e8', d='M28 104 Q32 170 100 172 Q168 170 172 104Z')
    + s('path', d='M42 124 Q100 136 158 124', stroke='#ffffff', stroke_width=4)
    + z('rect', '#8fc7e8', x=78, y=170, width=44, height=10, rx=3))

# 17 soup bowl
ITEMS['soup-bowl'] = (
    s('path', d='M78 54 Q70 44 78 34 Q86 24 78 14 M100 56 Q92 46 100 36 Q108 26 100 16 M122 54 Q114 44 122 34 Q130 24 122 14', stroke='#b9a99c', stroke_width=3)
    + z('ellipse', '#f5b971', cx=100, cy=100, rx=70, ry=20)
    + s('rect', '#e8735a', x=66, y=92, width=10, height=8, rx=2, stroke_width=2)
    + s('rect', '#9ccf7a', x=112, y=102, width=9, height=7, rx=2, stroke_width=2)
    + s('rect', '#ffe27a', x=90, y=104, width=10, height=8, rx=2, stroke_width=2)
    + stick('M128 96 L170 52', '#c9d3db', 8)
    + z('path', '#8fb3e0', d='M30 100 Q34 168 100 170 Q166 168 170 100 Q100 124 30 100Z')
    + s('path', d='M46 130 Q100 146 154 130', stroke='#ffffff', stroke_width=4)
    + z('rect', '#8fb3e0', x=76, y=168, width=48, height=12, rx=4))

# 18 sandwich
ITEMS['sandwich'] = (
    z('rect', '#f6e0c4', x=36, y=150, width=128, height=26, rx=6)
    + z('rect', '#e04b5a', x=34, y=140, width=132, height=14, rx=4)
    + z('rect', '#ffe27a', x=40, y=130, width=124, height=12, rx=3)
    + z('path', '#9ccf7a', d='M28 132 Q40 118 52 128 Q64 116 76 128 Q88 116 100 128 Q112 116 124 128 Q136 116 148 128 Q160 116 172 132 Q100 140 28 132Z')
    + z('path', '#d9a66b', d='M36 128 L100 34 L164 128Z')
    + s('path', '#f6e0c4', d='M52 120 L100 50 L148 120Z', stroke_width=2))

# 19 hot dog
ITEMS['hot-dog'] = '<g transform="rotate(-14 100 110)">' + (
    z('rect', '#f5b971', x=34, y=82, width=132, height=40, rx=20)
    + z('rect', '#e8735a', x=20, y=96, width=160, height=28, rx=14)
    + stick('M44 106 L56 98 L68 110 L80 98 L92 110 L104 98 L116 110 L128 98 L140 110 L152 100', '#ffe27a', 7)
    + z('path', '#f5b971', d='M30 114 Q30 154 72 154 L128 154 Q170 154 170 114 Q100 132 30 114Z')
) + '</g>'

# 20 french fries
ITEMS['french-fries'] = (
    ''.join(z('rect', '#ffe27a', x=x, y=y, width=14, height=80, rx=3, transform=f'rotate({r} {x+7} {y+80})')
            for x, y, r in ((60, 40, -14), (78, 26, -6), (96, 34, 2), (114, 22, 8), (130, 40, 16), (86, 48, -2), (106, 50, 6)))
    + z('path', '#e04b5a', d='M50 96 Q100 112 150 96 L138 178 L62 178Z')
    + mf(100, 138, 13, 22))
