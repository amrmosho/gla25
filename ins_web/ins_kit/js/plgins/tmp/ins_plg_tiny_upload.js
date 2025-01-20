/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_tiny_upload {
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
            class: "_light_box_" + name + " ins-form-image-upload",
            style: style,
        });
    }
    _name = "";
    _upload_plg = null;


    _upload(_name) {
        var t = this;

        var ondone = function(data) {

            ins("." + _name + "-link")._setattr("href", "/" + data["filepath"]);
            ins("." + _name + "-del-btns")._removeclass("ins-hidden");
            ins("." + _name + "-upload-btns")._addclass("ins-hidden");
            ins("." + _name + "-input")._setvalue(data["name"]);

        };



        if (t._upload_plg == null) {
            ins("ins_plg_upload")._plgin({
                    o: ".ins_upload_file",
                    file_info: ".ins-uploader-file-info",
                    "drop_area": ".ins-uploader-file-drop_area",
                    ondone: ondone,
                    dir: "ins_upload/",
                },
                function(plg) {

                    t._upload_plg = plg;
                }
            );
        } else {
            t._upload_plg.options["dir"] = path;
            t._upload_plg.options["ondone"] = ondone

        }
    }



    _out() {
        var t = this;
        t._name = this.options["name"];
        t._upload(t._name);


        ins("." + t._name + "-delete-btn")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                var _name = o._getData("name");

                ins("." + _name + "-upload-btns")._removeclass("ins-hidden");
                ins("." + _name + "-file-info")._addclass("ins-hidden");
                ins("." + _name + "-input")._setvalue("");
                ins("." + _name + " .ins-uploader-file-info-item")._remove();





            },
            true
        );

    }
}