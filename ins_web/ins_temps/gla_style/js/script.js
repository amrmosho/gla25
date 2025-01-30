ins(".gla-phone-menu")._on("click", (o) => {
    if (ins("body")._hasClass("menu-open")) {
        ins("body")._removeClass("menu-open")
    } else {
        ins("body")._addClass("menu-open")
    }
}, true);
ins(".gla-header-search-btn")._on("click", (o) => {
    if (ins("body")._hasClass("open-search")) {
        ins("body")._removeClass("open-search")
    } else {
        ins("body")._addClass("open-search")
    }
}, true);

ins(".gla-header-search-input")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {

        var v = o._getValue();

        window.location = "/product/do/filter/title=" + v;
    }
}, true);