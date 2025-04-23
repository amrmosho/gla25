ins(".gla-ltabs")._on("click", (o) => {
    var indx = o._getData("show");

    ins(".gla-ltabs-item")._removeClass("active")
    ins(".gla-ltabs-item." + indx)._addClass("active")

    ins(".gla-ltabs")._removeClass("gla-active")
    o._addClass("gla-active")




}, true)