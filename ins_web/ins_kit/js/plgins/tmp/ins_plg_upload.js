export class ins_plg_upload {
    options = {};
    constructor(o, id) {
        this.options = o;
    }
    update(dir) {
        this.options["dir"] = dir;
    }
    _progressbar = "";
    _on_done(j) {
        if (!ins(this.options["ondone"])._isEmpty()) {
            if (typeof this.options["ondone"] === "string") {
                window[this.options["ondone"]](j);
            } else {
                this.options["ondone"](j);
            }
        }
    }
    _on_end(j) {
        if (!ins(this.options["onend"])._isEmpty()) {
            if (typeof this.options["onend"] === "string") {
                window[this.options["onend"]](j);
            } else {
                this.options["onend"](j);
            }
        }
    }
    _onprogress(percentComplete, data, options) {
        var filedata = data.get("uploads");




        if (!ins(options["file_progres"])._isEmpty()) {
            ins(options["file_progres"])._css({ width: percentComplete + "%" });
        }
        if (!ins(options["file_percenting"])._isEmpty()) {
            ins(options["file_percenting"])._settext(
                Math.round(percentComplete) + "%"
            );
        }
        if (!ins(options["file_progres_circle"])._isEmpty()) {
            ins(options["file_progres_circle"])._setattr(
                "stroke-dasharray",
                Math.round(percentComplete) + ",100"
            );
        }
        if (!ins(options["file_title"])._isEmpty()) {
            var str = filedata["name"];
            if (str.length > 12) str = str.substring(str.length - 12, str.length);
            ins(options["file_title"])._settext(str);
        }
        if (percentComplete == 100) {

            if (options["file_info"] == "msg") {

            } else {

                ins(options["file_info"])._remove();



            }
            //  ins(options["file_percenting"]).
        }



    }
    updateCount = 0;
    filesCount = 0;
    updated = [];
    _upload(data, options) {
        var t = this;
        let xhttp = new XMLHttpRequest();
        /** full pass folder */
        /** path in ins_upload folder */
        if (options["dir"] != null) {
            data.dir = options["dir"];
            data.append("dir", options["dir"]);
        }
        /** path in ins_upload folder */
        if (options["path"] != null) {
            data.path = options["path"];
        }
        if (options["exts"] != null) {
            data.exts = options["exts"];
            data.append("exts", options["exts"]);
        }





        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var j = JSON.parse(this.responseText);

                console.log(j);
                console.log(j["status"]);

                if (j["status"] == 0) {

                    ins(j["msg"])._ui._notification({ "class": "ins-danger" })

                } else {

                    t.updateCount++;
                    t.updated.push(j);
                    t._on_done(j, options);
                    if (t.filesCount == t.updateCount) {
                        t._on_end(t.updated, options);
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






        var url = "/ins_ajax.php?get_file=/eng/upload_1";
        xhttp.open("POST", url, true);
        xhttp.send(data);
        return xhttp;
    }

    _update_ui(options) {




        if (!ins(options["file_info"])._isEmpty()) {


            if (options["file_info"] == "msg") {

                var infoid = ins()._data._get_unique_id();
                var h = '<div class="' + infoid + ' ins-flex " ><div class="ins-uploader-file-title ins-padding-m  ins-col-10"> percenting </div> <div class="ins-uploader-file-percenting ins-padding-m   ins-col-2">  </div><div style="height: 23px;top: auto;bottom: 0;" class="ins-progress-bar  ins-success  ins-uploader-file-progres">  </div></div>';
                ins(h)._ui._note({ "class": infoid + "_p ins-info" })
                options["file_info"] = "." + infoid + "_p"
                options["file_title"] = "." + infoid + " .ins-uploader-file-title";
                options["file_progres"] = "." + infoid + " .ins-uploader-file-progres";
                options["file_percenting"] = "." + infoid + " .ins-uploader-file-percenting";



            } else {



                var p = ins(options["file_info"])._parent();
                var m = ins(options["file_info"])._get(0);
                var c = ins(m)._clone();

                var id = ins()._data._get_unique_id();


                c._removeclass("ins-hidden");
                c._addclass(id);
                c._addclass("ins-uploader-file-info-item")
                p._append(c);
                options["file_info"] = options["file_info"].trim() + "." + id;





                ins(options["file_info"])._removeclass("ins-hidden");
                if (
                    ins(options["file_info"] + " .ins-uploader-file-title")._isExists(true)
                ) {
                    options["file_title"] = options["file_info"] + " .ins-uploader-file-title";
                }
                if (
                    ins(options["file_info"] + " .ins-uploader-file-progres")._isExists(
                        true
                    )
                ) {
                    options["file_progres"] =
                        options["file_info"] + " .ins-uploader-file-progres";
                }
                if (
                    ins(options["file_info"] + " .ins-uploader-file-percenting")._isExists(
                        true
                    )
                ) {
                    options["file_percenting"] =
                        options["file_info"] + " .ins-uploader-file-percenting";
                }
                if (
                    ins(options["file_info"] + " .ins-uploader-file-circle")._isExists(
                        true
                    )
                ) {
                    options["file_progres_circle"] =
                        options["file_info"] + " .ins-uploader-file-circle";
                }
            }
        }

        return options;
        g
    }


    _m_files(file) {
        var t = this;
        if (!ins(t.options["file_info"])._isEmpty()) {
            var options = JSON.parse(JSON.stringify(t.options));
            options = t._update_ui(options);
            var data = new FormData();
            data.append("uploads", file);
            t._upload(data, options);
        }
    }


    _change() {
        var t = this;

        var e = t.options["o"]._get(0);
        console.log(t.options["o"]._get(0));
        t.updateCount = 0;
        t.updated = [];
        t.filesCount = e.files.length;
        Array.from(e.files).forEach((file) => {
            t._m_files(file);
        });

    }
    _out() {
        var t = this;

        console.log(t.options);


        if (typeof t.options["o"] == "string") {

            t.options["o"] = ins(t.options["o"]);

        }


        t.options["o"]._on(
            "change",
            function(o) {

                t._change();

            },
            false
        );
        if (!ins(this.options["drop_area"])._isEmpty()) {
            ins(this.options["drop_area"])._on(
                "drop",
                function(o, ev) {

                    ev.preventDefault();
                    let dt = ev.dataTransfer
                    let files = dt.files
                    t.updateCount = 0;
                    t.updated = [];
                    t.filesCount = files.length;
                    Array.from(files).forEach((file) => {
                        t._m_files(file);
                    });
                    o._removeclass("ins-upload-drop-hover");
                },
                false
            );
            ins(this.options["drop_area"])._on(
                "dragleave",
                function(o, ev) {
                    ev.preventDefault();
                    o._removeclass("ins-upload-drop-hover");
                },
                true
            );
            ins(this.options["drop_area"])._on(
                "dragover",
                function(o, ev) {
                    ev.preventDefault()
                    o._addclass("ins-upload-drop-hover")
                },
                false
            );
            ins(this.options["drop_area"])._on(
                "dragenter",
                function(o, ev) {
                    ev.preventDefault()
                    o._addclass("ins-upload-drop-hover")
                },
                false
            );
        }
    }
}