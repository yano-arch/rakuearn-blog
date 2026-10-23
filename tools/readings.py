"""日本語のタイトル・タグのひらがな読みを data/readings_ja.json に書き出す（「ねこ」で「猫」を探せるようにする）。
イラストを追加したら実行: python3 tools/readings.py   （pykakasi が必要）"""
import json, glob, sys
sys.path.insert(0, '.')
import pykakasi
k = pykakasi.kakasi()
items = json.load(open('data/illustrations.json', encoding='utf-8'))
for f in sorted(glob.glob('data/items/*.json')):
    try: items += json.load(open(f, encoding='utf-8'))
    except Exception: pass
out = {}
for i in items:
    ja = i['t'].get('ja')
    if not ja: continue
    words = [ja[0]] + ja[2]
    r = {''.join(x['hira'] for x in k.convert(w)) for w in words}
    r -= set(words)
    if r: out[i['slug']] = ' '.join(sorted(r))
json.dump(out, open('data/readings_ja.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(out), 'items')
