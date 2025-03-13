ins(".-signup-step-1-btn")._on("click", (o) => {
    if (ins(".-signup-mobile-inpt")._getValue() == "") {
        ins("Please enter mobile number")._ui._notification({ "class": "ins-danger" });

    } else {
        ins()._ui._addLoader()

        ins(".-signup-form")._data._submit(function(data) {

            ins("_signup_ui_step2")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("Mobile number already exists")._ui._notification({ "class": "ins-danger" });
                } else {
                    ins(".-signup-area")._setHTML(d);
                    resend_otp();
                }
                ins()._ui._removeLoader()

            });


        });
    }
}, true);

ins(".-signup-step-2-btn")._on("click", (o) => {
    var otp = ins(".-login-otp-inpt")._getValue();

    if (otp.trim() === "") {
        ins("OTP cannot be empty")._ui._notification({ "class": "ins-danger" });
    } else {
        ins(".-signup-form")._data._submit(function(data) {
            ins("_signup_ui_step3")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("Invalid OTP")._ui._notification({ "class": "ins-danger" });
                } else if (d == "-2") {
                    ins("OTP code has been expired")._ui._notification({ "class": "ins-danger" });

                } else {
                    ins(".-signup-area")._setHTML(d);
                }
            });
        });
    }
}, true);



ins(".-signup-step-3-btn")._on("click", (o) => {
    var password = ins(".-signup-password-inpt")._getValue();
    var confirmPassword = ins(".-signup-confirm-password-inpt")._getValue();
    if (password !== confirmPassword) {
        ins("Passwords do not match")._ui._notification({ "class": "ins-danger" });
    } else {
        ins(".-signup-form")._data._submit(function(data) {
            ins("_signup")._ajax._app(data, (d) => {
                if (d != "-1") {
                    ins("Signup completed successfully")._ui._notification();
                    ins(".-signup-area")._setHTML(d);
                }
            });
        });
    }
}, true);


ins(".-forgot-step-1-btn")._on("click", (o) => {
    ins()._ui._addLoader()
    if (ins(".-forgot-mobile-inpt")._getValue() == "") {
        ins("Please enter mobile number")._ui._notification({ "class": "ins-danger" });
    } else {
        ins(".-forgot-form")._data._submit(function(data) {
            ins("_forgot_ui_step2")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("This mobile doesn't have an account")._ui._notification({ "class": "ins-danger" });
                } else {
                    ins(".-signup-area")._setHTML(d);
                    resend_otp();
                }
                ins()._ui._removeLoader()
            });

        });
    }
}, true);


ins(".-forgot-step-2-btn")._on("click", (o) => {
    var otp = ins(".-forgot-otp-inpt")._getValue();

    if (otp.trim() === "") {
        ins("OTP cannot be empty")._ui._notification({ "class": "ins-danger" });
    } else {
        ins(".-forgot-form")._data._submit(function(data) {
            ins("_forgot_ui_step3")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("Invalid OTP")._ui._notification({ "class": "ins-danger" });
                } else if (d == "-2") {
                    ins("OTP code has been expired")._ui._notification({ "class": "ins-danger" });

                } else {
                    ins(".-signup-area")._setHTML(d);
                }
            });
        });
    }
}, true);
ins(".-forgot-step-3-btn")._on("click", (o) => {
    var password = ins(".-signup-password-inpt")._getValue();
    var confirmPassword = ins(".-signup-confirm-password-inpt")._getValue();
    if (password !== confirmPassword) {
        ins("Passwords do not match")._ui._notification({ "class": "ins-danger" });
    } else {

        ins(".-forgot-form")._data._submit(function(data) {
            ins("_reset_password")._ajax._app(data, (d) => {
                if (d != "-1") {
                    ins("Password rest successfully")._ui._notification();
                    ins(".-signup-area")._setHTML(d);
                }
            });
        });
    }
}, true);






function _login() {
    ins(".-email-form")._data._submit(function(data) {
        ins("_login")._ajax._app(data, (d) => {
            if (d != "-1") {
                ins("Login successful")._ui._notification();
                window.location.href = d;
            } else {
                ins("Invalid mobile number or password")._ui._notification({ "class": "ins-danger" });
            }
        });
    });

}


ins(".-login-btn")._on("click", (o) => {
    _login()
}, true);

ins(".-login-email-mobile-inpt")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _login()
    }
});

ins(".-login-otp-btn")._on("click", (o) => {
    _login_otp();
}, true);

ins(".-login-otp-inpt")._on("keyup", (o, e) => {
    if (e.keyCode == 13) {
        _login_otp();
    }
});

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
    if (o._hasClass("-forgot-otp")) {
        var mobile = ins(".-forgot-mobile-inpt")._getValue()

    } else {
        var mobile = ins(".-login-mobile-inpt")._getValue()

    }
    ins("_resend_otp")._ajax._app({ "mobile": mobile }, (data) => {})
    resend_otp();
})

ins(".-show-password")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active")
        ins(".-signup-password-inpt")._setAttribute("type", "password")
    } else {
        ins(".-signup-password-inpt")._setAttribute("type", "")
        o._addClass("ins-active")
    }
}, true);




ins(".-show-confirm-password")._on("click", (o) => {
    if (o._hasClass("ins-active")) {
        o._removeClass("ins-active")
        ins(".-signup-confirm-password-inpt")._setAttribute("type", "password")
    } else {
        ins(".-signup-confirm-password-inpt")._setAttribute("type", "")
        o._addClass("ins-active")
    }
}, true);


ins(".-signup-back-1-btn")._on("click", (o) => {
    ins("_signup_ui_step1")._ajax._app({}, (d) => {
        ins(".-signup-area")._setHTML(d);
    })
}, true);