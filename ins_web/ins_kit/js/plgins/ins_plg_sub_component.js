/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_sub_component {
    options = {};

    _id = "";
    constructor(o, id) {
        this._id = id;

        this.options = o;
        this.options.o._setdata("pid", id);
        this.options.o._addclass(id);
        this.options.o._addclass("_sub_component");

    }


    _me() {
        return this.options.o;
    }




    _panel(url) {
        var self = this;
        url += "/get_tmp_index/ins_main/";
        ins()._ajax._send(url, {}, "POST", function(data) {
            var options = {
                data: data,
                class: "_sub_component_light",

                onclose: function() {
                    self._sub_component_updata();
                }
            }
            ins()._ui._ins_lightbox(options);
        });
    }

    _sub_component_updata() {
        var self = this;
        var url = this.options.url + "/get_tmp_index/ins_main/";
        ins()._ajax._send(url, {}, "POST", function(data) {
            self._me()._sethtml(data);

            ins()._ui._update_ui();
            /*
                        var plg = ins()._get_plgins("ins_plg_list");
                        console.log(plg);
                        plg.onUpdate = function() {
                            alert("xxxxx");
                        }*/

        });
    }


    _actions() {
        var self = this;
        ins("." + this._id + " .ins-list-addbtn ,." + this._id + " .ins-list-row-edit ")._on("click", function(e, evo) {
            evo.preventDefault();
            var url = e._getattr("href");
            self._panel(url);
        }, true)


        ins("._sub_component_light form")._on("submit", function(e, o) {
            o.preventDefault();
            var cc = e._data._get_inputs();
            ins()._ajax._to("eng/ins_form", cc, function(data) {

                ins()._ui._lightbox_remove();
                self._sub_component_updata();

            });
        });
    }

    _out() {

        this._sub_component_updata();
        this._actions();



    }
}