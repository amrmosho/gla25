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
    // Active main image
ins(".-side-img")._on("click", (o) => {
        var src = o._getData("src");
        var p = o._parent(".-side-img-cont");
        ins(".-side-img")._removeClass("ins-active");
        ins(".-side-img-cont")._removeClass("ins-active");
        o._addClass("ins-active");
        p._addClass("ins-active");
        ins(".-main-img")._addClass("gla-ahide");
        setTimeout(() => {
            ins(".-main-img")._setAttribute("src", src);
            ins(".-main-img")._removeClass("gla-ahide");
        }, 100);
    }, true)
    // Pagination
ins(".ins-pagination-btn")._on("click", (o) => {
    var page = o._getData("page");
    var currentPage = parseInt(ins(".ins-pagination-btn.active")._getData("page"), 10);
    if (page === "prev") {
        if (currentPage > 1) {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            get_page(currentPage - 1);
        }
    } else if (page == "next") {
        var numPages = o._getData("tpages");
        if (currentPage < numPages) {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            get_page(currentPage + 1);
        }
    } else if (page != currentPage) {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        get_page(parseInt(page, 10));
        o._addClass("active");
    }
}, true);
ins(".-go-to-page-btn")._on("click", (o) => {
    var numPages = o._getData("tpages");
    var page = ins(".-page-input")._getValue();
    var currentPage = parseInt(ins(".ins-pagination-btn.active")._getData("page"), 10);
    if (page == currentPage) {
        ins("You are already on this page")._ui._notification();
    } else {
        if (page == 0 || page == "") {
            ins("Type page number")._ui._notification({ class: "ins-danger" });
        } else {
            if (numPages < page) {
                ins("This page not exist")._ui._notification({ class: "ins-danger" });
            } else {
                get_page(page);
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }
        }
    }
}, true);



function get_page(page) {
    ins(".ins-pagination-btn")._removeClass("active");

    url = ins()._map._hurl({ "page": page })
    window.location = url
}
ins(".-add-cart-btn")._on("click", (o) => {
    var ops = o._getData();
    ops.count = ins(".count-inpt")._getValue()
    ops["lang"] = "ar"
    ins("_cart_lightbox_ui")._ajax._app(ops, (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-cart  '></i> Cart",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:650px;    "
        });
    })
})
ins(".-continue-shopping-btn")._on("click", (o) => {
    ins(".ins-panel-overlay.ins-opened")._remove()
    ins()._ui._removeLightbox();
}, true)
ins(".-remove-item-cart-btn")._on("click", (o) => {
    var ops = o._getData()
    var p = o._parent(".-item-card");
    if (confirm("Are you sure tou want to remove this item from cart?")) {
        ins("_remove_item_cart")._ajax._app(ops, (data) => {
            var jdata = JSON.parse(data)
            if (jdata["status"] == "1") {
                ins(".-cart-cont")._setHTML(jdata["ui"])
            }
            p._remove()
            ins("Item removed!")._ui._notification()
        })
    }
}, true)
ins(".-remove-item-side-cart-btn")._on("click", (o) => {
        var ops = o._getData()
        var p = o._parents(".-item-card");
        if (confirm("Are you sure tou want to remove this item from cart?")) {
            ins("_remove_item_cart")._ajax._app(ops, (data) => {
                var jdata = JSON.parse(data)
                if (jdata["status"] == "1") {
                    ins(".-cart-cont")._setHTML(jdata["ui"])
                }
                p._remove()
                ins("Item removed!")._ui._notification()
            })
        }
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


    /*else {
        ins(".-subtype-btn")._removeClass("ins-active")
        ins(".-type-btn")._removeClass("ins-active")
        o._addClass("ins-active");
        var ops = o._getData()
        ins("_show_subtypes")._ajax._app(ops, (d) => {
            ins(".-subtypes-area")._setHTML(d)
        })
    }*/
});
/*
ins(".-subtype-btn")._on("click", function(o) {

    if (o._hasClass("ins-active")) {
        ins(".-subtype-btn")._removeClass("ins-active")
        ins(".-type-btn")._removeClass("ins-active")
        _submitfilter()
    } else {
        ins(".-subtype-btn")._removeClass("ins-active")
        o._addClass("ins-active");
        _submitfilter()
    }
});
*/












ins(".-type-inner-btn")._on("click", function(o) {
    if (!o._hasClass("ins-active")) {
        ins(".-subtype-inner-btn")._removeClass("ins-active")
        ins(".-type-inner-btn")._removeClass("ins-active")
        o._addClass("ins-active");
        var ops = o._getData()
        ins("_show_subtypes_inner")._ajax._app(ops, (d) => {
            ins(".-subtypes-area")._setHTML(d)
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
    }
    if (name == "types" || type == "all") {
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
        types = "types=" + t;
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

    if (sql != "") {

        stype = "search"
    } else {
        stype = "reset"
    }
    ins("_filter_redirect")._ajax._app({ "sql": sql, "type": stype }, function(data) {
        window.location = data;
    });
}