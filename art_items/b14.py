from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

SK = '#ffd9b8'


def arm(d, col, w=9):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 5)


def body(cx, top, bottom, col, hw=34):
    return z('path', col, d=f'M{cx-hw} {bottom} Q{cx-hw+2} {top+2} {cx} {top} Q{cx+hw-2} {top+2} {cx+hw} {bottom}Z')


def head(cx, cy, hair, r=34):
    k = r / 34
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    o += s('path', hair, d=(f'M{cx-34*k:.1f} {cy-2*k:.1f} Q{cx-32*k:.1f} {cy-36*k:.1f} {cx} {cy-35*k:.1f} '
                            f'Q{cx+32*k:.1f} {cy-36*k:.1f} {cx+34*k:.1f} {cy-2*k:.1f} Q{cx+20*k:.1f} {cy-18*k:.1f} {cx} {cy-17*k:.1f} '
                            f'Q{cx-20*k:.1f} {cy-18*k:.1f} {cx-34*k:.1f} {cy-2*k:.1f}Z'))
    return o


def eyes(cx, cy, kind='dot', k=1.0, dx=0):
    o = ''
    for i, x in enumerate((cx - 12 * k + dx, cx + 12 * k + dx)):
        y = cy + 2 * k
        if kind == 'dot':
            o += dot(x, y, 3.5 * min(1, k + 0.15))
        elif kind == 'happy':
            o += s('path', d=f'M{x-5} {y+2} Q{x} {y-5} {x+5} {y+2}', stroke_width=2.5)
        elif kind == 'shut':
            o += s('path', d=f'M{x-5} {y-1} Q{x} {y+4} {x+5} {y-1}', stroke_width=2.5)
        elif kind == 'squeeze':
            sg = 1 if i == 0 else -1
            o += s('path', d=f'M{x-5*sg} {y-4} L{x+4*sg} {y} L{x-5*sg} {y+4}', stroke_width=2.5)
        elif kind == 'wide':
            o += s('circle', '#ffffff', cx=x, cy=y, r=6, stroke_width=2.5) + dot(x, y, 2.5)
    return o


def ck(cx, cy, k=1.0, col=CH):
    return (f'<ellipse cx="{cx-20*k}" cy="{cy+13*k}" rx="{7*k}" ry="{4*k}" fill="{col}" stroke="none"/>'
            f'<ellipse cx="{cx+20*k}" cy="{cy+13*k}" rx="{7*k}" ry="{4*k}" fill="{col}" stroke="none"/>')


def mouth(cx, cy, kind='smile', k=1.0):
    y = cy + 16 * k
    if kind == 'smile':
        return s('path', d=f'M{cx-6*k} {y} Q{cx} {y+5*k} {cx+6*k} {y}')
    if kind == 'open':
        return s('path', '#c0504d', d=f'M{cx-8*k} {y-2*k} Q{cx} {y+12*k} {cx+8*k} {y-2*k}Z', stroke_width=2.5)
    if kind == 'big':
        return s('path', '#c0504d', d=f'M{cx-11*k} {y-3*k} Q{cx} {y+16*k} {cx+11*k} {y-3*k}Z', stroke_width=2.5)
    if kind == 'o':
        return f'<circle cx="{cx}" cy="{y+2*k}" r="{4*k}" fill="#c0504d" stroke-width="2.5"/>'
    if kind == 'flat':
        return s('path', d=f'M{cx-6*k} {y+1} L{cx+6*k} {y+1}')
    if kind == 'frown':
        return s('path', d=f'M{cx-6*k} {y+3*k} Q{cx} {y-3*k} {cx+6*k} {y+3*k}')
    if kind == 'wavy':
        return s('path', d=f'M{cx-9*k} {y+1} Q{cx-6*k} {y-3} {cx-3*k} {y+1} Q{cx} {y+5} {cx+3*k} {y+1} Q{cx+6*k} {y-3} {cx+9*k} {y+1}', stroke_width=2.5)
    return ''


def drop(x, y, k=1.0, col='#8fc7e8'):
    return z('path', col, d=f'M{x} {y} Q{x-6*k} {y+10*k} {x} {y+14*k} Q{x+6*k} {y+10*k} {x} {y}Z', stroke_width=2.5)


def note(x, y, col='#e8735a'):
    return (z('ellipse', col, cx=x, cy=y, rx=7, ry=5.5, transform=f'rotate(-20 {x} {y})')
            + s('path', d=f'M{x+6} {y-1} L{x+6} {y-26} Q{x+12} {y-20} {x+18} {y-18}', stroke_width=3))


def plus(x, y, r=5):
    return s('path', d=f'M{x} {y-r} L{x} {y+r} M{x-r} {y} L{x+r} {y}', stroke_width=2.5)


def sparkle(x, y, r=10, col='#ffe27a'):
    q = r * 0.28
    return z('path', col, d=f'M{x} {y-r} Q{x+q} {y-q} {x+r} {y} Q{x+q} {y+q} {x} {y+r} Q{x-q} {y+q} {x-r} {y} Q{x-q} {y-q} {x} {y-r}Z', stroke_width=2.5)


def heart(x, y, k=1.0, col='#f07a8a'):
    return z('path', col, d=(f'M{x} {y+14*k} C{x-12*k} {y+4*k} {x-20*k} {y-4*k} {x-14*k} {y-12*k} '
                             f'C{x-8*k} {y-20*k} {x} {y-15*k} {x} {y-8*k} C{x} {y-15*k} {x+8*k} {y-20*k} {x+14*k} {y-12*k} '
                             f'C{x+20*k} {y-4*k} {x+12*k} {y+4*k} {x} {y+14*k}Z'), stroke_width=2.5)


def ground(x1=34, x2=166, y=186):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2.5)


# 1. asking for directions
ITEMS['person-asking-directions'] = (
    body(58, 142, 184, '#8fc7e8', 25)
    + head(58, 110, '#2b2220', 25) + eyes(58, 110, 'dot', 0.74, dx=3) + ck(58, 110, 0.74) + mouth(60, 110, 'o', 0.74)
    + s('path', d='M42 52 Q42 38 54 38 Q66 38 66 49 Q66 57 57 61 L57 68', stroke_width=9)
    + s('path', d='M42 52 Q42 38 54 38 Q66 38 66 49 Q66 57 57 61 L57 68', stroke='#f5b971', stroke_width=4)
    + z('circle', '#f5b971', cx=57, cy=80, r=4.5)
    + body(128, 132, 184, '#9ccf7a', 30)
    + arm('M146 146 Q164 126 170 100', '#9ccf7a')
    + z('circle', SK, cx=171, cy=94, r=8) + s('path', d='M172 88 L176 74', stroke_width=7) + s('path', d='M172 88 L176 74', stroke=SK, stroke_width=3)
    + head(124, 96, '#5a4033', 30) + eyes(124, 96, 'dot', 0.88, dx=-3) + ck(124, 96, 0.88) + mouth(122, 96, 'open', 0.88)
    + s('path', d='M150 42 Q164 34 176 42 M168 34 L176 42 L166 46', stroke_width=2.5)
)

# 2. searching with a flashlight
ITEMS['person-flashlight'] = (
    s('path', '#ffe27a', d='M144 124 L184 96 L184 168 L144 140Z', stroke='none')
    + s('path', d='M150 120 L184 96 M150 144 L184 168', stroke_width=2, stroke_dasharray='4 6')
    + s('circle', '#ffe27a', cx=42, cy=44, r=12, stroke_width=2.5) + s('circle', '#fbf6ee', cx=48, cy=40, r=10, stroke='none')
    + plus(150, 44, 4) + plus(76, 32, 3.5) + plus(178, 66, 3)
    + body(80, 142, 186, '#5b6b7a', 32)
    + arm('M100 156 Q112 150 118 138', '#5b6b7a')
    + z('rect', '#e8735a', x=112, y=126, width=26, height=14, rx=3)
    + z('rect', '#c9d3db', x=136, y=121, width=9, height=24, rx=2)
    + z('circle', SK, cx=116, cy=136, r=8)
    + head(80, 100, '#2b2220') + eyes(80, 100, 'dot', dx=6) + ck(80, 100) + mouth(84, 100, 'o')
)

# 3. peeking from behind a wall
bricks = ('M104 64 L174 64 M104 94 L174 94 M104 124 L174 124 M104 154 L174 154 '
          'M140 36 L140 64 M122 64 L122 94 M156 64 L156 94 M140 94 L140 124 M122 124 L122 154 M156 124 L156 154 M140 154 L140 182')
ITEMS['person-peeking-wall'] = (
    body(98, 132, 182, '#f6a6b8', 32)
    + head(80, 96, '#5a4033') + eyes(80, 96, 'dot', dx=-2) + ck(80, 96) + mouth(78, 96, 'smile')
    + z('rect', '#f6e0c4', x=100, y=36, width=74, height=146, rx=2)
    + s('path', d=bricks, stroke_width=2.5)
    + z('circle', SK, cx=102, cy=118, r=8) + z('circle', SK, cx=102, cy=146, r=8)
    + s('path', d='M28 182 L178 182', stroke_width=2.5)
    + s('path', d='M42 52 L50 60 M36 70 L46 72 M58 42 L60 52', stroke_width=2.5)
)

# 4. sneezing
ITEMS['person-sneezing'] = (
    body(84, 140, 186, '#f5b971', 32)
    + head(80, 100, '#2b2220')
    + s('path', d='M54 82 L66 86 M106 82 L94 86', stroke_width=2.5)
    + eyes(80, 100, 'squeeze') + ck(80, 100) + mouth(84, 100, 'big')
    + s('path', d='M120 106 L142 98 M122 120 L150 120 M120 134 L142 142 M116 92 L132 80 M116 148 L132 160', stroke_width=3)
    + dot(156, 92, 4, '#8fc7e8') + dot(162, 112, 3.5, '#8fc7e8') + dot(160, 132, 4, '#8fc7e8') + dot(150, 150, 3, '#8fc7e8')
    + dot(172, 122, 3, '#8fc7e8') + dot(146, 72, 3, '#8fc7e8')
    + s('path', d='M48 156 Q60 150 66 156', stroke_width=2)
)

# 5. happy tears
ITEMS['person-happy-tears'] = (
    body(100, 138, 186, '#f6a6b8', 34)
    + z('circle', SK, cx=64, cy=150, r=9) + z('circle', SK, cx=136, cy=150, r=9)
    + head(100, 96, '#c9a36b') + eyes(100, 96, 'happy') + ck(100, 96) + mouth(100, 96, 'big')
    + s('path', '#8fc7e8', d='M80 102 Q76 112 78 122 Q82 128 84 120 Q84 110 80 102Z', stroke_width=2)
    + s('path', '#8fc7e8', d='M120 102 Q124 112 122 122 Q118 128 116 120 Q116 110 120 102Z', stroke_width=2)
    + drop(48, 92, 0.9) + drop(152, 92, 0.9)
    + sparkle(40, 46, 10) + sparkle(160, 46, 10) + plus(140, 30, 4) + plus(60, 30, 4)
)

# 6. determined
ITEMS['person-determined'] = (
    body(96, 138, 186, '#e8735a', 34)
    + arm('M120 160 Q132 150 130 136', '#e8735a')
    + z('rect', SK, x=117, y=116, width=22, height=22, rx=8)
    + s('path', d='M117 124 L124 124 M117 131 L124 131 M128 116 L128 122 M133 116 L133 122', stroke_width=2)
    + head(92, 92, '#2b2220')
    + z('rect', '#ffffff', x=58, y=72, width=68, height=10, rx=3)
    + s('path', '#ffffff', d='M58 76 Q44 70 38 78 Q46 82 58 80Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M58 80 Q46 88 42 98 Q52 94 60 82Z', stroke_width=2.5)
    + s('path', d='M72 88 L86 92 M112 88 L98 92', stroke_width=3)
    + eyes(92, 96, 'dot') + ck(92, 92) + mouth(92, 92, 'flat')
    + sparkle(156, 64, 13) + sparkle(170, 98, 7, '#ffffff') + s('path', d='M150 28 L152 40 M168 34 L162 44', stroke_width=2.5)
)

# 7. relaxing with tea
ITEMS['person-relaxing-tea'] = (
    body(100, 136, 186, '#9ccf7a', 36)
    + head(100, 92, '#5a4033') + eyes(100, 92, 'shut') + ck(100, 92) + mouth(100, 92, 'smile')
    + s('path', d='M144 144 Q158 144 157 154 Q156 164 144 162', stroke_width=7)
    + s('path', d='M144 144 Q158 144 157 154 Q156 164 144 162', stroke='#f6e0c4', stroke_width=2.5)
    + z('path', '#f6e0c4', d='M114 136 L148 136 L145 166 Q131 174 117 166Z')
    + s('ellipse', '#9a6a3f', cx=131, cy=136, rx=17, ry=3.5, stroke_width=2.5)
    + z('circle', SK, cx=114, cy=154, r=9)
    + s('path', d='M126 128 Q122 120 126 114 Q130 108 126 100 M138 128 Q134 120 138 114 Q142 108 138 100', stroke_width=2.5)
    + s('path', d='M40 60 Q44 54 48 60 Q52 66 56 60 M152 52 Q156 46 160 52 Q164 58 168 52', stroke_width=2.5)
)

# 8. meditating cross-legged
ITEMS['person-meditating'] = (
    s('ellipse', '#f6e0c4', cx=100, cy=104, rx=74, ry=74, stroke='none')
    + z('path', '#8fb3e0', d='M40 176 Q44 156 80 156 L120 156 Q156 156 160 176 Q130 186 100 176 Q70 186 40 176Z')
    + body(100, 118, 166, '#7cc4b0', 32)
    + arm('M72 140 Q58 152 56 160', '#7cc4b0') + arm('M128 140 Q142 152 144 160', '#7cc4b0')
    + z('circle', SK, cx=54, cy=164, r=8) + z('circle', SK, cx=146, cy=164, r=8)
    + head(100, 80, '#2b2220') + eyes(100, 80, 'shut') + ck(100, 80) + mouth(100, 80, 'smile')
    + plus(36, 54, 4) + plus(164, 54, 4) + plus(160, 112, 3) + plus(40, 112, 3)
)

# 9. dancing
ITEMS['person-dancing'] = (
    arm('M86 162 Q74 172 60 174', '#5b6b7a') + arm('M112 160 Q122 172 124 184', '#5b6b7a')
    + z('ellipse', '#8b6b4f', cx=56, cy=174, rx=9, ry=6) + z('ellipse', '#8b6b4f', cx=128, cy=184, rx=9, ry=6)
    + arm('M84 130 Q62 120 48 98', '#f07a8a') + arm('M118 132 Q140 136 154 128', '#f07a8a')
    + z('circle', SK, cx=46, cy=92, r=9) + z('circle', SK, cx=160, cy=126, r=9)
    + z('path', '#f07a8a', d='M70 166 Q72 120 100 118 Q128 120 130 166Z', transform='rotate(-8 100 140)')
    + head(106, 84, '#5a4033') + eyes(106, 84, 'happy') + ck(106, 84) + mouth(106, 84, 'open')
    + note(150, 62) + note(42, 148, '#8fc7e8') + s('path', d='M170 92 L178 86 M30 70 L36 76', stroke_width=2.5)
)

# 10. whistling
ITEMS['person-whistling'] = (
    body(88, 138, 186, '#8fb3e0', 34)
    + head(88, 96, '#c9a36b') + eyes(88, 96, 'shut') + ck(88, 96)
    + s('path', d='M74 82 Q78 78 82 82 M94 82 Q98 78 102 82', stroke_width=2.5)
    + s('circle', '#c0504d', cx=98, cy=114, r=3.5, stroke_width=2.5)
    + s('path', d='M110 112 L118 108 M112 120 L120 120', stroke_width=2.5)
    + note(138, 92, '#ffc94d') + note(156, 60, '#e8735a') + note(126, 46, '#7cc4b0')
)

# 11. nodding in agreement
ITEMS['person-nodding'] = (
    body(84, 140, 186, '#ffc94d', 34)
    + head(84, 102, '#2b2220') + eyes(84, 102, 'happy') + ck(84, 102) + mouth(84, 102, 'smile')
    + s('path', d='M46 72 Q40 86 44 100 M38 66 Q30 84 36 104', stroke_width=2.5)
    + z('circle', '#ffffff', cx=146, cy=58, r=28)
    + s('path', '#ffffff', d='M128 78 L118 96 L140 84', stroke_width=3)
    + s('path', '#ffffff', d='M124 80 L136 82', stroke='#ffffff', stroke_width=6)
    + s('path', d='M133 58 L143 69 L161 46', stroke='#7cc4a0', stroke_width=6)
)

# 12. raising a hand to ask
ITEMS['person-raising-hand'] = (
    body(92, 138, 186, '#7cc4b0', 34)
    + arm('M116 146 Q130 110 132 58', '#7cc4b0')
    + z('ellipse', SK, cx=132, cy=48, rx=10, ry=12)
    + head(88, 98, '#5a4033') + eyes(88, 98, 'dot') + ck(88, 98) + mouth(88, 98, 'open')
    + s('path', d='M150 34 L160 28 M154 50 L166 50 M112 32 L106 24', stroke_width=2.5)
)

# 13. daydreaming
ITEMS['person-daydreaming'] = (
    body(74, 142, 186, '#f6a6b8', 34)
    + head(72, 112, '#5a4033') + eyes(72, 112, 'happy', dx=2) + ck(72, 112) + mouth(74, 112, 'smile')
    + arm('M96 168 Q110 156 100 140', '#f6a6b8') + z('circle', SK, cx=98, cy=134, r=9)
    + z('circle', '#ffffff', cx=104, cy=72, r=4) + z('circle', '#ffffff', cx=114, cy=58, r=6)
    + z('path', '#ffffff', d='M112 40 Q108 22 128 22 Q136 8 152 16 Q170 8 176 26 Q188 36 178 50 Q178 66 160 64 Q148 74 134 64 Q114 66 116 52 Q106 48 112 40Z')
    + heart(146, 40, 0.9)
)

# 14. putting a coin into a piggy bank
PG = '#f6a6b8'
ITEMS['person-piggy-bank'] = (
    body(58, 144, 186, '#8fc7e8', 28)
    + arm('M76 156 Q98 140 108 116', '#8fc7e8')
    + z('circle', SK, cx=110, cy=110, r=8)
    + head(56, 108, '#2b2220', 28) + eyes(56, 108, 'dot', 0.82, dx=3) + ck(56, 108, 0.82) + mouth(58, 108, 'smile', 0.82)
    + z('rect', PG, x=112, y=166, width=10, height=16, rx=3) + z('rect', PG, x=154, y=166, width=10, height=16, rx=3)
    + z('path', PG, d='M126 132 L122 116 L138 126Z')
    + z('ellipse', PG, cx=140, cy=152, rx=36, ry=26)
    + s('path', d='M176 150 Q186 146 182 140', stroke_width=2.5)
    + s('path', d='M122 130 L136 130', stroke_width=4)
    + z('ellipse', '#f07a8a', cx=106, cy=154, rx=7, ry=9)
    + dot(104, 151, 1.6) + dot(104, 157, 1.6)
    + dot(120, 144, 3) + ck(118, 140, 0.4)
    + z('circle', '#ffc94d', cx=124, cy=106, r=10) + s('circle', cx=124, cy=106, r=5, stroke_width=2)
    + plus(146, 104, 4) + plus(150, 86, 3)
)

# 15. sad person with an empty wallet
ITEMS['person-empty-wallet'] = (
    body(80, 140, 186, '#b9a99c', 34)
    + head(78, 98, '#5a4033')
    + s('path', d='M60 86 L70 82 M96 86 L86 82', stroke_width=2.5)
    + eyes(78, 98, 'dot') + ck(78, 98) + mouth(78, 98, 'frown')
    + drop(108, 70, 1.0)
    + z('path', '#8b6b4f', d='M114 130 L164 130 L164 152 L114 152Z')
    + s('path', '#5b6b7a', d='M120 136 L158 136 L158 150 L120 150Z', stroke_width=2.5)
    + z('rect', '#9a6a3f', x=112, y=148, width=54, height=30, rx=5)
    + s('path', d='M152 158 L166 158 L166 168 L152 168Z', stroke_width=2.5) + dot(158, 163, 2)
    + z('circle', SK, cx=112, cy=164, r=9)
    + s('circle', '#f4f4f0', cx=140, cy=116, r=5, stroke_width=2) + s('circle', '#f4f4f0', cx=150, cy=102, r=4, stroke_width=2)
    + s('circle', '#f4f4f0', cx=136, cy=94, r=3, stroke_width=2)
    + s('path', d='M162 104 Q168 96 174 104 M154 82 Q160 74 166 82', stroke_width=2.5)
)

# 16. running late with toast in mouth
ITEMS['person-running-late'] = (
    s('path', d='M22 108 L44 108 M18 126 L40 126 M26 144 L46 144', stroke_width=3)
    + arm('M88 158 Q72 168 62 158', '#5b6b7a') + arm('M106 160 Q124 166 128 184', '#5b6b7a')
    + z('ellipse', '#8b6b4f', cx=58, cy=154, rx=9, ry=6) + z('ellipse', '#8b6b4f', cx=134, cy=184, rx=9, ry=6)
    + arm('M80 130 Q62 132 56 116', '#8fb3e0') + arm('M118 132 Q136 140 148 130', '#8fb3e0')
    + z('circle', SK, cx=54, cy=110, r=8) + z('circle', SK, cx=152, cy=126, r=8)
    + z('path', '#8fb3e0', d='M70 166 Q72 118 100 116 Q128 118 130 166Z', transform='rotate(12 100 140)')
    + head(106, 76, '#2b2220') + eyes(106, 76, 'dot', dx=4) + ck(106, 76)
    + z('path', '#d9a66b', d='M114 92 L142 86 Q152 90 146 100 L148 120 L122 124Z')
    + s('path', '#f5d58a', d='M120 97 L140 93 Q144 96 141 100 L142 115 L125 118Z', stroke='none')
    + drop(70, 44, 1.0) + drop(148, 48, 0.8)
)

# 17. checking a wristwatch
ITEMS['person-checking-watch'] = (
    body(86, 140, 186, '#e8735a', 34)
    + arm('M108 160 Q130 150 128 128', '#e8735a')
    + z('circle', SK, cx=130, cy=118, r=10)
    + s('rect', '#5b6b7a', x=118, y=130, width=22, height=8, rx=2, stroke_width=2)
    + z('circle', '#ffffff', cx=152, cy=74, r=22)
    + s('path', d='M152 74 L152 60 M152 74 L162 80', stroke_width=3)
    + s('path', d='M128 68 L132 70 M152 46 L152 52 M176 74 L170 74', stroke_width=2)
    + s('path', d='M134 108 Q140 96 146 98', stroke_width=2, stroke_dasharray='3 5')
    + head(84, 98, '#c9a36b')
    + s('path', d='M64 84 L74 86 M104 84 L94 86', stroke_width=2.5)
    + eyes(84, 98, 'dot', dx=4) + ck(84, 98) + mouth(86, 98, 'flat')
    + drop(46, 72, 0.9)
)

# 18. sleepless at night
ITEMS['person-sleepless'] = (
    z('rect', '#5b6b7a', x=110, y=26, width=64, height=56, rx=4)
    + s('path', d='M142 26 L142 82 M110 54 L174 54', stroke_width=2.5)
    + s('circle', '#ffe27a', cx=126, cy=40, r=8, stroke='none') + s('circle', '#5b6b7a', cx=130, cy=37, r=7, stroke='none')
    + dot(160, 40, 2, '#ffe27a') + dot(126, 68, 2, '#ffe27a') + dot(162, 70, 2.5, '#ffe27a')
    + z('rect', '#8b6b4f', x=24, y=106, width=12, height=78, rx=3)
    + z('rect', '#8b6b4f', x=30, y=150, width=146, height=24, rx=3)
    + z('ellipse', '#ffffff', cx=66, cy=126, rx=32, ry=14)
    + head(70, 112, '#2b2220', 28)
    + eyes(70, 112, 'wide', 0.82) + ck(70, 112, 0.82)
    + s('path', d='M56 120 Q60 123 64 120 M76 120 Q80 123 84 120', stroke='#8fb3e0', stroke_width=2)
    + mouth(70, 112, 'flat', 0.82)
    + z('path', '#8fb3e0', d='M88 124 Q130 116 172 128 L172 156 L60 156 Q66 134 88 124Z')
    + s('path', '#f4f4f0', d='M60 138 Q120 128 172 138', stroke_width=2.5)
)

# 19. hot and fanning
ITEMS['person-hot-fan'] = (
    z('circle', '#ffc94d', cx=160, cy=40, r=14)
    + s('path', d='M160 16 L160 20 M182 40 L178 40 M176 24 L173 27 M144 24 L147 27 M176 56 L173 53', stroke_width=2.5)
    + body(82, 140, 186, '#f5d58a', 34)
    + arm('M106 158 Q124 152 126 136', '#f5d58a')
    + s('path', d='M128 132 L136 112', stroke='#8b6b4f', stroke_width=5)
    + z('ellipse', '#8fc7e8', cx=144, cy=96, rx=20, ry=18, transform='rotate(20 144 96)')
    + s('path', d='M140 100 L134 112 M144 92 L136 112 M150 96 L138 112', stroke_width=1.5)
    + z('circle', SK, cx=128, cy=132, r=9)
    + head(80, 98, '#5a4033') + eyes(80, 98, 'squeeze') + ck(80, 98, 1, '#f07a8a') + mouth(80, 98, 'open')
    + drop(42, 76, 0.9) + drop(116, 64, 0.8) + drop(36, 112, 0.7)
    + s('path', d='M52 40 Q58 34 52 28 M68 44 Q74 38 68 32', stroke_width=2.5)
)

# 20. cold, shivering in a scarf
ITEMS['person-cold-scarf'] = (
    body(100, 138, 186, '#8fb3e0', 34)
    + z('circle', SK, cx=78, cy=160, r=9) + z('circle', SK, cx=122, cy=160, r=9)
    + head(100, 90, '#2b2220')
    + z('path', '#ffffff', d='M70 70 Q72 46 100 44 Q128 46 130 70 Q100 58 70 70Z')
    + z('circle', '#ffffff', cx=100, cy=42, r=8)
    + eyes(100, 92, 'squeeze') + ck(100, 90, 1, '#f6a6b8') + mouth(100, 90, 'wavy')
    + z('rect', '#e8735a', x=66, y=120, width=68, height=16, rx=8)
    + z('rect', '#e8735a', x=112, y=128, width=14, height=36, rx=3)
    + s('path', d='M116 164 L116 170 M121 164 L121 170', stroke_width=2.5)
    + s('path', d='M46 94 L54 100 L46 106 L54 112 M154 94 L146 100 L154 106 L146 112', stroke_width=2.5)
    + s('path', d='M36 50 L36 64 M30 54 L42 60 M30 60 L42 54 M164 30 L164 44 M158 34 L170 40 M158 40 L170 34 M160 150 L160 162 M155 153 L165 159 M155 159 L165 153', stroke_width=2)
)
