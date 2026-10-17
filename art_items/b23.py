import math, re
from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}


def mir(d):
    """mirror an absolute M/L/Q/C/Z path about x=100"""
    out, i = [], 0
    for tok in re.findall(r'[A-Za-z]|-?\d+\.?\d*', d):
        if tok.isalpha():
            out.append(tok); i = 0
        else:
            v = float(tok)
            out.append(f'{200 - v:g}' if i % 2 == 0 else tok); i += 1
    return ' '.join(out)


def thick(d, color, w=14, inner=8):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


def aface(cx, cy, sep=11, ch=None, m=True):
    ch = ch if ch is not None else sep + 9
    o = dot(cx - sep, cy) + dot(cx + sep, cy) + cheeks(cx - ch, cx + ch, cy + 10, 6, 3.5)
    if m:
        o += s('path', d=f'M{cx-5} {cy+9} Q{cx} {cy+14} {cx+5} {cy+9}', stroke_width=2.5)
    return o


def water(top, rest, c='#8fc7e8'):
    return ('<g transform="translate(4 4)">' + s('path', c, d=top + ' ' + rest, stroke='none') + '</g>'
            + s('path', c, d=top + ' ' + rest, stroke='none') + s('path', d=top))


def mouth_w(cx, cy):
    return s('path', d=f'M{cx-6} {cy} Q{cx-3} {cy+4} {cx} {cy} Q{cx+3} {cy+4} {cx+6} {cy}', stroke_width=2.5)


# 1. polar bear
W = '#f4f4f0'
ITEMS['polar-bear'] = (
    z('circle', W, cx=72, cy=60, r=13) + z('circle', W, cx=128, cy=60, r=13)
    + s('circle', '#c9d3db', cx=72, cy=60, r=6, stroke='none') + s('circle', '#c9d3db', cx=128, cy=60, r=6, stroke='none')
    + z('ellipse', W, cx=100, cy=144, rx=44, ry=38)
    + z('ellipse', W, cx=78, cy=178, rx=15, ry=9) + z('ellipse', W, cx=122, cy=178, rx=15, ry=9)
    + z('ellipse', W, cx=66, cy=138, rx=11, ry=17, transform='rotate(20 66 138)')
    + z('ellipse', W, cx=134, cy=138, rx=11, ry=17, transform='rotate(-20 134 138)')
    + z('circle', W, cx=100, cy=92, r=34)
    + s('ellipse', '#ffffff', cx=100, cy=104, rx=14, ry=10, stroke_width=2.5)
    + f'<ellipse cx="100" cy="99" rx="6" ry="4" fill="{OUT}" stroke="none"/>'
    + dot(87, 86) + dot(113, 86) + cheeks(76, 124, 100, 6, 3.5) + mouth_w(100, 105)
)

# 2. red panda
RP, DK = '#e8735a', '#8b6b4f'
ITEMS['red-panda'] = (
    z('ellipse', RP, cx=146, cy=146, rx=15, ry=34, transform='rotate(35 146 146)')
    + '<g transform="rotate(35 146 146)">'
    + s('path', d='M139 122 L153 122 M135 136 L157 136 M135 152 L157 152 M138 166 L154 166', stroke='#9a6a3f', stroke_width=5)
    + '</g>'
    + z('ellipse', RP, cx=100, cy=146, rx=38, ry=34)
    + s('ellipse', DK, cx=100, cy=156, rx=20, ry=18, stroke='none')
    + z('ellipse', DK, cx=84, cy=178, rx=12, ry=8) + z('ellipse', DK, cx=116, cy=178, rx=12, ry=8)
    + z('path', RP, d='M66 72 Q60 46 82 54Z') + z('path', RP, d='M134 72 Q140 46 118 54Z')
    + s('path', W, d='M68 66 Q66 54 78 58Z', stroke='none') + s('path', W, d='M132 66 Q134 54 122 58Z', stroke='none')
    + z('ellipse', RP, cx=100, cy=94, rx=40, ry=33)
    + s('ellipse', W, cx=72, cy=100, rx=9, ry=11, stroke='none') + s('ellipse', W, cx=128, cy=100, rx=9, ry=11, stroke='none')
    + s('ellipse', W, cx=86, cy=78, rx=6, ry=4, stroke='none') + s('ellipse', W, cx=114, cy=78, rx=6, ry=4, stroke='none')
    + s('ellipse', W, cx=100, cy=108, rx=15, ry=11, stroke='none')
    + dot(88, 90) + dot(112, 90) + cheeks(82, 118, 104, 5, 3)
    + f'<ellipse cx="100" cy="102" rx="5" ry="3.5" fill="{OUT}" stroke="none"/>' + mouth_w(100, 107)
)

# 3. otter floating on its back
OT = '#9a6a3f'
ITEMS['otter'] = (
    z('ellipse', OT, cx=160, cy=136, rx=18, ry=8, transform='rotate(-15 160 136)')
    + z('ellipse', OT, cx=104, cy=132, rx=54, ry=24)
    + s('ellipse', '#d9a66b', cx=108, cy=126, rx=38, ry=14, stroke='none')
    + z('ellipse', OT, cx=148, cy=110, rx=7, ry=11, transform='rotate(20 148 110)')
    + z('path', '#f6a6b8', d='M98 122 Q100 102 112 100 Q124 102 126 122Z')
    + s('path', d='M112 102 L112 120 M104 106 L106 120 M120 106 L118 120', stroke_width=2)
    + z('circle', OT, cx=96, cy=118, r=7) + z('circle', OT, cx=128, cy=118, r=7)
    + z('circle', OT, cx=36, cy=96, r=8) + z('circle', OT, cx=74, cy=94, r=8)
    + z('circle', OT, cx=56, cy=112, r=26)
    + s('ellipse', '#d9a66b', cx=56, cy=122, rx=14, ry=9, stroke='none')
    + dot(46, 110) + dot(66, 110) + cheeks(38, 74, 122, 5, 3)
    + f'<ellipse cx="56" cy="118" rx="4" ry="3" fill="{OUT}" stroke="none"/>' + mouth_w(56, 123)
    + water('M24 148 Q40 138 56 148 Q72 158 88 148 Q104 138 120 148 Q136 158 152 148 Q166 140 178 148', 'L178 172 Q100 180 24 172Z')
    + s('path', d='M44 162 Q52 158 60 162 M110 166 Q118 162 126 166', stroke='#ffffff', stroke_width=2.5)
)

# 4. beaver holding a log
BV = '#9a6a3f'
ITEMS['beaver'] = (
    z('ellipse', DK, cx=142, cy=168, rx=32, ry=12, transform='rotate(-12 142 168)')
    + '<g transform="rotate(-12 142 168)">'
    + s('path', d='M124 162 L160 174 M124 174 L160 162 M140 158 L140 178', stroke='#5b4636', stroke_width=1.5)
    + '</g>'
    + z('ellipse', BV, cx=100, cy=142, rx=38, ry=36)
    + s('ellipse', '#d9a66b', cx=100, cy=150, rx=22, ry=22, stroke='none')
    + z('ellipse', DK, cx=82, cy=178, rx=12, ry=7) + z('ellipse', DK, cx=118, cy=178, rx=12, ry=7)
    + z('circle', BV, cx=74, cy=66, r=9) + z('circle', BV, cx=126, cy=66, r=9)
    + z('circle', BV, cx=100, cy=92, r=32)
    + s('ellipse', '#d9a66b', cx=100, cy=104, rx=15, ry=10, stroke='none')
    + z('rect', '#ffffff', x=94, y=106, width=12, height=10, rx=2) + s('path', d='M100 107 L100 115', stroke_width=2)
    + f'<ellipse cx="100" cy="99" rx="6" ry="4" fill="{OUT}" stroke="none"/>'
    + dot(88, 86) + dot(112, 86) + cheeks(78, 122, 98, 6, 3.5)
    + z('rect', '#d9a66b', x=66, y=128, width=68, height=14, rx=7)
    + s('ellipse', '#f6e0c4', cx=130, cy=135, rx=4, ry=6, stroke_width=2)
    + z('circle', BV, cx=82, cy=134, r=7) + z('circle', BV, cx=118, cy=134, r=7)
)

# 5. bat
WG, BB = '#5b6b7a', '#b9a99c'
wing = 'M86 106 Q62 72 26 80 Q36 94 32 108 Q46 104 50 120 Q60 112 68 128 Q78 118 88 128Z'
ITEMS['bat'] = (
    z('path', WG, d=wing) + z('path', WG, d=mir(wing))
    + s('path', d='M44 92 Q60 100 74 112 M86 106 Q74 104 60 108', stroke='#8fa0b0', stroke_width=2)
    + s('path', d=mir('M44 92 Q60 100 74 112 M86 106 Q74 104 60 108'), stroke='#8fa0b0', stroke_width=2)
    + z('ellipse', BB, cx=100, cy=136, rx=20, ry=24)
    + s('path', d='M92 160 L90 168 M108 160 L110 168', stroke_width=3)
    + z('path', BB, d='M76 82 L72 46 L96 66Z') + z('path', BB, d='M124 82 L128 46 L104 66Z')
    + s('path', '#f6a6b8', d='M79 74 L77 56 L90 66Z', stroke='none') + s('path', '#f6a6b8', d='M121 74 L123 56 L110 66Z', stroke='none')
    + z('circle', BB, cx=100, cy=94, r=28)
    + dot(89, 92) + dot(111, 92) + cheeks(80, 120, 102, 5, 3)
    + s('path', d='M94 104 Q100 109 106 104', stroke_width=2.5)
    + s('path', '#ffffff', d='M95 106 L97 111 L99 107Z', stroke_width=1.5)
    + s('path', '#ffffff', d='M101 107 L103 111 L105 106Z', stroke_width=1.5)
)

# 6. camel (side view, facing left)
CM = '#d9a66b'
ITEMS['camel'] = (
    z('rect', CM, x=70, y=124, width=11, height=52, rx=5) + z('rect', CM, x=132, y=124, width=11, height=52, rx=5)
    + s('path', d='M154 116 Q164 128 160 144', stroke_width=3)
    + z('path', CM, d='M46 86 Q50 116 72 120 L84 108 Q62 100 60 80Z')
    + z('path', CM, d='M60 132 Q52 102 74 100 Q86 62 106 98 Q124 62 140 100 Q162 104 156 132 Q108 148 60 132Z')
    + z('rect', CM, x=84, y=128, width=11, height=48, rx=5) + z('rect', CM, x=118, y=128, width=11, height=48, rx=5)
    + z('ellipse', CM, cx=48, cy=74, rx=22, ry=14)
    + z('ellipse', CM, cx=60, cy=60, rx=5, ry=8, transform='rotate(20 60 60)')
    + dot(48, 70) + cheeks(56, 56, 80, 5, 3)
    + dot(30, 72, 2.5) + s('path', d='M30 80 Q36 84 42 80', stroke_width=2.5)
    + s('path', d='M28 180 L174 180', stroke_width=2)
)

# 7. alpaca
AL = '#f6e0c4'
ITEMS['alpaca'] = (
    z('rect', AL, x=78, y=136, width=11, height=42, rx=5) + z('rect', AL, x=126, y=136, width=11, height=42, rx=5)
    + z('path', AL, d='M68 132 Q56 112 74 104 Q82 88 100 96 Q114 84 128 98 Q150 96 150 116 Q162 134 144 144 Q132 156 112 148 Q98 158 84 148 Q64 150 68 132Z')
    + z('rect', AL, x=92, y=140, width=11, height=38, rx=5) + z('rect', AL, x=112, y=140, width=11, height=38, rx=5)
    + s('path', d='M152 112 Q166 112 162 126', stroke_width=3)
    + z('path', AL, d='M58 122 Q50 96 52 72 L82 72 Q80 96 86 114Z')
    + s('path', d='M58 86 Q66 90 74 86 M58 100 Q66 104 76 100', stroke_width=2)
    + z('ellipse', AL, cx=54, cy=36, rx=5, ry=11, transform='rotate(-15 54 36)')
    + z('ellipse', AL, cx=80, cy=36, rx=5, ry=11, transform='rotate(15 80 36)')
    + z('ellipse', AL, cx=67, cy=62, rx=24, ry=20)
    + s('path', '#ffffff', d='M46 54 Q44 40 56 42 Q62 32 72 40 Q84 36 88 52 Q76 46 67 50 Q56 46 46 54Z', stroke_width=2.5)
    + z('ellipse', '#ffffff', cx=67, cy=72, rx=11, ry=8)
    + dot(57, 62) + dot(77, 62) + cheeks(50, 84, 70, 5, 3)
    + dot(67, 69, 2.5) + mouth_w(67, 74)
)

# 8. mouse
MS = '#b9a99c'
ITEMS['mouse'] = (
    s('path', d='M132 162 Q170 172 166 146 Q162 128 148 136', stroke_width=3)
    + z('circle', MS, cx=68, cy=66, r=22) + z('circle', MS, cx=132, cy=66, r=22)
    + s('circle', '#f6a6b8', cx=68, cy=66, r=12, stroke='none') + s('circle', '#f6a6b8', cx=132, cy=66, r=12, stroke='none')
    + z('ellipse', MS, cx=100, cy=148, rx=36, ry=32)
    + s('ellipse', '#f4f4f0', cx=100, cy=154, rx=18, ry=18, stroke='none')
    + z('ellipse', '#f6a6b8', cx=84, cy=178, rx=11, ry=6) + z('ellipse', '#f6a6b8', cx=116, cy=178, rx=11, ry=6)
    + z('circle', MS, cx=100, cy=102, r=30)
    + dot(89, 98) + dot(111, 98) + cheeks(80, 120, 110, 5, 3)
    + s('circle', '#f6a6b8', cx=100, cy=108, r=4, stroke_width=2) + mouth_w(100, 113)
    + s('path', d='M80 106 L64 102 M80 112 L64 114 M120 106 L136 102 M120 112 L136 114', stroke_width=2)
)

# 9. dolphin jumping
DP = '#8fb3e0'
ITEMS['dolphin'] = (
    z('path', DP, d='M92 64 Q94 38 116 40 Q106 50 110 60Z')
    + z('path', DP, d='M58 148 L32 150 Q44 158 46 174 Q58 164 66 154Z')
    + z('path', DP, d='M54 152 Q56 74 124 54 Q156 48 170 68 L180 78 Q176 86 160 86 Q120 84 90 116 Q74 134 66 156Z')
    + s('path', '#f4f4f0', d='M164 84 Q124 84 96 110 Q80 128 70 150 Q74 120 96 100 Q124 80 160 80Z', stroke='none')
    + z('path', DP, d='M112 90 Q118 110 104 120 Q102 106 100 98Z')
    + dot(148, 66) + cheeks(156, 156, 76, 5, 3)
    + s('path', d='M166 80 Q172 82 178 78', stroke_width=2.5)
    + water('M26 168 Q38 158 50 166 Q62 174 74 166 Q86 158 98 166', 'Q92 178 62 178 Q32 178 26 168Z')
    + s('circle', '#8fc7e8', cx=84, cy=150, r=4, stroke_width=2) + s('circle', '#8fc7e8', cx=98, cy=158, r=3, stroke_width=2)
    + s('circle', '#8fc7e8', cx=30, cy=150, r=3.5, stroke_width=2)
)

# 10. whale with a water spout
WH = '#8fb3e0'
ITEMS['whale'] = (
    z('path', '#8fc7e8', d='M84 82 Q78 62 60 54 Q78 54 84 68 Q90 54 108 54 Q90 62 84 82Z')
    + s('circle', '#8fc7e8', cx=56, cy=50, r=5, stroke_width=2) + s('circle', '#8fc7e8', cx=112, cy=50, r=5, stroke_width=2)
    + s('circle', '#8fc7e8', cx=68, cy=38, r=4, stroke_width=2) + s('circle', '#8fc7e8', cx=100, cy=38, r=4, stroke_width=2)
    + s('circle', '#8fc7e8', cx=84, cy=32, r=4.5, stroke_width=2)
    + z('path', WH, d='M28 132 Q28 84 86 82 Q134 82 150 120 L168 98 Q180 112 170 126 Q180 138 172 152 L150 136 Q132 166 84 166 Q28 166 28 132Z')
    + s('path', '#f4f4f0', d='M32 142 Q50 164 88 164 Q122 164 140 146 Q96 158 32 142Z', stroke_width=2.5)
    + s('path', d='M60 150 L62 160 M80 153 L81 163 M100 152 L100 162 M118 149 L117 159', stroke_width=2)
    + z('path', WH, d='M90 132 Q104 150 92 156 Q82 148 84 134Z')
    + dot(56, 118) + cheeks(66, 66, 128, 6, 3.5)
    + s('path', d='M34 130 Q44 138 54 132', stroke_width=2.5)
)

# 11. friendly shark
SH = '#c9d3db'
ITEMS['shark'] = (
    z('path', SH, d='M86 82 Q98 48 122 42 Q114 64 124 82Z')
    + z('path', SH, d='M150 104 L178 74 Q170 108 178 140 L150 118Z')
    + z('path', SH, d='M24 112 Q48 76 108 76 Q148 78 164 110 Q144 142 100 142 Q48 142 24 112Z')
    + s('path', '#f4f4f0', d='M28 116 Q60 140 104 140 Q136 138 152 124 Q100 130 28 116Z', stroke='none')
    + s('path', d='M98 98 Q94 106 98 114 M108 96 Q104 106 108 116 M118 98 Q114 106 118 114', stroke_width=2.5)
    + z('path', SH, d='M84 126 Q78 152 62 160 Q66 142 68 128Z')
    + dot(54, 98) + cheeks(62, 62, 110, 6, 3.5)
    + s('path', '#ffffff', d='M30 114 Q44 126 60 118Z', stroke_width=2.5)
    + s('path', d='M36 117 L38 121 M44 120 L45 124 M52 120 L52 123', stroke_width=1.5)
)

# 12. octopus
OC = '#f07a8a'
tents = ['M76 120 Q52 134 44 154 Q38 172 54 172', 'M86 126 Q74 148 76 166 Q78 182 90 176', 'M96 128 Q96 150 92 166']
ITEMS['octopus'] = (
    ''.join(thick(t, OC) + thick(mir(t), OC) for t in tents)
    + z('ellipse', OC, cx=100, cy=86, rx=46, ry=44)
    + s('circle', '#f6a6b8', cx=78, cy=62, r=6, stroke='none') + s('circle', '#f6a6b8', cx=112, cy=54, r=4.5, stroke='none')
    + s('circle', '#f6a6b8', cx=126, cy=70, r=3.5, stroke='none')
    + dot(86, 100) + dot(114, 100) + cheeks(76, 124, 112, 6, 3.5)
    + f'<circle cx="100" cy="114" r="4" fill="#c0504d" stroke-width="2.5"/>'
)

# 13. squid
SQ = '#f4f4f0'
arms = ['M80 120 Q70 146 78 166', 'M92 124 Q88 150 94 172']
ITEMS['squid'] = (
    s('path', d='M84 118 Q66 148 52 168', stroke_width=7) + s('path', d='M84 118 Q66 148 52 168', stroke=SQ, stroke_width=2.5)
    + s('path', d=mir('M84 118 Q66 148 52 168'), stroke_width=7) + s('path', d=mir('M84 118 Q66 148 52 168'), stroke=SQ, stroke_width=2.5)
    + z('ellipse', SQ, cx=50, cy=172, rx=8, ry=6) + z('ellipse', SQ, cx=150, cy=172, rx=8, ry=6)
    + ''.join(thick(a, SQ, 13, 7) + thick(mir(a), SQ, 13, 7) for a in arms)
    + z('path', SQ, d='M86 48 L54 72 L82 86Z') + z('path', SQ, d=mir('M86 48 L54 72 L82 86Z'))
    + z('path', SQ, d='M100 26 Q134 58 130 120 L70 120 Q66 58 100 26Z')
    + s('circle', '#f6a6b8', cx=94, cy=54, r=4, stroke='none') + s('circle', '#f6a6b8', cx=108, cy=66, r=5, stroke='none')
    + s('circle', '#f6a6b8', cx=90, cy=74, r=3, stroke='none')
    + aface(100, 96, 13)
)

# 14. crab
CR = '#e8735a'
legs = ['M62 136 L40 144 L30 160', 'M64 148 L46 160 L40 176', 'M74 156 L62 170 L60 182']
claw = 'M50 98 Q26 96 30 70 Q36 58 50 62 L44 76 L58 78 Q62 94 50 98Z'
ITEMS['crab'] = (
    ''.join(thick(l, CR, 12, 6) + thick(mir(l), CR, 12, 6) for l in legs)
    + thick('M70 122 L50 96', CR, 12, 6) + thick(mir('M70 122 L50 96'), CR, 12, 6)
    + z('path', CR, d=claw) + z('path', CR, d=mir(claw))
    + s('path', d='M88 110 L86 90 M112 110 L114 90', stroke_width=3)
    + z('circle', '#ffffff', cx=86, cy=84, r=9) + z('circle', '#ffffff', cx=114, cy=84, r=9)
    + dot(87, 85) + dot(113, 85)
    + z('ellipse', CR, cx=100, cy=134, rx=44, ry=30)
    + cheeks(78, 122, 136, 6, 3.5) + s('path', d='M92 132 Q100 140 108 132', stroke_width=2.5)
)

# 15. jellyfish
JF = '#f6a6b8'
ITEMS['jellyfish'] = (
    s('path', d='M64 112 Q56 128 64 144 Q72 160 62 176', stroke_width=3)
    + s('path', d='M136 112 Q144 128 136 144 Q128 160 138 176', stroke_width=3)
    + thick('M88 112 Q80 130 90 146 Q98 160 88 174', '#f5d58a', 12, 6)
    + thick('M112 112 Q120 130 110 146 Q102 160 112 174', '#f5d58a', 12, 6)
    + s('path', d='M100 116 Q106 136 98 156', stroke_width=3)
    + z('path', JF, d='M42 110 Q42 40 100 40 Q158 40 158 110 Q148 118 137 110 Q126 118 115 110 Q104 118 93 110 Q82 118 71 110 Q60 118 50 110Q46 114 42 110Z')
    + s('path', d='M60 72 Q66 56 82 50', stroke='#ffffff', stroke_width=4)
    + dot(86, 84) + dot(114, 84) + cheeks(76, 124, 95, 6, 3.5, ) .replace(CH, '#f07a8a')
    + s('path', d='M94 94 Q100 100 106 94', stroke_width=2.5)
)

# 16. seal lying down, head raised
SE = '#c9d3db'
ITEMS['seal'] = (
    z('path', SE, d='M150 158 L176 140 Q180 156 172 164 Q180 172 174 180 L150 172Z')
    + z('path', SE, d='M42 104 Q40 66 74 64 Q106 66 108 104 Q118 140 156 152 Q160 174 140 176 L76 176 Q44 172 42 140Z')
    + s('path', '#f4f4f0', d='M50 150 Q60 172 90 174 L120 174 Q90 164 50 150Z', stroke='none')
    + s('circle', '#b0bcc6', cx=110, cy=150, r=4, stroke='none') + s('circle', '#b0bcc6', cx=128, cy=160, r=3, stroke='none')
    + s('circle', '#b0bcc6', cx=96, cy=136, r=3, stroke='none')
    + z('path', SE, d='M80 152 Q104 160 106 174 Q88 176 72 166Z')
    + dot(62, 92) + dot(86, 92) + cheeks(54, 94, 104, 5, 3)
    + s('ellipse', '#f4f4f0', cx=74, cy=104, rx=11, ry=8, stroke_width=2)
    + f'<ellipse cx="74" cy="100" rx="4.5" ry="3" fill="{OUT}" stroke="none"/>' + mouth_w(74, 105)
    + s('path', d='M62 104 L48 100 M62 108 L48 110 M86 104 L100 100 M86 108 L100 110', stroke_width=1.8)
)

# 17. sea turtle swimming
SL, TG = '#7cc4a0', '#9ccf7a'
ITEMS['sea-turtle'] = (
    z('path', TG, d='M72 86 Q50 68 36 70 Q48 86 64 98Z')
    + z('path', TG, d='M124 84 Q146 54 170 52 Q156 80 134 96Z')
    + z('ellipse', TG, cx=156, cy=106, rx=20, ry=15)
    + z('path', SL, d='M46 116 Q50 64 100 62 Q146 64 148 114 Q100 126 46 116Z')
    + s('path', '#f5d58a', d='M46 116 Q100 126 148 114 Q140 128 100 130 Q60 130 46 116Z', stroke_width=2.5)
    + s('path', d='M86 76 L114 76 L122 94 L110 110 L88 110 L78 94Z', stroke_width=2.5)
    + s('path', d='M86 76 L76 66 M114 76 L124 66 M78 94 L54 96 M122 94 L144 96 M88 110 L84 120 M110 110 L114 120', stroke_width=2.5)
    + z('path', TG, d='M126 122 Q156 130 168 156 Q140 154 118 132Z')
    + z('path', TG, d='M60 124 Q42 138 34 152 Q56 150 72 130Z')
    + dot(160, 102) + cheeks(168, 168, 112, 4.5, 3)
    + s('path', d='M164 112 Q169 115 174 111', stroke_width=2.5)
    + s('circle', '#ffffff', cx=172, cy=76, r=4, stroke_width=2) + s('circle', '#ffffff', cx=178, cy=64, r=3, stroke_width=2)
)

# 18. clownfish
CF = '#f5a04d'
ITEMS['clownfish'] = (
    z('path', CF, d='M72 76 Q94 46 128 72Z')
    + z('path', CF, d='M52 104 L28 80 Q36 104 28 128Z')
    + z('path', CF, d='M84 132 Q94 156 112 136Z')
    + z('ellipse', CF, cx=98, cy=104, rx=56, ry=36)
    + s('path', '#ffffff', d='M120 71 Q110 104 120 137 L108 139 Q98 104 108 69Z', stroke='none')
    + s('path', '#ffffff', d='M86 68 Q78 104 86 140 L72 138 Q64 104 72 70Z', stroke='none')
    + s('path', '#ffffff', d='M52 92 Q48 104 52 116 L46 112 Q44 104 46 96Z', stroke='none')
    + s('path', d='M120 71 Q110 104 120 137 M108 69 Q98 104 108 139 M86 68 Q78 104 86 140 M72 70 Q64 104 72 138', stroke_width=2.5)
    + s('ellipse', cx=98, cy=104, rx=56, ry=36)
    + dot(134, 96) + cheeks(140, 140, 108, 5, 3)
    + s('path', d='M146 110 Q150 114 154 110', stroke_width=2.5)
)

# 19. pufferfish
PF = '#f5d58a'
spikes = ''
for ang in range(-150, 181, 30):
    if abs(ang) == 180 or ang == 150 or ang == -150:
        continue
    a = math.radians(ang); b1 = math.radians(ang - 9); b2 = math.radians(ang + 9)
    p = lambda r, t: f'{100 + r * math.cos(t):.1f} {104 + r * math.sin(t):.1f}'
    spikes += z('path', PF, d=f'M{p(46, b1)} L{p(66, a)} L{p(46, b2)}Z')
ITEMS['pufferfish'] = (
    z('path', PF, d='M52 104 L28 84 Q34 104 28 124Z')
    + spikes
    + z('circle', PF, cx=100, cy=104, r=50)
    + s('ellipse', '#f4f4f0', cx=100, cy=128, rx=30, ry=18, stroke='none')
    + s('circle', '#d9a66b', cx=78, cy=74, r=3.5, stroke='none') + s('circle', '#d9a66b', cx=100, cy=66, r=3.5, stroke='none')
    + s('circle', '#d9a66b', cx=122, cy=74, r=3.5, stroke='none')
    + z('path', PF, d='M140 110 Q156 100 158 118 Q148 122 140 116Z')
    + dot(86, 96) + dot(114, 96) + cheeks(74, 126, 108, 6, 3.5)
    + f'<circle cx="100" cy="116" r="5" fill="#c0504d" stroke-width="2.5"/>'
)

# 20. starfish
def star(cx, cy, R, r):
    pts = []
    for i in range(5):
        a = math.radians(-90 + 72 * i); b = math.radians(-90 + 72 * i + 36)
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a), cx + r * math.cos(b), cy + r * math.sin(b)))
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(5):
        nx, ny = pts[(i + 1) % 5][0], pts[(i + 1) % 5][1]
        d += f' Q{pts[i][2]:.1f} {pts[i][3]:.1f} {nx:.1f} {ny:.1f}'
    return d + 'Z'
ST = '#f5b971'
ITEMS['starfish'] = (
    z('path', ST, d=star(100, 108, 78, 26))
    + ''.join(s('circle', '#f6e0c4', cx=x, cy=y, r=3, stroke='none') for x, y in
              [(100, 52), (100, 64), (48, 92), (60, 96), (152, 92), (140, 96), (68, 156), (76, 144), (132, 156), (124, 144)])
    + aface(100, 104, 12)
)
