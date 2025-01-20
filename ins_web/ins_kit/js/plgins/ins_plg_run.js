/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_run {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _onloadList() {
        var g = ins()._map._get();
        if (g["list_mode"] != null && g["list_mode"] == "view" && !ins(g["id"])._isEmpty()) {
            var obj = ins(ins(".ins-view-mode .ins-tr")._get(1));
            if (g["id"] != null) {
                var obj = ins(".ins-view-mode-td.__" + g["id"]);
            }
            if (obj._isExists(true)) {
                obj._parent()._addclass("ins-active");
                var id = obj._find("span")._getData("id");
                ins(".ins-view-mode-data")._ui._addloader();
                var url = ins()._map._url({ "id": id, "mode": "view" });
                ins()._ajax._load(url, obj._getData(), function(d) {
                    ins(".ins-view-mode-data")._sethtml(d);
                    ins()._ui._removeloader();
                });

            }
        }
    }
    _out() {
        ins("input,select,textarea")._each(function(obj, a) {
            var elements = obj._get(0);
            if (!ins(obj._getData("required_message"))._isEmpty()) {
                elements.oninvalid = function(e) {
                    e.target.setCustomValidity("");
                    if (!e.target.validity.valid) {
                        e.target.setCustomValidity(obj._getData("required_message"));
                    }
                };
                elements.oninput = function(e) {
                    e.target.setCustomValidity("");
                };
            }
        })
        ins("ins_plg_ui")._plgin({});
        this._onloadList();
    }
}