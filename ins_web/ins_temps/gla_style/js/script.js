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


ins(".-user-menu-btn")._on("click", (o) => {
    if (ins("body")._hasClass("open-user-menu")) {
        ins("body")._removeClass("open-user-menu")
    } else {
        ins("body")._addClass("open-user-menu")
    }
}, true);


ins(".gla-header-search-input")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {

        var v = o._getValue();

        window.location = "/product/do/filter/title=" + v;
    }
}, true);

function _submit() {
    var v = ins(".-cal-update-nput")._getValue();
    if (v == "" || v == null || v == undefined || v == 0) {
        ins("Please enter a valid number")._ui._notification({ "class": "ins-danger" });
    } else {
        window.location = "/plan/" + v + "/";
    }


}

ins(".-cal-update-btn")._on("click", (o) => {
    _submit();
}, true)

ins(".-cal-update-nput")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _submit();
    }
}, true)