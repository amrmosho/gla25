/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_input_select_auto {
    options = {};
    constructor(o) {
        this.options = o;
    }
    _g(n) {
        var p = this.options.o;
        if (n == null) {
            return p
        }
        return p._find(n);
    }
    _show(st) {
        if (st == "hide") {
            if (this._g()._hasClass("ins-open")) {
                this._g()._removeClass("ins-open")
            }
        } else if (st == "show") {
            if (!this._g()._hasClass("ins-open")) {
                this._g()._addClass("ins-open")
            }
        } else {
            if (this._g()._hasClass("ins-open")) {
                this._g()._removeClass("ins-open")
            } else {
                this._g()._addClass("ins-open")
            }
        }
    }
    _update(v) {
        this._show("hide");
        this._g(".-auto-list-input-inp")._setValue(v._getData("value"))
        this._g(".-auto-list-value-inp ")._setValue(v._getHtml())
    }
    _update_active(v) {


        var d = true;

        if (v == "down") {
            var i = this._g("li.ins-active")._get("index")

            var c = this._g("li.ins-vis")._get("count")


            if (i < (c - 2)) {

                var act = this._g("li.ins-vis")._get(i + 1)

                //  ins(".-auto-list-inp")._get(0).scrollBy(0, 40)
                d = true

            } else {

                d = false
            }





        } else if (v == "up") {

            var i = this._g("li.ins-active")._get("index")
            if (i > 0) {
                var act = this._g("li.ins-vis")._get(i - 1)
                    //ins(".-auto-list-inp")._get(0).scrollBy(0, -40)
                d = true

            } else {

                d = false
            }



        } else {
            var act = this._g("li.ins-vis")._get(0)
        }

        if (d) {
            this._g("li")._removeClass("ins-active");
            act.classList.add("ins-active");
        }
    }
    _actions() {



        if (this._g("li.-set-selected") != null) {


            this._update(this._g("li.-set-selected"));


        }

        this._g(".-auto-list-show-btn")._on("click", (o) => {
            this._show();
            this._g(".-auto-list-value-inp ")._get(0).focus({ focusVisible: true });
            this._update_active("");
        }, true)
        this._g("li")._on("click", (o) => {
            this._update(o);
        }, true)
        var items = this._g("li")._get()

        this._g(".-auto-list-value-inp ")._on("focusout", (o, e) => {
            this._update(this._g("li.ins-active"));

        })


        this._g(".-auto-list-value-inp ")._on("keyup", (o, e) => {
            if (!this._g()._hasClass("ins-open")) {
                this._g()._addClass("ins-open")
            }


            console.log(e.keyCode);
            if (e.keyCode == 27) {
                this._show("hide");
            } else if (e.keyCode == 13) {
                this._update(this._g("li.ins-active"));
            } else if (e.keyCode == 40) {
                this._update_active("down");
            } else if (e.keyCode == 38) {
                this._update_active("up");
            } else {
                if (this._g("li.ins-from-input") != null) {
                    this._g("li.ins-from-input")._remove()
                }
                var v = o._getValue();
                items.forEach(element => {
                    if (element.innerText.toLowerCase().search(v.toLowerCase()) > -1) {
                        element.classList.remove("ins-hidden");
                        element.classList.add("ins-vis");
                    } else {
                        element.classList.add("ins-hidden");
                        element.classList.remove("ins-vis");
                    }
                });
                if (this._g("li.ins-vis") == null) {
                    ins(".-auto-list-inp")._append('<li data-value="' + v + '" class="ins-col-12 ins-from-input  ins-vis">' + v + '</li>')
                }
                this._update_active("");
            }
        }, true)
    }
    _out() {
        this._actions()
    }
}