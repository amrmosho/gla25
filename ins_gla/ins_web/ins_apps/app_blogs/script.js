function actions(ds) {

    if (ds["p"] != "") {
        var imgs = "<div data-p='" + ds[0].path + "' class='-img-cont ins-flex-center'><div class='lni lni-xmark  ins-rounded ins-danger    ins-button-text -img-remove'></div>" +
            "<a target='_blank'  href='" + ds[0].fullpath + "' class='lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link'></a>  <img src='" + ds[0].fullpath + "' /></div>";
        var paths = ds[0].path;
        ins(ds["p"])._find("input")._setValue(paths)
        ins(ds["p"])._find(".ins-form-upload-imgs")._setHTML(imgs)
    }
}


var ondone = function(ds) {
    console.log(ds);
    //  actions(ds)
};

var options = {
    o: ins(".-upload-image  "),
    onend: ondone,
    dir: "usss",
    "mode": "multi"
}
ins(".-upload-image")._on("click", (o) => {
    options._p = "." + o._getData("p");
    ins("ins_plg_py_upload")._plgin(options,
        function(plg) {}
    );

}, true)