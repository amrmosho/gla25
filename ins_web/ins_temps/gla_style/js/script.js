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
    var u = ins()._map._hurl({ "s": v, "alias": "products" })

    window.location = u;
}, true);




ins(".gla-header-search-input")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        var v = o._getValue();

        var u = ins()._map._hurl({ "s": v, "alias": "products" })

        window.location = u;
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
    ins("ajx_users/logout")._ajax._ins_ajax({}, (o) => {
        window.location.reload();
    })
}, true)

ins(".-remove-error-msg")._on("click", (o) => {
    o._parents(".error-msg")._remove();
}, true)


ins(".-show-password")._on("click", (o) => {
    var f = o._parents(".ins-form-input-cont")._find(".ins-form-input");
    if (f._getAttribute("type") == "password") {
        f._setAttribute("type", "text")
        o._addClass("ins-active");
    } else {
        f._setAttribute("type", "password")
        o._removeClass("ins-active");
    }

}, true)