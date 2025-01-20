/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_daterange {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _out() {
        ins(".ins-date-range-action")._on("change", (o, e) => {
            var obj = o._get(0);
            var ops = obj.options;
            var item = ops[obj.selectedIndex];
            var selectedData = ins(item)._getData();
            var _id = o._getData("_id");


            Object.keys(ops)
                .forEach(element => {
                    var c = ops[element].getAttribute("value")
                    ins(".p-daterange-area." + _id)._removeClass("p-daterange-show-" + c);
                });
            ins(".p-daterange-area." + _id)._removeClass("p-daterange-show-template");



            ins(".p-daterange-area." + _id)._find(".ui-date-range-offset input")._setValue("");

            var frm = ins(".p-daterange-area." + _id)._find(".ins-date-range-from");
            var tos = ins(".p-daterange-area." + _id)._find(".ins-date-range-to");


            if (selectedData["action"] == "template") {
                ins(".p-daterange-area." + _id)._addClass("p-daterange-show-template");
                ins(".p-daterange-area." + _id + " .templat-input")._remove();

                var h = "<div><input type='hidden' name='" + frm._getAttribute("name") + "' value='" + selectedData["from_date"] + "' class='templat-input ins-form-input   filter_item'/> <input class='templat-input filter_item ins-form-input ' type='hidden'  name='" + tos._getAttribute("name") + "' value='" + selectedData["to_date"] + "'/></div>";

                ins(".p-daterange-area." + _id)._append(h);


                frm._removeClass("filter_item");
                tos._removeClass("filter_item");

            } else {

                ins(".p-daterange-area." + _id + " .templat-input")._remove();

                ins(".p-daterange-area." + _id)._addClass("p-daterange-show-" + o._getValue());
                tos._addClass("filter_item");
                frm._addClass("filter_item");

            }

        });
    }
}