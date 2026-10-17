from art import z, s, dot, cheeks, face, OUT, CH, at

ITEMS = {}
SK = '#ffd9b8'


def zr(tag, fill, ang, ox, oy, **a):
    """回転した図形のズレ塗り（ズレ方向は常に右下）"""
    sa = at(a)
    g = f'rotate({ang} {ox} {oy})'
    return (f'<g transform="translate(4 4)"><g transform="{g}"><{tag} {sa} fill="{fill}" stroke="none"/></g></g>'
            f'<g transform="{g}"><{tag} {sa} fill="none"/></g>')


def rg(ang, cx, cy, body):
    return f'<g transform="rotate({ang} {cx} {cy})">{body}</g>'


def thick(d, color, w=12, inner=7):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def plus(cx, cy, a, b):
    """十字（a=腕の半幅, b=腕の長さ）"""
    return (f'M{cx-a} {cy-b} L{cx+a} {cy-b} L{cx+a} {cy-a} L{cx+b} {cy-a} L{cx+b} {cy+a} L{cx+a} {cy+a} '
            f'L{cx+a} {cy+b} L{cx-a} {cy+b} L{cx-a} {cy+a} L{cx-b} {cy+a} L{cx-b} {cy-a} L{cx-a} {cy-a}Z')


def body(cx, top, color, w=34, bottom=180):
    return z('path', color, d=f'M{cx-w} {bottom} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bottom}Z')


def f2(cx, cy, hair, r=34, eyes='dot', mouth='smile', blush=CH, brx=7):
    k = r / 34

    def P(x, y):
        return f'{cx + x * k:.1f} {cy + y * k:.1f}'
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=f'M{P(-34,-2)} Q{P(-32,-36)} {P(0,-35)} Q{P(32,-36)} {P(34,-2)} Q{P(20,-18)} {P(0,-17)} Q{P(-20,-18)} {P(-34,-2)}Z')
    sw = 2.5 if k < 0.9 else 3
    if eyes == 'dot':
        o += dot(cx - 12 * k, cy + 2 * k, 3.5 * k) + dot(cx + 12 * k, cy + 2 * k, 3.5 * k)
    elif eyes == 'closed':
        o += s('path', d=f'M{P(-17,2)} Q{P(-12,7)} {P(-7,2)} M{P(7,2)} Q{P(12,7)} {P(17,2)}', stroke_width=sw)
    elif eyes == 'shut':
        o += s('path', d=f'M{P(-17,-3)} L{P(-8,2)} L{P(-17,7)} M{P(17,-3)} L{P(8,2)} L{P(17,7)}', stroke_width=sw)
    elif eyes == 'droop':
        o += s('path', d=f'M{P(-17,4)} Q{P(-12,0)} {P(-7,4)} M{P(7,4)} Q{P(12,0)} {P(17,4)}', stroke_width=sw)
        o += s('path', d=f'M{P(-18,-6)} L{P(-8,-9)} M{P(18,-6)} L{P(8,-9)}', stroke_width=2.5)
    elif eyes == 'sad':
        o += dot(cx - 12 * k, cy + 3 * k, 3.5 * k) + dot(cx + 12 * k, cy + 3 * k, 3.5 * k)
        o += s('path', d=f'M{P(-19,-5)} L{P(-8,-9)} M{P(19,-5)} L{P(8,-9)}', stroke_width=2.5)
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, brx * k, (brx - 3) * k * 0.9 + 0.6)  # ほっぺ
    o = o.replace(f'fill="{CH}"', f'fill="{blush}"') if blush != CH else o
    if mouth == 'smile':
        o += s('path', d=f'M{P(-6,16)} Q{P(0,21)} {P(6,16)}', stroke_width=sw)
    elif mouth == 'open':
        o += s('path', '#c0504d', d=f'M{P(-8,14)} Q{P(0,28)} {P(8,14)}Z', stroke_width=2.5)
    elif mouth == 'o':
        o += f'<circle cx="{cx}" cy="{cy + 18 * k:.1f}" r="{4 * k:.1f}" fill="#c0504d" stroke-width="2.5"/>'
    elif mouth == 'wavy':
        o += s('path', d=f'M{P(-9,18)} Q{P(-4.5,13)} {P(0,18)} Q{P(4.5,23)} {P(9,18)}', stroke_width=2.5)
    elif mouth == 'frown':
        o += s('path', d=f'M{P(-6,20)} Q{P(0,14)} {P(6,20)}', stroke_width=sw)
    return o


def drop(x, y, sc=1, c='#8fc7e8'):
    return s('path', c, d=f'M{x} {y} Q{x+6*sc} {y+9*sc} {x+6*sc} {y+12*sc} Q{x+6*sc} {y+18*sc} {x} {y+18*sc} '
             f'Q{x-6*sc} {y+18*sc} {x-6*sc} {y+12*sc} Q{x-6*sc} {y+9*sc} {x} {y}Z', stroke_width=2.5)


def bubble(x, y, r):
    return s('circle', '#ffffff', cx=x, cy=y, r=r, stroke_width=2.5) + s('path', d=f'M{x-r*0.5:.1f} {y-r*0.1:.1f} Q{x-r*0.45:.1f} {y-r*0.5:.1f} {x-r*0.05:.1f} {y-r*0.55:.1f}', stroke_width=1.8)


def puff(x, y, r, c='#f4f4f0'):
    return z('circle', c, cx=x, cy=y, r=r)


# 1. hospital
ITEMS['hospital'] = (
    z('rect', '#f4f4f0', x=70, y=32, width=60, height=44, rx=4)
    + z('circle', '#7cc4b0', cx=100, cy=52, r=14)
    + s('path', '#ffffff', d=plus(100, 52, 3.5, 9), stroke_width=2)
    + z('rect', '#f4f4f0', x=36, y=72, width=128, height=108, rx=3)
    + z('rect', '#7cc4b0', x=30, y=66, width=140, height=10, rx=3)
    + ''.join(s('rect', '#8fc7e8', x=x, y=y, width=16, height=16, rx=2, stroke_width=2.5)
              for y in (88, 114) for x in (48, 72, 112, 136))
    + ''.join(s('rect', '#8fc7e8', x=x, y=142, width=16, height=16, rx=2, stroke_width=2.5) for x in (48, 136))
    + s('rect', '#8fc7e8', x=92, y=88, width=16, height=16, rx=2, stroke_width=2.5)
    + s('rect', '#8fc7e8', x=92, y=114, width=16, height=16, rx=2, stroke_width=2.5)
    + z('rect', '#7cc4b0', x=76, y=136, width=48, height=8, rx=3)
    + z('rect', '#8fc7e8', x=82, y=144, width=36, height=36)
    + s('path', d='M100 144 L100 180', stroke_width=2.5)
    + z('ellipse', '#9ccf7a', cx=30, cy=172, rx=14, ry=10)
    + z('ellipse', '#9ccf7a', cx=168, cy=172, rx=14, ry=10)
    + s('path', d='M18 182 L182 182', stroke_width=2.5)
)

# 2. ambulance
ITEMS['ambulance'] = (
    z('rect', '#e04b5a', x=66, y=62, width=24, height=12, rx=4)
    + s('path', d='M62 56 L56 50 M78 54 L78 46 M94 56 L100 50', stroke_width=2.5)
    + z('path', '#f4f4f0', d='M26 152 L26 80 Q26 74 32 74 L126 74 L126 152Z')
    + z('path', '#f4f4f0', d='M124 92 L150 92 Q160 94 166 108 L174 122 L174 152 L124 152Z')
    + s('path', '#8fc7e8', d='M132 100 L148 100 Q155 102 160 120 L132 120Z', stroke_width=2.5)
    + s('rect', '#e8735a', x=26, y=128, width=148, height=9, stroke_width=2.5)
    + z('rect', '#7cc4b0', x=52, y=88, width=44, height=34, rx=4)
    + s('path', '#ffffff', d=plus(74, 105, 4, 11), stroke_width=2)
    + s('rect', '#ffc94d', x=166, y=140, width=8, height=7, rx=2, stroke_width=2)
    + z('circle', '#5b6b7a', cx=58, cy=154, r=15) + s('circle', '#c9d3db', cx=58, cy=154, r=6, stroke_width=2.5)
    + z('circle', '#5b6b7a', cx=144, cy=154, r=15) + s('circle', '#c9d3db', cx=144, cy=154, r=6, stroke_width=2.5)
    + s('path', d='M18 182 L182 182', stroke_width=2.5)
)

# 3. stethoscope
TUBE = 'M100 106 L100 140 Q100 174 126 174 Q150 174 150 148 L150 128'
ITEMS['stethoscope'] = (
    thick('M66 36 Q58 82 100 106', '#8fb3e0') + thick('M134 36 Q142 82 100 106', '#8fb3e0')
    + thick(TUBE, '#8fb3e0')
    + z('circle', '#5b6b7a', cx=66, cy=34, r=7) + z('circle', '#5b6b7a', cx=134, cy=34, r=7)
    + z('circle', '#c9d3db', cx=100, cy=106, r=8)
    + z('rect', '#c9d3db', x=144, y=120, width=12, height=10, rx=2)
    + z('circle', '#c9d3db', cx=150, cy=104, r=20)
    + s('circle', '#8fb3e0', cx=150, cy=104, r=12, stroke_width=2.5)
)

# 4. thermometer
ITEMS['thermometer'] = (
    z('rect', '#f4f4f0', x=84, y=26, width=32, height=128, rx=16)
    + s('rect', '#e04b5a', x=95, y=70, width=10, height=84, rx=3, stroke='none')
    + s('path', d='M95 74 L95 150 M105 74 L105 150 M95 74 Q100 68 105 74', stroke_width=2.5)
    + ''.join(s('path', d=f'M116 {y} L{108 if i % 2 else 110} {y}', stroke_width=2.5) for i, y in enumerate(range(44, 140, 12)))
    + z('circle', '#e04b5a', cx=100, cy=158, r=22)
    + dot(92, 158, 3) + dot(108, 158, 3) + cheeks(85, 115, 166, 4.5, 2.8, ) .replace(CH, '#f6a6b8')
    + s('path', d='M96 166 Q100 170 104 166', stroke_width=2.5)
    + s('path', d='M140 50 L150 44 M142 66 L154 66 M140 82 L150 88 M60 50 L50 44 M58 66 L46 66 M60 82 L50 88', stroke_width=2.5)
)

# 5. pills
ITEMS['pills'] = (
    zr('rect', '#f4f4f0', -20, 90, 68, x=40, y=50, width=100, height=36, rx=18)
    + rg(-20, 90, 68, s('path', '#e8735a', d='M90 50 L58 50 A18 18 0 0 0 58 86 L90 86Z') + s('path', d='M90 50 L90 86'))
    + rg(-20, 90, 68, dot(62, 66, 3) + dot(80, 66, 3) + s('path', d='M67 74 Q71 78 75 74', stroke_width=2.5))
    + z('circle', '#f4f4f0', cx=62, cy=142, r=26) + s('path', d='M42 142 L82 142', stroke_width=2.5)
    + zr('rect', '#ffe27a', 25, 136, 140, x=104, y=126, width=66, height=28, rx=14)
    + rg(25, 136, 140, s('path', '#8fb3e0', d='M137 126 L157 126 A14 14 0 0 1 157 154 L137 154Z') + s('path', d='M137 126 L137 154'))
    + z('circle', '#f6a6b8', cx=160, cy=78, r=15) + s('path', d='M150 78 L170 78', stroke_width=2.5)
    + z('circle', '#9ccf7a', cx=118, cy=176, r=9)
)

# 6. medicine bottle
ITEMS['medicine-bottle'] = (
    z('rect', '#d9a66b', x=56, y=70, width=88, height=110, rx=14)
    + z('rect', '#d9a66b', x=72, y=58, width=56, height=16, rx=3)
    + z('rect', '#f4f4f0', x=64, y=28, width=72, height=32, rx=6)
    + s('path', d='M78 34 L78 54 M92 34 L92 54 M108 34 L108 54 M122 34 L122 54', stroke_width=2.5)
    + s('rect', '#ffffff', x=66, y=98, width=68, height=56, rx=5)
    + s('path', '#7cc4b0', d=plus(100, 126, 5, 15), stroke_width=2.5)
    + s('path', d='M64 80 Q64 74 70 72', stroke='#f6e0c4', stroke_width=3)
    + z('circle', '#f4f4f0', cx=162, cy=170, r=11) + s('path', d='M155 170 L169 170', stroke_width=2)
    + zr('rect', '#f6a6b8', -30, 36, 168, x=22, y=161, width=28, height=14, rx=7)
)

# 7. vaccine (syringe + vial)
SA = -40
ITEMS['vaccine'] = (
    zr('rect', '#f4f4f0', SA, 92, 100, x=92 - 82, y=100 - 3, width=36, height=6, rx=2)
    + zr('rect', '#8fb3e0', SA, 92, 100, x=92 - 86, y=100 - 16, width=8, height=32, rx=3)
    + zr('rect', '#f4f4f0', SA, 92, 100, x=92 - 50, y=100 - 15, width=88, height=30, rx=4)
    + rg(SA, 92, 100, s('rect', '#8fc7e8', x=92 - 4, y=100 - 15, width=42, height=30, stroke='none')
         + s('path', d='M88 85 L88 115', stroke_width=2.5)
         + s('rect', x=92 - 50, y=100 - 15, width=88, height=30, rx=4)
         + ''.join(s('path', d=f'M{x} 85 L{x} 93', stroke_width=2) for x in (60, 74, 102, 116)))
    + zr('rect', '#c9d3db', SA, 92, 100, x=92 - 54, y=100 - 22, width=8, height=44, rx=3)
    + zr('rect', '#c9d3db', SA, 92, 100, x=92 + 38, y=100 - 7, width=12, height=14, rx=2)
    + rg(SA, 92, 100, s('path', d='M142 100 L174 100', stroke_width=2.5))
    + z('rect', '#f4f4f0', x=136, y=132, width=34, height=44, rx=6)
    + s('rect', '#8fc7e8', x=139, y=150, width=28, height=23, rx=3, stroke='none')
    + s('path', d='M139 150 L167 150', stroke_width=2.5)
    + z('rect', '#8fb3e0', x=140, y=120, width=26, height=14, rx=3)
)

# 8. bandage
BA = -28
ITEMS['bandage'] = (
    zr('rect', '#f5b971', BA, 100, 100, x=26, y=74, width=148, height=52, rx=26)
    + zr('rect', '#f6e0c4', BA, 100, 100, x=74, y=80, width=52, height=40, rx=6)
    + rg(BA, 100, 100, ''.join(dot(x, y, 2.2, '#d9a66b') for x in (44, 56) for y in (90, 110))
         + ''.join(dot(x, y, 2.2, '#d9a66b') for x in (144, 156) for y in (90, 110))
         + dot(90, 98, 3) + dot(110, 98, 3) + cheeks(83, 117, 106, 4.5, 2.8)
         + s('path', d='M96 106 Q100 110 104 106', stroke_width=2.5))
)

# 9. first aid kit
ITEMS['first-aid-kit'] = (
    s('path', d='M74 72 L74 52 Q74 44 82 44 L118 44 Q126 44 126 52 L126 72', stroke_width=11)
    + s('path', d='M74 72 L74 52 Q74 44 82 44 L118 44 Q126 44 126 52 L126 72', stroke='#5b6b7a', stroke_width=6)
    + z('rect', '#7cc4b0', x=30, y=68, width=140, height=108, rx=14)
    + s('path', d='M30 94 L170 94', stroke_width=2.5)
    + z('rect', '#c9d3db', x=92, y=88, width=16, height=12, rx=3)
    + z('path', '#ffffff', d=plus(100, 136, 8, 26))
)

# 10. face mask
ITEMS['face-mask'] = (
    s('path', d='M52 82 Q20 76 22 104 Q24 132 54 128', stroke_width=3)
    + s('path', d='M148 82 Q180 76 178 104 Q176 132 146 128', stroke_width=3)
    + z('path', '#ffffff', d='M50 74 Q100 58 150 74 L152 128 Q100 152 48 128Z')
    + s('path', d='M54 92 Q100 82 146 92 M54 108 Q100 100 146 108 M54 124 Q100 120 146 124', stroke_width=2.5, stroke='#b9a99c')
    + s('path', d='M80 72 Q100 66 120 72', stroke='#8fc7e8', stroke_width=3)
)

# 11. hand washing
ITEMS['hand-washing'] = (
    z('rect', '#c9d3db', x=124, y=26, width=46, height=14, rx=6)
    + z('rect', '#c9d3db', x=124, y=38, width=14, height=22, rx=3)
    + s('rect', '#8fc7e8', x=126, y=62, width=10, height=46, rx=4, stroke_width=2.5)
    + z('path', '#f4f4f0', d='M24 140 L176 140 Q172 182 100 182 Q28 182 24 140Z')
    + zr('rect', '#8fc7e8', -20, 40, 120, x=22, y=106, width=26, height=28, rx=5)
    + zr('rect', '#f5b971', 20, 160, 118, x=150, y=104, width=26, height=28, rx=5)
    + zr('ellipse', SK, -20, 76, 112, cx=76, cy=112, rx=32, ry=17)
    + zr('ellipse', SK, 20, 122, 106, cx=122, cy=106, rx=32, ry=17)
    + rg(20, 122, 106, s('path', d='M110 92 Q114 86 120 90', stroke_width=2.5))
    + bubble(98, 92, 9) + bubble(82, 98, 6) + bubble(112, 128, 7) + bubble(66, 132, 8)
    + bubble(56, 84, 6) + bubble(146, 88, 6) + bubble(96, 126, 5)
)

# 12. hand sanitizer
ITEMS['hand-sanitizer'] = (
    z('rect', '#8fc7e8', x=56, y=84, width=88, height=96, rx=18)
    + z('rect', '#f4f4f0', x=86, y=64, width=28, height=24, rx=3)
    + z('rect', '#f4f4f0', x=94, y=48, width=12, height=18)
    + z('path', '#f4f4f0', d='M64 36 L116 36 Q122 36 122 42 L122 50 L64 50 Q58 50 58 43 Q58 36 64 36Z')
    + s('rect', '#ffffff', x=68, y=110, width=64, height=52, rx=6)
    + s('path', '#7cc4b0', d='M100 118 Q112 134 112 142 Q112 154 100 154 Q88 154 88 142 Q88 134 100 118Z', stroke_width=2.5)
    + s('path', d='M64 96 Q64 90 70 88', stroke='#ffffff', stroke_width=3)
    + z('rect', '#f4f4f0', x=50, y=40, width=12, height=8, rx=2) + drop(55, 58, 1.0, '#c9e6f2')
    + s('path', d='M150 50 L150 66 M142 58 L158 58 M164 84 L164 94 M159 89 L169 89', stroke_width=2.5)
)

# 13. gargling
ITEMS['gargling'] = (
    body(96, 134, '#8fc7e8')
    + rg(-22, 92, 90, f2(92, 90, '#2b2220', eyes='closed', mouth='o'))
    + thick('M120 150 Q150 140 150 112', '#8fc7e8', w=13, inner=8)
    + z('path', '#ffffff', d='M138 82 L164 82 L160 112 L142 112Z')
    + s('path', '#8fc7e8', d='M140 92 L162 92 L160 112 L142 112Z', stroke='none')
    + s('path', d='M138 82 L164 82 L160 112 L142 112Z', stroke_width=3)
    + z('circle', SK, cx=150, cy=114, r=10)
    + bubble(108, 52, 7) + bubble(122, 38, 9) + bubble(104, 28, 6) + bubble(136, 56, 5)
)

# 14. coughing
ITEMS['coughing'] = (
    body(96, 132, '#9ccf7a')
    + f2(92, 86, '#5a4033', eyes='shut', mouth='o')
    + thick('M72 160 Q66 128 84 112', '#9ccf7a', w=14, inner=9)
    + z('circle', SK, cx=90, cy=106, r=11)
    + s('path', d='M126 96 L136 92 M128 108 L140 110 M124 120 L134 126', stroke_width=2.5)
    + puff(150, 92, 11) + puff(166, 76, 7) + puff(160, 116, 8) + puff(176, 100, 5)
)

# 15. fever
ITEMS['fever'] = (
    body(100, 134, '#8fb3e0')
    + f2(100, 90, '#2b2220', eyes='droop', mouth='frown', blush='#f07a8a', brx=9)
    + zr('rect', '#f4f4f0', 18, 104, 110, x=104, y=106, width=34, height=8, rx=4)
    + rg(18, 104, 110, s('rect', '#e04b5a', x=128, y=106, width=10, height=8, rx=4, stroke_width=2))
    + z('path', '#8fc7e8', d='M64 58 Q100 30 136 58 Q140 68 128 70 Q100 60 72 70 Q60 68 64 58Z')
    + s('rect', '#ffffff', x=84, y=48, width=10, height=10, rx=2, stroke_width=2)
    + s('rect', '#ffffff', x=104, y=46, width=10, height=10, rx=2, stroke_width=2)
    + s('path', d='M98 38 Q100 30 104 36', stroke_width=3)
    + s('path', d='M46 72 Q40 80 46 88 Q52 96 46 104 M154 72 Q148 80 154 88 Q160 96 154 104', stroke='#e8735a', stroke_width=3)
    + drop(146, 112, 0.8)
)

# 16. headache
ITEMS['headache'] = (
    body(100, 134, '#f5b971')
    + thick('M72 160 Q58 130 64 104', '#f5b971', w=14, inner=9)
    + thick('M128 160 Q142 130 136 104', '#f5b971', w=14, inner=9)
    + f2(100, 90, '#5a4033', eyes='shut', mouth='wavy')
    + z('circle', SK, cx=66, cy=96, r=11) + z('circle', SK, cx=134, cy=96, r=11)
    + z('path', '#ffe27a', d='M40 30 L54 30 L48 42 L58 42 L38 64 L44 48 L34 48Z')
    + z('path', '#ffe27a', d='M150 28 L164 28 L158 40 L168 40 L148 62 L154 46 L144 46Z')
    + s('path', d='M86 40 L92 30 L98 40 L104 30 L110 40 L116 30', stroke='#e8735a', stroke_width=3)
)

# 17. stomachache
ITEMS['stomachache'] = (
    body(100, 130, '#a98bd0', w=40)
    + f2(100, 86, '#2b2220', eyes='sad', mouth='frown')
    + thick('M66 148 Q72 164 88 160', '#a98bd0', w=14, inner=9)
    + thick('M134 148 Q128 160 114 156', '#a98bd0', w=14, inner=9)
    + s('path', d='M100 168 Q92 166 94 160 Q98 154 104 160 Q106 168 98 170', stroke_width=2.5)
    + z('circle', SK, cx=88, cy=158, r=11) + z('circle', SK, cx=114, cy=154, r=11)
    + s('path', d='M46 140 L38 146 L46 152 L38 158 M154 140 L162 146 L154 152 L162 158', stroke='#e8735a', stroke_width=3)
    + drop(144, 54, 0.9) + drop(56, 60, 0.7)
)

# 18. toothache
TOOTH = ('M24 36 Q24 24 35 26 Q41 28 47 26 Q58 24 58 36 Q58 46 54 52 L52 66 Q49 71 46 66 L44 56 '
         'Q41 52 38 56 L36 66 Q33 71 30 66 L28 52 Q24 46 24 36Z')
ITEMS['toothache'] = (
    body(96, 134, '#7cc4b0')
    + f2(94, 90, '#5a4033', eyes='shut', mouth='wavy')
    + z('circle', SK, cx=124, cy=104, r=15) + s('ellipse', CH, cx=124, cy=104, rx=7, ry=4.5, stroke='none')
    + thick('M118 160 Q150 146 142 118', '#7cc4b0', w=14, inner=9)
    + z('circle', SK, cx=140, cy=112, r=11)
    + z('path', '#ffffff', d=TOOTH)
    + s('path', d='M40 28 L37 36 L44 40 L40 48', stroke_width=2.5)
    + s('path', d='M66 30 L76 26 M66 44 L78 46 M14 22 L20 28', stroke='#e8735a', stroke_width=3)
    + s('path', d='M150 70 L160 64 M154 84 L166 84', stroke='#e8735a', stroke_width=3)
)

# 19. flu in bed
ITEMS['flu-in-bed'] = (
    z('rect', '#d9a66b', x=20, y=66, width=18, height=116, rx=5)
    + z('rect', '#d9a66b', x=164, y=110, width=16, height=72, rx=5)
    + z('rect', '#f4f4f0', x=30, y=128, width=142, height=30, rx=4)
    + z('ellipse', '#ffffff', cx=68, cy=118, rx=32, ry=14)
    + f2(68, 98, '#5a4033', r=26, eyes='droop', mouth='frown', blush='#f07a8a', brx=8)
    + z('rect', '#f4f4f0', x=50, y=72, width=36, height=12, rx=4)
    + z('path', '#8fb3e0', d='M44 122 Q60 116 96 112 Q140 104 172 118 L172 160 L44 160Z')
    + ''.join(s('circle', '#ffffff', cx=x, cy=y, r=4, stroke_width=2) for x, y in ((70, 134), (100, 126), (130, 138), (156, 128), (110, 150), (80, 152), (150, 152)))
    + z('rect', '#d9a66b', x=20, y=156, width=160, height=12, rx=3)
    + drop(110, 70, 0.8) + s('path', d='M120 60 Q126 52 120 44', stroke_width=2.5)
)

# 20. hay fever
POL = ((30, 40), (48, 26), (24, 70), (148, 48), (166, 66), (174, 40), (40, 112), (30, 150), (172, 150), (130, 24), (62, 44))
ITEMS['hay-fever'] = (
    body(92, 134, '#f6a6b8')
    + f2(88, 90, '#c9a36b', eyes='shut', mouth='open')
    + s('circle', '#f07a8a', cx=88, cy=98, r=4, stroke_width=2)
    + puff(140, 104, 11) + puff(158, 90, 8) + puff(156, 120, 7) + puff(172, 106, 5)
    + s('path', d='M122 92 L130 86 M124 120 L132 128', stroke_width=2.5)
    + ''.join(s('circle', '#ffe27a', cx=x, cy=y, r=4.5, stroke_width=2) for x, y in POL)
)
