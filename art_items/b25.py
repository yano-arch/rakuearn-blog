from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}


def kao(cx, cy, gap=11, r=3.5, cg=None, cdy=10, crx=6, cry=3.5, mouth=True, mw=5):
    """dot eyes + pink cheeks + small smile"""
    cg = cg if cg is not None else gap + 9
    o = dot(cx - gap, cy, r) + dot(cx + gap, cy, r) + cheeks(cx - cg, cx + cg, cy + cdy, crx, cry)
    if mouth:
        o += s('path', d=f'M{cx-mw} {cy+8} Q{cx} {cy+13} {cx+mw} {cy+8}', stroke_width=2.5)
    return o


def tube(d, color, w):
    return s('path', d=d, stroke_width=w + 6) + s('path', d=d, stroke=color, stroke_width=w)


# 1. firefly glowing
ITEMS['firefly'] = (
    s('circle', cx=100, cy=146, r=40, stroke='#ffe27a', stroke_width=3)
    + s('circle', cx=100, cy=146, r=48, stroke='#ffe27a', stroke_width=2, stroke_dasharray='4 8')
    + z('ellipse', '#c9d3db', cx=68, cy=104, rx=16, ry=30, transform='rotate(35 68 104)')
    + z('ellipse', '#c9d3db', cx=132, cy=104, rx=16, ry=30, transform='rotate(-35 132 104)')
    + z('circle', '#ffe27a', cx=100, cy=146, r=28)
    + z('ellipse', '#5b6b7a', cx=100, cy=112, rx=24, ry=16)
    + s('path', d='M88 56 Q80 38 70 34 M112 56 Q120 38 130 34', stroke_width=3)
    + dot(70, 34, 4) + dot(130, 34, 4)
    + z('circle', '#e8735a', cx=100, cy=78, r=26)
    + kao(100, 78, 10, cg=17, cdy=9, crx=5, cry=3)
    + s('path', d='M42 150 L32 150 M158 150 L168 150 M58 186 L50 192 M142 186 L150 192', stroke='#ffc94d', stroke_width=3)
)

# 2. cicada on a tree
ITEMS['cicada'] = (
    z('rect', '#9a6a3f', x=68, y=18, width=64, height=170, rx=6)
    + s('path', d='M80 30 L82 60 M120 150 L118 180 M124 40 L122 56', stroke_width=2)
    + z('path', '#c9d3db', d='M90 92 Q50 110 58 172 Q74 178 96 130Z')
    + z('path', '#c9d3db', d='M110 92 Q150 110 142 172 Q126 178 104 130Z')
    + s('path', d='M86 110 Q72 130 66 164 M114 110 Q128 130 134 164', stroke_width=2)
    + z('ellipse', '#7cc4a0', cx=100, cy=126, rx=18, ry=40)
    + s('path', d='M86 140 L114 140 M88 152 L112 152 M91 163 L109 163', stroke_width=2)
    + z('ellipse', '#7cc4a0', cx=100, cy=80, rx=30, ry=20)
    + z('circle', '#5b6b7a', cx=70, cy=76, r=8) + z('circle', '#5b6b7a', cx=130, cy=76, r=8)
    + kao(100, 80, 9, cg=16, cdy=7, crx=5, cry=3, mw=4)
)

# 3. grasshopper
ITEMS['grasshopper'] = (
    s('path', d='M28 170 L176 170', stroke_width=2.5)
    + s('path', d='M62 126 L52 168 M84 134 L80 168', stroke_width=4)
    + z('ellipse', '#9ccf7a', cx=108, cy=124, rx=54, ry=20, transform='rotate(-8 108 124)')
    + s('path', d='M120 108 Q140 106 162 116', stroke_width=2)
    + z('path', '#7cc4a0', d='M100 120 Q126 62 150 76 Q158 90 172 166 L162 168 Q144 104 138 98 Q124 118 116 132Z')
    + s('path', d='M54 84 Q40 50 60 26 M64 82 Q60 50 82 30', stroke_width=2.5)
    + z('circle', '#9ccf7a', cx=60, cy=106, r=26)
    + dot(52, 102, 4) + cheeks(44, 66, 114, 5, 3)
    + s('path', d='M46 120 Q51 124 56 120', stroke_width=2.5)
)

# 4. cute spider on a web
web = ''.join(s('path', d=f'M100 92 L{x} {y}', stroke_width=2) for x, y in
              ((100, 22), (162, 40), (182, 96), (160, 156), (40, 156), (18, 96), (38, 40)))
for rr in (30, 50, 70):
    pts = []
    for x, y in ((100, 22), (162, 40), (182, 96), (160, 156), (40, 156), (18, 96), (38, 40)):
        dx, dy = x - 100, y - 92
        L = (dx * dx + dy * dy) ** 0.5
        pts.append((100 + dx * rr / L, 92 + dy * rr / L))
    d = 'M' + ' L'.join(f'{px:.1f} {py:.1f}' for px, py in pts[:5]) + ' M' + ' L'.join(f'{px:.1f} {py:.1f}' for px, py in pts[4:] + pts[:1])
    web += s('path', d=d, stroke_width=2)
legs = ''
for sgn in (-1, 1):
    for i, (a, b) in enumerate(((-16, -34), (-2, -16), (12, 2), (24, 22))):
        x1 = 100 + sgn * 22
        legs += s('path', d=f'M{x1} {128+a//2} Q{100+sgn*46} {118+a} {100+sgn*54} {136+b}', stroke_width=4)
ITEMS['spider'] = (
    web + s('path', d='M100 22 L100 96', stroke_width=2)
    + legs
    + z('ellipse', '#8fb3e0', cx=100, cy=148, rx=26, ry=24)
    + z('circle', '#8fb3e0', cx=100, cy=118, r=26)
    + kao(100, 118, 9, cg=16, cdy=8, crx=5, cry=3, mw=4)
    + s('circle', '#f4f4f0', cx=100, cy=152, r=6, stroke_width=2)
)

# 5. friendly snake (coiled)
ITEMS['snake'] = (
    z('path', '#9ccf7a', d='M150 162 Q176 166 182 152 Q176 176 150 176Z')
    + z('ellipse', '#9ccf7a', cx=100, cy=162, rx=60, ry=18)
    + z('ellipse', '#9ccf7a', cx=100, cy=140, rx=46, ry=16)
    + z('ellipse', '#9ccf7a', cx=100, cy=120, rx=32, ry=14)
    + dot(70, 164, 4, '#7cc4a0') + dot(100, 170, 4, '#7cc4a0') + dot(130, 164, 4, '#7cc4a0')
    + dot(80, 146, 4, '#7cc4a0') + dot(120, 146, 4, '#7cc4a0')
    + z('path', '#9ccf7a', d='M88 122 Q82 96 96 82 L118 86 Q106 100 112 122Z')
    + s('path', d='M134 72 L146 76 M146 76 L152 72 M146 76 L151 81', stroke='#e04b5a', stroke_width=2.5)
    + z('ellipse', '#9ccf7a', cx=104, cy=66, rx=32, ry=24)
    + kao(104, 64, 11, cg=19, cdy=9, crx=5, cry=3)
)

# 6. crocodile
ITEMS['crocodile'] = (
    z('path', '#7cc4a0', d='M70 118 Q40 116 22 138 Q48 140 72 146Z')
    + z('ellipse', '#7cc4a0', cx=66, cy=152, rx=10, ry=8) + z('ellipse', '#7cc4a0', cx=118, cy=152, rx=10, ry=8)
    + z('ellipse', '#7cc4a0', cx=94, cy=130, rx=42, ry=22)
    + s('path', d='M70 110 l6 -8 l6 8 M88 108 l6 -8 l6 8 M106 110 l6 -8 l6 8', stroke_width=2.5)
    + z('rect', '#7cc4a0', x=112, y=110, width=68, height=32, rx=14)
    + s('path', d='M120 128 Q150 134 176 126', stroke_width=2.5)
    + s('path', '#ffffff', d='M134 130 l3 6 l3 -5 Z M148 132 l3 6 l3 -6 Z M162 131 l3 6 l3 -6Z', stroke_width=1.5)
    + dot(170, 118, 2.5)
    + z('circle', '#7cc4a0', cx=128, cy=106, r=12)
    + dot(130, 104, 4) + cheeks(122, 146, 118, 5, 3)
)

# 7. chameleon on a branch
ITEMS['chameleon'] = (
    z('path', '#9a6a3f', d='M20 150 L180 142 L180 154 L20 162Z')
    + s('path', d='M150 146 L166 128', stroke_width=4)
    + z('path', '#9ccf7a', d='M162 130 Q172 118 166 112 Q158 116 162 130Z')
    + tube('M60 120 Q34 130 36 104 Q40 86 56 92 Q66 100 56 108 Q48 110 50 102', '#9ccf7a', 10)
    + s('path', d='M74 132 L68 152 M128 132 L134 150', stroke_width=5)
    + z('path', '#9ccf7a', d='M54 120 Q60 82 100 82 Q140 82 146 112 Q130 138 100 138 Q70 138 54 120Z')
    + s('path', d='M76 100 Q100 90 124 100', stroke='#7cc4a0', stroke_width=3)
    + s('path', d='M78 116 Q100 108 122 116', stroke='#7cc4a0', stroke_width=3)
    + z('path', '#9ccf7a', d='M120 104 Q126 70 150 72 Q170 82 168 108 Q150 122 122 116Z')
    + z('circle', '#f5d58a', cx=146, cy=94, r=12)
    + dot(149, 94, 4) + cheeks(158, 158, 110, 5, 3)
    + s('path', d='M154 114 Q160 118 166 112', stroke_width=2.5)
    + dot(84, 152, 5, OUT) + dot(116, 150, 5, OUT)
)

# 8. friendly dinosaur (long neck)
ITEMS['dinosaur'] = (
    z('path', '#7cc4b0', d='M140 130 Q170 140 184 166 Q160 162 132 152Z')
    + z('rect', '#7cc4b0', x=76, y=148, width=18, height=32, rx=6) + z('rect', '#7cc4b0', x=120, y=148, width=18, height=32, rx=6)
    + z('path', '#7cc4b0', d='M76 118 Q60 80 62 56 L88 56 Q86 86 110 112Z')
    + z('ellipse', '#7cc4b0', cx=106, cy=136, rx=46, ry=30)
    + s('circle', '#9ccf7a', cx=96, cy=124, r=7, stroke_width=2) + s('circle', '#9ccf7a', cx=118, cy=134, r=5, stroke_width=2)
    + s('circle', '#9ccf7a', cx=128, cy=118, r=6, stroke_width=2)
    + z('ellipse', '#7cc4b0', cx=66, cy=48, rx=30, ry=22)
    + kao(62, 46, 10, cg=17, cdy=9, crx=5, cry=3)
)

# 9. fluffy baby penguin
ITEMS['penguin-chick'] = (
    z('ellipse', '#ffc94d', cx=82, cy=180, rx=14, ry=6) + z('ellipse', '#ffc94d', cx=118, cy=180, rx=14, ry=6)
    + z('ellipse', '#b9a99c', cx=56, cy=132, rx=11, ry=24, transform='rotate(20 56 132)')
    + z('ellipse', '#b9a99c', cx=144, cy=132, rx=11, ry=24, transform='rotate(-20 144 132)')
    + z('path', '#b9a99c', d='M100 54 Q154 56 152 124 Q152 176 100 178 Q48 176 48 124 Q46 56 100 54Z')
    + s('path', '#b9a99c', d='M92 56 Q94 40 100 44 Q104 36 110 56', stroke_width=3)
    + s('path', '#5b6b7a', d='M60 96 Q62 60 100 58 Q138 60 140 96 Q120 80 100 82 Q80 80 60 96Z', stroke='none')
    + s('path', '#f4f4f0', d='M64 104 Q66 82 100 82 Q134 82 136 104 Q134 132 100 134 Q66 132 64 104Z', stroke_width=2.5)
    + kao(100, 104, 14, cg=22, cdy=10, crx=6, cry=3.5, mouth=False)
    + s('path', '#5b6b7a', d='M94 112 L106 112 L100 120Z', stroke_width=2)
    + s('path', d='M80 150 l4 4 M100 156 l0 5 M120 150 l-4 4', stroke_width=2)
)

# 10. swallow flying
ITEMS['swallow-bird'] = (
    z('path', '#5b6b7a', d='M96 114 Q80 150 44 170 Q96 162 124 116Z')
    +     z('path', '#5b6b7a', d='M70 110 L24 88 Q36 108 30 132 L76 120Z')
    + z('path', '#5b6b7a', d='M88 100 Q90 50 60 26 Q126 40 124 100Z')
    + z('path', '#f4f4f0', d='M66 118 Q100 150 150 120 Q130 106 100 106 Q80 106 66 118Z')
    + z('path', '#5b6b7a', d='M64 116 Q90 90 136 96 Q166 98 170 112 Q160 122 150 120 Q110 112 64 116Z')
    + s('path', '#e8735a', d='M150 120 Q166 124 170 112 Q162 104 150 108Z', stroke_width=2.5)
    + s('path', '#5b6b7a', d='M170 106 L182 108 L170 112Z', stroke_width=2)
    + dot(156, 104, 3.5, '#ffffff')
)

# 11. mole popping out of the ground
ITEMS['mole'] = (
    s('path', d='M22 176 L178 176', stroke_width=2.5)
    + z('path', '#b9a99c', d='M58 150 Q56 70 100 68 Q144 70 142 150Z')
    + s('path', d='M88 70 L86 60 M100 68 L100 58 M112 70 L114 60', stroke_width=2)
    + kao(100, 104, 14, cg=24, cdy=12, crx=6, cry=3.5, mouth=False)
    + z('ellipse', '#f6a6b8', cx=100, cy=118, rx=11, ry=8)
    + s('path', d='M94 130 Q100 134 106 130', stroke_width=2.5)
    + z('path', '#9a6a3f', d='M30 176 Q40 138 72 140 Q100 132 128 140 Q160 138 170 176Z')
    + dot(60, 160, 3, '#8b6b4f') + dot(100, 152, 3, '#8b6b4f') + dot(140, 162, 3, '#8b6b4f') + dot(84, 166, 3, '#8b6b4f')
    + z('ellipse', '#f6a6b8', cx=68, cy=142, rx=13, ry=9) + z('ellipse', '#f6a6b8', cx=132, cy=142, rx=13, ry=9)
    + s('path', d='M60 134 L58 128 M68 133 L68 126 M76 134 L78 128 M124 134 L122 128 M132 133 L132 126 M140 134 L142 128', stroke_width=2)
    + s('path', '#9ccf7a', d='M160 176 L156 160 L164 168 L168 154 L172 176Z', stroke_width=2)
)

# 12. lobster
ITEMS['lobster'] = (
    s('path', d='M88 70 Q70 40 40 30 M112 70 Q130 40 160 30', stroke_width=2.5)
    + s('path', d='M78 112 L56 122 M78 124 L58 136 M122 112 L144 122 M122 124 L142 136', stroke_width=4)
    + s('path', d='M80 92 Q60 90 54 72 M120 92 Q140 90 146 72', stroke_width=6)
    + z('path', '#e8735a', d='M52 76 Q30 70 30 46 Q34 30 50 32 L50 52 L62 44 Q72 62 52 76Z')
    + z('path', '#e8735a', d='M148 76 Q170 70 170 46 Q166 30 150 32 L150 52 L138 44 Q128 62 148 76Z')
    + z('path', '#e8735a', d='M80 156 L120 156 L132 182 L100 176 L68 182Z')
    + z('rect', '#e8735a', x=80, y=136, width=40, height=22, rx=8)
    + z('rect', '#e8735a', x=78, y=118, width=44, height=22, rx=8)
    + z('ellipse', '#e8735a', cx=100, cy=96, rx=28, ry=30)
    + kao(100, 92, 10, cg=17, cdy=10, crx=5, cry=3)
)

# 13. puppy and kitten together
ITEMS['puppy-kitten-friends'] = (
    # puppy (left)
    z('ellipse', '#d9a66b', cx=66, cy=150, rx=30, ry=30)
    + z('ellipse', '#d9a66b', cx=56, cy=178, rx=9, ry=5) + z('ellipse', '#d9a66b', cx=78, cy=178, rx=9, ry=5)
    + z('circle', '#d9a66b', cx=64, cy=100, r=27)
    + z('path', '#9a6a3f', d='M40 86 Q28 106 36 122 Q48 112 48 88Z') + z('path', '#9a6a3f', d='M88 86 Q100 106 92 122 Q80 112 80 88Z')
    + dot(55, 100) + dot(73, 100) + f'<ellipse cx="64" cy="110" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>'
    + cheeks(46, 82, 114, 5, 3) + s('path', d='M58 117 Q64 122 70 117', stroke_width=2.5)
    # kitten (right)
    + s('path', d='M152 170 Q186 166 176 136', stroke_width=11) + s('path', d='M152 170 Q186 166 176 136', stroke='#b9a99c', stroke_width=5)
    + z('ellipse', '#b9a99c', cx=136, cy=152, rx=28, ry=28)
    + z('ellipse', '#b9a99c', cx=126, cy=178, rx=9, ry=5) + z('ellipse', '#b9a99c', cx=146, cy=178, rx=9, ry=5)
    + z('path', '#b9a99c', d='M114 92 L114 64 L134 80Z') + z('path', '#b9a99c', d='M160 92 L160 64 L140 80Z')
    + z('circle', '#b9a99c', cx=137, cy=104, r=26)
    + s('path', d='M131 80 L132 88 M137 79 L137 88 M143 80 L142 88', stroke_width=2)
    + dot(128, 104) + dot(146, 104) + cheeks(120, 154, 115, 5, 3)
    + s('path', '#f6a6b8', d='M134 110 L140 110 L137 113Z', stroke_width=1.5)
    + s('path', d='M132 116 Q134.5 119 137 116 Q139.5 119 142 116', stroke_width=2)
    + z('path', '#f07a8a', d='M100 72 C94 67 90 63 93 58 C96 54 100 57 100 61 C100 57 104 54 107 58 C110 63 106 67 100 72Z')
)

# 14. dog holding a bone
ITEMS['dog-bone'] = (
    z('ellipse', '#f6e0c4', cx=100, cy=150, rx=40, ry=34)
    + z('ellipse', '#f6e0c4', cx=86, cy=182, rx=12, ry=6) + z('ellipse', '#f6e0c4', cx=114, cy=182, rx=12, ry=6)
    + s('path', d='M138 160 Q164 150 158 124', stroke_width=3)
    + z('circle', '#f6e0c4', cx=100, cy=86, r=34)
    + z('path', '#d9a66b', d='M70 68 Q52 96 62 116 Q78 102 78 72Z') + z('path', '#d9a66b', d='M130 68 Q148 96 138 116 Q122 102 122 72Z')
    + s('circle', '#d9a66b', cx=114, cy=80, r=8, stroke='none')
    + dot(88, 82) + dot(112, 82) + f'<ellipse cx="100" cy="94" rx="6" ry="4" fill="{OUT}" stroke="none"/>'
    + cheeks(78, 122, 98, 6, 3.5)
    + z('circle', '#ffffff', cx=54, cy=104, r=7) + z('circle', '#ffffff', cx=54, cy=116, r=7)
    + z('circle', '#ffffff', cx=146, cy=104, r=7) + z('circle', '#ffffff', cx=146, cy=116, r=7)
    + z('rect', '#ffffff', x=54, y=102, width=92, height=14, rx=4)
)

# 15. cat in a cardboard box
ITEMS['cat-box'] = (
    z('path', '#d9a66b', d='M44 112 L24 92 L56 92 L64 112Z') + z('path', '#d9a66b', d='M156 112 L176 92 L144 92 L136 112Z')
    + z('path', '#b9a99c', d='M70 80 L72 46 L94 64Z') + z('path', '#b9a99c', d='M130 80 L128 46 L106 64Z')
    + s('path', '#f6a6b8', d='M76 68 L77 56 L86 64Z', stroke_width=2) + s('path', '#f6a6b8', d='M124 68 L123 56 L114 64Z', stroke_width=2)
    + z('circle', '#b9a99c', cx=100, cy=92, r=32)
    + s('path', d='M92 62 L94 72 M100 61 L100 72 M108 62 L106 72', stroke_width=2.5)
    + dot(88, 90) + dot(112, 90) + cheeks(78, 122, 102, 6, 3.5)
    + s('path', '#f6a6b8', d='M96 98 L104 98 L100 102Z', stroke_width=2)
    + s('path', d='M94 105 Q97 109 100 105 Q103 109 106 105', stroke_width=2.5)
    + s('path', d='M66 96 L54 93 M66 102 L54 104 M134 96 L146 93 M134 102 L146 104', stroke_width=2)
    + z('rect', '#d9a66b', x=44, y=112, width=112, height=68, rx=3)
    + s('path', d='M90 112 L90 130 M110 112 L110 130', stroke_width=2)
    + z('ellipse', '#b9a99c', cx=82, cy=114, rx=11, ry=7) + z('ellipse', '#b9a99c', cx=118, cy=114, rx=11, ry=7)
)

# 16. bird nest with eggs and mother bird
ITEMS['bird-nest'] = (
    z('path', '#9a6a3f', d='M20 150 L180 140 L180 150 L20 160Z')
    + z('ellipse', '#8fc7e8', cx=58, cy=118, rx=12, ry=15) + z('ellipse', '#8fc7e8', cx=80, cy=114, rx=12, ry=15)
    + dot(56, 112, 2, '#ffffff') + dot(78, 108, 2, '#ffffff')
    + z('path', '#f5b971', d='M120 118 Q114 90 132 84 L150 100 Z')
    + z('ellipse', '#f5b971', cx=124, cy=104, rx=28, ry=24)
    + z('path', '#e8735a', d='M106 104 Q120 92 136 104 Q124 116 106 104Z')
    + z('circle', '#f5b971', cx=144, cy=74, r=20)
    + z('path', '#ffc94d', d='M162 72 L176 76 L162 82Z')
    + dot(150, 72) + cheeks(156, 156, 84, 5, 3)
    + z('path', '#d9a66b', d='M34 116 Q36 152 100 152 Q164 152 166 116 Q100 128 34 116Z')
    + s('path', d='M42 126 Q70 136 100 132 M60 142 Q100 146 140 140 M108 130 Q140 132 160 124', stroke_width=2)
)

# 17. school of small fish
def fish(x, y, k, col):
    return (z('path', col, d=f'M{x-14*k} {y} L{x-26*k} {y-10*k} L{x-26*k} {y+10*k}Z')
            + z('ellipse', col, cx=x, cy=y, rx=18 * k, ry=11 * k)
            + dot(x + 9 * k, y - 2 * k, 2.6 * k + 0.6) + s('ellipse', CH, cx=x + 5 * k, cy=y + 4 * k, rx=3 * k, ry=2 * k, stroke='none'))
ITEMS['fish-school'] = (
    fish(150, 100, 1.4, '#f5b971')
    + fish(108, 70, 1, '#8fc7e8') + fish(110, 128, 1, '#8fc7e8')
    + fish(70, 46, 0.9, '#8fc7e8') + fish(66, 100, 0.9, '#8fc7e8') + fish(70, 154, 0.9, '#8fc7e8')
    + fish(40, 74, 0.8, '#8fb3e0') + fish(40, 128, 0.8, '#8fb3e0')
    + s('circle', '#ffffff', cx=178, cy=64, r=5, stroke_width=2) + s('circle', '#ffffff', cx=168, cy=46, r=3.5, stroke_width=2)
    + s('circle', '#ffffff', cx=176, cy=32, r=2.5, stroke_width=2)
)

# 18. mother duck with ducklings in a line
def duck(x, y, k, col, beak='#ffc94d'):
    return (z('ellipse', beak, cx=x - 6 * k, cy=y + 26 * k, rx=7 * k, ry=3 * k)
            + z('path', col, d=f'M{x-24*k} {y+2*k} L{x-32*k} {y-8*k} L{x-18*k} {y-6*k}Z')
            + z('ellipse', col, cx=x, cy=y + 4 * k, rx=24 * k, ry=18 * k)
            + s('path', d=f'M{x-12*k} {y+2*k} Q{x} {y+14*k} {x+12*k} {y+2*k}', stroke_width=2.5)
            + z('circle', col, cx=x + 14 * k, cy=y - 20 * k, r=13 * k)
            + z('path', beak, d=f'M{x+25*k} {y-22*k} L{x+36*k} {y-18*k} L{x+25*k} {y-14*k}Z')
            + dot(x + 18 * k, y - 22 * k, 2.5 * k + 0.8) + s('ellipse', CH, cx=x + 16 * k, cy=y - 13 * k, rx=4 * k, ry=2.5 * k, stroke='none'))
ITEMS['duckling-line'] = (
    s('path', d='M24 82 L64 82 M50 120 L104 120 M84 184 L184 184', stroke='#8fc7e8', stroke_width=3)
    + duck(40, 62, 0.62, '#ffe27a', '#f5b971')
    + duck(76, 98, 0.7, '#ffe27a', '#f5b971')
    + duck(132, 142, 1.5, '#f4f4f0')
)

# 19. paw prints
def paw(x, y, k, col, rot):
    return (f'<g transform="rotate({rot} {x} {y})">'
            + z('ellipse', col, cx=x, cy=y + 6 * k, rx=15 * k, ry=12 * k)
            + z('ellipse', col, cx=x - 15 * k, cy=y - 10 * k, rx=6 * k, ry=7.5 * k)
            + z('ellipse', col, cx=x - 5 * k, cy=y - 18 * k, rx=6 * k, ry=7.5 * k)
            + z('ellipse', col, cx=x + 7 * k, cy=y - 18 * k, rx=6 * k, ry=7.5 * k)
            + z('ellipse', col, cx=x + 17 * k, cy=y - 10 * k, rx=6 * k, ry=7.5 * k)
            + '</g>')
ITEMS['paw-print'] = (
    paw(54, 150, 1.1, '#d9a66b', -20)
    + paw(100, 104, 1.25, '#f6a6b8', 15)
    + paw(146, 60, 1.1, '#d9a66b', -10)
)

# 20. puffin
ITEMS['puffin'] = (
    z('path', '#ffc94d', d='M72 172 L60 182 L92 182 L88 172Z') + z('path', '#ffc94d', d='M112 172 L108 182 L140 182 L128 172Z')
    + z('ellipse', '#5b6b7a', cx=56, cy=128, rx=12, ry=30, transform='rotate(14 56 128)')
    + z('ellipse', '#5b6b7a', cx=144, cy=128, rx=12, ry=30, transform='rotate(-14 144 128)')
    + z('ellipse', '#5b6b7a', cx=100, cy=128, rx=44, ry=50)
    + s('ellipse', '#f4f4f0', cx=100, cy=140, rx=30, ry=34, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=100, cy=70, r=34)
    + s('path', '#f4f4f0', d='M72 76 Q72 52 100 52 Q128 52 128 76 Q124 96 100 96 Q76 96 72 76Z', stroke_width=2.5)
    + dot(86, 70) + dot(114, 70) + cheeks(80, 120, 84, 5, 3)
    + z('path', '#e8735a', d='M88 78 Q100 70 112 78 L104 104 Q100 108 96 104Z')
    + s('path', '#ffc94d', d='M91 84 Q100 80 109 84 L107 90 Q100 87 93 90Z', stroke='none')
)
