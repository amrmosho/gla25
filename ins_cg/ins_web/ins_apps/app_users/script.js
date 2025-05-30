ins(".-guser-login-btn")._on("click", (o) => {
    ins(".-login-form")._data._submit(function(data) {
        ins("_login")._ajax._app(data, (d) => {

            if (d == "-1") {
                ins("Invalid login data")._ui._notification({ "class": "ins-danger" })
            } else {
                ins("Login successfully")._ui._notification()
                ins(".-login-form")._ui._addLoader()
                setTimeout(() => {
                    window.location.reload()
                }, 3000);

            }

        })
    })
}, true)

ins(".-add-address-btn")._on("click", (o) => {
    ins(".-add-address-area")._data._submit(function(data) {
        ins("_add_address")._ajax._app(data, (d) => {
            ins(".-addresses-area")._setHTML(d);
            ins("Address added successfully")._ui._notification()
        })
    })
}, true)

ins(".-update-address-btn")._on("click", (o) => {
    ins(".-update-address-area")._data._submit(function(data) {
        ins("_update_address")._ajax._app(data, (d) => {
            ins(".-addresses-area")._setHTML(d);
            ins("Address updated successfully")._ui._notification()
        })
    })
}, true)



ins(".-add-address")._on("click", (o) => {

    ins("_add_address_ui")._ajax._app({}, (data) => {
        ins(".-addresses-area")._setHTML(data);
    })
})


ins(".-back-address-btn")._on("click", (o) => {
    ins("_addresses_area_ui")._ajax._app({}, (d) => {
        ins(".-addresses-area")._setHTML(d);
    })
})

ins(".-update-address")._on("click", (o) => {

    ins("_update_address_ui")._ajax._app(o._getData(), (data) => {
        ins(".-addresses-area")._setHTML(data);
    })
})


ins(".-remove-address-btn")._on("click", (o) => {
    var p = o._parents(".-address-cont");
    if (confirm("Are you sure you want to remove this address?")) {
        ins("_remove_address")._ajax._app(o._getData(), (data) => {
            ins("Address removed!")._ui._notification()
            p._remove()

        })

    }
}, true)




function _login_m() {

    var mobile = ins(".-login-mobile-inpt")._getValue();
    if (mobile == "" || mobile == null) {
        ins("Mobile number is required")._ui._notification({ "class": "ins-danger" })
        return false;
    } else if (mobile.length < 10) {
        ins("Invalid mobile number")._ui._notification({ "class": "ins-danger" })
        return false;
    }

    ins("_login_mobile")._ajax._app({ "mobile": mobile }, (d) => {
        if (d == "-1") {
            ins("Invalid mobile number")._ui._notification({ "class": "ins-danger" })
        } else {
            ins("OTP sent successfully")._ui._notification()
            ins(".-login-area")._setHTML(d)
            resend_otp();

        }
    })
    ins(".-guser-m-menu")._toggleClass("ins-hide")
}


function resend_otp() {

    let count = 10
    const countdown = setInterval(() => {
        count--
        if (count > 1) {
            ins(".-otp-resend-counter")._setHTML(count)

        } else {
            ins(".-otp-resend-counter")._setHTML(count)
        }
        if (count == 0) {
            ins(".-resend-count-otp")._addClass("ins-hidden")
            ins(".-resend-otp-btn")._removeClass("ins-hidden")
            clearInterval(countdown)
        }
    }, 1000)

}

ins(".-resend-otp-btn")._on("click", (o) => {
    ins(".-otp-resend-counter")._setHTML("10")
    ins(".-resend-count-otp")._removeClass("ins-hidden")
    ins(".-resend-otp-btn")._addClass("ins-hidden")
    ins("OTP sent successfully")._ui._notification()
    resend_otp();


})

function _login_otp() {

    ins(".-otp-form")._data._submit(function(data) {
        ins("_login_otp")._ajax._app(data, (d) => {
            if (d == "-1") {
                ins("Invalid OTP")._ui._notification({ "class": "ins-danger" })
            } else {
                ins("Login successfully")._ui._notification()
                ins(".-otp-form")._ui._addLoader()
                setTimeout(() => {
                    window.location.reload()
                }, 3000);

            }
        })
    })

}



ins(".-guser-m-btn")._on("click", (o) => {
    _login_m()
}, true)

ins(".-login-mobile-inpt")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _login_m()
    }
})


ins(".-guser-o-btn")._on("click", (o) => {
    _login_otp()
}, true)

ins(".-login-otp-inpt")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _login_otp()
    }
})



ins(".-show-password")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active")
        ins(".-password-inpt")._setAttribute("type", "password")
    } else {
        ins(".-password-inpt")._setAttribute("type", "")
        o._addClass("ins-active")
    }
}, true);




ins(".-show-confirm-password")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active")
        ins(".-confirm-password-inpt")._setAttribute("type", "password")
    } else {
        ins(".-confirm-password-inpt")._setAttribute("type", "")
        o._addClass("ins-active")
    }
}, true);



ins(".-show-old-password")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active")
        ins(".-update-old-password-inpt")._setAttribute("type", "password")
    } else {
        ins(".-update-old-password-inpt")._setAttribute("type", "")
        o._addClass("ins-active")
    }
}, true);



ins(".-update-name-btn")._on("click", (o) => {
    var fname = ins(".-signup-first-name-inpt")._getValue()
    var lname = ins(".-signup-last-name-inpt")._getValue()
    ins("_update_user_name")._ajax._app({ "fname": fname, "lname": lname }, (d) => {
        var jdata = JSON.parse(d)
        if (jdata["status"] == "1") {
            ins(jdata["msg"])._ui._notification()
        } else {
            ins(jdata["msg"])._ui._notification({ "class": "ins-danger" })

        }

    })

}, true);


ins(".-update-password-btn")._on("click", (o) => {
    var password = ins(".-update-password-inpt")._getValue();
    var confirmPassword = ins(".-update-confirm-password-inpt")._getValue();
    var oldPassword = ins(".-update-old-password-inpt")._getValue();


    if (password !== confirmPassword) {
        ins("Passwords do not match")._ui._notification({ "class": "ins-danger" });
    } else if (oldPassword == "") {
        ins("Please enter old password")._ui._notification({ "class": "ins-danger" });

    } else {
        ins("_update_password")._ajax._app({ "password": password, "old_password": oldPassword }, (d) => {
            var jdata = JSON.parse(d)
            if (jdata["status"] == "1") {
                ins(jdata["msg"])._ui._notification()
                ins(".-update-password-inpt")._setValue("")
                ins(".-update-confirm-password-inpt")._setValue("")
                ins(".-update-old-password-inpt")._setValue("")
            } else {
                ins(jdata["msg"])._ui._notification({ "class": "ins-danger" })

            }
        });
    }
}, true);




ins(".-update-email-inpt")._on("keyup", (o) => {
    ins("_check_email")._ajax._app({ "email": o._getValue() }, (d) => {
        ins(".-verified-area")._setHTML(d)

    })
}, true);

ins(".-send-email-veri-btn")._on("click", (o) => {
    var email = ins(".-update-email-inpt")._getValue()
    if (email == "") {
        ins("enter_valid_number")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" });

        })
    } else {
        ins("_send_email_otp")._ajax._app({ "email": email }, (d) => {
            ins("An email with activation link sent to your email address " + email)._ui._notification()
        });
    }
}, true);

function actions(ds) {
    if (ds["p"] != "") {
        var imgs = "<div data-p='" + ds[0].path + "' class='-img-cont ins-flex-center'><div class='lni lni-xmark  ins-rounded ins-danger    ins-button-text -img-remove'></div>" +
            "<a target='_blank'  href='" + ds[0].fullpath + "' class='lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link'></a>  <img src='" + ds[0].fullpath + "' /></div>";
        ins(ds["p"])._find(".ins-form-upload-imgs")._setHTML(imgs)
    }
}

function reval(p) {
    var sp = "";
    var paths = "";
    ins("." + p + " .-img-remove ")._each((i) => {
        paths += sp + i._getData("p");
        sp = ",";
    })
    ins("." + p)._find("input")._setValue(paths)
}


ins(".ins-form-upload-cont .-img-remove ")._on("click", (o) => {
    var p = o._parents(".ins-form-upload-imgs-cont")._getData("id");
    o._parent()._remove()
    reval(p)
    data = {}
    data.oid = ins(".-order-id-area")._getData("oid")

    ins("_remove_image")._ajax._app(data, (d) => {
        ins("Receipt removed successfully")._ui._notification()
    })
}, true);



var ondone = function(ds) {
    actions(ds)
    data = {}
    data.oid = ins(".-order-id-area")._getData("oid")
    data.path = ds[0].path
    ins("_upload_image")._ajax._app(data, (d) => {
        ins("Receipt uploaded successfully")._ui._notification()
    })
};

var options = {
    o: ins(".-upload-image"),
    onend: ondone,
    dir: "receipts"
}
ins(".-upload-image")._on("click", (o) => {
    options._p = "." + o._getData("p");
    ins("ins_plg_py_upload")._plgin(options,
        function(plg) {}
    );

}, true)