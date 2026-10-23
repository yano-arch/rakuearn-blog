(function () {
  /* トップの検索：全イラストの索引（/{lang}/search.json）から探して表示する */
  var input = document.getElementById("q");
  if (!input) return;
  var results = document.getElementById("results"), browse = document.getElementById("browse");
  var grid = document.getElementById("grid"), empty = document.getElementById("empty"), count = document.getElementById("count");
  var base = input.getAttribute("data-base"), index = null, loading = null;

  function load() {
    if (index) return Promise.resolve(index);
    if (!loading) loading = fetch(input.getAttribute("data-index")).then(function (r) { return r.json(); })
      .then(function (d) {
        index = d.map(function (x) {
          return { s: x[0], t: x[1], n: norm(x[1]), k: norm(x[2] + " " + x[0].replace(/-/g, " ")), d: norm(x[3] || "") };
        });
        return index;
      });
    return loading;
  }
  // ひらがな・カタカナ・全角英数を同じものとして扱う
  function norm(t) {
    return t.toLowerCase().replace(/[\u30a1-\u30f6]/g, function (c) { return String.fromCharCode(c.charCodeAt(0) - 0x60); })
      .replace(/[\uff01-\uff5e]/g, function (c) { return String.fromCharCode(c.charCodeAt(0) - 0xfee0); });
  }
  function esc(t) { return t.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function run() {
    var q = norm(input.value.trim());
    var u = new URL(location.href);
    if (q) u.searchParams.set("q", input.value.trim()); else u.searchParams.delete("q");
    history.replaceState(null, "", u);
    if (!q) { results.hidden = true; browse.hidden = false; return; }
    load().then(function (idx) {
      var words = q.split(/\s+/);
      // タイトル → タグ → 説明文 の順に当てはまり度で並べる
      var hits = [];
      idx.forEach(function (x) {
        var sc = 0;
        for (var i = 0; i < words.length; i++) {
          var w = words[i];
          if (x.n.indexOf(w) > -1) sc += x.n === w ? 6 : 4;
          else if (x.k.indexOf(w) > -1) sc += 2;
          else if (x.d.indexOf(w) > -1) sc += 1;
          else return;
        }
        hits.push({ x: x, sc: sc });
      });
      hits = hits.sort(function (a, b) { return b.sc - a.sc; }).map(function (h) { return h.x; });
      grid.innerHTML = hits.slice(0, 300).map(function (x) {
        return '<a class="card" href="' + base + x.s + '/"><span class="thumb"><img src="/images/svg/' + x.s +
          '.svg" alt="' + esc(x.t) + '" width="200" height="200" loading="lazy"></span><span class="name">' + esc(x.t) + "</span></a>";
      }).join("");
      empty.hidden = hits.length !== 0;
      count.textContent = count.getAttribute("data-tpl").replace("{n}", hits.length);
      results.hidden = false; browse.hidden = true;
    });
  }
  var timer;
  input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(run, 120); });
  input.form.addEventListener("submit", function (ev) { ev.preventDefault(); clearTimeout(timer); run(); input.blur(); });
  var init = new URLSearchParams(location.search).get("q");
  if (init) {
    input.value = init; run();
    // ほかのページの検索窓から来たときは、結果が見える位置までスクロール
    if (document.referrer.indexOf(location.origin) === 0) input.form.scrollIntoView({ block: "start" });
  }
})();

/* ダウンロード共通処理と、人物イラストの肌の色切り替え */
(function () {
  function save(url, name) {
    var t = document.createElement("a");
    t.href = url; t.download = name || "";
    document.body.appendChild(t); t.click(); t.remove();
  }
  var box = document.getElementById("skin"), art = document.getElementById("art");
  var base = box && box.getAttribute("data-base"), tone = base, svgText = null;

  function getSvg() {
    if (svgText) return Promise.resolve(svgText);
    return fetch(box.getAttribute("data-svg")).then(function (r) { return r.text(); })
      .then(function (t) { svgText = t; return t; });
  }
  function recolored() {
    return getSvg().then(function (t) { return t.split(base).join(tone); });
  }
  function toneName(a) {
    var n = a.getAttribute("download") || "";
    var i = Array.prototype.indexOf.call(box.querySelectorAll(".sw"), box.querySelector(".sw.on"));
    return n.replace(/\.(png|svg)$/, "-skin" + (i + 1) + ".$1");
  }

  // a[data-dl] のダウンロードを実行（肌の色を変えていれば、その色で書き出す）
  window.FuwaDL = function (a) {
    if (!box || tone === base) return save(a.href, a.getAttribute("download"));
    var kind = a.getAttribute("data-dl"), name = toneName(a);
    return recolored().then(function (text) {
      var svgUrl = URL.createObjectURL(new Blob([text], { type: "image/svg+xml" }));
      if (kind === "svg") { save(svgUrl, name); setTimeout(function () { URL.revokeObjectURL(svgUrl); }, 4000); return; }
      return new Promise(function (resolve) {
        var img = new Image();
        img.onload = function () {
          var c = document.createElement("canvas"); c.width = 1000; c.height = 1000;
          c.getContext("2d").drawImage(img, 0, 0, 1000, 1000);
          URL.revokeObjectURL(svgUrl);
          c.toBlob(function (b) {
            var u = URL.createObjectURL(b); save(u, name);
            setTimeout(function () { URL.revokeObjectURL(u); }, 4000); resolve();
          }, "image/png");
        };
        img.src = svgUrl;
      });
    });
  };

  // リワード広告がないページでは、肌の色を変えたときだけ自前で書き出す
  if (!document.getElementById("rw")) {
    document.addEventListener("click", function (ev) {
      var a = ev.target.closest && ev.target.closest("a[data-dl]");
      if (!a || !box || tone === base) return;
      ev.preventDefault(); window.FuwaDL(a);
    });
  }

  if (!box || !art) return;
  var original = art.src;
  box.addEventListener("click", function (ev) {
    var b = ev.target.closest(".sw");
    if (!b) return;
    box.querySelectorAll(".sw").forEach(function (x) { x.classList.remove("on"); x.setAttribute("aria-pressed", "false"); });
    b.classList.add("on"); b.setAttribute("aria-pressed", "true");
    tone = b.getAttribute("data-c");
    if (tone === base) { art.src = original; return; }
    recolored().then(function (t) { art.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(t); });
  });
})();

/* ダウンロード前のリワード広告（Google Ad Manager / GPT）
   広告が出ない・読み込めない・広告ブロック時は、待たせずにそのままダウンロードする */
(function () {
  var rw = document.getElementById("rw");
  if (!rw) return;
  var cfg = JSON.parse(rw.getAttribute("data-cfg"));
  var msg = document.getElementById("rw-msg"), ok = document.getElementById("rw-ok"), cancel = document.getElementById("rw-cancel");
  var bodyText = msg.textContent, pending = null, busy = false;

  function download(a) { window.FuwaDL(a); }
  function close() { rw.hidden = true; busy = false; ok.disabled = false; ok.hidden = false; msg.textContent = bodyText; }
  function fallback() { download(pending); close(); }
  function finish(granted) {
    rw.hidden = false; busy = false; ok.disabled = false;
    if (granted) { msg.textContent = cfg.thanks; ok.hidden = true; download(pending); setTimeout(close, 1500); }
    else { msg.textContent = cfg.closed; }
  }

  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a[data-dl]");
    if (!a) return;
    ev.preventDefault(); pending = a; rw.hidden = false; ok.focus();
  });
  cancel.addEventListener("click", close);
  rw.addEventListener("click", function (e) { if (e.target === rw && !busy) close(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !rw.hidden && !busy) close(); });
  ok.addEventListener("click", function () {
    if (busy) return;
    busy = true; ok.disabled = true; msg.textContent = cfg.loading;
    if (!cfg.unit) return previewAd();
    showRewarded();
  });

  // プレビュー用：5秒のダミー広告
  function previewAd() {
    var n = 5, box = document.createElement("div");
    box.className = "rw-fake"; rw.hidden = true; document.body.appendChild(box);
    (function tick() {
      box.textContent = "AD (rewarded) " + n;
      if (n-- <= 0) { box.remove(); finish(true); } else setTimeout(tick, 1000);
    })();
  }

  function showRewarded() {
    var done = false;
    var timer = setTimeout(function () { if (!done) { done = true; fallback(); } }, 8000);
    function giveUp() { if (!done) { done = true; clearTimeout(timer); fallback(); } }
    window.googletag = window.googletag || { cmd: [] };
    if (!document.getElementById("gpt-js")) {
      var sc = document.createElement("script");
      sc.id = "gpt-js"; sc.async = true; sc.src = "https://securepubads.g.doubleclick.net/tag/js/gpt.js";
      sc.onerror = giveUp; document.head.appendChild(sc);
    }
    googletag.cmd.push(function () {
      var slot = googletag.defineOutOfPageSlot(cfg.unit, googletag.enums.OutOfPageFormat.REWARDED);
      if (!slot) return giveUp();
      slot.addService(googletag.pubads());
      var pubads = googletag.pubads(), granted = false;
      function onReady(e) { if (e.slot !== slot) return; done = true; clearTimeout(timer); rw.hidden = true; e.makeRewardedVisible(); }
      function onGranted(e) { if (e.slot === slot) granted = true; }
      function onRender(e) { if (e.slot === slot && e.isEmpty) giveUp(); }
      function onClosed(e) {
        if (e.slot !== slot) return;
        pubads.removeEventListener("rewardedSlotReady", onReady);
        pubads.removeEventListener("rewardedSlotGranted", onGranted);
        pubads.removeEventListener("rewardedSlotClosed", onClosed);
        pubads.removeEventListener("slotRenderEnded", onRender);
        googletag.destroySlots([slot]);
        finish(granted);
      }
      pubads.addEventListener("rewardedSlotReady", onReady);
      pubads.addEventListener("rewardedSlotGranted", onGranted);
      pubads.addEventListener("rewardedSlotClosed", onClosed);
      pubads.addEventListener("slotRenderEnded", onRender);
      googletag.enableServices();
      googletag.display(slot);
    });
  }
})();
