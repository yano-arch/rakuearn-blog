"""ローカル専用：art.py の定義から public/images に SVG と PNG を書き出す（cairosvg が必要）"""
import os, cairosvg, art
os.makedirs('public/images/svg',exist_ok=True); os.makedirs('public/images/png',exist_ok=True)
for slug,body in art.drawings().items():
    s=art.svg(body); open(f'public/images/svg/{slug}.svg','w').write(s)
    cairosvg.svg2png(bytestring=s.encode(),write_to=f'public/images/png/{slug}.png',output_width=1000,output_height=1000)
    print('ok',slug)
