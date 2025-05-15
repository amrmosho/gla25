function aj_search(get, data, ret) {
    data["get"] = get;
    ins("_call_search")._ajax._app(data, ret)
}
ins(".ins-form-bool-f")._on("change", o => {
    var page = ins(".ins-pagination-area")._getData("page");
    search(page)
}, "true");


ins(".ins-pagination-btn-prev")._on("click", o => {
    var page = ins(".ins-pagination-area")._getData("page");
    if (page > 1) {
        page = page - 1;
        search(page);
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}, true)


ins(".ins-pagination-btn-next")._on("click", o => {
    var tpages = o._getData("tpages");
    var page = ins(".ins-pagination-area")._getData("page");
    if (page < tpages) {
        page = parseInt(page, 10) + 1;
        search(page);
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });

    }
}, true)

ins(".ins-pagination-btn")._on("click", o => {
    var page = o._getData("page");
    search(page);
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}, true)




ins(".-go-to-page-btn")._on("click", o => {
    var page = ins(".-page-input")._getValue();
    var thispage = ins(".ins-pagination-area")._getData("page");
    var tpages = o._getData("tpages");
    if (page > 0 && page <= tpages && page != thispage) {
        search(page);
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}, true)

function search(page) {
    setTimeout(o => {
        ins(".-list-filter-ui")._data._submit((data) => {


            
            var sdata = {}
            Object.keys(data).forEach((k, i) => {
                if (data[k] != "0" &&
                    data[k] != "-") {
                    sdata[k] = data[k];
                }
            })
            console.log(sdata)

            sdata["page"] = page;
            aj_search("_products_ui", sdata, data => {
                ins(".-products-area")._setHTML(data)
            })
        })
    }, 100)
}




ins(".-order-select")._on("click", (o) => {
    var page = ins(".-page-input")._getValue();

search(page)

})

ins(".-add-cart-btn")._on("click", (o) => {
    var ops = o._getData();
    ops.count = ins(".count-inpt")._getValue()
    ops["lang"] = "ar"
    ins("_add_to_card")._ajax._app(ops, (data) => {
        var jdata = JSON.parse(data)
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-cart  '></i> " + ops["lbtitle"],
            data: jdata["ui"],
            data_style: "position: relative;top: 0;",
            style: "width:650px;    "
        });


    })
})

ins(".-remove-item-side-cart-btn")._on("click", (o) => {
    var ops = o._getData()
    var p = o._parents(".-item-card");


    ins("remove_item_confirm")._data._trans((text) => {

        if (confirm(text)) {
            ins("_remove_item_cart")._ajax._app(ops, (data) => {
                var jdata = JSON.parse(data)
                ins(".-cart-cont")._setHTML(jdata["ui"])

                ins("item_removed")._data._trans((removed) => {
                    ins(removed)._ui._notification()
                })

            })
        }
    })

}, true)