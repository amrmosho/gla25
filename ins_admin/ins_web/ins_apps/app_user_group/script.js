ins(function() {
    custom(() => {
        update_apps();
    })
})._load()


ins(".-ug-apps-per-reload-btn")._on("click", (o) => {
    update_apps()
})




function _apps_call(m, ops, ondone) {
    ops["c"] = m
    ins("_apps_call")._ajax._app(ops, ondone);
}

function update_apps() {
    _apps_call("_get_apps_per", ins(".-ug-apps-per-reload-btn")._getData(), (data) => {
        ins(".-ug-apps-per")._setHTML(data)
    })
}





ins("select.menu")._on("change", (o) => {

    _apps_call("_get_apps_get_apps", { "_v": ins("select.menu")._getValue() }, (data) => {
        ins("select.app")._setHTML(data);
    })
}, true)







ins(".-apps-per-ui-add-btn")._on("click", (o) => {
    ins(".-apps-per-ui-cont")._data._submit((cdata) => {
        _apps_call("_get_apps_per_update", cdata, (data) => {
            ins()._ui._removeLightbox();
            ins(".-ug-apps-per")._setHTML(data);

        })

    })
}, true)



ins(".-ug-apps-per-add-btn")._on("click", (o) => {
    _apps_call("_get_apps_per_ui", o._getData(), (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-gear-1  '></i> Add App Permission",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:600px;    "
        });
    })

})
ins(".-app-per-item-delete")._on("click", (o) => {
    _apps_call("_get_apps_per_delete", o._getData(), (data) => {
        ins(".-ug-apps-per")._setHTML(data);
    })
}, true)





ins(".-app-per-item-edit")._on("click", (o) => {
    _apps_call("_get_apps_per_edit_ui", o._getData(), (data) => {

        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-gear-1  '></i> Update Apps Permission",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:600px;    "

        });
    })
}, true)

////////////////////////////////////////////////////////////////////////////

function _custom_call(m, ops, ondone) {
    ops["c"] = m
    ins("_custom_call")._ajax._app(ops, ondone);
}


function custom(ondone = () => {}) {
    _custom_call("_get_custom_per", ins(".-ug-custom-per-reload-btn")._getData(), (data) => {
        ins(".-ug-custom-per")._setHTML(data);
        ondone()
    })
}



ins(".-custom-per-item-delete")._on("click", (o) => {
    _custom_call("_get_custom_per_delete", o._getData(), (data) => {
        ins(".-ug-custom-per")._setHTML(data);
    })
}, true)


ins(".-custom-per-item-edit")._on("click", (o) => {
    _custom_call("_get_custom_per_edit_ui", o._getData(), (data) => {

        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-gear-1  '></i> Update Custom Permission",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:600px;    "
        });
    })
}, true)



ins(".-custom-per-ui-add-btn")._on("click", (o) => {
    ins(".-custom-per-ui-cont")._data._submit((cdata) => {
        _custom_call("_get_custom_per_update", cdata, (data) => {
            ins()._ui._removeLightbox();
            ins(".-ug-custom-per")._setHTML(data);

        })

    })
}, true)


ins(".-ug-custom-per-reload-btn")._on("click", (o) => {
    custom()
})

ins(".-ug-custom-per-add-btn")._on("click", (o) => {


    _custom_call("_get_custom_per_ui", o._getData(), (data) => {
        ins()._ui._addLightbox({
            "mode": "right_panel",
            title: "<i class='lni ins-icon lni-gear-1  '></i> Add Custom Permission",
            data: data,
            data_style: "position: relative;top: 0;",
            style: "width:600px;    "
        });
    })

})