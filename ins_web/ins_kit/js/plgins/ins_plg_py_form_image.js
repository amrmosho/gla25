/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_form_image {
    options = {};
    constructor(o = null, id) {
        this.options = o;
        this._id = id;
    }
    actions(ds) {
        if (ds["p"] != "") {
            var imgs = "<div data-p='" + ds[0].path + "' class='-img-cont ins-flex-center'><div class='lni lni-xmark  ins-rounded ins-danger    ins-button-text -img-remove'></div>" +
                "<a target='_blank'  href='" + ds[0].fullpath + "' class='lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link'></a>  <img src='" + ds[0].fullpath + "' /></div>";
            var paths = ds[0].path;
            ins(ds["p"])._find("input")._setValue(paths)
            ins(ds["p"])._find(".ins-form-upload-imgs")._setHTML(imgs)
        }
    }




    m_actions(ds) {
        var data = ds;
        if (ds["p"] != "") {
            var paths = "";
            var sp = "";
            data.forEach(element => {
                if (element != "") {
                    var imgs = "<div class='-img-cont'> <i  data-p='" + element.path + "' class='lni lni-xmark  ins-rounded ins-danger  ins-button-text -remove-img'></i> <img src='" + element.fullpath + "' /></div>";
                    var imgs = "<div data-p='" + element.path + "'  draggable= 'true' class='-img-cont ins-flex-center'>" +
                        "<div  class='lni lni-menu-meatballs-1  ins-rounded ins-dark -img-darg'></div>" +
                        "<div class='lni lni-xmark  ins-rounded ins-danger ins-button-text -img-remove'></div>" +
                        "<a target='_blank'  href='" + element.fullpath + "' class='lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link'></a>" +
                        "<img src='" + element.fullpath + "' /></div>";
                    ins(ds["p"])._find(".ins-form-upload-imgs")._append(imgs)
                    paths += sp + element.path;
                    sp = ",";
                }
            });
            ins(ds["p"])._find("input")._setValue(paths)
        }
    }
    reval(p) {
        var sp = "";
        var paths = "";
        ins("." + p + " .-img-remove ")._each((i) => {
            paths += sp + i._getData("p");
            sp = ",";
        })
        ins("." + p)._find("input")._setValue(paths)
    }
    imgs_actions() {
        var t = this;
        ins(".ins-form-upload-cont .-img-remove ")._on("click", (o) => {
            var p = o._parents(".ins-form-upload-imgs-cont")._getData("id");
            o._parent()._remove()
            t.reval(p)
        }, true)




        ins(".-img-cont")._on(
            "dragstart", (o, ev) => {
                var id = "drag-" + new Date().getTime();
                o._setAttribute("id", id);
                o._addClass("-img-drag");
                ev.dataTransfer.setData("text", id);
            })
        ins(".-img-cont")._on("dragover", (drop_object, ev) => {
            ev.preventDefault()
        })
        ins(".-img-cont")._on("drop", (o, ev) => {
            ev.preventDefault()
            var drag_object = ins("#" + ev.dataTransfer.getData("text"));
            drag_object._removeClass("-img-drag");
            ins(o)._appendBefor(drag_object);
            var p = drag_object._parents(".ins-form-upload-imgs-cont")._getData("id");
            t.reval(p);
        })
        ins(".-img-cont")._on(
            "dragleave",
            function(o, ev) {
                ev.preventDefault();
                ins(".-img-drop-hover")._removeClass("-img-drop-hover")
            }
        );
        ins(".-img-cont")._on(
            "dragenter",
            function(o, ev) {
                ev.preventDefault()
                ins(".-img-drop-hover")._removeClass("-img-drop-hover")
                o._addClass("-img-drop-hover")
            },
        );
        ins(".-img-cont")._on(
            "dragend",
            function(o, ev) {
                ev.preventDefault()
                ins(".-img-drop-hover")._removeClass("-img-drop-hover")
                ins(".-img-drag")._removeClass("-img-drag")
            },
        );
    }



    _out() {
        var t = this
        t.imgs_actions();
        var ondone = function(ds) {
            if (ds["mode"] != null && ds["mode"] == "multi") {
                t.m_actions(ds);
            } else {
                t.actions(ds)
            }
        };
        var path = "/"
        var options = {
            o: t.options.o,
            onend: ondone,
            dir: path
        };
        if (t.options.o._getData("_dir") != null) {
            options.dir = t.options.o._getData("_dir");
        }
        if (t.options.o._getData("_exts") != null) {
            options.exts = t.options.o._getData("_exts");
        }
        if (t.options.o._getData("_size") != null) {
            options.size = t.options.o._getData("_size");
        }
        this.options.o._on("click", (o) => {
            if (t.options.o._getData("mode") != null) {
                options.mode = t.options.o._getData("mode");
            }
            options._p = "." + o._getData("p");
            ins("ins_plg_py_upload")._plgin(options,
                function(plg) {}
            );
        })
    }
}