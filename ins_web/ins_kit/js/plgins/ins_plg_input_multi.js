/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_input_multi {
    options = {};
    constructor(o) {
        this.options = o;

    }

    _f(a) {
        return this.options.o._find(a);

    }


    _itob() {



        var old = this._f(".ins-input")._getValue();

        var olds = old.split(",")
        if (this._f(".ins-tag") != null) {

            this._f(".ins-tag")._remove();

        }

        for (var item in olds) {
            if (olds[item] != "") {
                var h = "<div onclick='aaaa' class='ins-form-tag ins-flex-space-between    ins-bg-2 ins-border  ins-tag'><span>" + olds[item] + "</span><i class='lni ins-padding-m ins-tag-del ins-button-text ins-padding-h lni-xmark'></i></div>"
                this._f(".ins-input-adder")._appendBefor(h)
            }
        }



    }



    remove(o) {
        var h = o._parent()._find("span")._getHtml();

        var old = this._f(".ins-input")._getValue();
        var olds = old.split(",")
        var ne = "";
        for (var item in olds) {
            if (olds[item] != h && olds[item] != "") {
                ne += "," + olds[item];
            }
        }

        this._f(".ins-input")._setValue(ne)

        o._parent()._remove()

    }

    _add(a) {

        var old = this._f(".ins-input")._getValue();

        var oa = old.split(",");
        console.log(oa);
        console.log(a);

        if (!oa.includes(a)) {

            old += "," + a;

            this._f(".ins-input")._setValue(old)
            this._itob()

        }


    }

    _out() {


        var t = this

        ins(".ins-tag-del")._on(
            "click",
            (o, e) => {
                t.remove(o)
            }
        );

        this._f(".ins-input-adder")._on(
            "keyup",
            (o, e) => {
                if (e.keyCode == 13) {
                    t._add(o._getValue())

                    o._setValue("")


                }
            }
        );





    }
}