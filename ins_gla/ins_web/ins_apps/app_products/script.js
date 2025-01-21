ins(".-open-panel")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active");
    } else {
        o._addClass("ins-active");
    }
}, true)
ins(".-type-btn")._on("click", (o) => {



    if (o._hasClass("ins-active")) {
        o._setCSS({ border: " 1px solid var(--grey-l)" });
        o._removeClass("ins-gold-bg", "ins-gold-color", "ins-active");
        o._addClass("ins-grey-color");

    } else {
        ins(".-type-btn")._removeClass("ins-gold-bg", "ins-gold-color", "ins-active");
        ins(".-type-btn")._addClass("ins-grey-color");
        ins(".-type-btn")._setCSS({ border: " 1px solid var(--grey-l)" });
        o._removeCSS("border");
        o._addClass("ins-gold-bg", "ins-gold-color", "ins-active");
        o._removeClass("ins-grey-color");
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
    ins(".-main-img")._setAttribute("src", src);
}, true)



// Pagination
ins(".ins-pagination-btn")._on("click", (o) => {
    var page = o._getData("page");
    var currentPage = parseInt(ins(".ins-pagination-btn.active")._getData("page"), 10);
    ins(".ins-pagination-btn")._removeClass("active");
    if (page === "prev") {
        if (currentPage > 1) {
            get_page(currentPage - 1);
        } else {
            get_page(currentPage);
        }
    } else if (page == "next") {
        var numPages = o._getData("tpages");
        if (currentPage < numPages) {
            get_page(currentPage + 1);
        } else {
            get_page(currentPage);
        }
    } else if (page == "first") {
        get_page(1);
    } else if (page == "last") {
        get_page(numPages);
    } else {
        get_page(parseInt(page, 10));
        o._addClass("active");
    }
}, true);

function get_page(page) {
    ins("generate_product_html")._ajax._app({ "page": page }, function(data) {
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
            style: "width:500px;    "
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
            ins("Item removed!")._ui._notification({ "class": "ins-success" })
        })
    }

}, true)