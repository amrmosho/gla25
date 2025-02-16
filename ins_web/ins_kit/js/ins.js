/* global html2canvas */
function InsMap(o) {
    this.o = o;
}
InsMap.prototype._setKey = (name = "", action = (k) => {}) => {
    function doaction(ek, jk) {
        if (ek == jk) {
            action(jk);
        }
    }
    ins()._insAjax(function(ajax) {
        ajax._json("keys_map.json", (json) => {
            if (ins(json[name])._isExists) {
                var jk = json[name];
                ins("body")._event("keydown", (o, e) => {
                    if (jk.alt == true && e.altKey) {
                        doaction(e.key, jk.key);
                    } else if (jk.alt == null) {
                        doaction(e.key, jk.key);
                    }
                })
            }
        });
    })
};
InsMap.prototype._getKey = (name = "", onGet = (k) => {}) => {
    ins()._insAjax(function(ajax) {
        ajax._json("keys_map.json", (json) => {
            if (ins(json[name])._isExists) {
                onGet(json[name]);
            } else {
                onGet("-1");
            }
        });
    })
};
InsMap.prototype._get_page_data = function(page = ".ins_main") {
    try {
        if (ins(page)._isExists(true)) {
            return JSON.parse(ins(page)._getData("data"));
        } else {
            return {};
        }
    } catch (error) {
        return {};
    }
};
InsMap.prototype._lang = function() {
    var g = this._get();
    if (g["lang"] == null) {
        g["lang"] = ins("body")._getData("lang");
    }
    return g["lang"];
};



InsMap.prototype._surl = function(adds = {}, ...remove) {
    var url = "/";
    if (this.o == "undefined" || this.o == null) {
        this.o = ".ins-app"
    }
    var j = JSON.parse(ins(this.o)._getData("data"));
    var urldata = j["_g"];
    Object.keys(adds).forEach(function(k) {
        urldata[k] = adds[k];
    });



    if (j["_a"] != null) {
        url += "/" + j["_a"] + "/";
    }

    if (urldata["alias"] != null) {
        url += "/" + urldata["alias"] + "/";
        delete urldata.alias;
    }
    if (urldata["mode"] != null && !remove.includes("mode")) {
        url += "/" + urldata["mode"] + "/";
        delete urldata.mode;
    }
    if (urldata["id"] != null) {
        url += "/" + urldata["id"] + "/";
        delete urldata.id;
    }
    url += "do/"
    Object.keys(urldata).forEach(function(k) {
        if (!remove.includes(k)) {
            url += "/" + k + "/" + urldata[k];
        }
    });
    url = ins()._data._replaceAll("///", "/", url);
    url = ins()._data._replaceAll("//", "/", url);
    return url;
};


InsMap.prototype._hurl = function(adds = {}, ...remove) {
    var url = "/";

    if (this.o == "undefined" || this.o == null) {
        this.o = ".ins-app"
    }

    var j = JSON.parse(ins(this.o)._getData("data"));
    var urldata = j["_g"];

    Object.keys(adds).forEach(function(k) {
        urldata[k] = adds[k];
    });

    if (j["_a"] != null && j["_a"] !== "ins_gla" && j["_a"] !== "home") {
        url += "/" + j["_a"];
    }


    if (urldata["alias"] != null && urldata["alias"] !== "home") {
        url += "/" + urldata["alias"];
        delete urldata.alias;
    }

    if (urldata["mode"] != null && !remove.includes("mode")) {
        url += "/" + urldata["mode"];
        delete urldata.mode;
    }

    if (urldata["id"] != null) {
        url += "/" + urldata["id"];
        delete urldata.id;
    }

    url += "/do";

    Object.keys(urldata).forEach(function(k) {
        if (!remove.includes(k)) {
            url += "/" + k + "/" + urldata[k];
        }
    });
    console.log(j);
    console.log(urldata);

    url = ins()._data._replaceAll("///", "/", url);
    url = ins()._data._replaceAll("//", "/", url);
    return url;
};


InsMap.prototype._url = function(adds = {}, ...remove) {
    var url = "/";
    if (this.o == "undefined" || this.o == null) {
        this.o = ".ins-app"
    }
    var j = JSON.parse(ins(this.o)._getData("data"));
    var urldata = j["_g"];
    Object.keys(adds).forEach(function(k) {
        urldata[k] = adds[k];
    });



    if (j["_ta"] != null) {
        url += "/" + j["_ta"] + "/";
    }

    if (urldata["alias"] != null) {
        url += "/" + urldata["alias"] + "/";
        delete urldata.alias;
    }
    if (urldata["mode"] != null && !remove.includes("mode")) {
        url += "/" + urldata["mode"] + "/";
        delete urldata.mode;
    }
    if (urldata["id"] != null) {
        url += "/" + urldata["id"] + "/";
        delete urldata.id;
    }
    url += "do/"
    Object.keys(urldata).forEach(function(k) {
        if (!remove.includes(k)) {
            url += "/" + k + "/" + urldata[k];
        }
    });
    url = ins()._data._replaceAll("///", "/", url);
    url = ins()._data._replaceAll("//", "/", url);
    return url;
};
InsMap.prototype._get = function(page = ".ins-app") {
    try {
        if (ins(page)._isExists(true)) {
            var j = JSON.parse(ins(page)._getData("data"));
            return j["_g"];
        } else {
            return {};
        }
    } catch (error) {
        return {};
    }
};


InsMap.prototype._data = function(page = ".ins-app") {
    try {
        if (ins(page)._isExists(true)) {
            var j = JSON.parse(ins(page)._getData("data"));
            return j;
        } else {
            return {};
        }
    } catch (error) {
        return {};
    }
};
/**
 * type name like compnont name } defult 'gen'
 * @param {setfor {org/me} defult 'me' ,callback ondone } options 
 */
InsMap.prototype._removeUserSettings = function(options) {
    var s = options.setfor == null ? "me" : options.setfor;
    var data = {
        type: this.o,
        status: "remove_settings",
        setfor: s
    };
    ins()._ajax._to("eng/users", data, function(data) {
        if (options.ondone != null) {
            options.ondone();
        }
    });
};

function InsDB(o) {
    this.o = o;
}
//<editor-fold defaultstate="collapsed" desc="UI">
function UI(o) {
    this.o = o;
}
var updated = [];

function updateui(m, t) {
    switch (t) {
        case "plgin":
            var op = m._getData();
            op.o = m;
            ins(m._getData("plgin"))._plgin(op, function(cls) {});
            break;
        case "plgin_change":
            var op = m._getData();
            op.o = m;
            ins(m._getData("plgin"))._plgin_change(op, function(cls) {});
            break;
        case "chart":
            var options = m._getData();
            options.o = "#" + m._getAttribute("id");
            ins("ins_plg_charts")._plgin(options, function(cls) {});
            break;
        case "ins_print":
        case "print":
            m._on(
                "click",
                function(o, e) {
                    ins()._print(o);
                },
                true
            );
            break;
        case "clear_connect":
            m._event("input", function(e) {
                var a = e._getValue();
                a = a.replace(/\s+|-|\'|\"|\/|\&/g, "_");
                a = a.replace(/\_+/g, "-");
                ins("." + e._getData("jsto"))._setValue(a);
            });
            break;
        case "ins_autocomplete":
            ins("ins_plg_listauto")._plgin({ o: m }, function() {});
            break;
        case "ins_json_editor":
            ins("ins_json_editor")._plgin({ o: m }, function() {});
            break;
        case "ins_to_buttons_list":
            var options = {};
            if (ins(m._getData("onchange"))._isExists()) {
                options.onchange = window[m._getData("onchange")];
            }
            m._ui._to_buttons_list(options);
            break;
        case "ins_json_form":
            ins("ins_plg_json_area")._plgin({ o: m });
            break;
        case "clone":
            m._on("click", function(e) {
                ins(e._getData("cloneto"))._append(
                    ins(e._getData("clone"))._getMyHtml()
                );
                ins()._ui._update();
            });
            break;
        case "fill_select":
            m._event("click", function(e) {
                var option = m._getData();
                if (!ins(e._getData("onfill"))._isEmpty())
                    option.onfill = function() {
                        window[e._getData("onfill")](e, ins(e._getData("to")));
                    };
                ins()._ui._fill_select(option);
            });
            break;
        case "ui_create_pdf":
            m._event("click", function(o) {
                ins()._ui._ui_create_pdf(o);
            });
            break;
        case "ui_create_image":
            m._event("click", function(o) {
                ins()._ui._ui_create_image(o);
            });
            break;
        case "doprint":
            m._event("click", function(o, e) {
                window.print();
            });
            break;
        case "print_area":
            function printImage(image) {
                var printWindow = window.open(
                    "",
                    "Print Window",
                    "height=600,width=900"
                );
                if (printWindow) {
                    printWindow.document.write("<html><head><title>Print Window</title>");
                    printWindow.document.write("</head><body ><img src='");
                    printWindow.document.write(image);
                    printWindow.document.write("' /></body></html>");
                    printWindow.focus();
                    setTimeout(function() {
                        printWindow.print();
                        printWindow.close();
                    }, 500);
                }
            }
            m._on("click", function(o, e) {
                ins()._ui._create_image({
                    area: o._getData("area"),
                    callback: function(data) {
                        var data = JSON.parse(data);
                        printImage(data["url"]);
                    },
                });
            });
            break;
        case "ins_tooltip":
            var tootip = null;
            m._event("mouseover", function(o, e) {
                var data = [];
                if (!ins(o._getData("text"))._isEmpty()) {
                    data.push({
                        name: "div",
                        child: o._getData("html"),
                        event: [],
                        attrs: {},
                    });
                } else if (!ins(o._getData("title"))._isEmpty()) {
                    data.push({
                        name: "div",
                        child: o._getData("title"),
                        event: [],
                        attrs: {},
                    });
                } else if (!ins(o._getData("tip"))._isEmpty()) {
                    data.push({
                        name: "div",
                        child: o._getData("tip"),
                        event: [],
                        attrs: {},
                    });
                } else if (!ins(o._getHtml())._isEmpty()) {
                    data.push({ name: "div", data: o._getHtml(), event: [], attrs: {} });
                }
                if (!ins(o._getData("img"))._isEmpty()) {
                    data.push({
                        name: "img",
                        data: t,
                        event: [],
                        attrs: { src: o._getData("img") },
                    });
                }
                ins(".ins_added_tooltip")._remove();
                tootip = ins()._ui._get(data, "div", {
                    class: "ins_tooltip ins_added_tooltip ins_menu",
                });
                ins(tootip)._setCSS({
                    top: e.clientY - (tootip.offsetHeight + 10) + "px",
                    left: e.clientX - (tootip.offsetWidth / 2 + 50) + "px",
                });
                ins("body")._append(tootip);
            });
            m._event("mouseout", function(o, e) {
                if (ins(tootip)._isExists()) {
                    ins(tootip)._remove();
                }
            });
            m._event("mousemove", function(o, e) {
                ins(tootip)._setCSS({
                    top: e.clientY - (tootip.offsetHeight + 20) + "px",
                    left: e.clientX - (tootip.offsetWidth / 2 + 20) + "px",
                });
            });
            break;
        case "ins_data_update":
            var do_ins_udate = (e) => {
                var op = {
                    get_file: "db/update",
                    table: e._getData("type"),
                    id: e._getData("id"),
                    field: e._getData("name"),
                    value: e._getValue(),
                };
                ins()._ui._page_progress_run();
                ins()._ajax._send("/ins_ajax.php", op, null, function() {
                    ins()._ui._page_progress_hide();
                    ins()._ui._send_tiny_message();
                });
            };
            if (m._p("tagName") === "SELECT" || m._p("tagName") === "INPUT") {
                m._event("change", do_ins_udate);
            } else if (m._p("tagName") === "INPUT") {
                m._event("input", do_ins_udate);
            } else {
                m._event("click", do_ins_udate);
            }
            break;
        case "select_append":
            m._event("click", function(e) {
                var option = e._getData();
                option.url =
                    "/ins_admin/" +
                    e._getData("type") +
                    "/add/do/get_tmp_index/main_style/ins_appendto_combo/" +
                    e._getData("to") +
                    "/";
                if (!ins(e._getData("select_text"))._isEmpty())
                    option.url += "select_text/" + e._getData("select_text") + "/";
                if (!ins(e._getData("select_value"))._isEmpty())
                    option.url += "select_value/" + e._getData("select_value") + "/";
                if (!ins(e._getData("onclose"))._isEmpty())
                    option.url += "onclose/" + e._getData("onclose") + "/";
                if (!ins(e._getData("onopen"))._isEmpty()) {
                    option.onopen = function() {
                        window[e._getData("onopen")](e);
                    };
                }
                option.onclose = function() {
                    if (!ins(e._getData("onclose"))._isEmpty()) {
                        window[e._getData("onclose")](e);
                    }
                };
                ins()._ui._ins_lightbox(option);
            });
            break;
        case "ajax_upload_delete":
            m._event(
                "click",
                function(ie) {
                    var options = { status: "delete", file: m._getData("file") };
                    ins(ie)._ajax._send(
                        "/ins_ajax.php?get_file=/eng/upload_1",
                        options,
                        "POST",
                        function(d) {
                            var p = m._parent();
                            //  var f = p._find("._file");
                            var pb = p._find(".progress_bar");
                            if (ins(p._find("img"))._isExists()) {
                                p._find("img")._setAttribute("src", "");
                            }
                            pb._setCSS({ width: "0px" });
                            pb._setText("");
                            p._removeClass("uploaded");
                            p._find("*")._removeClass("uploaded");
                            // if (!ins(f)._isEmpty()) {
                            if (!ins(m._getData("ondelete"))._isEmpty()) {
                                window[m._getData("ondelete")](options, m);
                            }
                            // }
                        }
                    );
                },
                false
            );
            break;
        case "ins_datepicker":
            ins("ins_plg_datePicker")._plgin({ o: m }, function() {});
            break;
        case "lightbox_remove":
            m._event("click", function(e) {
                ins()._ui._removeLightbox();
            });
            break;
        case "collapsed":
        case "ins_collapsed":
            m._ui._collapsed();
            break;
        default:
            var ops = "";
            var g = t.toLowerCase();
            var d = m._getData(g);
            if (m._getData(g + "_options") != null) {
                ops = m._getData(g + "_options"); {
                    var ps = ops.split(",");
                }
                if (ps.length > 1) {
                    ps.forEach(function(o, i) {
                        if (o == "this") {
                            ps[i] = m;
                        }
                    });
                } else {
                    ps = ops
                    if (ps == "this") {
                        ps = m;
                    }
                }
                if (d == "this") {
                    d = m;
                }
                ins(d)._readProp("_" + t, ps);
            } else {
                if (d == "this" || d == null) {
                    d = m;
                }
                ins(d)._readProp("_" + t);
            }
            break;
    }
}
UI.prototype._ins_print = function(options) {
    if (ins(this.o)._isExists()) {
        options.id = this.o;
    }
    var option = {};
    option.url =
        "/ins_ajax.php?get_file=pages/print&header=true&id=" + options.id;
    if (ins(options.datatype)._isExists()) {
        option.url += "&datatype=" + options.datatype;
    }
    if (ins(options.dataid)._isExists()) {
        option.url += "&dataid=" + options.dataid;
    }
    if (ins(options.xref)._isExists()) {
        option.url += "&xref=" + options.xref;
    }
    if (ins(options.xref_field)._isExists()) {
        option.url += "&xref_field=" + options.xref_field;
    }
    ins()._ui._ins_lightbox(option);
};
UI.prototype._update = function() {
    var ui = this;
    ins(".ins_tiny_editor .ins_tiny_editor_body")._each(function(e) {
        var t = e._parent()._find(".ins_tiny_editor_textarea");
        e._setHTML(t._getValue());
        ins("ins_plg_code_editor")._plgin({ "name": "_111" });
    });
    ins(".jsaction,.ins_jsaction,.insaction")
        ._get()
        .forEach(function(e) {
            if (!updated.includes(e)) {
                updated.push(e);
                var m = ins(e);
                if (ins(m._getData("insaction"))._isExists()) {
                    ui._updateObject(m, "insaction");
                }
                var events = ["click", "change", "mouseover", "mouseout", "keydown", "focus", "submit", "mousedown", "mouseup", "mousemove", "dblclick"];
                events.forEach(function(e) {
                    if (ins(m._getData("ins" + e))._isExists()) {
                        m._on(e, function(o) {
                            ui._updateObject(o, "ins" + e);
                        })
                    }
                })
            }
        });
};
UI.prototype._updateObject = function(obj, act = "insclick") {
    var ex = obj._getData(act).split(",");
    ex.forEach(function(e) {
        updateui(obj, e);
    });
};
UI.prototype._order = function(options) {
    var t = ins(this.o)._get(0);
    for (var i = 0; i < t.childNodes.length; i++) {
        ins(t.childNodes[i])._darg({
            ondragstart: function(o, ev) {
                var id = "drag-" + new Date().getTime();
                o._setAttribute("id", id);
                ev.dataTransfer.setData("text", id);
            },
            hander: options.hander,
        });
        ins(t.childNodes[i])._drop({
            ondrop: function(drop_object, ev) {
                var drag_object = ins("#" + ev.dataTransfer.getData("text"))._get(0);
                ins(drop_object)._append_befor(drag_object);
                if (ins(options.ondone)._isExists()) {
                    options.ondone(drop_object, drag_object);
                }
            },
        });
    }
};
//<editor-fold defaultstate="collapsed" desc="create">
UI.prototype._get = function(tags, parent, parent_attrs) {
    var r = [];
    for (var k in tags) {
        var t = tags[k];
        var a = this._create(t.name, t.data, t.attrs, t.child);
        if (t.event !== null) {
            ins(a)._event(t.event[0], t.event[1]);
        }
        r.push(a);
    }
    if (parent === null) {
        parent = "div";
    }
    return this._create(parent, null, parent_attrs, r);
};
UI.prototype._render = function(callback) {
    var options = {};
    options["data"] = JSON.stringify(this.o);
    options["get_file"] = "inputs/ui";
    options["lang"] = ins()._map._lang();
    ins()._ajax._send("/ins_ajax.php", options, "POST", callback);
}
UI.prototype._create = function(tag, text, attrs, child) {
    var o = document.createElement(tag);
    for (var k in attrs) {
        o.setAttribute(k, attrs[k]);
    }
    if (!ins(child)._isEmpty()) {
        if (Array.isArray(child)) {
            child.forEach(function(c) {
                if (c != null) {
                    o.appendChild(c);
                }
            });
        } else if (typeof child === "object") {
            o.appendChild(child);
        } else if (typeof child === "string") {
            o.innerHTML = child;
            //o.appendChild(t);
        }
    }
    if (!ins(text)._isEmpty()) {
        if (Array.isArray(text)) {
            text.forEach(function(c) {
                if (c != null) {
                    o.appendChild(c);
                }
            });
        } else if (typeof text === "object") {
            o.appendChild(text);
        } else if (typeof text === "string") {
            //  var t = document.createTextNode(text);
            var t = document.createElement("div");
            t.innerHTML = text;
            o.appendChild(t);
        }
    }
    return o;
};
UI.prototype._createNS = function(name, child = "", attrs) {
    var o = document.createElementNS("http://www.w3.org/2000/svg", name);
    for (var k in attrs) {
        o.setAttribute(k, attrs[k]);
    }
    if (!ins(child)._isEmpty()) {
        if (Array.isArray(child)) {
            child.forEach(function(c) {
                if (c != null) {
                    o.appendChild(c);
                }
            });
        } else if (typeof child === "object") {
            o.appendChild(child);
        } else if (typeof child === "string") {
            o.innerHTML = child;
        }
    }
    return o;
};
/*
 *
 * @param {type} tag
 * @param {type} text
 * @param {type} attrs
 * @param {type} child
 * @returns {UI.prototype._create.o|Element}
 *
 *
 * 
 */
UI.prototype._create = function(tag, text, attrs, child) {
    var o = document.createElement(tag);
    for (var k in attrs) {
        o.setAttribute(k, attrs[k]);
    }
    if (!ins(child)._isEmpty()) {
        if (Array.isArray(child)) {
            child.forEach(function(c) {
                if (c != null) {
                    o.appendChild(c);
                }
            });
        } else if (typeof child === "object") {
            o.appendChild(child);
        } else if (typeof child === "string") {
            o.innerHTML = child;
            //o.appendChild(t);
        }
    }
    if (!ins(text)._isEmpty()) {
        if (Array.isArray(text)) {
            text.forEach(function(c) {
                if (c != null) {
                    o.appendChild(c);
                }
            });
        } else if (typeof text === "object") {
            o.appendChild(text);
        } else if (typeof text === "string") {
            //  var t = document.createTextNode(text);
            var t = document.createElement("div");
            t.innerHTML = text;
            o.appendChild(t);
        }
    }
    return o;
};
//</editor-fold>
//<editor-fold defaultstate="collapsed" desc="objects">
/**
 *
 * @param {type} title
 * @param {type} data
 * @param {type} url
 * @param {type} style
 * @param {type} addclass
 * @returns {undefined}
 */
/**
 *
 * @param {type} title
 * @param {type} data
 * @param {type} url
 * @param {type} style
 * @param {type} addclass
 * @returns {undefined}
 */
//
/**
 *
 * @param {type} options {to, select_text, select_value, select_type, select_table}
 * @returns {Ajax.prototype._send.xhttp|XMLHttpRequest}
 */
UI.prototype._fill_select = function(options) {
    options.root = "true";
    options.get_file = "/ins_ajax/pages/get_combo_options";
    return ins()._ajax._send("/ins_ajax.php", options, "POST", function(d) {
        ins(options.to)._setHTML(d);
        if (ins(options.onfill)._isExists()) {
            options.onfill();
        }
    });
};
/**
 *
 * @param {Json} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
UI.prototype._ins_lightbox = function(options, onreday) {
    options.checkIgnore = true;
    return ins("ins_plg_lightbox")._plgin(options, onreday);
};
UI.prototype._addLightbox = function(options, onreday) {
    options.checkIgnore = true;
    return ins("ins_plg_lightbox")._plgin(options, onreday);
};
UI.prototype._removeLightbox = function() {
    var addclass = "";
    if (ins(this.o)._isExists()) {
        addclass = this.o;
    }
    ins(".ins_lightbox" + addclass + ",.ins-lightbox" + addclass)._remove();
};

UI.prototype._removeLightPanel = function() {
    var addclass = "";
    if (ins(this.o)._isExists()) {
        addclass = this.o;
    }
    ins(".ins-panel-overlay" + addclass + ",.ins-panel-overlay" + addclass)._remove();
};


/**
 *
 * @param {type} options [area ,callback]
 * @returns {undefined}
 */
UI.prototype._create_image = function(options) {
    ins("/ins_lib/js/lib/html2canvas.min.js")._onload(function() {
        window.scrollTo(0, 0);
        html2canvas(document.querySelector(options.area)).then(function(canvas) {
            var base64URL = canvas
                .toDataURL("image/jpeg")
                .replace("image/jpeg", "image/octet-stream");
            options.get_file = "/ins_ajax/eng/screenshot";
            options.image = base64URL;
            options.root = "true";
            ins()._ajax._post({
                url: "/ins_ajax.php",
                options: options,
                onprogress: options.onprogress,
                callback: function(d) {
                    options.callback(d);
                },
            });
        });
    });
};
UI.prototype._ui_create_image = function(t) {
    var o = ins(t);
    var area = "";
    if (ins(this.o)._isExists()) {
        area = this.o;
    } else if (ins(o._getData("area"))._isExists()) {
        area = o._getData("area");
    }
    if (!ins(area)._isEmpty()) {
        ins()._ui._create_image({
            area: area,
            onprogress: function(p) {
                if (ins(o._getData("onprogress"))._isExists()) {
                    ins(o._getData("onprogress"))._setCSS({ width: p + "%" });
                    if (p == 100) {
                        ins(o._getData("onprogress"))._setCSS({ width: "0%" });
                    }
                }
            },
            callback: function(jdata) {
                var data = JSON.parse(jdata.trim());
                if (ins(o._getData("callback"))._isExists()) {
                    window[o._getData("callback")](data, o);
                } else {
                    window.open(data.url, "_blank");
                }
            },
        });
    }
};
/**
 *
 * @param {type} options [area ,callback]
 * @returns {undefined}
 */
UI.prototype._ui_create_pdf = function(t) {
    var o = ins(t);
    var options = o._getData();
    if (ins(this.o)._isExists()) {
        options.area = this.o;
    } else if (ins(o._getData("area"))._isExists()) {
        options.area = o._getData("area");
    }
    options.onprogress = function(p) {
        if (ins(o._getData("onprogress"))._isExists()) {
            ins(o._getData("onprogress"))._setCSS({ width: p + "%" });
            if (p == 100) {
                ins(o._getData("onprogress"))._setCSS({ width: "0%" });
            }
        }
    };
    options.callback = function(jdata) {
        var data = JSON.parse(jdata.trim());
        if (ins(o._getData("callback"))._isExists()) {
            window[o._getData("callback")](data, o);
        } else {
            window.open(data.url, "_blank");
        }
    };
    ins()._ui._create_pdf(options);
};
/**
 *
 * @param {type} options [area ,callback]
 * @returns {undefined}
 */
UI.prototype._create_pdf = function(options) {
    ins("/ins_lib/js/lib/html2canvas.min.js")._onload(function() {
        var element = document.querySelector(options.area);
        window.scrollTo(0, 0);
        html2canvas(
            element, {
                width: element.scrollWidth,
                height: element.scrollHeight,
            }
        ).then(function(canvas) {
            ins("/ins_lib/js/lib/jspdf.min.js")._onload(function() {
                var imgData = canvas.toDataURL("image/jpeg", 1.0);
                var pdf = new jsPDF("1", "pt", "a4");
                pdf.addImage(imgData, "JPEG", 0, 0, 595.28, 841.89);
                pdf.output("datauristring");
                options.get_file = "/ins_ajax/eng/screenshot";
                options.image = pdf.output("datauristring");
                options.root = "true";
                if (ins(options.filename)._isEmpty()) {
                    options.filename = ins()._data._get_unique_id() + ".pdf";
                }
                ins()._ajax._post({
                    url: "/ins_ajax.php",
                    options: options,
                    onprogress: options.onprogress,
                    callback: function(d) {
                        options.callback(d);
                    },
                });
            });
        });
    });
};
//</editor-fold>
UI.prototype._print = function(t) {
    if (!ins(this.o)._isEmpty()) {
        var area = this.o;
        ins()._ajax._send(
            "/ins_ajax.php", { get_file: "pages/print_area_data" },
            null,
            function(data) {
                var prtContent = document.getElementById(area);
                data += prtContent.innerHTML;
                var WinPrint = window.open(
                    "",
                    "",
                    "left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0"
                );
                WinPrint.document.write(data);
                WinPrint.document.close();
                WinPrint.focus();
                WinPrint.print();
                // WinPrint.close();
            }
        );
    } else {
        window.print();
    }
};
UI.prototype._addButtonLoader = function() {
    var inp = ins(this.o);
    inp._setData('loaderTitle', inp._getHtml());
    inp._setHTML('<i class="lni lni-spinner-solid ins-spin"></i>');
    inp._get(0).disabled = true;
}
UI.prototype._removeButtonLoader = function() {
    var inp = ins(this.o);
    inp._setHTML(inp._getData('loaderTitle'));
    inp._get(0).disabled = false;
}
UI.prototype._addLoader = function(type) {
    var mclass = "";
    if (ins(this.o)._isEmpty()) {
        this.o = "body";
    } else {
        mclass = " ins-full ";
    }
    if (ins(type)._isEmpty()) type = "";
    var i = this._create("i", "", { class: "fas fa-circle-notch fa-spin" });
    var node = this._create(
        "span",
        "", { class: "ins-loader  ins-panel-overlay   ins-opened  " + type + mclass },
        i
    );
    return ins(this.o)._append(node);
}
UI.prototype._removeLoader = function() {
        if (ins(this.o)._isEmpty()) this.o = "body";
        ins(this.o + " .ins-loader")._remove();
    }
    /**
     *
     * @param {type} msg
     * @param {type} type ["success","info","warning","error"] def:info
     * @returns message node
     */
UI.prototype._send_tiny_message = function(
    msg,
    msgclass = "ins-info "
) {
    var ms = msg;
    ins(ms)._ui._notification({
        class: msgclass
    });
};
UI.prototype._message = function(options = {}) {
    options.o = this.o;
    ins("ins_plg_messages")._getPlgin(options, function(cls) {
        cls._out();
    });
};
UI.prototype._notification = function(
    options = {}
) {
    options.o = this.o;
    options.mode = "notification";
    ins("ins_plg_messages")._getPlgin(options, function(cls) {
        cls._out();
    });
};
UI.prototype._note = function(
    options = {}
) {
    options.o = this.o;
    options.mode = "note";
    ins("ins_plg_messages")._getPlgin(options, function(cls) {
        cls._out();
    });
};
UI.prototype._confirm = function(
    options = {}
) {
    options.o = this.o;
    options.mode = "confirm";
    ins("ins_plg_messages")._getPlgin(options, function(cls) {
        cls._out();
    });
};
UI.prototype._alert = function(
    options = {}
) {
    options.o = this.o;
    options.mode = "alert";
    ins("ins_plg_messages")._getPlgin(options, function(cls) {
        cls._out();
    });
};
UI.prototype._page_progress_show = function() {
    ins(".ins-page-progress")._addClass("ins-active");
    ins(".ins-page-progress  .ins-progress-bar ")._setCSS({ width: "0" });
};
UI.prototype._page_progress_hide = function() {
    if (loader_interval != null) {
        clearInterval(loader_interval);
        loader_interval = null;
    }
    ins(".ins-page-progress")._removeClass("ins-active");
    ins(".ins-page-progress  .ins-progress-bar ")._setCSS({ width: "0" });
};
UI.prototype._page_progress = function(v) {
    ins(".ins-page-progress")._addClass("ins-active");
    ins(".ins-page-progress  .ins-progress-bar ")._setCSS({ width: v });
};
var loader_interval;
UI.prototype._page_progress_run = function(v) {
    ins(".ins-page-progress")._addClass("ins-active");
    ins(".ins-page-progress  .ins-progress-bar ")._setCSS({ width: "0" });
    var i = 0;
    loader_interval = setInterval(function() {
        i++;
        if (i == 100) {
            i = 0;
        }
        ins(".ins-page-progress  .ins-progress-bar ")._setCSS({
            width: +i + "%",
        });
    }, 10);
};
//</editor-fold>
//<editor-fold defaultstate="collapsed" desc="Data">
function Data(o) {
    this.o = o;
}
Data.prototype._get = function(w = "") {
    var en = {
        operation_done_msg: "operation done successfully ",
        operation_error_msg: "operation Error ",
        months: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "Novemeber",
            "Decemeber",
        ],
        days: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    };
    var ar = {
        operation_done_msg: "تم العمليه بنجاح  ",
        operation_error_msg: "حدث مشلكله اثناء العمليه ",
        months: [
            "يناير",
            "فبراير",
            "مارس",
            "ابريل",
            "مايو",
            "يونيو",
            "يوليو",
            "أغسطس",
            "سبتمبر",
            "أكتوبر",
            "نوفمبر",
            "ديسمبر",
        ],
        days: [
            "الاحد",
            "الاثنين",
            "الاثنين",
            "الاربعاء",
            "الخميس",
            "الجمعة",
            "السبت",
        ],
    };
    var r = "";
    if (ins("ar")._map._lan) {
        r = ar[w];
    } else {
        r = en[w];
    }
    return r;
};
Data.prototype._interval = function(code, time) {
    setInterval(code, time);
};
var tmr = null;
var itmr = 0;
/**
 * 
 * @param {time,offest,frame,end} ops 
 */
Data.prototype._timer = function(ops) {
    donwTime = ops["time"];
    offest = ops["offest"];
    tmr = setInterval(function() {
        if (donwTime > 0) {
            donwTime -= offest;
            itmr++;
            if (ops["frame"] != null) {
                ops["frame"](itmr, donwTime);
            }
        } else {
            if (tmr != null) {
                clearInterval(tmr);
                tmr = null;
                if (ops["end"] != null) {
                    ops["end"]();
                }
            }
        }
    }, offest * 1000);
};
Data.prototype._settimer = function(time, code) {
    setInterval(code, time);
};
Data.prototype._json_join = function(object1, object2) {
    return Object.assign(object1, object2);
};
/*
Data.prototype._timer = function(options) {
    var t = this;
    options.end = options.end ? options.end : false;
    options.repeat = options.repeat !== undefined ? options.repeat : true;
    options.time = options.time ? options.time : 1000;
    if (!options.end) {
        window.setTimeout(function() {
            options = options.func(options);
            if (options.repeat === true) {
                t._timer(options);
            } else if (options.repeat > 0) {
                options.repeat--;
                t._timer(options);
            }
        }, options.time);
    }
};*/
Data.prototype._date_gettoday = function(time, code) {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();
    if (dd < 10) {
        dd = "0" + dd;
    }
    if (mm < 10) {
        mm = "0" + mm;
    }
    return yyyy + "-" + mm + "-" + dd;
};
Data.prototype._date_offset = function(date, offset, operation = "plus") {
    var d = new Date(date);
    if (operation == "minus") {
        d.setDate(d.getDate() - offset);
    } else {
        d.setDate(d.getDate() + offset);
    }
    var curr_date = d.getDate();
    var curr_month = d.getMonth() + 1;
    var curr_year = d.getFullYear();
    d = curr_year + "-" + curr_month + "-" + curr_date;
    return d;
};
Data.prototype._generatePassword = function(length = 8) {
    var charset =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
};
Data.prototype._page_data = function(page = ".ins_main") {
    try {
        if (ins(page)._isExists(true)) {
            return JSON.parse(ins(page)._getData("data"));
        } else {
            return {};
        }
    } catch (error) {
        return {};
    }
};
Data.prototype._get_page_data = function(page = ".ins_main") {
    try {
        if (ins(page)._isExists(true)) {
            return JSON.parse(ins(page)._getData("data"));
        } else {
            return {};
        }
    } catch (error) {
        return {};
    }
};


Data.prototype._setSession = function(data, done) {
    ins("server/setSession")._plg(data, (a) => {
        done(a)
    });
};


Data.prototype._getSession = function(name, done) {
    ins("server/getSession")._plg({ "name": name }, (a) => {
        done(a)
    });
};



Data.prototype._removeSession = function(name, done) {
    ins("server/removeSession")._plg({ "name": name }, (a) => {
        done(a)
    });
};




Data.prototype._get_unique_id = function(name, done) {
    return "_" + Math.random().toString(36).substr(2, 9);
};
Data.prototype._addtourl = function(url, ...adds) {
    var d = "";
    adds.forEach(function(a) {
        d += "/" + a;
    });

    if (url.indexOf("do") != -1) {
        url += "/";
    } else {
        url += "/do/";
    }
    url += d;
    url = this._replaceAll("///", "/", url);
    url = this._replaceAll("//", "/", url);
    return url;
};
Data.prototype._addtomyurl = function(...adds) {
    var d = "";
    var url = ins(this.o)._getData("url");
    adds.forEach(function(a) {
        d += "/" + a;
    });
    if (url.indexOf("do") != -1) {
        url += "/";
    } else {
        url += "/do/";
    }
    url += d;
    url = this._replaceAll("///", "/", url);
    url = this._replaceAll("//", "/", url);
    return url;
};
Data.prototype._getmainurl = function(page = ".ins_main") {
    return this._get_page_data(page).url;
};
Data.prototype._replaceAll = function(search, replacement, String = null) {
    if (String === null) {
        String = this.o;
    }
    return String.replace(new RegExp(search, "g"), replacement);
};
Data.prototype._exists = function() {
    return !(typeof this.o === "undefined" || this.o === null);
};
Data.prototype._update_variables = function(search, String = null) {
    var t = this;
    if (String === null) {
        String = this.o;
    }
    if (!ins(search)._isEmpty()) {
        Object.keys(search).forEach(function(i) {
            String = t._replaceAll("@{" + i + "}", search[i], String);
        });
    }
    return String;
};
Data.prototype._isExists = function(i = false) {
    if (i === true) {
        return !(
            typeof ins(this.o)._get(0) === "undefined" || ins(this.o)._get(0) === null
        );
    } else {
        return !(typeof this.o === "undefined" || this.o === null);
    }
};
Data.prototype._validateEmail = function(email) {
    var re =
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};
Data.prototype._clear_inputs = function() {
    ins(this.o)._insData(function(data) {
        return data._formClear(done);
    });
};
Data.prototype._update_inputs = function(j) {
    ins(this.o)._insData(function(data) {
        return data._formUpdate(j);
    });
};
Data.prototype._fromSubmit = function(done) {
    ins(this.o)._insData(function(data) {
        return data._fromSubmit(done);
    });
};
Data.prototype._submit = function(done, onerror) {
        var data = ins(this.o)._data._get_inputs();
        if (!data.error) {
            delete data.error;
            delete data.error_inputs;
            done(data);
        } else {
            data.error_inputs.forEach(function(a) {
                ins(a)._parents(".ins-form-item")._addClass("ins-from-input-error");
                a.focus();
            });
            if (onerror != null) {
                onerror(data);
            }
        }
    }
    //** ols version */
Data.prototype._get_inputs = function(done) {
    var o = this;
    let options = {};
    options.error = false;
    options.error_inputs = [];
    if (ins(ins(this.o)
            ._find("input,select,textarea"))._isExists()) {
        ins(this.o)
            ._find("input,select,textarea")
            ._each(function(item, indx) {
                let v = item._getValue();
                if (!ins(v)._isEmpty()) {
                    if (
                        item._getAttribute("type") === "checkbox" ||
                        item._getAttribute("type") === "checkbox" ||
                        item._getAttribute("type") === "radio"
                    ) {
                        if (item._get(0).checked) {
                            if (ins(item._getAttribute("name"))._isExists()) {
                                var n = item._getAttribute("name");
                                if (n.search("]") > 0) {
                                    if (ins(options[n])._isExists()) {
                                        v = options[n] + "," + v;
                                    }
                                }
                                options[n] = v;
                            }
                        }
                    } else if (item._getAttribute("type") === "email" && !o._validateEmail(v)) {
                        options.error = true;
                        options.error_inputs.push(ins(item)._get(0));
                    } else {
                        if (ins(item._getAttribute("name"))._isExists()) {
                            var n = item._getAttribute("name");
                            if (n.search("]") > 0) {
                                if (ins(options[n])._isExists()) {
                                    v = options[n] + "," + v;
                                }
                            }
                            options[n] = v;
                        }
                    }
                    if (
                        ins(item._getAttribute("required"))._isExists() &&
                        ins(item._getAttribute("minlength"))._isExists()
                    ) {
                        if (parseInt(item._getAttribute("minlength")) > v.length) {
                            options.error = true;
                            options.error_inputs.push(ins(item)._get(0));
                        }
                    }
                } else if (
                    ins(item._getAttribute("required"))._isExists() ||
                    ins(item._getAttribute("data-required"))._isExists()
                ) {
                    options.error = true;
                    options.error_inputs.push(ins(item)._get(0));
                }
            });
    }
    return options;
};
Data.prototype._app_settings_get = function(name = "") {
    ins(this.o)._insData(function(data) {
        data._app_settings_get(name);
    });
};
Data.prototype._app_settings_set = function(name, value, ondone) {
    ins(this.o)._insData(function(data) {
        data._app_settings_set(name, value, ondone);
    });
};
//</editor-fold>
//<editor-fold defaultstate="collapsed" desc="Animation">
function Animation(o) {
    this.o = o;
}
Animation.prototype._toggle_css = function(from, to, speed, actclass) {
    ins(this.o)._insAnimation(function(animation) {
        animation._toggle_css(from, to, speed, actclass);
    })
};
Animation.prototype._fadeout = function(callback, speed) {
    ins(this.o)._insAnimation(function(animation) {
        animation._fadeout(from, to, speed, actclass);
    })
};
Animation.prototype._fadein = function(callback, speed) {
    ins(this.o)._insAnimation(function(animation) {
        animation._fadein(from, to, speed, actclass);
    })
};
Animation.prototype._height = function(h, addclass, removeclass, speed) {
    ins(this.o)._insAnimation(function(animation) {
        animation._height(from, to, speed, actclass);
    })
};
//</editor-fold>
//<editor-fold defaultstate="collapsed" desc="Ajax">
if (typeof ins_jax == "undefined") {
    let ins_jax = null;
}

function Ajax(o, callback) {
    this.o = o;
}
Ajax.prototype._send = function(url, options, callback) {
    ins(this.o)._insAjax(function(ajax) {
        ajax._send(url, options, callback);
    })
};
Ajax.prototype._call = function(options, callback) {
    ///ins_ajax/home/ajx_upload/upload_file/do/_t/ajx/
    var url = "/ins_ajax/" + options["_a"] + "/" + options["_p"] + "/" + options["_m"] + "/"


    delete options["_a"];
    delete options["_c"];
    delete options["_m"];
    ins(this.o)._insAjax(function(ajax) {
        ajax._send(url, options, callback);
    })
};
Ajax.prototype._ins_ajax = function(options, callback) {

    var g = ins()._map._data();
    var url = "/ins_ajax/home/" + this.o + "/do/_t/ajx/_area/" + g["_a"] + "/_alias/" + g["_g"]["alias"] + "/"
    delete options["_a"];
    delete options["_c"];
    ins(this.o)._insAjax(function(ajax) {
        ajax._send(url, options, callback);
    })
};
Ajax.prototype._app = function(options, callback) {
    var s = ins(".ins-app")._getData("data")
    var g = ins()._map._data();


    s = JSON.parse(s);
    if (options["_p"] != null) {
        s["_p"] = options["_p"];
    }
    if (options["_a"] != null) {
        s["_a"] = options["_a"];
    }
    if (s["_a"] == "") {
        s["_a"] = "home";
    }
    var url = "/ins_ajax/" + s["_a"] + "/" + s["_p"] + "/" + this.o + "/do/_area/" + g["_a"] + "/_alias/" + g["_g"]["alias"] + "/"
    delete options["_a"];
    delete options["_p"];
    delete options["_m"];
    ins(this.o)._insAjax(function(ajax) {
        ajax._send(url, options, callback);
    })
};
Ajax.prototype._wdgt = function(options, callback) {
    if (options["_a"] == "" || options["_a"] == null) {
        options["_a"] = "home";
    }
    var url = "/ins_ajax/" + options["_a"] + "/" + options["_w"] + "/" + this.o + "/do/_t/wdgt"
    delete options["_a"];
    delete options["_w"];
    delete options["_m"];
    ins(this.o)._insAjax(function(ajax) {
        ajax._send(url, options, callback);
    })
};
Ajax.prototype._abort = function(ajax) {
    ins(this.o)._insAjax(function(ajax) {
        ajax._abort(ajax);
    })
    return this;
};
//</editor-fold>
//<editor-fold defaultstate="collapsed" desc="mian">
/**start_here */
function INS(o) {
    this.o = o;
    this._ui = new UI(o);
    //   this._drawing = new Drawing(o);
    this._ajax = new Ajax(o);
    this._data = new Data(o);
    this._animation = new Animation(o);
    this._map = new InsMap(o);
    this._db = new InsDB(o);
    this._load = function() {
        if (window.addEventListener) {
            // W3C standard
            window.addEventListener("load", this.o, false); // NB **not** 'onload'
        } else if (window.attachEvent) {
            // Microsoft
            window.attachEvent("onload", this.o);
        }
        return this.o;
    };
    this._get = function(n, p) {
        let evo = [];
        if (typeof this.o === "string") {
            if (p) {
                evo = window.parent.document.querySelectorAll(this.o);
            } else {
                evo = document.querySelectorAll(this.o);
            }

        } else if (this.o === document) {
            evo = [document];
        } else {
            if (this.o instanceof NodeList) {
                evo = this.o;
            } else if (this.o instanceof INS) {
                evo = this.o._get();
            } else {
                evo = [this.o];
            }
        }
        if (n != null) {
            if (n == "last") {
                return evo[evo.length - 1];
            } else if (n == "first") {
                return evo[0];
            } else if (n == "count") {
                if (evo != null) {
                    return evo.length;

                } else {

                    return 0;

                }

            } else if (n == "index") {

                var children = evo[0].parentNode.childNodes;


                i = 0;
                for (; i < children.length; i++) {
                    if (children[i] == evo[0]) {
                        return i;
                    }
                }
                return -1;




            } else {
                return evo[n];
            }
        } else {
            return evo;
        }
    };
    this._each = function(fun, end) {
        if (ins(this._get())._isExists()) {
            var count = this._get().length;
            this._get().forEach(function(item, indx) {
                var isend = (indx == (count - 1));
                fun(ins(item), indx, isend);
            });
        }
    };
}
INS.prototype._index = function(num, isparent) {
    return ins(this._get(num, isparent));
};
INS.prototype._plg = function(ops = {}, ondone = (cls) => any) {

    var names = this.o.split("/");
    pname = "ins_plg_" + names[0];
    plg = ins()._check_plgin(pname);
    if (plg == false) {
        ins(pname)._getPlgin(ops, function(cls) {
            cls[names[1]](ops, ondone)
        });
    } else {
        plg[names[1]](ops, ondone)
    }
};
/**
 * @param {function(cls)} callback 
 */
INS.prototype._insAjax = function(callback = (cls) => any) {
    var o = this.o;
    /** @var {ins_plg_ajax} cls  */
    ins("ins_plg_ajax")._getPlgin({ o: this.o }, function(cls) {
        callback(cls);
    });
}
INS.prototype._insAnimation = function(callback = (cls) => any) {
    var o = this.o;
    /** @var {ins_plg_ajax} cls  */
    ins("ins_plg_animation")._getPlgin({ o: this.o }, function(cls) {
        callback(cls);
    });
}
INS.prototype._insData = function(callback = (cls) => any) {
    var o = this.o;
    /** @var {ins_plg_ajax} cls  */
    ins("ins_plg_data")._getPlgin({ o: this.o }, function(cls) {
        callback(cls);
    });
}
INS.prototype._toggleClass = function(actclass) {
    var o = ins(this.o);
    if (o._hasClass(actclass)) {
        this._removeClass(actclass);
    } else {
        this._addClass(actclass);
    }
};
var fileupdated = [];
INS.prototype.fileLoad = function(callback) {
    var file = this.o;
    if (fileupdated.indexOf(file) >= 0) {
        callback("exsit");
        return null;
    } else {
        var script = document.createElement("script");
        script.src = file;
        script.onload = function(e) {
            callback("done");
            fileupdated.push(file);
        };
        document.head.appendChild(script);
        return ins(script);
    }
};
INS.prototype.filesLoad = function(callback) {
    var r = this.o;
    var file = r[r.length - 1];
    ins(file).fileLoad(function() {
        r.pop();
        if (r.length == 0) {
            callback();
        } else {
            ins(r).filesLoad(callback);
        }
    });
};
INS.prototype._insclude_css = function(callback) {
    var file = this.o;
    if (fileupdated.indexOf(file) >= 0) {
        callback("exsit");
        return null;
    } else {
        var head = document.getElementsByTagName('head')[0];
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = file;
        link.media = 'all';
        fileupdated.push(file);
        head.appendChild(link);
        callback("done");
    }
};
INS.prototype._onload = function(callback) {
    var file = this.o;
    if (fileupdated.indexOf(file) >= 0) {
        callback("exsit");
        return null;
    } else {
        var script = document.createElement("script");
        script.src = file;
        script.onload = function(e) {
            callback("done");
            fileupdated.push(file);
        };
        document.head.appendChild(script);
        return ins(script);
    }
};
INS.prototype._toggle_show = function() {
    if (this._hasClass("ins_hidden")) {
        this._removeClass("ins_hidden");
    } else {
        this._addClass("ins_hidden");
    }
};
INS.prototype._toggle = function(...fns) {
    var i = 0;
    this._on("click", function(obj, event) {
        if (i >= fns.length) {
            i = 0;
        }
        if (!ins(fns[i])._isEmpty()) {
            fns[i](obj, event);
        }
        i++;
    });
};
INS.prototype._chart = function(options, plg) {
    options.o = this.o;
    ins("ins_plg_charts")._plgin(options, plg);
};
INS.prototype._getclasses = function(sp = null, not = []) {
    var r = {};
    this._get().forEach(function(item) {
        if (!ins(item.classList)._isEmpty()) {
            Object.assign(r, item.classList);
            if (sp !== null) {
                var tmp = "";
                Object.keys(r).forEach(function(c) {
                    if (not.indexOf(r[c]) == -1) {
                        tmp += sp + r[c];
                    }
                });
                r = tmp;
            }
        }
    });
    return r;
};
// events 
{
    INS.prototype._darg = function(options) {
        var t = ins(this._get(0));
        if (ins(options.hander)._isExists()) {
            var h = ins(t._find(options.hander));
            h._on(
                "mousedown",
                function() {
                    t._setAttribute("draggable", "true");
                },
                true
            );
            ins(document)._on("mouseup", function() {}, true);
            t._on(
                "dragend",
                function(o, ev) {
                    t._removeAttribute("draggable");
                    if (ins(options.ondragend)._isExists()) {
                        options.ondragend(o, ev);
                    }
                },
                true
            );
        } else {
            t._setAttribute("draggable", "true");
        }
        this._on(
            "dragstart",
            function(o, ev) {
                if (ins(options.ondragstart)._isExists()) {
                    options.ondragstart(o, ev);
                }
            },
            true
        );
    };
    INS.prototype._drop = function(options) {
        var t = this;
        t._event("drop", function(o, ev) {
            ev.preventDefault();
            if (ins(options.ondrop)._isExists()) {
                options.ondrop(o, ev);
            }
        });
        t._event("dragover", function(o, ev) {
            ev.preventDefault();
            if (ins(options.ondragover)._isExists()) {
                options.ondragover(o, ev);
            }
        });
    };
    INS.prototype._document_event = function(event, callback, useCapture) {
        document.addEventListener(
            event,
            function(e) {
                callback(e);
            },
            useCapture
        );
        return this;
    };
    INS.prototype._event = function(event, callback, useCapture) {
        if (ins(useCapture)._isEmpty()) useCapture = false;
        this._get().forEach(function(item, indx) {
            item.addEventListener(
                event,
                (e) => {
                    callback(ins(item), e);
                },
                useCapture
            );
        });
        return this;
    };
    INS.prototype._on = function(event, callback, ps, useCapture) {
        var o = this;
        var os = this.o;
        if (ins(useCapture)._isEmpty()) useCapture = false;
        document.addEventListener(
            event,
            function(e) {
                o._get().forEach(function(item) {
                    if (e.target === item) {
                        callback(ins(e.target), e, item);
                    } else if (ps && ins(ins(e.target)._parents(os).o)._isExists()) {
                        if (ins(e.target)._parents(os)._get(0) === item) {
                            callback(ins(item), e, item);
                        }
                    }
                });
            },
            useCapture
        );
        return this;
    };
}
// other
{
    INS.prototype._isExists = function(i = false) {
        if (i === true) {
            return !(
                typeof ins(this.o)._get(0) === "undefined" || ins(this.o)._get(0) === null
            );
        } else {
            return !(typeof this.o === "undefined" || this.o === null);
        }
    };
    INS.prototype._isEmpty = function() {
        return typeof this.o === "undefined" || this.o === null || this.o === "";
    };
    INS.prototype._isChecked = function() {
        return ins(this.o)._get(0).checked;
    };

    INS.prototype._checked = function() {
        return ins(this.o)._get(0).checked;
    };

}
//attr
{
    INS.prototype._getAttribute = function(type) {
        return this._get(0).getAttribute(type);
    };
    INS.prototype._setAttribute = function(type, value) {
        this._get().forEach(function(item, indx) {
            try {
                item.setAttribute(type, value);
            } catch (err) {}
        });
        return this;
    };
    INS.prototype._removeAttribute = function(type) {
        this._get().forEach(function(item) {
            item.removeAttribute(type);
        });
        return this;
    };
    INS.prototype._hasAttribute = function(type) {
        var attr = this._get(0).getAttribute(type);
        return (!ins(attr)._isEmpty());
    };
}
//Class
{
    INS.prototype._removeClass = function(...removeClass) {
        this._get().forEach(function(item, indx) {
            if (ins(item)._isExists() && !ins(removeClass[0])._isEmpty()) {
                item.classList.remove(...removeClass);
            }
        });
        return this;
    };
    INS.prototype._hasClass = function(value) {
        var r = false;
        this._get().forEach(function(item, indx) {
            if (item.classList.contains(value)) {
                r = true;
            }
        });
        return r;
    };
    INS.prototype._setClass = function(...addClass) {
        this._get().forEach(function(item, indx) {
            if (ins(item)._isExists() && !ins(addClass[0])._isEmpty()) {
                item.classList.add(...addClass);
            }
        });
        return this;
    };
    INS.prototype._getClass = () => {
        var r = false;
        this._get().forEach(function(item, indx) {
            return item.classList
        });
        return r;
    };
    INS.prototype._addClass = function(...addClass) {
        this._get().forEach(function(item, indx) {
            if (ins(item)._isExists() && !ins(addClass[0])._isEmpty()) {
                item.classList.add(...addClass);
            }
        });
        return this;
    };
}
//css
{
    INS.prototype._removeCSS = function(name) {
        var r = false;
        this._get().forEach(function(item) {
            if (item != null) {
                item.style.removeProperty(name);
            }
        });
        return r;
    };
    INS.prototype._getCSS = function(name) {
        var r = "";
        this._get().forEach(function(item) {
            if (Array.isArray(name)) {
                r = {};
                name.forEach(function(n) {
                    if (item.style.getPropertyValue(n) !== "") {
                        r[n] = item.style.getPropertyValue(n);
                    }
                });
            } else {
                r = item.style.getPropertyValue(name);
            }
        });
        return r;
    };
    INS.prototype._setCSS = function(css, value = "") {
        this._get().forEach(function(item) {
            if (value !== "") {
                item.style[css] = value;
            } else {
                for (var name in css) {
                    if (ins(item)._isExists()) {
                        item.style[name] = css[name];
                    }
                }
            }
        });
        return this;
    };
    INS.prototype._hasStyle = function(name) {
        r = false;
        this._get().forEach(function(item) {
            if (item.style.contains(name)) {
                r = true;
            }
        });
        return r;
    };
}
// html
{
    INS.prototype._getMyHtml = function() {
        return this._get(0).outerHTML;
    };
    INS.prototype._getHtml = function() {
        return this._get(0).innerHTML;
    };
    INS.prototype._setHTML = function(value, callback) {
        this._get().forEach(function(item, indx) {
            item.innerHTML = value;
            if (callback != null) {
                callback();
            }
        });
        return this;
    };
    INS.prototype._removeHtml = function(value, callback) {
        this._get().forEach(function(item, indx) {
            item.innerHTML = "";
            if (callback != null) {
                callback();
            }
        });
        return this;
    };
}
// text
{
    INS.prototype._getText = function() {
        return this._get(0).innerText;
    };
    INS.prototype._setText = function(value) {
        this._get().forEach(function(item, indx) {
            item.innerText = value;
        });
        return this;
    };
}
//data
{
    INS.prototype._getData = function(type = "") {
        let r = "";
        if (ins(this._get(0))._isExists()) {
            if (type === "") {
                r = {};
                Object.assign(r, this._get(0).dataset);
            } else {
                r = this._get(0).dataset[type];
            }
        }
        return r;
    };
    INS.prototype._setData = function(type, value) {
        this._get().forEach(function(item, indx) {
            item.dataset[type] = value;
        });
        return this;
    };
    INS.prototype._hasData = function(value) {
        try {
            if (this._get(0) != null) {
                return value in this._get(0).dataset;
            } else {
                return false;
            }
        } catch (err) {
            return false;
        }
    };
}
//value
{
    INS.prototype._getValue = function() {
        var r = null;
        if (ins(this._get()[0])._isExists()) {
            if (ins(this._get(0).getAttribute("multiple"))._isExists()) {
                r = [];
                for (var i = 0; i < this._get(0).options.length; i++) {
                    if (this._get(0).options[i].selected)
                        r.push(this._get(0).options[i].value);
                }
            } else {
                r = this._get()[0].value;
            }
        }
        return r;
    };
    INS.prototype._setValue = function(value) {
        this._get().forEach(function(item, indx) {
            if (ins(item.getAttribute("multiple"))._isExists()) {
                for (var i = 0; i < item.options.length; i++) {
                    if (value.indexOf(item.options[i].value) > -1)
                        item.options[i].selected = true;
                }
            } else {
                item.value = value;
            }
        });
        return this;
    };
    INS.prototype._removeValue = function() {
        this._get().forEach(function(item, indx) {
            if (ins(item.getAttribute("multiple"))._isExists()) {
                for (var i = 0; i < item.options.length; i++) {
                    item.options[i].selected = fales;
                }
            } else {
                item.value = "";
            }
        });
        return this;
    };
    INS.prototype._hasValue = function() {
        var r = null;
        r = this._getValue();
        return (!ins(r)._isEmpty());
    };
}
//object
{
    INS.prototype._p = function(prop, value) {
        var r = [];
        var l = this._get().length;
        this._get().forEach(function(item, indx) {
            if (ins(value)._isEmpty()) {
                if (l === 1) {
                    r = item[prop];
                } else {
                    r.push(item[prop]);
                }
            } else {
                item[prop] = value;
                r.push(value);
            }
        });
        return r;
    };
    INS.prototype._function = function(o) {
        window[this.o](o);
    };
    INS.prototype._remove = function(callback) {
        this._get().forEach(function(item) {
            item.remove(item.selectedIndex);
        });
        if (!ins(callback)._isEmpty()) {
            window[callback](this);
        }
    };
    INS.prototype._focus = function() {
        this._get().forEach(function(item) {
            item.focus();
        });
    };
    INS.prototype._find = function(o) {
        var r = null;
        if (this._get(0) != null) {
            if (this._get(0).querySelectorAll(o).length > 0) {
                r = ins(this._get(0).querySelectorAll(o));
            }
        }
        return r;
    };
    INS.prototype._getchild_bytag = function(tag) {
        var item = null;
        for (var i = 0; i < this._get(0).childNodes.length; i++) {
            if (this._get(0).childNodes[i].tagName === tag) {
                item = ins(this._get(0).childNodes[i]);
                break;
            }
        }
        return item;
    };
    /**
     *
     * @returns {Array[node]}
     */
    INS.prototype._getchildren = function() {
        var r = [];
        for (var i = 0; i < this._get(0).childNodes.length; i++) {
            r[i] = this._get(0).childNodes[i];
        }
        return r;
    };
    INS.prototype._getindex = function(data) {
        var o = this._get(0);
        var p = o.parentElement;
        var r = [];
        for (var i = 0; i < p.childNodes.length; i++) {
            r[i] = p.childNodes[i];
        }
        return r.indexOf(o);
    };
    INS.prototype._is_in_childs = function(target) {
        var r = false;
        if (ins(this._get(0).childNodes)._isExists()) {
            var ch = this._getchilds();
            if (ch.length > 0) {
                for (var i = 0; i < ch.length; i++) {
                    if (!r) {
                        var mo = ch[i];
                        if (mo == target) {
                            r = true;
                            continue;
                        } else {
                            r = ins(mo)._is_in_childs(target);
                            if (r) {
                                continue;
                            }
                        }
                    }
                }
            }
        }
        return r;
    };
    INS.prototype._getchild_byclass = function(classname) {
        var item = null;
        for (var i = 0; i < this._get(0).childNodes.length; i++) {
            if (ins(this._get(0).childNodes[i].classList)._isExists()) {
                if (this._get(0).childNodes[i].classList.contains(classname)) {
                    item = ins(this._get(0).childNodes[i]);
                    break;
                }
            }
        }
        return item;
    };
    INS.prototype._equal = function(o) {
        return this._get(0) === this._getobj(o);
    };
    INS.prototype._parent = function() {
        return ins(this._get(0).parentElement);
    };
    INS.prototype._getparent = function() {
        return ins(this._get(0).parentElement);
    };
    INS.prototype._height = function() {
        return this._get(0).offsetHeight;
    };
    INS.prototype._parents = function(v) {
        var get_item = null;
        if (!ins(v)._isEmpty()) {
            get_item = ins(v)._get();
        }
        var a = this._get(0).parentNode;
        var els = [];
        while (a) {
            els.unshift(a);
            if (get_item != null) {
                get_item.forEach(function(iemt) {
                    if (iemt == a) {
                        els = ins(iemt);
                        a = null;
                    }
                });
            }
            if (a == null) {
                continue;
            } else {
                a = a.parentNode;
            }
        }
        return els;
    };
    INS.prototype._is_parents = function(v) {
        var get_item = null;
        var r = false;
        if (!ins(v)._isEmpty()) {
            get_item = ins(v)._get();
        }
        var a = this._get(0).parentNode;
        var els = [];
        while (a) {
            els.unshift(a);
            if (get_item != null) {
                get_item.forEach(function(iemt) {
                    if (iemt == a) {
                        els = ins(iemt);
                        a = null;
                        r = true;
                        return true;
                    }
                });
            }
            if (a == null) {
                continue;
            } else {
                a = a.parentNode;
            }
        }
        return r;
    };
    /**
     *
     * @param {type} type
     * @returns {r|data|obj|r@call;_get@arr;dataset|String|Date|$}
     */
    INS.prototype._getobj = function(data) {
        if (typeof data === "string") {
            var c = ins()._ui._create("div", "", "", data);
            r = c.children[0];
        } else if (data instanceof INS) {
            r = data._get(0);
        } else {
            r = data;
        }
        return r;
    };
    INS.prototype._clone = function() {
        var r = null;
        if (typeof this.o === "string") {
            var c = ins()._ui._create("div", "", "", this.o);
            r = c.children[0];
        } else if (this.o instanceof INS) {
            r = this.o._get(0).cloneNode(true);
        } else if (ins(this.o)._isExists()) {
            r = this.o.cloneNode(true);
        }
        return ins(r);
    };
    INS.prototype._srcSet = function(name, value) {
        ins(this.o)._each((i) => {
            i._get(0)[name] = value;
        })
        return ins(this.o);
    };
    INS.prototype._append = function(data) {
        var r = this._getobj(data);
        this._get().forEach(function(item, indx) {
            item.appendChild(r);
        });
        return ins(r);
    };

    INS.prototype._appendBefor = function(data) {
        var r = this._getobj(data);
        this._get().forEach(function(item, indx) {
            item.parentNode.insertBefore(r, item);
        });
        return ins(r);
    };

    INS.prototype._append_befor = function(data) {
        var r = this._getobj(data);
        this._get().forEach(function(item, indx) {
            item.parentNode.insertBefore(r, item);
        });
        return ins(r);
    };
    INS.prototype._append_after = function(data) {
        var r = this._getobj(data);
        this._get().forEach(function(item, indx) {
            item.parentNode.insertBefore(r, item.nextSibling);
        });
        return ins(r);
    };
    INS.prototype._show = function() {
        ins(this.o)._removeClass("ins-hidden");
        return ins(this.o);
    };
    INS.prototype._hide = function() {
        ins(this.o)._addClass("ins-hidden");
        return ins(this.o);
    };
}
//page
{
    INS.prototype._setscroll = function(value) {
        this._get().forEach(function(item, indx) {
            item.scrollTop = value;
        });
        return this;
    };
    INS.prototype._reload = function(url = "") {
        if (url != "") {
            window.location = url;
        } else {
            window.location.reload();
        }
    };
}
INS.prototype._o = function(o) {
    this.o = o;
    return this._get();
};
var plg_number = 0;
var plgins = {};
var addplgins = [];
INS.prototype._add_plgin = function(plgin_name, plg) {
    plgins[plgin_name] = plg;
}
INS.prototype._check_plgin = function(plgin_name) {
    if (Object.keys(plgins).includes(plgin_name)) {
        return plgins[plgin_name];
    } else {
        return false;
    }
}
INS.prototype._get_plgins = function(plgin = "") {
    if (plgin == "") {
        return plgins;
    } else {
        return plgins[plgin];
    }
}
INS.prototype._getPlgin = function(Options, onReady) {
    var plg = this.o;
    try {
        if (!(plg in plgins)) {
            var pl = "/ins_web/ins_kit/js/plgins/" + plg + ".js";
            import (pl).then((module) => {
                Object.keys(module).forEach(function(k) {
                    if (k != plg) {
                        window[k] = module[k]
                    }
                })
                if (Options == null) {
                    Options = {};
                }
                var k = ins()._data._get_unique_id();
                plgins[plg] = new module[plg](Options, k);
                if (onReady != null) {
                    onReady(plgins[plg]);
                }
                return plgins[plg];
            });
        } else {
            plgins[plg]["options"] = Options;
            onReady(plgins[plg]);
            return plgins[plg];
        }
    } catch (err) {}
};
INS.prototype._plgin_change = function(Options, onReady) {
    try {
        var plg = this.o;
        var myplgin = plg.trim();
        if (!addplgins.includes(myplgin)) {
            addplgins.push(myplgin);
            var pl = "/ins_web/ins_kit/js/plgins/" + plg + ".js?003";
            import (pl).then((module) => {
                Object.keys(module).forEach(function(k) {
                    if (k != myplgin) {
                        window[k] = module[k]
                    }
                })
                if (Options == null) {
                    Options = {};
                }
                var k = ins()._data._get_unique_id();
                plgins[myplgin] = new module[myplgin](Options, k);
                plgins[myplgin]._change();
                if (onReady != null) {
                    onReady(plgins[myplgin]);
                }
            });
        } else {
            plgins[myplgin]["options"] = Options;
            plgins[myplgin]._change();
        }
    } catch (err) {}
};
INS.prototype._plgin = function(Options, onReady) {
    try {
        var plg = this.o;
        var myplgin = plg.trim();
        if (!addplgins.includes(myplgin)) {
            addplgins.push(myplgin);
            var pl = "/ins_web/ins_kit/js/plgins/" + plg + ".js?003";
            import (pl).then((module) => {
                Object.keys(module).forEach(function(k) {
                    if (k != myplgin) {
                        window[k] = module[k]
                    }
                })
                if (Options == null) {
                    Options = {};
                }
                var k = ins()._data._get_unique_id();
                plgins[myplgin] = new module[myplgin](Options, k);
                plgins[myplgin]._out();
                if (onReady != null) {
                    onReady(plgins[myplgin]);
                }
            });
        } else {
            plgins[myplgin]["options"] = Options;
            plgins[myplgin]._out();
        }
    } catch (err) {}
};
//old version
{
    INS.prototype._readProp = function(prop, ...options) {
        var ps = prop.split(".");
        if (ps.length > 1) {
            if (options == null) {
                ins(this.o)[ps[0]][ps[1]]();
            } else {
                ins(this.o)[ps[0]][ps[1]](...options);
            }
        } else {
            if (options == null) {
                return ins(this.o)[prop]();
            } else {
                return ins(this.o)[prop](...options);
            }
        }
    }
}

function ins(o) {
    return new INS(o);
}
ins(function() {
    ins("ins_plg_run")._plgin({});
    ins()._ui._update();
})._load();