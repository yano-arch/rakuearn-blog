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

/* ダウンロード前のリワード広告（Google Ad Manager / GPT）
   広告が出ない・読み込めない・広告ブロック時は、待たせずにそのままダウンロードする */
(function () {
  var rw = document.getElementById("rw");
  if (!rw) return;
  var cfg = JSON.parse(rw.getAttribute("data-cfg"));
  var msg = document.getElementById("rw-msg"), ok = document.getElementById("rw-ok"), cancel = document.getElementById("rw-cancel");
  var bodyText = msg.textContent, pending = null, busy = false;

  function download(a) {
    var t = document.createElement("a");
    t.href = a.href; t.download = a.getAttribute("download") || "";
    document.body.appendChild(t); t.click(); t.remove();
  }
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
