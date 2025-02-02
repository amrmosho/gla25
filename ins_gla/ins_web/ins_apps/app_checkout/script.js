ins(".-address-btn")._on("click", (o) => {
    ins(".-address-btn")._setAttribute("src", "/ins_web/ins_uploads/style/radio.svg")
    ins("_select_address")._ajax._app(o._getData(), (data) => {

    })
    o._setAttribute("src", "/ins_web/ins_uploads/style/radio_checked.svg")
}, true)

ins(".-payment-btn")._on("click", (o) => {

    window.location = ins()._data._addtourl(o._getData("url"), "/payment/")

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





ins(".-proccesd-payment-btn,.-payment-step-btn")._on("click", (o) => {
    ins("_check_address")._ajax._app({}, (d) => {
        if (d == "-1") {
            ins("You have to select address or store")._ui._notification({ class: "ins-danger" })
        } else {
            window.location = "/checkout/payment/"
        }
    })
}, true)


function update_data(p, k) {
    var value = p._getValue();
    ins("_update_item_data")._ajax._app({ "value": value, "k": k }, (data) => {})
}

ins(".-minus-btn")._on("click", (o) => {
    var p = o._parent(".-counter-cont")._find(".count-inpt")
    if (p._getValue() > 1) {
        p._setValue(p._getValue() - 1);
        update_data(p, o._getData("pid"))
    }
}, true)



ins(".-plus-btn")._on("click", (o) => {
    var p = o._parent(".-counter-cont")._find(".count-inpt")
    let val = parseInt(p._getValue(), 10);
    p._setValue(val + 1);
    update_data(p, o._getData("pid"))
}, true)

ins(".-back-address-btn")._on("click", (o) => {
    ins("_addresses_area_ui")._ajax._app({}, (d) => {
        ins(".-addresses-area")._setHTML(d);
    })
})


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

ins(".-remove-item-cart-btn")._on("click", (o) => {
    var ops = o._getData()
    var p = o._parent(".-item-card");
    if (confirm("Are you sure tou want to remove this item from cart?")) {
        ins("_remove_item_cart")._ajax._app(ops, (data) => {
            var jdata = JSON.parse(data)
            if (jdata["status"] == "1") {
                window.location.reload()
            }
            p._remove()
            ins("Item removed!")._ui._notification()
        })
    }

}, true)



function update_address_btn(o) {
    var f = o._find(".-address-radio-btn");
    ins(".-delivery-type-btn")._addClass("inactive")
    ins(".-delivery-type-btn")._removeClass("ins-gold-bg")
    o._removeClass("inactive")
    o._addClass("ins-gold-bg")
    ins(".-address-radio-btn")._setAttribute("src", "/ins_web/ins_uploads/style/radio.svg")
    f._setAttribute("src", "/ins_web/ins_uploads/style/radio_checked.svg")
}


ins(".-delivery-type-btn")._on("click", (o) => {
    update_address_btn(o);
    ins("_select_address_ui")._ajax._app(o._getData(), (d) => {
        ins(".-addresses-area")._setHTML(d);
    })
}, true)

ins(".-payment-type-btn")._on("click", (o) => {
    var f = o._find(".-payment-type-btn-img");
    ins(".-payment-type-btn")._removeClass("ins-active")
    o._addClass("ins-active")
    ins(".-payment-type-btn-img")._setAttribute("src", "/ins_web/ins_uploads/style/radio.svg")
    f._setAttribute("src", "/ins_web/ins_uploads/style/radio_checked_b.svg")
    ins("_update_payment_data")._ajax._app(o._getData(), (d) => {

    })
}, true)



ins(".-submit-order-btn")._on("click", (o) => {
    ins("_submit_order")._ajax._app({}, (d) => {
        if (d == "-1") {
            ins("You have to select payment method")._ui._notification()
        } else {
            window.location = "/checkout/order/"
        }
    })
}, true)


ins(function() {
    g = ins()._map._get();
    if (g["mode"] == "order") {
        let count = 10
        const countdown = setInterval(() => {
            count--
            if (count > 1) {
                ins(".-otp-resend-counter")._setHTML(count + " seconds")

            } else {
                ins(".-otp-resend-counter")._setHTML(count + " second")
            }
            if (count == 0) {
                clearInterval(countdown)
                window.location = "/puser/order/"
            }
        }, 1000)
    }
})._load()