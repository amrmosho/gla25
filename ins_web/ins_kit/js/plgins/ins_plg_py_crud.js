/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_crud {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _update_list_body() {
        var u = ins()._map._url({ "insrender": "app", "mode": "curd_list_body" })
        ins()._ajax._send(u, {}, (data) => {
            ins(".app-crud-body")._setHTML(data);
        })
    }
    _update_slector() {
        var l = ins(".ins-tr.active")._get().length;
        if (l > 0) {
            ins(".app-crud-list-status-bar .-status-bar-select-info")._setHTML("<span style='    font-weight: 500;' class='ins-font-s'>" + l + " Selected  <a class='ins-raw-selector-unseelect'> Unselect</a></span> ")
        } else {
            ins(".app-crud-list-status-bar .-status-bar-select-info")._setHTML(" ")
        }
    }
    _search() {
        var t = this;
        ins(".app-crud-list-search-btn")._on("click", (o) => {
            ins(".-crud-list-filter-panel")._addClass("ins-opened");
        }, true)
        ins(".-crud-list-filter-close-btn")._on("click", (o) => {
            ins(".-crud-list-filter-panel")._removeClass("ins-opened");
        }, true)
        ins(".-crud-list-filter-update-btn")._on("click", (o) => {
            t.updat_search();
        })
        ins(".-crud-list-search-txt")._on("keydown", function(o, e) {
            if (e.keyCode == 13) {
                ins(".filter-item-" + o._getData("to"))._setValue(o._getValue())
                t.updat_search();
            }
        }, true)
    }
    updat_search() {
        ins(".-crud-list-filter-area")._data._submit(function(data) {
            var f = "";
            Object.keys(data).forEach(function(k) {
                f += k + "=" + data[k] + ";";
            })
            var u = ins()._map._url({ "f": f })
            window.location = u;
        })
    }
    _name() {
        return ins(".app-crud-body")._getData("cname")
    }
    _pags() {
        var n = this._name()
        ins(".app-crud-list-page-slct")._on("change", (inp) => {
            var u = ins()._map._url({ "page": inp._getValue() })
            window.location = u
        }, true)
        ins(".app-crud-list-page-count-slct")._on("change", (inp) => {
            ins("users/set_settings")._plg({ "name": n, "pg_count": inp._getValue() }, (a) => {
                window.location.reload()
            });
        }, true)
    }

    _actions() {
        this._search();
        this._pags();
        ins(".ins-raw-selector-unseelect")._on("click", (o) => {
            ins(".ins-tr")._removeClass("active")
            ins(".app-crud-list-status-bar .-status-bar-select-info")._setHTML(" ")
        })
        ins(".ins-raw-selector-all")._on("click", (o) => {
            var tr = o._parents(".ins-table-data")._find(".ins-tr");
            if (o._hasClass("active")) {
                o._removeClass("active");
                tr._removeClass("active");
            } else {
                o._addClass("active")
                tr._addClass("active");
            }
            this._update_slector();
        })
        ins(".ins-raw-selector")._on("click", (o) => {
            var p = o._parents(".ins-tr");
            if (p._hasClass("active")) {
                p._removeClass("active")
            } else {
                p._addClass("active")
            }
            this._update_slector();
        })
        ins(".app-crud-list-copy")._on("click", (o) => {
            var u = ins()._map._url({ "insrender": "app", "id": o._getData("id"), "mode": "curd_list_copy" })
            console.log(u);
            ins()._ajax._send(u, {}, (data) => {
                ins(".app-crud-body")._setHTML(data);
                ins(o._getData("cm"))._ui._notification()
            })
        }, true)
        ins(".app-crud-list-mcopy")._on("click", (o) => {
            var ls = ins(".ins-tr.active .ins-raw-selector")._get();
            if (ls.length > 0) {
                var sp = "";
                var ids = "";
                ls.forEach(element => {
                    ids += sp + ins(element)._getData("id");
                    sp = ",";
                });
                var u = ins()._map._url({ "insrender": "app", "id": ids, "mode": "curd_list_copy" })
                ins()._ajax._send(u, {}, (data) => {
                    ins(".app-crud-body")._setHTML(data);
                    ins(o._getData("cm"))._ui._notification()
                })
                o._parents(".ins-menu")._removeClass("ins-act")
            }
        }, true)



        function ids() {
            var ids = ""
            var ls = ins(".ins-tr.active .ins-raw-selector")._get();
            if (ls.length > 0) {
                var sp = "";
                var ids = "";
                ls.forEach(element => {
                    ids += sp + ins(element)._getData("id");
                    sp = ",";
                });

                return ids;
            }
            return ""

        }



        ins(".app-crud-list-mdelete")._on("click", (o) => {
            if (ids() != "") {
                if (confirm(o._getData("cm"))) {
                    var u = ins()._map._url({ "insrender": "app", "ids": ids(), "mode": "curd_list_delete" })
                    ins()._ajax._send(u, {}, (data) => {
                        ins(".app-crud-body")._setHTML(data);
                        ins(o._getData("dm"))._ui._notification()
                    })
                    o._parents(".ins-menu")._removeClass("ins-act")
                }
            }
        }, true);





        ins(".app-crud-trash-res")._on("click", (o) => {
            if (ids() != "") {

                var u = ins()._map._url({ "insrender": "app", "ids": ids(), "mode": "trash", "id": "curd_trash_res" })
                ins()._ajax._send(u, {}, (data) => {
                    ins(".app-crud-body")._setHTML(data);
                    ins(o._getData("dm"))._ui._notification()
                })
                o._parents(".ins-menu")._removeClass("ins-act")

            }
        }, true);


        ins(".app-crud-trash-remove")._on("click", (o) => {
            if (ids() != "") {

                var u = ins()._map._url({ "insrender": "app", "ids": ids(), "id": "curd_trash_remove" })
                ins()._ajax._send(u, {}, (data) => {
                    ins(".app-crud-body")._setHTML(data);
                    ins(o._getData("dm"))._ui._notification()
                })
                o._parents(".ins-menu")._removeClass("ins-act")

            }
        }, true);


        ins(".app-crud-trash-resall")._on("click", (o) => {
            var u = ins()._map._url({ "insrender": "app", "id": "curd_trash_resall" })
            ins()._ajax._send(u, {}, (data) => {
                ins(".app-crud-body")._setHTML(data);
                ins(o._getData("dm"))._ui._notification()
            })
            o._parents(".ins-menu")._removeClass("ins-act")
        }, true);



        ins(".app-crud-trash-clear")._on("click", (o) => {
            var u = ins()._map._url({ "insrender": "app", "id": "curd_trash_clear" })
            ins()._ajax._send(u, {}, (data) => {
                ins(".app-crud-body")._setHTML(data);
                ins(o._getData("dm"))._ui._notification()
            })
            o._parents(".ins-menu")._removeClass("ins-act")
        }, true);







        ins(".app-crud-list-delete")._on("click", (o) => {
            if (confirm(o._getData("cm"))) {
                var u = ins()._map._url({ "insrender": "app", "ids": o._getData("id"), "mode": "curd_list_delete" })
                ins()._ajax._send(u, {}, (data) => {
                    ins(".app-crud-body")._setHTML(data);
                    ins(o._getData("dm"))._ui._notification()
                })
            }
        })
    }


    _form() {

        ins(".crud-form-submit-back")._on("click", (inp) => {

            ins(".crud-form-body")._data._submit(() => {
                ins(inp)._ui._addButtonLoader()
                inp._get(0).disabled = true;
                ins(".crud-form-body")._append("<input type='text' value='_tobak' name='reaction'  />")
                var form = ins(".crud-form-body")._get(0);
                form.submit();
            }, () => {
                ins("Please ensure that all required fields are filled out before submitting.! ")._ui._notification({ "class": "ins-danger" })
            });
        }, true)

        ins(".crud-form-submit")._on("click", (inp) => {

            ins(".crud-form-body")._data._submit(() => {
                ins(inp)._ui._addButtonLoader()
                inp._get(0).disabled = true;
                var form = ins(".crud-form-body")._get(0);
                form.submit();
            }, () => {
                ins("Please ensure that all required fields are filled out before submitting.! ")._ui._notification({ "class": "ins-danger" })
            });
        }, true)
        ins(".crud-form-reset")._on("click", (inp) => {
            var form = ins(".crud-form-body")._get(0);
            form.reset();
        }, true)
    }

    _lang() {


        ins(".ui-input-lang-update")._on("click", function(o) {


            ins(".ui-input-lang-area")._data._submit(function(data) {

                ins("ajx_input/lang_update")._ajax._ins_ajax(data, (data) => {
                    ins()._ui._removeLightPanel()

                    ins("langs updates")._ui._notification()

                })
            })

        }, true)


        ins(".ui-input-lang-ui")._on("click", function(o) {
            ins("ajx_input/lang_ui")._ajax._ins_ajax(o._getData(), (data) => {
                ins()._ui._addLightbox({
                    "mode": "right_panel",
                    title: "<i class='lni ins-icon lni-bookmark-circle'></i> Update Custom Permission",
                    data: data,
                    data_style: "position: relative;top: 0;",
                    style: "width:600px;    "
                });
            })

        }, true)

    }


    _tags() {





        ins(".ch-tag-search-inp")._on("keyup", function(o) {
            var w = o._getValue();

            if (w == "") {

                ins(".ch-tag-item-cont")._removeClass("ins-hidden")


            } else {

                ins(".ch-tag-item-cont")._addClass("ins-hidden")

                ins(".ch-tag-item-cont .ins-col-grow")._each((t) => {
                    var text = t._getText()


                    if (text.toLowerCase().search(w.toLowerCase()) != -1) {
                        t._parents(".ch-tag-item-cont")._removeClass("ins-hidden")
                    }
                })
            }


        }, true)




        ins(".ch-tag-item-save")._on("click", function(o) {
            ins(".ch-tag-item-add-area")._data._submit(function(data) {
                ins("ajx_tags/save")._ajax._ins_ajax(data, (data) => {
                    ins(".ins-fixpanel-right .ins-data  ")._setHTML(data);
                })
            })

        }, true)

        ins(".app-crud-list-name-slc")._on("change", function(o) {
            var u = ins()._map._url({ "inscl": o._getValue() }, "mode")
            window.location = u;



        }, true)


        ins(".ch-tag-item-back")._on("click", function(o) {
            ins("ajx_tags/ui")._ajax._ins_ajax(o._getData(), (data) => {
                ins(".ins-fixpanel-right .ins-data  ")._setHTML(data);
            })


        }, true)



        ins(".ch-tag-item-add")._on("click", function(o) {
            ins("ajx_tags/add")._ajax._ins_ajax(o._getData(), (data) => {
                ins(".ins-fixpanel-right .ins-data  ")._setHTML(data);
            })


        }, true)


        ins(".ch-tag-item-remove")._on("click", function(o) {
            if (confirm("Are you sure you won't delete this tag?")) {
                ins("ajx_tags/remove")._ajax._ins_ajax(o._getData(), (data) => {
                    ins(".ins-fixpanel-right .ins-data  ")._setHTML(data);
                })

            }
        }, true)
        ins(".app-crud-list-remove-tag")._on("click", function(o) {
            var op = o._getData();
            op["st"] = "0";
            ins("ajx_tags/update")._ajax._ins_ajax(op, (data) => {
                var mclass = "._" + op["obj"] + "_" + op["oid"] + "_tags"
                ins(mclass)._setHTML(data);
            })

        }, true)



        ins(".ch-tag-item")._on("change", function(o) {
            var op = o._getData();

            if (o._isChecked()) {
                op["st"] = "1";
            } else {;
                op["st"] = "0";
            }

            ins("ajx_tags/update")._ajax._ins_ajax(op, (data) => {

                var mclass = "._" + op["obj"] + "_" + op["oid"] + "_tags"


                ins(mclass)._setHTML(data);
            })

        }, true)

        ins(".app-crud-list-add-tag")._on("click", function(o) {

            ins("ajx_tags/ui")._ajax._ins_ajax(o._getData(), (data) => {

                ins()._ui._addLightbox({
                    "mode": "right_panel",
                    title: "<i class='lni ins-icon lni-bookmark-circle'></i> Update Custom Permission",
                    data: data,
                    data_style: "position: relative;top: 0;",
                    style: "width:600px;    "
                });
            })

        }, true)


    }

    _out() {

        this._lang()

        this._form()
        this._actions();
        this._tags();
    }
}