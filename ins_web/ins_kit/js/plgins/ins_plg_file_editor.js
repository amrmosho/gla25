/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_file_editor {
    options = {};

    p;
    constructor(o) {
        this.options = o;
    }

    _file = 'ins_admin/ins_coms/com_settings/sys_files_manger/properties.json';

    _ajax(options, ondata) {
        options.file = this._file
        ins()._ui._page_progress_run();
        ins()._ajax._to("inputs/editor_file", options, ondata);
    }


    _update() {
        var self = this;
        this._ajax({ "status": "get" }, function(d) {
            self.p.editor.setValue(d);
        })


    }



    _actions() {
        var self = this;
        ins(".ins-set-data")._on("click", function(o) {
            var d = {
                "status": "set",
                "data": self.p.editor.getValue()

            };
            self._ajax(d, function(a) {
                ins()._ui._send_tiny_message();
                ins()._ui._page_progress_hide();

            })
        })


        ins(".ins-set-data")._on("click", function(o) {
            self._update();
        })




    }
    _ui() {
        var self = this;

        var ui = { "status": "ui" };
        this._ajax(ui, function(odata) {
            self.options.o._sethtml(odata, function() {
                ins("ins_plg_code_editor")._plgin({ "name": "_111" }, function(plgin) {

                    self.p = plgin;
                });
            });
        })

    }

    _out() {
        this._actions();

        this._ui();

    }
}