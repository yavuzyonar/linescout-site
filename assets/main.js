// OddsLighthouse — shared behavior: age gate + dynamic article listing

(function ageGate() {
  var KEY = "oddslighthouse_age_ok";
  document.addEventListener("DOMContentLoaded", function () {
    var gate = document.getElementById("age-gate");
    if (!gate) return;
    var ok = false;
    try { ok = localStorage.getItem(KEY) === "1"; } catch (e) {}
    if (ok) { gate.classList.add("hidden"); return; }
    var yes = document.getElementById("age-yes");
    var no = document.getElementById("age-no");
    if (yes) yes.addEventListener("click", function () {
      try { localStorage.setItem(KEY, "1"); } catch (e) {}
      gate.classList.add("hidden");
    });
    if (no) no.addEventListener("click", function () {
      window.location.href = "https://www.ncpgambling.org/";
    });
  });
})();

// Renders article cards into a container from articles/manifest.json.
// `base` = relative path prefix to the site root (e.g. "" on homepage, "../" inside /articles/).
function renderArticleList(containerId, base, opts) {
  opts = opts || {};
  var el = document.getElementById(containerId);
  if (!el) return;
  fetch(base + "articles/manifest.json", { cache: "no-store" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var items = data.articles.slice().sort(function (a, b) {
        return new Date(b.date) - new Date(a.date);
      });
      if (opts.category) items = items.filter(function (a) { return a.category === opts.category; });
      if (opts.categories) items = items.filter(function (a) { return opts.categories.indexOf(a.category) !== -1; });
      if (opts.excludeCategories) items = items.filter(function (a) { return opts.excludeCategories.indexOf(a.category) === -1; });
      if (opts.limit) items = items.slice(0, opts.limit);
      if (items.length === 0) {
        el.innerHTML = '<p style="color:#94a0b2;">No guides in this section yet — check back soon.</p>';
        return;
      }
      el.innerHTML = items.map(function (a) {
        return (
          '<div class="card">' +
            '<div class="kicker">' + a.category + '</div>' +
            '<h3><a href="' + base + 'articles/' + a.slug + '.html">' + a.title + '</a></h3>' +
            '<p>' + a.excerpt + '</p>' +
            '<div class="meta">' + a.date + ' &middot; ' + a.readTime + '</div>' +
          '</div>'
        );
      }).join("");
    })
    .catch(function () {
      el.innerHTML = '<p style="color:#94a0b2;">Articles are loading — refresh in a moment.</p>';
    });
}
