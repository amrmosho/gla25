function aj_search(get, data, ret) {
    data["get"] = get;
    ins("_call_search")._ajax._app(data, ret)
}
ins(".ins-form-bool-f")._on("change", o => {
    var page = ins(".ins-pagination-area")._getData("page");
    search(page);
}, "true");





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
            sdata["page"] = page;
            aj_search("_products_ui", sdata, data => {
                ins(".-products-area")._setHTML(data)
            })
        })
    }, 100)
}