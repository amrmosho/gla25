from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"

class AppCart(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    @property
    def session_name(sel):
        return "glaproducts"
    
    def _cart_step_summary(self):
        sedata=self.ins._server._get_session(self.session_name)
        subtotal = 0
        for k,v in sedata.items():
         subtotal+= float(v["price"]) * float(v["count"])
        total = subtotal 
        uidata = []
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details","_data-ar":"تفاصيلك","_trans":"true", "class": "ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal","_data-ar":"المجموع الفرعي","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end  -subtotal-text"})
        uidata.append({"_data": "Shipping","_data-ar":"شحن","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","_data-ar": "مجاني","_trans":"true","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total","_data-ar":"المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":str(total), "_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه","class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end  -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        lbtitle = "Change in price"
        if self.ins._langs._this_get()["name"] == "ar":
            lbtitle = "تغير في السعر"
        uidata.append({"data-lbtitle":lbtitle,"_type":"a","data-url":"/checkout/delivery","_data": "Procced to address <img src='"+p+"style/right_arrow.svg'></img>","_data-ar":"انتقل إلى العنوان","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper -cart-next-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        
        return uidata
    
  
    def ui(self):
      ## Cart Area
        sedata=self.ins._server._get_session(self.session_name)
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        for k,v in sedata.items():
            uidata+= ELUI(self.ins).counter_pro_block(v)
        uidata.append({"end":"true"})
       
       
       
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex -cart-summary-area  ins-padding-2xl","style":"background:white;height:100%;   border-left: 1px solid var(--primary-l);"})
        uidata+= self._cart_step_summary()
        uidata.append({"end":"true"})   


        
        return uidata


    def out(self):
        return self.ui()
