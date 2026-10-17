from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}

SK = '#ffd9b8'
RED = '#c0504d'


def sface(cx, cy, r, hair, mouth='smile', eyes='dot', hair_on=True):
    """face() at any radius, with extra eye/mouth variants"""
    k = r / 34
    def p(dx, dy):
        return f'{cx + dx * k:.1f} {cy + dy * k:.1f}'
    o = z('circle', SK, cx=cx, cy=cy, r=r)
    if hair_on:
        o += s('path', hair, d=f'M{p(-34,-2)} Q{p(-32,-36)} {p(0,-35)} Q{p(32,-36)} {p(34,-2)} '
                               f'Q{p(20,-18)} {p(0,-17)} Q{p(-20,-18)} {p(-34,-2)}Z')
    er = max(2.5, 3.5 * k)
    sw = 2.5
    if eyes == 'dot':
        o += dot(cx - 12 * k, cy + 2 * k, er) + dot(cx + 12 * k, cy + 2 * k, er)
    elif eyes == 'happy':
        for sx in (-1, 1):
            o += s('path', d=f'M{p(sx*12-6,4)} Q{p(sx*12,-4)} {p(sx*12+6,4)}', stroke_width=sw)
    elif eyes == 'closed':
        for sx in (-1, 1):
            o += s('path', d=f'M{p(sx*12-6,1)} Q{p(sx*12,7)} {p(sx*12+6,1)}', stroke_width=sw)
    elif eyes == 'cry':
        o += s('path', d=f'M{p(-18,-4)} L{p(-8,2)} L{p(-18,8)}', stroke_width=sw)
        o += s('path', d=f'M{p(18,-4)} L{p(8,2)} L{p(18,8)}', stroke_width=sw)
    elif eyes == 'wink':
        o += dot(cx - 12 * k, cy + 2 * k, er)
        o += s('path', d=f'M{p(6,4)} Q{p(12,-4)} {p(18,4)}', stroke_width=sw)
    o += cheeks(cx - 20 * k, cx + 20 * k, cy + 13 * k, 7 * k, 4 * k)
    if mouth == 'smile':
        o += s('path', d=f'M{p(-6,16)} Q{p(0,21)} {p(6,16)}', stroke_width=sw)
    elif mouth == 'open':
        o += s('path', RED, d=f'M{p(-8,14)} Q{p(0,28)} {p(8,14)}Z', stroke_width=sw)
    elif mouth == 'big':
        o += s('path', RED, d=f'M{p(-11,13)} Q{p(0,32)} {p(11,13)}Z', stroke_width=sw)
    elif mouth == 'wail':
        o += s('ellipse', RED, cx=cx, cy=cy + 20 * k, rx=9 * k, ry=10 * k, stroke_width=sw)
    elif mouth == 'o':
        o += s('circle', RED, cx=cx, cy=cy + 18 * k, r=4 * k, stroke_width=sw)
    elif mouth == 'calm':
        o += s('path', d=f'M{p(-4,17)} Q{p(0,20)} {p(4,17)}', stroke_width=sw)
    return o


def torso(cx, top, bottom, w, col):
    return z('path', col, d=f'M{cx-w} {bottom} Q{cx-w+2} {top+2} {cx} {top} Q{cx+w-2} {top+2} {cx+w} {bottom}Z')


def limb(d, col, w=13):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 6)


def hand(x, y, r=8):
    return z('circle', SK, cx=x, cy=y, r=r)


def heart(cx, cy, k, col='#f07a8a', zz=True, sw=3):
    d = (f'M{cx} {cy+16*k} C{cx-12*k} {cy+6*k} {cx-20*k} {cy-2*k} {cx-14*k} {cy-12*k} '
         f'C{cx-8*k} {cy-20*k} {cx} {cy-15*k} {cx} {cy-8*k} C{cx} {cy-15*k} {cx+8*k} {cy-20*k} {cx+14*k} {cy-12*k} '
         f'C{cx+20*k} {cy-2*k} {cx+12*k} {cy+6*k} {cx} {cy+16*k}Z')
    return z('path', col, d=d) if zz else s('path', col, d=d, stroke_width=sw)


def spark(cx, cy, r, col='#ffe27a', sw=2):
    q = r * 0.28
    d = (f'M{cx} {cy-r} Q{cx+q} {cy-q} {cx+r} {cy} Q{cx+q} {cy+q} {cx} {cy+r} '
         f'Q{cx-q} {cy+q} {cx-r} {cy} Q{cx-q} {cy-q} {cx} {cy-r}Z')
    return s('path', col, d=d, stroke_width=sw)


def drop(x, y, h=12, col='#8fc7e8'):
    w = h * 0.45
    return s('path', col, d=f'M{x} {y} Q{x+w} {y+h*0.6} {x} {y+h} Q{x-w} {y+h*0.6} {x} {y}Z', stroke_width=2)


# 1. child in a raincoat and boots
ITEMS['person-raincoat'] = (
    drop(34, 40) + drop(166, 52) + drop(42, 104) + drop(170, 120) + drop(150, 26, 10)
    + z('path', '#e8735a', d='M76 150 L94 150 L94 178 L70 178 Q68 172 76 170Z')
    + z('path', '#e8735a', d='M106 150 L124 150 L124 170 Q132 172 130 178 L106 178Z')
    + z('circle', '#ffe27a', cx=100, cy=80, r=44)
    + torso(100, 118, 160, 38, '#ffe27a')
    + s('path', d='M100 122 L100 160', stroke_width=2.5)
    + dot(92, 136, 3) + dot(92, 154, 3)
    + limb('M70 136 Q60 150 62 160', '#ffe27a') + hand(63, 162, 7)
    + limb('M130 136 Q140 150 138 160', '#ffe27a') + hand(137, 162, 7)
    + sface(100, 86, 32, '#5a4033', 'open')
)

# 2. watering plants with a watering can
ITEMS['person-gardening'] = (
    torso(72, 112, 176, 34, '#9ccf7a')
    + face(72, 78, SK, '#2b2220', 'smile')
    + limb('M96 130 Q110 132 120 128', '#9ccf7a')
    + z('path', '#8fc7e8', d='M118 112 L152 112 L148 146 L122 146Z')
    + s('path', d='M126 112 Q135 92 144 112', stroke_width=4)
    + z('path', '#8fc7e8', d='M150 124 L176 102 L180 108 L152 134Z')
    + hand(122, 128, 8)
    + drop(176, 116, 9) + drop(168, 128, 9) + drop(180, 134, 9)
    + s('path', d='M172 172 L172 156', stroke_width=2.5)
    + s('path', '#7cc4a0', d='M172 160 Q160 160 158 150 Q170 148 172 160Z', stroke_width=2)
    + s('path', '#7cc4a0', d='M172 158 Q182 154 184 146 Q174 144 172 158Z', stroke_width=2)
    + z('path', '#e8735a', d='M160 170 L184 170 L180 184 L164 184Z')
)

# 3. person sitting on a park bench
ITEMS['person-on-bench'] = (
    z('rect', '#d9a66b', x=32, y=88, width=136, height=14, rx=4)
    + z('rect', '#d9a66b', x=32, y=108, width=136, height=14, rx=4)
    + z('rect', '#5b6b7a', x=44, y=134, width=10, height=46)
    + z('rect', '#5b6b7a', x=146, y=134, width=10, height=46)
    + torso(100, 100, 140, 32, '#8fb3e0')
    + z('rect', '#d9a66b', x=28, y=130, width=144, height=14, rx=4)
    + z('rect', '#5b6b7a', x=80, y=128, width=18, height=40, rx=6)
    + z('rect', '#5b6b7a', x=104, y=128, width=18, height=40, rx=6)
    + z('ellipse', '#e8735a', cx=86, cy=172, rx=13, ry=7) + z('ellipse', '#e8735a', cx=116, cy=172, rx=13, ry=7)
    + hand(74, 130, 8) + hand(128, 130, 8)
    + face(100, 64, SK, '#c9a36b', 'smile')
)

# 4. lying on a sofa with a phone
ITEMS['person-lazy-sofa'] = (
    z('rect', '#8fb3e0', x=28, y=96, width=144, height=40, rx=14)
    + z('rect', '#5b6b7a', x=40, y=160, width=10, height=14, rx=2)
    + z('rect', '#5b6b7a', x=150, y=160, width=10, height=14, rx=2)
    + z('rect', '#8fb3e0', x=28, y=128, width=144, height=34, rx=8)
    + z('rect', '#8fb3e0', x=18, y=110, width=26, height=52, rx=12)
    + z('rect', '#8fb3e0', x=156, y=110, width=26, height=52, rx=12)
    + limb('M120 120 Q144 116 160 104', '#5b6b7a', 15)
    + z('ellipse', '#ffe27a', cx=166, cy=100, rx=9, ry=6, transform='rotate(-30 166 100)')
    + z('ellipse', '#f5b971', cx=94, cy=120, rx=36, ry=17)
    + sface(50, 96, 28, '#5a4033', 'smile')
    + limb('M80 114 Q92 96 100 70', '#f5b971')
    + z('rect', '#5b6b7a', x=88, y=34, width=22, height=34, rx=4, transform='rotate(-10 99 51)')
    + s('rect', '#d8eef8', x=92, y=39, width=14, height=22, rx=2, transform='rotate(-10 99 51)', stroke_width=2)
    + hand(101, 68, 7)
)

# 5. two friends laughing together
ITEMS['friends-laughing'] = (
    torso(64, 124, 178, 32, '#e8735a')
    + torso(136, 124, 178, 32, '#7cc4b0')
    + limb('M150 140 Q164 154 154 164', '#7cc4b0') + hand(152, 166, 7)
    + limb('M86 140 Q104 136 116 132', '#e8735a') + hand(118, 132, 7)
    + sface(64, 92, 30, '#2b2220', 'big', 'happy')
    + sface(136, 92, 30, '#c9a36b', 'big', 'happy')
    + s('path', d='M36 46 L28 38 M52 40 L50 30 M164 40 L172 32 M150 36 L150 26', stroke_width=2.5)
    + spark(100, 52, 8)
)

# 6. three friends posing together
ITEMS['friends-group-photo'] = (
    torso(50, 128, 180, 28, '#f6a6b8')
    + torso(150, 128, 180, 28, '#8fb3e0')
    + sface(50, 102, 26, '#5a4033', 'smile')
    + sface(150, 102, 26, '#2b2220', 'smile', 'wink')
    + torso(100, 118, 182, 30, '#ffc94d')
    + limb('M76 140 Q66 150 60 150', '#ffc94d')
    + limb('M124 140 Q134 150 140 150', '#ffc94d')
    + sface(100, 88, 30, '#c9a36b', 'open')
    + spark(36, 46, 9) + spark(166, 50, 7) + spark(150, 30, 5)
)

# 7. welcoming with open arms
ITEMS['person-welcome'] = (
    torso(100, 118, 180, 36, '#f5b971')
    + limb('M72 132 Q52 122 40 100', '#f5b971') + hand(38, 96, 9)
    + limb('M128 132 Q148 122 160 100', '#f5b971') + hand(162, 96, 9)
    + face(100, 82, SK, '#5a4033', 'open')
    + spark(36, 56, 8) + spark(164, 56, 8) + spark(176, 136, 6) + spark(24, 136, 6)
)

# 8. holding a card with a heart
ITEMS['person-thank-you-card'] = (
    torso(100, 112, 180, 36, '#7cc4b0')
    + face(100, 76, SK, '#2b2220', 'smile')
    + z('rect', '#ffffff', x=66, y=118, width=68, height=52, rx=4)
    + heart(100, 142, 0.85)
    + hand(66, 150, 8) + hand(134, 150, 8)
    + heart(164, 56, 0.5, zz=False, sw=2) + heart(36, 76, 0.4, zz=False, sw=2)
)

# 9. smiling and making a peace sign
ITEMS['person-peace-sign'] = (
    torso(92, 118, 180, 36, '#f6a6b8')
    + limb('M118 136 Q140 126 146 100', '#f6a6b8')
    + z('ellipse', SK, cx=140, cy=66, rx=5.5, ry=14, transform='rotate(-14 140 66)')
    + z('ellipse', SK, cx=158, cy=68, rx=5.5, ry=14, transform='rotate(16 158 68)')
    + z('circle', SK, cx=148, cy=88, r=11)
    + s('path', d='M141 90 Q146 94 152 92', stroke_width=2)
    + face(88, 82, SK, '#5a4033', 'open')
    + spark(42, 44, 8) + spark(176, 40, 6)
)

# 10. opening a present with sparkles
ITEMS['person-opening-present'] = (
    torso(100, 102, 150, 34, '#8fb3e0')
    + face(100, 66, SK, '#c9a36b', 'o')
    + spark(76, 112, 9) + spark(104, 106, 7) + spark(124, 118, 6)
    + z('rect', '#9ccf7a', x=56, y=128, width=88, height=54, rx=3)
    + s('rect', '#e8735a', x=92, y=128, width=16, height=54, stroke_width=2.5)
    + z('rect', '#9ccf7a', x=134, y=100, width=48, height=16, rx=3, transform='rotate(28 158 108)')
    + s('rect', '#e8735a', x=150, y=100, width=12, height=16, transform='rotate(28 158 108)', stroke_width=2.5)
    + hand(58, 136, 8) + hand(142, 136, 8)
    + s('path', d='M36 98 L28 92 M38 112 L28 112 M88 26 L84 18', stroke_width=2.5)
)

# 11. pregnant woman gently holding her belly
ITEMS['pregnant-woman'] = (
    z('path', '#5a4033', d='M62 70 Q60 40 94 36 Q128 40 126 70 L130 118 L58 118Z')
    + z('path', '#f6a6b8', d='M60 182 Q60 116 94 106 Q118 108 122 126 Q152 140 148 166 Q144 182 124 182Z')
    + s('path', d='M112 130 Q100 136 98 150', stroke_width=2.5)
    + hand(122, 132, 8) + hand(136, 170, 8)
    + face(94, 72, SK, '#5a4033', 'smile')
    + heart(156, 98, 0.55, zz=False, sw=2) + spark(40, 140, 6)
)

# 12. newborn baby swaddled in a blanket
ITEMS['newborn-baby'] = (
    z('ellipse', '#8fc7e8', cx=100, cy=112, rx=50, ry=68)
    + s('path', d='M100 70 Q102 58 110 60', stroke_width=2.5)
    + sface(100, 88, 28, '#5a4033', 'calm', 'closed', hair_on=False)
    + z('path', '#8fc7e8', d='M54 118 Q90 116 146 158 Q136 180 100 180 Q60 178 52 140Z')
    + z('path', '#8fc7e8', d='M148 118 Q118 120 84 150 Q100 162 130 168 Q150 150 148 118Z')
    + s('path', d='M78 160 Q96 168 112 172', stroke_width=2)
    + spark(160, 54, 7) + spark(40, 64, 5)
)

# 13. toddler taking first steps
ITEMS['toddler-first-steps'] = (
    z('ellipse', '#f6e0c4', cx=82, cy=170, rx=10, ry=12, transform='rotate(-10 82 170)')
    + z('ellipse', '#f6e0c4', cx=118, cy=166, rx=10, ry=12, transform='rotate(14 118 166)')
    + torso(100, 102, 160, 30, '#f5d58a')
    + limb('M74 118 Q58 110 50 92', '#f5d58a') + hand(48, 88, 8)
    + limb('M126 118 Q142 110 150 92', '#f5d58a') + hand(152, 88, 8)
    + sface(100, 66, 32, '#c9a36b', 'open')
    + s('path', d='M164 132 L176 128 M164 146 L178 146', stroke_width=2.5)
)

# 14. child having a tantrum
ITEMS['kid-tantrum'] = (
    z('ellipse', '#8fb3e0', cx=58, cy=170, rx=22, ry=10, transform='rotate(-20 58 170)')
    + z('ellipse', '#8fb3e0', cx=142, cy=170, rx=22, ry=10, transform='rotate(20 142 170)')
    + torso(100, 118, 176, 32, '#e8735a')
    + limb('M74 132 Q54 120 46 98', '#e8735a') + hand(44, 92, 8)
    + limb('M126 132 Q146 120 154 98', '#e8735a') + hand(156, 92, 8)
    + sface(100, 84, 32, '#2b2220', 'wail', 'cry')
    + drop(58, 64, 12) + drop(146, 60, 12) + drop(40, 124, 10)
    + s('path', d='M78 36 L72 26 M100 30 L100 18 M122 36 L128 26', stroke_width=2.5)
    + s('path', d='M164 126 L178 122 M164 138 L178 140 M36 140 L22 138', stroke_width=2.5)
)

# 15. child sleeping hugging a teddy bear
ITEMS['kid-sleeping-teddy'] = (
    z('rect', '#ffffff', x=26, y=74, width=96, height=48, rx=22)
    + z('circle', '#d9a66b', cx=126, cy=86, r=8) + z('circle', '#d9a66b', cx=150, cy=86, r=8)
    + z('circle', '#d9a66b', cx=138, cy=104, r=20)
    + s('ellipse', '#f6e0c4', cx=138, cy=110, rx=8, ry=6, stroke_width=2)
    + dot(131, 100, 2.8) + dot(145, 100, 2.8) + dot(138, 108, 2.2)
    + sface(76, 98, 30, '#5a4033', 'calm', 'closed')
    + z('path', '#8fb3e0', d='M24 182 L24 128 Q100 116 178 124 L178 182Z')
    + s('path', d='M40 150 L166 150', stroke_width=2) + s('path', d='M40 168 L166 168', stroke_width=2)
    + hand(116, 126, 8) + hand(156, 126, 8)
    + s('path', '#ffe27a', d='M166 30 Q150 38 154 54 Q160 66 176 62 Q162 56 164 44 Q164 36 166 30Z', stroke_width=2)
    + spark(40, 40, 6) + spark(130, 40, 5)
)

# 16. grandmother knitting with yarn
ITEMS['grandma-knitting'] = (
    z('circle', '#e8e1d8', cx=92, cy=36, r=13)
    + torso(92, 110, 180, 38, '#7cc4b0')
    + face(92, 74, SK, '#e8e1d8', 'smile')
    + s('circle', cx=80, cy=76, r=8, stroke_width=2) + s('circle', cx=104, cy=76, r=8, stroke_width=2)
    + s('path', d='M88 76 L96 76', stroke_width=2)
    + s('path', d='M62 148 L118 112 M80 112 L132 150', stroke='#b9a99c', stroke_width=4)
    + z('rect', '#f07a8a', x=74, y=126, width=40, height=30, rx=3)
    + s('path', d='M80 134 L86 140 L92 134 L98 140 L104 134 L110 140 M80 146 L86 152 L92 146 L98 152 L104 146 L110 152', stroke_width=2)
    + hand(72, 140, 8) + hand(118, 144, 8)
    + s('path', d='M112 158 Q130 178 142 166', stroke_width=2)
    + z('circle', '#f07a8a', cx=156, cy=166, r=16)
    + s('path', d='M146 156 Q156 166 150 180 M156 152 Q170 162 164 180 M144 168 Q156 160 170 166', stroke_width=2)
)

# 17. grandfather reading a newspaper
ITEMS['grandpa-newspaper'] = (
    z('ellipse', '#e8e1d8', cx=66, cy=78, rx=8, ry=14)
    + z('ellipse', '#e8e1d8', cx=134, cy=78, rx=8, ry=14)
    + torso(100, 110, 180, 38, '#c9a36b')
    + sface(100, 76, 34, '#e8e1d8', 'calm', hair_on=False)
    + s('path', d='M78 54 Q100 44 122 54', stroke_width=2)
    + s('circle', cx=88, cy=78, r=8, stroke_width=2) + s('circle', cx=112, cy=78, r=8, stroke_width=2)
    + s('path', d='M96 78 L104 78', stroke_width=2)
    + s('path', '#e8e1d8', d='M88 92 Q100 86 112 92 Q100 98 88 92Z', stroke_width=2)
    + z('path', '#f4f4f0', d='M40 112 L100 118 L160 112 L160 176 L100 182 L40 176Z')
    + s('path', d='M100 118 L100 182', stroke_width=2)
    + s('rect', '#b9a99c', x=50, y=126, width=40, height=14, rx=2, stroke='none')
    + ''.join(s('path', d=f'M50 {y} L90 {y}', stroke='#b9a99c', stroke_width=3) for y in (150, 160, 170))
    + ''.join(s('path', d=f'M110 {y} L150 {y}', stroke='#b9a99c', stroke_width=3) for y in (130, 140, 150, 160, 170))
    + hand(40, 140, 8) + hand(160, 140, 8)
)


def avatar(cx, cy, r, col):
    hr = 0.34 * r
    hy = cy - 0.24 * r
    sy = cy + 0.71 * r
    sx = 0.704 * r
    ty = cy + 0.2 * r
    return (z('circle', col, cx=cx, cy=cy, r=r)
            + s('path', '#ffffff', d=f'M{cx-sx:.1f} {sy:.1f} Q{cx-sx*0.8:.1f} {ty:.1f} {cx} {ty:.1f} '
                                     f'Q{cx+sx*0.8:.1f} {ty:.1f} {cx+sx:.1f} {sy:.1f} A{r} {r} 0 0 1 {cx-sx:.1f} {sy:.1f}Z')
            + s('circle', '#ffffff', cx=cx, cy=hy, r=hr))


# 18. simple round profile avatar
ITEMS['avatar-person'] = avatar(98, 98, 72, '#8fc7e8')

# 19. three overlapping profile avatars
ITEMS['avatar-group'] = (
    avatar(58, 116, 38, '#f6a6b8') + avatar(142, 116, 38, '#9ccf7a') + avatar(100, 92, 46, '#8fc7e8')
)

# 20. making a heart shape with hands
ITEMS['person-heart-hands'] = (
    torso(100, 118, 180, 38, '#f5d58a')
    + limb('M72 140 Q80 148 90 140', '#f5d58a')
    + limb('M128 140 Q120 148 110 140', '#f5d58a')
    + face(100, 80, SK, '#2b2220', 'smile')
    + s('path', SK, d='M100 158 Q82 146 82 132 Q84 120 96 124 Q100 128 100 134 '
                       'Q100 128 104 124 Q116 120 118 132 Q118 146 100 158Z', stroke_width=7)
    + heart(100, 140, 0.55, sw=2, zz=False)
    + heart(40, 60, 0.5) + heart(162, 48, 0.4, zz=False, sw=2) + heart(166, 104, 0.35, zz=False, sw=2)
)
