"""バッチの見本シートを作る: python3 tools/preview.py b03 /path/out.png"""
import sys, importlib, json, cairosvg
sys.path.insert(0, '.')
import art
b, out = sys.argv[1], sys.argv[2]
items = importlib.import_module(f'art_items.{b}').ITEMS
meta = {m['slug']: m for m in json.load(open(f'data/items/{b}.json', encoding='utf-8'))}
cells = ''
for i, (slug, body) in enumerate(items.items()):
    x = (i % 5) * 220 + 10; y = (i // 5) * 240 + 10
    name = meta.get(slug, {}).get('t', {}).get('ja', ['?'])[0]
    cells += (f'<rect x="{x}" y="{y}" width="200" height="200" rx="16" fill="#fbf6ee"/>'
              f'<g transform="translate({x} {y})" stroke="{art.OUT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</g>'
              f'<text x="{x+100}" y="{y+222}" font-family="sans-serif" font-size="13" text-anchor="middle" fill="#666">{slug} / {name}</text>')
rows = (len(items) + 4) // 5
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1110 {rows*240+10}" width="2220" height="{(rows*240+10)*2}"><rect width="100%" height="100%" fill="#fff"/>{cells}</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to=out)
missing = set(items) ^ set(meta)
print('ok', len(items), 'drawings', len(meta), 'meta', ('MISMATCH ' + str(missing)) if missing else '')
