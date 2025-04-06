ins(".-home-ai-btn")._on("click", o => {

    ins("ai")._ajax._app(o._getData(), (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-bookmark-circle'></i> Chat with Insya",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:80%;    "
        });
    })

}, true)


ins(".-home-ai-send-btn")._on("click", o => {



    ins()._ui._addLoader()

    //  var u = ins()._map._url({ "insrender": "app", "id": ins(".-crud-list-ai-close-btn")._getData("id"), "mode": "curd_list_ai" })

    var v = ins(".-home-ai-txt")._getValue()
    ins("ai_call")._ajax._app({ "v": v }, (data) => {



        ins(".-home-ai-body")._setHTML(data);
        ins(".-home-ai-txt")._setValue("")
        ins()._ui._removeLoader()

        ins()._ui._update()
    })
}, true)


ins(".-sales-update-btn")._on("click", o => {

    var f = ins(".-sales-inpt-from")._getValue();
    var t = ins(".-sales-inpt-to")._getValue();
    var a = ins(".-sales-inpt-action")._getValue();

    if (f != "" && t != "") {
        var url = ins()._map._url({ "f": f, "t": t, "a": a });
        window.location = url
    }




}, true)