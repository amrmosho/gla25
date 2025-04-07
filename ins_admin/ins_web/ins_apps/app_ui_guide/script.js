ins(".-ui-show-info")._on("click", (o) => {
    var p = o._parent()._find(".-ui-info-data");
    ins()._ui._addLightbox({
        "mode": "right_panel",
        title: "<i class='lni ins-icon lni-gear-1  '></i> info",
        data: "<div class='code'>" +
            p._getHtml() + "</div>",
        data_style: "position: relative;top: 0;",
        style: "width:600px;    "

    });

}, true)