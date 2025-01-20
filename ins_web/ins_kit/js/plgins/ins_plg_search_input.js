/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_search_input {
    options = {};
    constructor(o) {
        this.options = o;



    }
    _uselect(o) {



        if (o != null) {
            var options = this._options(o);

            var h = o._getHtml();
            o._parents(".ins-list-fix")._find(".ins-plg-search-value-input")._setValue(o._getData("value"));
            o._parents(".ins-list-fix")._find(".ins-plg-search-value-ui")._setHtml(h);
            o._parents(".ins-list-fix")._removeClass("ins-opend");

            o._parents(".ui_parent")._removeclass("ins-from-input-error")

            if (!ins(options["onchange"])._isEmpty()) {

                window[options["onchange"]](o, o._getData("value"));
            }
        }


    }

    _parent(o) {
        return o._parents(".ins-list-fix")
    }
    _get(o, g) {
        return this._parent(o)._find(g);
    }

    _options(o) {
        var c = this._get(o, ".ins-plg-search-input")._getData("data");
        return JSON.parse(c);
    }




    _out() {


        var sl = this;
        ins(".ins-list-fix-open-btn")._on("click", function(o) {
            o._parents(".ins-list-fix")._addClass("ins-opend");
            ins(".ins-plg-search-input")._focus();
        }, true)
        ins(".ins-list-close-btn")._on("click", function(o) {
            o._parents(".ins-list-fix")._removeClass("ins-opend");
        }, true)
        ins(".ins-plg-search-results-item")._on("click", function(o) {
            sl._uselect(o);
        }, true)
        var activeLimt = 50;
        var activeIndex = 0;





        ins(".ins-plg-search-input")._on(
            "keydown",
            function(o, e) {
                if (e.keyCode == 13 || e.keyCode == 38 || e.keyCode == 40) {
                    e.preventDefault();
                }




            });

        ins(".ins-plg-search-input")._on(
            "keyup",
            function(o, e) {
                if (e.keyCode == 13) {
                    e.preventDefault();
                    if (ins(".ins-plg-search-results-item.ins-active")._isExists(true)) {
                        var o = ins(".ins-plg-search-results-item.ins-active");



                        sl._uselect(o);
                    }
                }
                if (e.keyCode == 38) {
                    e.preventDefault();
                    activeIndex--;
                    if (activeIndex < 0) {
                        activeIndex = activeLimt - 1;
                    }
                    ins(".ins-plg-search-results-item")._removeClass("ins-active");
                    var o = ins(ins(".ins-plg-search-results-item")._get(activeIndex))._addClass("ins-active");
                }
                if (e.keyCode == 40) {
                    e.preventDefault();
                    activeIndex++;
                    if (activeLimt <= activeIndex) {
                        activeIndex = 0;
                    }
                    ins(".ins-plg-search-results-item")._removeClass("ins-active");
                    var o = ins(ins(".ins-plg-search-results-item")._get(activeIndex))._addClass("ins-active");
                }
            }
        );
        ins(".ins-plg-search-input")._on("input", function(o) {
            ins(".ins-plg-search-results-area")._ui._addloader();
            var c = o._getData("data");
            var options = JSON.parse(c);
            options.value = o._getValue(o);
            if (options.value.length > 0) {
                ins()._ajax._to("inputs/search", options, function(data) {
                    activeIndex = 0;
                    if (data.trim() == "") {
                        sl._parent(o)._find(".ins-plg-search-results-area")._setHtml("<p class='ins-warning-color'> <i class='lni lni-warning'></i> No results found.</p>");
                    } else {
                        sl._parent(o)._find(".ins-plg-search-results-area")._setHtml(data);
                        activeLimt = ins(".ins-plg-search-results-item")._get().length;
                    }
                    ins()._ui._removeloader();
                });
            } else {
                sl._parent(o)._find(".ins-plg-search-results-area")._setHtml("<p class='ins-info-color'> <i class='lni lni-keyboard'></i> Type your search query.</p>");
                ins()._ui._removeloader();
            }
        })
    }
}