# rakuearn — 無料イラスト素材サイト（8言語）

静的サイト。Python標準ライブラリだけでビルドでき、Vercelにそのまま載せられます。

## 構成
- `art.py` … イラストの定義（ズレ塗り画風のパーツ関数＋各イラスト）
- `make_images.py` … `public/images/` に SVG / PNG(1000px) を書き出す（ローカル専用・`pip install cairosvg`）
- `data/illustrations.json` … イラストごとのカテゴリ・8言語のタイトル/説明/タグ
- `data/ui.json` … 画面の文言・利用規約・プライバシーポリシー（8言語）
- `build.py` … `dist/` にサイトを生成（hreflang・sitemap.xml・robots.txt・構造化データ込み）
- `static/` … CSS / 検索用JS

## イラストを追加する手順
1. `art.py` の `I` に描画を追加し、`SLUGS` にURL用の英語名を追加
2. `python3 make_images.py`
3. `data/illustrations.json` に1件追加（8言語のタイトル・説明・タグ）
4. `python3 build.py --preview` で確認 → push

## URL
`/{lang}/` トップ、`/{lang}/illust/{slug}/` 個別、`/{lang}/category/{cat}/`、`/{lang}/license/`、`/{lang}/privacy/`
言語: en, ja, es, pt, fr, de, zh, ko。`/` はブラウザの言語に合わせて自動で振り分け。

## 公開（Vercel）
1. GitHubにpush → Vercelで新規プロジェクトとしてインポート（Framework: Other）
2. `vercel.json` の設定で `python3 build.py` → `dist/` が公開される
   ※ビルド環境でPythonが使えない場合は、ローカルで `python3 build.py` した `dist/` をOutput Directoryにして配信
3. Domains に `rakuearn.com` を追加し、DNSをVercelの指示どおり設定

## 広告（AdSense）
承認後、`build.py` 冒頭の `ADSENSE_CLIENT` と `ADSENSE_SLOTS` を設定するだけで、
全ページの広告枠（上・サイド・下）と `ads.txt` が出力されます。未設定のあいだ広告枠は表示されません。
問い合わせ先は `CONTACT_EMAIL`（support@studyshort.co.jp）で変更できます。
