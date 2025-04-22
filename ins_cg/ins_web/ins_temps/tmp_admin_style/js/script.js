ins(".-tp-logout-btn")._on("click", (o) => {
    ins("users/logout")._plg();
}, true)

ins(".-tp-usupdate")._on("click", (o) => {
    var ops = { "name": "gen" };
    var n = o._getData("n");
    var v = o._getData("v");
    ops[n] = v;
    ins("users/set_settings")._plg(ops, (a) => {
        window.location.reload()
    });
}, true)


/*

ins(".-tp-style-light")._on("click", (inp) => {

    ins("users/set_settings")._plg({ "name": "gen", "style": "light" }, (a) => {
        window.location.reload()
    });
}, true)

ins(".-tp-style-dark")._on("click", (inp) => {
    ins("users/set_settings")._plg({ "name": "gen", "style": "dark" }, (a) => {
        window.location.reload()
    });
}, true)*/