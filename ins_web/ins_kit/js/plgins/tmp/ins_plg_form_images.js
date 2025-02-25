/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_form_images {
    options = {};
    _id = "";
    constructor(o = null, id) {
        this.options = o;
        this._id = id;
    }
    _panel(data, name, onopen, style = "width: 60%;height: 350px;max-width: 500px; ") {
        ins()._ui._ins_lightbox({
            title: false,
            options: { "data-name": name },
            onopen: onopen,
            onclose: function() {},
            addto: "body",
            data: data,
            class: "_light_box_" + name + " ins-form-image-upload ",
            style: style,
        });
    }
    _name = "";
    _upload_plg = null;
    _getfile_plg = null;
    _browser_plg = null;

    _addToinput(_name, value, path) {
        var v = ins("." + _name + "-input")._getValue();
        try {
            var jv = JSON.parse(v);
        } catch (err) {
            var jv = [];
        }


        path = path.replace("//", "");
        jv.push({ "name": value, "path": path });
        ins("." + _name + "-input")._setvalue(JSON.stringify(jv));
    }

    _updateInput(_name) {

        var mData = [];
        ins("." + _name + "-images-area img")._each(function(o) {
            var mi = { "path": o._getData("path"), "name": o._getData("name") };
            mData.push(mi);
        })
        ins("." + _name + "-input")._setvalue(JSON.stringify(mData));

    }



    _removeFrominput(_name, value) {
        var v = ins("." + _name + "-input")._getValue();
        if (v == "") {
            var jv = [];
        } else {
            var jv = JSON.parse(v);
        }
        jv.forEach(function(item, index, object) {
            if (item["name"] == value) {
                object.splice(index, 1);
            }
        });
        ins("." + _name + "-input")._setvalue(JSON.stringify(jv));
    }

    _addToImages(_name, value, path, inner_path) {
        var h = "<div title='" + _name + "'  style='    height: 120px;'  class='ins-col-3 ins-padding-l ins-flex-center ins-card '>" +
            "<span data-value='" + value + "' data-name='" + _name + "' class='ins-form-images-remove ins-button-text-danger  ins-radius-s  ins-avatar-s' style='position: absolute;bottom: 2px;right: 5px;'>" +
            "<i class='lni lni-trash-can'></i></span>" +
            "<a href='" + path + "' target='_blnak'  class='ins-button-text  ins-radius-s  ins-avatar-s' style='position: absolute;bottom: 2px;   right: 33px;'>" +
            "<i class='lni lni-link'></i></a>" +

            "<a class='ins-form-images-remove ins-button-text-danger  ins-radius-s  ins-avatar-s' style='position: absolute;bottom: 2px;   right: 61px;'>" +
            "<i class='lni lni-move'></i></a>" +

            " <img data-path ='" + inner_path + "' data-name ='" + value + "'  class='ins-radius-m' style='max-width:100%;max-height: 100% ;' src='" + path + "' />" +
            "</div>";
        var p = ins("." + _name + "-images-area")._parent();
        p._find(".ins-icon")._addclass("ins-hidden");
        ins("." + _name + "-images-area")._append(h);




        return h;
    }

    _order(_name) {
        var t = this;
        ins("." + _name + "-images-area")._ui._order({
            "ondone": function() {
                t._updateInput(_name);
            }
        })
    }


    _upload(path, innerpath, _name) {
        var t = this;
        var ondone = function(data) {


            t._addToinput(_name, data["name"], innerpath + "/" + data["name"]);
            t._addToImages(_name, data["name"], data["filepath"], innerpath + "/" + data["name"]);
        };

        var onend = function(data) {
            ins(".ins-lightbox." + "_light_box_" + _name)._remove();
            t._order(_name);

        };
        var c = ins()._get_plgins();

        console.log();



        if (c["ins_plg_upload"] == null) {

            var ops = {
                o: ".ins_upload_file",
                file_info: ".ins-uploader-file-info",
                "drop_area": ".ins-uploader-file-drop_area",
                ondone: ondone,
                onend: onend,
                dir: path,
            }

            if (t.options["o"]._getData("exts") != null) {

                ops["exts"] = t.options["o"]._getData("exts");
            }

            ins("ins_plg_upload")._plgin(ops,
                function(plg) {}
            );
        } else {
            c["ins_plg_upload"].options["dir"] = path;
            c["ins_plg_upload"].options["ondone"] = ondone
            c["ins_plg_upload"].options["onend"] = onend;
        }
    }
    _update(_name, dir) {
        var t = this;
        try {
            if (ins("." + _name + "-input")._isExists(true)) {
                var v = ins("." + _name + "-input")._getValue();
                if (v != "") {
                    var jv = JSON.parse(v);
                    jv.forEach(function(item, index, object) {
                        t._addToImages(_name, item["name"], dir + "/" + item["path"], item["path"]);



                    });
                    t._order(_name);

                }
            }
        } catch (err) {}
    }
    _out() {


        var t = this;
        t._name = this.options["name"];
        var uploadPath = ins("." + t._name + " .ins-form-input-upload")._getData("path");
        t._update(t._name, uploadPath);
        ins("." + t._name + " .ins-form-images-remove")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                t._name = o._getData("name");
                t._removeFrominput(t._name, o._getData("value"));
                o._parent()._remove();

                var c = ins("." + t._name + " .ins-form-images-remove")._get().length;
                if (c == 0) {
                    var p = ins("." + t._name + "-images-area")._parent();
                    p._find(".ins-icon")._removeClass("ins-hidden");
                }

            },
            true
        );
        ins("." + t._name + " .ins-form-images-browser")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                var ondone = function(file, path) {


                    t._name = o._getData("name");
                    var path = path.replace("//", "/");
                    var file = o._getData("innerpath") + "/" + file.replace("//", "/");


                    t._addToinput(t._name, ins()._data._get_unique_id(), file);
                    t._addToImages(t._name, ins()._data._get_unique_id(), path, file);
                    t._order(t._name);

                };
                if (t._browser_plg == null) {
                    ins("ins_plg_file_browser")._plgin({
                            o: o,
                            "data-path": o._getData("path"),
                            "ondone": ondone
                        },
                        function(plg) {
                            t._browser_plg = plg;
                            t._browser_plg._open(o);

                        }

                    );
                } else {
                    t._browser_plg.options["dir"] = o._getData("path");
                    t._browser_plg.options["ondone"] = ondone;
                }
            },
            true
        );
        ins("." + t._name + " .ins-form-input-upload")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                t._name = o._getData("name");
                t._upload(o._getData("path") + o._getData("innerpath"), o._getData("innerpath"), t._name);
                ins()._ajax._to("inputs/upload", {}, function(d) {
                    t._panel(d, t._name);
                });
            },
            true
        );
    }
}