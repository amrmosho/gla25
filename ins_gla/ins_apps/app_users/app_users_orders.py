from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI
class AppUsersOrders(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def u(self, mode):
        return self.ins._server._url({"mode": mode},)
    @property
    def session_name(sel):
        return "glaproducts"
    def order(self):
        sedata = self.ins._server._get_session(self.session_name)
        uidata = []
        subtotal = 0
        uidata = [{"start": "true", "class": "ins-col-12 ins-flex "},
                  {"_data": "Order ID(8 /2025)", "class": "ins-col-12 ins-strong-m ins-title-m"}]
        for k, v in sedata.items():
            subtotal += v["price"]
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
            {"_data": "2",
             "class": " ins-col-4  ins-grey-d-color   ins-text-center ins-title-xs ins-strong-l"},
            {"_data": "",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            {"_data": "3333",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
        ]
        uidata += footer
        return self.ins._ui._render(uidata)
    def out(self, ins):
        usmenu = [
            {"start": "true", "class": "  ins-col-12 ins-gap-20  ins-flex    ins-padding-2xl"},
         
         
         
            # order item block 1
            {"start": "true", "class": " ins-flex-space-between  ins-card  ins-col-12 ins-border   ins-flex   ins-padding-l"},
            {"_data": f'  Order  ID(8 /2025) ',
                "class": " ins-col-10  ins-primary-d-color ins-title-s	 ins-strong-l "},
            {"_data": f'  Done',
                "class": " ins-col-2 ins-radius-m  ins-text-upper ins-avatar-s ins-success "},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-flex ins-col-10"},
            {"_data": f' Date  ',
                "class": " ins-col-4    ins-grey-color "},
            {"_data": f' Items Count ',
             "class": " ins-col-4    ins-grey-color"},
            {"_data": f' Orders Total ',
             "class": " ins-col-4 ins-grey-color "},
            {"_data": f' 01/30/2025 ',
             "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l ", "style": "    margin-top: -22px;"},
            {"_data": f' 15 ',
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"_data": f'EGP 3000 ',
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"end": "true"},
            {"class": " ins-col-1"},
            {"class": "ins-button-cricle ins-grey-d",
                "_data": '<i class=" lni ins-icon ins-white-color lni-arrow-right"></i>'},
            {"end": "true"},
            
            
               # order item block 1
            {"start": "true", "class": " ins-flex-space-between  ins-card  ins-col-12 ins-border   ins-flex   ins-padding-l"},
            {"_data": f'  Order  ID(8 /2025) ',
                "class": " ins-col-10  ins-primary-d-color ins-title-s	 ins-strong-l "},
            {"_data": f'  Done',
                "class": " ins-col-2 ins-radius-m  ins-text-upper ins-avatar-s ins-success "},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-flex ins-col-10"},
            {"_data": f' Date  ',
                "class": " ins-col-4    ins-grey-color "},
            {"_data": f' Items Count ',
             "class": " ins-col-4    ins-grey-color"},
            {"_data": f' Orders Total ',
             "class": " ins-col-4 ins-grey-color "},
            {"_data": f' 01/30/2025 ',
             "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l ", "style": "    margin-top: -22px;"},
            {"_data": f' 15 ',
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"_data": f'EGP 3000 ',
                "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
            {"end": "true"},
            {"class": " ins-col-1"},
            {"_type":"a" ,"href":"/puser/order/1","class": "ins-button-cricle ins-grey-d",
                "_data": '<i class=" lni ins-icon ins-white-color lni-arrow-right"></i>'},
            {"end": "true"},
            {"end": "true"},
            
            
            {"end": "true"}
        ]
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
