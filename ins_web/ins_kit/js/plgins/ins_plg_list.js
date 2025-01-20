/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_list {
    options = {};
    _main = "";
    constructor(o) {
        this.options = o;
        this._main = ".ins_main." + this.options.o._getData("main");
    }
    _ajax(options, ondone, page = "pages/list") {
        var self = this;
        ins()._ajax._to(
            page,
            options,
            function(data) {
                ins(ondone)._isExists(function() {
                    ondone(data);
                });
                self._mian();
            }
        );
    }
    _mian() {
        if (ins(this.options.onUpdate)._isExists()) {
            this.options.onUpdate();
        }
        ins()._ajax._update_main(function() {
            ins()._ui._page_progress_hide();
        }, "", this._main);
    }
    _list_multi_update(mode, e) {
        var self = this;
        var ids = "";
        var table = ins()._data._page_data(self._main).table;
        var m = "";
        ins(".check_list_ids:checked")._each(function(e) {
            ids += m + e._getvalue();
            m = ",";
        });
        if (ids == "" && e._getData("no_ids_needs") == null) {
            alert("no items chosen");
        } else {
            var c = e._getData();
            c.mode = mode;
            c.ids = ids;
            c.table = table;
            ins()._ui._page_progress_run();
            if (ins(e._getData("c" + mode))._isExists()) {
                c.type = "call";
                window[e._getData("c" + mode)](ids, c);
            } else {
                if (ins(e._getData("b" + mode))._isExists()) {
                    c.type = "callbefor";
                    window[e._getData("b" + mode)](ids, c);
                }
                var options = e._getData();
                options.mode = mode;
                options.ids = ids;
                options.table = table;
                options = Object.assign({}, ins()._map._get_page_data(self._main), options);
                if (ins(e._getData("co" + mode))._isExists()) {
                    c.type = "condition";
                    if (window[e._getData("a" + mode)](ids, c)) {
                        self._ajax(options, function() {
                            if (ins(e._getData("a" + mode))._isExists()) {
                                c.type = "callafter";
                                window[e._getData("a" + mode)](ids, c);
                            }
                            if (e._hasdata("done_message")) {
                                ins()._ui._send_tiny_message(
                                    e._getData("done_message"),
                                    "ins-success",
                                    "lni  lni-checkmark"
                                );
                            } else {
                                ins()._ui._send_tiny_message();
                            }
                        })
                    }
                } else {
                    self._ajax(options, function() {
                        if (ins(e._getData("a" + mode))._isExists()) {
                            c.type = "callafter";
                            window[e._getData("a" + mode)](ids, c);
                        }
                        if (e._hasdata("done_message")) {
                            ins()._ui._send_tiny_message(
                                e._getData("done_message"),
                                "ins-success",
                                "lni  lni-checkmark"
                            );
                        } else {
                            ins()._ui._send_tiny_message();
                        }
                    });
                }
            }
        }
    }
    list_multi_update() {
        var self = this;
        ins(".list_multi_update")._on(
            "click",
            function(e) {
                var mode = e._getData("mode");
                if (ins(mode)._isEmpty()) {
                    mode = e._getparent()._getData("mode");
                }
                if (!ins(e._getData("jsconfirm"))._isEmpty()) {
                    if (confirm(e._getData("jsconfirm"))) {
                        self._list_multi_update(mode, e);
                    }
                } else {
                    self._list_multi_update(mode, e);
                }
            },
            true
        );
    }



    _updatefliter($this, get = false) {
        var f = "";
        var v = "";
        var se = false;
        ins(".ins-form-input.filter_item,.ins-form-input.ins-filter-item")._each(function(o) {
            if (o._getvalue() != "") {
                f += o._getattr("name") + "=" + o._getvalue() + ";";
                se = true;
            }
        });
        if ($this._hasclass("bt_item_search")) {
            f += $this._getData("filter_field") + "=" + $this._getData("filter_value") + ";";
            se = true;
        } else {
            if (!ins(ins(".filter_labels")._getData("act_label"))._isEmpty()) {
                f +=
                    "sys_labels=" + ins(".filter_labels")._getData("act_label") + ";";
                se = true;
            }
        }
        if (se) {
            var u = ins(".ins_filter_bar,.ins-filter-area")._getData("url").split("do/");


            if (ins(u[1])._isEmpty()) {

                u[1] = "";
            }
            if (get) {
                return u[0] + "do/filter/" + f + "/" + u[1];

            } else {

                window.location = u[0] + "do/filter/" + f + "/" + u[1];


            }
        }
    }


    _reset() {
        ins(".ins-form-input.filter_item,.ins-form-input.ins-filter-item")._each(function(o) {
            if (o._hasData("defult")) {
                console.log(o._get(0));
                o._setValue(o._getData("defult"))
            } else {
                o._setValue("");
            }
        });
    }

    _filter() {
        var self = this;
        ins(".ins-form-input.filter_item.oninput")._on("input", function(e) {
            self._updatefliter(e);
        });
        ins(".ins-form-input.filter_item")._on(
            "keyup",
            function(o, e) {
                if (e.keyCode == 13) {
                    self._updatefliter(o);
                }
            }
        );


        ins(".ins_reset_btn")._on("click", function(e) {
            self._reset(e);
        }, true);

        ins(".ins_filter_btn,.ins-filter-btn")._on("click", function(e) {
            self._updatefliter(e);
        }, true);
        ins(".bt_item_search")._on("click", function(e) {
            self._updatefliter(e);
        });





        ins(".ins-filter-template-del-btn")._on(
            "click",
            function(o) {
                ins()._ajax._to("eng/list/filter", o._getData(), function(data) {
                    ins(".ins-filter-templates-area")._setHtml(data);
                    o._parents(".ins-tr")._remove();
                });
            }, true);


        ins(".ins-filter-template-update")._on(
            "click",
            function(o) {

                var ops = o._getData();
                ops["temp_title"] = o._parents(".ins-tr")._find("input.temp_title")._getValue()

                ins()._ajax._to("eng/list/filter", ops, function(data) {
                    ins(".ins-filter-templates-area")._setHtml(data);


                });
            }, true);







        ins(".ins-filter-template-add-btn")._on(
            "click",
            function(o) {
                var c = self._updatefliter(o, true);


                ins()._ajax._to("eng/list/filter", { "status": "_add_ui", "data": c, "type": o._getData("type") }, function(data) {
                    ins()._ui._addLightbox({
                        title: "Add new filter Template",
                        data: data,
                        data_style: "position: relative;top: 0;",
                        style: "height: auto;width:600px;    "
                    });
                });
            }, true);

        ins(".ins-filter-template-save-btn ")._on(
            "click",
            function(o) {
                ins(".ins-lightbox-body")._data._submit(function(dbdata) {
                    dbdata["status"] = "_add_save"
                    ins()._ajax._to("eng/list/filter", dbdata, function(data) {

                        ins(".ins-filter-templates-area")._setHtml(data);

                        ins()._ui._removeLightbox();

                    });

                })
            }, true);




        ins(".ins-filter-template-mage-btn")._on(
            "click",
            function(o) {
                var c = self._updatefliter(o, true);


                ins()._ajax._to("eng/list/filter", { "status": "_mange_ui", "data": c, "type": o._getData("type") }, function(data) {
                    ins()._ui._addLightbox({
                        title: "Manage filters",
                        data: data,
                        data_style: "position: relative;top: 0;",
                        style: "height: auto;width:600px;    "
                    });
                });
            }, true);





    }
    _test() {
        ins(".ins_pages_select")._on("change", function(e) {
            window.location = ins()._data._addtourl(
                e._getData("url"),
                "/page/" + e._getvalue() + "/"
            );
        });
        ins(".list_limit_option")._on("change", function(o) {
            var val = "12";
            if (o._getvalue() != "") {
                val = o._getvalue();
            }
            ins()._data._set_session(o._getData("jsname"), val, function() {
                window.location.reload();
            });
        });
    }
    _actions() {




        ins(".ins-editable-update-btn")._on("click", function(o) {

            ins(".ins-editable-area")._data._submit(function(dbdata) {
                ins(`.ed_${dbdata["ed_name"]}_${dbdata["ed_id"]}`)._ui._addloader();

                dbdata["ajstatus"] = "update";
                ins()._ajax._to("eng/get_input", dbdata, function(data) {
                    ins(`.ed_${dbdata["ed_name"]}_${dbdata["ed_id"]}`)._setHtml(data.trim());
                    ins()._ui._send_tiny_message();
                    ins()._ui._removeLightbox();

                    ins(`.ed_${dbdata["ed_name"]}_${dbdata["ed_id"]}`)._ui._removeloader();

                });

            })

        });




        ins(".ins-editable-btn")._on("click", function(o) {
            ins()._ajax._to("eng/get_input", o._getData(), function(data) {
                ins()._ui._ins_lightbox({
                    title: o._getData("ed_lb_title"),
                    data: data,
                    data_style: "position: relative;top: 0;",
                    style: "height: auto;width:600px;    "
                });
            });
        });




        ins()._map._setKey("export_all", (k) => {
            var href = ins(".list-action-menue-btn.list-export-all-btn")._getAttribute("href");
            window.open(href, "_blank");
        });
        ins()._map._setKey("export", (k) => {
            var href = ins(".list-action-menue-btn.list-export-btn")._getAttribute("href");
            window.open(href, "_blank");
        });
        ins()._map._setKey("trash", (k) => {
            var href = ins(".list-action-menue-btn.list-trash-btn")._getAttribute("href");
            window.open(href, "_blank");
        });
        ins()._map._setKey("settings", (k) => {
            var href = ins(".list-action-menue-btn.list-settings-btn")._getAttribute("href");
            window.open(href, "_blank");
        });
        ins()._map._setKey("print", (k) => {
            window.print();
        });
        ins()._map._setKey("print", (k) => {
            window.print();
        });
        ins()._map._setKey("add", (k) => {
            ins()._ui._send_tiny_message("Go to add...")
            window.location.href = ins()._map._url({ "mode": "add" })
        });

        ins()._map._setKey("copy", (k) => {
            ins()._ui._send_tiny_message("Copy...");
            var e = ins("._list_copy_btn")
            var mode = e._getData("mode");
            self._list_multi_update(mode, e);
        });
        ins()._map._setKey("delete", (k) => {
            ins()._ui._send_tiny_message("Delete...", "ins-danger");
            var e = ins(".list_delete_btn")
            var mode = e._getData("mode");
            if (confirm(e._getData("jsconfirm"))) {
                self._list_multi_update(mode, e);
            }
        });
        var self = this;

        ins("input.all_rows_select")._on("change", function(o) {
            if (ins(o)._get(0).checked) {
                ins(".check_list_ids")._setattr("checked", true);
            } else {
                ins(".check_list_ids")._removeattr("checked");
            }
        });


        ins(".list_status_update")._on(
            "click",
            function(e) {
                var mode = e._getData("mode");
                var ids = "";
                if (!ins(e._getData("jsconfirm"))._isEmpty()) {
                    if (confirm(e._getData("jsconfirm"))) {
                        if (!ins(e._getData("ids"))._isEmpty()) {
                            ids = e._getData("ids");
                        }
                        var table = ins()._data._page_data(self._main).table;
                        ins()._ui._page_progress_run();
                        options = e._getData();
                        options.mode = mode;
                        options.ids = ids;
                        options.table = table;
                        options = Object.assign({}, ins()._map._get_page_data(self._main), options);
                        self._ajax(options, function() {
                            if (e._hasdata("done_message")) {
                                ins()._ui._send_tiny_message(
                                    e._getData("done_message"),
                                    "ins-success",
                                    "lni  lni-checkmark"
                                );
                            } else {
                                ins()._ui._send_tiny_message();
                            }
                        });
                        /*  return ins()._ajax._send(
                              "pages/list",
                              options,
                              "POST",
                              function() {
                                  self._mian();
                              }
                          );*/
                    }
                } else {
                    if (!ins(e._getData("ids"))._isEmpty()) {
                        ids = e._getData("ids");
                    }
                    console.log(mode);
                    var table = ins()._data._page_data(self._main).table;
                    var options = {
                        mode: mode,
                        ids: ids,
                        table: table,
                    };
                    self._ajax(options);
                    /*
                                        return ins()._ajax._to("pages/list", options, function() {
                                            self._mian();
                                        });*/
                }
            },
            true
        );
        ins(".ins-list-show-lightdata")._on("click", function(o) {
            var options = o._getData();
            ins()._ajax._to("db/get_value", options, function(d) {
                ins()._ui._ins_lightbox({
                    title: options["title"],
                    data: d,
                    data_style: "    position: relative;top: 0;",
                    style: "    height: auto;width:600px;    "
                });
            });
        });
        ins(".ins-form-bool-f")._on(
            "change",
            function(o) {
                var c = o._get(0);
                var e = o._parent()._find(".ins-form-input");
                if (c.checked) {
                    e._setvalue("1");
                } else {
                    e._setvalue("0");
                }
                if (e._getData("insaction") == "ins_data_update") {
                    var op = {
                        get_file: "db/update",
                        table: e._getData("type"),
                        id: e._getData("id"),
                        field: e._getData("name"),
                        value: e._getvalue(),
                    };
                    ins()._ui._page_progress_run();
                    ins()._ajax._send("/ins_ajax.php", op, null, function() {
                        ins()._ui._page_progress_hide();
                        ins()._ui._send_tiny_message();
                    });
                }
            },
            true
        );
    }
    _history() {
        ins(".sys_history_show_hide_data")._on(
            "click",
            function(t) {
                ins("." + t._getData("sys_history_data"))._toggle_class(
                    "sys_history_data_show"
                );
            },
            true
        );
        ins(".ins-view-mode-close")._on(
            "click",
            function(t) {
                ins(".ins-view-mode-data")._sethtml("");
                var updateurl = ins()._map._url({}, "id", "list_mode");
                window.history.pushState('page2', 'Title', updateurl);
                ins(".ins-table-data-area")._removeclass("ins-view-mode");
                ins(" .ins-tr")._removeclass("ins-active");
            }, true)





        ins(".ins-filter-bar-close-btn")._on("click", function(t) {
            ins(".ins_filter_area")._removeClass("ins-opened");
            ins("body")._removeClass("ins-filter-opend")


        })




        ins(".ins-filter-bar-btn")._on("click", function(t) {



            if (ins("body")._hasClass("ins-filter-opend")) {
                ins("body")._removeClass("ins-filter-opend")

                ins(".ins_filter_area")._removeClass("ins-opened");


            } else {

                ins("body")._addClass("ins-filter-opend")
                ins(".ins_filter_area")._addClass("ins-opened");

            }



        }, true);


        ins(".ins-create-view-mode-btn")._on("click", function(t) {
            ins(".ins-create-view-mode-btn")._removeclass("ins-active");
            ins(t)._addclass("ins-active");
            ins(".ins-table-data-area")._addclass("ins-view-mode");
            ins(".ins-view-mode-data")._ui._addloader();
            ins()._ajax._load(t._getData("url"), t._getData(), function(d) {
                ins(".ins-view-mode-data")._setdata("url", t._getData("url"));
                ins(".ins-view-mode-data")._sethtml(d);
                ins()._ui._removeloader();
            });
        }, true);
        ins(".ins-view-mode-btn")._on(
            "dblclick",
            function(t) {
                var g = ins()._map._get();
                ins(".ins-view-mode .ins-tr")._removeclass("ins-active");
                t._parent()._addclass("ins-active");
                var id = t._find("span")._getData("id");
                ins(".ins-table-data-area")._addclass("ins-view-mode");
                var updateurl = ins()._map._url({ "id": id, "mode": "list", "list_mode": "view" });
                window.history.pushState('page2', 'Title', updateurl);
                ins(".ins-view-mode-data")._ui._addloader();
                var url = ins()._map._url({ "id": id, "mode": "view", "list_mode": "view" });
                ins()._ajax._load(url, t._getData(), function(d) {
                    console.log(d);
                    ins(".ins-view-mode-data")._sethtml(d);
                    ins()._ui._removeloader();
                });
            },
            true
        );

        ins(".ins-submit-ajax-btn")._on(
            "click",
            function(o) {


                ins()._ui._removeLightbox();

                var name = o._getData("myname");
                var mypath = o._getData("mypath");
                var submit_area = o._getData("submit_area");
                var get = o._getData("get");
                var callback = o._getData("callback");
                var options = o._getData();

                delete options["callback"];

                delete options["myname"];
                delete options["mypath"];
                delete options["submit_area"];
                delete options["get"];


                ins(submit_area)._data._submit((data) => {


                    ins(get)._ajax._class(
                        data,
                        function(data) {



                            ins()._ui._send_tiny_message(
                                data,
                                "ins-success",
                                "lni  lni-checkmark"
                            );

                            if (callback == "close") {


                                ins()._ui._removeLightbox()
                            }
                        }, {
                            _lang: ins("body")._getData("lang"),
                            _myname: name,
                            _mypath: mypath,
                        });

                });
            }, true);




        ins(".ins-light-ajax_btn")._on(
            "click",
            function(o) {

                ins()._ui._removeLightbox();

                var name = o._getData("myname");
                var mypath = o._getData("mypath");


                var lbtitle = o._getData("lbtitle");
                var lbstyle = o._getData("lbstyle");
                var get = o._getData("get");

                var options = o._getData();

                delete options["myname"];
                delete options["mypath"];
                delete options["lbtitle"];
                delete options["lbstyle"];
                delete options["get"];



                ins(get)._ajax._class(
                    options,
                    function(data) {
                        ins()._ui._removeLightbox();
                        ins()._ui._lightbox(lbtitle, data, null, lbstyle);
                    }, {
                        _lang: ins("body")._getData("lang"),
                        _myname: name,
                        _mypath: mypath,
                    });




            }, true);




        ins(".list_get_history")._on(
            "click",
            function(t) {
                var options = t._getData();
                options.root = "true";
                options.get_file = "/ins_ajax/db/sys_history";
                return ins()._ajax._send("/ins_ajax.php", options, function(data) {
                    ins()._ui._lightbox("History", data, null, "width:650px;height:80%");
                });
            },
            true
        );
    }
    g = {};
    _onload() {
        console.log(this.g);
        //  ins(".ins-view-mode .ins-tr")._addclass("ins-light");
    }



    _settigns
    _out() {

        this.g = ins()._map._get();
        this._test();
        this._filter();

        this._history();
        this.list_multi_update();
        this._actions();
    }
}