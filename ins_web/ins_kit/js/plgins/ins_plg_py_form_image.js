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





    _out() {



        var t = this

        var ondone = function(data) {

            var p = t.options.o._parent();
            p._find("input")._setValue(data.path)
            p._find("img")._setAttribute("src", data.fullpath)


        };

        var onend = function(data) {
            // ins(".ins-lightbox." + "_light_box_" + _name)._remove();
            //  t._order(_name);

        };

        var path = "/"
            // if (t._upload_plg == null) {
        var options = {
            o: t.options.o,
            ondone: ondone,
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


        ins("ins_plg_py_upload")._plgin(options,
            function(plg) {
                t._upload_plg = plg;
            }
        );
        /*} else {
            t._upload_plg.options["dir"] = path;
            t._upload_plg.options["ondone"] = ondone
        }*/




    }

}