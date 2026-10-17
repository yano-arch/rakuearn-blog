"""バッチ単位で public/images に SVG/PNG を書き出す: python3 tools/export_batch.py b01 b07"""
import sys, importlib, cairosvg
sys.path.insert(0, '.')
import art
for b in sys.argv[1:]:
    for slug, body in importlib.import_module(f'art_items.{b}').ITEMS.items():
        s = art.svg(body); open(f'public/images/svg/{slug}.svg', 'w').write(s)
        cairosvg.svg2png(bytestring=s.encode(), write_to=f'public/images/png/{slug}.png', output_width=1000, output_height=1000)
        print(b, slug)
