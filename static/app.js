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
