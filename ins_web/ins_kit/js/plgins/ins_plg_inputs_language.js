export class ins_plg_inputs_language {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _out() {



        ins(".ins-input-update-language-value")._on(
            "click",
            function(o, ev) {
                ev.preventDefault();
                ins()._ui._page_progress_run();

                var ops = o._getData();
                ops["lang_value"] = ins("textarea.ins-input-update-language-input")._getvalue();

                console.log(ops);


                ins()._ui._lightbox_remove();


                ins()._ajax._to("inputs/language", ops, function(data) {
                    ins()._ui._lightbox_remove();
                    ins()._ui._send_tiny_message();
                    ins()._ui._page_progress_hide();
                });
            },
            true
        );

        ins(".ins-input-update-language")._on(
            "click",
            function(o) {

                ins()._ui._page_progress_run();
                var ops = o._getData();
                ins()._ajax._to("inputs/language", ops, function(data) {
                    var lop = {
                        data: data,
                        title: " Update " + ops["obj_title"] + " language ",
                        "data_style": "    overflow: hidden;",
                        "style": "height:410px;width:550px"
                    }

                    ins()._ui._lightbox_remove();

                    ins()._ui._ins_lightbox(lop, function() {
                        ins()._ui._page_progress_hide();
                    });
                    ins()._ui._page_progress_hide();
                });
            },
            true
        );



    }
}