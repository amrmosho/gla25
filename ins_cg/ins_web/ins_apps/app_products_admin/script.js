ins(".-save-and-next")._on("click", o => {
    ins(".crud-form-body")._data._submit(data => {
        ins()._ui._addLoader();
        ins("submit_setp_one")._ajax._app(data, r => {
            url = ins()._map._url({ "mode": "edit", "id": r })
            window.location = url
            ins()._ui._removeLoader();
        })
    })
}, true)

function files_update_value() {
    var vdata = [];
    ins(".files-input-row")._each(function(o, i) {
        o._data._submit((data) => {
            vdata.push(data)
        })
    })
    ins(".files-data-inpt")._setValue(JSON.stringify(vdata))
}
ins(".files-input-del")._on("click", o => {
    o._parents(".files-input-row")._remove();
    files_update_value()
}, true)
ins(".files-input-row select , .files-input-row input")._on("change", o => {
    setTimeout(o => {

        files_update_value();

    }, 100)
}, true)


ins(".files-input-row select.type")._on("change", o => {

    var p = o._parents(".files-input-row")
    p._data._submit((data) => {
        data["type"] = o._getValue();
        data["oname"] = data["name"];

        ins("_file_ui_row")._ajax._app(data, r => {
            p._setHTML(r)
        })

    })

}, true)

function f_m_actions(ds) {
    var data = ds;
    if (ds["p"] != "") {
        data.forEach(element => {
            if (element != "") {
                ins("_file_ui")._ajax._app(element, r => {
                    ins(ds["p"])._append(r);
                    files_update_value()
                })
            }
        });
    }
}

function _plg() {
    ins(".upload_files_btn")._on("click", (o) => {
        var options = {
            o: o,
            onend: function(ds) {
                f_m_actions(ds);
            },
            dir: o._getData("_dir"),
            exts: "zip",
            size: "300000",
            mode: 'multi',
            _p: "._files_parents",
        };
        ins("ins_plg_py_upload")._plgin(options,
            function(plg) {}
        );
    })
}
window.onload = function() {
    _plg();

    var mode = ins()._map._get()["mode"]

    if (mode == "edit") {
        var vs = ins(".files-data-inpt")._getValue();
        var vs = JSON.parse(vs);

        vs.forEach(element => {

            element["updatemode"] = "edit";

            ins("_file_ui")._ajax._app(element, r => {

                ins("._files_parents")._append(r);
                files_update_value()
            })
        });

    }

};