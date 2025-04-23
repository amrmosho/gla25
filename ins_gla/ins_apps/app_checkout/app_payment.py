from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"

class AppPayment(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    @property
    def session_payment_name(sel):
        return "glapayment"
    
    @property
    def session_name(sel):
        return "glaproducts"
    
    @property
    def session_address_name(sel):
        return "glaaddress"


    def items_area(self,string= False):
        ## Items Area
        uidata = []
        sedata=self.ins._server._get_session(self.session_name)
        shipping = self.ins._db._get_row("gla_settings","shipping_fees","id=1")["shipping_fees"]

        rq = self.ins._server._req()
        subtotal = 0
        chargs = 0
        for k,v in sedata.items():
            subtotal+= float(v["price"]) * float(v["count"])
            uidata+= ELUI(self.ins).small_pro_block(v)
            uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-line ins-col-12 not-for-phone"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"_data": "Voucher", "_data-ar":" قسيمة","_trans":"true","class": "ins-col-12  ins-grey-d-color ins-strong-m  not-for-phone "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","placeholder-ar":" رمز","_trans":"true","name":"voucher","pclass":"ins-col-12  not-for-phone","style":"    background: white;border-radius:4px;"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 -fees-info ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details","_data-ar":"تفاصيلك","_trans":"true", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "_data-ar":"المجموع الفرعي","_trans":"true","class": "ins-col-6 ins-m-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-m-col-6 ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -subtotal-text"})
        pclass = "ins-hidden"

        total = subtotal  
        uidata.append({"start": "true", "class": f"-online-payment-fee  ins-col-12 ins-flex {pclass}"})
        uidata.append({"_data": "Online payment fee","_data-ar": "رسوم الدفع عبر الإنترنت", "_trans":"true","class": "ins-col-6  ins-m-col-6 ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(chargs),"data-value" : chargs,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-m-col-6 ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -chargs-text"})
        uidata.append({"end": "true"})
        asession = self.ins._server._get_session(self.session_address_name)

        if asession["type"] == "delivery":
            uidata.append({"_data": "Shipping", "_data-ar":" شحن","_trans":"true", "class": "ins-col-6  ins-m-col-6 ins-title-xs  ins-grey-color ins-strong-m"})
            if total > 200000:
              uidata.append({"_data": "Free","_data-ar": "مجاني","_trans":"true","data-value" : 0, "class": "ins-col-6  ins-m-col-6 ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
            else:
              uidata.append({"_data": str(shipping),"data-value" : int(shipping),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-m-col-6 ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end -shipping-text"})
              total +=int(shipping)
           
           
       
       
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "_data-ar":" المجموع","_trans":"true", "class": "ins-col-6  ins-m-col-6 ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(total),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-m-col-6 ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})

        back_url = self.ins._server._url({"mode":"delivery"},["id"])
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m  -address-card","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        if type(asession) == dict and "type" in asession and  asession["type"] == "store":
            
            stores = self.ins._db._get_data("gla_address","*",update_lang=True)
            for s in stores:
               if str(s["id"]) == str(asession["id"]):
                  store = s
            ainfo = [
            {"_data": "Pickup Address","_data-ar": "عنوان الاستلام ", "_trans":"true","class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "},
            {"class":"ins-space-s"},
            {"_data": store.get("title",""),"class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
            {"_data": store.get("address",""), "class": "ins-col-12 ins-grey-color"},
            {"_data": f"Phone: {store['phone']} | WhatsApp: {store['whatsapp']} | Email:  {store['email']}" ,"_data-ar": f"هاتف: {store['phone']} | واتساب: {store['whatsapp']} | بريد الكتروني:  {store['email']}" ,"_trans":"true","class":"ins-col-12 ins-grey-d-color ins-strong-m ins-title-14 not-for-phone"},
            {"end": "true"},
            {"class":"ins-space-xl"}
            ]
        else:
           address = self.ins._db._get_row("gla_user_address","*",f"id='{asession['id']}'")
           ainfo = [
           {"_data": "Shipping Address","_data-ar":"عنوان الشحن","_trans":"true", "class": "ins-col-6 ins-title-s ins-grey-d-color ins-strong-l ins-m-col-6"},
           {"class":"ins-space-s"},
           {"_data": address.get("title",""), "class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
           {"_data": address.get("address",""), "class": "ins-col-12 ins-grey-color"},
           {"_data": f"Mobile: {address.get('phone','')} | Email: {address.get('email','')}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14 not-for-phone"},
           {"_data": f"Mobile: {address.get('phone','')} ", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14 not-for-web"},
           {"end": "true"},
           {"class":"ins-space-xl"}
           ]
        uidata+=ainfo
        if subtotal < 20000:
             uidata.append({"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","_data-ar":"اتمام الشراء","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-grey-l  ins-text-upper","style":"    height: 46px;color:white;"})
             remaining = 20000 - subtotal
             n = self.ins._data._format_currency(float(remaining), symbol=False)
             remaining = f"{n} EGP"
      
             msg = f"Add {remaining} to place your order"
             if self.ins._langs._this_get()["name"] == "ar":
                 remaining = f"{n} جنيه"
                 msg = f"أضف {remaining} لإتمام طلبك"
             uidata.append({"_data": msg,"class":"ins-col-12  ins-text-center"})
        else:
           uidata.append({"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","_data-ar": "اتمام الشراء ","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper -submit-order-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
       

        
        
        
        
        
        
        
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "_data-ar":"رجوع","_trans":"true","class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	-back-btn","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "_data-ar":"سيتم حفظ معلوماتك في حساب المتجر. من خلال الاستمرار، فإنك توافق على سياسة المتجر","_trans":"true","class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})
        
        
        if string:
         return self.ins._ui._render( uidata)
        else:
         return uidata


    def ui(self):
        pdata = self.ins._server._get_session(self.session_payment_name)
        sclass = "ins-hidden"
        if pdata and pdata["type"] !="":
          ddata = self.ins._db._get_row("gla_payment_methods","*",f"id='{pdata['type']}'")
          if ddata["charges"] !="":
            sclass = ""

       
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        uidata.append({"start":"true","class":"ins-col-12 ins-flex"})
        uidata.append({"start":"true","class":"ins-col-12 ins-gap-o"})
        uidata.append({"_data":"payment","_data-ar":"دفع","_trans":"true","class":"ins-col-12 ins-title-m		 ins-strong-m ins-grey-d-color ins-text-upper"})
        uidata.append({"_data":"All transactions are secure and encrypted","_data-ar":"جميع المعاملات آمنة ومشفرة","_trans":"true","class":"ins-col-12 ins-title-xs ins-grey-color -step-des"})
        
        
        uidata.append({"_data":" Checkout charges may apply","_data-ar":"قد يتم تطبيق رسوم الدفع الالكتروني","_trans":"true","class":f"ins-col-12 ins-card ins-info -extra-fees-card {sclass}"})
        
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})
        
        
        
        payments = self.ins._db._get_data("gla_payment_methods","*",update_lang=True)

        i = 0
        for payment in payments:
            i +=1
            img = "style/radio.svg"
            pclass = ""
            if pdata:
                if str(pdata["type"]) == str(payment["id"]):
                   img = "style/radio_checked_b.svg"
                   pclass = "ins-active"


            pcard = [
                     {"start":"true","class":"ins-col-12 ins-flex ins-gap-o"},
                     {"start":"true","data-name":payment["id"],"class":f"{pclass} ins-col-12 ins-flex-center -payment-type-btn ins-m-flex-start {payment.get('class','')}"},
                     {"_type":"img","src":f"{p}{img}","loading":"lazy","class":"-payment-type-btn-img"},
                     {"_data": payment["title"],"class":"ins-strong-m ins-grey-m-color payment-title"},
               ]
            if payment["charges_type"] !="" and payment["charges"] !="":
               pcard = [
                     {"start":"true","class":"ins-col-12 ins-flex ins-gap-o"},
                     {"start":"true","data-charges_type":payment["charges_type"],"data-charges":payment["charges"],"data-name":payment["id"],"class":f"{pclass} ins-col-12 ins-flex-center -payment-type-btn ins-m-flex-start {payment.get('class','')}"},
                     {"_type":"img","src":f"{p}{img}","loading":"lazy","class":"-payment-type-btn-img"},
                     {"_data": payment["title"],"class":"ins-strong-m ins-grey-m-color payment-title"},
               ]
           
            pcard.append({"class":"ins-col-grow ins-m-col-6"})
            if payment['logo']:
               pcard.append({"_type":"img","src":f"{p}{payment['logo']}","loading":"lazy","class":"ins-flex-end -payment-img","style":"max-width:40px"})
            
            pcard.append({"end":"true"})
            pcard.append({"_data":payment["des"],"class":f"ins-col-12 ins-title-xs ins-grey-color ins-text-none -payment-subtype-area -payment-subtype-area-{payment['id']} {pclass}"})
            pcard.append({"end":"true"})
            uidata+=pcard
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex -items-area  ins-padding-2xl","style":"background:white;   border-left: 1px solid var(--primary-l);"})
        uidata+=self.items_area()
        uidata.append({"end":"true"})
        return uidata
   
   

    def out(self):

        return self.ui()