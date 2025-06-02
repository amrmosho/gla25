from ins_cg.ins_kit._elui import ELUI
from ins_cg.ins_kit._pros import Pros
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"


class AppCheckoutCart(App):
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

        cgurl = self.ins._server._url({"mode": "payment"})

        if type(sdata) == dict:
            uidata = [
                {"start": "true", "class": " gla-container  ins-flex-start",
                    "style": "position: relative;top: 20px;"},
                {"start": "true", "class": "ins-col-12 ins-flex-center  w-content ins-padding-2xl "},
                {"class": "w-line ins-col-12"},
                {"_data": "Cart <span class='w-citem ins-primary '>1</span>",
                    "class": "ins-col-2 ins-title-s  ins-primary-color w-item ins-strong-m"},
                {"_data": "Payment <span class='w-citem ins-info ' >2</span>",
                    "class": "ins-col-2 ins-title-s w-item ins-strong-m"},
                {"end": "true"},
                {"start": "true",
                    "class": "ins-col-9 ins-flex-center ins-card"},
            ]
            t = 0

            for k, v in sdata.items():
                t += v["price"]
                uidata += ELUI(self.ins).cart_pro_block(v)
                uidata.append({"class": "ins-space-xs"})
            uidata += [
                {"end": "true"},
                {"start": "true",
                 "class": "ins-flex ins-card ins-padding-l ins-col-3"},
                {"class": "ins-space-xs"},
                {"_data":  str(t), "_view": "currency", "_currency_symbol": "$",
                 "class": "ins-col-12   ins-title-l  ins-primary-d-color"},
                {"_data":  "Total",
                 "class": "ins-col-12   ins-title-l  ins-primary-d-color"},
                {"class": "ins-space-s"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-flex ins-col-12 ins-gap-o"},
                {"href": cgurl, "_type": "a", "_data": "<img src='"+p+"style/cart.svg'></img> Continue to Checkout ",  "_trans": "true",
                 "class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-primary -add-cart-btn", "style": "    height: 46px;    border: 1px solid var(--primary-d);"},
                {"end": "true"}
            ]

            return self.ins._ui._render(uidata)
        else:
            return self.no_data()

    def out(self):
        self.app._include("style.css")
        return self.ui()
