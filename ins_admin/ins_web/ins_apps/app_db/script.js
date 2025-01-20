ins(".-db-sql-update-btn")._on("click", (o) => {
    var v = ins(".-db-sql-input")._getValue();
    if (v.trim() != "") {
        ins()._ui._addLoader()
        ins("_update_q")._ajax._app({ "q": v }, (data) => {
            if (data.trim() == "done") {
                ins("update..")._ui._notification({ "class": "ins-success" })

                window.location.reload()
            } else {
                ins(".db-res")._setHTML(data)
                ins("update..")._ui._notification({ "class": "ins-success" })

            }
            ins()._ui._removeLoader()

        })
    } else {

        alert("No query to run")
    }

}, true)




ins(".-db-reload-btn")._on("click", (o) => {
    window.location.reload()
}, true);


ins(".-db-s-del")._on("click", (o) => {
    if (confirm(o._getData("m"))) {
        ins("_del")._ajax._app(o._getData(), (data) => {
            ins(".db-res")._setHTML(data)
            ins("Data update..")._ui._notification({ "class": "ins-success" })

        })
    }
}, true)




ins(".db-get-q")._on("click", (o) => {
    ins("_q")._ajax._app(o._getData(), (data) => {
        ins(".-db-sql-input")._setValue(data);
        ins("Query Updated..")._ui._notification({ "class": "ins-success" })

    })
}, true)