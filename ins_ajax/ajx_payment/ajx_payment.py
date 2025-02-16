import json
from ins_kit._engine._bp import App
from flask import session, request

class AjxPayment(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def update_payment_status(self, order_id, status):
        self.ins._db._update("gla_order", {"payment_status": status}, f"id='{order_id}'")
        return "1"

    def payment_callback(self):
        data = request.data
        odata = json.loads(data)
        order_id = str(odata["obj"]["order"]["merchant_order_id"])

        payment_status = "success" if str(odata["obj"]["success"]) == "True" else "failed"
        self.update_payment_status(order_id, payment_status)
        return "1"

