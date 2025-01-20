export function showicon(p) {
    var t = p.querySelector("i");
    var _name = ins(".ins-lightbox-data")._getData("name");
    if (ins(".ins-lightbox-data")._getData("mode") || "mode" == "texteditor") {
        var plgins = ins()._get_plgins();
        plgins["ins_plg_texteditor"]._addicon(t.outerHTML);
    } else {
        ins("." + _name + "-input")._setvalue(t.outerHTML);
        ins("." + _name + "-icon")._sethtml(t.outerHTML);
    }
    ins()._ui._lightbox_remove();

}

/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_form_icon {
    options = {};
    _id = "";
    constructor(o = null, id) {
        this.options = o;
        this._id = id;

    }


    _panel(data, name, mode) {

        var options = { "data-name": name };
        if (mode != null) {
            options["data-mode"] = mode;
        }

        ins()._ui._ins_lightbox({
            title: false,
            options: options,
            // onopen: onopen,
            onclose: function() {},
            addto: "body",
            data: data,
            class: "_light_box_" + name,
            style: "width: 80%;height: 80%;max-width: 1000px;min-height: 600px;",
        });
    }



    _out() {
        var t = this;




        t._name = this.options["name"];

        ins("." + t._name + " .ins-form-input-icon")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                t._name = o._getData("name");
                ins(".ins-lightbox")._remove();
                ins()._ajax._to("inputs/icon", { "single": "true" }, function(d) {

                    t._panel(d, t._name, t.options["mode"]);
                });
            },
            true
        );




        ins("." + t._name + " .ins-form-input-clear")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                var _name = o._getData("name");

                ins("." + _name + "-img")._setattr("src", "/ins_images/ins_sys/noimage.png");
                ins("." + _name + "-input")._setvalue("");
            },
            true
        );

    }
}