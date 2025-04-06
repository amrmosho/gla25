ins(".wi-slideshow-th-item")._on("click", function(o) {
    var indx = o._getData("in");
    trsn(indx)
}, true)
ins(".wi-slideshow-slide")._on("swiped-left", function(o) {
    var ins_shc = 3;
    indx++;
    if (indx > ins_shc) {
        indx = 1
    }
    trsn(indx)
}, true)
indx = 1
var cc

function trsn(indx) {
    ins(".wi-slideshow-th-item")._removeClass("active")
    ins(".wi-slideshow-th-item._" + indx)._addClass("active")
    ins(".wi-slideshow-slide")._setCSS({ "z-index": "0" })
    ins(".wi-slideshow-slide._" + indx)._setCSS({ "z-index": "1" })
    ins(".wi-slideshow-slide")._addClass("_other")
    ins(".wi-slideshow-slide._" + indx)._removeClass("_other")
    ins(".wi-slideshow-slide")._removeClass("opa_0")
    ins(".wi-slideshow-slide._" + indx)._addClass("loaded", "active")
    setTimeout(() => {
        ins(".wi-slideshow-slide._other")._removeClass("loaded", "active")
        ins(".wi-slideshow-slide._other .wi-slideshow-data")._removeClass("opa_1")
        ins(".wi-slideshow-slide._" + indx + " .wi-slideshow-data")._addClass("opa_1")
    }, 800);
    clearTimeout(cc);
    cc = setTimeout(() => {
        var ins_shc = 3;
        indx++;
        if (indx > ins_shc) {
            indx = 1
        }
        trsn(indx);
    }, 10000);
}
ins(() => {
    trsn(indx);
})._load()