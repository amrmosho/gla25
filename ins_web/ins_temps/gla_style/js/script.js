ins(".gla-phone-menu")._on("click", (o) => {
    if (ins("body")._hasClass("menu-open")) {
        ins("body")._removeClass("menu-open")
    } else {
        ins("body")._addClass("menu-open")
    }
});