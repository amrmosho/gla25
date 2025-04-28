// Active main image
function getId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ?
        match[2] :
        null;
}

function getsk(url) {
    var c = url.split("-")
    var c = c[c.length - 1];
    return '<div class="sketchfab-embed-wrapper ins-col-12 -render-object"> <iframe style="width:100%;height:550px" title="Ray-Ban Meta Wayfarer Matte and Shiny" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/' + c + '/embed"> </iframe></div>'
}

function youtube(url) {
    var c = url.split("-")
    var c = c[c.length - 1];
    var id = getId(url)
    console.log(getId(url));
    url = '//www.youtube.com/embed/' + id
    return '<div class="ins-col-12 -render-object"> <iframe style="width:100%;height:550px"  src="' + url + '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
}
ins(".-side-img")._on("click", (o) => {
    var ops = o._getData()
    var p = o._parent(".-side-img-cont");
    ins(".-side-img")._removeClass("ins-active");
    ins(".-side-img-cont")._removeClass("ins-active");
    o._addClass("ins-active");
    p._addClass("ins-active");
    ins(".-main-img")._addClass("gla-ahide");
    ins(".-main-img-cont .-render-object")._remove();
    if (o._getData("type") == "img") {
        ins(".-main-img")._removeClass("ins-hidden");
        setTimeout(() => {
            ins(".-main-img")._setAttribute("src", ops["src"]);
            ins(".-main-img")._removeClass("gla-ahide");
        }, 100);
    } else {
        ins(".-main-img")._addClass("ins-hidden");
        if (ops["type"] == "youtube") {
            ins(".-main-img-cont")._append(youtube(ops["src"]));
        } else {
            ins(".-main-img-cont")._append(getsk(ops["src"]));
        }
    }
}, true)