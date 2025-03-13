ins(".-type-btn")._on("click", (o) => {
    ins(".-type-btn")._removeClass("ins-active");
    o._addClass("ins-active");
})

ins(".-add-cart-btn")._on("click", (o) => {

    var p = o._parents(".-plan-body")._find(".product-data-area");
    var pdata = {};
    p._each((e) => {
        e._data._submit((cdata) => {
            pdata[e._getData("mname")] = cdata;
        });
    });
    pdata = JSON.stringify(pdata)


    ins("_cart_lightbox_ui")._ajax._app({ "data": pdata }, (data) => {
        var jdata = JSON.parse(data)
        if (jdata["status"] == "0") {
            ins()._ui._addLightbox({
                "mode": "right_panel",
                title: "<i class='lni ins-icon lni-cart  '></i> " + o._getData("lbtitle"),
                data: jdata["ui"],
                data_style: "position: relative;top: 0;",
                style: "width:650px;    "
            });
        } else {
            ins(jdata["msg"])._ui._notification({ class: "ins-danger" })

        }

    })

})
ins(".-continue-shopping-btn")._on("click", (o) => {
    ins(".ins-panel-overlay.ins-opened")._remove()
    ins()._ui._removeLightbox();
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
            setTimeout(() => {
                if (jdata["count"] > 0) {
                    ins(".-cart-counter")._setHTML(jdata["count"])
                } else {
                    ins(".-cart-counter")._addClass("ins-hidden")

                }
            }, 100)
        })
    }
}, true)