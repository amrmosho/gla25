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
            ins("Item removed!")._ui._notification({ "class": "ins-success" })
        })
    }

}, true)

ins(".-product-filter-btn")._on("click", (o) => {
    ins(".-filter-area")._data._submit((data) => {

        ins("_filter")._ajax._app(data, (d) => {

            console.log(d)
        })

    })
}, true)




/**Filter Area */
var filterData = {};

function updateSQL() {
    var sqlParts = [];
    for (var key in filterData) {
        if (Array.isArray(filterData[key])) {
            var orConditions = filterData[key].map(function(v) {
                return key + " LIKE '%" + v.toLowerCase() + "%'";
            }).join(" OR ");
            sqlParts.push("(" + orConditions + ")");
        } else {
            sqlParts.push(key + " LIKE '%" + filterData[key].toLowerCase() + "%'");
        }
    }
    var sql = sqlParts.join(" AND ");
    ins(".-sql-filter-input")._setValue(sql);
}







ins(".-title-input")._on("keyup", function(o) {
    var value = o._getValue().trim();
    if (value) {
        filterData["title"] = value;
    } else {
        delete filterData["title"];
    }
    updateSQL();
});


// Handle Type Button Functionality
ins(".-type-btn")._on("click", function(o) {
    var value = o._getData("name");

    if (o._hasClass("ins-active")) {
        o._setCSS({ border: "1px solid var(--grey-l)" });
        o._removeClass(["ins-gold-bg"], ["ins-gold-color"], ["ins-active"]);
        o._addClass("ins-grey-color");

        if (filterData["types"]) {
            filterData["types"] = filterData["types"].filter(function(v) {
                return v !== value;
            });
            if (filterData["types"].length === 0) {
                delete filterData["types"];
            }
        }
    } else {
        // Activate button styling
        o._removeCSS("border");
        o._addClass(["ins-gold-bg"], ["ins-gold-color"], ["ins-active"]);
        o._removeClass("ins-grey-color");

        // Add value to filterData
        if (!filterData["types"]) {
            filterData["types"] = [];
        }
        if (!filterData["types"].includes(value)) {
            filterData["types"].push(value);
        }
    }

    updateSQL();
});

ins(".-category-checkbox")._on("click", function(o) {
    var value = o._getData("value");
    if (o._checked()) {
        if (!filterData["fk_product_category_id"]) {
            filterData["fk_product_category_id"] = [];
        }
        if (!filterData["fk_product_category_id"].includes(value)) {
            filterData["fk_product_category_id"].push(value);
        }
    } else {
        if (filterData["fk_product_category_id"]) {
            filterData["fk_product_category_id"] = filterData["fk_product_category_id"].filter(function(v) { return v !== value; });
            if (filterData["fk_product_category_id"].length === 0) {
                delete filterData["fk_product_category_id"];
            }
        }
    }
    updateSQL();
});

ins(".-weight-select")._on("change", function(o) {
    var value = o._getValue();
    if (value) {
        filterData["weight"] = value;
    } else {
        delete filterData["weight"];
    }
    updateSQL();
});


ins(".-product-filter-btn")._on("click", (o) => {
    var sql = ins(".-sql-filter-input")._getValue()
    ins("generate_product_html")._ajax._app({ "sql": sql }, function(data) {
        ins(".-products-area")._setHTML(data);
    })

})

ins(".-product-reset-btn")._on("click", function() {
    // Reset filterData object
    filterData = {};

    // Reset input field for title
    ins(".-title-input")._setValue('');

    // Reset weight select field
    ins(".-weight-select")._setValue('');

    // Reset checkboxes (Category)
    ins(".-category-checkbox")._each(function(item) {
        item._get(0).checked = false; // Uncheck all checkboxes
    });

    // Reset type buttons (remove active styles)
    ins(".-type-btn")._each(function(button) {
        button._removeClass("ins-gold-bg", "ins-gold-color", "ins-active");
        button._addClass("ins-grey-color");
        button._setCSS({ border: "1px solid var(--grey-l)" });
    });
    ins("generate_product_html")._ajax._app({}, function(data) {
            ins(".-products-area")._setHTML(data);
        })
        // Reset filter SQL
    updateSQL();
});