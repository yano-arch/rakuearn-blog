from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

def mouth_w(cx, cy):
    return s('path', d=f'M{cx-6} {cy} Q{cx-3} {cy+4} {cx} {cy} Q{cx+3} {cy+4} {cx+6} {cy}', stroke_width=2.5)

# 1. cat sitting, tail curled
ITEMS['cat-sitting'] = (
    s('path', d='M130 168 Q170 168 166 136 Q162 116 146 124', stroke_width=14)
    + s('path', d='M130 168 Q170 168 166 136 Q162 116 146 124', stroke='#f5b971', stroke_width=8)
    + z('ellipse', '#f5b971', cx=100, cy=142, rx=38, ry=38)
    + s('ellipse', '#f6e0c4', cx=100, cy=150, rx=20, ry=22, stroke_width=2)
    + z('ellipse', '#f5b971', cx=86, cy=178, rx=11, ry=7) + z('ellipse', '#f5b971', cx=114, cy=178, rx=11, ry=7)
    + z('path', '#f5b971', d='M70 76 L72 40 L98 58Z') + z('path', '#f5b971', d='M130 76 L128 40 L102 58Z')
    + s('path', '#f6a6b8', d='M76 64 L77 50 L88 58Z', stroke_width=2) + s('path', '#f6a6b8', d='M124 64 L123 50 L112 58Z', stroke_width=2)
    + z('circle', '#f5b971', cx=100, cy=86, r=32)
    + s('path', d='M92 56 L94 66 M100 55 L100 66 M108 56 L106 66', stroke_width=2.5)
    + dot(88, 86) + dot(112, 86) + cheeks(78, 122, 98, 6, 3.5)
    + s('path', '#f6a6b8', d='M96 94 L104 94 L100 98Z', stroke_width=2)
    + mouth_w(100, 100)
    + s('path', d='M66 92 L54 89 M66 98 L54 100 M134 92 L146 89 M134 98 L146 100', stroke_width=2)
)

# 2. rabbit
ITEMS['rabbit'] = (
    z('circle', '#f4f4f0', cx=136, cy=164, r=10)
    + z('ellipse', '#f4f4f0', cx=84, cy=56, rx=12, ry=30, transform='rotate(-10 84 56)')
    + z('ellipse', '#f4f4f0', cx=116, cy=56, rx=12, ry=30, transform='rotate(10 116 56)')
    + s('ellipse', '#f6a6b8', cx=84, cy=58, rx=5, ry=20, transform='rotate(-10 84 58)', stroke='none')
    + s('ellipse', '#f6a6b8', cx=116, cy=58, rx=5, ry=20, transform='rotate(10 116 58)', stroke='none')
    + z('ellipse', '#f4f4f0', cx=100, cy=148, rx=38, ry=32)
    + z('ellipse', '#f4f4f0', cx=84, cy=178, rx=12, ry=7) + z('ellipse', '#f4f4f0', cx=116, cy=178, rx=12, ry=7)
    + z('circle', '#f4f4f0', cx=100, cy=108, r=30)
    + dot(89, 106) + dot(111, 106) + cheeks(79, 121, 118, 6, 3.5)
    + s('ellipse', '#f6a6b8', cx=100, cy=114, rx=3.5, ry=2.5, stroke='none')
    + mouth_w(100, 118)
)

# 3. brown bear sitting
ITEMS['bear'] = (
    z('circle', '#9a6a3f', cx=72, cy=56, r=13) + z('circle', '#9a6a3f', cx=128, cy=56, r=13)
    + s('circle', '#d9a66b', cx=72, cy=56, r=6, stroke='none') + s('circle', '#d9a66b', cx=128, cy=56, r=6, stroke='none')
    + z('ellipse', '#9a6a3f', cx=100, cy=144, rx=44, ry=38)
    + s('ellipse', '#d9a66b', cx=100, cy=150, rx=24, ry=22, stroke='none')
    + z('ellipse', '#9a6a3f', cx=62, cy=140, rx=11, ry=16) + z('ellipse', '#9a6a3f', cx=138, cy=140, rx=11, ry=16)
    + z('ellipse', '#9a6a3f', cx=78, cy=176, rx=15, ry=10) + z('ellipse', '#9a6a3f', cx=122, cy=176, rx=15, ry=10)
    + s('ellipse', '#d9a66b', cx=78, cy=177, rx=7, ry=5, stroke='none') + s('ellipse', '#d9a66b', cx=122, cy=177, rx=7, ry=5, stroke='none')
    + z('circle', '#9a6a3f', cx=100, cy=84, r=34)
    + s('ellipse', '#f6e0c4', cx=100, cy=98, rx=14, ry=11, stroke_width=2.5)
    + dot(87, 82) + dot(113, 82) + cheeks(76, 124, 96, 6, 3.5)
    + f'<ellipse cx="100" cy="94" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + s('path', d='M95 101 Q100 105 105 101', stroke_width=2.5)
)

# 4. panda holding bamboo
DK = '#5b6b7a'
ITEMS['panda'] = (
    z('circle', DK, cx=72, cy=56, r=12) + z('circle', DK, cx=124, cy=56, r=12)
    + z('ellipse', '#ffffff', cx=96, cy=146, rx=40, ry=34)
    + z('ellipse', DK, cx=74, cy=176, rx=15, ry=9) + z('ellipse', DK, cx=118, cy=176, rx=15, ry=9)
    + z('ellipse', DK, cx=58, cy=140, rx=10, ry=15)
    + z('rect', '#9ccf7a', x=132, y=40, width=12, height=140, rx=3)
    + s('path', d='M132 76 L144 76 M132 112 L144 112 M132 148 L144 148', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M144 60 Q166 44 178 54 Q164 70 144 60Z')
    + z('path', '#7cc4a0', d='M132 92 Q112 80 104 88 Q116 102 132 92Z')
    + z('circle', '#ffffff', cx=98, cy=84, r=32)
    + s('ellipse', DK, cx=86, cy=84, rx=8, ry=10, transform='rotate(25 86 84)', stroke='none')
    + s('ellipse', DK, cx=110, cy=84, rx=8, ry=10, transform='rotate(-25 110 84)', stroke='none')
    + dot(87, 84, 3, '#ffffff') + dot(109, 84, 3, '#ffffff') + cheeks(76, 120, 98, 6, 3.5)
    + f'<ellipse cx="98" cy="96" rx="4.5" ry="3" fill="{OUT}" stroke="none"/>'
    + s('path', d='M93 102 Q98 106 103 102', stroke_width=2.5)
    + z('ellipse', DK, cx=136, cy=128, rx=13, ry=10)
)

# 5. penguin standing
ITEMS['penguin'] = (
    z('ellipse', '#ffc94d', cx=86, cy=178, rx=12, ry=6) + z('ellipse', '#ffc94d', cx=114, cy=178, rx=12, ry=6)
    + z('ellipse', DK, cx=58, cy=124, rx=10, ry=28, transform='rotate(18 58 124)')
    + z('ellipse', DK, cx=142, cy=124, rx=10, ry=28, transform='rotate(-18 142 124)')
    + z('ellipse', DK, cx=100, cy=112, rx=44, ry=64)
    + s('path', '#ffffff', d='M100 70 Q84 58 76 74 Q68 96 72 130 Q76 168 100 170 Q124 168 128 130 Q132 96 124 74 Q116 58 100 70Z', stroke_width=2.5)
    + dot(88, 88) + dot(112, 88) + cheeks(80, 120, 100, 6, 3.5)
    + z('path', '#ffc94d', d='M93 96 L107 96 L100 106Z')
)

# 6. owl on a branch
ITEMS['owl'] = (
    z('path', '#8b6b4f', d='M28 160 Q100 152 172 162 L172 172 Q100 164 28 172Z')
    + z('path', '#7cc4a0', d='M156 160 Q170 146 180 152 Q172 166 156 160Z')
    + z('path', '#d9a66b', d='M56 110 Q56 64 68 44 L84 62 Q100 56 116 62 L132 44 Q144 64 144 110 Q144 160 100 160 Q56 160 56 110Z')
    + s('ellipse', '#f6e0c4', cx=100, cy=130, rx=26, ry=26, stroke='none')
    + s('path', d='M90 124 Q94 128 98 124 M102 124 Q106 128 110 124 M96 138 Q100 142 104 138', stroke_width=2)
    + z('ellipse', '#9a6a3f', cx=62, cy=124, rx=10, ry=24) + z('ellipse', '#9a6a3f', cx=138, cy=124, rx=10, ry=24)
    + s('circle', '#ffffff', cx=84, cy=88, r=14, stroke_width=2.5) + s('circle', '#ffffff', cx=116, cy=88, r=14, stroke_width=2.5)
    + dot(84, 89, 4.5) + dot(116, 89, 4.5) + cheeks(76, 124, 108, 6, 3.5)
    + z('path', '#ffc94d', d='M94 100 L106 100 L100 110Z')
    + s('path', '#ffc94d', d='M86 160 L86 166 M92 160 L92 166 M108 160 L108 166 M114 160 L114 166', stroke_width=3)
)

# 7. goldfish with bubbles
ITEMS['goldfish'] = (
    z('path', '#e8735a', d='M124 112 Q158 66 176 82 Q160 112 176 142 Q158 158 124 112Z')
    + s('path', d='M140 100 Q156 92 166 90 M140 124 Q156 132 166 134', stroke_width=2)
    + z('path', '#f5b971', d='M70 88 Q90 56 118 76 Q106 82 96 88Z')
    + z('path', '#f5b971', d='M86 134 Q92 156 110 152 Q104 140 102 132Z')
    + z('ellipse', '#e8735a', cx=92, cy=112, rx=42, ry=30)
    + s('path', d='M98 104 Q104 112 98 120 M110 104 Q116 112 110 120', stroke_width=2)
    + dot(70, 106) + cheeks(72, 72, 120, 6, 3.5)
    + f'<circle cx="55" cy="116" r="3.5" fill="#c0504d" stroke-width="2.5"/>'
    + s('circle', '#ffffff', cx=44, cy=82, r=7, stroke_width=2.5)
    + s('circle', '#ffffff', cx=34, cy=58, r=5, stroke_width=2.5)
    + s('circle', '#ffffff', cx=48, cy=38, r=3.5, stroke_width=2)
)

# 8. frog sitting
FG = '#9ccf7a'
ITEMS['frog'] = (
    z('ellipse', FG, cx=56, cy=164, rx=18, ry=14) + z('ellipse', FG, cx=144, cy=164, rx=18, ry=14)
    + z('ellipse', FG, cx=100, cy=144, rx=44, ry=36)
    + s('ellipse', '#f5d58a', cx=100, cy=152, rx=26, ry=22, stroke='none')
    + z('circle', FG, cx=74, cy=68, r=16) + z('circle', FG, cx=126, cy=68, r=16)
    + z('ellipse', FG, cx=100, cy=100, rx=54, ry=30)
    + dot(74, 66, 4.5) + dot(126, 66, 4.5) + cheeks(66, 134, 106, 7, 4)
    + s('path', d='M84 104 Q100 116 116 104', stroke_width=3)
    + z('ellipse', FG, cx=80, cy=178, rx=13, ry=7) + z('ellipse', FG, cx=120, cy=178, rx=13, ry=7)
)

# 9. hamster holding a sunflower seed
HM = '#f5b971'
ITEMS['hamster'] = (
    z('circle', HM, cx=66, cy=76, r=12) + z('circle', HM, cx=134, cy=76, r=12)
    + s('circle', '#f6a6b8', cx=66, cy=76, r=6, stroke='none') + s('circle', '#f6a6b8', cx=134, cy=76, r=6, stroke='none')
    + z('ellipse', HM, cx=82, cy=176, rx=11, ry=6) + z('ellipse', HM, cx=118, cy=176, rx=11, ry=6)
    + z('ellipse', HM, cx=100, cy=124, rx=56, ry=52)
    + s('path', '#f6e0c4', d='M60 120 Q66 110 84 112 Q100 120 116 112 Q134 110 140 120 Q144 168 100 172 Q56 168 60 120Z', stroke='none')
    + dot(84, 104) + dot(116, 104) + cheeks(68, 132, 118, 7, 4)
    + s('ellipse', '#f6a6b8', cx=100, cy=112, rx=3.5, ry=2.5, stroke='none')
    + mouth_w(100, 116)
    + z('path', DK, d='M100 126 Q116 144 100 168 Q84 144 100 126Z')
    + s('path', d='M100 134 L100 160 M94 140 L94 154 M106 140 L106 154', stroke='#f4f4f0', stroke_width=2)
    + z('circle', HM, cx=84, cy=146, r=7) + z('circle', HM, cx=116, cy=146, r=7)
)

# 10. yellow baby chick
CK = '#ffe27a'
ITEMS['chick'] = (
    s('path', d='M86 166 L86 180 M80 182 L86 178 L92 182 M114 166 L114 180 M108 182 L114 178 L120 182', stroke='#e8735a', stroke_width=3.5)
    + z('path', CK, d='M96 62 Q90 44 100 40 Q102 52 106 50 Q112 40 118 48 Q108 54 106 64Z')
    + z('ellipse', CK, cx=100, cy=114, rx=50, ry=52)
    + z('path', CK, d='M54 120 Q42 136 62 146 Q70 136 66 122Z')
    + z('path', CK, d='M146 120 Q158 136 138 146 Q130 136 134 122Z')
    + dot(84, 106) + dot(116, 106) + cheeks(72, 128, 120, 7, 4)
    + z('path', '#f5b971', d='M92 114 L108 114 L100 124Z')
)
