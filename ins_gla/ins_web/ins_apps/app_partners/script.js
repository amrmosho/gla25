ins(".-area-select")._on("change", (o) => {
    var val = o._getValue();
    if (val == "all") {
        ins(".pro-partner-block")._removeClass("ins-hidden");
    } else {
        ins(".pro-partner-block")._addClass("ins-hidden");
        ins(".pro-partner-block._" + val)._removeClass("ins-hidden");
    }
})