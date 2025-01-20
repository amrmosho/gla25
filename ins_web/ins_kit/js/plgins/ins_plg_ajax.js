/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_ajax {
    options = {};
    constructor(o) {
        this.options = o;

    }

    _send = function(url, options, callback, onprogress, type = "POST") {



        type = type == null ? "POST" : type;
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {


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
        xhttp.upload.onprogress = function(e) {
            if (e.lengthComputable) {
                var percentComplete = (e.loaded / e.total) * 100;
                if (ins(onprogress)._isExists()) {
                    onprogress(percentComplete, e);
                }
            }
        };
        var fd = new FormData();
        try {

            if (options instanceof FormData) {
                fd = options;
            } else if (typeof options === "string") {
                url += "?" + options;
            } else {
                Object.keys(options).forEach(function(k) {
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


    _myClass = function(data, callback, addoptions = null) {
        var options = ins()._data._get_page_data();

        if (ins(addoptions)._isExists()) {
            Object.keys(addoptions).forEach(function(k) {
                k = k.trim();
                options[k] = addoptions[k];
            });
        }


        Object.keys(data).forEach(function(k) {
            options[k] = data[k];
        });
        options.get_file = "eng/get_class_ajax";


        if (ins(options.ajaxstatus)._isEmpty()) {
            options.ajaxstatus = this.options.o;
        }
        if (ins(options.lang)._isEmpty()) {
            options.lang = ins("body")._getData("lang");
        }
        return this._send("/ins_ajax.php", options, callback);
    };
    /**
     *
     * @param {type} options :{}
     * @param {type} callback
     * @param {type} file :/ajax/actions.php
     * @returns {unresolved}
     *
     */
    _myFloder = function(data, callback, file) {
        if (file == null) {
            file = "/ajax/actions";
        }
        var options = ins()._data._get_page_data();
        Object.keys(data).forEach(function(k) {
            options[k] = data[k];
        });
        options.myname = options["_myname"];
        options.root = "true";
        options.get_file = "/" + options["_mypath"] + file;
        if (ins(options.lang)._isEmpty()) {
            options.lang = ins("body")._getData("lang");
        }

        return this._send("/ins_ajax.php", options, callback);
    };
    /**
     * 
     * @param {String} to  file 'eng/lang'
     * @param {Json} options  options 'will send to file'
     * @param {Function} callback  'data: get data'
     */
    _myAjax = function(to, options, callback) {
        /** @var {ins_plg_ajax} cls  */

        var moptions = ins()._data._get_page_data();

        Object.keys(options).forEach(function(k) {
            k = k.trim();
            moptions[k] = options[k];
        });



        moptions["get_file"] = to;


        this._send("/ins_ajax.php", moptions, callback);
    };
    /**
     *
     * @param {type} attrs {url,options,callback}
     * @returns {Ajax.prototype._send.xhttp|XMLHttpRequest}
     */
    _get = function(url, options, onprogress) {
        return this._send(
            url, options, callback, onprogress, "GET"
        );
    };


    _json = (file, ondone, path = "/ins_lib/includes/json/") => {


            fetch(path + file)
                .then((response) => response.json())
                .then(ondone);
        }
        /** load main component */
    _load = function(to, options, callback) {
        var url = ins()._data._addtourl(to, "/get_tmp_index/ins_main");
        this._send(url, options, callback);
    };
    _abort = function(ajax) {
        if (!ins(ajax)._data._exists()) {
            ajax = ins_jax;
        }
        if (ins(ajax)._data._exists()) {
            ajax.abort();
        }
        return this;
    };
    _updateComponent = function(addtourl = "", to = ".ins_main", done = function() {}) {

        var url = "/" + ins()._data._getmainurl(to);

        url = ins()._data._addtourl(url, "/get_tmp_index/ins_main", addtourl);
        ins()._ui._page_progress_run();




        return this._myAjax(
            "eng/get_main", ins()._map._get(),
            function(data) {


                var d = ins()._ui._create("div");
                ins(d)._sethtml(data);
                var h = ins(d)._gethtml();
                if (to == ".ins_main") {
                    h = "<div class='ins_mian_data'>" + h + "</div>";
                }
                ins(to)._sethtml(h);
                ins()._ui._page_progress_hide()
                done();
            },
        );
    };

    _out() {

    }
}