ins(".-type-btn")._on("click", (o) => {
    ins(".-type-btn")._removeClass("ins-active");
    o._addClass("ins-active");
})

ins(".-cal-update-btn")._on("click", (o) => {
    var v = ins(".-cal-update-nput")._getValue();

    window.location = "/plan/" + v + "/";

}, true)


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
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-cart  '></i> Cart",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:650px;    "
        });
    })





})