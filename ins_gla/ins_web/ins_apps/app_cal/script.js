ins(".-type-btn")._on("click", (o) => {
    ins(".-type-btn")._removeClass("ins-active");
    o._addClass("ins-active");
})

ins(".-cal-update-btn")._on("click", (o) => {
    var v = ins(".-cal-update-nput")._getValue();

    window.location = "/plan/" + v + "/";

}, true)