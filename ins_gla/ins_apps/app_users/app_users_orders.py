from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI
class AppUsersOrders(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)

    def u(self, mode):
        return self.ins._server._url({"mode": mode},)
    def order(self):
        g= self.ins._server._get()
        sedata = self.ins._db._jget("gla_order_item", "*", f"fk_order_id='{g["id"]}'")
        sedata._jwith("gla_product product", "th_main", rfk="fk_product_id" ,join="left join")
        sedata=sedata._jrun()

        uidata = []
        subtotal = 0
        tcount = 0
        uidata = [{"start": "true", "class": "ins-col-12 ins-flex "},
                  {"_data": f"Order ID({g["id"]} /2025)", "class": "ins-col-12 ins-strong-m ins-title-m"}]
        for v in sedata:
            tcount += v["quantity"]
            subtotal += float(v["price"])
            uidata += ELUI(self.ins).counter_user_order_block(v)
        footer = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card"},
            {"class": "ins-radius-m", "style": "    width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex  "},
            {"_data": f' Count  ',
                "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": f'   ',
                "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": f' Total  ',
             "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": str(tcount),
             "class": " ins-col-4  ins-grey-d-color   ins-text-center ins-title-xs ins-strong-l"},
            {"_data": "",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            {"_data": str(subtotal),"_view":"currency","_currency_symbol":" EGP",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
        ]
        uidata += footer
        return self.ins._ui._render(uidata)
    def out(self, ins):
        udata = self.user._check()
        odata = self.ins._db._get_data("gla_order", "*", f"fk_user_id='{udata["id"]}'")
        usmenu = [{"start": "true", "class": "  ins-col-12 ins-gap-20  ins-flex    ins-padding-2xl"}]
        i = 0
        odata.reverse()
        for v in odata:
            if (v["order_status"] == "pending"):
                status_class = "ins-warning"
            elif (v["order_status"] == "confirmed"):
                status_class = "ins-secondary"
            elif (v["order_status"] == "canceled"):
                status_class = "ins-danger"
            elif (v["order_status"] == "delivered"):
                status_class = "ins-success"
            i += 1
            style = ""
            if i == 1:
                style = "border: 2px solid var(--gold) !important;"
            order = [{"start": "true", "class": " ins-flex-space-between  ins-card  ins-col-12 ins-border   ins-flex   ins-padding-l","style":style},
            {"_data": f'  Order  ID({v["id"]} /2025) ',"class": " ins-col-9 ins-primary-d-color ins-title-s	 ins-strong-l "}
            ]
            if i == 1:
                order+=[{"_data": f'  New ',"class": "ins-tag ins-gold  ins-strong-m  ins-text-upper ins-radius-m  ins-text-upper ins-text-center"}]

            order+=[{"_data": f'{v["order_status"]}',
                "class": f"{status_class} ins-col-2 ins-radius-m  ins-text-upper ins-avatar-s ins-gold-d "},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-flex ins-col-10"},
            {"_data": f' Date  ',
                "class": " ins-col-4    ins-grey-color "},
            {"_data": f' Items Count ',
             "class": " ins-col-4    ins-grey-color"},
            {"_data": f' Orders Total ',
             "class": " ins-col-4 ins-grey-color "},
            {"_data": f'{v["kit_created"]}',"_view":"date",
             "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l ", "style": "    margin-top: -22px;"},
            {"_data": f' 15 ',
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"_data": f'{v["total"]}', "_view": "currency", "_currency_symbol": " EGP",
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"end": "true"},
            {"class": " ins-col-1"},
            {"_type":"a" ,"href":f"/puser/order/{v["id"]}","class": "ins-button-cricle ins-grey-d",
                "_data": '<i class=" lni ins-icon ins-white-color lni-arrow-right"></i>'},
            {"end": "true"}]
            
            usmenu+=order
            
        usmenu.append({"end": "true"})
        
        uidata = [
            {"start": "true", "class": "ins-col-12  "},
            {"start": "true", "class": "gla-container ins-flex-start "},
        ]
        
        g= ins._server._get()
        
        
        
        if "id" in g:
                
            uidata .append({"start": "true", "class": "  ins-flex-start  ins-padding-2xl  ins-col-12"})
            uidata .append({"class": "  ins-flex-start  ins-gap-20   ins-col-12" ,"_data":self.order()})
            uidata .append({"end": "true"})
       
        else:
            
            uidata .append({"start": "true", "class": "ins-flex ins-col-12 "})
            uidata += usmenu
            uidata .append({"end": "true"})
    
      
        uidata .append({"end": "true"})
        return self.ins._ui._render(uidata)
