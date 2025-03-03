ins(".-address-btn")._on("click", (o) => {
    ins(".-address-btn")._setAttribute("src", "/ins_web/ins_uploads/style/radio.svg")
    ins("_select_address")._ajax._app(o._getData(), (data) => {})
    o._setAttribute("src", "/ins_web/ins_uploads/style/radio_checked.svg")
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



ins(".-update-cart-price-btn")._on("click", (o) => {
    var ops = o._getData();

    ins("update_cart_price")._ajax._app(ops, (data) => {
        window.location.reload()
    })

}, true)


ins(".-empty-cart-btn")._on("click", (o) => {
    var ops = o._getData();

    if (confirm("Are you sure you want to empty cart?")) {
        ins("empty_cart")._ajax._app(ops, (data) => {
            window.location.reload()
        })
    }

}, true)

function price_check(o) {
    var ops = o._getData();

    ins("price_check")._ajax._app(ops, (data) => {
        if (data == "1") {
            window.location = ops["url"]

        } else {
            ins()._ui._addLightbox({
                "mode": "",
                title: "<span class='ins-title-20  '>" + ops["lbtitle"] + "</span> ",
                data: data,
                data_style: "position: relative;top: 0;",
                style: "width:600px;    "
            });
        }

    })
}
ins(".-payment-btn")._on("click", (o) => {
    ins("_check_address")._ajax._app(o._getData(), (data) => {
        if (data == "-1") {
            ins("Please select address")._ui._notification({ "class": "ins-danger" })
        } else {
            price_check(o);
        }
    })
})
ins(".-cart-next-btn")._on("click", (o) => {
    price_check(o);
}, true)


function update_data(p, k) {
    var value = p._getValue();
    ins("_update_item_data")._ajax._app({ "value": value, "k": k }, (data) => {
        ins(".-cart-summary-area")._setHTML(data)
    })
}

ins(".-minus-btn")._on("click", (o) => {
    var p = o._parent(".-counter-cont")._find(".count-inpt")
    if (p._getValue() > 1) {
        p._setValue(p._getValue() - 1);
        update_data(p, o._getData("pid"))
    }
}, true)

ins(".count-inpt")._on("change", (o) => {
    if (o._getValue() >= 1) {
        update_data(o, o._getData("pid"))
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
                ins("._app_checkout")._setHTML(jdata["ui"])
            }
            p._remove()
            ins(".-cart-summary-area")._setHTML(jdata["ui"])

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
    var button = o._find(".-payment-type-btn-img");

    ins(".-payment-type-btn")._removeClass("ins-active");
    ins(".-payment-subtype-area")._removeClass("ins-active");

    o._addClass("ins-active");
    ins(".-payment-subtype-area-" + o._getData("name"))._addClass("ins-active");

    ins(".-extra-fees-card")._addClass("ins-hidden");

    if ("charges" in o._getData() && o._getData("charges") !== "") {
        ins(".-extra-fees-card")._removeClass("ins-hidden");
    }

    ins(".-payment-type-btn-img")._setAttribute("src", "/ins_web/ins_uploads/style/radio.svg");
    button._setAttribute("src", "/ins_web/ins_uploads/style/radio_checked_b.svg");

    ins("_update_payment_data")._ajax._app(o._getData(), (d) => {
        if (d !== "1") {
            ins(".-items-area")._setHTML(d);
        }
    });
}, true);

ins(".-african-bank-button")._on("click", function() {
    let targetCard = ins(".-bank-card-african")._get(0);
    if (targetCard) {
        setTimeout(() => {
            ins(".-bank-card-african")._addClass("ins-active");

        }, 300);
        setTimeout(() => {
            ins(".-bank-card-african")._removeClass("ins-active");

        }, 600);
        targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
    }
});


ins(".-copy-number")._on("click", (o) => {
    var number = o._getData("number");
    navigator.clipboard.writeText(number).then(() => {
        ins("Number copied to clipboard!")._ui._notification();
    }).catch(err => {
        ins("Failed to copy number")._ui._notification({ "class": "ins-danger" });
    });
}, true);
ins(".-submit-order-btn")._on("click", (o) => {
    var ops = o._getData()
    ins("price_check")._ajax._app({}, (data) => {
        if (data == "1") {
            ins()._ui._addLoader()
            ins("Redirecting to payment...")._ui._notification()
            ins("_submit_order")._ajax._app({}, (d) => {
                jdata = JSON.parse(d)
                if (jdata["status"] == "-1") {
                    ins("You have to select payment method")._ui._notification()
                    ins()._ui._removeLoader()
                } else if (jdata["status"] == "1") {
                    window.location = "/checkout/order/?merchant_order_id=" + jdata["oid"]
                    ins()._ui._removeLoader()
                } else {
                    setTimeout(() => {
                        window.location = jdata["url"]
                        ins()._ui._removeLoader()
                    }, 3000);
                }

            })

        } else {
            ins()._ui._addLightbox({
                "mode": "",
                title: "<span class='ins-title-20  '>" + ops["lbtitle"] + "</span> ",
                data: data,
                data_style: "position: relative;top: 0;",
                style: "width:600px;    "
            });
        }

    })


}, true)
ins(".-continue-shopping-btn")._on("click", (o) => {
    ins(".ins-panel-overlay.ins-opened")._remove()
    ins()._ui._removeLightbox();
}, true)
ins(function() {
    g = ins()._map._get();
    if (g["mode"] == "order") {
        ins("_check_order_status")._ajax._app({ url: ins(".-url-area")._getData("url") }, (d) => {
            console.log(d)
            if (d != "1") {
                let count = 10
                const countdown = setInterval(() => {
                    count--
                    if (count > 1) {
                        ins(".-countdown")._setHTML(count)
                    } else {
                        ins(".-countdown")._setHTML(count)
                    }
                    if (count == 0) {
                        clearInterval(countdown)
                        window.location = d
                    }
                }, 1000)
            }
        })
    }
})._load()