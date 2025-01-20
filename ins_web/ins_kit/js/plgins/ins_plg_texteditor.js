export class ins_plg_texteditor {
    _name = "";
    _class = "";
    options = {};
    _selected;
    constructor(o, id) {
        this.options = o;
    }

    _body_setcode(h) {
        ins(this._class + " .ins-text-editor-body")._sethtml(h);
    };

    _body_getcode() {
        return ins(this._class + " .ins-text-editor-body")._gethtml();
    };

    _text_set(h) {
        ins(this._class + " .ins-text-editor-textarea")._setvalue(h);
    };

    _selection_css_change(name, value) {
        var c = {};


        this._selected = this._get_selection();




        c[name] = value;

        ins(this._selected)._css(c);

        this._update_to_code();
    }

    _selection_css_get(name) {
        return ins(this._selected)._getcss(name);
    }
    _selection_attr(attr, value) {
        return ins(this._selected)._setattr(attr, value);
    }
    _selection_data(value) {
        return ins(this._selected)._sethtml(value);
    }

    _reviw_area_update() {
        if (ins(".ins-review-area")._isExists(true)) {
            ins(".ins-review-area")._sethtml(this._selected.outerHTML);
        }

    }
    _selection_css_remove(name) {

        ins(this._selected)._removeStyle(name);
    }
    _selection_class_add(c) {
        ins(this._selected)._addclass(c);
    }
    _selection_class_remove(...c) {
        ins(this._selected)._removeclass(...c);
    }


    _update_to_code() {
        this._text_set(this._body_getcode())
    };


    _get_selection() {
        var self = this;


        var n = window.getSelection().focusNode;

        if (ins(n)._is_parents(".ins-text-editor-body")) {

            var s = window.getSelection().focusNode.parentNode;
            if (s == null || ins(".ins-text-editor-body")._get(0) == s) {
                self._exeCmd("formatBlock", "p");
                s = window.getSelection().focusNode.parentNode;

            }
            return s;
        };
        return null;

    }

    _update_selection() {
        if (this._get_selection() != null) {
            this._selected = this._get_selection();

        }
    }

    _panel(data, onclose, style = "width: 80%;height: 80%;max-width: 1000px;max-height: 600px;", data_style = "") {
        var self = this;
        ins()._ui._ins_lightbox({
            title: false,
            options: { "data-name": self._name },
            // onopen: onopen,
            onclose: onclose,
            addto: "body",
            data: data,
            class: "_light_box_" + self._name,
            style: style,
            data_style: data_style,
        });
    }

    _exeCmd(cmd, block = null) {

        document.execCommand(cmd, false, block);
    }

    _addicon(icon) {


        ins(this._selected)._append(icon);

    }

    _addimg(getimg, status = "") {
        if (status == "update") {
            ins(this._selected)._setattr("src", getimg);
            this._reviw_area_update();

        } else {
            var img = ins()._ui._create("img", "", { src: getimg, style: "width:300px;height:auto" })

            ins(this._selected)._append(img);

        }
    }




    _font_size(o) {

        var v = o._getData("v");
        var cl = v.search("ins-font-");
        this._selection_class_remove("ins-font-s", "ins-font-m", "ins-font-l", "ins-font-xl", "ins-font-xxl", "ins-font-xxxl");

        var m = v.search('\\-');
        var t = v.search('\\+');


        if (cl != -1) {
            this._selection_css_remove("font-size");

            this._selection_class_add(v);
        } else if (t != -1 || m != -1) {

            var g = this._selection_css_get("font-size");
            var n = 12;
            if (!ins(g)._isEmpty()) {
                n = parseFloat(g.replace("px", ""));
            }
            if (m != -1) {
                n -= 4;
            } else {
                n += 4
            }
            this._selection_css_change("font-size", n + "px");

        } else {
            this._selection_css_change("font-size", v);
        }




    }

    _showcode() {
        var self = this;
        var c = this._body_getcode();

        var g = '<textarea class="ins-form-input ins-text-editor-lcode ins-full">' + c + '</textarea>';




        this._panel(g, function() {


            var lc = ins(".ins-text-editor-lcode")._getValue();

            self._text_set(lc);
            self._body_setcode(lc)
        });
    }

    _settings(o) {
        var self = this;

        var s = ins(self._selected);
        var uidata = [
            { "type": "start", "class": "ins-padding-xl ins-bg-4 ins-body" },
        ];

        var t = "";
        if (self._selected.tagName == "IMG" || s._hasclass("fas")) {
            uidata.push({ "type": "div", "data": self._selected.outerHTML, "class": "ins-review-area  ins-fcol-12 ins-card ins-padding-xl  ins-flex-center" });

            t = "img";
        } else if (s._hasclass("fas") || s._hasclass("far") || s._hasclass("lni") || s._hasclass("fab")) {

            t = "icon";

            uidata.push({ "type": "div", "data": self._selected.outerHTML, "class": "ins-review-area ins-fcol-12 ins-card ins-padding-xl  ins-flex-center" });
        } else {
            uidata.push({ "type": "textarea", "title": "text", "value": s._gethtml(), "class": "ins-data-area" });
        }
        uidata.push({ "type": "textarea", "title": "classes", "value": s._getattr("class"), "class": "ins-class-area" });
        uidata.push({ "type": "textarea", "title": "css", "value": s._getattr("style"), "class": "ins-css-area" });
        uidata.push({ "type": "end" });

        if (t == "img" || t == "icon") {

            uidata.push({ "type": "div", "class": "ins-space-s" });

            uidata.push({ "type": "start", "class": "ins-flex-center  ins-padding-m" });
            if (t == "img") {

                uidata.push({ "type": "li", "data": "Update", "data-c": "update_image", "class": "ins-button ins-editor-action   ins-fcol-3" });
            }

            uidata.push({ "type": "li", "data": "Remove", "data-c": "remove_selected", "class": "ins-button  ins-editor-action ins-fcol-3" });
            uidata.push({ "type": "end" });
        }


        ins(uidata)._ui._render(function(getdata) {
            self._panel(getdata, function() {
                self._update_to_code();
            }, "height:auto;width:550px", "position: relative;");

        });


    }

    imgplg = null;
    _insertimage(status = "") {
        var self = this;

        if (self.imgplg == null) {
            ins("ins_plg_file_browser")._plgin({
                    "path": "/ins-upload/",
                    onselect: function(file, path) {
                        self._addimg(path, status);
                    }
                },
                function(plg) {
                    self.imgplg = plg;
                    self.imgplg._run();
                });
        } else {
            self.imgplg._run();
            self.imgplg.onselect = function(file, path) {
                self._addimg(path, status);
            }
        }

    }


    _background(o) {



    }

    _color(o) {



    }
    _insertlink(o) {
        var linkURL = prompt('Enter a URL:', 'http://');
        this._exeCmd("createlink", linkURL);
    }
    _removeselected(o) {
        var c = confirm("are you sure you want to delete seleced object");
        if (c) {

            ins(this._selected)._remove();
            this._selected = null;
            ins()._ui._lightbox_remove();
        }

    }


    _exeACtion(o, action) {
        var self = this;

        switch (action) {
            case "fullscreen":
                ins(self._class)._toggle_class("ins-editor-fullscreen");
                o._toggle_class("ins-active");
                break;
            case "showcode":
                self._showcode();
                break;
            case "background":
                self._background();
                break;
            case "color":
                self._color();
                break;
            case "font_size":
                self._font_size(o);
                break;
            case "settings":
                self._settings(o);
                break;
            case "insertimage":
                self._insertimage(o);
                break;

            case "remove_selected":
                self._removeselected(o);
                break;
            case "update_image":
                self._insertimage("update");
                break;
            case "insertlink":
                self._insertlink("update");
                break;



        }



    }

    _formt() {
        var self = this;
        ins(self._class + " .ins-editor-format")._on(
            "click",
            function(o, e) {
                e.preventDefault();;
                self._exeCmd(o._getData("c"));
            },
            true
        );
        ins(".ins-editor-action")._on(
            "click",
            function(o, e) {
                e.preventDefault();

                self._update_selection();

                self._exeACtion(o, o._getData("c"));
            },
            true
        );




        ins(self._class + " .ins-text-editor-prepare")._on(
            "click",
            function(o, e) {
                self._update_selection();

                if (ins(self._selected)._isEmpty()) {

                    alert("No postion selected");
                    e.preventDefault();

                }

            },
            true
        );


        /*
                ins(self._class + " .ins-editor-action-css-byvalue")._on(
                    "click",
                    function(o, e) {
                        self._update_selection();


                    },
                    true
                );*/

        ins(self._class + " .ins-editor-action-css-byvalue")._on(
            "input",
            function(o, e) {
                e.preventDefault();

                console.log(o._getvalue());
                self._selection_css_change(o._getData("css"), o._getvalue());

            },
            true
        );
        ins(self._class + " .ins-editor-action-css")._on(
            "click",
            function(o, e) {
                e.preventDefault();;
                self._selection_css_change(o._getData("c"), o._getData("v"));


            },
            true
        );
        ins(" .ins-class-area")._on(
            "input",
            function(o, e) {
                e.preventDefault();;
                self._selection_attr("class", o._getvalue());

                self._reviw_area_update();

            },
            true
        );
        ins(".ins-css-area")._on(
            "input",
            function(o, e) {
                e.preventDefault();
                self._selection_attr("style", o._getvalue());
                self._reviw_area_update();

            },
            true
        );

        ins(".ins-data-area")._on(
            "input",
            function(o, e) {
                e.preventDefault();
                self._selection_data(o._getvalue());


            },
            true
        );

        ins(self._class + " img ," + self._class + " .ins-text-editor-body .lni ," + self._class + " .ins-text-editor-body .ins-data-icon," + self._class + " .ins-text-editor-body .fas ," + self._class + " .ins-text-editor-body .far," + self._class + " .ins-text-editor-body .fab"

        )._on(
            "click",
            function(o, e) {
                e.preventDefault();
                self._selected = o._get(0);
                self._exeACtion(o, "settings");


            },
            true
        );
        ins(self._class + " .ins-menu .ins-header")._on(
            "click",
            function(o, e) {
                e.preventDefault();

                self._update_selection();


            },
            true
        );




        ins(self._class + " .ins-text-editor-lcode")._on(
            "change",
            function(o, e) {
                e.preventDefault();

                self._update_selection();


            },
            true
        )



        var self = this;
        ins(self._class + " .ins-editor-format-block")._on(
            "click",
            function(o, e) {
                e.preventDefault();;
                self._exeCmd("formatBlock", o._getData("c"));
            },
            true
        );

        ins(self._class + " .ins-text-editor-body")._on("input", function(e, o) {
            self._update_to_code()
        });
    }

    _actions() {
        var slef = this;
        slef._formt();
    }

    _out() {
        var self = this;

        self._name = this.options["name"];
        self._class = "." + self._name.trim();
        self._actions();




        var lc = ins(this._class + " .ins-text-editor-textarea")._getValue();

        self._body_setcode(lc)
    }
}