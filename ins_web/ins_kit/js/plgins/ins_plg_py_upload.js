/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_py_upload {
    options = {};
    _files = []
    updateCount = 0;
    filesCount = 0;
    updated = [];
    constructor(o) {
        this.options = o;
    }
    _panel(o) {
        var title = "";
        if (this.options.o._getData("ptitle") != null) {
            title = this.options.o._getData("ptitle");
        } else {
            title = "Upload"
        }
        var f = 'image/png,image/jpg';
        if (!ins(this.options["exts"])._isEmpty()) {
            f = this.options["exts"];
        }
        var size = 3;
        if (!ins(this.options["size"])._isEmpty()) {
            size = this.options["size"];
        }
        var fs = f.split(",");
        var format = '';
        var sp = ' '
        fs.forEach((a) => {
            a = a.replace("image/*", "images")
            a = a.replace("image/", "")
            a = a.replace("application/", "")
            format += `${sp} .${a}`
            sp = ', '
        })
        var id = ins()._data._get_unique_id()
        format += ` and size: ${size}MB`
        var pdata = "<div class='ins-padding-m'>";
        pdata += `<div class='ins-title-m ins-strong'>${title}</div>`;
        pdata += `<div class='-pupload-filea-names ins-paddng-xl'></div>`;
        pdata += "<div class='ins-padding-xl '>";
        pdata += "<div style='height:167px  ;  border: 2px var(--border) dashed;' class='ins-padding-xl -pupload-upload-zone  ins-flex-center ins-card'>";
        pdata += "<div class='  ins-col-6 ins-flex-center'><i class='lni ins-text-center ins-font-2xl ins-col-12 lni-upload'> </i> <span class='ins-col-12'> Drag and drop, or  <label for='" + id + "_file'  class='ins-primary-color'> choose a file</label></span><span class='ins-col-12 ins-font-s'> Accepted formats: " + format + "</span></div>";
        pdata += "</div>";
        pdata += "<div class='ins-flex-end  ins-col-12 ins-padding-m'>";
        if (this.options.mode == "multi") {
            pdata += "<input multiple type='file' accept='" + f + "' id='" + id + "_file' class='-pupload-file-input ins-hidden'>";
            // pdata += "<div class='ins-button -pupload-filea-upload ins-primary ins-col-4'> Confrim </div>";
        } else {
            pdata += "<input  type='file' accept='" + f + "' id='" + id + "_file' class='-pupload-file-input ins-hidden'>";
        }
        pdata += "</div>";
        pdata += "</div>";
        var ops = {
            "title": false,
            data: pdata,
            style: "height:auto;width:630px;",
            data_style: "position: relative;"
        }
        ins()._ui._addLightbox(ops);
    }
    _update_files() {
        var t = this
        var h = "<ul class='ins-flex ins-padding-xl ins-padding-h'>"
        var max = 3;
        if (!ins(this.options["size"])._isEmpty()) {
            max = this.options["size"];
        }
        Array.from(t._files).forEach((a, i) => {
            var _size = a.size;
            i = 0;
            var d = true;
            if (_size > 900) {
                _size /= 1024;
                _size /= 1024;
                _size = (Math.round(_size * 100) / 100);
                if (_size > max) {
                    ins("File exceeded maximum allowed size")._ui._notification({ "class": "ins-danger" })
                    var d = false;
                }
            }
            if (d) {
                var cls = a["name"].replace(".", "_");
                h += `<li class='ins-font-s ins-col-12 ins-flex'>
            <span class='ins-col-11'>${a["name"]}  </span> 
            <i data-i='${i}' class='lni lni-trash-can  ins-button-text -pupload-files-remove'></i>
            <progress class='ins-col-12 -update-lb-progress ${cls}' id="file" value="0" max="100"> 0</progress>
            </li>`
            }
        })
        ins(".-pupload-filea-names")._setHTML(h)
        h += "</ul>"
            // if (this.options.mode != "multi") {
        this._g_upload()
            //}
    }
    _on_done(j) {
        j["p"] = this.options._p;
        if (this.options.mode != null) {
            j["mode"] = this.options.mode;


        }
        if (j["status"] == "-1") {
            ins(j["msg"])._ui._notification({ "class": "ins-danger" })
        } else {
            ins()._ui._removeLightbox()
            if (!ins(this.options["ondone"])._isEmpty()) {
                if (typeof this.options["ondone"] === "string") {
                    window[this.options["ondone"]](j);
                } else {
                    this.options["ondone"](j);
                }
            }
        }
    }
    _on_end(j) {
        j["p"] = this.options._p;

        if (this.options.mode != null) {
            j["mode"] = this.options.mode;


        }

        if (!ins(this.options["onend"])._isEmpty()) {
            if (typeof this.options["onend"] === "string") {
                window[this.options["onend"]](j);
            } else {
                this.options["onend"](j);
            }
        }
    }
    _onprogress(percentComplete, data, options) {
        ins(".-update-lb-progress")._setAttribute("value", percentComplete);
        if (percentComplete == 100) {}
    }
    _upload(data, options) {
        var t = this;
        let xhttp = new XMLHttpRequest();
        console.log(options)
        if (options["dir"] != null) {
            data.dir = options["dir"];
            data.append("dir", options["dir"]);
        }
        if (options["exts"] != null) {
            data.exts = options["exts"];
            data.append("exts", options["exts"]);
        }
        if (options["size"] != null) {
            data.exts = options["size"];
            data.append("size", options["size"]);
        }
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var j = JSON.parse(this.responseText);
                if (j["status"] == 0) {
                    ins(j["msg"])._ui._notification({ "class": "ins-danger" })
                } else {
                    t.updateCount++;
                    t.updated.push(j);
                    t._on_done(j, options);
                    if (t.filesCount == t.updateCount) {
                        t._on_end(t.updated, options);
                        t.updated = [];
                        t.updateCount = 0
                    }
                }
            }
        };
        xhttp.upload.o = options;
        xhttp.upload.onprogress = function(e) {
            if (e.lengthComputable) {
                var percentComplete = (e.loaded / e.total) * 100;
                t._onprogress(percentComplete, data, this.o);
            }
        };
        var url = " /ins_ajax/home/ajx_upload/upload_file/do/_t/ajx/";
        xhttp.open("POST", url, true);
        t.updateCount = 0;
        xhttp.send(data);
        return xhttp;
    }
    _g_upload() {
        var t = this;
        t.filesCount = t._files.length;
        Array.from(t._files).forEach((file) => {
            var data = new FormData();
            data.append("uploads", file);
            t._upload(data, t.options);
        });
    }
    _g(n) {
        return ins(p)._find(n)
    }
    coll_actions = false;
    _actions() {
        var t = this
        ins(".-pupload-file-input")._on("change", (o, ev) => {
            ev.preventDefault()
            t._files = o._get(0).files
            t._update_files();
        })
        ins(".-pupload-upload-zone")._on(
            "drop",
            function(o, ev) {
                ev.preventDefault();
                let dt = ev.dataTransfer
                let files = dt.files
                t._files = files
                t._update_files();
            })
        ins(".-pupload-upload-zone")._on(
            "dragleave",
            function(o, ev) {
                o._removeClass("ins-upload-drop-hover");
            },
            true
        );
        ins(".-pupload-upload-zone")._on(
            "dragleave",
            function(o, ev) {
                ev.preventDefault();
                o._removeClass("ins-upload-drop-hover");
            },
            true
        );
        ins(".-pupload-upload-zone")._on(
            "dragover",
            function(o, ev) {
                ev.preventDefault()
                o._addClass("ins-upload-drop-hover")
            },
            false
        );
        ins(".-pupload-upload-zone")._on(
            "dragenter",
            function(o, ev) {
                ev.preventDefault()
                o._addClass("ins-upload-drop-hover")
            },
            false
        );
        if (this.options.mode != "multi") {
            ins(".-pupload-filea-upload")._on("click", (o) => {
                t._g_upload()
            })
        }
        ins(".-pupload-files-remove")._on("click", (o) => {
            const filesArray = [...t._files];
            filesArray.splice(o._getData("i"), 1);
            const dataTransfer = new DataTransfer();
            filesArray.forEach(file => dataTransfer.items.add(file));
            t._files = dataTransfer.files;
            t._update_files();
            if (t._files.length == 0) {
                ins(".-pupload-file-input")._setValue("");
            }
        })
    }
    _callActions() {
        var t = this
        return function() {
            if (!t.coll_actions) {
                t._actions();
                t.coll_actions = true;
            } else {}
        };
    }
    _out() {
        console.log(this.options);
        const callOnce = this._callActions();
        callOnce()
        this._panel(this.options.o)
    }
}