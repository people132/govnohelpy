function(a) {
    var b = a.target.closest("a");
    if (!a.metaKey && b) {
      var c = H.decode(b.getAttribute("href"));
      if (c && lj(c) && "_blank" !== b.getAttribute("target") && !/^\/p\//.test(c.path)) {
        var d, e = b.closest("*[data-id]");
        e && (d = e.getAttribute(hb));
        e = !1;
        var f = b.closest(".article-content");
        f && (e = "articleBody" == f.getAttribute("itemprop"));
        if ((d || e) && !this.A.getSetting(tb) && !Mi(b, "label") && !c.path.startsWith("/search/label")) return this.A.select(e ? c.url : d, b), a.preventDefault(), a.stopPropagation(), !1;
        a = b.getAttribute("data-view-name");
        b = H.decode();
        a ? (b.param(yc, c.param(yc)), c = b) : (b.param(Wa) && 0 < b.param(Wa).length && c.param(Wa, b.param(Wa)), b.param(yc) && c.param(yc, b.param(yc)));
        (c = c.encode()) && window.location.href != c && Zg(window.location, c);
        return !1
      }
    }

    function(a) {
        var b = a.target.closest(g);
        if (b) {
          var c = b.dataset.id;
          if (c && !a.metaKey) {
            if (a.target.matches("a")) {
              var d = a.target.getAttribute("href");
              if (H.decode(d).authority && H.isCrossDomain(d) && a.target.closest(".title")) return
            }
            a.stopPropagation();
            a.preventDefault();
            this.ui.select(c, b);
            return !1
          }
        }
      }