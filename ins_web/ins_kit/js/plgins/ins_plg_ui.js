/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_ui {
    options = {};
    constructor(o) {
        this.options = o;
    }

    _tabs() {


        ins(".ins-tabs > ul li ,.ins-tabs-rounded > ul li")._on(
            "click",
            function(o) {
                var p = o._parent();
                if (!o._hasClass("ins-act") && !o._hasClass("ins-active")) {
                    p._find("li")._removeClass("ins-act", "ins-active");
                    o._addClass("ins-act", "ins-active");
                }
                var pp = p._parent();
                pp._find(".ins-tabs-body>div ,.ins-body>div ")._addClass("ins-hidden");
                pp._find("." + o._getData("show"))._removeClass("ins_hidden");
                pp._find("." + o._getData("show"))._removeClass("ins-hidden");
            },
            true
        );


        ins(".ins-panel .ins-header")._on(
            "click",
            function(o) {
                var p = o._parent();
                if (!p._hasClass("ins-active")) {

                    p._addClass("ins-active");
                    if (!ins(p._getData("onchange"))._isEmpty()) {
                        window[p._getData("onchange")]("opened");
                    }
                } else {
                    p._removeClass("ins-active");
                    if (!ins(p._getData("onchange"))._isEmpty()) {

                        window[p._getData("onchange")]("closed");
                    }
                }
            },
            true
        );
    }


    _menu() {
        ins(".ins-menu h3 ,.ins-menu .ins-header")._on(
            "click",
            function(o) {

                var e = o._parent();
                if (e._hasClass("ins-act")) {
                    e._removeClass("ins-act");
                } else {
                    ins(".ins-menu")._removeClass("ins-act");

                    e._addClass("ins-act");
                }
            },
            true
        );
    }

    _inputs() {

        ins(".ins-form-bool-f")._on(
            "change",
            function(o) {
                var c = o._get(0);
                var e = o._parent()._find(".ins-form-checkbool");

                if (c.checked) {
                    e._setValue("1");

                } else {
                    e._setValue("0");
                }

            },
            true
        );









    }



    _out() {
        this._inputs();

        this._tabs();
        this._menu();


    }
}