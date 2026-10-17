from art import z, s, dot, cheeks, face, OUT, CH

ITEMS = {}
SK = '#ffd9b8'


def body(fill, cx=100, top=136, bottom=186):
    return z('path', fill, d=f'M{cx-36} {bottom} Q{cx-34} {top+2} {cx} {top} Q{cx+34} {top+2} {cx+36} {bottom}Z')


def note(x, y, fill='#a98bd0', k=1.0):
    return (z('ellipse', fill, cx=x, cy=y, rx=7 * k, ry=5.5 * k)
            + s('path', d=f'M{x+7*k} {y} L{x+7*k} {y-22*k} Q{x+14*k} {y-16*k} {x+16*k} {y-8*k}', stroke_width=2.5))


def face_s(cx, cy, w=10, r=3):
    return (dot(cx - w, cy, r) + dot(cx + w, cy, r) + cheeks(cx - w - 7, cx + w + 7, cy + 7, 5, 3)
            + s('path', d=f'M{cx-4} {cy+6} Q{cx} {cy+10} {cx+4} {cy+6}', stroke_width=2.5))


def thick(d, color, w=9, inner=4):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def rot(a, cx, cy, body):
    return f'<g transform="rotate({a} {cx} {cy})">{body}</g>'


# 1. guitar
ITEMS['guitar'] = (
    z('rect', '#9a6a3f', x=93, y=34, width=14, height=64)
    + z('rect', '#8b6b4f', x=88, y=20, width=24, height=22, rx=5)
    + dot(84, 26, 3) + dot(84, 36, 3) + dot(116, 26, 3) + dot(116, 36, 3)
    + z('path', '#f5b971', d='M100 86 C122 84 130 100 124 118 C142 126 142 182 100 184 C58 182 58 126 76 118 C70 100 78 84 100 86Z')
    + s('path', '#9a6a3f', d='M93 86 L107 86 L107 112 L93 112Z', stroke_width=2.5)
    + s('circle', '#8b6b4f', cx=100, cy=130, r=11)
    + s('rect', '#9a6a3f', x=84, y=158, width=32, height=8, rx=3, stroke_width=2.5)
    + s('path', d='M96 30 L96 160 M100 30 L100 160 M104 30 L104 160', stroke_width=1)
    + note(156, 70, '#7cc4b0', 0.9) + note(40, 92, '#f07a8a', 0.8)
)

# 2. piano
ITEMS['piano'] = (
    z('rect', '#9a6a3f', x=44, y=56, width=112, height=58, rx=4)
    + z('rect', '#8b6b4f', x=38, y=48, width=124, height=12, rx=3)
    + z('rect', '#ffffff', x=76, y=66, width=48, height=34, rx=2)
    + s('path', d='M82 76 L118 76 M82 84 L118 84 M82 92 L118 92', stroke_width=1.5)
    + dot(90, 84, 3) + dot(102, 80, 3) + dot(112, 88, 3)
    + z('rect', '#9a6a3f', x=48, y=136, width=12, height=40)
    + z('rect', '#9a6a3f', x=140, y=136, width=12, height=40)
    + s('rect', '#8b6b4f', x=60, y=136, width=80, height=34)
    + z('rect', '#ffffff', x=36, y=112, width=128, height=26, rx=3)
    + s('path', d=' '.join(f'M{36+i*16} 112 L{36+i*16} 138' for i in range(1, 8)), stroke_width=2)
    + ''.join(s('rect', OUT, x=36 + i * 16 - 4, y=112, width=8, height=14, stroke_width=1)
              for i in (1, 2, 4, 5, 6))
    + s('rect', '#ffc94d', x=92, y=166, width=16, height=6, rx=2, stroke_width=2)
    + s('path', d='M30 178 L170 178', stroke_width=2.5)
)

# 3. violin
VB = ('M92 66 C116 66 122 80 116 96 C112 104 110 110 116 118 C130 132 126 174 92 174 '
      'C58 174 54 132 68 118 C74 110 72 104 68 96 C62 80 68 66 92 66Z')
ITEMS['violin'] = (
    z('rect', '#8b6b4f', x=87, y=30, width=10, height=40)
    + z('circle', '#8b6b4f', cx=92, cy=26, r=8)
    + s('path', d='M84 34 L78 34 M100 34 L106 34', stroke_width=3)
    + z('path', '#d9a66b', d=VB)
    + s('rect', '#5b6b7a', x=87, y=66, width=10, height=58, rx=3, stroke_width=2.5)
    + s('path', d='M74 122 Q70 136 76 148 M110 122 Q114 136 108 148', stroke_width=2.5)
    + s('rect', '#f6e0c4', x=80, y=134, width=24, height=5, rx=2, stroke_width=2)
    + s('path', '#5b6b7a', d='M84 152 L100 152 L96 170 L88 170Z', stroke_width=2)
    + s('path', d='M90 36 L90 152 M94 36 L94 152', stroke_width=1)
    + thick('M128 178 L168 30', '#8b6b4f', 7, 3)
    + s('path', d='M134 172 L170 40', stroke_width=1.5)
    + z('rect', '#5b6b7a', x=124, y=162, width=12, height=14, rx=2)
)

# 4. drums
ITEMS['drums'] = (
    s('path', d='M162 70 L162 176 M162 176 L148 180 M162 176 L176 180', stroke_width=3)
    + z('ellipse', '#ffc94d', cx=162, cy=66, rx=22, ry=6)
    + s('path', d='M40 146 L30 178 M56 146 L66 178 M48 146 L48 178', stroke_width=3)
    + z('rect', '#8fc7e8', x=26, y=118, width=44, height=28)
    + s('path', d='M32 120 L40 144 L48 120 L56 144 L64 120', stroke_width=2)
    + z('ellipse', '#ffffff', cx=48, cy=118, rx=22, ry=6)
    + z('circle', '#e8735a', cx=104, cy=136, r=42)
    + z('circle', '#ffffff', cx=104, cy=136, r=32)
    + face_s(104, 134, 12, 3.5)
    + z('rect', '#e8735a', x=86, y=74, width=36, height=22)
    + z('ellipse', '#ffffff', cx=104, cy=74, rx=18, ry=5)
    + thick('M26 98 L58 70', '#d9a66b', 7, 3) + thick('M40 104 L72 80', '#d9a66b', 7, 3)
)

# 5. trumpet
ITEMS['trumpet'] = (
    s('rect', x=60, y=104, width=82, height=34, rx=15, stroke_width=11)
    + s('rect', x=60, y=104, width=82, height=34, rx=15, stroke='#ffc94d', stroke_width=5)
    + z('path', '#ffc94d', d='M138 98 Q156 96 172 74 L172 138 Q156 116 138 114Z')
    + z('ellipse', '#ffc94d', cx=172, cy=106, rx=8, ry=32)
    + s('ellipse', '#f5b971', cx=172, cy=106, rx=4, ry=24, stroke_width=2)
    + z('rect', '#ffc94d', x=40, y=98, width=102, height=14, rx=4)
    + z('path', '#b9a99c', d='M26 96 L40 101 L40 109 L26 114Z')
    + ''.join(z('rect', '#ffc94d', x=x, y=76, width=11, height=28, rx=2)
              + z('rect', '#f6e0c4', x=x - 2, y=68, width=15, height=8, rx=3) for x in (76, 94, 112))
    + note(60, 56, '#a98bd0', 0.9) + note(128, 44, '#7cc4b0', 0.8)
)

# 6. singing-mic
ITEMS['singing-mic'] = (
    body('#f07a8a', cx=92)
    + face(92, 96, SK, '#5a4033', 'open')
    + thick('M136 162 L146 128', '#5b6b7a', 10, 5)
    + z('circle', '#c9d3db', cx=148, cy=120, r=12)
    + s('path', d='M140 116 L156 116 M139 122 L157 122', stroke_width=1.5)
    + z('circle', SK, cx=134, cy=162, r=9)
    + note(40, 54, '#a98bd0') + note(150, 52, '#7cc4b0', 0.9) + note(30, 120, '#f5b971', 0.8)
)

# 7. karaoke
ITEMS['karaoke'] = (
    z('circle', '#c9d3db', cx=160, cy=40, r=15)
    + s('path', d='M146 34 L174 34 M146 46 L174 46 M154 26 L152 54 M166 26 L168 54', stroke_width=1.5)
    + s('path', d='M160 18 L160 25', stroke_width=2)
    + z('rect', '#5b6b7a', x=26, y=34, width=104, height=70, rx=5)
    + s('rect', '#a98bd0', x=33, y=41, width=90, height=56, rx=3, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=104, cy=58, r=9, stroke_width=2)
    + s('rect', '#ffffff', x=42, y=74, width=48, height=6, rx=3, stroke_width=1.5)
    + s('rect', '#f6a6b8', x=42, y=84, width=34, height=6, rx=3, stroke_width=1.5)
    + s('path', d='M78 104 L78 116 M58 116 L98 116', stroke_width=3)
    + s('path', d='M158 92 L158 172 M144 176 L172 176', stroke_width=3)
    + z('circle', '#c9d3db', cx=158, cy=84, r=10)
    + z('path', '#f07a8a', d='M30 140 Q30 128 42 128 L120 128 Q132 128 132 140 L132 176 L30 176Z')
    + z('rect', '#f07a8a', x=26, y=152, width=110, height=24, rx=6)
    + s('path', d='M80 132 L80 150', stroke_width=2)
    + note(146, 124, '#7cc4b0', 0.8)
)

# 8. music-notes
ITEMS['music-notes'] = (
    z('path', '#a98bd0', d='M84 56 L152 40 L152 56 L84 72Z')
    + s('path', d='M84 60 L84 146 M152 44 L152 130', stroke_width=4)
    + z('ellipse', '#a98bd0', cx=68, cy=148, rx=20, ry=15)
    + z('ellipse', '#a98bd0', cx=136, cy=132, rx=20, ry=15)
    + dot(62, 146, 2.5) + dot(74, 146, 2.5) + dot(130, 130, 2.5) + dot(142, 130, 2.5)
    + cheeks(56, 80, 153, 4, 2.5) + cheeks(124, 148, 137, 4, 2.5)
    + note(44, 70, '#f07a8a', 1.1)
    + s('path', '#ffe27a', d='M168 82 L171 90 L179 92 L171 95 L168 103 L165 95 L157 92 L165 90Z', stroke_width=2)
    + s('path', '#ffe27a', d='M40 104 L42 110 L48 112 L42 114 L40 120 L38 114 L32 112 L38 110Z', stroke_width=2)
)

# 9. painting-easel
ITEMS['painting-easel'] = (
    thick('M94 28 L94 176', '#9a6a3f', 9, 4)
    + thick('M94 28 L58 180', '#9a6a3f', 9, 4) + thick('M94 28 L130 180', '#9a6a3f', 9, 4)
    + z('rect', '#ffffff', x=44, y=38, width=100, height=78, rx=2)
    + s('rect', '#8fc7e8', x=50, y=44, width=88, height=66, stroke_width=0)
    + s('circle', '#ffe27a', cx=118, cy=62, r=9, stroke_width=2)
    + s('path', '#9ccf7a', d='M50 110 L50 92 Q70 70 90 90 Q108 76 138 96 L138 110Z', stroke_width=2)
    + s('rect', x=50, y=44, width=88, height=66, stroke_width=2)
    + z('rect', '#9a6a3f', x=38, y=116, width=112, height=9, rx=3)
    + z('path', '#d9a66b', d='M128 150 Q132 130 156 132 Q182 136 180 156 Q176 176 152 174 Q140 172 146 162 Q148 154 138 158 Q126 162 128 150Z')
    + s('circle', '#e04b5a', cx=146, cy=142, r=4.5, stroke_width=2)
    + s('circle', '#ffe27a', cx=160, cy=140, r=4.5, stroke_width=2)
    + s('circle', '#8fb3e0', cx=170, cy=152, r=4.5, stroke_width=2)
    + s('circle', '#9ccf7a', cx=162, cy=164, r=4.5, stroke_width=2)
    + thick('M120 134 L152 104', '#f5b971', 7, 3)
    + s('path', '#e04b5a', d='M152 104 L158 94 L162 100Z', stroke_width=2)
)

# 10. sewing-machine
ITEMS['sewing-machine'] = (
    s('path', d='M108 40 Q84 40 72 64 Q60 90 54 120', stroke_width=1.5)
    + z('rect', '#e8735a', x=100, y=30, width=16, height=20, rx=3)
    + z('path', '#f6a6b8', d='M38 64 Q38 54 48 54 L152 54 Q162 54 162 64 L162 152 L122 152 L122 94 L66 94 L66 122 L38 122Z')
    + s('rect', '#ffffff', x=80, y=66, width=30, height=12, rx=4, stroke_width=2)
    + z('circle', '#b9a99c', cx=166, cy=94, r=13)
    + dot(166, 94, 3)
    + s('path', d='M52 122 L52 144', stroke_width=2.5)
    + s('path', d='M44 140 L60 140', stroke_width=3)
    + z('rect', '#c9d3db', x=26, y=150, width=148, height=24, rx=5)
    + s('path', '#8fc7e8', d='M30 146 L104 146 L108 156 L34 156Z', stroke_width=2)
    + s('path', d='M38 151 L44 151 M50 151 L56 151 M62 151 L68 151 M74 151 L80 151', stroke_width=1.5)
    + face_s(142, 120, 8, 3)
)

# 11. pottery
ITEMS['pottery'] = (
    z('path', '#5b6b7a', d='M64 154 L136 154 L146 180 L54 180Z')
    + z('ellipse', '#c9d3db', cx=100, cy=152, rx=58, ry=10)
    + z('path', '#d9a66b', d='M74 148 Q62 122 80 102 Q88 92 84 78 L116 78 Q112 92 120 102 Q138 122 126 148Z')
    + s('ellipse', '#9a6a3f', cx=100, cy=78, rx=16, ry=4, stroke_width=2.5)
    + s('path', d='M74 128 Q100 134 126 128', stroke_width=1.5)
    + thick('M24 150 Q40 132 62 120', SK, 12, 6) + z('circle', SK, cx=66, cy=118, r=10)
    + thick('M176 150 Q160 132 138 120', SK, 12, 6) + z('circle', SK, cx=134, cy=118, r=10)
    + dot(92, 116, 3) + dot(108, 116, 3) + cheeks(84, 116, 123, 4.5, 2.5)
    + s('path', d='M96 124 Q100 128 104 124', stroke_width=2.5)
    + s('path', d='M40 168 Q36 160 42 154 M160 168 Q164 160 158 154', stroke_width=2)
)

# 12. fishing
ITEMS['fishing'] = (
    s('path', d='M152 32 L150 98', stroke_width=1.5)
    + thick('M32 178 Q60 70 152 32', '#9a6a3f', 8, 3)
    + z('circle', '#c9d3db', cx=50, cy=150, r=9)
    + dot(50, 150, 2.5)
    + z('path', '#8fc7e8', d='M150 98 C168 104 170 140 152 156 C134 140 132 104 150 98Z')
    + z('path', '#8fc7e8', d='M152 152 L138 174 L166 174Z')
    + s('path', d='M140 118 Q152 124 164 118', stroke_width=2)
    + dot(144, 108, 3) + dot(158, 108, 3)
    + s('path', d='M142 132 L148 128 M162 132 L156 128', stroke_width=1.5)
    + s('path', '#8fc7e8', d='M86 182 Q100 172 114 182 Q128 172 142 182 Q156 172 172 182Z', stroke_width=2.5)
    + s('path', d='M126 100 L118 96 M176 100 L184 96 M128 88 L122 82', stroke_width=2)
)

# 13. video-game
ITEMS['video-game'] = (
    z('path', '#a98bd0', d='M52 72 Q100 62 148 72 Q176 78 178 124 Q180 156 160 156 Q146 156 134 132 '
      'L66 132 Q54 156 40 156 Q20 156 22 124 Q24 78 52 72Z')
    + s('path', '#ffffff', d='M52 92 L64 92 L64 104 L76 104 L76 116 L64 116 L64 128 L52 128 L52 116 L40 116 L40 104 L52 104Z', stroke_width=2.5)
    + s('circle', '#e04b5a', cx=146, cy=94, r=6, stroke_width=2.5)
    + s('circle', '#9ccf7a', cx=160, cy=108, r=6, stroke_width=2.5)
    + s('circle', '#8fb3e0', cx=146, cy=122, r=6, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=132, cy=108, r=6, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=86, cy=118, r=10) + z('circle', '#5b6b7a', cx=114, cy=118, r=10)
    + s('rect', '#f6e0c4', x=90, y=86, width=20, height=8, rx=4, stroke_width=2)
)

# 14. board-game
squares = ''
cols = ['#f07a8a', '#ffe27a', '#8fc7e8', '#ffffff']
k = 0
for i in range(7):
    squares += s('rect', cols[k % 4], x=34 + i * 19, y=44, width=17, height=17, rx=2, stroke_width=2); k += 1
for j in range(1, 5):
    squares += s('rect', cols[k % 4], x=148, y=44 + j * 19, width=17, height=17, rx=2, stroke_width=2); k += 1
for i in range(5, -1, -1):
    squares += s('rect', cols[k % 4], x=34 + i * 19, y=120, width=17, height=17, rx=2, stroke_width=2); k += 1
for j in range(3, 0, -1):
    squares += s('rect', cols[k % 4], x=34, y=44 + j * 19, width=17, height=17, rx=2, stroke_width=2); k += 1


def pawn(x, y, c):
    return z('path', c, d=f'M{x-11} {y+16} Q{x} {y-4} {x+11} {y+16}Z') + z('circle', c, cx=x, cy=y - 4, r=8)


def die(x, y, pips):
    o = z('rect', '#ffffff', x=x, y=y, width=30, height=30, rx=6)
    for px, py in pips:
        o += dot(x + px, y + py, 3)
    return o


ITEMS['board-game'] = (
    z('rect', '#9ccf7a', x=26, y=36, width=148, height=110, rx=6)
    + squares
    + s('circle', '#f6e0c4', cx=100, cy=90, r=16, stroke_width=2)
    + s('path', '#ffc94d', d='M100 80 L103 87 L110 88 L105 93 L106 100 L100 96 L94 100 L95 93 L90 88 L97 87Z', stroke_width=1.5)
    + pawn(62, 112, '#e8735a') + pawn(156, 70, '#8fb3e0')
    + die(70, 148, [(8, 8), (15, 15), (22, 22)])
    + die(112, 152, [(8, 8), (22, 8), (8, 22), (22, 22)])
)

# 15. playing-cards
HEART = 'M0 10 C-6 5 -10 1 -10 -4 C-10 -9 -3 -10 0 -4 C3 -10 10 -9 10 -4 C10 1 6 5 0 10Z'


def pip(kind, x, y, k=1.0):
    t = f'translate({x} {y}) scale({k})'
    if kind == 'heart':
        return f'<g transform="{t}">' + s('path', '#e04b5a', d=HEART, stroke_width=2 / k) + '</g>'
    if kind == 'diamond':
        return f'<g transform="{t}">' + s('path', '#e04b5a', d='M0 -11 L8 0 L0 11 L-8 0Z', stroke_width=2 / k) + '</g>'
    return (f'<g transform="{t}">' + s('circle', '#5b6b7a', cx=0, cy=-5, r=5, stroke_width=2 / k)
            + s('circle', '#5b6b7a', cx=-5, cy=2, r=5, stroke_width=2 / k)
            + s('circle', '#5b6b7a', cx=5, cy=2, r=5, stroke_width=2 / k)
            + s('path', '#5b6b7a', d='M0 2 L-4 11 L4 11Z', stroke_width=2 / k) + '</g>')


def card(kind):
    return (z('rect', '#ffffff', x=68, y=40, width=64, height=92, rx=6)
            + pip(kind, 100, 86, 1.6) + pip(kind, 78, 52, 0.6) + pip(kind, 122, 120, 0.6))


ITEMS['playing-cards'] = (
    rot(-22, 100, 176, card('club')) + rot(22, 100, 176, card('diamond')) + rot(0, 100, 176, card('heart'))
)

# 16. shogi
grid = ' '.join(f'M{46+i*12} 48 L{46+i*12} 138' for i in range(10)) + ' ' + \
       ' '.join(f'M46 {48+j*10} L154 {48+j*10}' for j in range(10))


def koma(cx, cy, w=10, h=9, flip=False):
    if flip:
        d = f'M{cx-w*0.6} {cy-h} L{cx+w*0.6} {cy-h} L{cx+w*0.75} {cy+h*0.4} L{cx} {cy+h} L{cx-w*0.75} {cy+h*0.4}Z'
    else:
        d = f'M{cx} {cy-h} L{cx+w*0.75} {cy-h*0.4} L{cx+w*0.6} {cy+h} L{cx-w*0.6} {cy+h} L{cx-w*0.75} {cy-h*0.4}Z'
    return d


ITEMS['shogi'] = (
    z('rect', '#d9a66b', x=34, y=136, width=132, height=20, rx=2)
    + z('rect', '#f5d58a', x=34, y=38, width=132, height=108, rx=3)
    + s('path', d=grid, stroke_width=1)
    + ''.join(s('path', '#f6e0c4', d=koma(52 + i * 12, 113 + (6 if False else 0), 9, 4), stroke_width=1.5)
              for i in range(0))
    + ''.join(s('path', '#f6e0c4', d=koma(52 + i * 12, 123, 11, 4.6), stroke_width=1.5) for i in (0, 2, 3, 5, 6, 8))
    + ''.join(s('path', '#f6e0c4', d=koma(52 + i * 12, 63, 11, 4.6, True), stroke_width=1.5) for i in (1, 2, 4, 6, 7))
    + s('path', '#f6e0c4', d=koma(88, 93, 11, 4.6), stroke_width=1.5)
    + s('path', '#f6e0c4', d=koma(112, 73, 11, 4.6, True), stroke_width=1.5)
    + z('path', '#f6e0c4', d=koma(150, 158, 30, 22))
    + face_s(150, 160, 7, 3)
)

# 17. jigsaw-puzzle


def piece(x, y, sz, t, r, b, l):
    a, c = 0.38 * sz, 0.62 * sz
    rad = 0.16 * sz

    def bump(kind, px, py):
        if kind == 0:
            return f' L{px} {py}'
        sw = 1 if kind == 1 else 0
        return f' A{rad} {rad} 0 1 {sw} {px} {py}'
    d = f'M{x} {y}'
    d += f' L{x+a} {y}' + bump(t, x + c, y) + f' L{x+sz} {y}'
    d += f' L{x+sz} {y+a}' + bump(r, x + sz, y + c) + f' L{x+sz} {y+sz}'
    d += f' L{x+c} {y+sz}' + bump(b, x + a, y + sz) + f' L{x} {y+sz}'
    d += f' L{x} {y+c}' + bump(l, x, y + a) + ' Z'
    return d


P = 52
ITEMS['jigsaw-puzzle'] = (
    z('path', '#8fc7e8', d=piece(26, 76, P, 0, 1, -1, 0))
    + z('path', '#f5b971', d=piece(78, 76, P, 0, 0, 1, -1))
    + z('path', '#9ccf7a', d=piece(26, 128, P, 1, -1, 0, 0))
    + s('path', d=piece(78, 128, P, -1, 0, 0, 1), stroke_width=2, stroke_dasharray='5 5')
    + '<g transform="translate(-6 4)">' + rot(14, 150, 64, z('path', '#f07a8a', d=piece(124, 38, P, -1, 0, 0, 1))
          + dot(141, 64, 3) + dot(159, 64, 3) + cheeks(134, 166, 71, 5, 3)
          + s('path', d='M146 70 Q150 74 154 70', stroke_width=2.5)) + '</g>'
    + s('path', d='M112 30 L104 22 M124 24 L122 14 M100 44 L90 40', stroke_width=2)
)

# 18. comic-book
ITEMS['comic-book'] = (
    z('path', '#ffffff', d='M100 52 Q70 42 28 48 L28 160 Q70 154 100 164Z')
    + z('path', '#ffffff', d='M100 52 Q130 42 172 48 L172 160 Q130 154 100 164Z')
    + s('path', d='M100 52 L100 164', stroke_width=3)
    + s('rect', '#8fc7e8', x=36, y=58, width=56, height=40, rx=2, stroke_width=2)
    + s('circle', '#ffd9b8', cx=56, cy=84, r=10, stroke_width=2)
    + dot(52, 84, 1.8) + dot(60, 84, 1.8)
    + s('path', '#ffffff', d='M68 64 L88 64 Q90 64 90 70 L90 74 Q90 78 86 78 L76 78 L72 84 L72 78 L68 78 Q66 78 66 74 L66 70 Q66 64 68 64Z', stroke_width=1.5)
    + s('rect', '#f5d58a', x=36, y=104, width=26, height=48, rx=2, stroke_width=2)
    + s('rect', '#f6a6b8', x=66, y=104, width=26, height=48, rx=2, stroke_width=2)
    + s('path', '#ffc94d', d='M79 116 L82 124 L90 124 L84 130 L86 138 L79 133 L72 138 L74 130 L68 124 L76 124Z', stroke_width=1.5)
    + s('path', d='M42 140 L56 116', stroke_width=2)
    + s('rect', '#9ccf7a', x=108, y=58, width=56, height=46, rx=2, stroke_width=2)
    + s('path', '#ffe27a', d='M136 62 L140 74 L152 70 L144 80 L156 86 L142 86 L144 98 L136 88 L128 98 L130 86 L116 86 L128 80 L120 70 L132 74Z', stroke_width=1.5)
    + s('rect', '#f5b971', x=108, y=110, width=56, height=42, rx=2, stroke_width=2)
    + s('ellipse', '#ffffff', cx=136, cy=128, rx=18, ry=10, stroke_width=1.5)
    + s('path', '#ffffff', d='M128 136 L124 146 L136 137', stroke_width=1.5)
    + dot(129, 128, 2) + dot(136, 128, 2) + dot(143, 128, 2)
)

# 19. movie-theater
ITEMS['movie-theater'] = (
    rot(-14, 150, 130,
        z('path', '#f5d58a', d='M118 108 L182 108 L182 122 Q176 126 182 130 L182 152 L118 152 L118 130 Q124 126 118 122Z')
        + s('path', d='M138 110 L138 150', stroke_width=1.5, stroke_dasharray='4 4')
        + s('path', '#e04b5a', d='M160 120 L163 127 L171 128 L165 133 L167 141 L160 137 L153 141 L155 133 L149 128 L157 127Z', stroke_width=1.5))
    + ''.join(z('circle', '#f6e0c4', cx=x, cy=y, r=12) for x, y in
              ((50, 82), (70, 70), (92, 64), (114, 70), (130, 84), (60, 60), (84, 48), (106, 50)))
    + s('circle', '#ffe27a', cx=76, cy=58, r=5, stroke_width=1.5)
    + s('circle', '#ffe27a', cx=118, cy=60, r=5, stroke_width=1.5)
    + z('path', '#ffffff', d='M40 84 L140 84 L126 178 L54 178Z')
    + s('path', '#e04b5a', d='M54 84 L68 84 L72 178 L60 178Z', stroke_width=2)
    + s('path', '#e04b5a', d='M84 84 L96 84 L96 178 L84 178Z', stroke_width=2)
    + s('path', '#e04b5a', d='M112 84 L126 84 L120 178 L108 178Z', stroke_width=2)
    + s('path', d='M40 84 L140 84 L126 178 L54 178Z')
    + s('ellipse', '#ffffff', cx=90, cy=128, rx=22, ry=14, stroke_width=2)
    + face_s(90, 126, 8, 3)
)

# 20. film-reel
ITEMS['film-reel'] = (
    z('rect', '#5b6b7a', x=84, y=146, width=94, height=30, rx=2)
    + ''.join(s('rect', '#ffffff', x=x, y=149, width=6, height=5, rx=1, stroke_width=1) +
              s('rect', '#ffffff', x=x, y=168, width=6, height=5, rx=1, stroke_width=1) for x in range(124, 176, 12))
    + ''.join(s('rect', '#8fc7e8', x=x, y=156, width=18, height=10, rx=1, stroke_width=1.5) for x in (124, 148))
    + z('circle', '#c9d3db', cx=90, cy=94, r=58)
    + ''.join(s('circle', '#ffffff', cx=round(90 + 34 * __import__('math').cos(a), 1),
                cy=round(94 + 34 * __import__('math').sin(a), 1), r=13)
              for a in [i * 2 * 3.14159 / 5 - 1.5708 for i in range(5)])
    + z('circle', '#5b6b7a', cx=90, cy=94, r=10)
    + dot(90, 94, 3.5, '#ffffff')
)
