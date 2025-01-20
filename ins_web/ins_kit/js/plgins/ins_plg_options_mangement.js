/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_options_mangement {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _update(status = "", data = "") {
        var ops = { options: this._options_id, status: status, data: data, mode: this._options_mode };


        var self = this;


        ins()._ui._page_progress_show();
        ins()._ajax._to("inputs/options", ops, function(data) {
            ins(".ins-lightbox-data")._sethtml(data);
            ins()._ui._page_progress_hide();
            ins()._ui._send_tiny_message("Updated");

            ins(".-options-rows")._ui._order({
                "ondone": function() {
                    self._updateTodata();

                }
            });
        });
    }
    _updateData() {
        var self = this;
        var data = {};


        var len = ins(".-options-row")._get();

        len = len.length;



        ins(".ins-lightbox-data .-options-row")._each(function(o, i) {
            var g = ins(o)._data._get_inputs();
            delete g.error;
            delete g.error_inputs;
            var k = g.key;

            if (self._options_mode == "single") {

                delete g.key;
                data[k] = g.value;


            } else {
                data[k] = g;
            }
        });

        self._update("update", JSON.stringify(data));
    }

    _options_mode = "";
    _options_id = "";

    _updateTodata() {
        this._options_mode = ins(".-options-rows-update")._getData("options_mode");
        this._options_id = ins(".-options-rows-update")._getData("options");

        this._updateData();

    }


    _out() {

        var self = this;



        ins(".-options-rows-add")._on("click", (o) => {
            self._options_mode = o._getData("options_mode");
            self._options_id = o._getData("options");


            self._update("add");
        }, true)
        ins(".-options-row-delete")._on("click", (o) => {

            self._options_mode = o._getData("options_mode");
            self._options_id = o._getData("options");


            self._update("delete", o._getData("key"));
        }, true);





        ins(".-options-rows-update")._on("click", (o) => {
            self._updateTodata();
        }, true);


        var lbstyle = "";
        var lbclass = "";
        if (this.options.o._hasData("lightbox_style")) {
            lbstyle = this.options.o._getData("lightbox_style");
        }
        if (this.options.o._hasData("lightbox_class")) {
            lbclass = this.options.o._getData("lightbox_class");
        }
        this.options.o._on("click", (o) => {



            if (this.options.o._hasData("options_mode")) {
                self._options_mode = o._getData("options_mode");
            } else {

                self._options_mode = "normal";

            }
            self._options_id = o._getData("options");



            var ops = { options: self._options_id, status: "", data: "", mode: self._options_mode };

            ins()._ui._page_progress_show();
            ins()._ajax._to("inputs/options", ops, function(data) {
                ins(".ins-lightbox-data")._sethtml(data);



                ins()._ui._ins_lightbox({
                    title: "Options",
                    data: data,

                    onclose: function() {
                        self.options.onUpdate();



                    },
                    class: lbclass,
                    style: lbstyle,
                });




                ins()._ui._page_progress_hide();

                self._update();


            });




        })
    }
}