/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_lightbox {
    options = {};
    constructor(o = null) {
        this.options = o;
    }

    _updateOptions() {



        this.options.body = { class: this.bodyClass };
        this.options.body.style = this.bodyDefualtstyle;
        if (!ins(this.options.style)._isEmpty()) {
            this.options.body.style = this.options.style;
        }

        this.options.body.style += this.bodyMorestyle;

        this.options.lightbox = { class: this.parentClass };
        if (!ins(this.options.class)._isEmpty()) {
            this.options.lightbox.class += " " + this.options.class;
        }

        if (ins(this.options.data)._isEmpty()) {
            this.options.data = "";
        }
    }


    parentClass = " ins_lightbox ins-lightbox ";
    dataClass = " ins_lightbox_data ins-lightbox-data  ";
    bodyClass = " ins_lightbox_body ins-lightbox-body ";
    bodyDefualtstyle = "width:60%;height:60%";
    bodyMorestyle = ";min-height:100px;";



    _out() {
        if (this.options["mode"] == "right_panel") {
            this.parentClass = "ins-panel-overlay ins-opened";
            this.bodyClass = "ins-fixpanel-end  ins-fixpanel";
            this.dataClass = " ins-data  ";
            this.bodyDefualtstyle = "";
            this.bodyMorestyle = "";
        } else if (this.options["mode"] == "left_panel") {
            this.parentClass = "ins-panel-overlay  ins-fixpanel ins-opened";
            this.bodyClass = "ins-fixpanel-start ins-fixpanel  ins-opened";
            this.dataClass = " ins-data  ";
            this.bodyDefualtstyle = "";
            this.bodyMorestyle = "";

        } else {
            this.parentClass = " ins_lightbox ins-lightbox ";
            this.dataClass = " ins_lightbox_data ins-lightbox-data  ";
            this.bodyClass = " ins_lightbox_body  ins-lightbox-body ";
            this.bodyDefualtstyle = "width:60%;height:60%";
            this.bodyMorestyle = ";min-height:100px;";



        }

        if (this.options.body_class) {
            this.bodyClass += " " + this.options.body_class;
        }


        this._updateOptions();


        var id = "_" + Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);



        this.options.lightbox.class += "  " + id + " ";

        if (!ins(this.options.url)._isEmpty()) {
            this.options.data = ins()._ui._create("iframe", "loding", {
                src: this.options.url,
            });
            this.options.lightbox.class += " iframe ";
        }


        var data_options = {};
        if (ins(this.options.options)._isExists()) {
            data_options = this.options.options;
        }
        if (this.options.data_class) {
            this.dataClass += " " + this.options.data_class;
        }

        data_options["class"] = this.dataClass;

        if (this.options.data_style) {
            data_options.style = this.options.data_style;
        }



        var lclose = ins()._ui._create("i", "", {
            class: "ins_close ins-close  lni  lni-xmark",
        });

        if (!ins(this.options["title"])._isEmpty()) {
            var title = ins()._ui._create("div", this.options.title, {
                class: "ins-title-l",
            });
        }

        var ltitle = ins()._ui._create("div", [title, lclose], {
            class: "ins-header ins-flex-space-between",
        });
        if (this.options.title === false) {
            ltitle = lclose;
            data_options["class"] = " ins-full-data " + this.dataClass;
        }

        var ldata = ins()._ui._create("div", null, data_options, this.options.data);

        var lbody = ins()._ui._create("div", [ltitle, ldata], this.options.body);

        this.node = ins()._ui._create("div", lbody, this.options.lightbox);

        ins(lclose)._event("click", () => {


            ins(".ins-fixpanel  ")._removeClass("ins-opened")

            setTimeout(() => {

                if (ins(this.options.onclose)._isExists()) {
                    this.options.onclose();
                }
                ins("." + id)._remove();
            }, 100);


        });

        var addto = "body";
        if (ins(this.options.addto)._isExists()) {
            addto = this.options.addto;
        }
        ins(addto)._append(this.node);




        setTimeout(() => {
            ins(".ins-fixpanel")._addClass("ins-opened")


        }, 100);


        ins()._ui._update();

        if (ins(this.options.onopen)._isExists()) {
            this.options.onopen();
        }
        // document.getElementsByTagName(addto)[0].appendChild(this.node);
    }

    node = null;
    _remove() {
        ins(this.node)._remove();
        if (ins(this.options.onclose)._isExists()) {
            this.options.onclose();
        }
    }
}