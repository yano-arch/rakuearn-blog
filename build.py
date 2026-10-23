"""FuwaFuwa イラスト素材サイトの静的ビルド（Python標準ライブラリのみ）

  python3 build.py            本番用（広告枠は ADSENSE_CLIENT を設定したときだけ出る）
  python3 build.py --preview  広告枠の位置を点線の枠で表示するプレビュー用

出力先: dist/
"""
import json, os, shutil, sys, html
from urllib.parse import quote, unquote
from datetime import date

# ===== 設定 =====
SITE_URL = "https://rakuearn.com"
SITE_NAME = "FuwaFuwa"
CONTACT_EMAIL = "support@studyshort.co.jp"
ADSENSE_CLIENT = "ca-pub-6815652261319315"  # AdSense サイト運営者ID（審査用の読み込みタグと ads.txt を出力）
ADSENSE_SLOTS = {"top": "", "feed": "", "side": "", "bottom": ""}  # 各広告ユニットの data-ad-slot
# ダウンロード時のリワード広告（Google Ad Manager の広告ユニットパス。例: "/1234567/fuwafuwa_rewarded"）
# 未設定・広告が出ない・広告ブロック時は、そのままダウンロードできる
REWARDED_AD_UNIT = ""
LANGS = ["en", "ja", "es", "pt", "fr", "de", "zh", "ko"]
DEFAULT_LANG = "en"
CATS = ["people", "work", "animals", "food", "nature", "home", "tech", "school", "travel", "events", "sports", "health", "hobby"]
PREVIEW = "--preview" in sys.argv
OUT = "dist"

UI = json.load(open("data/ui.json", encoding="utf-8"))
# 肌の色の切り替え（人物イラスト）。先頭が標準の肌色で、イラストはこの色で描かれている
SKIN_TONES = ["#ffd9b8", "#f1c27d", "#e0ac69", "#c68642", "#8d5a3b"]
import glob
_raw = []
for _f in ["data/illustrations.json"] + sorted(glob.glob("data/items/*.json")):
    try:
        _raw += json.load(open(_f, encoding="utf-8"))
    except Exception as _ex:
        print("skip (not ready):", _f, _ex)
# 画像を書き出し済み（＝チェック済み）のイラストだけを公開する。並びは追加した順
ITEMS = [x for x in _raw if os.path.exists(f"public/images/svg/{x['slug']}.svg")]
NEWEST = list(reversed(ITEMS))
PER_PAGE = 60          # カテゴリーページ1ページあたりの点数
NEW_ON_HOME = 20       # トップの「新着」に出す点数
CAT_SAMPLES = 4        # トップのカテゴリーカードに出す代表イラストの数
e = lambda s: html.escape(str(s), quote=True)
import hashlib
# CSS/JS は中身のハッシュをURLに付け、更新したら必ず新しいものが読み込まれるようにする
ASSET_V = {f: hashlib.md5(open(f"static/{f}", "rb").read()).hexdigest()[:8] for f in ("style.css", "app.js")}

LOGO = ('<svg viewBox="0 0 40 40" width="34" height="34" aria-hidden="true"><g stroke="#3b2f2a" stroke-width="2.4" '
        'stroke-linecap="round"><circle cx="21.5" cy="21.5" r="15" fill="#f5b971" stroke="none"/>'
        '<circle cx="19.5" cy="19.5" r="15" fill="none"/><circle cx="14" cy="19" r="1.8" fill="#3b2f2a" stroke="none"/>'
        '<circle cx="25" cy="19" r="1.8" fill="#3b2f2a" stroke="none"/><ellipse cx="10.5" cy="24" rx="3" ry="1.8" '
        'fill="#f4a0a0" stroke="none"/><ellipse cx="28.5" cy="24" rx="3" ry="1.8" fill="#f4a0a0" stroke="none"/>'
        '<path d="M17 24 Q19.5 26.5 22 24" fill="none" stroke-width="2"/></g></svg>')


def url(lang, kind="home", arg=None):
    if kind == "home": return f"/{lang}/"
    if kind == "illust": return f"/{lang}/illust/{arg}/"
    if kind == "cat": return f"/{lang}/category/{arg}/"
    if kind == "tag": return f"/{lang}/tag/{quote(tag_key(arg), safe='')}/"
    return f"/{lang}/{kind}/"


def tag_key(tag):
    return tag.strip().lower().replace("/", "-").replace(" ", "-")


def cap(lang, k):
    return k[:1].upper() + k[1:] if lang in ("en", "es", "pt", "fr", "de") else k


MIN_TAG = 3   # この点数以上あるキーワードだけ、まとめページを作る
TAGS = {}     # lang -> {tag_key: (表示名, [items])}


def build_tags():
    for lang in LANGS:
        d = {}
        for i in NEWEST:
            for tg in t(i, lang)[2]:
                k = tag_key(tg)
                if not k: continue
                d.setdefault(k, [tg.strip(), []])[1].append(i)
        TAGS[lang] = {k: v for k, v in d.items() if len(v[1]) >= MIN_TAG}


def tag_href(lang, tg):
    k = tag_key(tg)
    return url(lang, "tag", tg) if k in TAGS.get(lang, {}) else f"{url(lang)}?q={quote(tg)}"


def ad(slot, lang):
    label = f'<span class="ad-label">{e(UI[lang]["ad_label"])}</span>'
    if ADSENSE_CLIENT and ADSENSE_SLOTS.get(slot):
        return (f'<div class="ad ad-{slot}">{label}<ins class="adsbygoogle" style="display:block" '
                f'data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="{ADSENSE_SLOTS.get(slot, "")}" '
                f'data-ad-format="auto" data-full-width-responsive="true"></ins>'
                f'<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script></div>')
    if PREVIEW:
        return f'<div class="ad ad-{slot}">{label}<div class="ad-preview">AD ({slot})</div></div>'
    return ""


def layout(lang, kind, arg, title, desc, body, og_image=None, jsonld=None, full_title=None):
    u = UI[lang]
    canonical = SITE_URL + url(lang, kind, arg)
    if kind == "tag":  # キーワードページは言語ごとに別物なので、言語切り替えは各言語のトップへ
        alts = ""
        opts = "".join(f'<option value="{url(lang, kind, arg) if l == lang else url(l)}"{" selected" if l == lang else ""}>'
                       f'{e(UI[l]["lang_name"])}</option>' for l in LANGS)
    else:
        alts = "".join(f'<link rel="alternate" hreflang="{UI[l]["html_lang"]}" href="{SITE_URL}{url(l, kind, arg)}">'
                       for l in LANGS)
        alts += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}{url(DEFAULT_LANG, kind, arg)}">'
        opts = "".join(f'<option value="{url(l, kind, arg)}"{" selected" if l == lang else ""}>{e(UI[l]["lang_name"])}</option>'
                       for l in LANGS)
    fonts = "family=Nunito:wght@400;700;800"
    if lang == "ja": fonts += "&family=M+PLUS+Rounded+1c:wght@400;700"
    og = SITE_URL + (og_image or "/images/png/smiling-earth.png")
    adsense = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" '
               f'crossorigin="anonymous"></script>') if ADSENSE_CLIENT else ""
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    if full_title: full_title = f"{full_title} | {SITE_NAME}"
    elif kind == "home": full_title = u["home_title"]
    elif kind == "illust": full_title = f"{u['title_illust'].format(t=title)} | {SITE_NAME}"
    elif kind == "cat": full_title = f"{u['title_cat'].format(c=title)} | {SITE_NAME}"
    else: full_title = f"{title} | {SITE_NAME}"
    return f"""<!doctype html>
<html lang="{u['html_lang']}" class="lang-{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
{alts}
<meta property="og:type" content="website">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="/static/style.css?v={ASSET_V['style.css']}">
{adsense}{ld}
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{url(lang)}">{LOGO}<span><b>{SITE_NAME}</b><small>{e(u['tagline'])}</small></span></a>
  {"" if kind == "home" else f'''<form class="hsearch" role="search" action="{url(lang)}" method="get">
    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></g></svg>
    <input type="search" name="q" placeholder="{e(u['search'])}" aria-label="{e(u['search'])}" autocomplete="off" enterkeyhint="search"></form>'''}
  <nav>
    <a href="{url(lang, 'license')}">{e(u['license'])}</a>
    <label class="lang"><span class="sr">{e(u['language'])}</span>
      <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></g></svg>
      <select onchange="location.href=this.value">{opts}</select></label>
  </nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <p>{e(u['footer'])}</p>
  <p class="links"><a href="{url(lang, 'about-us')}">{e(u['about-us'])}</a><a href="{url(lang, 'faq')}">{e(u['faq'])}</a><a href="{url(lang, 'license')}">{e(u['license'])}</a><a href="{url(lang, 'privacy')}">{e(u['privacy'])}</a><a href="{url(lang, 'contact')}">{e(u['contact'])}</a></p>
  <p class="copy">© {date.today().year} {SITE_NAME}</p>
</div></footer>
<script src="/static/app.js?v={ASSET_V['app.js']}" defer></script>
</body>
</html>"""


def t(item, lang): return item["t"].get(lang) or item["t"][DEFAULT_LANG]


def card(item, lang):
    title, _, tags = t(item, lang)
    q = " ".join([title] + tags).lower()
    return (f'<a class="card" href="{url(lang, "illust", item["slug"])}" data-q="{e(q)}">'
            f'<span class="thumb"><img src="/images/svg/{item["slug"]}.svg" alt="{e(title)}" width="200" height="200" loading="lazy"></span>'
            f'<span class="name">{e(title)}</span></a>')


def chips(lang, active=None):
    u = UI[lang]
    out = [f'<a class="chip{" on" if active is None else ""}" href="{url(lang)}">{e(u["all"])}</a>']
    for c in CATS:
        if any(i["cat"] == c for i in ITEMS):
            out.append(f'<a class="chip{" on" if active == c else ""}" href="{url(lang, "cat", c)}">{e(u["cats"][c])}</a>')
    return f'<nav class="chips">{"".join(out)}</nav>'


def badges(u):
    return (f'<ul class="badges"><li>{e(u["badge_free"])}</li><li>{e(u["badge_credit"])}</li>'
            f'<li>{e(u["badge_formats"])}</li></ul>')


# トップのヒーローに並べるイラスト（スラッグ, 左%, 上%, 幅%, アニメの遅れ秒）
HERO = [("sun", 2, 0, 17, 0), ("airplane-sky", 19, 6, 22, -1.2), ("smiling-earth", 41, 0, 26, -2.4),
        ("heart-balloons", 72, 0, 21, -0.6), ("person-waving", 0, 44, 22, -1.8), ("ice-cream", 22, 58, 15, -3),
        ("cat-sitting", 38, 50, 20, -0.9), ("potted-plant", 58, 54, 17, -2.1), ("puppy-sitting", 76, 46, 21, -1.5),
        ("rice-ball", 63, 22, 12, -2.7)]


def hero_art():
    return "".join(
        f'<img src="/images/svg/{s}.svg" alt="" width="200" height="200" '
        f'style="left:{x}%;top:{y}%;width:{w}%;animation-delay:{d}s">'
        for s, x, y, w, d in HERO)


def cat_items(c): return [i for i in ITEMS if i["cat"] == c]


def cat_card(lang, c):
    u = UI[lang]
    items = cat_items(c)
    imgs = "".join(f'<img src="/images/svg/{i["slug"]}.svg" alt="" width="100" height="100" loading="lazy">'
                   for i in items[:CAT_SAMPLES])
    return (f'<a class="cat-card" href="{url(lang, "cat", c)}"><span class="cat-imgs">{imgs}</span>'
            f'<span class="cat-name">{e(u["cats"][c])}</span>'
            f'<span class="cat-count">{e(u["count"].format(n=len(items)))}</span></a>')


def page_home(lang):
    u = UI[lang]
    cats = "".join(cat_card(lang, c) for c in CATS if cat_items(c))
    new = "".join(card(i, lang) for i in NEWEST[:NEW_ON_HOME])
    body = f"""
<section class="hero">
  <div class="hero-text">
    <h1>{e(u['hero_title'])}</h1>
    <p>{e(u['hero_sub'])}</p>
    {badges(u)}
  </div>
  <div class="hero-art" aria-hidden="true">{hero_art()}</div>
</section>
<form class="search" role="search" onsubmit="return false">
  <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></g></svg>
  <input id="q" type="search" placeholder="{e(u['search'])}" aria-label="{e(u['search'])}" autocomplete="off"
    data-index="/{lang}/search.json" data-base="/{lang}/illust/">
</form>
<section id="results" hidden>
  <h2 class="section-title">{e(u['results'])} <small id="count" data-tpl="{e(u['count'])}"></small></h2>
  <div class="grid" id="grid"></div>
  <p class="empty" id="empty" hidden>{e(u['no_results'])}</p>
</section>
<div id="browse">
{ad('top', lang)}
<h2 class="section-title">{e(u['browse'])} <small>{e(u['count'].format(n=len(ITEMS)))}</small></h2>
<div class="cat-grid">{cats}</div>
{ad('feed', lang)}
<h2 class="section-title">{e(u['latest'])}</h2>
<div class="grid">{new}</div>
{popular_tags(lang, 40)}
<section class="home-about prose">
  <h2>{e(u['about-us'] if lang != 'ja' else 'FuwaFuwaについて')}</h2>
  {"".join(f"<p>{e(p.replace('{n}', f'{len(ITEMS) // 100 * 100:,}'))}</p>" for _, p in u['about-us_body'][:2])}
  <p><a href="{url(lang, 'about-us')}">{e(u['about-us'])} ›</a>　<a href="{url(lang, 'faq')}">{e(u['faq'])} ›</a></p>
</section>
</div>
{ad('bottom', lang)}"""
    home_desc = u["home_desc"].format(n=f"{len(ITEMS) // 100 * 100:,}")
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{SITE_URL}/#website", "url": SITE_URL + url(lang), "name": SITE_NAME,
         "description": home_desc, "inLanguage": u["html_lang"],
         "potentialAction": {"@type": "SearchAction", "target": f"{SITE_URL}{url(lang)}?q={{search_term_string}}",
                             "query-input": "required name=search_term_string"}},
        {"@type": "Organization", "@id": f"{SITE_URL}/#org", "name": SITE_NAME, "url": SITE_URL,
         "logo": f"{SITE_URL}/favicon.svg", "email": CONTACT_EMAIL}]}
    return layout(lang, "home", None, SITE_NAME, home_desc, body, jsonld=jsonld)


def pager(lang, c, p, pages):
    u = UI[lang]
    if pages <= 1: return ""
    link = lambda n: url(lang, "cat", c if n == 1 else f"{c}/{n}")
    out = []
    if p > 1: out.append(f'<a class="pg" href="{link(p - 1)}" rel="prev">‹ {e(u["prev"])}</a>')
    for n in range(1, pages + 1):
        out.append(f'<span class="pg on">{n}</span>' if n == p else f'<a class="pg" href="{link(n)}">{n}</a>')
    if p < pages: out.append(f'<a class="pg" href="{link(p + 1)}" rel="next">{e(u["next"])} ›</a>')
    return f'<nav class="pager">{"".join(out)}</nav>'


def page_cat(lang, c, p=1):
    u = UI[lang]
    items = cat_items(c)
    pages = max(1, -(-len(items) // PER_PAGE))
    chunk = items[(p - 1) * PER_PAGE: p * PER_PAGE]
    cards = [card(i, lang) for i in chunk]
    if len(cards) > 12: cards.insert(12, ad('feed', lang))
    name = u['cats'][c] + (f" ({p}/{pages})" if p > 1 else "")
    ex = u["sep"].join(t(i, lang)[0] for i in items[:3])
    body = f"""
<h1 class="page-title">{e(u['cat_h1'].format(c=u['cats'][c]))} <small>{e(u['count'].format(n=len(items)))}</small></h1>
{chips(lang, c)}
{ad('top', lang)}
<div class="grid">{"".join(cards)}</div>
{pager(lang, c, p, pages)}
{popular_tags(lang, 30, items) if p == 1 else ""}
{ad('bottom', lang)}"""
    desc = u["cat_desc"].format(c=u["cats"][c], n=len(items), ex=ex)
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": u["title_cat"].format(c=u["cats"][c]), "description": desc,
         "url": SITE_URL + url(lang, "cat", c), "inLanguage": u["html_lang"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": SITE_URL + url(lang)},
            {"@type": "ListItem", "position": 2, "name": u["cats"][c], "item": SITE_URL + url(lang, "cat", c)}]}]}
    return layout(lang, "cat", c if p == 1 else f"{c}/{p}", name, desc, body, jsonld=jsonld)


READINGS = json.load(open("data/readings_ja.json", encoding="utf-8")) if os.path.exists("data/readings_ja.json") else {}


def search_index(lang):
    # 英語のタイトル・タグも入れて、どの言語のページでも英語で探せるようにする
    # [slug, タイトル, タグ・カテゴリ・英語, 説明文, カテゴリ]
    return json.dumps([[i["slug"], t(i, lang)[0], " ".join(t(i, lang)[2] + [t(i, "en")[0]] + t(i, "en")[2] + [UI[lang]["cats"][i["cat"]]]
                                 + ([READINGS.get(i["slug"], "")] if lang == "ja" else [])),
                        t(i, lang)[1], i["cat"]] for i in NEWEST],
                      ensure_ascii=False, separators=(",", ":"))


def page_illust(lang, item):
    u = UI[lang]
    s = item["slug"]
    title, desc, tags = t(item, lang)
    has_skin = SKIN_TONES[0] in open(f"public/images/svg/{s}.svg", encoding="utf-8").read().lower()
    same = [i for i in ITEMS if i["cat"] == item["cat"] and i is not item]
    other = [i for i in ITEMS if i["cat"] != item["cat"]]
    related = (same + other)[:8]
    tag_html = "".join(f'<a href="{tag_href(lang, tg)}">#{e(tg)}</a>' for tg in tags)
    kw = [cap(lang, tg.strip()) for tg in tags[:3]] or [title]
    ks = u["kjoin"].join(kw)
    alt = u["alt"].format(t=title, k=kw[0])
    image_ld = {
        "@type": "ImageObject",
        "name": title, "description": desc, "inLanguage": u["html_lang"],
        "contentUrl": f"{SITE_URL}/images/png/{s}.png", "thumbnailUrl": f"{SITE_URL}/images/svg/{s}.svg",
        "license": SITE_URL + url(lang, "license"), "acquireLicensePage": SITE_URL + url(lang, "license"),
        "creditText": SITE_NAME, "creator": {"@type": "Organization", "name": SITE_NAME},
        "copyrightNotice": SITE_NAME, "datePublished": item["date"], "keywords": ", ".join(tags),
    }
    jsonld = {"@context": "https://schema.org", "@graph": [image_ld,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": SITE_URL + url(lang)},
            {"@type": "ListItem", "position": 2, "name": u["cats"][item["cat"]], "item": SITE_URL + url(lang, "cat", item["cat"])},
            {"@type": "ListItem", "position": 3, "name": title, "item": SITE_URL + url(lang, "illust", s)}]}]}
    body = f"""
<nav class="crumbs"><a href="{url(lang)}">{e(u['home'])}</a><span>›</span><a href="{url(lang, 'cat', item['cat'])}">{e(u['cats'][item['cat']])}</a><span>›</span><span>{e(title)}</span></nav>
<article class="detail">
  <div class="detail-left"><div class="detail-art"><img id="art" src="/images/svg/{s}.svg" alt="{e(alt)}" width="480" height="480"></div>{skin_picker(lang, s) if has_skin else ""}</div>
  <div class="detail-info">
    <h1>{e(title)}</h1>
    <p class="desc">{e(desc)}</p>
    <div class="dl">
      <a class="btn primary" data-dl="png" href="/images/png/{s}.png" download="{SITE_NAME.lower()}-{s}.png">{e(u['download_png'])} <small>1000×1000</small></a>
      <a class="btn" data-dl="svg" href="/images/svg/{s}.svg" download="{SITE_NAME.lower()}-{s}.svg">{e(u['download_svg'])}</a>
    </div>
    <p class="note">{e(u['license_short'])} <a href="{url(lang, 'license')}">{e(u['license'])}</a></p>
    <h2 class="about-h">{e(u['about_h'])}</h2>
    <p class="about">{e(u['about'].format(ks=ks))}</p>
    <div class="tags"><span>{e(u['tags'])}</span>{tag_html}</div>
    {ad('side', lang)}
  </div>
</article>
{rewarded_modal(lang)}
<h2 class="section-title">{e(u['related'])}</h2>
<div class="grid">{"".join(card(i, lang) for i in related)}</div>
{ad('bottom', lang)}"""
    sp = "" if lang in ("ja", "zh", "ko") else " "
    return layout(lang, "illust", s, title, desc + sp + u["kw_desc"].format(ks=ks), body,
                  og_image=f"/images/png/{s}.png", jsonld=jsonld,
                  full_title=u["title_illust2"].format(t=title, k=kw[0]))


def popular_tags(lang, n=40, items=None):
    """人気キーワードのリンク集（内部リンク用）"""
    u = UI[lang]
    tags = TAGS[lang]
    if items is not None:
        keys = {tag_key(tg) for i in items for tg in t(i, lang)[2]}
        tags = {k: v for k, v in tags.items() if k in keys}
    top = sorted(tags.items(), key=lambda kv: (-len(kv[1][1]), kv[0]))[:n]
    if not top: return ""
    links = "".join(f'<a href="{url(lang, "tag", name)}">{e(cap(lang, name))} <small>{len(its)}</small></a>'
                    for _, (name, its) in top)
    return f'<h2 class="section-title">{e(u["popular"])}</h2><div class="tags kw">{links}</div>'


def page_tag(lang, key):
    u = UI[lang]
    name, items = TAGS[lang][key]
    k = cap(lang, name)
    ex = u["sep"].join(t(i, lang)[0] for i in items[:3])
    desc = u["tag_desc"].format(k=name if lang != "de" else k, n=len(items), ex=ex)
    cards = [card(i, lang) for i in items]
    if len(cards) > 12: cards.insert(12, ad('feed', lang))
    cats = sorted({i["cat"] for i in items}, key=CATS.index)
    body = f"""
<nav class="crumbs"><a href="{url(lang)}">{e(u['home'])}</a><span>›</span><span>{e(u['tag_h1'].format(k=k))}</span></nav>
<h1 class="page-title">{e(u['tag_h1'].format(k=k))} <small>{e(u['count'].format(n=len(items)))}</small></h1>
<p class="lead">{e(desc)}</p>
{ad('top', lang)}
<div class="grid">{"".join(cards)}</div>
{popular_tags(lang, 24, [j for c in cats for j in cat_items(c)])}
{ad('bottom', lang)}"""
    title = u["tag_title"].format(k=k)
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": title, "description": desc, "url": SITE_URL + url(lang, "tag", name),
         "inLanguage": u["html_lang"],
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
             {"@type": "ListItem", "position": n + 1, "url": SITE_URL + url(lang, "illust", i["slug"])}
             for n, i in enumerate(items[:30])]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": SITE_URL + url(lang)},
            {"@type": "ListItem", "position": 2, "name": u["tag_h1"].format(k=k), "item": SITE_URL + url(lang, "tag", name)}]}]}
    return layout(lang, "tag", name, k, desc, body, og_image=f"/images/png/{items[0]['slug']}.png",
                  jsonld=jsonld, full_title=title)


def skin_picker(lang, slug):
    u = UI[lang]
    btns = "".join(
        f'<button type="button" class="sw{" on" if i == 0 else ""}" data-c="{c}" style="background:{c}" '
        f'aria-label="{e(u["skin_label"])} {i + 1}" aria-pressed="{"true" if i == 0 else "false"}"></button>'
        for i, c in enumerate(SKIN_TONES))
    return (f'<div class="skin" id="skin" data-base="{SKIN_TONES[0]}" data-svg="/images/svg/{slug}.svg">'
            f'<span>{e(u["skin_label"])}</span><div class="sws">{btns}</div></div>')


def rewarded_modal(lang):
    """ダウンロード前のリワード広告の確認画面（REWARDED_AD_UNIT 設定時、またはプレビュー時のみ動く）"""
    if not (REWARDED_AD_UNIT or PREVIEW): return ""
    u = UI[lang]
    cfg = json.dumps({"unit": REWARDED_AD_UNIT, "preview": PREVIEW, "loading": u["rw_loading"],
                      "closed": u["rw_closed"], "thanks": u["rw_thanks"]}, ensure_ascii=False)
    return f"""<div class="rw" id="rw" hidden role="dialog" aria-modal="true" aria-labelledby="rw-title" data-cfg='{e(cfg)}'>
  <div class="rw-box">
    <img src="/images/svg/gift-box.svg" alt="" width="96" height="96">
    <h2 id="rw-title">{e(u['rw_title'])}</h2>
    <p id="rw-msg">{e(u['rw_body'])}</p>
    <div class="rw-actions">
      <button type="button" class="btn primary" id="rw-ok">{e(u['rw_watch'])}</button>
      <button type="button" class="btn" id="rw-cancel">{e(u['rw_cancel'])}</button>
    </div>
  </div>
</div>"""


TEXT_PAGES = ["about-us", "faq", "license", "privacy", "contact"]


def page_text(lang, kind):
    u = UI[lang]
    n = f"{len(ITEMS) // 100 * 100:,}"
    title = u[f"{kind}_title"]
    body_secs = [(h, p.replace("{n}", n)) for h, p in u[f"{kind}_body"]]
    secs = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in body_secs)
    jsonld = None
    if kind == "faq":
        jsonld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": u["html_lang"],
                  "mainEntity": [{"@type": "Question", "name": h,
                                  "acceptedAnswer": {"@type": "Answer", "text": p}} for h, p in body_secs]}
    mail = f'<p class="mail"><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>' if kind in ("contact", "privacy", "license") else ""
    body = f"""<article class="prose"><h1>{e(title)}</h1>{secs}{mail}</article>"""
    desc = body_secs[0][1][:150]
    return layout(lang, kind, None, title, desc, body, jsonld=jsonld)


def adsense_tag():
    return (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" '
            f'crossorigin="anonymous"></script>') if ADSENSE_CLIENT else ""


def page_root():
    links = "".join(f'<a href="/{l}/" hreflang="{UI[l]["html_lang"]}">{e(UI[l]["lang_name"])}</a>' for l in LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{UI[l]["html_lang"]}" href="{SITE_URL}/{l}/">' for l in LANGS)
    langs_js = json.dumps(LANGS)
    en = UI["en"]
    intros = "".join(f'<li lang="{UI[l]["html_lang"]}"><a href="/{l}/"><b>{e(UI[l]["lang_name"])}</b></a> — {e(UI[l]["root_intro"])}</li>'
                     for l in LANGS)
    cards = "".join(card(i, "en") for i in NEWEST[:24])
    foot = "".join(f'<a href="{url("en", k)}">{e(en[k] if k != "license" else en["license"])}</a>' for k in TEXT_PAGES)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_NAME} — free cute illustrations (commercial use OK)</title>
<meta name="description" content="{e(UI['en']['meta_desc'])}">
<link rel="canonical" href="{SITE_URL}/">
{alts}<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap">
<link rel="stylesheet" href="/static/style.css?v={ASSET_V['style.css']}">
{adsense_tag()}
<script>(function(){{if(/bot|crawl|spider|slurp|google|mediapartners|adsbot|lighthouse/i.test(navigator.userAgent))return;
if(sessionStorage&&sessionStorage.getItem("fw-stay"))return;
var L={langs_js};var p=(navigator.languages||[navigator.language||"en"]);
for(var i=0;i<p.length;i++){{var c=(p[i]||"").toLowerCase().split("-")[0];if(L.indexOf(c)>-1){{location.replace("/"+c+"/");return;}}}}
location.replace("/{DEFAULT_LANG}/");}})();</script>
</head><body class="root-page"><main class="root wrap">{LOGO.replace('width="34" height="34"', 'width="72" height="72"')}
<h1>{SITE_NAME}</h1><p>Free, soft &amp; cute illustrations</p>
<p class="root-lead">{e(en['root_intro'])}</p>
<nav class="root-langs">{links}</nav>
<h2 class="section-title">{e(en['latest'])}</h2>
<div class="grid">{cards}</div>
<h2 class="section-title">Choose your language</h2>
<ul class="root-intros">{intros}</ul>
<p class="root-foot">{foot}</p>
</main></body></html>"""


def sitemap(lang):
    """言語ごとのサイトマップ（hreflang の相互リンク＋イラストページには画像情報付き）"""
    rows = []
    pages = [("home", None)] + [(k, None) for k in TEXT_PAGES]
    for c in CATS:
        n = -(-len(cat_items(c)) // PER_PAGE)
        pages += [("cat", c if k == 1 else f"{c}/{k}") for k in range(1, n + 1)]
    pages += [("illust", i["slug"]) for i in ITEMS]
    titles = {i["slug"]: t(i, lang)[0] for i in ITEMS}
    for kind, arg in pages:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{UI[l]["html_lang"]}" href="{SITE_URL}{url(l, kind, arg)}"/>'
                       for l in LANGS)
        img = ""
        if kind == "illust":
            img = (f'<image:image><image:loc>{SITE_URL}/images/png/{arg}.png</image:loc></image:image>')
        rows.append(f"<url><loc>{SITE_URL}{url(lang, kind, arg)}</loc>{alts}{img}</url>")
    for name, _ in TAGS[lang].values():
        rows.append(f"<url><loc>{SITE_URL}{url(lang, 'tag', name)}</loc></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
            + "".join(rows) + "</urlset>")


def sitemap_index():
    today = date.today().isoformat()
    rows = "".join(f"<sitemap><loc>{SITE_URL}/sitemap-{l}.xml</loc><lastmod>{today}</lastmod></sitemap>" for l in LANGS)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + rows + "</sitemapindex>")


def write(path, text):
    full = os.path.join(OUT, unquote(path).lstrip("/"))
    if full.endswith("/"): full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)


def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    shutil.copytree("public", OUT)
    shutil.copytree("static", os.path.join(OUT, "static"))
    build_tags()
    for lang in LANGS:
        for key in TAGS[lang]:
            write(url(lang, "tag", TAGS[lang][key][0]), page_tag(lang, key))
        write(url(lang), page_home(lang))
        for kind in TEXT_PAGES:
            write(url(lang, kind), page_text(lang, kind))
        for c in CATS:
            n = -(-len(cat_items(c)) // PER_PAGE)
            for k in range(1, n + 1):
                write(url(lang, "cat", c if k == 1 else f"{c}/{k}"), page_cat(lang, c, k))
        write(f"/{lang}/search.json", search_index(lang))
        for item in ITEMS:
            write(url(lang, "illust", item["slug"]), page_illust(lang, item))
    write("/index.html", page_root())
    write("/404.html", page_root().replace('<script>', '<script type="text/plain">').replace(
        "<p>Free, soft &amp; cute illustrations</p>", "<p>404 — Page not found</p>"))
    for l in LANGS:
        write(f"/sitemap-{l}.xml", sitemap(l))
    write("/sitemap.xml", sitemap_index())
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("/favicon.svg", LOGO.replace(' width="34" height="34"', ' xmlns="http://www.w3.org/2000/svg"'))
    if ADSENSE_CLIENT:
        write("/ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print(f"built {OUT}/ — {len(LANGS)} languages, {len(ITEMS)} illustrations, {n} files{' (preview)' if PREVIEW else ''}")


if __name__ == "__main__":
    main()
