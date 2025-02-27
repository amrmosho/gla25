ins(".ap-ai-btn")._on("click", (o) => {
    ins(".ap-ai-data")._setHTML("")

    var v = ins(".ap-ai-txt")._getValue();
    ins("_get")._ajax._app({ "v": v }, (o) => {

        ins(".ap-ai-data")._setHTML("<pre>" + o + "</pre>")
        console.log(o)
    })

})