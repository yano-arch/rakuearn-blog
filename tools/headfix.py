"""頭が体から浮いている人物を検出し、体（服）を上に伸ばして頭とくっつける補正を data/fixes.json に書く。
python3 tools/headfix.py            # 検出のみ
python3 tools/headfix.py --write    # 補正を保存（そのあと export で画像を作り直す）
"""
import re, io, sys, json, math, cairosvg
sys.path.insert(0, '.')
import art
from PIL import Image
SC = 4
PAIR = re.compile(r'<g transform="translate\(4 4\)"><(\w+) (.*?) fill="([^"]+)" stroke="none"/></g><\1 \2 fill="none"/>')

def render(body):
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=art.svg(body).encode(),
                      output_width=200 * SC, output_height=200 * SC))).convert('RGBA')

def dark(c): return c[3] > 200 and c[0] < 100 and c[1] < 90 and c[2] < 90

def heads(body):
    return [(float(a), float(b), float(r)) for a, b, r in
            re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="#ffd9b8"', body) if 14 <= float(r) <= 44]

def gaps(body):
    """各頭について (隙間px, 隙間が最小の列x, 下の線のy)"""
    im = render(body); px = im.load(); out = []
    for cx, cy, R in heads(body):
        best = (99, None, None)
        for dx in range(-int(R * .6), int(R * .6) + 1):
            x = cx + dx
            if not 0 <= x < 200: continue
            yb = cy + math.sqrt(max(R * R - dx * dx, 0)) + 2; y = yb
            while y < 199 and not dark(px[int(x * SC), int(y * SC)]): y += .25
            if y < 199 and y - yb < best[0]: best = (y - yb, x, y)
        out.append((cx, cy, R) + best)
    return out

def owner(body, x, y):
    """(x,y) の線を持つ z() 要素（体）"""
    for m in PAIR.finditer(body):
        im = render(m.group(0)); px = im.load()
        for dy in (0, .5, 1, -.5, 1.5):
            if dark(px[int(x * SC), int((y + dy) * SC)]): return m
    return None

def bottom(m):
    a = render(m.group(0)).getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox()
    return a[3] / SC

def plan(body, limit=2.5):
    fixes = []
    for cx, cy, R, g, x, y in gaps(body):
        if g < limit or x is None: continue
        m = owner(body, x, y)
        if not m: continue
        B = bottom(m) - 5   # 塗りのずれ分を除いた体の下端あたりを固定点に
        k = round((B - y + g + 3) / (B - y), 3)
        if k > 1.6: continue
        fixes.append({"match": m.group(2), "anchor": round(B, 1), "k": k, "gap": round(g, 1)})
    return fixes

if __name__ == '__main__':
    d = art.drawings()
    allf = json.load(open('data/fixes.json')) if '--keep' in sys.argv else {}
    for slug, body in d.items():
        if '#ffd9b8' not in body: continue
        f = plan(body)
        if f:
            allf[slug] = f
            print(slug, [(x['gap'], x['k']) for x in f])
    print(len(allf), 'items')
    if '--write' in sys.argv:
        json.dump(allf, open('data/fixes.json', 'w'), ensure_ascii=False, indent=1)
