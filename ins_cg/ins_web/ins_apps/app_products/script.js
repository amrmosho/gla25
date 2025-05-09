ins(".-open-panel")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active");
    } else {
        o._addClass("ins-active");
    }
}, true)
ins(".-minus-btn")._on("click", (o) => {
    if (ins(".count-inpt")._getValue() > 1) {
        ins(".count-inpt")._setValue(ins(".count-inpt")._getValue() - 1);
    }
}, true)
ins(".-plus-btn")._on("click", (o) => {
    let val = parseInt(ins(".count-inpt")._getValue(), 10);
    ins(".count-inpt")._setValue(val + 1);
}, true)






ins(".-pro-d-tabs")._on("click", (o) => {
    ins(".-pro-d-tabs")._removeClass("ins-primary")
    o._addClass("ins-primary")
    ins(".-pro-d-cont")._addClass("ins-hidden")
    ins("." + o._getData('s'))._removeClass("ins-hidden")

}, true)





ins(".p-comments-btn")._on("click", (o) => {



    ins(".p-comments-cont")._data._submit((data) => {

        ins("plg_comments.ajax")._ajax._plgin(data, (data) => {

            ins(".p-comments-data")._setHTML(data);
        })

    })


})

ins(".-pro-action")._on("click", (o) => {

    ins("plg_comments.ajax")._ajax._plgin(o._getData(), (data) => {

        console.log(data);
    })
    ins("_pro_action")._ajax._app(o._getData(), (data) => {

        if (data.trim() == "1") {

            o._addClass("ins-success")

        } else {

            o._removeClass("ins-success")


        }
    })

}, true)



ins(".-filter-menu")._on("click", (o) => {
    if (ins(".-filter-area")._hasClass("menu-open")) {
        ins(".-filter-area")._removeClass("menu-open")
    } else {
        ins(".-filter-area")._addClass("menu-open")
    }
}, true);



ins(".-close-filter")._on("click", (o) => {
    ins(".-filter-area")._removeClass("menu-open")

}, true);




ins(".-continue-shopping-btn")._on("click", (o) => {
    ins(".ins-panel-overlay.ins-opened")._remove()
    ins()._ui._removeLightbox();
}, true)


/**Filter Area */

ins(".-type-btn")._on("click", function(o) {

    if (o._hasClass("ins-active")) {
        ins(".-type-btn")._removeClass("ins-active")
    } else {
        ins(".-type-btn")._removeClass("ins-active")
        o._addClass("ins-active")
    }

    _submitfilter()

});





ins(".-type-inner-btn")._on("click", function(o) {
    if (!o._hasClass("ins-active")) {
        ins(".-subtype-inner-btn")._removeClass("ins-active")
        ins(".-type-inner-btn")._removeClass("ins-active")
        o._addClass("ins-active");
        var ops = o._getData()
        ins("_show_subtypes_inner")._ajax._app(ops, (d) => {
            ins(".-subtypes-area")._setHTML(d)
            _submitfilterInner()

        })

    }
});


ins(".-subtype-inner-btn")._on("click", function(o) {

    if (!o._hasClass("ins-active")) {
        ins(".-subtype-inner-btn")._removeClass("ins-active")
        o._addClass("ins-active");
        _submitfilterInner()
    }
});



function _submitfilterInner() {
    t = "";
    sp = "";
    pid = 0

    ins(".-type-inner-btn.ins-active")._each(function(item) {
        t += sp + item._getData("name");
        pid = item._getData("pid")
        sp = ",";
    });
    st = "";
    sp = "";
    ins(".-subtype-inner-btn.ins-active")._each(function(sitem) {
        st += sp + sitem._getData("name");
        sp = ",";
    });

    var types = "";
    if (t != "") {
        types = "types=" + t;
    }

    var subtypes = "";
    if (st != "") {
        subtypes = "subtypes=" + st;
    }
    var sql = ""
    spr = "";
    if (types != "") {
        sql += spr + types;
        spr = "&";
    }
    if (subtypes != "") {
        sql += spr + subtypes;
        spr = "&";
    }
    if (sql != "") {
        ins("_filter_redirect_inner")._ajax._app({ "sql": sql, "type": "search", "pid": pid }, function(data) {
            window.location = data;
        })
    } else {
        ins("No filter selected")._ui._notification()
    }
}


ins(".-category-checkbox")._on("change", function(o) {
    ins(".-weight-select")._setValue("")
    ins(".-type-btn")._removeClass("ins-active")
    if (o._get(0).checked) {
        ins(".-category-checkbox")._each(function(item) {
            item._get(0).checked = false;
        });
        o._get(0).checked = true;
    } else {
        o._get(0).checked = false;
    }
    _submitfilter();
}, true);




ins(".-filter-price-btn")._on("click", function(o) {

    var from = ins(".-price-from-input")._getValue()
    var to = ins(".-price-to-input")._getValue()
    if (from == "" && to == "") {
        ins("You have to enter 'From' and 'To' values")._ui._notification({ class: "ins-danger" })

    } else if (from == "") {
        ins("You have to enter 'From' value")._ui._notification({ class: "ins-danger" })

    } else if (to == "")(
        ins("You have to enter 'To' value")._ui._notification({ class: "ins-danger" })

    )
    else {
        _submitfilter()

    }




}, true)

ins(".-price-to-filter-input")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _submitfilter()
    }
})


function _remove_filter(name, type = "") {

    if (name == "fk_product_category_id" || type == "all") {
        ins(".-category-checkbox")._each(function(item) {
            item._get(0).checked = false;
        });
        ins(".-type-btn.ins-active")._each(function(item) {
            item._removeClass("ins-active")
        });
    }
    if (name == "types_data" || type == "all") {
        ins(".-type-btn.ins-active")._each(function(item) {
            item._removeClass("ins-active")
        });
    }

    if (name == "price_range" || type == "all") {
        ins(".-price-from-input")._setValue("")
        ins(".-price-to-input")._setValue("")
    }

    if (name == "weight" || type == "all") {
        ins(".-weight-select")._setValue("")
    }

    if (name == "title" || type == "all") {
        ins(".-product-filter-input")._setValue("")
    }


    _submitfilter()
}









ins(".-remove-filter-btn")._on("click", (o) => {
    _remove_filter(o._getData("name"), type = "")

})

ins(".-remove-filter-all-btn")._on("click", (o) => {
    _remove_filter("", "all")

})


ins(".-product-filter-input")._on("change", (o) => {
    _submitfilter()
})


ins(".-order-select")._on("change", (o) => {
    _submitfilter()
})


function _submitfilter() {

    var tit = ins(".-product-filter-input")._getValue();
    var title = ""
    if (tit != "") {
        title = "title=" + tit
    }


    var c = "";
    sp = "";
    ins(".-category-checkbox")._each(function(item) {
        if (item._checked()) {
            c += sp + item._getData("value");
            sp = ",";
        }
    });
    var category = "";
    if (c != "") {
        category = "fk_product_category_id=" + c;
    }

    t = "";
    sp = "";
    ins(".-type-btn.ins-active")._each(function(item) {
        t += sp + item._getData("name");
        sp = ",";
    });
    var types = "";
    if (t != "") {
        types = "types_data=" + t;
    }

    var weight = "";
    if (ins(".-weight-select")._getValue() != "" && ins(".-weight-select")._getValue() != 0) {
        weight = "weight=" + ins(".-weight-select")._getValue();
    }

    var fromPrice = ins(".-price-from-filter-input")._getValue();
    var toPrice = ins(".-price-to-filter-input")._getValue();
    var priceRange = "";
    if (fromPrice != "" && toPrice != "") {
        priceRange = "price_range=" + fromPrice + "-" + toPrice;
    }

    var sql = "";
    spr = "";

    if (category != "") {
        sql += spr + category;
        spr = "&";
    }
    if (title != "") {
        sql += spr + title;
        spr = "&";
    }
    if (types != "") {
        sql += spr + types;
        spr = "&";
    }
    if (weight != "") {
        sql += spr + weight;
        spr = "&";
    }
    if (priceRange != "") {
        sql += spr + priceRange;
        spr = "&";
    }
    var order = ins(".-order-select")._getValue()
    if (sql != "" || order != "") {
        stype = "search"
    } else {
        stype = "reset"
    }

    ins("_filter_redirect")._ajax._app({ "sql": sql, "type": stype, order: order }, function(data) {
        window.location = data;
    });
}