/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_messages {
    options = {};
    constructor(o) {
        this.options = o;
    }

    _note() {
        if (this.options["class"] == null) {
            this.options["class"] = " ins-info ";
        }
        var msg = this.options["msg"];
        var msgclass = this.options["class"];
        var un = ins()._data._get_unique_id();
        if (ins(msg)._isEmpty()) {
            msg = "  <i class='lni  ins-icon  lni-checkmark'></i> " + ins()._data._get("operation_done_msg");
        }
        var node = ins()._ui._create(
            "div",
            msg, { class: "ins_message   ins-message  " + un + " " + msgclass }
        );
        var d = ins(".ins-message-area")._append(node);


        return d;
    }

    _notification() {
        if (this.options["class"] == null) {
            this.options["class"] = " ins-info ";
        }
        var msg = this.options["msg"];
        var msgclass = this.options["class"];
        var un = ins()._data._get_unique_id();

        ins("operation_done_msg")._data._trans((w) => {



            if (ins(msg)._isEmpty()) {
                msg = "  <i class='lni  ins-icon  lni-checkmark'></i> " + w;
            }
            var node = ins()._ui._create(
                "div",
                msg, { class: "ins_message   ins-message  " + un + " " + msgclass }
            );
            var d = ins(".ins-message-area")._append(node);
            ins()._data._settimer(this.time, function() {
                d._addClass("ins-remove");
            });
            ins()._data._settimer(6000, function() {
                d._remove();
            });
            return node;

        })
    }
    _alert() {
        if (this.options["title"] == null) {
            this.options["title"] = "Alert";
        }
        var options = {
            "body_class": this.options["class"],
            "title": this.options["title"],
            "data": "<div class='ins-padding-xl'>" + this.options["msg"] + "</div>",
            "style": "height:auto;width:650px;max-width:90%",
            "data_style": "height: auto;position: RELATIVE;top: 0;"
        };
        ins()._ui._ins_lightbox(options)
    }

    _confirm() {

        var un = ins()._data._get_unique_id();
        if (this.options["title"] == null) {
            this.options["title"] = "Confirm";
        }
        if (this.options["confirm_btn_title"] == null) {
            this.options["confirm_btn_title"] = "Ok";
        }
        if (this.options["cancel_btn_title"] == null) {
            this.options["cancel_btn_title"] = "Cancel";
        }



        var self = this;
        var buttons = " <div class='insa-padding-xl ins-col-12  ins-flex-center'><div class='ins-button ins-cancel-btn " + un + " ins-col-3'>" + this.options["cancel_btn_title"] + "</div><div class='ins-button ins-confirm-btn " + un + " ins-primary  ins-col-3'>" + this.options["confirm_btn_title"] + "</div></div>";
        var body = "<div class=' ins-flex-center'><div class='ins-col-12  ins-padding-xl ins-bg-4 ins-flex'>" + this.options["msg"] + "</div> " + buttons + " <div class='ins-col-12 '></div></div>";


        ins(".ins-cancel-btn." + un)._on("click", function(o) {

            if (self.options["cancel"] != null) {
                self.options["cancel"](o);
            }
            ins("." + un)._ui._removeLightbox();
        });

        ins(".ins-confirm-btn." + un)._on("click", function() {

            if (self.options["confirm"] != null) {
                self.options["confirm"](o);
            }
            ins("." + un)._ui._removeLightbox();

        });
        var options = {

            "class": un,
            "body_class": this.options["class"],
            "title": this.options["title"],
            "data": body,
            "style": "height:auto;width:650px;max-width:90%",
            "data_style": "height: auto;position: RELATIVE;top: 0;"
        };
        ins()._ui._ins_lightbox(options)
    }


    _comment() {}
    time = 5000
    _out() {
        if (this.options.o != null && typeof this.options.o != "string") {
            this.options["msg"] = this.options.o._getData("msmsg");
            this.options["class"] = this.options.o._getData("msclass");
        } else {
            this.options["msg"] = this.options.o;
        }



        if (this.options["mode"] == "confirm") {
            this._confirm();
        } else
        if (this.options["mode"] == "alert") {
            this._alert();
        } else if (this.options["mode"] == "note") {
            this._note();



        } else {
            this._notification();
        }
    }
}