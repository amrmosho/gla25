ins(".-order-btn")._on("click", function(o) {
    ins("_order_ui")._ajax._app(o._getData(), (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:70%;"
        });
    })

}, true)

ins(".-change-status")._on("click", function(o) {



    ins("_change_status_ui")._ajax._app(
        o._getData(), (data) => {
            ins()._ui._addLightbox({
                "mode": "right_panel",
                data: data,
                data_style: "position: relative;top: 0;",
                style: "width:650px;"
            });
        }, {}



    )




}, true)
ins(".ins-view-close")._on("click", function(o) {
    ins(".ins-panel-overlay")._remove()
    ins()._ui._removeLightbox();
}, true)

ins(".-save-status")._on("click", (o) => {
    ins("_update_statue")._ajax._app({ "value": ins("select.status")._getValue(), "oid": o._getData("tid") }, (data) => {

        window.location.reload()
    });

})