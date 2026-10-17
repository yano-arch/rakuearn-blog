from art import z, s, dot, cheeks, face, OUT, CH
import math
ITEMS = {}


def mouth_w(cx, cy):
    return s('path', d=f'M{cx-6} {cy} Q{cx-3} {cy+4} {cx} {cy} Q{cx+3} {cy+4} {cx+6} {cy}', stroke_width=2.5)


def smile(cx, cy, w=5):
    return s('path', d=f'M{cx-w} {cy} Q{cx} {cy+5} {cx+w} {cy}', stroke_width=2.5)


def thick(d, col, w=10):
    """outlined thick stroke (tail, arm, antler)"""
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=col, stroke_width=w)


def scallop(cx, cy, r, n, bump):
    pts = []
    for i in range(n):
        a1 = 2 * math.pi * i / n - math.pi / 2
        a2 = 2 * math.pi * (i + 0.5) / n - math.pi / 2
        a3 = 2 * math.pi * (i + 1) / n - math.pi / 2
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        c = (cx + (r + bump) * math.cos(a2), cy + (r + bump) * math.sin(a2))
        p3 = (cx + r * math.cos(a3), cy + r * math.sin(a3))
        if i == 0:
            pts.append(f'M{p1[0]:.1f} {p1[1]:.1f}')
        pts.append(f'Q{c[0]:.1f} {c[1]:.1f} {p3[0]:.1f} {p3[1]:.1f}')
    return ' '.join(pts) + 'Z'


def sit(col, belly=None, cy=148, rx=38, ry=32, fcol=None):
    """round sitting body + two front feet"""
    fc = fcol or col
    o = z('ellipse', col, cx=100, cy=cy, rx=rx, ry=ry)
    if belly:
        o += s('ellipse', belly, cx=100, cy=cy + 6, rx=rx * 0.55, ry=ry * 0.65, stroke='none')
    o += z('ellipse', fc, cx=84, cy=cy + ry - 2, rx=12, ry=7) + z('ellipse', fc, cx=116, cy=cy + ry - 2, rx=12, ry=7)
    return o


# 1. rooster (side view, facing right)
ITEMS['rooster'] = (
    s('path', d='M94 150 L94 178 M86 180 L102 180 M114 150 L114 178 M106 180 L122 180', stroke_width=3)
    + z('path', '#e8735a', d='M70 118 Q36 104 40 58 Q60 74 74 98Z')
    + z('path', '#9ccf7a', d='M68 124 Q34 124 28 90 Q52 96 72 112Z')
    + z('path', '#f5b971', d='M74 108 Q52 80 64 48 Q78 70 84 98Z')
    + z('ellipse', '#f4f4f0', cx=102, cy=124, rx=40, ry=32)
    + z('path', '#e04b5a', d='M116 54 Q112 36 124 40 Q128 26 138 38 Q150 32 150 52Z')
    + z('circle', '#f4f4f0', cx=132, cy=74, r=25)
    + z('path', '#ffc94d', d='M154 66 L172 74 L154 82Z')
    + z('path', '#e04b5a', d='M148 84 Q156 100 146 100 Q140 92 144 84Z')
    + dot(140, 68) + f'<ellipse cx="134" cy="82" rx="6" ry="3.5" fill="{CH}" stroke="none"/>'
    + s('path', '#f6e0c4', d='M78 118 Q100 108 122 120 Q106 144 78 118Z', stroke_width=2.5)
)

# 2. duck floating on water (facing left)
ITEMS['duck'] = (
    z('ellipse', '#8fc7e8', cx=104, cy=166, rx=74, ry=14)
    + z('path', '#f4f4f0', d='M148 126 L176 104 L170 138Z')
    + z('ellipse', '#f4f4f0', cx=110, cy=138, rx=52, ry=30)
    + z('circle', '#f4f4f0', cx=78, cy=84, r=29)
    + z('path', '#ffc94d', d='M54 82 Q30 80 30 92 Q36 102 56 96Z')
    + dot(74, 78) + f'<ellipse cx="84" cy="92" rx="6" ry="3.5" fill="{CH}" stroke="none"/>'
    + s('path', '#c9d3db', d='M100 132 Q128 120 152 134 Q130 156 100 132Z', stroke_width=2.5)
    + s('path', d='M40 178 Q50 172 60 178 M140 180 Q150 174 160 180', stroke='#8fc7e8', stroke_width=2.5)
)

# 3. donkey (sitting, long ears, white muzzle)
ITEMS['donkey'] = (
    sit('#b9a99c', '#f4f4f0', cy=150, rx=36, ry=30, fcol='#5b6b7a')
    + z('ellipse', '#b9a99c', cx=78, cy=46, rx=9, ry=24, transform='rotate(-18 78 46)')
    + z('ellipse', '#b9a99c', cx=122, cy=46, rx=9, ry=24, transform='rotate(18 122 46)')
    + s('ellipse', '#f4f4f0', cx=78, cy=48, rx=4, ry=15, transform='rotate(-18 78 48)', stroke='none')
    + s('ellipse', '#f4f4f0', cx=122, cy=48, rx=4, ry=15, transform='rotate(18 122 48)', stroke='none')
    + z('ellipse', '#b9a99c', cx=100, cy=86, rx=30, ry=36)
    + s('path', '#5b6b7a', d='M90 54 Q92 42 100 46 Q108 40 112 54 Q100 60 90 54Z', stroke_width=2.5)
    + z('ellipse', '#f4f4f0', cx=100, cy=108, rx=23, ry=15)
    + dot(87, 80) + dot(113, 80) + cheeks(76, 124, 94, 5, 3)
    + dot(93, 104, 2.5) + dot(107, 104, 2.5) + smile(100, 112)
)

# 4. lion with a mane
ITEMS['lion'] = (
    thick('M132 160 Q166 160 164 128', '#f5d58a', 6) + z('circle', '#9a6a3f', cx=164, cy=124, r=9)
    + sit('#f5d58a', '#f6e0c4', cy=150, rx=36, ry=30)
    + z('path', '#d9a66b', d=scallop(100, 86, 44, 12, 12))
    + z('circle', '#f5d58a', cx=74, cy=58, r=10) + z('circle', '#f5d58a', cx=126, cy=58, r=10)
    + z('circle', '#f5d58a', cx=100, cy=90, r=31)
    + s('ellipse', '#f6e0c4', cx=100, cy=104, rx=16, ry=11, stroke='none')
    + dot(88, 86) + dot(112, 86) + cheeks(78, 122, 98, 5, 3)
    + s('path', '#9a6a3f', d='M95 97 L105 97 L100 102Z', stroke_width=2)
    + mouth_w(100, 104)
)

# 5. tiger (orange with stripes)
T = '#f5b971'
ITEMS['tiger'] = (
    thick('M134 166 Q170 164 164 130', T, 7)
    + s('path', d='M166 150 L156 148 M168 138 L158 138', stroke_width=3)
    + sit(T, '#f4f4f0', cy=148, rx=38, ry=32)
    + s('path', OUT, d='M64 140 L76 144 L64 148Z M136 140 L124 144 L136 148Z M66 156 L76 158 L68 162Z M134 156 L124 158 L132 162Z', stroke='none')
    + z('circle', T, cx=72, cy=58, r=13) + z('circle', T, cx=128, cy=58, r=13)
    + s('circle', '#f4f4f0', cx=72, cy=58, r=6, stroke='none') + s('circle', '#f4f4f0', cx=128, cy=58, r=6, stroke='none')
    + z('circle', T, cx=100, cy=88, r=34)
    + s('ellipse', '#f4f4f0', cx=100, cy=104, rx=18, ry=12, stroke='none')
    + s('path', OUT, d='M92 56 L100 68 L108 56Z M68 82 L80 86 L68 90Z M132 82 L120 86 L132 90Z M70 98 L80 100 L72 104Z M130 98 L120 100 L128 104Z', stroke='none')
    + dot(88, 86) + dot(112, 86) + cheeks(80, 120, 97, 5, 3)
    + s('path', '#f6a6b8', d='M95 97 L105 97 L100 102Z', stroke_width=2)
    + mouth_w(100, 104)
)

# 6. elephant
E = '#c9d3db'
ITEMS['elephant'] = (
    sit(E, None, cy=152, rx=38, ry=28)
    + z('ellipse', E, cx=60, cy=84, rx=26, ry=32) + z('ellipse', E, cx=140, cy=84, rx=26, ry=32)
    + s('ellipse', '#f6a6b8', cx=60, cy=86, rx=14, ry=20, stroke='none') + s('ellipse', '#f6a6b8', cx=140, cy=86, rx=14, ry=20, stroke='none')
    + z('circle', E, cx=100, cy=80, r=33)
    + '<g transform="translate(4 4)">' + s('path', E, d='M89 98 L89 128 Q90 150 114 148 Q128 146 126 132 Q124 126 118 130 Q114 136 108 132 Q104 128 105 120 L111 98Z', stroke='none') + '</g>'
    + s('path', E, d='M89 98 L89 128 Q90 150 114 148 Q128 146 126 132 Q124 126 118 130 Q114 136 108 132 Q104 128 105 120 L111 98Z', stroke='none')
    + s('path', d='M89 104 L89 128 Q90 150 114 148 Q128 146 126 132 Q124 126 118 130 Q114 136 108 132 Q104 128 105 120 L111 104')
    + dot(86, 78) + dot(114, 78) + cheeks(76, 124, 90, 5, 3)
    + s('path', d='M94 112 L100 112 M94 122 L100 122', stroke_width=2)
)

# 7. giraffe
G = '#f5d58a'; GS = '#d9a66b'
ITEMS['giraffe'] = (
    thick('M156 138 Q168 148 166 162', G, 3) + z('ellipse', '#9a6a3f', cx=166, cy=166, rx=4, ry=6)
    + z('rect', G, x=84, y=146, width=12, height=34, rx=5) + z('rect', G, x=104, y=146, width=12, height=34, rx=5)
    + z('rect', G, x=130, y=146, width=12, height=34, rx=5) + z('rect', G, x=146, y=146, width=12, height=34, rx=5)
    + z('ellipse', G, cx=120, cy=138, rx=44, ry=24)
    + s('ellipse', GS, cx=106, cy=136, rx=8, ry=6, stroke='none') + s('ellipse', GS, cx=128, cy=128, rx=7, ry=5, stroke='none')
    + s('ellipse', GS, cx=146, cy=140, rx=8, ry=6, stroke='none') + s('ellipse', GS, cx=124, cy=148, rx=6, ry=5, stroke='none')
    + z('rect', G, x=78, y=56, width=26, height=96, rx=10)
    + s('ellipse', GS, cx=90, cy=86, rx=6, ry=5, stroke='none') + s('ellipse', GS, cx=94, cy=108, rx=6, ry=5, stroke='none')
    + s('ellipse', GS, cx=88, cy=128, rx=5, ry=5, stroke='none')
    + s('path', d='M82 36 L78 20 M102 36 L106 20') + dot(78, 18, 5, '#9a6a3f') + dot(106, 18, 5, '#9a6a3f')
    + z('ellipse', G, cx=64, cy=42, rx=10, ry=5, transform='rotate(-20 64 42)')
    + z('ellipse', G, cx=120, cy=42, rx=10, ry=5, transform='rotate(20 120 42)')
    + z('ellipse', G, cx=92, cy=50, rx=25, ry=20)
    + s('ellipse', '#f6e0c4', cx=92, cy=60, rx=14, ry=8, stroke='none')
    + dot(82, 46, 3) + dot(102, 46, 3) + cheeks(74, 110, 56, 5, 3)
    + dot(88, 58, 1.8) + dot(96, 58, 1.8) + smile(92, 63, 4)
)

# 8. zebra
W = '#f4f4f0'
ITEMS['zebra'] = (
    sit(W, None, cy=150, rx=36, ry=30, fcol='#5b6b7a')
    + s('path', OUT, d='M64 138 L82 142 L64 148Z M136 138 L118 142 L136 148Z M66 156 L80 158 L70 164Z M134 156 L120 158 L130 164Z', stroke='none')
    + z('ellipse', W, cx=74, cy=54, rx=10, ry=15, transform='rotate(-25 74 54)')
    + z('ellipse', W, cx=126, cy=54, rx=10, ry=15, transform='rotate(25 126 54)')
    + s('ellipse', OUT, cx=74, cy=56, rx=4, ry=8, transform='rotate(-25 74 56)', stroke='none')
    + s('ellipse', OUT, cx=126, cy=56, rx=4, ry=8, transform='rotate(25 126 56)', stroke='none')
    + z('path', '#5b6b7a', d='M84 56 L86 36 L94 46 L100 32 L106 46 L114 36 L116 56Z')
    + z('ellipse', W, cx=100, cy=86, rx=30, ry=36)
    + s('path', OUT, d='M92 52 L100 64 L108 52Z M70 76 L82 80 L71 86Z M130 76 L118 80 L129 86Z M72 94 L80 96 L74 100Z M128 94 L120 96 L126 100Z', stroke='none')
    + z('ellipse', '#5b6b7a', cx=100, cy=108, rx=22, ry=14)
    + dot(87, 80) + dot(113, 80) + cheeks(78, 122, 92, 5, 3)
    + dot(93, 104, 2.5, W) + dot(107, 104, 2.5, W) + s('path', d='M95 113 Q100 117 105 113', stroke=W, stroke_width=2.5)
)

# 9. hippo (pink)
P = '#f6a6b8'
ITEMS['hippo'] = (
    sit(P, None, cy=152, rx=44, ry=28)
    + z('circle', P, cx=76, cy=54, r=9) + z('circle', P, cx=124, cy=54, r=9)
    + s('circle', '#f07a8a', cx=76, cy=54, r=4, stroke='none') + s('circle', '#f07a8a', cx=124, cy=54, r=4, stroke='none')
    + z('ellipse', P, cx=100, cy=76, rx=32, ry=26)
    + z('ellipse', P, cx=100, cy=108, rx=42, ry=26)
    + dot(88, 70) + dot(112, 70)
    + f'<ellipse cx="86" cy="98" rx="3.5" ry="5" fill="{OUT}" stroke="none"/><ellipse cx="114" cy="98" rx="3.5" ry="5" fill="{OUT}" stroke="none"/>'
    + cheeks(70, 130, 110, 6, 3.5)
    + s('path', d='M84 116 Q100 126 116 116', stroke_width=2.5)
)

# 10. rhino (gray, big horn)
R = '#b9a99c'
ITEMS['rhino'] = (
    sit(R, None, cy=152, rx=42, ry=28)
    + z('ellipse', R, cx=72, cy=54, rx=9, ry=13, transform='rotate(-25 72 54)') + z('ellipse', R, cx=128, cy=54, rx=9, ry=13, transform='rotate(25 128 54)')
    + z('ellipse', R, cx=100, cy=86, rx=36, ry=32)
    + z('ellipse', R, cx=100, cy=112, rx=30, ry=18)
    + z('path', '#f4f4f0', d='M88 106 Q92 80 112 62 Q108 84 114 106Z')
    + dot(78, 82) + dot(122, 82) + cheeks(72, 128, 96, 5, 3)
    + dot(88, 112, 2.5) + dot(112, 112, 2.5) + smile(100, 118)
)

# 11. monkey with banana
M = '#9a6a3f'; MF = '#f6e0c4'
ITEMS['monkey'] = (
    thick('M132 170 Q172 168 166 134 Q162 120 150 126', M, 6)
    + sit(M, MF, cy=150, rx=34, ry=30)
    + z('circle', M, cx=62, cy=86, r=14) + z('circle', M, cx=138, cy=86, r=14)
    + s('circle', MF, cx=62, cy=86, r=7, stroke='none') + s('circle', MF, cx=138, cy=86, r=7, stroke='none')
    + z('circle', M, cx=100, cy=84, r=34)
    + s('path', MF, d='M100 76 Q90 62 80 70 Q70 80 76 96 Q82 114 100 114 Q118 114 124 96 Q130 80 120 70 Q110 62 100 76Z', stroke='none')
    + dot(89, 84) + dot(111, 84) + cheeks(80, 120, 97, 5, 3)
    + dot(96, 96, 1.8) + dot(104, 96, 1.8) + smile(100, 102, 6)
    + z('path', '#ffe27a', d='M116 152 Q148 146 152 116 Q156 118 156 122 Q156 152 120 160Z')
    + s('path', d='M152 116 L154 110', stroke_width=4)
    + z('ellipse', M, cx=124, cy=154, rx=9, ry=7)
)

# 12. gorilla
GR = '#5b6b7a'; GF = '#b9a99c'
ITEMS['gorilla'] = (
    z('path', GR, d='M48 176 Q42 120 70 108 L130 108 Q158 120 152 176Z')
    + s('ellipse', GF, cx=100, cy=148, rx=24, ry=22, stroke='none')
    + z('path', GR, d='M58 116 Q38 140 44 174 L64 174 Q62 146 74 128Z')
    + z('path', GR, d='M142 116 Q162 140 156 174 L136 174 Q138 146 126 128Z')
    + z('ellipse', GF, cx=54, cy=176, rx=13, ry=8) + z('ellipse', GF, cx=146, cy=176, rx=13, ry=8)
    + z('path', GR, d='M66 92 Q64 48 100 40 Q136 48 134 92 Q132 122 100 124 Q68 122 66 92Z')
    + z('path', GF, d='M76 88 Q78 74 100 76 Q122 74 124 88 Q128 116 100 118 Q72 116 76 88Z')
    + s('path', GR, d='M74 82 Q86 72 100 80 Q114 72 126 82 Q114 84 100 86 Q86 84 74 82Z', stroke_width=2.5)
    + dot(89, 90) + dot(111, 90) + cheeks(82, 118, 102, 5, 3)
    + dot(96, 100, 2) + dot(104, 100, 2) + smile(100, 108, 6)
)

# 13. kangaroo with a joey (side view, facing right)
K = '#d9a66b'; KB = '#f6e0c4'
ITEMS['kangaroo'] = (
    z('path', K, d='M78 148 Q52 168 28 174 Q50 184 86 168Z')
    + z('ellipse', K, cx=110, cy=178, rx=28, ry=7)
    + z('ellipse', K, cx=98, cy=128, rx=34, ry=46)
    + s('ellipse', KB, cx=108, cy=136, rx=20, ry=30, stroke='none')
    + z('ellipse', K, cx=84, cy=164, rx=20, ry=13)
    + z('ellipse', K, cx=104, cy=36, rx=7, ry=16, transform='rotate(-15 104 36)')
    + z('ellipse', K, cx=118, cy=34, rx=7, ry=16, transform='rotate(12 118 34)')
    + z('ellipse', K, cx=122, cy=64, rx=26, ry=19)
    + dot(124, 58) + dot(146, 62, 3.5) + f'<ellipse cx="130" cy="72" rx="6" ry="3.5" fill="{CH}" stroke="none"/>'
    + s('path', d='M138 72 Q142 76 146 72', stroke_width=2.5)
    + z('ellipse', K, cx=104, cy=108, rx=4, ry=8, transform='rotate(-20 104 108)')
    + z('ellipse', K, cx=118, cy=106, rx=4, ry=8, transform='rotate(20 118 106)')
    + z('circle', K, cx=112, cy=120, r=12)
    + dot(108, 118, 2.5) + dot(118, 118, 2.5) + dot(114, 124, 1.8)
    + z('path', KB, d='M88 124 Q108 132 130 122 Q132 152 110 158 Q90 154 88 124Z')
    + thick('M124 92 Q138 100 140 112', K, 7)
)

# 14. koala on a branch
KO = '#b9a99c'
ITEMS['koala'] = (
    z('ellipse', KO, cx=100, cy=138, rx=34, ry=30)
    + s('ellipse', '#f4f4f0', cx=100, cy=144, rx=18, ry=18, stroke='none')
    + z('circle', KO, cx=64, cy=66, r=19) + z('circle', KO, cx=136, cy=66, r=19)
    + s('circle', '#f4f4f0', cx=64, cy=66, r=10, stroke='none') + s('circle', '#f4f4f0', cx=136, cy=66, r=10, stroke='none')
    + z('circle', KO, cx=100, cy=86, r=33)
    + f'<ellipse cx="100" cy="92" rx="8" ry="10" fill="#5b6b7a"/>'
    + dot(84, 84) + dot(116, 84) + cheeks(76, 124, 98, 5, 3)
    + smile(100, 106, 4)
    + z('path', '#8b6b4f', d='M22 166 Q100 150 182 154 L182 168 Q100 164 22 180Z')
    + z('path', '#9ccf7a', d='M30 172 Q24 150 42 144 Q46 166 30 172Z')
    + z('path', '#9ccf7a', d='M170 160 Q168 140 184 134 Q188 156 170 160Z')
    + z('ellipse', KO, cx=76, cy=160, rx=11, ry=8) + z('ellipse', KO, cx=124, cy=158, rx=11, ry=8)
    + z('ellipse', KO, cx=92, cy=166, rx=9, ry=6) + z('ellipse', KO, cx=110, cy=165, rx=9, ry=6)
)

# 15. sloth hanging from a branch
SL = '#b9a99c'
ITEMS['sloth'] = (
    z('rect', '#8b6b4f', x=22, y=34, width=160, height=12, rx=6)
    + z('path', '#9ccf7a', d='M34 46 Q26 62 38 70 Q46 56 34 46Z') + z('path', '#9ccf7a', d='M166 46 Q160 64 172 70 Q178 56 166 46Z')
    + thick('M76 108 Q66 70 76 42', SL, 12) + thick('M124 108 Q134 70 124 42', SL, 12)
    + s('path', d='M70 34 Q76 28 82 36 M118 36 Q124 28 130 34', stroke_width=3)
    + z('ellipse', SL, cx=100, cy=142, rx=32, ry=36)
    + z('ellipse', SL, cx=82, cy=176, rx=10, ry=8) + z('ellipse', SL, cx=118, cy=176, rx=10, ry=8)
    + z('circle', SL, cx=100, cy=96, r=30)
    + s('ellipse', '#f6e0c4', cx=100, cy=100, rx=24, ry=20, stroke='none')
    + s('path', '#8b6b4f', d='M78 92 Q84 84 94 92 Q90 102 80 100Z M122 92 Q116 84 106 92 Q110 102 120 100Z', stroke='none')
    + dot(87, 94, 3) + dot(113, 94, 3)
    + f'<ellipse cx="100" cy="104" rx="4" ry="3" fill="{OUT}" stroke="none"/>'
    + cheeks(80, 120, 108, 5, 3) + smile(100, 110, 5)
)

# 16. fox
F = '#e8735a'; FW = '#f4f4f0'
ITEMS['fox'] = (
    z('path', F, d='M128 168 Q176 172 172 120 Q170 98 152 104 Q160 140 124 150Z')
    + s('path', FW, d='M164 104 Q172 106 172 120 Q170 132 166 136 Q156 120 152 106 Q158 102 164 104Z', stroke_width=2.5)
    + sit(F, FW, cy=146, rx=32, ry=32)
    + z('path', F, d='M70 70 L68 30 L96 54Z') + z('path', F, d='M130 70 L132 30 L104 54Z')
    + s('path', '#5b6b7a', d='M74 62 L72 40 L88 54Z', stroke='none') + s('path', '#5b6b7a', d='M126 62 L128 40 L112 54Z', stroke='none')
    + z('path', F, d='M64 80 Q64 52 100 50 Q136 52 136 80 Q134 106 100 118 Q66 106 64 80Z')
    + s('path', FW, d='M67 90 Q84 90 100 104 Q116 90 133 90 Q126 108 100 118 Q74 108 67 90Z', stroke='none')
    + dot(86, 82) + dot(114, 82) + cheeks(76, 124, 92, 5, 3)
    + f'<ellipse cx="100" cy="104" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + smile(100, 109, 4)
)

# 17. raccoon
RC = '#b9a99c'; RD = '#5b6b7a'
ITEMS['raccoon'] = (
    thick('M128 166 Q170 166 168 128', RC, 14)
    + s('path', d='M150 158 L150 168 M159 149 L167 156 M163 138 L173 138', stroke=RD, stroke_width=5)
    + sit(RC, '#f4f4f0', cy=148, rx=36, ry=32, fcol=RD)
    + z('path', RC, d='M70 72 L70 42 L92 56Z') + z('path', RC, d='M130 72 L130 42 L108 56Z')
    + s('path', RD, d='M74 64 L74 50 L86 57Z', stroke='none') + s('path', RD, d='M126 64 L126 50 L114 57Z', stroke='none')
    + z('circle', RC, cx=100, cy=88, r=34)
    + s('path', '#f4f4f0', d='M72 98 Q84 92 100 98 Q116 92 128 98 Q124 116 100 120 Q76 116 72 98Z', stroke='none')
    + s('path', RD, d='M68 86 Q74 74 92 80 Q100 84 108 80 Q126 74 132 86 Q128 98 114 96 Q100 92 86 96 Q72 98 68 86Z', stroke='none')
    + dot(86, 86, 5, '#ffffff') + dot(114, 86, 5, '#ffffff') + dot(86, 86, 3) + dot(114, 86, 3)
    + cheeks(76, 124, 104, 5, 3)
    + f'<ellipse cx="100" cy="104" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + mouth_w(100, 109)
)

# 18. deer with antlers
D = '#d9a66b'; DA = '#9a6a3f'
ITEMS['deer'] = (
    sit(D, '#f6e0c4', cy=152, rx=34, ry=28, fcol=DA)
    + dot(74, 138, 3.5, '#f4f4f0') + dot(126, 138, 3.5, '#f4f4f0') + dot(78, 152, 3, '#f4f4f0') + dot(122, 152, 3, '#f4f4f0')
    + thick('M86 62 Q72 44 66 26 M74 46 Q60 44 52 36', DA, 5)
    + thick('M114 62 Q128 44 134 26 M126 46 Q140 44 148 36', DA, 5)
    + z('ellipse', D, cx=62, cy=76, rx=16, ry=8, transform='rotate(-20 62 76)')
    + z('ellipse', D, cx=138, cy=76, rx=16, ry=8, transform='rotate(20 138 76)')
    + s('ellipse', '#f6e0c4', cx=62, cy=76, rx=9, ry=4, transform='rotate(-20 62 76)', stroke='none')
    + s('ellipse', '#f6e0c4', cx=138, cy=76, rx=9, ry=4, transform='rotate(20 138 76)', stroke='none')
    + z('ellipse', D, cx=100, cy=92, rx=30, ry=34)
    + s('ellipse', '#f6e0c4', cx=100, cy=110, rx=17, ry=12, stroke='none')
    + dot(88, 88) + dot(112, 88) + cheeks(80, 120, 100, 5, 3)
    + f'<ellipse cx="100" cy="106" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + smile(100, 112, 4)
)

# 19. squirrel holding an acorn
SQ = '#d9a66b'
ITEMS['squirrel'] = (
    z('path', SQ, d='M120 170 Q170 172 172 120 Q174 70 140 52 Q118 44 112 66 Q132 64 144 84 Q156 110 126 140Z')
    + s('path', d='M138 160 Q160 140 158 110', stroke='#f6e0c4', stroke_width=4)
    + sit(SQ, '#f6e0c4', cy=148, rx=32, ry=30)
    + z('path', SQ, d='M72 74 L74 46 L92 62Z') + z('path', SQ, d='M128 74 L126 46 L108 62Z')
    + s('path', '#f6a6b8', d='M77 66 L78 54 L86 62Z', stroke='none') + s('path', '#f6a6b8', d='M123 66 L122 54 L114 62Z', stroke='none')
    + z('circle', SQ, cx=100, cy=90, r=30)
    + s('ellipse', '#f6e0c4', cx=100, cy=104, rx=14, ry=9, stroke='none')
    + dot(89, 88) + dot(111, 88) + cheeks(80, 120, 100, 5, 3)
    + f'<ellipse cx="100" cy="100" rx="3.5" ry="2.5" fill="{OUT}" stroke="none"/>'
    + mouth_w(100, 104)
    + z('ellipse', '#f5d58a', cx=100, cy=144, rx=12, ry=15)
    + z('path', '#8b6b4f', d='M86 136 Q86 122 100 122 Q114 122 114 136Z') + s('path', d='M100 122 L102 115', stroke_width=3)
    + s('path', d='M90 128 L110 128 M88 132 L112 132', stroke_width=1.5)
    + z('ellipse', SQ, cx=84, cy=146, rx=8, ry=10) + z('ellipse', SQ, cx=116, cy=146, rx=8, ry=10)
)

# 20. wolf
WO = '#8b9aa8'; WL = '#e8e1d8'
WO = '#5b6b7a'; WL = '#c9d3db'
ITEMS['wolf'] = (
    z('path', WO, d='M128 168 Q178 170 172 126 Q168 110 156 114 Q160 146 124 152Z')
    + s('path', WL, d='M160 114 Q170 116 172 126 Q172 134 168 140 Q160 128 156 116Z', stroke_width=2.5)
    + sit(WO, WL, cy=148, rx=32, ry=32)
    + z('path', WO, d='M70 72 L70 30 L96 54Z') + z('path', WO, d='M130 72 L130 30 L104 54Z')
    + s('path', WL, d='M75 62 L75 42 L88 55Z', stroke='none') + s('path', WL, d='M125 62 L125 42 L112 55Z', stroke='none')
    + z('path', WO, d='M62 82 Q62 52 100 50 Q138 52 138 82 Q134 102 120 108 L100 120 L80 108 Q66 102 62 82Z')
    + s('path', WL, d='M66 92 Q86 86 100 96 Q114 86 134 92 Q130 102 118 108 L100 120 L82 108 Q70 102 66 92Z', stroke='none')
    + s('path', WL, d='M92 54 L100 74 L108 54Z', stroke='none')
    + dot(86, 82) + dot(114, 82) + cheeks(76, 124, 94, 5, 3)
    + f'<ellipse cx="100" cy="104" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + smile(100, 110, 4)
)
