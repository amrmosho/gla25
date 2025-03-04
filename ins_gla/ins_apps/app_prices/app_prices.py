import json
from uuid import uuid4
from ins_kit._engine._bp import App


class AppPrices(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _price(ins,options,data):
        uidata=[
        {"_data": str(data["buy"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card ins-title-center ins-col-5 ins-flex-center ins-padding-l ins-padding-h ins-text-center",},
        {"_data": str(data["sell"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card  ins-col-5 ins-title-center ins-flex-center ins-padding-l ins-padding-h ins-text-center",},

        ]
        return ins._ui._render(uidata)
    def _price_24(ins,options,data):
        uidata=[
        {"_data": str(data["buy_24"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card ins-title-center ins-col-5 ins-flex-center ins-padding-l ins-padding-h ins-text-center",},
        {"_data": str(data["sell_24"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card  ins-col-5 ins-title-center ins-flex-center ins-padding-l ins-padding-h ins-text-center",},

        ]
        return ins._ui._render(uidata)
  
 



    def out(self):

        r = self.ins._apps._crud(properties=self.app._properties)

        return r
