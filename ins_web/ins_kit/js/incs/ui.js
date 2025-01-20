/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* global ins */

function sendNotfMessage(msg, type = "ins-info", icon = "") {
    ins(function() {
        ins()._ui._send_tiny_message(msg, type, icon);
    })._load();
}

var o = null;

function ins_select_manage_update() {
    var s = o._parent()._find("select");
    var options = o._getData();
    options["get_file"] = "eng/select_full";
    ins()._ajax._send("/ins_ajax.php", options, "POST", function(data) {
        s._sethtml(data);
        s._get(0).selectedIndex = s._get(0).options.length - 1;
    });
}





ins(".ins-select-other")._on("change", function(o) {

    if (o._getvalue() == "other") {
        o._parent()._find(".ins-other-input")._removeClass("ins-hidden");


    } else {
        o._parent()._find(".ins-other-input")._addClass("ins-hidden");

        o._parent()._find(".ins-other-input")._setValue("");
    };

})

ins(".ins_select_manage_btn")._on(
    "click",
    function(e) {
        o = e;
        var title = "manage list";
        if (o._getData("lightbox_title")) {
            title = o._getData("lightbox_title");
        }
        var options = {
            title: title,
            style: "width:60%;height:auto;",
            data_style: "height:500px;",
            url: "/ins_admin/" +
                e._getData("manage") +
                "/add/do/get_tmp_index/main_style/onclose/ins_select_manage_update/",
            onclose: function() {
                ins_select_manage_update();
            },
        };
        ins()._ui._ins_lightbox(options);
    },
    true
);

ins(".ins_btn_list_action ")._on("click", function(e) {
    var options = e._getData();
    options.get_file = "eng/add_to_lists";

    ins()._ajax._send("/ins_ajax.php", options, "POST", function(data) {
        ins(".ins_lightbox_data")._sethtml(data);
        options.status = "get";
        ins()._ajax._send("/ins_ajax.php", options, "POST", function(a) {
            ins("select." + e._getData("name"))._sethtml(a);
        });
    });
});

ins(
    ".ui_editable_select  .ins_btn_manage ,.ui_editable_list .ins_btn_manage "
)._on("click", function(e) {
    var options = { get_file: "eng/add_to_lists", name: e._getData("name") };
    options.status = "manage";
    ins()._ajax._send("/ins_ajax.php", options, "POST", function(data) {
        ins()._ui._lightbox("manage list", data, "", "width: 30%;height: 60%;");
    });
});

ins(".ui_editable_select  .ins_btn_save,.ui_editable_list  .ins_btn_save ")._on(
    "click",
    function(e) {
        var t = e._parent()._find("input.list_value");
        var s = e._parent()._parent()._find("select");

        var options = {
            get_file: "eng/add_to_lists",
            value: t._getvalue(),
            name: e._getData("name"),
        };

        options.status = "add";

        ins()._ajax._send("/ins_ajax.php", options, "POST", function(v) {
            options.value = v.trim();

            options.status = "get";
            ins()._ajax._send("/ins_ajax.php", options, "POST", function(a) {
                s._sethtml(a);
            });

            e._parent()._addclass("ins_hidden");
        });
    }
);
ins(".ins-from-input-error input")._on("input", function(e, o) {
    e._parents(".ui_parent")._removeclass("ins-from-input-error")
});

ins(function() {

    ins("input,select,textarea")._event("invalid", function(e, o) {
        e._parents(".ui_parent")._addclass("ins-from-input-error")
        o.preventDefault();
    });
















    ins()._map._setKey("back", (k) => {
        ins()._ui._send_tiny_message("Back to home...")

        var u = ins()._map._url({}, "mode");;
        window.location.href = u;
    });
    ins()._map._setKey("send", (k) => {


        ins()._ui._send_tiny_message("Send data ...")

        var form = ins(".ins-form-page")._get(0);
        _main_form_onsubmit(form);
        form.submit();
    });
})._load();

function _main_form_onsubmit(form) {
    var inp = ins(form)._find(".ins-form-submit");
    inp._sethtml('<i class="lni lni-spinner-solid ins-spin"></i>');
    inp._get(0).disabled = true;
}