ins(".blog-next-btn")._on("click", function(o) {


    var next = ins(".blog-next-btn")._getData("next")





    ins("a")._ajax._app({ "n": next }, function(data) {


        ins(".blog-items-area ")._setHTML(data);


    })









}, true)