ins(".-type-btn")._on("click", (o) => {
    ins(".-type-btn")._removeClass("ins-active");
    o._addClass("ins-active");
})

function _submit() {
    var v = ins(".-cal-update-nput")._getValue();

    if (v == "" || v == null || v == undefined || v == 0) {
        ins("Please enter a valid number")._ui._notification({ "class": "ins-danger" });
    } else {
        window.location = "/plan/" + v + "/";
    }


}

ins(".-cal-update-btn")._on("click", (o) => {
    _submit();
}, true)

ins(".-cal-update-nput")._on("keyup", (o, e) => {
    console.log(e.keyCode);
    if (e.keyCode == 13) {
        _submit();
    }
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