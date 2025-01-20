if (menujs == null) {
    var menujs = 0;
    ins(".ins-menu-parent")._on("click", (o) => {
        if (!o._hasClass("open-item")) {
            ins(".ins-menu-item")._removeClass("open-item");
            o._addClass("open-item");
            ins("body")._addClass("sub-menu-open");
        } else {
            ins(".ins-menu-item")._removeClass("open-item");
            ins("body")._removeClass("sub-menu-open");
        }

    }, true)
}