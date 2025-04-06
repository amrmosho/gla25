ins(".wi-pros-tab-btn")._on("click", function(o) {
    var v = o._getData("view")
    ins(".wi-pros-tab-btn")._removeClass("gla-active")
    o._addClass("gla-active")
    ins(".wi-pros-tab-cont")._removeClass("gla-show")
    ins(v)._addClass("gla-show")
    ins(".-view-more-btn")._setAttribute("href", o._getData("url"))

}, true)
ins(() => {})._load()