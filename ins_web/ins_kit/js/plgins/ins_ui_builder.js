/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_ui_builder {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _code = ".ins_editor_ins_code";
    _obj = ".ins_editor_ins_stage  >.ins_editor_ui_contner";

    _ajax(options, ondone) {
        ins("_ins_editor_code_update")._ajax._class(options, ondone);
    }
    _update_js_code(code) {
        var a = JSON.parse(code);
        var code = JSON.stringify(a, 0, 4).trim();
        return code;
    }
    _update_code_fomart() {
        var self = this;
        var u = self._update_js_code(ins(this._code)._getvalue());
        ins(self._code)._setvalue(
            self._update_js_code(ins(self._code)._getvalue())
        );
        var ins_code_texteditor = ins()._get_plgins("ins_plg_code_editor");
        if (ins_code_texteditor != null) {
            ins_code_texteditor.editor.setValue(u);



        }
    }

    _all_update_to_stage() {
        ins()._ui._page_progress_run();

        var o = {
            ins_code: ins(".ins_editor_ins_code")._getvalue(),
            action: "update",
        };

        var slef = this;

        this._ajax(o, function(data) {
            ins(".ins_editor_ins_stage")._sethtml(data);
            ins()._ui._update_ui();
            ins()._ui._send_tiny_message();
            ins()._ui._page_progress_hide();
            slef._update_code_fomart();

        });
    }



    _all_send_data(o) {

        ins()._ui._page_progress_run();

        var options = o._getData();


        options["ins_code"] = ins(".ins_editor_ins_code")._getvalue();
        options["action"] = "update";


        ins()._ajax._to(o._getData("to"), options, function(data) {

            ins()._ui._update_ui();
            ins()._ui._send_tiny_message();
            ins()._ui._page_progress_hide();
        });




    }

    _all_save_data() {

        ins()._ui._page_progress_run();

        var o = {
            ins_code: ins(".ins_editor_ins_code")._getvalue(),
            action: "save",
        };
        this._ajax(o, function(data) {
            ins(".ins_editor_ins_stage")._sethtml(data);
            ins()._ui._update_ui();
            ins()._ui._send_tiny_message();
            ins()._ui._page_progress_hide();

        });
    }






    _all_dwonload_data() {

        ins()._ui._page_progress_run();

        var o = {
            ins_code: ins(".ins_editor_ins_code")._getvalue(),
            action: "dwonload",
        };

        this._ajax(o, function(data) {
            window.location.href = "/ins_export.php?name=" + data;


            ins()._ui._send_tiny_message();
            ins()._ui._page_progress_hide();

        });
    }





    _ui_actions() {
        ins(".ins_toolbar_btn_half")._on("click", function(o, event) {

            ins(".ins_toolbar_btn_fullscreen")._removeclass("ins-active");
            ins(".ins_editor_panel")._removeclass("ins-fixpanel-fullscreen")


            if (ins(".ins_editor_ui")._hasclass("ins-fixpanel-halfscreen")) {
                ins(".ins_editor_ui")._removeclass("ins-fixpanel-halfscreen");
                o._removeclass("ins-active");

            } else {
                ins(".ins_editor_ui")._addclass("ins-fixpanel-halfscreen")
                o._addclass("ins-active");
            }

        }, true);

        ins(".ins_toolbar_btn_fullscreen")._on("click", function(o, event) {


            ins(".ins_toolbar_btn_half")._removeclass("ins-active");
            ins(".ins_editor_ui")._removeclass("ins-fixpanel-halfscreen");


            if (ins(".ins_editor_panel")._hasclass("ins-fixpanel-fullscreen")) {
                ins(".ins_editor_panel")._removeclass("ins-fixpanel-fullscreen")
                o._removeclass("ins-active");

            } else {
                ins(".ins_editor_panel")._addclass("ins-fixpanel-fullscreen")
                o._addclass("ins-active");
            }

        }, true);


    }



    _code_actions() {
        var slef = this;

        ins(".ins_toolbar_btn_format_code")._on("click", function(o, event) {
            slef._update_code_fomart();
        }, true);

        ins(".ins_toolbar_btn_dwonload")._on("click", function(o, event) {

            slef._all_dwonload_data();

        }, true);
        ins(".ins_toolbar_btn_update")._on(
            "click",
            function() {
                slef._all_update_to_stage();
            },
            true
        );

        ins("*")._on("keydown", function(o, event) {
            if (event.ctrlKey && event.keyCode == 120) {
                slef._all_update_to_stage();
            }
        });



        ins(".ins_toolbar_btn_save")._on(
            "click",
            function() {
                slef._all_save_data();
            },
            true
        );



        ins(".ins_toolbar_ui_builder_btn_send")._on(
            "click",
            function(o) {
                slef._all_send_data(o);
            },
            true
        );

        ins(".ins_select_change_file")._on(
            "change",
            function(o) {

                var updateurl = ins()._map._url({ "id": o._getvalue() });

                window.location.href = updateurl;


            },
            true
        );


        ins("*")._on("keydown", function(o, event) {
            if (event.ctrlKey && event.keyCode == 121) {
                slef._all_save_data();
            }
        });




    }
    _actions() {
        var slef = this;
        slef._ui_actions();
        slef._code_actions();

    }
    _out() {
        var slef = this;
        slef._actions();
        slef._all_update_to_stage();




    }
}