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



ins(".gla-search-btn")._on("click", (o, e) => {
    var v = ins(".gla-header-search-input")._getValue();
    window.location = "/product/do/filter/title=" + v;
}, true);

ins(".gla-header-search-input")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        var v = o._getValue();
        window.location = "/product/do/filter/title=" + v;
    }
}, true);

function _submit() {
    var v = ins(".-cal-update-nput")._getValue();
    if (v === "" || v === null || v === undefined || v == 0 || isNaN(v)) {
        ins("Please enter a valid number")._ui._notification({ "class": "ins-danger" });
    } else {
        window.location = "/plan/" + v + "/";
    }
}




function _submit_phone() {
    var v = ins(".-cal-update-nput-phone")._getValue();
    if (v === "" || v === null || v === undefined || v == 0 || isNaN(v)) {
        ins("Please enter a valid number")._ui._notification({ "class": "ins-danger" });
    } else {
        window.location = "/plan/" + v + "/";
    }
}





ins(".-cal-update-btn-phone")._on("click", (o) => {
    _submit_phone();
}, true)

ins(".-cal-update-nput-phone")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _submit_phone();
    }
}, true)



ins(".-cal-update-btn")._on("click", (o) => {
    _submit();
}, true)

ins(".-cal-update-nput")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _submit();
    }
}, true)






ins(".-logout-btn")._on("click", (o) => {
    ins("_logout")._ajax._app({ "_p": "app_content" }, (d) => {
        window.location = "/"
    })
}, true)