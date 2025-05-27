from ins_cg.ins_apps.app_checkout.app_checkout_cart import AppCheckoutCart
from ins_cg.ins_apps.app_checkout.app_checkout_pyment import AppCheckoutPyment
from ins_cg.ins_kit._pros import Pros
from ins_kit._engine._bp import App
from ins_plgs.plg_login.plg_login import PlgLogin
p = "/ins_web/ins_uploads/"


class AppCheckout(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def pay(self):

        sdata = self.ins._server._get_session(Pros(self.ins).session_name)
        t = 0
        for k, v in sdata.items():
            t += v["price"]

        add = {

            "fk_user_id": "1",
            "total": str("t"),
            "payment_method": "card",
            "order_status": "paied",
            "items": self.ins._json._encode(sdata)
        }

        self.ins._db._insert("gla_order", add)
        self.ins._server._del_session(Pros(self.ins).session_name)

        uidata = [
            {"start": "true", "class": " gla-container  ins-flex-center",
             "style": "position: relative;top: 20px;"},
            {
                "start": "true", "class": "ins-col-12 ins-card ins-flex ins-padding-2xl ins-success"},
            {"class": "ins-icons-check-circle "},
            {"_data": "Payment done successfully",
                "_trans": "true", "class": "ins-col-grow"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)

    def no_items_ui(self):

        uidata = [
            {"start": "true", "class": " gla-container  ins-flex-center",
                "style": "position: relative;top: 20px;"},
            {"_data": "There is no items in cart",
                "class": "ins-col-8 ins-flex-center ins-padding-m ins-card"},
            {"end": "true"}
        ]

        return self.ins._ui._render(uidata)

    def out(self):

        l = PlgLogin(self)

        self.app._include("style.css")
        data = self.ins._server._get()

        sdata = self.ins._server._get_session(Pros(self.ins).session_name)
        if not sdata:
            return self.no_items_ui()

        if data["mode"] == "payment":
            if l.is_login():
                self.app._include("style.css")
                return AppCheckoutPyment(self).out()
            else:
                return l._login_ui()
        elif data["mode"] == "pay":
            return self.pay()
        else:
            return AppCheckoutCart(self).out()
