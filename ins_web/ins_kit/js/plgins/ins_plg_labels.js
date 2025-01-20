/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_labels {
    options = {};
    constructor(o) {
        this.options = o;
    }

    labels_actions(options, acdone) {
        options.type = ins(".labels_area_filter")._getData("type");
        options.root = "true";
        options.get_file = "/ins_ajax/pages/labels";
        return ins()._ajax._send("/ins_ajax.php", options, "POST", acdone);
    }


    update_label_tds(o) {
        var self = this;

        var options = {
            status: "update_obj",
            obj_id: o._getData("obj_id"),
            obj_type: o._getData("obj_type"),
        };
        this.labels_actions(options, function(data) {
            o._sethtml(data);
            self.update_rowStyle(o);

        });
    }


    update_rowStyle(o) {
        var p = o._parent()._parent();
        if (o._find(".tag_obj_item") == null) {
            p._removeStyle("'background-color'");
        } else {
            var color = o._find(".tag_obj_item")._getData("color");
            p._css("background-color", color + "40");

        }
    }
    update_labels() {
        var self = this;




        this.labels_actions({ status: "get_labels" }, function(data) {


            ins(".labels_area_filter")._sethtml(data);
            ins(".tag_item")._setattr("draggable", "true");
        });
        ins(".labels_area")._each(function(o) {
            // self.update_label_tds(o);
        });
    }


    t_obj = null;


    _lightbox(tite, data) {
        ins()._ui._ins_lightbox({
            title: tite,
            data: data,
            style: "height:auto;width:600px;",
            data_style: "position: relative;top: 0;"
        });
    }


    _tag() {
        var self = this;


        ins(".inspl-labels-add")._on("click", function() {
            self.labels_actions({ status: "add" }, function(data) {
                self._lightbox("Add Label", data);
            });
        }, true);






        ins(".inspl-labels-label-delete")._on("click", function(o) {
            var options = { id: o._getData("id"), status: "delete" };
            self.labels_actions(options, function(data) {
                ins(".labels_area_filter")._sethtml(data);
                ins()._ui._lightbox_remove();
            });
        });


        ins(".inspl-labels-label-settings")._on("click", function(e) {
            var options = { id: e._getData("id"), status: "edit" };
            self.labels_actions(options, function(data) {

                self._lightbox("Edit Label", data)

            });
        });

        ins(".inspl-labels-label-form")._on("submit", function(o, event) {
            event.preventDefault();
            self.labels_actions(o._data._get_inputs(), function(data) {
                ins(".labels_area_filter")._sethtml(data);
                ins()._ui._lightbox_remove();
                ins()._ui._send_tiny_message();
            });
        });

    }



    _actions() {


        var self = this;

        ins(".tag_item")._on("dragstart", function(e, v) {
            v.dataTransfer.setData("id", e._getData("id"));
            v.dataTransfer.setData("obj", e);
            self.t_obj = e;
            e._css({ opacity: "0.5" });
        });


        ins(document)._event("dragend", function(e, v) {
            if (self.t_obj !== null) {
                self.t_obj._css({ opacity: "1" });
                self.t_obj = null;
            }
        });


        ins(".labels_area")._on("dragleave", function(e, v) {
            e._css({ background: "transparent" });
        });

        ins(".labels_area")._on("dragover", function(e, v) {
            v.preventDefault();
            e._css({ background: "#ff8040" });
        });

        ins(".labels_area")._on("drop", function(o, e) {
            e.preventDefault();
            o._css({ background: "transparent" });
            if (self.t_obj !== null) {
                self.t_obj._css({ opacity: "1" });
                self.t_obj = null;
            }
            var options = {
                status: "add_to_obj",
                label_id: e.dataTransfer.getData("id"),
                obj_id: o._getData("obj_id"),
                obj_type: o._getData("obj_type"),
            };
            self.labels_actions(options, function(data) {
                self.update_label_tds(o);
                ins()._ui._send_tiny_message();

            });
        });


        ins(".delete_from_obj")._on("click", function(o) {
            let oid = o._getData("objid");
            var options = {
                id: o._getData("id"),
                status: "delete_from_obj",
                obj_id: oid,
            };
            self.labels_actions(options, function() {
                ins()._ui._send_tiny_message();

                var l = ins('.labels_area[data-obj_id="' + oid + '"]');
                self.update_label_tds(l);
                self.update_rowStyle(o);
            });
        });


    }







    _out() {
        ins(function() {})._load();
        var self = this;
        self.update_labels();

        self._tag();

        self._actions();





    }
}