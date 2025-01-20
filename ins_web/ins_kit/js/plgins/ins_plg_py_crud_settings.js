/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_crud_settings {
    options = {};
    constructor(o) {
        this.options = o;
    }
    o() {
        return ins(".crd-set-data-area")._getData()
    }
    t() {
        return ins(".crd-set-data-area")._getData("t")
    }
    get_data() {
        var sdata = [];
        sdata = this.o()
        sdata["list_name"] = ins(".crd-set-update-lists-slct")._getValue();
        this.j(this.t(), sdata, (data) => {
            ins(".crd-set-data-area")._setHTML(data)
        })
    }
    j(name, ops, done) {
        ins("ajx_crud_setting/" + name)._ajax._ins_ajax(ops, done)
    }
    update_list() {
        var sdata = [];
        sdata = this.o()
        var sel = this;
        this.j("get_list_names", sdata, (data) => {
            ins(".crd-set-update-lists-slct")._setHTML(data);
            sel.get_data()
        })
    }
    update_data(data) {
        this.update_list();
    }
    _actions() {
        var sel = this;
        sel.update_list();
        ins(".crd-set-update-lists-slct")._on("change", (o) => {
            sel.get_data()
        })




        ins(".crd-set-update-del-btn")._on("click", (o) => {
            var v = ins(".crd-set-update-lists-slct")._getValue();
            var sdata = [];
            sdata = this.o()
            sdata["list_name"] = v;
            this.j("del_list", sdata, (data) => {
                sel.update_list();
            })
        })
        ins(".crd-set-update-dupl-btn")._on("click", (o) => {
            var v = ins(".crd-set-update-lists-slct")._getValue();
            var sdata = [];
            sdata = this.o()
            sdata["list_name"] = v;
            this.j("dupl_list", sdata, (data) => {
                sel.update_data(data);
            })
        })
        ins(".crd-set-update-new-btn")._on("click", (o) => {
            var v = ins(".crd-set-update-lists-slct")._getValue();
            var sdata = [];
            sdata = this.o()
            sdata["list_name"] = v;
            this.j("new_list", sdata, (data) => {
                sel.update_data(data);
            })
        })
        ins(".crd-set-update-defa-btn")._on("click", (o) => {
            var v = ins(".crd-set-update-lists-slct")._getValue();
            var sdata = [];
            sdata = this.o()
            sdata["list_name"] = v;
            this.j("active_list", sdata, (data) => {
                sel.update_data(data);
            })
        })
        ins(".crd-set-update-data-btn")._on("click", (o) => {
            ins(".crd-set-data-area")._data._submit((data) => {
                var sdata = [];
                sdata = this.o()
                var o = "update_list";
                if (sdata["t"] == "opss") {
                    o = "update_ops";
                } else if (sdata["t"] == "set") {
                    o = "update_set";
                }
                data["list_name"] = ins(".crd-set-update-lists-slct")._getValue();
                sdata["data"] = JSON.stringify(data);
                this.j(o, sdata, (data) => {
                    if (sdata["t"] == "set") {
                        sel.update_data(data);
                    }
                    ins("Data updated :)")._ui._notification({});
                })
            })
        })
        ins(".crd-set-update-btn")._on("click", (o) => {
            ins(".crd-set-update-btn")._removeClass("ins-active")
            o._addClass("ins-active")
            ins(".crd-set-data-area")._setData("t", o._getData("g"))
            if (o._getData("i") != null) {
                ins(".crd-set-data-area")._setData("i", o._getData("i"))
            }
            sel.get_data()
        })
    }
    _out() {
        this._actions();
    }
}