(function () {
  var input = document.getElementById("q");
  var grid = document.getElementById("grid");
  if (!input || !grid) return;
  var cards = grid.querySelectorAll(".card");
  var empty = document.getElementById("empty");
  var count = document.getElementById("count");

  function run() {
    var q = input.value.trim().toLowerCase();
    var words = q ? q.split(/\s+/) : [];
    var shown = 0;
    cards.forEach(function (c) {
      var hay = c.getAttribute("data-q") || "";
      var ok = words.every(function (w) { return hay.indexOf(w) > -1; });
      c.hidden = !ok;
      if (ok) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
    if (count) count.textContent = count.getAttribute("data-tpl").replace("{n}", shown);
    var u = new URL(location.href);
    if (q) u.searchParams.set("q", input.value.trim()); else u.searchParams.delete("q");
    history.replaceState(null, "", u);
  }

  var init = new URLSearchParams(location.search).get("q");
  if (init) { input.value = init; run(); }
  input.addEventListener("input", run);
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
