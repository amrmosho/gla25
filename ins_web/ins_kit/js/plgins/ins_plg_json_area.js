/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_json_area {
    options = {};
    constructor(o) {
        this.options = o;
    }

    _ins_json_form_update(o, k) {
        var input = ins(o._getData("input"));

        var allj = [];
        ins(k)
            ._find("._ins_json_form_row")
            ._find(o._getData("inputs"))
            ._each(function(i) {
                var j = ins(i)._data._get_inputs();
                delete j.error;
                delete j.error_inputs;
                allj.push(j);
            });


        input._setvalue(JSON.stringify(allj));
    }


    _out() {


        var o = this.options.o;

        var th = this;
        var k = ins()._data._get_unique_id();
        o._addclass(k);
        k = "." + k;
        var data_body = o._append(
            "<div class='ins_grid ins-col-12 _ins_json_form_row '></div>"
        );
        var add_btn = ins(o._getData("add_btn"));
        var delete_btn = ins(o._getData("delete_btn"));
        var inputs = ins(o._getData("inputs"));
        var h = inputs._getouterhtml();


        add_btn._on(
            "click",
            function() {

                var ap = data_body._append(h);
                ap._removeclass("ins_hidden");
                ins()._ui._update_ui();
            },
            true
        );
        delete_btn._on(
            "click",
            function(t) {
                t._parent()._remove();
                th._ins_json_form_update(o, k);
            },
            true
        );


        ins(
            k +
            " ._ins_json_form_row input," +
            k +
            " ._ins_json_form_row textarea," +
            k +
            "  ._ins_json_form_row select"
        )._on(
            "change",
            function() {
                th._ins_json_form_update(o, k);
            },
            true
        );


        if (!ins(ins(o._getData("input"))._getvalue())._isEmpty()) {
            var j = JSON.parse(ins(o._getData("input"))._getvalue());
            j.forEach(function(v) {
                var ap = data_body._append(h);
                ap._removeclass("ins_hidden");

                ins(ap)._data._update_inputs(v);
                ins()._ui._update_ui();
            });
        }
    };





}