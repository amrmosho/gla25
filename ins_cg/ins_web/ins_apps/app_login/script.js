ins(".-signup-step-1-btn")._on("click", (o) => {
    ins(".-signup-form")._data._submit(function(data) {
        ins()._ui._addLoader()
        ins("_signup_ui_step2")._ajax._app(data, (d) => {
            if (d == "-1") {
                ins("email_address_already_exists")._data._trans((text) => {
                    ins(text)._ui._notification({ "class": "ins-danger" })
                })
            } else {
                ins(".-signup-area")._setHTML(d);
                resend_otp();
            }
            ins()._ui._removeLoader()

        });


    });
}, true);

ins(".-signup-step-2-btn")._on("click", (o) => {
    var otp = ins(".-login-otp-inpt")._getValue();

    if (otp.trim() === "") {
        ins("otp_cannot_be_empty")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" })
        })
    } else {
        ins(".-signup-form")._data._submit(function(data) {
            ins("_signup_ui_step3")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("invalid_otp")._data._trans((text) => {
                        ins(text)._ui._notification({ "class": "ins-danger" })
                    })
                } else if (d == "-2") {
                    ins("otp_code_has_been_expired")._data._trans((text) => {
                        ins(text)._ui._notification({ "class": "ins-danger" })
                    })

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
    if (password.length < 8) {
        ins("password_long")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" })
        })
    } else {
        if (password !== confirmPassword) {
            ins("passwords_do_not_match")._data._trans((text) => {
                ins(text)._ui._notification({ "class": "ins-danger" })
            })
        } else {
            ins(".-signup-form")._data._submit(function(data) {
                ins("_signup")._ajax._app(data, (d) => {
                    if (d != "-1") {
                        ins("signup_completed_successfully")._data._trans((text) => {
                            ins(text)._ui._notification()
                        })
                        ins(".-signup-area")._setHTML(d);
                    }
                });
            });
        }
    }
}, true);

ins("input.-forgot-otp-inpt")._on("input", (el, e) => {
    let val = el._getValue();
    val = val.replace(/\D/g, '').substring(0, 4);
    el._setValue(val);
});

ins("input.-login-otp-inpt")._on("input", (el, e) => {
    let val = el._getValue();
    val = val.replace(/\D/g, '').substring(0, 4);
    el._setValue(val);
});


ins(".-forgot-step-1-btn")._on("click", (o) => {
    ins(".-forgot-form")._data._submit(function(data) {
        ins()._ui._addLoader()
        ins("_forgot_ui_step2")._ajax._app(data, (d) => {
            if (d == "-1") {
                ins("this_mobile_doesnt_have_an_account")._data._trans((text) => {
                    ins(text)._ui._notification({ "class": "ins-danger" })
                })
            } else {
                ins(".-signup-area")._setHTML(d);
                resend_otp();
            }
            ins()._ui._removeLoader()
        });

    });
}, true);


ins(".-forgot-step-2-btn")._on("click", (o) => {
    var otp = ins(".-forgot-otp-inpt")._getValue();

    if (otp.trim() === "") {
        ins("otp_cannot_be_empty")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" })
        })
    } else {
        ins(".-forgot-form")._data._submit(function(data) {
            ins("_forgot_ui_step3")._ajax._app(data, (d) => {
                if (d == "-1") {
                    ins("invalid_otp")._data._trans((text) => {
                        ins(text)._ui._notification({ "class": "ins-danger" })
                    })
                } else if (d == "-2") {
                    ins("otp_code_has_been_expired")._data._trans((text) => {
                        ins(text)._ui._notification({ "class": "ins-danger" })
                    })

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

    if (password.length < 8) {
        ins("password_long")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" })
        })
    } else {
        if (password !== confirmPassword) {
            ins("passwords_do_not_match")._data._trans((text) => {
                ins(text)._ui._notification({ "class": "ins-danger" })
            })
        } else {

            ins(".-forgot-form")._data._submit(function(data) {
                ins("_reset_password")._ajax._app(data, (d) => {
                    if (d != "-1") {
                        ins("password_rest_successfully")._data._trans((text) => {
                            ins(text)._ui._notification()
                        })
                        ins(".-signup-area")._setHTML(d);
                    }
                });
            });
        }
    }
}, true);




ins("input")._on("keyup", (o, e) => {
    o._parents(".ins-form-item")._removeClass("ins-from-input-error")
})



function _login() {
    var sdata = ins(".-email-form")._data._get_inputs();
    if (sdata.error) {
        ins("invalid_login")._data._trans((text) => {
            ins(text)._ui._notification({ "class": "ins-danger" })
            sdata.error_inputs.forEach(function(a) {
                ins(a)._parents(".ins-form-item")._addClass("ins-from-input-error");
                a.focus();
            });
        })
    } else {
        ins(".-email-form")._data._submit(function(data) {

            ins("_login")._ajax._app(data, (d) => {
                if (d != "-1") {
                    ins("login_successful")._data._trans((text) => {
                        ins(text)._ui._notification()
                    })
                    window.location.href = d;
                } else {
                    ins("invalid_mobile_number_or_password")._data._trans((text) => {
                        ins(text)._ui._notification({ "class": "ins-danger" })
                    })
                }
            });
        });
    }
}


ins(".-login-btn")._on("click", (o) => {
    _login()
}, true);

ins(".-login-email-inpt")._on("keyup", (o, e) => {
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
        var email = ins(".-forgot-email-inpt")._getValue()

    } else {
        var email = ins(".-login-email-inpt")._getValue()

    }
    ins("_resend_otp")._ajax._app({ "email": email }, (data) => {})
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