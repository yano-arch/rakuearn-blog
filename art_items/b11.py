from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}
SK = '#ffd9b8'


def arm(d, col, w=9):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 5)


def head(cx, cy, hair, skin=SK):
    o = z('circle', skin, cx=cx, cy=cy, r=34)
    o += s('path', hair, d=f'M{cx-34} {cy-2} Q{cx-32} {cy-36} {cx} {cy-35} Q{cx+32} {cy-36} {cx+34} {cy-2} Q{cx+20} {cy-18} {cx} {cy-17} Q{cx-20} {cy-18} {cx-34} {cy-2}Z')
    return o


def body(cx, top, bottom, col, hw=34):
    return z('path', col, d=f'M{cx-hw} {bottom} Q{cx-hw+2} {top+2} {cx} {top} Q{cx+hw-2} {top+2} {cx+hw} {bottom}Z')


def hand(x, y, r=9):
    return z('circle', SK, cx=x, cy=y, r=r)


def drop(x, y, k=1.0, col='#8fc7e8'):
    return z('path', col, d=f'M{x} {y} Q{x-6*k} {y+10*k} {x} {y+14*k} Q{x+6*k} {y+10*k} {x} {y}Z', stroke_width=2.5)


def heart(cx, cy, k=1.0):
    def p(x, y):
        return f'{cx + x*k:.1f} {cy + y*k:.1f}'
    return (f'M{p(0, 14)} C{p(-12, 4)} {p(-20, -4)} {p(-14, -12)} C{p(-8, -20)} {p(0, -15)} {p(0, -8)} '
            f'C{p(0, -15)} {p(8, -20)} {p(14, -12)} C{p(20, -4)} {p(12, 4)} {p(0, 14)}Z')


def star(cx, cy, R, r=None):
    import math
    r = r or R * 0.45
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = R if i % 2 == 0 else r
        pts.append(f'{cx + rr*math.cos(a):.1f} {cy + rr*math.sin(a):.1f}')
    return 'M' + ' L'.join(pts) + 'Z'


def qmark(x, y, k=1.0, col='#f5b971'):
    def p(a, b):
        return f'{x + a*k:.1f} {y + b*k:.1f}'
    d = f'M{p(0, 18)} Q{p(0, 0)} {p(15, 0)} Q{p(30, 0)} {p(30, 14)} Q{p(30, 24)} {p(18, 30)} L{p(18, 40)}'
    return (s('path', d=d, stroke_width=12 * k) + s('path', d=d, stroke=col, stroke_width=6 * k)
            + z('circle', col, cx=round(x + 18*k, 1), cy=round(y + 56*k, 1), r=round(6*k, 1)))


def closed_up(cx, cy):  # happy closed eyes  ^ ^
    return s('path', d=f'M{cx-18} {cy+4} Q{cx-12} {cy-3} {cx-6} {cy+4} M{cx+6} {cy+4} Q{cx+12} {cy-3} {cx+18} {cy+4}', stroke_width=3)


def closed_down(cx, cy):  # peaceful closed eyes
    return s('path', d=f'M{cx-18} {cy} Q{cx-12} {cy+6} {cx-6} {cy} M{cx+6} {cy} Q{cx+12} {cy+6} {cx+18} {cy}', stroke_width=3)


def pompom(cx, cy, R, col):
    import math
    d = ''
    n = 12
    for i in range(n + 1):
        a = math.radians(i * 360 / n)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        if i == 0:
            d = f'M{x:.1f} {y:.1f}'
        else:
            am = math.radians((i - 0.5) * 360 / n)
            qx, qy = cx + (R + 7) * math.cos(am), cy + (R + 7) * math.sin(am)
            d += f' Q{qx:.1f} {qy:.1f} {x:.1f} {y:.1f}'
    return z('path', col, d=d + 'Z') + s('path', d=f'M{cx-8} {cy-6} L{cx-2} {cy} M{cx+6} {cy-8} L{cx+2} {cy-2} M{cx-4} {cy+8} L{cx} {cy+2}', stroke_width=2.5)


RED = '#c0504d'

# 1. laughing out loud
ITEMS['person-laughing'] = (
    body(100, 136, 186, '#f5d58a')
    + arm('M70 150 Q70 168 86 168', '#f5d58a') + arm('M130 150 Q130 168 114 168', '#f5d58a')
    + hand(88, 168) + hand(112, 168)
    + head(100, 92, '#5a4033')
    + closed_up(100, 90) + cheeks(80, 120, 104)
    + s('path', RED, d='M86 106 Q100 104 114 106 Q112 126 100 126 Q88 126 86 106Z', stroke_width=2.5)
    + s('path', '#f6a6b8', d='M92 120 Q100 114 108 120 Q104 125 100 125 Q96 125 92 120Z', stroke='none')
    + s('path', d='M48 62 L36 54 M44 80 L30 80 M50 98 L38 104 M152 62 L164 54 M156 80 L170 80 M150 98 L162 104', stroke_width=3)
)

# 2. embarrassed, scratching head
ITEMS['person-embarrassed'] = (
    body(100, 136, 186, '#8fc7e8')
    + arm('M122 150 Q150 136 138 74', '#8fc7e8')
    + head(100, 92, '#2b2220')
    + dot(88, 96) + dot(112, 96)
    + f'<ellipse cx="80" cy="106" rx="10" ry="5.5" fill="#f07a8a" stroke="none"/><ellipse cx="120" cy="106" rx="10" ry="5.5" fill="#f07a8a" stroke="none"/>'
    + s('path', d='M76 104 L80 108 M82 104 L86 108 M114 104 L118 108 M120 104 L124 108', stroke_width=1.8)
    + s('path', d='M92 114 Q96 118 100 114 Q104 118 108 114', stroke_width=2.5)
    + hand(136, 68, 10)
    + s('path', d='M150 52 L156 46 M154 62 L162 60', stroke_width=2.5)
    + drop(64, 64, 1.0)
)

# 3. worried, hands clasped
ITEMS['person-worried'] = (
    body(100, 136, 186, '#b9a99c')
    + arm('M72 158 Q80 170 96 160', '#b9a99c') + arm('M128 158 Q120 170 104 160', '#b9a99c')
    + head(100, 92, '#c9a36b')
    + s('path', d='M80 86 L92 82 M108 82 L120 86', stroke_width=2.5)
    + dot(88, 96) + dot(112, 96) + cheeks(80, 120, 106)
    + s('path', d='M90 118 Q95 113 100 118 Q105 123 110 118', stroke_width=2.5)
    + hand(94, 156, 10) + hand(106, 158, 10)
    + drop(132, 62, 1.3) + drop(146, 84, 0.9)
)

# 4. exhausted, slumped, sigh
ITEMS['person-tired'] = (
    z('path', '#9ccf7a', d='M62 188 Q64 146 100 140 Q136 146 138 188Z')
    + arm('M70 160 Q62 176 64 184', '#9ccf7a') + arm('M130 160 Q138 176 136 184', '#9ccf7a')
    + hand(64, 184, 8) + hand(136, 184, 8)
    + head(96, 102, '#5a4033')
    + s('path', d='M78 106 L92 106 M100 106 L114 106', stroke_width=3)
    + s('path', d='M76 96 L90 100 M116 96 L102 100', stroke_width=2.5)
    + cheeks(76, 116, 116)
    + s('ellipse', OUT, cx=96, cy=124, rx=4, ry=3, stroke='none')
    + z('path', '#f4f4f0', d='M126 128 Q140 120 150 126 Q166 118 172 132 Q182 140 170 150 Q160 160 146 152 Q130 156 128 144 Q118 138 126 128Z')
    + s('path', d='M106 126 Q114 128 120 134', stroke_width=2.5)
    + s('path', d='M60 46 Q64 54 60 62 Q56 70 60 78 M136 46 Q140 54 136 62 Q132 70 136 78', stroke='#8fb3e0', stroke_width=3)
)

# 5. shy, peeking from behind hands
ITEMS['person-shy'] = (
    body(100, 136, 186, '#f6a6b8')
    + arm('M74 152 Q64 136 78 118', '#f6a6b8') + arm('M126 152 Q136 136 122 118', '#f6a6b8')
    + head(100, 92, '#5a4033')
    + dot(88, 90) + dot(112, 90)
    + f'<ellipse cx="78" cy="98" rx="8" ry="4" fill="#f07a8a" stroke="none"/><ellipse cx="122" cy="98" rx="8" ry="4" fill="#f07a8a" stroke="none"/>'
    + z('rect', SK, x=72, y=100, width=26, height=30, rx=11)
    + z('rect', SK, x=102, y=100, width=26, height=30, rx=11)
    + s('path', d='M79 101 L79 110 M86 100 L86 110 M114 100 L114 110 M121 101 L121 110', stroke_width=2)
    + s('path', '#f07a8a', d=heart(156, 60, 0.7), stroke_width=2)
    + s('path', '#f07a8a', d=heart(46, 76, 0.5), stroke_width=2)
)

# 6. confused, question marks
ITEMS['person-confused'] = (
    body(96, 138, 186, '#7cc4b0')
    + head(96, 96, '#2b2220')
    + s('path', d='M76 84 L88 86 M104 82 L116 78', stroke_width=2.5)
    + dot(84, 98) + dot(108, 96) + cheeks(76, 118, 110)
    + s('path', d='M88 118 Q92 114 96 118 Q100 122 104 118', stroke_width=2.5)
    + qmark(132, 26, 0.85) + qmark(42, 34, 0.6, '#8fb3e0') + qmark(150, 98, 0.5, '#f6a6b8')
)

# 7. proud, hands on hips
ITEMS['person-proud'] = (
    arm('M76 146 Q38 148 62 176', '#e8735a') + arm('M124 146 Q162 148 138 176', '#e8735a')
    + body(100, 136, 186, '#e8735a')
    + hand(66, 174) + hand(134, 174)
    + head(100, 90, '#5a4033')
    + closed_up(100, 88) + cheeks(80, 120, 100)
    + s('path', d='M92 110 Q100 118 108 110', stroke_width=3)
    + s('path', d='M80 76 L92 74 M108 74 L120 76', stroke_width=2.5)
    + z('path', '#ffe27a', d=star(152, 44, 11), stroke_width=2.5)
    + z('path', '#ffe27a', d=star(46, 52, 7), stroke_width=2.5)
)

# 8. making a wish
ITEMS['person-wishing'] = (
    body(100, 140, 186, '#8fb3e0')
    + arm('M74 160 Q82 158 94 146', '#8fb3e0') + arm('M126 160 Q118 158 106 146', '#8fb3e0')
    + head(100, 98, '#c9a36b')
    + closed_down(100, 98) + cheeks(80, 120, 110)
    + s('path', d='M95 118 Q100 122 105 118', stroke_width=2.5)
    + z('path', SK, d='M100 120 Q90 132 92 150 Q100 154 108 150 Q110 132 100 120Z')
    + s('path', d='M100 124 L100 150', stroke_width=2)
    + z('path', '#ffe27a', d=star(100, 36, 16))
    + s('path', d='M72 30 L66 26 M128 30 L134 26 M78 46 L72 50 M122 46 L128 50', stroke_width=2.5)
)

# 9. clapping
ITEMS['person-clapping'] = (
    body(100, 136, 186, '#f5b971')
    + arm('M72 156 Q70 140 92 132', '#f5b971') + arm('M128 156 Q130 140 108 132', '#f5b971')
    + head(100, 86, '#2b2220')
    + closed_up(100, 84) + cheeks(80, 120, 96)
    + s('path', RED, d='M92 102 Q100 114 108 102Z', stroke_width=2.5)
    + z('ellipse', SK, cx=94, cy=128, rx=8, ry=12, transform='rotate(-15 94 128)')
    + z('ellipse', SK, cx=106, cy=128, rx=8, ry=12, transform='rotate(15 106 128)')
    + s('path', d='M74 116 L64 110 M72 128 L60 128 M74 140 L64 146 M126 116 L136 110 M128 128 L140 128 M126 140 L136 146', stroke_width=3)
)

# 10. pointing to the side
ITEMS['person-pointing'] = (
    body(86, 136, 186, '#9ccf7a')
    + arm('M108 150 Q130 136 150 124', '#9ccf7a')
    + head(86, 92, '#5a4033')
    + dot(84, 94) + dot(108, 94) + cheeks(74, 114, 105)
    + s('path', RED, d='M90 110 Q98 122 106 110Z', stroke_width=2.5)
    + z('rect', SK, x=150, y=114, width=20, height=9, rx=4.5, transform='rotate(-25 150 118)')
    + hand(152, 124, 10)
    + s('path', d='M168 88 L174 80 M178 100 L186 96', stroke_width=2.5)
)

# 11. OK sign, arms making a circle over the head
ITEMS['person-ok-sign'] = (
    body(100, 146, 188, '#7cc4b0', 32)
    + arm('M74 160 Q44 120 56 76 Q66 44 94 36', '#7cc4b0') + arm('M126 160 Q156 120 144 76 Q134 44 106 36', '#7cc4b0')
    + hand(96, 34, 9) + hand(104, 34, 9)
    + head(100, 108, '#2b2220')
    + dot(88, 110) + dot(112, 110) + cheeks(80, 120, 120)
    + s('path', RED, d='M92 124 Q100 136 108 124Z', stroke_width=2.5)
)

# 12. X sign, arms crossed
ITEMS['person-x-sign'] = (
    body(100, 136, 186, '#e04b5a')
    + head(100, 90, '#5a4033')
    + s('path', d='M80 80 L92 84 M120 80 L108 84', stroke_width=2.5)
    + dot(88, 92) + dot(112, 92) + cheeks(80, 120, 102)
    + s('path', d='M92 112 L108 112', stroke_width=3)
    + arm('M70 172 L128 128', '#e04b5a', 14) + arm('M130 172 L72 128', '#e04b5a', 14)
    + hand(130, 126, 10) + hand(70, 126, 10)
)

# 13. shrugging, palms up
ITEMS['person-shrugging'] = (
    arm('M74 154 Q48 160 42 134', '#f5d58a') + arm('M126 154 Q152 160 158 134', '#f5d58a')
    + body(100, 138, 186, '#f5d58a')
    + z('path', SK, d='M28 128 Q42 138 56 128 Q50 120 42 120 Q34 120 28 128Z')
    + z('path', SK, d='M144 128 Q158 138 172 128 Q166 120 158 120 Q150 120 144 128Z')
    + head(100, 94, '#2b2220')
    + s('path', d='M78 76 Q86 70 94 76 M106 76 Q114 70 122 76', stroke_width=2.5)
    + dot(88, 94) + dot(112, 94) + cheeks(80, 120, 106)
    + s('path', d='M92 114 Q100 110 108 114', stroke_width=2.5)
)

# 14. big yawn
ITEMS['person-yawning'] = (
    body(100, 136, 186, '#8fb3e0')
    + arm('M126 156 Q148 150 132 128', '#8fb3e0')
    + head(100, 92, '#c9a36b')
    + s('path', d='M80 92 L93 94 M107 94 L120 92', stroke_width=3)
    + cheeks(78, 122, 104)
    + z('ellipse', RED, cx=100, cy=112, rx=10, ry=13)
    + s('ellipse', '#f6a6b8', cx=100, cy=118, rx=5, ry=4, stroke='none')
    + hand(128, 122, 9)
    + drop(76, 96, 0.7)
    + s('path', d='M140 50 Q148 42 156 50 Q164 58 172 50', stroke_width=2.5)
)

# 15. hungry, fork and drool
ITEMS['person-hungry'] = (
    body(96, 136, 186, '#f6a6b8')
    + arm('M118 156 Q140 150 144 128', '#f6a6b8')
    + s('rect', '#c9d3db', x=142, y=74, width=7, height=56, rx=3.5)
    + z('path', '#c9d3db', d='M134 54 L134 72 Q134 82 145.5 82 Q157 82 157 72 L157 54 L152 54 L152 70 L148 70 L148 54 L143 54 L143 70 L139 70 L139 54Z', stroke_width=2.5)
    + hand(144, 130, 10)
    + head(96, 92, '#2b2220')
    + dot(84, 92) + dot(108, 92) + cheeks(76, 116, 104)
    + s('path', RED, d='M86 108 Q96 124 106 108Z', stroke_width=2.5)
    + drop(104, 116, 1.0)
    + s('path', d='M40 120 Q46 114 52 120 Q58 126 64 120 M40 134 Q46 128 52 134 Q58 140 64 134', stroke_width=2.5)
)

# 16. in love, hearts floating
ITEMS['person-in-love'] = (
    body(100, 136, 186, '#f07a8a')
    + arm('M74 152 Q60 136 70 112', '#f07a8a') + arm('M126 152 Q140 136 130 112', '#f07a8a')
    + head(100, 92, '#5a4033')
    + s('path', '#e04b5a', d=heart(88, 94, 0.45), stroke='none') + s('path', '#e04b5a', d=heart(112, 94, 0.45), stroke='none')
    + cheeks(80, 120, 106)
    + s('path', d='M94 113 Q100 119 106 113', stroke_width=2.5)
    + hand(70, 108, 10) + hand(130, 108, 10)
    + z('path', '#f07a8a', d=heart(150, 46, 0.9)) + z('path', '#f6a6b8', d=heart(52, 52, 0.7))
    + z('path', '#f6a6b8', d=heart(168, 82, 0.5))
)

# 17. scared, shivering
ITEMS['person-scared'] = (
    body(100, 136, 186, '#c9d3db')
    + arm('M76 156 Q74 136 90 126', '#c9d3db') + arm('M124 156 Q126 136 110 126', '#c9d3db')
    + head(100, 86, '#2b2220')
    + s('path', d='M80 76 L92 72 M108 72 L120 76', stroke_width=2.5)
    + s('circle', '#ffffff', cx=88, cy=86, r=6, stroke_width=2.5) + s('circle', '#ffffff', cx=112, cy=86, r=6, stroke_width=2.5)
    + dot(88, 87, 2.5) + dot(112, 87, 2.5)
    + s('path', d='M88 106 Q92 102 96 106 Q100 110 104 106 Q108 102 112 106', stroke_width=2.5)
    + s('path', d='M80 52 L80 62 M90 50 L90 60 M100 50 L100 60', stroke='#8fb3e0', stroke_width=2.5)
    + hand(92, 124, 9) + hand(108, 124, 9)
    + s('path', d='M50 70 Q44 76 50 82 Q56 88 50 94 M38 120 Q32 126 38 132 Q44 138 38 144 M150 70 Q156 76 150 82 Q144 88 150 94 M162 120 Q168 126 162 132 Q156 138 162 144', stroke_width=3)
)

# 18. cheering with pom-poms
ITEMS['person-cheering-pompoms'] = (
    arm('M76 150 Q56 120 50 76', '#f5d58a') + arm('M124 150 Q144 120 150 76', '#f5d58a')
    + body(100, 136, 186, '#e8735a')
    + s('path', '#ffffff', d='M80 146 L100 162 L120 146', stroke_width=2.5)
    + head(100, 96, '#c9a36b')
    + z('circle', '#c9a36b', cx=66, cy=72, r=9) + z('circle', '#c9a36b', cx=134, cy=72, r=9)
    + closed_up(100, 94) + cheeks(80, 120, 106)
    + s('path', RED, d='M92 112 Q100 124 108 112Z', stroke_width=2.5)
    + pompom(48, 58, 18, '#f07a8a') + pompom(152, 58, 18, '#f07a8a')
)

# 19. bye-bye, big wave
ITEMS['person-bye-bye'] = (
    body(92, 136, 186, '#9ccf7a')
    + arm('M114 152 Q138 130 142 82', '#9ccf7a')
    + head(90, 96, '#5a4033')
    + dot(78, 96) + dot(102, 96) + cheeks(70, 110, 108)
    + s('path', RED, d='M82 112 Q90 124 98 112Z', stroke_width=2.5)
    + z('ellipse', SK, cx=144, cy=68, rx=13, ry=16, transform='rotate(15 144 68)')
    + s('path', d='M126 50 Q122 40 126 30 M116 56 Q110 42 116 28 M162 50 Q168 42 166 30 M172 58 Q182 44 176 30', stroke_width=3)
)

# 20. hugging a big heart
ITEMS['person-hugging-heart'] = (
    body(100, 120, 182, '#8fc7e8', 38)
    + head(100, 76, '#2b2220')
    + closed_up(100, 74) + cheeks(80, 120, 86)
    + s('path', d='M93 94 Q100 101 107 94', stroke_width=2.5)
    + z('path', '#f07a8a', d=heart(100, 146, 2.4))
    + arm('M64 130 Q58 156 82 158', '#8fc7e8') + arm('M136 130 Q142 156 118 158', '#8fc7e8')
    + hand(84, 158, 9) + hand(116, 158, 9)
)
