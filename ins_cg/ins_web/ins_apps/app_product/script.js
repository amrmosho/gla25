ins(".-add-new-item")._on("click", (o) => {
    ins("_add_new_item")._ajax._app({}, (data) => {
        ins(".-subtypes-area")._append(data)
    })
}, true)



ins(".-order-inpt")._on("change", (o) => {
    update_data("", o)
})


ins(".-types-select")._on("change", (o) => {
    update_data("", o)
})

ins(".-label-select")._on("change", (o) => {
    update_data("", o)
})


ins(".-remove-item")._on("click", (o) => {

    if (confirm("Are you sure you want to delete this item?")) {
        p = o._parents(".-subtypes-row");
        ops = o._getData();
        ops.area = ins(".-subtypes-textarea")._getValue();
        ins("_remove_item")._ajax._app(ops, (data) => {
            p._remove()
            ins(".-subtypes-textarea")._setValue(data)

        })


    }

})


function update_data(type, o) {
    if (type == "images") {
        var p = ins(o)._parents(".-subtypes-row");
    } else if (type == "rimages") {
        var p = ins("." + o)._parents(".-subtypes-row");
    } else {
        var p = o._parents(".-subtypes-row");
    }
    const uid = p._getData("uid");
    const textarea = ins(".-subtypes-textarea");
    var paths = "";
    var sp = "";

    var found = false;
    ins(p._find(".-img-remove"))._each((i) => {
        if (i._getData("p") != "" && i._getData("p") != undefined) {
            paths += sp + i._getData("p");
            sp = ",";
            found = true;
        } else {
            found = false
        }
    });

    if (!found) {
        ins(p._find(".-img-cont"))._each((i) => {
            if (i._getData("p") != "" && i._getData("p") != undefined) {

                paths += sp + i._getData("p");
                sp = ",";
            }
        });
    }




    var order = p._find(".-order-inpt")._getValue();
    var label = p._find(".-label-select")._getValue();
    const data = {
        area: textarea._getValue() || "{}",
        subtype: p._find(".-types-select")._getValue(),
        uid: uid,
        order: order,
        images: paths,
        label: label
    };
    ins("_update_product_type")._ajax._app(data, (response) => {
        try {
            const newData = JSON.parse(response);
            textarea._setValue(JSON.stringify(newData, null, 2));
        } catch (e) {
            const currentValue = textarea._getValue();
            try {
                JSON.parse(currentValue);
            } catch {
                textarea._setValue("{}");
            }
        }
    }, (error) => {
        console.error("Request failed:", error);
    });
}



function m_actions(ds) {
    var data = ds;
    if (ds["p"] != "") {
        var paths = "";
        var sp = "";
        data.forEach(element => {
            if (element != "") {
                var imgs = "<div class='-img-cont'> <i  data-p='" + element.path + "' class='lni lni-xmark  ins-rounded ins-danger  ins-button-text -remove-img'></i> <img src='" + element.fullpath + "' /></div>";
                var imgs = "<div data-p='" + element.path + "'  draggable= 'true' class='-img-cont ins-flex-center'>" +
                    "<div  class='lni lni-menu-meatballs-1  ins-rounded ins-dark -img-darg'></div>" +
                    "<div class='lni lni-xmark  ins-rounded ins-danger ins-button-text -img-remove'></div>" +
                    "<a target='_blank'  href='" + element.fullpath + "' class='lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link'></a>" +
                    "<img src='" + element.fullpath + "' /></div>";
                ins(ds["p"])._find(".ins-form-upload-imgs")._append(imgs)
                paths += sp + element.path;
                sp = ",";
            }
        });
        ins(ds["p"])._find("input")._setValue(paths)
    }
}

function reval(p) {
    var sp = "";
    var paths = "";
    ins("." + p + " .-img-cont ")._each((i) => {
        paths += sp + i._getData("p");
        sp = ",";
    })
    update_data("rimages", p)

}

ins(".-img-cont")._on("drop", (o, ev) => {
    ev.preventDefault()
    var drag_object = ins("#" + ev.dataTransfer.getData("text"));
    drag_object._removeClass("-img-drag");
    ins(o)._appendBefor(drag_object);
    var p = drag_object._parents(".ins-form-upload-imgs-cont")._getData("id");
    reval(p)
})

ins(".ins-form-upload-cont .-img-remove ")._on("click", (o) => {
    var p = o._parents(".ins-form-upload-imgs-cont")._getData("id");
    o._parent()._remove()
    reval(p)
}, true);


var ondone = function(ds) {
    m_actions(ds);
    let data = {
        paths: [],
        p: ds.p
    };

    ds.forEach((d) => {
        data.paths.push(d.path);
    });

    update_data("images", ds.p)


};





var options = {
    o: ins(".-upload-image"),
    onend: ondone,
    dir: "images/products",
    "mode": "multi"
}
ins(".-upload-image")._on("click", (o) => {
    options._p = "." + o._getData("p");
    ins("ins_plg_py_upload")._plgin(options,
        function(plg) {}
    );

}, true)

ins(function() {

    var g = ins()._map._get();
    if (g["mode"] == "edit") {
        ins()._ui._addLoader()
        setTimeout(() => {
            ins("_fill_subtype_area")._ajax._app({ "pid": g["id"] }, (data) => {
                var jdata = JSON.parse(data)
                ins(".-subtypes-area")._setHTML(jdata["ui"])
                ins(".-subtypes-textarea")._setValue(jdata["textarea"])
                ins()._ui._removeLoader()

            })

        }, 1000);
    }

})._load()