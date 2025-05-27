





function hashToInt(code) {
    const colorAsNumber = parseInt(code.slice(1), 16);
    const colorHexFormat = "0x" + colorAsNumber.toString(16);
    return colorHexFormat

}

function update_josn_file(path, jsonData) {


    _send('/ins_ajax/home/app_test/update_data/do/_area/home/_alias/test/', { "data": JSON.stringify(jsonData) }, (data) => {})


}



var _send = function (url, options, callback, onprogress, type = "POST") {
    type = type == null ? "POST" : type;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (callback != null) {
                callback(this.responseText, this);
            }
        } else if (this.readyState == 4) {
            if (callback != null) {
                callback(false);
            }
            console.error("inserror: code(" + this.status + ")\n call url want error\nurl:(" + url + ")\n options:");
            console.error(options);
        }
    };
    xhttp.upload.onprogress = function (e) {
        if (e.lengthComputable) {
        }
    };
    var fd = new FormData();
    try {
        if (options instanceof FormData) {
            fd = options;
        } else if (typeof options === "string") {
            url += "?" + options;
        } else {
            Object.keys(options).forEach(function (k) {
                if (type === "POST") {
                    fd.append(k, options[k]);
                } else {
                    if (url.indexOf("?") == -1) {
                        url += "?";
                    }
                    url += "&" + k + "=" + options[k];
                }
            });
        }
        xhttp.open(type, url, true);
        xhttp.send(fd);
        return xhttp;
    } catch (e) {
        console.log(o);
    }
};