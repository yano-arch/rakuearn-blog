# FuwaFuwa — 無料イラスト素材サイト（8言語）

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

## 公開（Cloudflare Pages）
1. Cloudflare ダッシュボード → Workers & Pages → Create → Pages → Connect to Git でこのリポジトリを選ぶ
2. Build command: `python3 build.py` / Build output directory: `dist`（Framework preset: None）
3. Custom domains に `rakuearn.com` を追加（ドメインがCloudflareにあればDNSは自動設定）
キャッシュ設定は `public/_headers`。無料プランは1サイト2万ファイルまで（1イラスト＝8言語ページ＋画像2枚で約10ファイル）。

## 広告
`build.py` 冒頭の設定だけで有効になる（未設定のあいだは何も表示されない）。

- バナー広告（AdSense）：`ADSENSE_CLIENT` と `ADSENSE_SLOTS`（top / feed / side / bottom）を設定。
  全ページの上・一覧の途中（12点目のあと）・個別ページのサイド・下に「広告」ラベル付きで出る。`ads.txt` も自動出力。
- ダウンロード時のリワード広告（Google Ad Manager）：`REWARDED_AD_UNIT` に広告ユニットのパスを設定。
  ダウンロードボタン → 確認画面 →「広告を見てダウンロード」→ 広告を最後まで見るとダウンロード開始。
  広告が埋まらない・読み込めない・広告ブロック時（8秒以内に表示されない場合）は、そのままダウンロードさせる。
- `python3 build.py --preview` で広告位置とリワードの流れ（5秒のダミー広告）を確認できる。
