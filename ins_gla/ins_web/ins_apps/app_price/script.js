ins(".a-price-update-btn")._on("click", (o) => {
    update("update");
}, true);

ins(".a-price-report-btn")._on("click", (o) => {
    update("report");
}, true);




function update(st) {
    /*ins("operation_done_msg")._data._trans((text) => {
        ins(text)._ui._notification({ class: "ins-danger" })
    })*/
    ins(".a-price-cont")._data._submit((data) => {
        data["set"] = st;
        var url = ins()._map._url(data)
        window.location = url
    })

}