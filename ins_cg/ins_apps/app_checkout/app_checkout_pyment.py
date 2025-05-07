from ins_cg.ins_kit._elui import ELUI
from ins_cg.ins_kit._pros import Pros
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"


class AppCheckoutPyment(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def no_data(self):
        uidata = [
            {"start": "true", "class": "ins-col-12  ins-flex-center",
                "style": "position: relative;top: 20px;"},
            {"_data": "There is no items in cart yet", "_data-ar": "لا يوجد أي عناصر في سلة التسوق بعد",
                "_trans": "true", "class": "ins-col-8 ins-card ins-padding-2xl ins-text-center"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)

    def ui(self):
        sdata = self.ins._server._get_session(Pros(self.ins).session_name)
        cgurl = self.ins._server._url({"mode": "pay"})

        t = 0
        for k, v in sdata.items():
            t += v["price"]

        if type(sdata) == dict:
            uidata = [
                {"start": "true", "class": " gla-container  ins-flex-start",
                    "style": "position: relative;top: 20px;"},
                {"start": "true", "class": "ins-col-12 ins-flex-center  w-content ins-padding-2xl "},
                {"class": "w-line ins-col-12"},
                {"_data": "Cart <span class='w-citem ins-info '>1</span>",
                    "class": "ins-col-2 ins-title-s   w-item ins-strong-m"},
                {"_data": "Payment <span class='w-citem  ins-primary  ' >2</span>",
                    "class": "ins-col-2 ins-title-s  ins-primary-color w-item ins-strong-m"},
                {"end": "true"},
                {"start": "true",
                 "class": "ins-flex  ins-padding-l ins-col-8"},


                {"start": "true",
                 "class": "ins-flex ins-card ins-padding-l ins-col-12"},
                {"_data": "Order summary",
                    "class": "ins-col-12 ins-title-s  ins-strong-m"},

                {"class": "ins-line ins-col-12"},

                {"start": "true",
                 "class": "ins-flex  ins-col-12"},


                {"_data": " Subtotal: ",
                    "class": "ins-col-grow   ins-strong-m"},
                {"_data":  str(t), "_view": "currency",
                 "_currency_symbol": "$", "class": "ins-col-1"},

                {"end": "true"},

                {"end": "true"},
                {"start": "true",
                 "class": "ins-flex ins-card ins-padding-l ins-col-12"},


                {"_data": " Discount code ",
                    "class": "ins-col-grow   ins-strong-m"},

                {"title": "  Enter discount code ", "_type": "input", "pclass": "ins-col-12"
                 },
                {"_data": "  Apple  ", "class": "ins-col-12 ins-button ins-primary"
                 },
                {"end": "true"},
                {"end": "true"},
                {"start": "true",
                 "class": "ins-flex ins-card ins-padding-l ins-col-4"},
                {"class": "ins-space-xs"},

                {"class": "ins-icons-credit-card-multiple"
                 },

                {"_data": "Card",  "class": "ins-col-grow"
                 },

                {"class": "ins-line ins-col-12"},

                {"class": "ins-icons-paypal"
                 },
                {"_data": "Paypal",  "class": "ins-col-grow"
                 },

                {"class": "ins-line ins-col-12"},
                {"class": "ins-icons-google-pay"
                 },

                {"_data": "Google Pay",  "class": "ins-col-grow"
                 },

                {"class": "ins-space-s"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-flex ins-col-12 ins-gap-o"},
                {"href": cgurl, "_type": "a", "_data": f"<img src='{p}style/cart.svg'></img> Pay {str(t)} ",  "_trans": "true",
                 "class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn", "style": "    height: 46px;    border: 1px solid var(--primary-d);"},
                {"end": "true"},
                {"end": "true"},



            ]

            return self.ins._ui._render(uidata)
        else:
            return self.no_data()

    def out(self):
        self.app._include("style.css")
        return self.ui()
