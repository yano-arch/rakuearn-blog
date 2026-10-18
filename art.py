OUT='#3b2f2a'; CH='#f4a0a0'
def at(d): return ' '.join(f'{k.replace("_","-")}="{v}"' for k,v in d.items())
def z(tag,fill,**a):
    s=at(a); return f'<g transform="translate(4 4)"><{tag} {s} fill="{fill}" stroke="none"/></g><{tag} {s} fill="none"/>'
def s(tag,fill='none',**a): return f'<{tag} {at(a)} fill="{fill}"/>'
def dot(x,y,r=3.5,c=OUT): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="none"/>'
def cheeks(x1,x2,y,rx=7,ry=4): return f'<ellipse cx="{x1}" cy="{y}" rx="{rx}" ry="{ry}" fill="{CH}" stroke="none"/><ellipse cx="{x2}" cy="{y}" rx="{rx}" ry="{ry}" fill="{CH}" stroke="none"/>'
def face(cx,cy,skin,hair,mouth='smile'):
    o=z('circle',skin,cx=cx,cy=cy,r=34)
    o+=s('path',hair,d=f'M{cx-34} {cy-2} Q{cx-32} {cy-36} {cx} {cy-35} Q{cx+32} {cy-36} {cx+34} {cy-2} Q{cx+20} {cy-18} {cx} {cy-17} Q{cx-20} {cy-18} {cx-34} {cy-2}Z')
    o+=dot(cx-12,cy+2)+dot(cx+12,cy+2)+cheeks(cx-20,cx+20,cy+13)
    if mouth=='smile': o+=s('path',d=f'M{cx-6} {cy+16} Q{cx} {cy+21} {cx+6} {cy+16}')
    elif mouth=='open': o+=s('path','#c0504d',d=f'M{cx-8} {cy+14} Q{cx} {cy+28} {cx+8} {cy+14}Z',stroke_width=2.5)
    else: o+=f'<circle cx="{cx}" cy="{cy+18}" r="4" fill="#c0504d" stroke-width="2.5"/>'
    return o
I={}
I['01_hello']=(z('path','#7cc4b0',d='M66 180 Q68 128 100 126 Q132 128 134 180Z')
 +s('path',d='M128 140 Q146 120 156 92',stroke_width=8)+s('path',d='M128 140 Q146 120 156 92',stroke='#7cc4b0',stroke_width=3)
 +z('circle','#ffd9b8',cx=158,cy=84,r=10)+face(100,82,'#ffd9b8','#2b2220','open'))
I['02_idea']=(z('path','#f5b971',d='M66 186 Q68 140 100 138 Q132 140 134 186Z')+face(100,98,'#ffd9b8','#5a4033','o')
 +z('circle','#ffe27a',cx=152,cy=42,r=18)+s('rect','#b9a99c',x=145,y=60,width=14,height=10,rx=3)
 +s('path',d='M152 12 L152 4 M176 22 L183 16 M128 22 L121 16 M182 44 L190 44',stroke_width=2.5))
I['03_dog']=(z('ellipse','#d9a66b',cx=104,cy=142,rx=40,ry=42)+z('ellipse','#d9a66b',cx=88,cy=182,rx=12,ry=7)+z('ellipse','#d9a66b',cx=120,cy=182,rx=12,ry=7)
 +s('path',d='M140 160 Q166 150 160 124',stroke_width=3)
 +z('circle','#d9a66b',cx=100,cy=82,r=32)
 +z('path','#9a6a3f',d='M72 66 Q56 92 66 110 Q80 98 80 70Z')+z('path','#9a6a3f',d='M128 66 Q144 92 134 110 Q120 98 120 70Z')
 +dot(89,82)+dot(111,82)+f'<ellipse cx="100" cy="94" rx="6" ry="4" fill="{OUT}" stroke="none"/>'+cheeks(80,120,98,6,3.5)
 +s('path',d='M92 102 Q96 107 100 101 Q104 107 108 102',stroke_width=2.5))
I['04_globe']=(z('circle','#8fc7e8',cx=100,cy=100,r=62)
 +s('path','#9ccf7a',d='M68 64 Q90 50 106 68 Q102 92 80 90 Q60 86 68 64Z',stroke_width=2.5)
 +s('path','#9ccf7a',d='M116 106 Q144 96 152 120 Q140 146 120 140 Q106 126 116 106Z',stroke_width=2.5)
 +s('path','#9ccf7a',d='M58 118 Q76 116 82 132 Q74 148 60 138Z',stroke_width=2.5)
 +dot(88,112)+dot(108,112)+cheeks(78,118,122,6,3.5)+s('path',d='M93 122 Q98 127 103 122',stroke_width=2.5))
I['05_airplane']=(z('ellipse','#ffffff',cx=60,cy=160,rx=30,ry=12)+z('ellipse','#ffffff',cx=150,cy=150,rx=24,ry=10)
 +z('path','#e8735a',d='M52 92 L40 60 L58 60 L76 90Z')
 +z('path','#f4f4f0',d='M36 104 Q36 88 58 88 L148 88 Q172 90 178 100 Q172 112 148 114 L58 114 Q36 114 36 104Z')
 +''.join(dot(x,98,4.5,'#8fc7e8') for x in (80,98,116,134))
 +z('path','#e8735a',d='M98 104 L72 142 L92 142 L124 104Z')+dot(162,99,3))
I['06_house']=(s('rect','#b9a99c',x=124,y=52,width=16,height=30)+z('rect','#f5d58a',x=56,y=96,width=88,height=80)
 +z('path','#e8735a',d='M44 102 L100 50 L156 102Z')+z('rect','#8b6b4f',x=86,y=130,width=26,height=46,rx=3)
 +z('rect','#8fc7e8',x=118,y=112,width=18,height=18,rx=2)+z('rect','#8fc7e8',x=62,y=112,width=18,height=18,rx=2)
 +s('path',d='M30 180 L170 180',stroke_width=2))
H='M100 116 C88 106 80 98 86 88 C92 80 100 85 100 92 C100 85 108 80 114 88 C120 98 112 106 100 116Z'
I['07_phone']=(z('rect','#5b6b7a',x=70,y=36,width=60,height=128,rx=10)+s('rect','#d8eef8',x=77,y=50,width=46,height=96,rx=4)
 +z('path','#f07a8a',d=H)+dot(100,156,3.5,'#d8eef8')
 +s('path','#f07a8a',d='M152 60 C147 56 144 52 147 48 C150 45 152 47 152 50 C152 47 154 45 157 48 C160 52 157 56 152 60Z',stroke_width=2)
 +s('path','#f07a8a',d='M46 92 C41 88 38 84 41 80 C44 77 46 79 46 82 C46 79 48 77 51 80 C54 84 51 88 46 92Z',stroke_width=2))
I['08_gift']=(z('rect','#9ccf7a',x=56,y=98,width=88,height=76,rx=3)+s('rect','#e8735a',x=92,y=98,width=16,height=76,stroke_width=2.5)
 +z('path','#e8735a',d='M100 82 Q70 50 64 74 Q66 88 100 82Z')+z('path','#e8735a',d='M100 82 Q130 50 136 74 Q134 88 100 82Z')
 +z('rect','#9ccf7a',x=48,y=80,width=104,height=22,rx=3)+s('rect','#e8735a',x=92,y=80,width=16,height=22,stroke_width=2.5))
I['09_plant']=(s('path',d='M100 126 L100 96')
 +z('path','#7cc4a0',d='M100 120 Q60 112 62 82 Q92 86 100 120Z')+z('path','#7cc4a0',d='M100 110 Q140 100 140 68 Q108 74 100 110Z')
 +z('path','#9ccf7a',d='M100 98 Q86 60 100 38 Q114 60 100 98Z')
 +z('path','#e8735a',d='M72 132 L128 132 L120 182 L80 182Z')+z('rect','#e8735a',x=64,y=122,width=72,height=14,rx=3)
 +dot(90,154)+dot(110,154)+cheeks(82,118,163,5,3)+s('path',d='M96 162 Q100 166 104 162',stroke_width=2.5))
I['10_cake']=(s('rect','#8fb3e0',x=97,y=66,width=7,height=28)+z('path','#ffc94d',d='M100 64 Q90 52 100 40 Q110 52 100 64Z')
 +z('rect','#f6e0c4',x=70,y=94,width=60,height=36,rx=4)+z('rect','#f6e0c4',x=50,y=130,width=100,height=46,rx=4)
 +s('path','#f6a6b8',d='M50 134 L150 134 L150 142 Q137 152 125 142 Q112 152 100 142 Q87 152 75 142 Q62 152 50 142Z',stroke_width=2.5)
 +dot(84,104,6,'#e04b5a')+dot(100,104,6,'#e04b5a')+dot(116,104,6,'#e04b5a')+s('path',d='M36 182 L164 182',stroke_width=2.5))
SLUGS={'01_hello':'person-waving','02_idea':'person-idea','03_dog':'puppy-sitting','04_globe':'smiling-earth',
 '05_airplane':'airplane-sky','06_house':'cozy-house','07_phone':'smartphone-hearts','08_gift':'gift-box',
 '09_plant':'potted-plant','10_cake':'birthday-cake'}
def svg(body,size=1000):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="{size}" height="{size}">'
            f'<g stroke="{OUT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>')
def drawings():
    """既存10点＋art_items/ 以下の各バッチ（ITEMS = {slug: body}）をまとめて返す"""
    import importlib, pkgutil, art_items
    d = {SLUGS[k]: v for k, v in I.items()}
    for m in sorted(pkgutil.iter_modules(art_items.__path__), key=lambda m: m.name):
        d.update(importlib.import_module(f"art_items.{m.name}").ITEMS)
    return d

import json as _json, os as _os, re as _re
_FIX = _json.load(open(_os.path.join(_os.path.dirname(__file__), 'data/fixes.json'))) if _os.path.exists(_os.path.join(_os.path.dirname(__file__), 'data/fixes.json')) else {}
def fix(slug, body):
    """data/fixes.json の補正（浮いた頭の下の体を縦に伸ばす）を当てる"""
    for f in _FIX.get(slug, []):
        a = _re.escape(f['match'])
        pat = _re.compile(r'<g transform="translate\(4 4\)"><(\w+) ' + a + r' fill="([^"]+)" stroke="none"/></g><\1 ' + a + r' fill="none"/>')
        tr = f'translate(0 {f["anchor"]}) scale(1 {f["k"]}) translate(0 {-f["anchor"]})'
        body = pat.sub(lambda m: f'<g transform="{tr}">{m.group(0)}</g>', body, count=1)
    return body
