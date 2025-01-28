ins(".-show-subtypes-btn")._on("click", function(o) {
    ins("_subtypes_ui")._ajax._app(o._getData(), (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:650px;"
        });
    })

}, true)
ins(".ins-view-close")._on("click", function(o) {
    ins(".ins-panel-overlay")._remove()
    ins()._ui._removeLightbox();
}, true)