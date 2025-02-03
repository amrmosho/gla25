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
    var sql = ins(".-sql-filter-input")._getValue()
    ins("generate_product_html")._ajax._app({ "page": page, "sql": sql }, function(data) {
        ins(".-products-area")._setHTML(data);
    })
}
ins(".-add-cart-btn")._on("click", (o) => {
    var ops = o._getData();
    ops.count = ins(".count-inpt")._getValue()
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
    var value = o._getData("name");
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active");
    } else {
        o._addClass("ins-active");
    }
});

function _submitfilter() {
    var title = "";
    if (ins(".-title-input")._getValue() != "") {
        title = "title=" + ins(".-title-input")._getValue();
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
    var weight = ""
    if (ins(".-weight-select")._getValue() != "") {
        weight = "weight=" + ins(".-weight-select")._getValue();
    }
    var sql = ""
    spr = "";
    if (title != "") {
        sql = title;
        spr = "&";
    }
    if (category != "") {
        sql += spr + category;
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
    if (sql != "") {
        ins("_filter_redirect")._ajax._app({ "sql": sql, "type": "search" }, function(data) {
            window.location = data;
        })
    } else {
        ins("No filter selected")._ui._notification()
    }
}
ins(".-product-filter-input")._on("keyup", function(o, e) {
    if (e.keyCode == 13) {
        _submitfilter()
    }
});
ins(".-product-filter-btn")._on("click", function(o) {
    _submitfilter()
});