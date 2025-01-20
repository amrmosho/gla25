/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_login {
    options = {};
    constructor(o) {
        this.options = o;
    }




    _timer() {
        var ii = 10;
        var i = 0;
        var h = ins(".ins-logplg-opt-resend-area")._getHtml();

        ins()._data._timer({
            time: ii,
            offest: 1,
            frame: function(a) {
                var c = ii - i
                ins(".ins-logplg-opt-resend-area")._addClass("ins-warning-color");
                ins(".ins-logplg-opt-resend-area")._setHtml("resend in " + c);
                i++;
            },
            end: function(a) {
                ins(".ins-logplg-opt-resend-area")._setHtml(h);
                ins(".ins-logplg-opt-resend-area")._removeClass("ins-warning-color");
                ins(".ins-logplg-opt-resend-area")._addClass("-otp-resend-btn");
                console.log("end");
            }
        })
    }





    _out() {

        var th = this;


        ins(".ins-logplg-opt-resend-btn")._on("click", function(o) {
            var uidata = [];
            var ops = o._getData();
            ops["type"] = "uiplugin";
            ops["name"] = "login";



            var uidata = [ops];
            ins(uidata)._ui._render(function(data) {
                if (data.trim() == 1) {
                    ins()._ui._send_tiny_message(
                        o._getData("msg"), "ins-success");

                    th._timer();


                }
            })
        })

        ins(".ins-logplg-forget-new-btn")._on("click", function(o) {
            var uidata = [];
            var ops = o._getData();
            ops["type"] = "uiplugin";
            ops["name"] = "login";
            ops["mode"] = "setpassword";
            ops["password"] = ins(".ins-logplg-forget-poassword-inp")._getValue();
            ops["repassword"] = ins(".ins-logplg-forget-repoassword-inp")._getValue();
            if (ops["repassword"] == ops["password"]) {
                ops["email"] = ins(".ins-logplg-forget-email-inp")._getValue();
                var uidata = [ops];
                ins(uidata)._ui._render(function(data) {
                    console.log(data.trim());
                    if (data.trim() == 1) {
                        var ops = o._getData();
                        ops["type"] = "uiplugin";
                        ops["name"] = "login";
                        ops["mode"] = "login";


                        var uidata = [ops];
                        ins(uidata)._ui._render(function(data) {
                            ins(".ins-logplg-area")._setHtml(data);
                        });
                        ins()._ui._send_tiny_message(
                            o._getData("updatemsg"), "ins-success");

                    } else {
                        ins()._ui._send_tiny_message(
                            o._getData("msg"), "ins-danger");
                    }
                });
            } else {

                ins()._ui._send_tiny_message(
                    o._getData("remsg"), "ins-danger");
            }
        }, true);


        ins(".ins-logplg-forget-otp-btn")._on("click", function(o) {
            var uidata = [];
            var ops = o._getData();
            ops["type"] = "uiplugin";
            ops["name"] = "login";
            ops["mode"] = "ckeck_otp";
            ops["otp"] = ins(".ins-logplg-forget-otp-inp")._getValue();
            ops["email"] = ins(".ins-logplg-forget-email-inp")._getValue();

            var uidata = [ops];
            ins(uidata)._ui._render(function(data) {
                if (data.trim() == 1) {
                    ops["mode"] = "update_password";
                    var uidata = [ops];
                    ins(uidata)._ui._render(function(data) {
                        ins(".ins-logplg-area")._setHtml(data);
                    });
                } else {
                    ins()._ui._send_tiny_message(
                        o._getData("msg"), "ins-danger")
                }
            });
        }, true);


        ins(".ins-logplg-forget-check-btn")._on("click", function(o) {
            var uidata = [];
            var ops = o._getData();
            ops["type"] = "uiplugin";
            ops["name"] = "login";
            ops["mode"] = "ckeck";
            ops["email"] = ins(".ins-logplg-forget-email-inp")._getValue();
            var uidata = [ops];
            ins(uidata)._ui._render(function(data) {
                if (data.trim() == 1) {
                    ops["type"] = "uiplugin";
                    ops["name"] = "login";
                    ops["mode"] = "forget_otp";

                    var uidata = [ops];
                    ins(uidata)._ui._render(function(data) {
                        ins(".ins-logplg-area")._setHtml(data);
                        th._timer();

                    });
                } else {
                    ins()._ui._send_tiny_message("email not exsiet ", "ins-danger")
                }
            });
        }, true);


        ins(".ins-logplg-change-btn")._on("click", function(o) {
            var uidata = [];
            var ops = o._getData();
            ops["type"] = "uiplugin";
            ops["name"] = "login";
            var uidata = [ops];
            ins(uidata)._ui._render(function(data) {
                ins(".ins-logplg-area")._setHtml(data);
            });
        }, true);


    }
}