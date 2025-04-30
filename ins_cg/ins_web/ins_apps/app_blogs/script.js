ins(".-category-checkbox")._on("change", function(o) {
    if (o._get(0).checked) {
        ins(".-category-checkbox")._each(function(item) {
            item._get(0).checked = false;
        });
        o._get(0).checked = true;
        url = ins()._map._hurl({ "mode": o._getData("alias") }, "page")
    } else {
        o._get(0).checked = false;
        url = ins()._map._hurl({}, "mode")
    }
    window.location = url;
}, true);

function get_page(page) {
    ins(".ins-pagination-btn")._removeClass("active");

    url = ins()._map._hurl({ "page": page })
    window.location = url
}

ins(".ins-pagination-btn")._on("click", (o) => {
    var page = o._getData("page");
    var currentPage = parseInt(ins(".ins-pagination-btn.ins-active")._getData("page"), 10);
    if (page === "prev") {
        if (currentPage > 1) {
            get_page(currentPage - 1);
        }
    } else if (page == "next") {
        var numPages = o._getData("tpages");

        if (currentPage < numPages) {
            get_page(currentPage + 1);
        }
    } else if (page != currentPage) {
        get_page(parseInt(page, 10));
        o._addClass("active");
    }
}, true);