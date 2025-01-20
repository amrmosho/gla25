/**
 *
 * @param {type} options {title:$title,url:$url ,style:$style ,class:$class,data:$data,onclose:function(){},onopen:function(){}}
 * @returns {undefined}
 */
export class ins_plg_data {
    options = {};
    o;
    constructor(o) {
        this.options.options = o;
        this.options.o = this.options.options.o;
    }
    _get = function(w = "") {
        var en = {
            operation_done_msg: "operation done successfully ",
            operation_error_msg: "operation Error ",
            months: [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "Novemeber",
                "Decemeber",
            ],
            days: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        };
        var ar = {
            operation_done_msg: "تم العمليه بنجاح  ",
            operation_error_msg: "حدث مشلكله اثناء العمليه ",
            months: [
                "يناير",
                "فبراير",
                "مارس",
                "ابريل",
                "مايو",
                "يونيو",
                "يوليو",
                "أغسطس",
                "سبتمبر",
                "أكتوبر",
                "نوفمبر",
                "ديسمبر",
            ],
            days: [
                "الاحد",
                "الاثنين",
                "الاثنين",
                "الاربعاء",
                "الخميس",
                "الجمعة",
                "السبت",
            ],
        };
        var r = "";
        if (ins()._map._lang() == "ar") {
            r = ar[w];
        } else {
            r = en[w];
        }
        return r;
    };
    _interval = function(code, time) {
        setInterval(code, time);
    };
    _settimer = function(time, code) {
        setInterval(code, time);
    };
    _json_join = function(object1, object2) {
        return Object.assign(object1, object2);
    };
    _timer = function(options) {
        var t = this;
        options.end = options.end ? options.end : false;
        options.repeat = options.repeat !== undefined ? options.repeat : true;
        options.time = options.time ? options.time : 1000;
        if (!options.end) {
            window.setTimeout(function() {
                options = options.func(options);
                if (options.repeat === true) {
                    t._timer(options);
                } else if (options.repeat > 0) {
                    options.repeat--;
                    t._timer(options);
                }
            }, options.time);
        }
    };
    _date_gettoday = function(time, code) {
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth() + 1; //January is 0!
        var yyyy = today.getFullYear();
        if (dd < 10) {
            dd = "0" + dd;
        }
        if (mm < 10) {
            mm = "0" + mm;
        }
        return yyyy + "-" + mm + "-" + dd;
    };
    _date_offset = function(date, offset, operation = "plus") {
        var d = new Date(date);
        if (operation == "minus") {
            d.setDate(d.getDate() - offset);
        } else {
            d.setDate(d.getDate() + offset);
        }
        var curr_date = d.getDate();
        var curr_month = d.getMonth() + 1;
        var curr_year = d.getFullYear();
        d = curr_year + "-" + curr_month + "-" + curr_date;
        return d;
    };
    _generatePassword = function(length = 8) {
        var charset =
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
            retVal = "";
        for (var i = 0, n = charset.length; i < length; ++i) {
            retVal += charset.charAt(Math.floor(Math.random() * n));
        }
        return retVal;
    };
    /*_getmonth = function (i) {
       var mos = [
         "January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "Novemeber",
         "Decemeber",
       ];
       return mos[i];
     };*/
    _page_data = function(page = ".ins_main") {
        return JSON.parse(ins(page)._getData("data"));
    };
    _get_page_data = function(page = ".ins_main") {
        return JSON.parse(ins(page)._getData("data"));
    };
    _set_session = function(name, value, done) {
        return ins()._ajax._send(
            "/ins_ajax/eng/session.php", { status: "set", name: name, value: value },
            "POST",
            done
        );
    };
    _get_session = function(name, done) {
        return ins()._ajax._send(
            "/ins_ajax/eng/session.php", { status: "get", name: name },
            "POST",
            done
        );
    };
    _get_unique_id = function(name, done) {
        return "_" + Math.random().toString(36).substr(2, 9);
    };
    _addtourl = function(url, ...adds) {
        var d = "";
        adds.forEach(function(a) {
            d += "/" + a;
        });
        if (url.indexOf("do") != -1) {
            url += "/";
        } else {
            url += "/do/";
        }
        url += d;
        url = this._replaceAll("///", "/", url);
        url = this._replaceAll("//", "/", url);
        return url;
    };
    _addtomyurl = function(...adds) {
        var d = "";
        var url = ins(this.options.options.o)._getData("url");
        adds.forEach(function(a) {
            d += "/" + a;
        });
        if (url.indexOf("do") != -1) {
            url += "/";
        } else {
            url += "/do/";
        }
        url += d;
        url = this._replaceAll("///", "/", url);
        url = this._replaceAll("//", "/", url);
        return url;
    };
    _getmainurl = function(page = ".ins_main") {
        return this._get_page_data(page).url;
    };
    /*_getdayweek = function (i) {
       var day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
       return day[i];
     };*/
    _replaceAll = function(search, replacement, String = null) {
        if (String === null) {
            String = this.options.options.o
        }
        return String.replace(new RegExp(search, "g"), replacement);
    };
    _exists = function() {
        return !(typeof this.options.options.o === "undefined" || this.options.options.o === null);
    };
    _update_variables = function(search, String = null) {
        var t = this;
        if (String === null) {
            String = this.options.options.o;
        }
        if (!ins(search)._isEmpty()) {
            Object.keys(search).forEach(function(i) {
                String = t._replaceAll("@{" + i + "}", search[i], String);
            });
        }
        return String;
    };
    _is_exists = function(i = false) {
        if (i === true) {
            return !(
                typeof ins(this.options.o)._get(0) === "undefined" || ins(this.options.o)._get(0) === null
            );
        } else {
            return !(typeof this.options.o === "undefined" || this.options.o === null);
        }
    };
    _is_empty = function() {
        return typeof this.options.o === "undefined" || this.options.o === null || this.options.o === "";
    };
    _validateEmail = function(email) {
        var re =
            /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    };
    _formClear = function() {
        ins(this.options.o)
            ._find("input,select,textarea")
            ._each(function(item, indx) {
                item._setvalue("");
            });
    };
    _formUpdate = function(j) {
        ins(this.options.o)
            ._find("input,select,textarea")
            ._each(function(item, indx) {
                var n = item._getattr("name");
                if (!ins(j[n])._isEmpty()) {
                    if (typeof j[n] === "object") {
                        j[n] = JSON.stringify(j[n]);
                    }
                    if (item._getData("type") == "image") {
                        item
                            ._parents(".ui_image")
                            ._find("img")
                            ._setattr("src", "/ins_upload/" + j[n]);
                    }
                    if (item._getData("type") == "ins-checkbox") {
                        if (j[n] == item._getValue()) {
                            console.log(item);
                            console.log(item._getData("type"));
                            item._get(0).checked = true;
                        };
                    }
                    item._setvalue(j[n]);
                }
            });
    };
    _fromSubmit = function(done) {
        var o = this;
        let options = {};
        options.error = false;
        options.error_inputs = [];
        ins(this.options.o)
            ._find("input,select,textarea")
            ._each(function(item, indx) {
                let v = item._getvalue();
                if (!ins(v)._isEmpty()) {
                    if (
                        item._getattr("type") === "checkbox" ||
                        item._getattr("type") === "radio"
                    ) {
                        if (item._get(0).checked) {
                            if (ins(item._getattr("name"))._isExists()) {
                                var n = item._getattr("name");
                                n = n.split("-")[0];
                                if (n.search("]") > 0) {
                                    if (ins(options[n])._isExists()) {
                                        v = options[n] + "," + v;
                                    }
                                }
                                options[n] = v;
                            }
                        }
                    } else if (item._getattr("type") === "email" && !o._validateEmail(v)) {
                        options.error = true;
                        options.error_inputs.push(ins(item)._get(0));
                    } else {
                        if (ins(item._getattr("name"))._isExists()) {
                            var n = item._getattr("name");
                            if (n.search("]") > 0) {
                                if (ins(options[n])._isExists()) {
                                    v = options[n] + "," + v;
                                }
                            }
                            options[n] = v;
                        }
                    }
                    if (
                        ins(item._getattr("required"))._isExists() &&
                        ins(item._getattr("minlength"))._isExists()
                    ) {
                        if (parseInt(item._getattr("minlength")) > v.length) {
                            options.error = true;
                            options.error_inputs.push(ins(item)._get(0));
                        }
                    }
                } else if (
                    ins(item._getattr("required"))._isExists() ||
                    ins(item._getattr("data-required"))._isExists()
                ) {
                    options.error = true;
                    options.error_inputs.push(ins(item)._get(0));
                }
            });
        if (done != null) { done(options); }
    };
    _app_settings_get = function(name = "") {
        var app = this.options.o;
        var app = ins()._data._get_page_data()._myname;
        ins("_get")._ajax._class({ name: name, app: app },
            function(data) {
                ondone(data);
            }, {
                _mypath: "ins_plgs/plg_sys_app_settings/",
                _myname: "plg_sys_app_settings",
            }
        );
    };
    _app_settings_set = function(name, value, ondone) {
        var app = this.options.o;
        var app = ins()._data._get_page_data()._myname;
        ins("_set")._ajax._class({ name: name, value: value, app: app },
            function(data) {
                ondone(data);
            }, {
                _mypath: "ins_plgs/plg_sys_app_settings/",
                _myname: "plg_sys_app_settings",
            }
        );
    };
    _out() {}
}