export class InsVHelper {
    constructor(t, THREE) {
        this.parent = t;
        this.three = THREE;
    }


    _on(selector, event, callback, useCapture = true) {
        document.addEventListener(event, function (e) {
            const targets = document.querySelectorAll(selector);
            targets.forEach(function (item) {
                if (item === e.target || item.contains(e.target)) {
                    callback(e.target, e, item);
                }
            });
        }, useCapture);
    }




    _updateAttr(selector, attar_name, value) {
        const targets = document.querySelectorAll(selector);
        targets.forEach(function (item) {
            item[attar_name] = value
        });
    }


    _ajax = function (url, options, callback, onprogress, type = "POST") {
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


}



