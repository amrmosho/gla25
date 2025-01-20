/**
 *
 * @returns {undefined}
 */
export class ins_plg_file_browser {
    options = {};
    id = "";
    _data = {};
    _path = "";
    _home = "";
    _clipboard = "";
    _clipboard_status = "";
    constructor(o, id) {
        this.options = o;
        this.id = id;
    }
    _get_this_path() {
        var c = ins(".ins-breadcrumb-bar")._getData("bodypath");
        this.path = c;
        return c;
    }
    _body(path, get, fun, more = {}) {
        if (path == null) {
            path = this._get_this_path();
        }
        more.path = path;
        more.get = get;
        var v = ins(".ins-files-browser-search-input")._getvalue();
        if (!ins(v)._isEmpty()) {
            more.w = v;
        }
        if (!ins(this._sort)._isEmpty()) {
            more.sort = this._sort;
            more.sort_type = this._sort_type;
        }
        var options = ins()._map._get_page_data();
        more.site = options["site"];
        more.lang = options["lang"];
        ins()._ajax._to("pages/ins_file_browser", more, function(d) {
            ins()._ui._removeloader();
            fun(d);
        });
    }
    _upload_plg = null;
    _upload() {
        var t = this;
        if (t._upload_plg == null) {
            ins("ins_plg_upload")._plgin({
                    o: ".ins_upload_file",
                    file_info: ".ins-uploader-file-info ",
                    "drop_area": ".ins-uploader-file-drop_area",
                    ondone: function(data) {},
                    dir: t._get_this_path(),
                },
                function(plg) {
                    t._upload_plg = plg;
                }
            );
        } else {
            t._upload_plg.options["dir"] = t._get_this_path();
        }
    }
    _sort = "";
    _sort_type = "a";
    _update_body(more, fun) {
        ins(".ins-files-browser")._ui._addloader();
        var t = this;
        var tme = ins(".ins-files-browser-body");
        t._body(
            this._get,
            "body",
            function(data) {
                tme._sethtml(data);
                ins()._ui._removeloader();
                if (fun != null) {
                    fun();
                }
            },
            more
        );
    }
    _update_dirs_area(more) {
        ins(".ins-files-browser")._ui._addloader();
        var t = this;
        var tme = ins(".ins-files-browser-dirs");
        t._body(
            t._home,
            "dirs",
            function(data) {
                tme._sethtml(data);
                ins()._ui._removeloader();
            }, { "bodypath": this._get_this_path(), "home": t._home }
        );
    }
    _panel(data, onopen, style = "width: 60%;height: 60%;max-width: 800px; ") {
        var t = this;
        var s = ins()._ui._ins_lightbox({
            title: false,
            options: {},
            onopen: onopen,
            onclose: function() {
                t._update_body();
            },
            addto: ".ins-files-browser",
            data: data,
            class: "ins-position-absolute",
            style: style,
        });
    }
    _panel_close() {
        ins(" .ins-files-browser .ins-lightbox")._remove();
    }
    _update_selected_informations() {
        var t = this;
        var cc = ins("." + t.id + "  .ins-files-browser-item.ins-active")._get()
            .length;
        if (cc > 0) {
            ins(".ins-selected-toolbar")._removeclass("ins-hidden");
            ins(".ins-selected-toolbar-count")._settext(cc);
            var paths = t._update_selected_files();
            t._body(
                this._get_this_path(),
                "files_info_data",
                function(data) {
                    ins(".ins-files-browser-infobar")._sethtml(data);
                }, { paths: paths, path: t._get_this_path() }
            );
        } else {
            ins(".ins-selected-toolbar")._addclass("ins-hidden");
        }
    }
    _update_selected_files() {
        var t = this;
        var paths = "";
        ins("." + t.id + "  .ins-files-browser-item.ins-active")._each(function(
            o
        ) {
            paths += "," + o._getData("path");
        });
        return paths;
    }
    _update_selected_actions(action) {
        var t = this;
        var cc = ins("." + t.id + "  .ins-files-browser-item.ins-active")._get()
            .length;
        var paths = t._update_selected_files();
        if (action == "delete") {
            if (confirm("Are you sure you want to delete (" + cc + ") file?")) {
                t._body(
                    null,
                    "body",
                    function(data) {
                        ins(".ins-files-browser-body")._sethtml(data);
                        ins()._ui._send_tiny_message();
                        t._update_selected_informations();
                        t._update_dirs_area();
                    }, { paths: paths, action: action }
                );
            }
        } else if (action == "download") {
            t._body(
                null,
                "body",
                function(data) {
                    var d = JSON.parse(data);
                    window.open(d["url"], '_blank');
                    console.log(d["url"]);
                    //  ins(".ins-files-browser-body")._sethtml(data);
                    //   ins()._ui._send_tiny_message();
                    //   t._update_selected_informations();
                    // t._update_dirs_area();
                }, { paths: paths, action: action }
            );
            /*  if (action == "cut") {
                  ins()._ui._send_tiny_message("(" + cc + ") file cuted");
              } else {
                  ins()._ui._send_tiny_message("(" + cc + ") file copiedh");
              }
              ins(".ins-selected-action-paste")._removeclass("ins-hidden");*/
        } else if (action == "copy" || action == "cut") {
            t._clipboard = paths;
            t._clipboard_status = action;
            if (action == "cut") {
                ins()._ui._send_tiny_message("(" + cc + ") file cuted");
            } else {
                ins()._ui._send_tiny_message("(" + cc + ") file copiedh");
            }
            ins(".ins-selected-action-paste")._removeclass("ins-hidden");
        } else if (action == "paste") {
            t._body(
                null,
                "body",
                function(data) {
                    ins(".ins-files-browser-body")._sethtml(data);
                    ins()._ui._send_tiny_message();
                    t._update_selected_informations();
                    t._update_dirs_area();
                    ins(".ins-selected-action-paste")._addclass("ins-hidden");
                }, { paths: t._clipboard, action: t._clipboard_status }
            );
        } else if (action == "clear") {
            ins(".ins-files-browser-item")._removeclass("ins-active");
            t._update_selected_informations();
        }
    }
    _do_panel_action(action, more) {
        var t = this;
        if (more == null) {
            var value = ins(".ins-file-browser-action-value")._getvalue();
            var d = { parh: t._get_this_path(), action: action, value: value };
        } else {
            var d = more;
        }
        t._body(
            null,
            "body",
            function(data) {
                try {
                    var j = JSON.parse(data);
                    if (ins(j["status"])._isExists()) {
                        alert(j["msg"]);
                    } else {
                        ins(".ins-files-browser-body")._sethtml(data);
                        ins()._ui._send_tiny_message();
                        t._panel_close();
                        t._update_dirs_area();
                    }
                } catch (e) {
                    ins(".ins-files-browser-body")._sethtml(data);
                    ins()._ui._send_tiny_message();
                    t._panel_close();
                    t._update_dirs_area();
                }
            },
            d
        );
    }
    _get_action_ui(action) {
        var t = this;
        t._body(
            this._get_this_path(),
            "ui_action",
            function(data) {
                t._panel(data, function() {}, "width:400px;height:276px;");
            }, { action: action, paths: t._update_selected_files() }
        );
    }
    _hide_show_action(o, c, u, onchnage) {
        var obj = {};
        if (o._hasclass(c)) {
            o._removeclass(c);
            obj[u] = "false";
            onchnage("false");
        } else {
            o._addclass(c);
            obj[u] = "true";
            onchnage("true");
        }
        ins(obj)._map._update_user_setting();
    }
    _search(s) {
        this._update_body({ w: s });
    }
    images = ["jpg", "png", 'jpeg', 'gif'];
    icons = { "csv": '<i class="fas  fa-file-csv"> </i>', "pdf": '<i class="fas  fa-file-pdf"> </i>', "txt": '<i class="fas  fa-file-word"> </i>', "file": '<i class="lni lni-empty-file"></i>' };
    _select_file(o) {
        var self = this;
        var file = o._getData("file");
        var path = o._getData("path");
        if (ins(self.options["ondone"])._isExists()) {
            self.options["ondone"](file, path);
        } else {
            var tme = o._parents(".ins_lightbox_data");
            var file = o._getData("file");
            var path = o._getData("path");
            var _exs = file.split(".");
            var _ex = _exs[_exs.length - 1];
            if (ins(tme._getData("val_to"))._isExists()) {
                ins("." + tme._getData("val_to"))._setvalue(file);
            }
            if (this.images.includes(_ex)) {
                if (ins(tme._getData("icon_to"))._isExists()) {
                    ins("." + tme._getData("icon_to"))._addclass("ins-hidden");
                }
                if (ins(tme._getData("src_to"))._isExists()) {
                    ins("." + tme._getData("src_to"))._removeclass("ins-hidden");
                    console.log(path);
                    ins("." + tme._getData("src_to"))._setattr("src", "");
                    ins("." + tme._getData("src_to"))._setattr("src", path);
                }
            } else {
                if (ins(tme._getData("src_to"))._isExists()) {
                    ins("." + tme._getData("src_to"))._addclass("ins-hidden");
                }
                if (ins(tme._getData("icon_to"))._isExists()) {
                    ins("." + tme._getData("icon_to"))._removeclass("ins-hidden");
                    if (!Object.keys(self.icons).includes(_ex)) {
                        _ex = "file";
                    }
                    ins("." + tme._getData("icon_to"))._sethtml(self.icons[_ex]);
                }
            }
            if (ins(self.options["onselect"])._isExists()) {
                self.options["onselect"](file, path);
            }
        }
    }
    _actions() {
        var self = this;
        ins("." + self.id + " .ins-files-browser-search-input")._on(
            "change",
            function(o) {
                self._search(o._getvalue());
            },
            true
        );
        ins("." + self.id + " .ins-selected-action")._on(
            "click",
            function(o) {
                self._update_selected_actions(o._getData("action"));
            },
            true
        );
        ins("." + self.id + " .ins-files-browser-ui-action")._on(
            "click",
            function(o) {
                self._get_action_ui(o._getData("action"));
            },
            true
        );
        ins("." + self.id + " .ins-files-browser-do-action")._on(
            "click",
            function(o) {
                self._do_panel_action(o._getData("action"));
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-sort ")._on(
            "click",
            function(o) {
                ins(".ins-files-browser-sort")._removeclass("ins-active");
                o._addclass("ins-active");
                self._sort = o._getData("sort");
                if (self._sort_type == "a") {
                    self._sort_type = "d";
                } else {
                    self._sort_type = "a";
                }
                self._update_body();
            },
            true
        );
        ins("." + self.id + "  .ins-file-browser-reload")._on(
            "click",
            function(o) {
                ins(".ins-files-browser-search-input")._setvalue("");
                self._sort = "";
                self._update_body({}, function() {
                    self._update_dirs_area();
                });
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-unselect-item ")._on(
            "click",
            function(o) {
                var path = o._parent()._getData("path");
                ins('.ins-files-browser-item[data-path="' + path + '"]')._removeclass(
                    "ins-active"
                );
                o._parent()._remove();
                self._update_selected_informations();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-rename-files")._on(
            "click",
            function(o) {
                var data = {};
                ins(".ins-file-browser-action-value")._each(function(o) {
                    data[o._getData("path")] = o._getvalue();
                });
                self._do_panel_action("rename_files", {
                    action: "rename_files",
                    data: JSON.stringify(data),
                });
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-select-all")._on(
            "click",
            function(o) {
                ins(".ins-files-browser-item")._toggle_class("ins-active");
                self._update_selected_informations();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-path-pin")._on(
            "click",
            function(o) {
                ins({
                    "ins-files-browser-path": self._get_this_path(),
                })._map._update_user_setting();
                ins()._ui._send_tiny_message();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-body-tolist")._on(
            "click",
            function(o) {
                o._addclass("ins-active");
                ins(".ins-files-browser-body-toblocks")._removeclass("ins-active");
                ins(".ins-files-browser-body-data")._addclass(
                    "ins-files-browser-body-list"
                );
                ins({
                    "ins-files-browser-body": "list",
                })._map._update_user_setting();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-body-toblocks")._on(
            "click",
            function(o) {
                o._addclass("ins-active");
                ins(".ins-files-browser-body-data")._removeclass(
                    "ins-files-browser-body-list"
                );
                ins(".ins-files-browser-body-tolist")._removeclass("ins-active");
                ins({ "ins-files-browser-body": "blocks" })._map._update_user_setting();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-item")._on(
            "click",
            function(o) {
                o._toggle_class("ins-active");
                self._update_selected_informations();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-file")._on(
            "dblclick",
            function(o) {
                self._select_file(o);
                ins()._ui._lightbox_remove();
            },
            true
        );
        ins("." + self.id + "  .ins-files-browser-dir")._on(
            "dblclick",
            function(o) {
                self._body(o._getData("path"), "body", function(data) {
                    ins(".ins-files-browser-body")._sethtml(data);
                }, { "home": o._getData("home") });
            },
            true
        );
        ins(
            "." +
            self.id +
            "  .ins-files-browser-dirs .ins-files-browser-dir,.ins-breadcrumb .ins-files-browser-dir"
        )._on(
            "click",
            function(o) {
                ins(".ins-files-browser-dirs   .ins-files-browser-dir")._removeclass(
                    "ins-active"
                );
                ins(".ins-files-browser")._ui._addloader();
                var cl =
                    '.ins-files-browser-dirs .ins-files-browser-dir[data-path="' +
                    o._getData("path") +
                    '"]';
                ins(cl)._addclass("ins-active");
                self._body(o._getData("path"), "body", function(data) {
                    ins(".ins-files-browser-body")._sethtml(data);
                    ins()._ui._removeloader();
                }, { "home": o._getData("home") });
            },
            true
        );
        ins("." + self.id + "  .ins-file-show-sidebar")._on(
            "click",
            function(me) {
                var o = ins(".ins-files-browser");
                var c = "ins-files-browser-full-body";
                var u = "ins-files-browser-full-body";
                if (me._hasclass("ins-active")) {
                    me._removeclass("ins-active");
                } else {
                    me._addclass("ins-active");
                }
                self._hide_show_action(o, c, u, function(x) {});
            },
            true
        );
        ins("." + self.id + "  .ins-file-show-infobar")._on(
            "click",
            function(me) {
                var o = ins(".ins-files-browser-body");
                var c = "ins-files-browser-show-infobar";
                var u = "ins-files-browser-show-infobar";
                self._hide_show_action(o, c, u, function(x) {
                    if (x == "true") {
                        me._addclass("ins-active");
                    } else {
                        me._removeclass("ins-active");
                    }
                });
            },
            true
        );
        ins("." + self.id + " .ins-file-browser-upload")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                self._upload();
                ins(" .ins-files-browser .ins-lightbox")._remove();
                ins()._ajax._to("inputs/upload", {}, function(d) {
                    self._panel(d);
                });
            },
            true
        );
    }
    _run(newdats = {}) {
        var t = this;
        ins()._ui._addloader();;
        var p = "/ins_upload/"
        if (newdats["path"] != null) {
            p = newdats["path"];
        }
        t._home = p;
        t._path = p;
        t._body(p, "home", function(data) {
            ins()._ui._lightbox_remove();
            ins()._ui._ins_lightbox({
                title: "files",
                class: " " + t.id,
                options: newdats,
                data: data,
                style: "width: 80%;height: 80%;max-width: 1200px;",
            });
        });
    }
    _open(o) {
        var t = this;
        var gdata = o._getData();
        delete gdata.insaction;
        delete gdata.plgin;
        var newdats = {};
        Object.keys(gdata).forEach(function(k) {
            newdats["data-" + k] = gdata[k];
        });
        newdats["path"] = o._getData("path");
        t._run(newdats);
    }
    _out() {
        var t = this;
        if (ins(this.options.o)._isExists()) {
            var me = this.options.o;
            me._on(
                "click",
                function(o) {
                    t._open(o)
                },
                true
            );
        }
        t._actions();
    }
}