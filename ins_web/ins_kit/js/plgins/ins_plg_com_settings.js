/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_com_settings {
    options = {};
    constructor(o) {
        this.options = o;
    }


    job(jdata) {



        if (!ins(ins("select.job")._getValue())._isEmpty()) {
            jdata["job"] = ins("select.job")._getValue();
            jdata["setfor"] = "job";

        };

        if (!ins(ins("select.only_user")._getValue())._isEmpty()) {
            jdata["user"] = ins("select.only_user")._getValue();
            jdata["setfor"] = "user";

        };

        return jdata;
    }



    temp_ui(dbdata, fun = function() {}) {

        var t = this;

        ins()._ajax._to("eng/list/mlist", t.job(dbdata), function(data) {
            ins(".ins-mlist-templates-area")._setHtml(data);
            ins()._ui._removeLightbox();
            fun();
        });
    }


    _update_ui(ops) {

        ops["status"] = "_mange_ui";
        ins()._ajax._to("eng/list/mlist", ops, function(data) {
            ins(".ins-mlist-templates-area")._setHtml(data);
        });
    }

    _mlist() {

        var t = this;





        ins(".ins-mlist-template-show-area")._on(
            "click",
            function(o) {

                ins(".ins-mlist-template-body-area")._hide();
                ins("." + o._getData("show"))._show();

            }, true)




        ins(".ins-mlist-item-update-omit-template")._on(
            "change",
            function(o) {

                var v = o._getValue();


                var t = ins(".ins-mlist-template-c-area textarea");
                var h = v;


                var j = {
                    "title": "",
                    "value": "",
                    "type": "text",
                    "style": "width:100px;",
                    "name": "com_tickets::_json",
                    "type": "function"

                };


                if (v == "normal") {


                    var j = {
                        "title": "",
                        "name": "",
                        "style": "width:100px;",
                        "type": "text"

                    };
                } else if (v == "options") {



                    var j = {
                        "title": "",
                        "value": "",
                        "op_id": "0",
                        "style": "width:100px;",
                        "type": "function",
                        "name": "com_tickets::_get_from_options"

                    };

                } else if (v == "json_options") {



                    var j = {
                        "title": "",
                        "value": "",
                        "op_id": "0",
                        "style": "width:100px;",
                        "type": "function",
                        "name": "com_tickets::_get_from_json_options"

                    };





                } else if (v == "json") {



                    var j = {
                        "title": "",
                        "value": "",
                        "type": "text",
                        "style": "width:100px;",
                        "name": "com_tickets::_json",
                        "type": "function"

                    };





                }


                t._setValue(JSON.stringify(j, null, 1));

            }, true)

        ins(".ins-mlist-update-m-ui")._on(
            "click",
            function(o) {
                t._update_ui(ins(".ins-mlist-template-add-btn")._getData());

            }, true)

        ins(".ins-mlist-template-add-btn")._on(
            "click",
            function(o) {

                var ops = { "status": "_add_ui", "type": o._getData("type") };
                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {
                    ins()._ui._addLightbox({
                        mode: "normal",
                        title: "Add new List Template",
                        data: data,
                        data_style: "position: relative;top: 0;",
                        style: "height: auto;width:600px;    "
                    });
                });
            }, true);







        ins(".ins-mlist-template-save-btn ")._on(
            "click",
            function(o) {
                ins(".ins-lightbox-body")._data._submit(function(dbdata) {
                    dbdata["status"] = "_add_save"
                    t.temp_ui(dbdata);

                })



            }, true);
        ins(".ins-mlist-template-del-btn")._on(
            "click",
            function(o) {
                t.temp_ui(o._getData(), function() {
                    o._parents(".ins-mlist-tr")._remove();

                });


            }, true);






        ins("select.job")._on("change",
            function(o) {
                var ops = o._getData();
                ins("select.only_user")._setValue("");
                ops["job"] = ins("select.job")._getValue();
                t._update_ui(ops);

            }, true);

        ins("select.only_user")._on("change",
            function(o) {
                var ops = o._getData();
                ins("select.job")._setValue("");
                ops["user"] = ins("select.only_user")._getValue();

                t._update_ui(ops);

            }, true);








        ins(".ins-mlist-template-update_def")._on(
            "click",
            function(o) {


                var ops = o._find("input")._getData();
                ops["temp_id"] = o._find("input")._getValue();

                ops["status"] = "update_def";

                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {
                    ins(".ins-mlist-templates-area")._setHtml(data);
                    ins("Settings defualt updated")._ui._notification();

                });
            }, true);










        ins(".ins-mlist-item-update-omit-cadd")._on(
            "click",
            function(o) {
                var ops = o._getData();

                ins(".ins-mlist-ctr")._find("input,textarea")._each(function(o) {
                    ops[o._getAttribute("name")] = o._getValue();

                })


                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {
                    ins(".ins-mlist-templates-data-table")._setHtml(data);

                });
            }, true);




        ins(".ins-mlist-template-update")._on(
            "click",
            function(o) {
                var ops = o._getData();

                o._parents(".ins-mlist-tr")._find("input")._each(function(o) {
                    if (o._getValue() != "") {
                        ops[o._getAttribute("name")] = o._getValue();
                    }
                })


                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {
                    ins(".ins-mlist-templates-area")._setHtml(data);
                    ins("Settings updated")._ui._notification();

                });
            }, true);




        ins(".ins-mlist-mang-data-btn")._on(
            "click",
            function(o) {

                var ops = o._getData();
                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {

                    ins()._ui._addLightbox({
                        "mode": "right_panel",
                        title: "Add new List Template",
                        data: data,
                        data_style: "position: relative;top: 0;",
                        style: "width:600px;    "
                    });


                    setTimeout(function(o) {

                        ins(".ins-mlist-template-data-area .ins-table-data")._ui._order({ "hander": null })

                    }, 1000)

                });
            }, true);





        ins(".ins-mlist-item-more-btn")._on(
            "click",
            function(o) {

                var p = o._parents(".ins-tr")._toggleClass("ins-mlist-item-more-status");




            }, true);




        ins(".ins-mlist-template-data-update-btn ")._on(
            "click",
            function(o) {

                t._get_mlist_template_data(o);
            }, true);




        ins(".ins-filter-template-data-update-btn ")._on(
            "click",
            function(o) {

                t._get_filter_template_data(o);
            }, true);





        ins(".ins-mlist-template-data-close-btn")._on(
            "click",
            function(o) {


                ins(".ins-panel-overlay")._remove();


            }, true);



        ins(".ins-mlist-item-update-omit-add")._on(
            "click",
            function(o) {
                var ops = o._getData();
                o._parents(".ins-tr")._find("input,textarea")._each(function(o) {
                    ops[o._getAttribute("name")] = o._getValue();
                })

                o._removeClass("ins-mlist-item-update-omit-add", "ins-danger-color")
                ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {
                    ins(".ins-mlist-templates-data-table")._setHtml(data);
                    setTimeout(function(o) {
                        ins(".ins-mlist-template-data-area .ins-table-data")._ui._order({ "hander": null })
                    }, 1000)
                });
            }, true);





        ins(".ins-mlist-item-update-omit")._on(
            "click",
            function(o) {


                var omit = o._getData("omit");

                if (omit == "1") {
                    o._addClass("ins-primary-color");
                    o._removeClass("ins-danger-color");

                    o._setData("omit", "0");
                } else {

                    o._removeClass("ins-primary-color");
                    o._addClass("ins-danger-color");

                    o._setData("omit", "1");

                }

            }, true);



    }












    _get_mlist_template_data(o) {
        var d = [];
        var t = this;
        ins(".ins-mlist-template-data-area .ins-tr")._each(function(tr) {

            var row = {};
            row["title"] = tr._find(".ins-form-input.title")._getValue();
            row["style"] = tr._find(".ins-form-input.style")._getValue();
            row["class"] = tr._find(".ins-form-input.class")._getValue();
            row["data"] = JSON.parse(tr._find("textarea.data")._getValue());
            row["key"] = tr._find(".ins-form-input.key")._getValue();



            row["omit"] = '0';

            if (tr._find(".ins-mlist-item-update-omit")._getData("omit") != null) {
                row["omit"] = tr._find(".ins-mlist-item-update-omit")._getData("omit");


            }

            d.push(row);
        })

        var ops = o._getData();
        ops["data"] = JSON.stringify(d);


        ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {

            ins(".ins-panel-overlay")._remove();
            ins("Settings updated")._ui._notification();


        })





    }





    _get_filter_template_data(o) {

        var t = this;

        var d = [];
        ins(".ins-mlist-template-data-area .ins-tr")._each(function(tr) {

            var row = {};
            row["title"] = tr._find(".ins-form-input.title")._getValue();
            row["style"] = tr._find(".ins-form-input.style")._getValue();
            row["class"] = tr._find(".ins-form-input.class")._getValue();
            row["data"] = JSON.parse(tr._find("textarea.data")._getValue());
            row["key"] = tr._find(".ins-form-input.key")._getValue();



            row["omit"] = '0';

            if (tr._find(".ins-mlist-item-update-omit")._getData("omit") != null) {
                row["omit"] = tr._find(".ins-mlist-item-update-omit")._getData("omit");


            }

            d.push(row);
        })

        var ops = o._getData();
        ops["data"] = JSON.stringify(d);

        ins()._ajax._to("eng/list/mlist", t.job(ops), function(data) {

            ins(".ins-panel-overlay")._remove();
            ins("Settings updated")._ui._notification();


        })





    }



    _out() {
        this._mlist();



        this._update_ui(ins(".ins-mlist-template-add-btn")._getData());
    }
}