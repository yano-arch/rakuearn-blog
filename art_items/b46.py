import math
from art import z, s, dot, cheeks, face, OUT, CH
ITEMS = {}


def bar(d, col, w=8):
    """縁取り付きの太い棒（ポール・取っ手など）"""
    return s('path', d=d, stroke_width=w) + s('path', d=d, stroke=col, stroke_width=w - 5)


def sector(cx, cy, r1, r2, a1, a2, fill):
    p = lambda r, a: (round(cx + r * math.cos(math.radians(a)), 1), round(cy + r * math.sin(math.radians(a)), 1))
    x1, y1 = p(r2, a1); x2, y2 = p(r2, a2); x3, y3 = p(r1, a2); x4, y4 = p(r1, a1)
    return s('path', fill, d=f'M{x1} {y1} A{r2} {r2} 0 0 1 {x2} {y2} L{x3} {y3} A{r1} {r1} 0 0 0 {x4} {y4}Z', stroke_width=2.5)


ITEMS['bus-stop'] = (
    z('rect', '#8fc7e8', x=32, y=70, width=96, height=82, rx=3)
    + s('path', d='M80 74 L80 148', stroke_width=2)
    + z('rect', '#7cc4b0', x=22, y=54, width=116, height=18, rx=5)
    + z('rect', '#5b6b7a', x=30, y=72, width=8, height=106) + z('rect', '#5b6b7a', x=122, y=72, width=8, height=106)
    + z('rect', '#d9a66b', x=46, y=134, width=68, height=10, rx=3)
    + s('path', d='M54 144 L54 166 M106 144 L106 166', stroke_width=4)
    + z('rect', '#c9d3db', x=154, y=74, width=8, height=104)
    + z('circle', '#e8735a', cx=158, cy=58, r=20) + s('circle', '#ffffff', cx=158, cy=58, r=13, stroke_width=2.5)
    + s('rect', '#ffc94d', x=150, y=51, width=16, height=11, rx=2, stroke_width=2) + dot(154, 64, 2.2) + dot(162, 64, 2.2)
    + z('rect', '#f4f4f0', x=146, y=96, width=24, height=30, rx=2)
    + s('path', d='M151 104 L165 104 M151 111 L165 111 M151 118 L160 118', stroke_width=2)
    + s('path', d='M18 178 L182 178', stroke_width=2))

ITEMS['train-platform'] = (
    z('path', '#f4f4f0', d='M182 66 L100 66 Q66 68 60 108 L60 142 L182 142Z')
    + s('path', '#8fb3e0', d='M62 112 L182 112 L182 124 L60 124Z', stroke_width=2.5)
    + s('path', '#8fc7e8', d='M76 100 Q80 80 98 78 L98 100Z', stroke_width=2.5)
    + ''.join(s('rect', '#8fc7e8', x=x, y=78, width=18, height=22, rx=3, stroke_width=2.5) for x in (112, 138, 164))
    + s('circle', '#ffe27a', cx=68, cy=132, r=4, stroke_width=2)
    + z('rect', '#7cc4b0', x=18, y=34, width=164, height=16, rx=4)
    + z('rect', '#c9d3db', x=24, y=50, width=10, height=98)
    + s('path', d='M46 50 L46 60', stroke_width=2.5)
    + z('circle', '#ffffff', cx=46, cy=74, r=14) + s('path', d='M46 74 L46 66 M46 74 L52 77', stroke_width=2.5)
    + z('rect', '#c9d3db', x=18, y=146, width=160, height=30, rx=2)
    + s('rect', '#ffe27a', x=18, y=150, width=160, height=7, stroke_width=2))

ITEMS['airport'] = (
    z('ellipse', '#ffffff', cx=158, cy=30, rx=18, ry=8)
    + z('path', '#e8735a', d='M48 40 L38 20 L52 20 L66 40Z')
    + z('path', '#f4f4f0', d='M36 46 Q36 38 50 38 L106 38 Q124 39 128 46 Q124 54 106 54 L50 54 Q36 54 36 46Z')
    + ''.join(dot(x, 45, 3.2, '#8fc7e8') for x in (66, 79, 92, 105))
    + z('path', '#e8735a', d='M84 49 L66 72 L80 72 L102 49Z')
    + z('rect', '#f4f4f0', x=146, y=74, width=14, height=50)
    + z('path', '#8fc7e8', d='M136 62 L170 62 L164 78 L142 78Z')
    + z('rect', '#5b6b7a', x=136, y=54, width=34, height=9, rx=3)
    + z('rect', '#f4f4f0', x=30, y=116, width=140, height=62)
    + z('path', '#7cc4b0', d='M24 120 Q100 92 176 120Z')
    + ''.join(s('rect', '#8fc7e8', x=x, y=126, width=20, height=24, rx=2, stroke_width=2.5) for x in (40, 64, 116, 140))
    + s('rect', '#8fb3e0', x=88, y=136, width=24, height=42, stroke_width=2.5) + s('path', d='M100 136 L100 178', stroke_width=2)
    + s('path', d='M18 178 L182 178', stroke_width=2))

ITEMS['passport'] = (
    z('rect', '#f4f4f0', x=58, y=34, width=92, height=136, rx=6)
    + z('rect', '#e04b5a', x=50, y=30, width=94, height=136, rx=8)
    + s('path', d='M62 32 L62 164', stroke_width=2)
    + s('circle', '#ffe27a', cx=103, cy=82, r=24, stroke_width=2.5)
    + s('ellipse', cx=103, cy=82, rx=11, ry=24, stroke_width=2) + s('path', d='M79 82 L127 82 M83 70 L123 70 M83 94 L123 94', stroke_width=2)
    + s('rect', '#ffe27a', x=78, y=118, width=50, height=6, rx=3, stroke_width=2)
    + s('rect', '#ffe27a', x=86, y=130, width=34, height=5, rx=2.5, stroke_width=2)
    + s('rect', '#ffe27a', x=93, y=146, width=20, height=13, rx=3, stroke_width=2)
    + s('path', d='M98 146 L98 159 M108 146 L108 159 M93 152.5 L113 152.5', stroke_width=1.5))

tk = ('M34 64 L122 64 A8 8 0 0 0 138 64 L166 64 Q174 64 174 72 L174 128 Q174 136 166 136 '
      'L138 136 A8 8 0 0 0 122 136 L34 136 Q26 136 26 128 L26 72 Q26 64 34 64Z')
ITEMS['ticket'] = ('<g transform="rotate(-10 100 100)">'
    + z('path', '#f5d58a', d=tk)
    + s('path', d='M130 78 L130 122', stroke_width=2.5, stroke_dasharray='4 6')
    + s('rect', '#e8735a', x=38, y=76, width=80, height=14, rx=4, stroke_width=2.5)
    + dot(48, 112, 5, '#7cc4b0') + dot(108, 112, 5, '#e8735a')
    + s('path', d='M56 112 L100 112', stroke_width=2.5, stroke_dasharray='3 6')
    + s('path', '#8fb3e0', d='M70 104 L86 100 Q90 100 90 102 Q90 104 86 105 L70 109Z', stroke_width=2)
    + s('path', '#8fb3e0', d='M78 103 L72 96 L76 96 L84 102Z', stroke_width=1.5)
    + s('path', d='M40 126 L80 126', stroke_width=2)
    + ''.join(s('path', d=f'M{x} 82 L{x} 120', stroke_width=w) for x, w in ((142, 3), (147, 1.5), (151, 3), (156, 2), (160, 1.5), (164, 3)))
    + '</g>')

ITEMS['luggage-cart'] = (
    s('path', d='M80 48 Q80 40 96 40 Q112 40 112 48', stroke_width=4)
    + z('ellipse', '#f5b971', cx=96, cy=64, rx=30, ry=15) + s('path', d='M76 60 L116 60', stroke_width=2)
    + z('rect', '#7cc4b0', x=66, y=78, width=66, height=32, rx=6)
    + s('path', d='M84 80 L84 108 M114 80 L114 108', stroke_width=2.5)
    + z('rect', '#e8735a', x=56, y=110, width=100, height=46, rx=7)
    + s('path', d='M80 112 L80 154 M132 112 L132 154', stroke_width=2.5)
    + s('rect', '#f5d58a', x=96, y=124, width=16, height=12, rx=2, stroke_width=2)
    + bar('M48 158 L38 60 L60 60', '#c9d3db')
    + z('rect', '#c9d3db', x=42, y=154, width=126, height=9, rx=3)
    + z('circle', '#5b6b7a', cx=62, cy=171, r=8) + z('circle', '#5b6b7a', cx=148, cy=171, r=8))

ITEMS['backpacker'] = (
    z('rect', '#e8735a', x=52, y=74, width=96, height=100, rx=18)
    + z('rect', '#7cc4b0', x=40, y=58, width=120, height=20, rx=10)
    + s('path', d='M56 64 L56 72 M144 64 L144 72', stroke_width=2.5)
    + z('path', '#f5d58a', d='M66 180 Q68 128 100 126 Q132 128 134 180Z')
    + s('path', d='M80 132 L78 180 M120 132 L122 180', stroke_width=8)
    + s('path', d='M80 132 L78 180 M120 132 L122 180', stroke='#9a6a3f', stroke_width=3)
    + s('path', d='M80 158 L120 158', stroke_width=3)
    + face(100, 88, '#ffd9b8', '#5a4033', 'smile')
    + z('circle', '#ffd9b8', cx=81, cy=146, r=9) + z('circle', '#ffd9b8', cx=119, cy=146, r=9))

ITEMS['hotel'] = (
    z('rect', '#f6e0c4', x=48, y=38, width=104, height=140, rx=3)
    + s('rect', '#e8735a', x=62, y=46, width=76, height=16, rx=4, stroke_width=2.5)
    + dot(84, 54, 3.5, '#ffe27a') + dot(100, 54, 3.5, '#ffe27a') + dot(116, 54, 3.5, '#ffe27a')
    + ''.join(s('rect', '#8fc7e8', x=x, y=y, width=20, height=16, rx=2, stroke_width=2.5)
              for x in (60, 90, 120) for y in (72, 96, 120))
    + z('rect', '#8fb3e0', x=84, y=152, width=32, height=26, rx=2) + s('path', d='M100 152 L100 178', stroke_width=2)
    + z('path', '#e8735a', d='M74 142 L126 142 L134 154 L66 154Z')
    + z('circle', '#9ccf7a', cx=40, cy=168, r=12) + z('circle', '#9ccf7a', cx=160, cy=168, r=12)
    + s('path', d='M20 179 L180 179', stroke_width=2))

ITEMS['ryokan'] = (
    s('path', d='M30 98 L30 104 M170 98 L170 104', stroke_width=2)
    + z('rect', '#f6e0c4', x=38, y=96, width=124, height=80)
    + s('rect', '#9a6a3f', x=38, y=96, width=8, height=80, stroke_width=2.5)
    + s('rect', '#9a6a3f', x=154, y=96, width=8, height=80, stroke_width=2.5)
    + ''.join(s('rect', '#f4f4f0', x=x, y=110, width=26, height=34, rx=1, stroke_width=2.5)
              + s('path', d=f'M{x+13} 110 L{x+13} 144 M{x} 121 L{x+26} 121 M{x} 133 L{x+26} 133', stroke_width=1.5)
              for x in (54, 120))
    + z('rect', '#8b6b4f', x=82, y=124, width=36, height=52)
    + ''.join(s('rect', '#8fb3e0', x=x, y=120, width=12, height=26, rx=1, stroke_width=2.5) for x in (80, 94, 108))
    + s('path', d='M78 120 L122 120', stroke_width=3)
    + z('path', '#5b6b7a', d='M16 100 Q42 96 56 66 L144 66 Q158 96 184 100Z')
    + s('path', d='M40 90 L160 90 M50 78 L150 78', stroke_width=2)
    + z('rect', '#5b6b7a', x=54, y=56, width=92, height=11, rx=3)
    + z('ellipse', '#e8735a', cx=30, cy=114, rx=8, ry=11) + z('ellipse', '#e8735a', cx=170, cy=114, rx=8, ry=11)
    + s('path', d='M23 114 L37 114 M163 114 L177 114', stroke_width=1.5)
    + s('path', d='M18 177 L182 177', stroke_width=2))

ITEMS['hot-spring'] = (
    s('path', d='M40 96 Q32 84 40 72 Q48 60 40 48 M160 96 Q152 84 160 72 Q168 60 160 48 M62 70 Q56 60 62 50 Q68 40 62 30', stroke_width=3, stroke='#b9a99c')
    + z('ellipse', '#b9a99c', cx=28, cy=132, rx=14, ry=11) + z('ellipse', '#b9a99c', cx=172, cy=132, rx=14, ry=11)
    + z('ellipse', '#8fc7e8', cx=100, cy=146, rx=74, ry=26)
    + face(100, 104, '#ffd9b8', '#2b2220', 'smile')
    + z('path', '#ffffff', d='M82 60 L118 60 Q124 66 118 72 L82 72 Q76 66 82 60Z')
    + s('path', '#8fc7e8', d='M27 146 Q60 128 100 132 Q140 128 173 146 Q170 170 100 172 Q30 170 27 146Z', stroke='none')
    + s('path', d='M30 140 Q60 128 100 132 Q140 128 170 140', stroke_width=2.5)
    + s('path', d='M66 150 Q74 146 82 150 M118 150 Q126 146 134 150', stroke_width=2, stroke='#ffffff')
    + z('ellipse', '#b9a99c', cx=44, cy=170, rx=16, ry=9) + z('ellipse', '#b9a99c', cx=82, cy=174, rx=16, ry=8)
    + z('ellipse', '#b9a99c', cx=120, cy=174, rx=16, ry=8) + z('ellipse', '#b9a99c', cx=158, cy=170, rx=16, ry=9))

ITEMS['beach-umbrella'] = (
    z('path', '#f5d58a', d='M18 160 Q100 148 182 160 L182 180 L18 180Z')
    + bar('M100 72 L100 168', '#f4f4f0')
    + z('path', '#e8735a', d='M28 78 Q36 30 100 26 Q164 30 172 78 Q154 70 137 78 Q118 70 100 78 Q82 70 63 78 Q46 70 28 78Z')
    + s('path', '#f4f4f0', d='M100 26 Q70 40 63 78 Q82 70 100 78Z', stroke_width=2.5)
    + s('path', '#f4f4f0', d='M100 26 Q130 40 137 78 Q154 70 172 78 Q164 30 100 26Z', stroke_width=2.5)
    + s('circle', '#e8735a', cx=100, cy=22, r=4, stroke_width=2.5)
    + s('path', d='M140 154 L130 174 M172 154 L176 174 M130 120 L150 154', stroke_width=4)
    + z('path', '#7cc4b0', d='M118 112 L132 106 L148 144 L176 144 L176 156 L140 156Z')
    + s('path', d='M126 124 L136 120 M132 136 L142 132', stroke_width=2, stroke='#ffffff')
    + z('circle', '#ffe27a', cx=52, cy=158, r=13)
    + s('path', '#e8735a', d='M52 145 Q44 158 52 171 Q60 158 52 145Z', stroke_width=2))

ITEMS['swim-ring'] = (
    z('path', '#f07a8a', fill_rule='evenodd',
      d='M42 96 A58 58 0 1 0 158 96 A58 58 0 1 0 42 96Z M76 96 A24 24 0 1 1 124 96 A24 24 0 1 1 76 96Z')
    + ''.join(sector(100, 96, 24, 58, a - 18, a + 18, '#ffffff') for a in (-45, 45, 135, 225))
    + s('path', d='M62 62 Q72 52 86 48', stroke='#ffffff', stroke_width=4)
    + z('path', '#8fc7e8', d='M20 144 Q40 136 60 144 Q80 152 100 144 Q120 136 140 144 Q160 152 180 144 L180 176 L20 176Z')
    + s('path', d='M46 162 Q54 158 62 162 M118 164 Q126 160 134 164', stroke='#ffffff', stroke_width=2.5))

lens_l = 'M30 82 L92 82 Q94 120 74 128 Q46 132 34 116 Q28 100 30 82Z'
lens_r = 'M170 82 L108 82 Q106 120 126 128 Q154 132 166 116 Q172 100 170 82Z'
ITEMS['sunglasses'] = (
    z('circle', '#ffe27a', cx=152, cy=40, r=13)
    + s('path', d='M152 18 L152 12 M174 40 L180 40 M130 40 L124 40 M168 24 L172 20 M136 24 L132 20', stroke_width=2.5)
    + s('path', d='M26 78 L20 70 M174 78 L180 70', stroke_width=5)
    + z('path', '#5b6b7a', d=lens_l) + z('path', '#5b6b7a', d=lens_r)
    + s('path', d='M42 96 L54 92 M44 108 L66 98', stroke='#ffffff', stroke_width=3)
    + s('path', d='M120 96 L132 92 M122 108 L144 98', stroke='#ffffff', stroke_width=3)
    + z('path', '#e8735a', d='M24 76 Q24 70 30 70 L84 70 Q100 80 116 70 L170 70 Q176 70 176 76 L176 84 L114 84 Q100 92 86 84 L24 84Z'))

ITEMS['sun-hat'] = (
    z('ellipse', '#f5d58a', cx=100, cy=122, rx=80, ry=32)
    + s('path', d='M36 124 Q100 160 164 124', stroke_width=2, stroke_dasharray='3 7')
    + z('path', '#f5d58a', d='M62 118 Q60 64 100 62 Q140 64 138 118 Q100 130 62 118Z')
    + s('path', d='M74 86 Q100 78 126 86', stroke_width=2, stroke_dasharray='3 7')
    + s('path', '#e8735a', d='M62 102 Q100 114 138 102 L138 118 Q100 130 62 118Z', stroke_width=2.5)
    + z('path', '#e8735a', d='M128 116 Q150 130 146 152 L136 146 Q140 132 122 120Z')
    + z('path', '#e8735a', d='M132 116 Q160 122 164 142 L154 142 Q150 128 128 120Z')
    + z('circle', '#f6a6b8', cx=128, cy=112, r=8) + dot(128, 112, 3, '#ffe27a'))

ITEMS['souvenir'] = (
    s('path', d='M72 82 Q72 54 86 54 Q98 54 98 82 M104 82 Q104 54 118 54 Q130 54 130 82', stroke_width=4)
    + bar('M136 34 L136 92', '#9a6a3f', 7)
    + z('path', '#e8735a', d='M138 36 L170 46 L138 58Z')
    + z('rect', '#7cc4b0', x=58, y=62, width=38, height=30, rx=3, transform='rotate(-12 77 77)')
    + s('path', d='M58 76 L96 76', stroke='#ffe27a', stroke_width=4, transform='rotate(-12 77 77)')
    + z('rect', '#f6a6b8', x=98, y=70, width=30, height=24, rx=3)
    + z('rect', '#f5b971', x=48, y=86, width=104, height=90, rx=4)
    + s('path', d='M48 98 L152 98', stroke_width=2)
    + s('circle', '#f4f4f0', cx=100, cy=136, r=22, stroke_width=2.5)
    + s('path', '#9ccf7a', d='M82 146 L94 126 L102 136 L108 128 L118 146Z', stroke_width=2)
    + dot(108, 122, 4, '#ffe27a'))

ITEMS['postcard'] = ('<g transform="rotate(-6 100 100)">'
    + z('rect', '#f4f4f0', x=24, y=50, width=152, height=104, rx=4)
    + s('rect', '#8fc7e8', x=34, y=60, width=64, height=84, rx=3, stroke_width=2.5)
    + s('path', '#9ccf7a', d='M34 144 L34 120 L54 96 L68 112 L78 102 L98 124 L98 144Z', stroke_width=2.5)
    + s('path', '#ffffff', d='M54 96 L48 104 L54 102 L60 104Z', stroke_width=2)
    + dot(80, 76, 6, '#ffe27a')
    + s('path', d='M108 64 L108 140', stroke_width=2)
    + s('path', d='M116 112 L164 112 M116 124 L164 124 M116 136 L150 136', stroke_width=2)
    + z('rect', '#f6a6b8', x=140, y=58, width=26, height=32, rx=2)
    + s('rect', '#ffffff', x=145, y=63, width=16, height=22, rx=1, stroke_width=1.5)
    + s('path', '#f07a8a', d='M153 80 C149 77 147 74 149 71 C151 69 153 70 153 72 C153 70 155 69 157 71 C159 74 157 77 153 80Z', stroke_width=1.5)
    + s('circle', cx=136, cy=84, r=11, stroke_width=2)
    + s('path', d='M116 74 Q120 70 124 74 Q128 78 132 74 M116 82 Q120 78 124 82', stroke_width=2)
    + '</g>')

ITEMS['compass'] = (
    s('circle', '#f5d58a', cx=100, cy=38, r=9) + s('circle', '#fbf6ee', cx=100, cy=38, r=3.5, stroke_width=2)
    + z('circle', '#f5d58a', cx=100, cy=108, r=64)
    + s('circle', '#f4f4f0', cx=100, cy=108, r=50)
    + s('path', d='M100 62 L100 70 M100 146 L100 154 M54 108 L62 108 M138 108 L146 108', stroke_width=3)
    + s('path', d='M133 75 L129 79 M67 75 L71 79 M133 141 L129 137 M67 141 L71 137', stroke_width=2)
    + z('path', '#e04b5a', d='M114 66 L107.5 110.6 L92.5 105.4Z')
    + z('path', '#c9d3db', d='M86 150 L92.5 105.4 L107.5 110.6Z')
    + z('circle', '#5b6b7a', cx=100, cy=108, r=6))

ITEMS['binoculars'] = (
    s('path', d='M40 150 Q100 196 160 150', stroke='#e8735a', stroke_width=5)
    + z('rect', '#c9d3db', x=86, y=78, width=28, height=28, rx=4)
    + z('rect', '#5b6b7a', x=50, y=44, width=30, height=30, rx=6) + z('rect', '#5b6b7a', x=120, y=44, width=30, height=30, rx=6)
    + z('rect', '#5b6b7a', x=34, y=64, width=60, height=92, rx=16) + z('rect', '#5b6b7a', x=106, y=64, width=60, height=92, rx=16)
    + s('rect', '#e8735a', x=34, y=86, width=60, height=10, stroke_width=2.5) + s('rect', '#e8735a', x=106, y=86, width=60, height=10, stroke_width=2.5)
    + s('circle', '#8fc7e8', cx=64, cy=126, r=20, stroke_width=2.5) + s('circle', '#8fc7e8', cx=136, cy=126, r=20, stroke_width=2.5)
    + s('path', d='M54 120 Q58 112 66 110 M126 120 Q130 112 138 110', stroke='#ffffff', stroke_width=3)
    + s('rect', '#c9d3db', x=94, y=56, width=12, height=20, rx=3, stroke_width=2.5))

boot = (z('path', '#9a6a3f', d='M56 60 L92 60 L94 112 Q130 114 146 128 Q154 138 152 150 L56 150Z')
        + s('path', '#8b6b4f', d='M124 118 Q148 126 152 150 L128 150 Q130 132 124 118Z', stroke_width=2.5)
        + s('path', d='M88 72 L100 78 M88 84 L102 90 M88 96 L106 104 M88 108 L112 116', stroke='#f5d58a', stroke_width=3)
        + s('rect', '#e8735a', x=52, y=54, width=44, height=12, rx=5, stroke_width=2.5)
        + z('rect', '#5b6b7a', x=50, y=148, width=106, height=12, rx=5)
        + ''.join(s('path', d=f'M{x} 160 L{x} 155', stroke_width=2) for x in (64, 80, 96, 112, 128, 144)))
ITEMS['hiking-boots'] = ('<g transform="translate(16 -10)">' + boot + '</g>'
                         + '<g transform="translate(-20 16)">' + boot + '</g>')

ITEMS['hiker'] = (
    z('path', '#9ccf7a', d='M18 156 L46 76 L78 156Z') + s('path', '#ffffff', d='M46 76 L38 98 L46 94 L54 98Z', stroke_width=2.5)
    + z('path', '#7cc4a0', d='M116 156 L156 70 L182 132 L182 156Z') + s('path', '#ffffff', d='M156 70 L146 92 L156 88 L166 92Z', stroke_width=2.5)
    + z('path', '#d9a66b', d='M18 154 Q100 146 182 154 L182 180 L18 180Z')
    + z('rect', '#7cc4b0', x=116, y=112, width=34, height=56, rx=10)
    + z('path', '#e8735a', d='M66 180 Q68 128 98 126 Q128 128 130 180Z')
    + s('path', d='M84 132 L82 180 M114 132 L116 180', stroke='#9a6a3f', stroke_width=4)
    + bar('M50 180 L60 112', '#9a6a3f', 8)
    + z('circle', '#ffd9b8', cx=60, cy=134, r=9)
    + face(98, 92, '#ffd9b8', '#5a4033', 'open')
    + z('ellipse', '#f5d58a', cx=98, cy=62, rx=44, ry=8)
    + z('path', '#f5d58a', d='M70 62 Q70 36 98 36 Q126 36 126 62Z')
    + s('path', '#7cc4b0', d='M71 54 L125 54 L126 62 L70 62Z', stroke_width=2.5))
