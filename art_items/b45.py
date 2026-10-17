from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}


def wh(cx, cy, r):
    return z('circle', '#5b6b7a', cx=cx, cy=cy, r=r) + s('circle', '#c9d3db', cx=cx, cy=cy, r=round(r * 0.42), stroke_width=2.5)


def ground(y, x1=24, x2=178):
    return s('path', d=f'M{x1} {y} L{x2} {y}', stroke_width=2)


SEDAN = 'M26 148 L26 124 Q26 110 42 108 L62 106 L78 80 Q82 74 90 74 L126 74 Q134 74 138 80 L152 106 L162 108 Q176 112 176 126 L176 148Z'


def sedan_parts():
    return (s('path', '#8fc7e8', d='M70 104 L82 84 Q85 81 90 81 L98 81 L98 104Z', stroke_width=2.5)
            + s('path', '#8fc7e8', d='M106 104 L106 81 L124 81 Q129 81 132 85 L142 104Z', stroke_width=2.5)
            + s('path', d='M102 110 L102 140', stroke_width=2.5) + s('path', d='M110 118 L118 118', stroke_width=2.5)
            + s('circle', '#ffe27a', cx=169, cy=118, r=4.5, stroke_width=2.5)
            + s('rect', '#e04b5a', x=24, y=114, width=7, height=9, rx=2, stroke_width=2))


def thick(d, color, w=10, inner=5):
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=color, stroke_width=inner)


# 1 taxi
checker = ''.join(f'<rect x="{x}" y="{126 + (4 if (x // 6) % 2 else 0)}" width="6" height="4" fill="{OUT}" stroke="none"/>' for x in range(30, 172, 6))
ITEMS['taxi'] = (
    z('rect', '#f4f4f0', x=94, y=60, width=28, height=16, rx=4)
    + z('path', '#ffc94d', d=SEDAN) + sedan_parts()
    + s('rect', '#ffffff', x=27, y=126, width=148, height=8, stroke_width=1.5) + checker
    + wh(60, 148, 16) + wh(142, 148, 16) + ground(170))

# 2 police car
ITEMS['police-car'] = (
    z('rect', '#e04b5a', x=92, y=62, width=16, height=14, rx=3) + z('rect', '#8fb3e0', x=108, y=62, width=16, height=14, rx=3)
    + s('path', d='M86 58 L80 52 M130 58 L136 52 M108 54 L108 46', stroke_width=2.5)
    + z('path', '#f4f4f0', d=SEDAN)
    + s('path', '#5b6b7a', d='M26 126 L176 126 L176 148 L26 148Z', stroke_width=2.5)
    + sedan_parts()
    + wh(60, 148, 16) + wh(142, 148, 16) + ground(170))

# 3 fire truck
ITEMS['fire-truck'] = (
    z('rect', '#ffc94d', x=136, y=58, width=16, height=12, rx=3)
    + z('rect', '#e04b5a', x=24, y=88, width=100, height=60, rx=4)
    + z('path', '#e04b5a', d='M120 148 L120 78 Q120 70 128 70 L152 70 Q162 70 166 82 L176 108 Q178 114 178 120 L178 148Z')
    + s('path', '#8fc7e8', d='M130 80 L150 80 Q156 80 159 88 L166 106 L130 106Z', stroke_width=2.5)
    + z('rect', '#f4f4f0', x=26, y=72, width=92, height=14, rx=3)
    + ''.join(s('path', d=f'M{x} 74 L{x} 84', stroke_width=2.5) for x in range(38, 116, 12))
    + s('rect', '#f4f4f0', x=24, y=118, width=154, height=8, stroke_width=2)
    + s('rect', '#f07a8a', x=34, y=96, width=34, height=18, rx=3, stroke_width=2.5)
    + s('rect', '#f07a8a', x=76, y=96, width=34, height=18, rx=3, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=172, cy=134, r=4.5, stroke_width=2.5)
    + wh(52, 150, 15) + wh(96, 150, 15) + wh(152, 150, 15) + ground(172))

# 4 truck
ITEMS['truck'] = (
    z('rect', '#f4f4f0', x=24, y=58, width=106, height=86, rx=5)
    + s('path', d='M40 74 L40 128 M56 74 L56 128', stroke='#c9d3db', stroke_width=2.5)
    + z('path', '#8fb3e0', d='M134 146 L134 86 Q134 78 142 78 L156 78 Q164 78 168 88 L178 114 L178 146Z')
    + s('path', '#8fc7e8', d='M142 88 L156 88 Q160 88 162 92 L170 112 L142 112Z', stroke_width=2.5)
    + s('rect', '#5b6b7a', x=24, y=142, width=154, height=8, rx=2, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=173, cy=128, r=4, stroke_width=2.5)
    + wh(52, 152, 15) + wh(96, 152, 15) + wh(154, 152, 15) + ground(174))

# 5 motorcycle
ITEMS['motorcycle'] = (
    wh(52, 146, 24) + wh(150, 146, 24)
    + thick('M150 146 L134 84', '#c9d3db', 10, 4)
    + thick('M52 146 L92 126', '#c9d3db', 10, 4)
    + z('path', '#e8735a', d='M28 128 Q32 108 58 108 L72 108 L70 118 Q48 116 38 132Z')
    + z('path', '#5b6b7a', d='M50 108 Q50 96 62 96 L98 96 L98 108Z')
    + z('rect', '#b9a99c', x=84, y=110, width=34, height=28, rx=6)
    + z('rect', '#c9d3db', x=46, y=130, width=52, height=9, rx=4.5)
    + z('path', '#e8735a', d='M92 112 Q92 90 112 88 L130 88 Q140 98 134 112Z')
    + s('path', d='M126 82 L144 76', stroke_width=5)
    + z('circle', '#ffe27a', cx=146, cy=98, r=7)
    + ground(172, 20, 180))

# 6 scooter
ITEMS['scooter'] = (
    wh(62, 154, 17) + wh(146, 154, 17)
    + s('path', d='M128 68 L158 62', stroke_width=5)
    + z('path', '#7cc4b0', d='M124 146 L134 72 L148 72 L152 146Z')
    + z('path', '#7cc4b0', d='M34 146 Q28 106 66 104 L94 104 Q102 106 100 118 L98 132 L128 132 L128 146Z')
    + z('path', '#8b6b4f', d='M46 104 Q48 92 64 92 L94 92 Q100 92 98 104Z')
    + z('path', '#7cc4b0', d='M128 148 Q132 130 148 130 Q164 132 168 148Z')
    + z('circle', '#ffe27a', cx=146, cy=86, r=6)
    + s('path', d='M44 122 Q60 116 76 120', stroke='#f4f4f0', stroke_width=4)
    + ground(176))

# 7 electric kick scooter
ITEMS['electric-scooter'] = (
    z('path', '#8fc7e8', d='M138 152 L124 56 L134 54 L148 150Z')
    + z('rect', '#5b6b7a', x=106, y=44, width=46, height=10, rx=5)
    + s('rect', '#e8735a', x=102, y=44, width=12, height=10, rx=4, stroke_width=2.5)
    + s('rect', '#e8735a', x=144, y=44, width=12, height=10, rx=4, stroke_width=2.5)
    + z('rect', '#5b6b7a', x=44, y=144, width=104, height=12, rx=6)
    + s('path', d='M36 160 Q38 146 54 146', stroke_width=3)
    + s('circle', '#ffe27a', cx=134, cy=72, r=4, stroke_width=2)
    + wh(52, 162, 13) + wh(150, 162, 13)
    + s('path', '#ffe27a', d='M96 92 L84 110 L94 110 L86 128 L104 104 L94 104 L102 92Z', stroke_width=2.5)
    + ground(178, 26, 176))

# 8 helicopter
ITEMS['helicopter'] = (
    z('rect', '#e8735a', x=28, y=100, width=44, height=12, rx=4)
    + z('path', '#e8735a', d='M28 106 L26 80 L40 80 L44 102Z')
    + s('circle', '#c9d3db', cx=34, cy=84, r=8, stroke_width=2.5)
    + s('path', d='M96 68 L96 82', stroke_width=6)
    + z('ellipse', '#e8735a', cx=104, cy=112, rx=46, ry=32)
    + s('path', '#8fc7e8', d='M118 82 Q146 88 150 112 L118 112Z', stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=90, cy=104, r=9, stroke_width=2.5)
    + z('rect', '#5b6b7a', x=40, y=60, width=116, height=8, rx=4)
    + s('path', d='M82 142 L78 156 M122 142 L126 156', stroke_width=3)
    + s('path', d='M58 156 L142 156 Q152 156 154 148', stroke_width=5)
    + s('path', '#ffffff', d='M30 176 Q46 168 62 176', stroke_width=2) + s('path', d='M140 178 Q156 170 172 178', stroke_width=2))

# 9 subway
ITEMS['subway'] = (
    z('path', '#5b6b7a', d='M28 178 L28 100 Q28 30 100 30 Q172 30 172 100 L172 178Z')
    + s('path', d='M82 160 L60 178 M118 160 L140 178', stroke='#c9d3db', stroke_width=3)
    + z('rect', '#f4f4f0', x=56, y=56, width=88, height=104, rx=18)
    + s('rect', '#8fc7e8', x=66, y=70, width=68, height=38, rx=6, stroke_width=2.5)
    + s('rect', '#9ccf7a', x=56, y=116, width=88, height=10, stroke_width=2.5)
    + s('circle', '#ffe27a', cx=74, cy=140, r=7, stroke_width=2.5) + s('circle', '#ffe27a', cx=126, cy=140, r=7, stroke_width=2.5)
    + s('rect', '#5b6b7a', x=64, y=158, width=72, height=8, rx=3, stroke_width=2.5)
    + s('rect', '#ffe27a', x=36, y=86, width=8, height=8, rx=2, stroke_width=2) + s('rect', '#ffe27a', x=156, y=86, width=8, height=8, rx=2, stroke_width=2))

# 10 tram
ITEMS['tram'] = (
    s('path', d='M20 50 L180 50', stroke_width=2)
    + s('path', d='M88 74 L100 52 L112 74 M88 52 L112 52', stroke_width=3)
    + z('rect', '#f4f4f0', x=26, y=74, width=148, height=74, rx=16)
    + s('path', '#7cc4b0', d='M26 118 L174 118 L174 132 Q174 148 158 148 L42 148 Q26 148 26 132Z', stroke_width=2.5)
    + ''.join(s('rect', '#8fc7e8', x=x, y=84, width=20, height=22, rx=4, stroke_width=2.5) for x in (38, 66, 114, 142))
    + s('rect', '#f5d58a', x=90, y=84, width=20, height=58, rx=3, stroke_width=2.5) + s('path', d='M100 86 L100 140', stroke_width=2)
    + s('circle', '#ffe27a', cx=168, cy=126, r=4, stroke_width=2)
    + ''.join(z('circle', '#5b6b7a', cx=x, cy=150, r=8) for x in (50, 72, 128, 150))
    + s('path', d='M22 162 L178 162', stroke_width=2.5) + s('path', d='M22 168 L178 168', stroke='#c9d3db', stroke_width=2.5))

# 11 ropeway
ITEMS['ropeway'] = (
    z('path', '#9ccf7a', d='M24 178 L64 118 L88 140 L130 90 L178 178Z')
    + s('path', '#ffffff', d='M120 102 L130 90 L140 104 L134 100 L128 106Z', stroke_width=2.5)
    + s('path', d='M22 40 L180 84', stroke_width=2.5)
    + s('path', d='M100 62 L100 82', stroke_width=4)
    + z('circle', '#5b6b7a', cx=100, cy=62, r=6)
    + z('rect', '#5b6b7a', x=78, y=78, width=44, height=10, rx=4)
    + z('rect', '#e04b5a', x=68, y=86, width=64, height=58, rx=10)
    + s('rect', '#8fc7e8', x=76, y=94, width=48, height=22, rx=4, stroke_width=2.5)
    + s('path', d='M100 94 L100 116', stroke_width=2)
    + s('rect', '#f4f4f0', x=68, y=124, width=64, height=6, stroke_width=2))

# 12 sailboat
ITEMS['sailboat'] = (
    s('path', d='M100 132 L100 34', stroke_width=4)
    + z('path', '#f07a8a', d='M102 34 L120 40 L102 46Z')
    + z('path', '#f4f4f0', d='M106 48 L106 124 L158 124Z')
    + z('path', '#f4f4f0', d='M94 56 L94 124 L48 124Z')
    + z('path', '#e8735a', d='M34 130 L166 130 Q156 156 132 158 L68 158 Q44 156 34 130Z')
    + s('rect', '#f4f4f0', x=50, y=138, width=100, height=6, stroke_width=2)
    + z('path', '#8fc7e8', d='M26 160 Q42 152 58 160 Q74 168 90 160 Q106 152 122 160 Q138 168 154 160 Q166 154 174 158 L174 176 L26 176Z'))

# 13 canoe
ITEMS['canoe'] = (
    s('path', d='M152 64 L124 162', stroke_width=5)
    + z('ellipse', '#9a6a3f', cx=124, cy=164, rx=7, ry=14)
    + z('path', '#7cc4b0', d='M62 138 Q64 104 92 102 Q120 104 122 138Z')
    + face(92, 70, '#ffd9b8', '#5a4033', 'smile')
    + thick('M114 116 Q132 106 146 88', '#7cc4b0', 10, 4)
    + z('circle', '#ffd9b8', cx=147, cy=86, r=7)
    + thick('M108 124 Q124 124 138 118', '#7cc4b0', 10, 4)
    + z('circle', '#ffd9b8', cx=139, cy=118, r=7)
    + z('path', '#d9a66b', d='M24 124 Q36 136 100 138 Q164 136 176 124 Q168 158 100 160 Q32 158 24 124Z')
    + s('path', d='M40 140 Q100 150 160 140', stroke='#9a6a3f', stroke_width=2.5)
    + s('path', d='M30 174 Q46 166 62 174 M86 176 Q102 168 118 176 M140 174 Q156 166 172 174', stroke='#8fc7e8', stroke_width=3))

# 14 submarine
ITEMS['submarine'] = (
    s('path', d='M110 74 L110 48 L124 48', stroke_width=5)
    + z('rect', '#ffc94d', x=84, y=70, width=40, height=34, rx=6)
    + z('path', '#b9a99c', d='M40 125 L26 110 L26 140Z')
    + z('rect', '#ffc94d', x=36, y=98, width=138, height=56, rx=28)
    + ''.join(s('circle', '#8fc7e8', cx=x, cy=124, r=9, stroke_width=2.5) for x in (78, 108, 138))
    + s('path', d='M48 140 L160 140', stroke='#f5b971', stroke_width=3)
    + s('circle', cx=150, cy=60, r=5, stroke_width=2) + s('circle', cx=160, cy=44, r=7, stroke_width=2) + s('circle', cx=142, cy=36, r=4, stroke_width=2)
    + s('path', d='M30 176 Q46 168 62 176 M88 178 Q104 170 120 178 M140 176 Q156 168 172 176', stroke='#8fc7e8', stroke_width=3))

# 15 steam locomotive
ITEMS['steam-locomotive'] = (
    z('ellipse', '#f4f4f0', cx=150, cy=44, rx=16, ry=11) + z('ellipse', '#f4f4f0', cx=126, cy=34, rx=13, ry=9) + z('ellipse', '#f4f4f0', cx=166, cy=30, rx=10, ry=7)
    + z('path', '#5b6b7a', d='M138 90 L134 58 L158 58 L154 90Z')
    + z('path', '#ffc94d', d='M100 90 Q100 76 112 76 Q124 76 124 90Z')
    + z('rect', '#5b6b7a', x=74, y=86, width=94, height=52, rx=12)
    + s('path', d='M96 88 L96 136 M140 88 L140 136', stroke='#ffc94d', stroke_width=3)
    + z('circle', '#ffe27a', cx=170, cy=100, r=6)
    + z('rect', '#e04b5a', x=30, y=62, width=48, height=80, rx=4)
    + z('rect', '#5b6b7a', x=24, y=54, width=60, height=12, rx=3)
    + s('rect', '#8fc7e8', x=40, y=74, width=28, height=22, rx=3, stroke_width=2.5)
    + s('rect', '#e04b5a', x=28, y=136, width=144, height=8, rx=2, stroke_width=2.5)
    + z('path', '#e04b5a', d='M164 140 L180 158 L164 158Z')
    + ''.join(z('circle', '#e04b5a', cx=x, cy=154, r=16) + s('circle', '#f4f4f0', cx=x, cy=154, r=5, stroke_width=2.5) for x in (54, 96, 138))
    + s('path', d='M54 159 L138 159', stroke_width=4)
    + s('path', d='M22 174 L180 174', stroke_width=2.5))

# 16 camper van
ITEMS['camper-van'] = (
    z('ellipse', '#f5b971', cx=96, cy=54, rx=54, ry=7)
    + s('path', d='M62 58 L62 66 M130 58 L130 66', stroke_width=3)
    + z('path', '#f4f4f0', d='M26 150 L26 84 Q26 66 44 66 L148 66 Q168 66 172 86 L178 118 L178 150Z')
    + s('path', '#7cc4b0', d='M26 118 L178 118 L178 150 L26 150Z', stroke_width=2.5)
    + s('rect', '#8fc7e8', x=38, y=78, width=28, height=26, rx=4, stroke_width=2.5)
    + s('path', '#f6a6b8', d='M38 82 Q38 78 42 78 L62 78 Q66 78 66 82 L66 88 Q58 92 52 86 Q46 92 38 88Z', stroke_width=2)
    + s('rect', '#8fc7e8', x=74, y=78, width=28, height=26, rx=4, stroke_width=2.5)
    + s('rect', '#f4f4f0', x=110, y=74, width=24, height=72, rx=3, stroke_width=2.5)
    + s('path', '#8fc7e8', d='M142 78 L156 78 Q164 78 166 88 L170 104 L142 104Z', stroke_width=2.5)
    + s('circle', '#ffe27a', cx=173, cy=128, r=4.5, stroke_width=2.5)
    + wh(62, 152, 16) + wh(148, 152, 16) + ground(174))

# 17 tractor
ITEMS['tractor'] = (
    z('rect', '#9ccf7a', x=42, y=46, width=64, height=10, rx=3)
    + s('path', d='M50 56 L48 104 M98 56 L100 104', stroke_width=5)
    + s('path', '#8fc7e8', d='M54 96 L56 60 L94 60 L96 96Z', stroke_width=2.5)
    + s('path', d='M152 108 L152 78', stroke_width=6) + z('rect', '#5b6b7a', x=146, y=72, width=12, height=8, rx=2)
    + z('path', '#9ccf7a', d='M44 132 L44 100 L172 106 Q178 108 178 116 L178 134Z')
    + s('path', d='M168 112 L168 128 M174 112 L174 128', stroke_width=2)
    + z('circle', '#5b6b7a', cx=66, cy=138, r=34) + s('circle', '#ffc94d', cx=66, cy=138, r=13, stroke_width=2.5)
    + ''.join(s('path', d=f'M{66 + 34 * c} {138 + 34 * sn} L{66 + 26 * c} {138 + 26 * sn}', stroke='#c9d3db', stroke_width=3)
              for c, sn in ((1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)))
    + z('circle', '#5b6b7a', cx=150, cy=154, r=18) + s('circle', '#ffc94d', cx=150, cy=154, r=7, stroke_width=2.5)
    + ground(174, 24, 180))

# 18 traffic light
ITEMS['traffic-light'] = (
    z('rect', '#5b6b7a', x=94, y=140, width=12, height=34)
    + z('rect', '#5b6b7a', x=80, y=170, width=40, height=10, rx=3)
    + z('rect', '#5b6b7a', x=72, y=26, width=56, height=120, rx=14)
    + s('circle', '#e04b5a', cx=100, cy=52, r=14, stroke_width=2.5)
    + s('circle', '#ffc94d', cx=100, cy=87, r=14, stroke_width=2.5)
    + s('circle', '#7cc4a0', cx=100, cy=122, r=14, stroke_width=2.5)
    + s('path', d='M84 42 Q100 30 116 42 M84 77 Q100 65 116 77 M84 112 Q100 100 116 112', stroke_width=3)
    + s('path', d='M140 46 L150 40 M142 56 L154 56 M140 66 L150 72', stroke='#e04b5a', stroke_width=2.5))

# 19 crosswalk with a person
ITEMS['crosswalk'] = (
    z('rect', '#c9d3db', x=24, y=138, width=152, height=40, rx=4)
    + ''.join(s('rect', '#ffffff', x=x, y=144, width=14, height=28, rx=2, stroke_width=2) for x in (32, 56, 80, 104, 128, 152))
    + thick('M94 124 L82 158', '#5b6b7a', 11, 5) + thick('M106 124 L120 156', '#5b6b7a', 11, 5)
    + z('ellipse', '#e8735a', cx=78, cy=162, rx=9, ry=5) + z('ellipse', '#e8735a', cx=124, cy=160, rx=9, ry=5)
    + thick('M80 110 Q70 118 66 130', '#8fb3e0', 9, 3) + z('circle', '#ffd9b8', cx=65, cy=132, r=7)
    + z('path', '#8fb3e0', d='M76 132 Q78 100 100 98 Q122 100 124 132Z')
    + thick('M118 108 Q132 94 138 76', '#8fb3e0', 9, 3) + z('circle', '#ffd9b8', cx=140, cy=72, r=8)
    + face(100, 64, '#ffd9b8', '#2b2220', 'open'))

# 20 gas station pump
ITEMS['gas-station'] = (
    z('rect', '#f4f4f0', x=52, y=36, width=76, height=18, rx=6)
    + z('rect', '#e04b5a', x=58, y=50, width=64, height=122, rx=6)
    + s('rect', '#8fc7e8', x=68, y=64, width=44, height=28, rx=4, stroke_width=2.5)
    + s('path', d='M76 74 L92 74 M76 82 L104 82', stroke_width=2)
    + s('rect', '#f4f4f0', x=58, y=104, width=64, height=26, stroke_width=2.5)
    + s('path', '#ffc94d', d='M90 108 Q82 118 82 122 Q82 128 90 128 Q98 128 98 122 Q98 118 90 108Z', stroke_width=2)
    + s('path', d='M146 98 Q164 134 142 154 Q132 162 122 158', stroke_width=5)
    + z('path', '#5b6b7a', d='M122 72 L144 72 Q150 72 150 78 L150 98 L142 98 L142 84 L122 84Z')
    + z('rect', '#5b6b7a', x=48, y=168, width=84, height=10, rx=3))
