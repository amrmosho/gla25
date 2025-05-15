ins(".-open-panel")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active");
    } else {
        o._addClass("ins-active");
    }
}, true)
ins(".-minus-btn")._on("click", (o) => {
    if (ins(".count-inpt")._getValue() > 1) {
        ins(".count-inpt")._setValue(ins(".count-inpt")._getValue() - 1);
    }
}, true)
ins(".-plus-btn")._on("click", (o) => {
    let val = parseInt(ins(".count-inpt")._getValue(), 10);
    ins(".count-inpt")._setValue(val + 1);
}, true)






ins(".-pro-d-tabs")._on("click", (o) => {
    ins(".-pro-d-tabs")._removeClass("ins-primary")
    o._addClass("ins-primary")
    ins(".-pro-d-cont")._addClass("ins-hidden")
    ins("." + o._getData('s'))._removeClass("ins-hidden")

}, true)





ins(".p-comments-btn")._on("click", (o) => {



    ins(".p-comments-cont")._data._submit((data) => {

        ins("plg_comments.ajax")._ajax._plgin(data, (data) => {

            ins(".p-comments-data")._setHTML(data);
        })

    })


})





ins(".-filter-menu")._on("click", (o) => {
    if (ins(".-filter-area")._hasClass("menu-open")) {
        ins(".-filter-area")._removeClass("menu-open")
    } else {
        ins(".-filter-area")._addClass("menu-open")
    }
}, true);



ins(".-close-filter")._on("click", (o) => {
    ins(".-filter-area")._removeClass("menu-open")

}, true);




ins(".-continue-shopping-btn")._on("click", (o) => {
    ins(".ins-panel-overlay.ins-opened")._remove()
    ins()._ui._removeLightbox();
}, true)


/**Filter Area */


