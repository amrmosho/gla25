export class ins_plg_listauto {
    options = {};
    _list = null;
    _me = null;
    constructor(o) {
        this.options = o;
        this._me = this.options.o;
        this.options.multiaple = false;
    }
    _name = "";


    updateValue(s, v) {

        var o = ins(s);

        var self = this;

        o._setvalue(v);

        var obj = o._find(
            'option[value="' + o._getvalue() + '"]');


        var view = obj._getData("view");
        if (ins(view)._isEmpty()) {
            view = obj._gettext();
        }

        if (!ins(view)._isEmpty()) {
            self._updateString(view, function(s) {
                o._parent()._find(".ins_au_keys_area")._sethtml(s);
            })
        }


        /*  c._update();
          c._get("select")._setvalue(v);
          c._updateitem();*/
    }




    _updateString(s, ondone) {
        ins("ins_plg_markdown")._plgin({
            string: s,
            format: function(data) {
                ondone(data);
            },
        }, );
    }

    _updateName(me) {

        this._name = me._parents(".ins_autocomplete_container")._getData("id");

    }
    _get(name) {
        return ins("." + this._name)._find(name)
    }


    _isMultiaple() {
        return (!ins(this._get("select")._getattr("multiple"))._isEmpty());
    }






    _updateItems(filter = "") {
        var self = this;

        try {
            this._get(".ins_autocomplete_list")._remove();
        } catch (err) {}
        var ul = ins()._ui._create("ul", "", {
            class: "ins_autocomplete_list  ",
        });
        this._get(".ins_autocomplete_data_list")._append(ul);
        var options = this._me._p("options");
        Object.keys(options).forEach(function(k) {
            var kn = ins(options[k]);
            var text = kn._gettext();
            if (text.toLowerCase().search(filter.toLowerCase()) > -1 || filter == "") {
                var disclass = "";
                if (options[k].selected === true) {
                    disclass = "ins_disabled";
                }
                self._updateString(text, function(text) {
                    var view = kn._getData("view");
                    if (ins(view)._isEmpty()) {
                        view = text;
                    }
                    var li = ins()._ui._create("li", "" + text, {
                        "data-value": kn._getattr("value"),
                        "data-view": view,
                        class: "ins_autocomplete_item " + disclass,
                    });
                    ins(ul)._append(li);
                    ins(li)._on("click", function(obj, e) {

                        if (!obj._hasclass(disclass)) {
                            self._updateName(obj);
                            if (self._isMultiaple()) {
                                self._get('option[value="' + obj._getData("value") + '"]')._p("selected", true);
                            } else {

                                self._get("select")._setvalue(obj._getData("value"));


                            }
                            if (!ins(self._get("select")._getData("onchange"))._isEmpty()) {
                                window[self._get("select")._getData("onchange")](self._get("select"), obj._getData("value"));
                            }
                            self._updateValue();
                            self._close(obj, e);
                        }
                    }, true);
                })
            }
        })
    }


    _open(o, e, cls = "") {



        ins(".ins_autocomplete_all")._removeclass("ins_opend", "ins-list-fix");
        ins(".all_input_area")._removeclass("ins_highlight_area");



        var self = this;
        e.preventDefault();
        self._updateItems();

        this._get(".ins_autocomplete_all")._addclass("ins_opend");
        if (cls != "") {
            this._get(".ins_autocomplete_all")._addclass(cls);
        }
        this._get(".all_input_area")._addclass("ins_highlight_area");
        this._get("input")._setvalue("");
        this._get("input")._get(0).focus();

    }


    _close() {


        this._get(".ins_autocomplete_list")._remove();
        this._get(".ins_autocomplete_all")._removeclass("ins_opend", "ins-list-fix");
        this._get(".all_input_area")._removeclass("ins_highlight_area");
    }

    _updateitems() {

        var self = this;
        var th = ins()._ui;



        var options = self._get("select")._p("options");

        self._get(".ins_au_keys_area")._sethtml("");
        Object.keys(options).forEach(function(k) {
            if (options[k].selected === true) {


                var obj = ins(options[k]);



                var view = obj._getData("view");
                if (ins(view)._isEmpty()) {
                    view = obj._gettext();
                }
                if (!ins(view)._isEmpty()) {
                    self._updateString(view, function(s) {

                        var ii = th._create("i", "", {
                            class: "lni  lni-xmark  ins-icon ins-button-text ins-light ",
                            "data-value": obj._getattr("value"),
                            "style": "font-size: 11px;"
                        });
                        var d = th._create("div", view, {
                            class: " ",
                            style: "display: block;    min-width: 80px;"
                        });

                        var sp = th._create("span", "", { class: "ins-tag ins-dark" }, [ii, d]);



                        ins(ii)._on("click", function(iiobj, e) {
                            self._get('option[value="' + iiobj._getData("value") + '"]')._p(
                                "selected",
                                false
                            );
                            iiobj._parent()._remove();

                        })



                        self._get(".ins_au_keys_area")._append(sp);
                    })
                }


            }
        })


    }

    _updateitem() {
        var self = this;



        var obj = this._get(
            'option[value="' + self._get("select")._getvalue() + '"]');
        var view = obj._getData("view");
        if (ins(view)._isEmpty()) {
            view = obj._gettext();
        }
        if (!ins(view)._isEmpty()) {
            self._updateString(view, function(s) {
                self._get(".ins_au_keys_area")._sethtml(s);
            })
        }
    }



    _updateValue() {

        if (this._isMultiaple()) {

            this._updateitems();
        } else {
            this._updateitem();

        }

    }


    _open_close(o, e, cls = "") {
        var self = this;
        if (self._get(".ins_autocomplete_all")._hasclass("ins_opend")) {
            self._close();
        } else {
            self._open(o, e, cls);
        }
    }


    _actions() {
        var self = this;


        this._get(".ins_au_keys_area")._on("click", function(o, e) {
            self._updateName(o);
            self._open_close(o, e);
        });


        this._get(".ins-list-open-btn")._on("click", function(o, e) {

            self._updateName(o);
            self._open_close(o, e);
        }, true);


        this._get(".ins-list-search-btn")._on("click", function(o, e) {
            self._updateName(o);
            self._open_close(o, e, "ins-list-fix");
        }, true);




        this._get(".ins-list-close-btn")._on("click", function(o, e) {
            self._updateName(o);
            self._close();
        }, true);
        this._get(".ins_autocomplete_input ")._on("input", function(o, e) {
            self._updateName(o);
            self._updateItems(o._getvalue())
        }, true);




    }


    _creatUi() {
        // this._me
        var th = ins()._ui;
        var select = this._get("select");
        self = this;

        var c = " ";
        var v = "";
        var ishows = th._create("i", "", {
            type: "text",
            class: " lni lni-chevron-left ins-list-open-btn ins-button-text",
            "data-name": c
        });
        var isearch = th._create("i", "", {
            type: "text",
            class: " lni lni-search-text ins-list-search-btn ins-button-text ",
            "data-name": c
        });
        var iclose = th._create("i", "", {
            type: "text",
            class: " lni  lni-xmark ins-list-close-btn  ins-button-text-danger",
            "data-name": c
        });





        var ins_au_keys_area = th._create("div", v, {
            type: "text",
            class: " ins_au_keys_area ins-flex-item-grow" + c,
            "style": "display: block;line-height: 25px;"
        });
        var title = th._create("h3", select._getData("title"), {
            type: "text",
            class: "ins-list-title  ins-flex-item-grow",
        });

        var actions = [ins_au_keys_area, isearch, ishows];


        if (select._getData("select_type") == "options") {


            var iedit = th._create("i", "", {
                type: "i",

                "data-options": select._getData("select_id"),

                class: " lni lni-pencil-1  ins-list-show-open  insaction ins-list-edit-btn  ins-button-text-danger",
                "data-id": this._name
            });

            ins(iedit)._on("click", function(o) {

                self._updateName(o);
                self._close();

            })




            ins("ins_plg_options_mangement")._plgin({
                o: ins(iedit),

                onUpdate: () => {
                    self._updateSelect();
                },
                "options": select._getData("select_id")
            }, function(cls) {});




            actions.push(iedit);

        }


        actions.push(iclose);



        var ins_autocomplete_input_area = th._create(
            "div", actions, {
                class: "ins_autocomplete_input_area ins-flex ins-flex-valign-start ins-form-input ins_ui_input ins-col-12 " +
                    c,
                "data-name": c
            }
        );
        var inps = th._create("input", "", {
            autocomplete: "off",
            value: v,
            type: "text",
            placeholder: "Search...",
            "placeholder-ar": "بحث ...",
            class: " ins_autocomplete_input ins-form-input ins-col-12   " + c,
            "data-name": c
        });


        var ins_autocomplete_data_list = th._create(
            "div", [inps], { class: " ins-col-12  ins_autocomplete_data_list " + c }
        );
        var _all_input_area = th._create(
            "div", [title, ins_autocomplete_input_area, ins_autocomplete_data_list], { class: " ins-col-12  all_input_area " + c, "data-name": this._name }
        );
        var cstyle = this._get("select")._getattr("style");
        var ins_autocomplete_all = ins(
            th._create(
                "div", [_all_input_area], { style: cstyle, class: " ins-col-12  ins_autocomplete_all  " + c }
            )
        );
        this._me._append_befor(ins_autocomplete_all);
        this._me._css({ display: "none" });
        this._updateValue();
    }

    _updateSelect() {



        self = this;


        ins()._ajax._to("inputs/get_select_options", self._get("select")._getData(), function(data) {
            self._get("select")._sethtml(data);
        })


    }
    _update() {
        this._me = this.options.o;


        if (!ins(this._me._get(0))._isEmpty()) {
            this._list = this._me._parent();
        }


    }
    _out() {


        this._me = this.options.o;
        var u = ins()._data._get_unique_id();
        if (!ins(this._me._get(0))._isEmpty()) {
            this._list = this._me._parent();
            this._list._addclass(u);
            this._list._addclass("ins_autocomplete_container");
            this._list._setdata("id", u);
            this._name = u;
            this._creatUi();
            this._actions();
            this._updateItems();

        }
    }
}