ins(".-pro-action")._on("click", (o) => {
    ins("ins_cg.app_products._pro_action")._ajax._app(o._getData(), (data) => {
        if (data.trim() == "1") {
            o._addClass("ins-primary")
        } else {
            o._removeClass("ins-primary")
        }
    })
}, true)