ins("select.src_area")._on("change", (o) => {
    ins("get_src_data")._ajax._app({ "_v": o._getValue() }, function(data) {
        var jdata = JSON.parse(data);
        ins("select.type")._setHTML(jdata["type_ops"])

    })
})



ins("select.fk_menu_id")._on("change", (o) => {
    ins("_menu_data")._ajax._app({ "_v": o._getValue() }, function(data) {
        var jdata = JSON.parse(data);
        ins("select.fk_menu_item_id")._setHTML(jdata["type_ops"])

    })
})

ins("select.type")._on("change", (o) => {
    _get_pros();

})

function _menus() {
    if (ins("select.fk_menu_id")._getValue() != "") {
        ins("_menu_data")._ajax._app({ "_v": ins("select.fk_menu_id")._getData("value"), "_mid": ins("select.fk_menu_item_id")._getData("value") }, function(data) {
            ins("select.fk_menu_item_id")._setHTML(data)
        })

    }

}

function _get_pros(ondone = () => {}) {
    if (ins("select.type")._getValue() != "") {
        var url_data = ins()._map._get();
        ins("get_pros")._ajax._app({ "_mode": url_data["mode"], "_id": url_data["id"], "_myarea": ins("select.src_area")._getValue(), "_type": ins("select.type")._getValue() }, function(data) {
            ins(".-pros-area")._setHTML(data)
            ondone()
        })

    }
}




ins(function() {

    var url_data = ins()._map._get();
    if (url_data["mode"] == "edit") {

        ins("get_src_data")._ajax._app({ "_mode": url_data["mode"], "_id": url_data["id"], "_type": ins("select.type")._getData("value"), "_v": ins("select.src_area")._getData("value") }, function(data) {
            var jdata = JSON.parse(data);
            ins("select.type")._setHTML(jdata["type_ops"])

            _get_pros(() => {

                _menus();
            });


        })

    }


})._load()