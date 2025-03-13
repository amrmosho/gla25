ins(".-add-new-time")._on("click", (o) => {
    ins("_add_new_item")._ajax._app({}, (data) => {
        ins(".-times-area")._append(data)
    })
}, true)



ins(".-remove-item")._on("click", (o) => {

    if (confirm("Are you sure you want to delete this item?")) {
        p = o._parents(".-times-row");
        ops = o._getData();
        ops.area = ins(".-times-textarea")._getValue();
        ins("_remove_item")._ajax._app(ops, (data) => {
            p._remove()
            ins(".-times-textarea")._setValue(data)

        })


    }

})

ins(".-from-time")._on("change", (o) => {

    update_data("", o)
})


ins(".-to-time")._on("change", (o) => {

    update_data("", o)
})



function update_data(type, o) {

    var p = o._parents(".-times-row")


    const uid = p._getData("uid");
    const textarea = ins(".-times-textarea");

    var from = p._find(".-from-time")._getValue();
    var to = p._find(".-to-time")._getValue();

    const data = {
        area: textarea._getValue() || "{}",
        uid: uid,
        from: from,
        to: to
    };
    ins("_update_times")._ajax._app(data, (response) => {
        try {
            const newData = JSON.parse(response);
            textarea._setValue(JSON.stringify(newData, null, 2));
        } catch (e) {
            const currentValue = textarea._getValue();
            try {
                JSON.parse(currentValue);
            } catch {
                textarea._setValue("{}");
            }
        }
    }, (error) => {
        console.error("Request failed:", error);
    });
}





ins(function() {

    var g = ins()._map._get();
    if (g["mode"] == "edit") {
        ins()._ui._addLoader()
        setTimeout(() => {
            ins("_fill_time_area")._ajax._app({}, (data) => {
                var jdata = JSON.parse(data)
                ins(".-times-area")._setHTML(jdata["ui"])
                ins(".-times-textarea")._setValue(jdata["textarea"])
                ins("_fill_messages")._ajax._app({}, (data) => {
                    var jdata = JSON.parse(data)
                    ins(".order_msg")._setValue(jdata["order_msg"])
                    ins(".order_msg_ar")._setValue(jdata["order_msg_ar"])
                })
                ins()._ui._removeLoader()
            })


        }, 1000);
    }

})._load()