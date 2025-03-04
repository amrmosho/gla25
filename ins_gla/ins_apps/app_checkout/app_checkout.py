from urllib.parse import parse_qs, urlparse

from flask import request
from ins_gla.ins_apps.app_checkout.app_cart import AppCart
from ins_gla.ins_apps.app_checkout.app_delivery import AppDelivery
from ins_gla.ins_apps.app_checkout.app_payment import AppPayment
from ins_gla.ins_kit._elui import ELUI
from ins_gla.ins_kit._gusers import Gusers
from ins_gla.ins_kit._payment import PaymobAPI
from ins_kit._engine._bp import App
p = "/ins_web/ins_uploads/"
class AppCheckout(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)
    @property
    def session_name(sel):
        return "glaproducts"
    


    @property
    def session_address_name(sel):
        return "glaaddress"
    @property
    def session_payment_name(sel):
        return "glapayment"
    

    def _update_item_data(self):
       data = self.ins._server._post()
       sdata = self.ins._server._get_session(self.session_name)
       sdata[data["k"]]["count"] = data["value"]
       self.ins._server._set_session(self.session_name,sdata)
       r = self.ins._ui._render(self._cart_step_summary())
       
       return r
    

    
    def update_cart_price(self):
     sedata = self.ins._server._get_session(self.session_name)
     ndata = {}
     for k,v in sedata.items():
       data = self.ins._db._get_row("gla_product","*",f"id='{v["id"]}'",update_lang=True)
       ndata[k] = v
       ndata[k]["price"] = data["price"]
     self.ins._server._set_session(self.session_name,ndata)
     return "1"
    

    def empty_cart(self):
      self.ins._server._del_session(self.session_name)
      return "1"


       
    
    def price_check(self):
        sedata = self.ins._server._get_session(self.session_name)
        checked = False
        change = [{"start":"true","class":"ins-col-12 ins-flex"}]   
        if sedata:
         for k,v in sedata.items():
             data = self.ins._db._get_row("gla_product","*",f"id='{v["id"]}'",update_lang=True)
             if str(v["price"]) != str(data["price"]):
                checked = True
                change += [
                     {"start": "true", "class": "ins-col-12 ins-flex -item-card"},
                     {"src": f"{p}{data["th_main"]}", "loading":"lazy","_type": "img", "class": "ins-radius-m", "style": "    width: 97px;"}, 
                     {"start": "true", "class": "ins-col-8 ins-flex"}, {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"},
                     {"_data": f"{data["title"]}", "class": "ins-col-12 ins-title-s	 ins-strong-l ins-grey-d-color", "style": "    !important;"},
                     {"_data": data.get("des", ""), "class": "ins-grey-color ins-col-12 ins-title-14", "style": "line-height: 20px; "},
                     {"end": "true"},
                     {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه","class": "-pro-price ins-col-12 ins-strong-l ins-primary-d-color ins-title-20"},
                     {"end": "true"},
                     {"class": "ins-line ins-col-12"},

                 ]
                
        if checked:
           uidata = [
              {"start":"true","class":"ins-padding-l ins-col-12 ins-flex"},
              {"_data":"Hello! The prices of the products in your cart have been updated. You can review the adjusted prices below.","_data-ar":"مرحبًا! تم تحديث أسعار المنتجات في سلة مشترياتك. يمكنك مراجعة الأسعار المعدلة أدناه.","_trans":"true","class":"ins-title-s ins-grey-d-color ins-col-12"}]
           uidata += change
           uidata +=[
                            {"start":"true","class":"ins-col-12 ins-flex-space-between"},

              {"_data":"Update cart","_data-ar":"تحديث السلة","_trans":"true","class":"ins-button-s ins-gold ins-col-4 -update-cart-price-btn"},
              {"_data":"Empty Cart","_data-ar":"تفريغ السلة","_trans":"true","class":"ins-button-s ins-gold-color ins-col-4 -empty-cart-btn"},
              {"end": "true"},
              {"end": "true"}

           ]
           
           return self.ins._ui._render(uidata)
        return "1"
                

    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata=self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"]) 
        self.ins._server._set_session(self.session_name,sedata)
        ndata=self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"
        r["ui"] = self.ins._ui._render(self._cart_step_summary())
        if not ndata:
            uidata=[
              {"start":"true","class":"ins-col-12  ins-flex-center","style":"position: relative;top: 20px;"},
              {"_data":"There is no items in cart yet","_data-ar":"لا يوجد أي عناصر في سلة التسوق بعد","_trans":"true","class":"ins-col-8 ins-card ins-padding-2xl ins-text-center"},
              {"end":"true"}
              ]           
           
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)
        return r
    def _mobile_no_ui(self):
        uidata=[
           {"start":"true","class":"ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
           {"start":"true","class":"ins-col-5 ins-flex-end ins-card -mobile-form  ins-text-start"},
           {"_data":"Login","class":"ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
           {"_type":"input","title":"Mobile Number","placeholder":"Enter Mobile Number","type":"number","name":"mobile","_start":"+20","class":"-login-mobile-inpt","pclass":"ins-col-12"},
           {"class":"ins-line ins-col-12"},
           {"_data":"Send OTP","class":"ins-button-s ins-gold-d ins-col-4 -guser-m-btn"},
           {"end":"true"}
           ,{"end":"true"}
           ]
        return uidata
    def _otp_ui(self):
        rq = self.ins._server._post()
        uidata=[
           {"start":"true","class":"ins-col-5 ins-flex-center ins-card -otp-form  ins-text-start"},
           {"_data":"Login","class":"ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
           {"_type":"input","title":"OTP","placeholder":"----","type":"text","name":"otp","class":"ins-title-l -login-otp-inpt ins-form-input ins-text-center","pclass":"ins-col-6","style":"  letter-spacing: 25px;    height: 60px;"},
           {"_type":"input","type":"text","name":"mobile","value":rq["mobile"],"class":"-login-mobile-inpt","pclass":"ins-col-12 ins-hidden"},
           {"_data": "Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span>","class":"ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
           {"_data": "Resend OTP","class":"ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn ins-hidden","style":"cursor:pointer;"},
           {"class":"ins-line ins-col-12"},
           {"start":"true","class":"ins-col-12 ins-flex-end"},
           {"_data":"Login","class":"ins-button-s ins-gold-d ins-col-5 -guser-o-btn"},
           {"end":"true"},
           {"end":"true"}
           ]
        return self.ins._ui._render( uidata)
    def _login_mobile(self):
        chck = self.user._mobile_login()
        if(chck == "1"):
            return self._otp_ui()
        else:
            return "-1"
    def _login_otp(self):
        chck = self.user._otp_check()
        if(chck):
            return "1"
        else:
            return "-1"
    def header_ui(self):
        rq = self.ins._server._req()
        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({},["mode","id","alias","filter"])
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","_data-ar":"الرئيسية /","_trans":"true","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "Checkout","_data-ar":"الدفع","_trans":"true","class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]
        uidata+=path
        if rq["mode"] == "cart":
           uidata.append({"_data":"My Cart","_data-ar":"عربة التسوق","_trans":"true","class":"ins-col-6 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        elif rq["mode"] == "delivery":
            uidata.append({"_data":"Delivery Details","_data-ar":"تفاصيل التسليم","_trans":"true","class":"ins-col-6 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        else:
           uidata.append({"_data":"Payment Information","_data-ar":"معلومات الدفع","_trans":"true","class":"ins-col-6 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        steps = [
            {
             "text":"My Cart",
             "text-ar":"عربة التسوق",
             "img":"ecart.svg",
             "mode":"cart",
             "url":"/checkout/cart"
             },
            {
             "text":"Delivery",          
             "text-ar":"تفاصيل التسليم",
             "img":"truck.svg",
             "mode":"delivery",
             "url":"/checkout/delivery"
             },
            {
             "text":"Payment",             
             "text-ar":"معلومات الدفع",
             "img":"money.svg",
             "mode":"payment",
             "url":"/checkout/payment"
             },
        ]

        ## checkout steps
        uidata.append({"start":"true","class":"ins-col-grow ins-flex-end"})
        i = 0
        sp = ""
        for s in steps:
         i+=1

         text = "<img src='"+p +"style/"+ s["img"]+"'></img>"+f"{i}"+". "+s["text"]
         style = "rotate:180deg;"
         lbtitle = "Change in price"

         if self.ins._langs._this_get()["name"] == "ar":
            text = "<img src='"+p +"style/"+ s["img"]+"'></img>"+f"{i}"+". "+s["text-ar"]
            style = ""
            lbtitle = "تغير في السعر"
         uidata.append({"class": sp,"style":style})

         active = ""
         if "mode" in rq and rq["mode"] == s["mode"]:
            active = "ins-gold-bg"
         if s["mode"] !="payment":
          uidata.append({"_type":"a","data-url":s["url"],"_data": text, "class": f"ins-button-s -step-button ins-flex-center -{s["mode"]}-btn -cart-next-btn {active}","data-lbtitle":lbtitle})
         else:
          uidata.append({"_type":"a","data-url":s["url"],"_data": text, "class": f"ins-button-s -step-button ins-flex-center -{s["mode"]}-btn {active}","data-lbtitle":lbtitle})

         sp="lni lni-chevron-left"
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        return uidata
    def _check_address(self):
       saddress = self.ins._server._get_session(self.session_address_name)
       if type(saddress) == dict and "id" in saddress and "type" in saddress:
          if saddress["type"] == "store":
             store = self.ins._db._get_row("gla_address","*",f"id='{saddress["id"]}'")
             if store:
               return "1"
             else:
                return "-1"
          address = self.ins._db._get_row("gla_user_address","*",f"id='{saddress["id"]}'")
          if address:
            return "1"
          else:
             return "-1"
       else:
          return "-1"
       
    def _select_address(self):
       post = self.ins._server._post()
       adddress = {"type":post["type"],"id":post["aid"]}
       self.ins._server._set_session(self.session_address_name,adddress)
       return "1"
   
   
    def _addresses_area_ui(self,string=True):
        rsdata=  self.user._check()
        addesses = self.ins._db._get_data("gla_user_address","*",f"fk_user_id = '{rsdata["id"]}' order by kit_created ASC",update_lang=True)
        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Saved Address","_data-ar":"العناوين المحفوظة ","_trans":"true","class":"ins-col-9 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_data": "Add Address","_data-ar":" إضافة عنوان","_trans":"true","class": "ins-button-s -add-address ins-text-center ins-strong-m ins-col-3 ins-gold-bg  ins-text-upper"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) != dict:
           asession = {"type":"delivery","id":"-1"}
        
        if addesses:
           for a in addesses:
              img = "style/radio.svg"
              if str(a["id"]) == str(asession["id"]) and asession["type"] == "delivery":
                 img = "style/radio_checked.svg"
              uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
              uidata.append({"_data":"<img data-aid = "+f"{a["id"]}"+" class='-address-btn' data-type='delivery' src='"+p + img+"'></img>","class":"ins-flex ins-col-1"})
              uidata.append({"start":"true","class":"ins-col-9 ins-flex"})
              uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
              uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
              uidata.append({"_data": "Mobile: "+a["phone"] + " | Email: "+ a["email"],"class":"ins-grey-d-color ins-col-12  ins-title-14"})
              uidata.append({"end":"true"})
              uidata.append({"start":"true","class":"ins-col-2 ins-flex-end"})
              uidata.append({"_data":"<i  class='-update-address  _a lni lni-pencil-1' data-aid = "+ str(a["id"])+"></i>","class":"ins-text-center"})
              uidata.append({"_data":"<i  class='lni lni-trash-3 _a_red'></i>","data-aid":a["id"],"class":"ins-text-center -remove-address-btn"})
              uidata.append({"end":"true"})
              uidata.append({"end":"true"})
        else:
           uidata.append({"start":"true","class":"ins-col-12 ins-card ins-padding-m ins-flex-center"})
           uidata.append({"_data":"No saved addresses yet","_data-ar":"لا يوجد عناوين محفوظة","_trans":"true"})
           uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
    
    
    def _store_area_ui(self,string=True):
        stores = self.ins._db._get_data("gla_address","*",update_lang=True)

        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Our Stores","_data-ar":"متاجرنا","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) != dict:
           asession = {"type":"store","id":"-1"}
        for a in stores:
           img = "style/radio.svg"
           if str(a["id"]) == str(asession["id"])  and asession["type"] == "store":
              img = "style/radio_checked.svg"
           uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
           uidata.append({"_data":"<img data-aid = "+f"{a["id"]}"+" class='-address-btn' data-type='store' src='"+p + img+"'></img>","class":"ins-flex ins-col-1"})
           uidata.append({"start":"true","class":"ins-col-11 ins-flex"})
           uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
           uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
           uidata.append({"_data": f"Phone: {a["phone"]} | WhatsApp: {a["whatsapp"]} | Email:  {a["email"]}" ,"_data-ar": f"هاتف: {a["phone"]} | واتساب: {a["whatsapp"]} | بريد الكتروني:  {a["email"]}" ,"_trans":"true","class":"ins-grey-d-color ins-col-12   ins-title-14"})
           uidata.append({"end":"true"})
           uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
    
    
    
    
    def _select_address_ui(self):
       data = self.ins._server._post()
       if "type" in data:
          if data["type"]== "delivery":
             return self._addresses_area_ui(True)
          else:
             return self._store_area_ui(True)
    
    
    

   
   
    def _remove_address(self):
      data = self.ins._server._post()
      self.ins._db._update("gla_user_address",{"kit_deleted":"1"},f"id='{data["aid"]}'")
      return "1"
    def _add_address(self):
       sdata = self.user._check()
       data = self.ins._server._post()
       data["fk_user_id"] = sdata["id"]
       data["title"] = data["first_name"] + " " +data["last_name"] 
       data["kit_modified"] = self.ins._date._date_time()
       aid = self.ins._db._insert("gla_user_address",data)
       adta = {
          "type":"delivery","id":aid
       }
       self.ins._server._set_session(self.session_address_name,adta)
       return self._addresses_area_ui()
    def _update_address(self):
       sdata = self.user._check()
       data = self.ins._server._post()
       data["fk_user_id"] = sdata["id"]
       data["title"] = data["first_name"] + " " +data["last_name"] 
       self.ins._db._update("gla_user_address",data,f"id='{data["address_id"]}'")
       adta = {
          "type":"delivery","id":data["address_id"]
       }
       self.ins._server._set_session(self.session_address_name,adta)
       return self._addresses_area_ui()
    
    def _update_address_ui(self):
        rq = self.ins._server._post()
        address = self.ins._db._get_row("gla_user_address","*",f"id='{rq["aid"]}'")
        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -update-address-area"})
        uidata.append({"_data": "Edit Address","_data-ar":"تعديل العنوان","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","value":address["first_name"],"type":"text","required":"true","placeholder":"First name*","placeholder-ar":"الاسم الأول*","_trans":"true","name":"first_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["last_name"],"type":"text","required":"true","placeholder":"Last name*","placeholder-ar":" اسم العائلة*","_trans":"true","name":"last_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["email"],"type":"text","required":"true","placeholder":"Email*","placeholder-ar":" بريد إلكتروني*","_trans":"true","name":"email","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["phone"],"type":"text","required":"true","placeholder":"Phone*","placeholder-ar":" هاتف*","_trans":"true","name":"phone","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["state"],"type":"text","required":"true","placeholder":"State*","placeholder-ar":" ولاية*","_trans":"true","name":"state","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["city"],"type":"text","required":"true","placeholder":"City*","placeholder-ar":" مدينة*","_trans":"true","name":"city","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address"],"type":"text","required":"true","placeholder":"Street address*","placeholder-ar":" عنوان الشارع*","_trans":"true","name":"address","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address_2"],"type":"text","placeholder":"Apartment, suits, etc (Optional)","placeholder-ar":"شقة، جناح، الخ (اختياري)*","_trans":"true","name":"address_2","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["id"],"type":"text","placeholder":"ID","name":"address_id","pclass":"ins-hidden"})
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})

        update = "Update Address <i class='lni lni-arrow-right'></i>"
        if self.ins._langs._this_get()["name"] == "ar":
          update = "تعديل العنوان <i class='lni lni-arrow-left'></i>"

       
        uidata.append({"_data": update, "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -update-address-btn ins-gold-d ins-col-4","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back", "_data-ar": " رجوع", "_trans": "true", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    
    def _add_address_ui(self):
        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -add-address-area"})
        uidata.append({"_data":"Add new Address","_data-ar":"إضافة عنوان جديد","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"First name*","placeholder-ar":"الاسم الأول*","_trans":"true","name":"first_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Last name*","placeholder-ar":" اسم العائلة*","_trans":"true","name":"last_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Email*","placeholder-ar":" بريد إلكتروني*","_trans":"true","name":"email","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Phone*","placeholder-ar":" هاتف*","_trans":"true","name":"phone","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"State*","placeholder-ar":" ولاية*","_trans":"true","name":"state","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"City*","placeholder-ar":" مدينة*","_trans":"true","name":"city","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Street address*","placeholder-ar":" عنوان الشارع*","_trans":"true","name":"address","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","placeholder":"Apartment, suits, etc (Optional)","placeholder-ar":"شقة، جناح، الخ (اختياري)*","_trans":"true","name":"address_2","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Add Address <img src='"+p+"style/right_arrow.svg'></img>","_data-ar":"إضافة عنوان ","_trans":"true", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -add-address-btn ins-gold-d ins-col-3","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back","_data-ar":"رجوع","_trans":"true", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    
    
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
  
  
  
    def items_area(self,string= False):
        ## Items Area
        uidata = []
        sedata=self.ins._server._get_session(self.session_name)
        rq = self.ins._server._req()
        subtotal = 0
        chargs = 0
        for k,v in sedata.items():
            subtotal+= float(v["price"]) * float(v["count"])
            uidata+= ELUI(self.ins).small_pro_block(v)
            uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-line ins-col-12"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"_data": "Voucher", "_data-ar":" قسيمة","_trans":"true","class": "ins-col-12  ins-grey-d-color ins-strong-m  "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","placeholder-ar":" رمز","_trans":"true","name":"voucher","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details","_data-ar":"تفاصيلك","_trans":"true", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "_data-ar":"المجموع الفرعي","_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -subtotal-text"})
        pclass = "ins-hidden"

        total = subtotal  
        uidata.append({"start": "true", "class": f"-online-payment-fee  ins-col-12 ins-flex {pclass}"})
        uidata.append({"_data": "Online payment fee","_data-ar": "رسوم الدفع عبر الإنترنت", "_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(chargs),"data-value" : chargs,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -chargs-text"})
        uidata.append({"end": "true"})
        uidata.append({"_data": "Shipping", "_data-ar":" شحن","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","_data-ar": "مجاني","_trans":"true","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "_data-ar":" المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(total),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        lbtitle = "Change in price"
        if self.ins._langs._this_get()["name"] == "ar":
         lbtitle = "تغير في السعر"


        if "mode" in rq and rq["mode"] == "delivery":
         back_url = self.ins._server._url({"mode":"cart"},["id"])
        else:
         back_url = self.ins._server._url({"mode":"delivery"},["id"])
        if "mode" in rq and rq["mode"] == "payment":
            uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
            asession = self.ins._server._get_session(self.session_address_name)
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
                {"_data": f"Phone: {store["phone"]} | WhatsApp: {store["whatsapp"]} | Email:  {store["email"]}" ,"_data-ar": f"هاتف: {store["phone"]} | واتساب: {store["whatsapp"]} | بريد الكتروني:  {store["email"]}" ,"_trans":"true","class":"ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
                {"end": "true"},
                {"class":"ins-space-xl"}
                ]
            else:
               address = self.ins._db._get_row("gla_user_address","*",f"id='{asession["id"]}'")
               ainfo = [
               {"_data": "Shipping Address","_data-ar":"عنوان الشحن","_trans":"true", "class": "ins-col-8 ins-title-s ins-grey-d-color ins-strong-l "},
               {"_data": "Edit Address","_data-ar":"تعديل العنوان","_trans":"true","data-aid" : str(address["id"]),"class": "-update-address ins-col-4 ins-flex-end ins-gold-d-color ins-strong-m ins-text-upper ins-button-text"},
               {"class":"ins-space-s"},
               {"_data": address.get("title",""), "class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
               {"_data": address.get("address",""), "class": "ins-col-12 ins-grey-color"},
               {"_data": f"Mobile: {address.get("phone","")} | Email: {address.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
               {"end": "true"},
               {"class":"ins-space-xl"}
               ]
            uidata+=ainfo
            uidata.append({"data-lbtitle":lbtitle,"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","_data-ar": "اتمام الشراء ","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper -submit-order-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        else:
          uidata.append({"data-lbtitle":lbtitle,"data-url":"/checkout/payment/","_data": "Procced to payment <img src='"+p+"style/right_arrow.svg'></img>", "_data-ar":" انتقل إلى الدفع","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -payment-btn  ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "_data-ar":"رجوع","_trans":"true","class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "_data-ar":"سيتم حفظ معلوماتك في حساب المتجر. من خلال الاستمرار، فإنك توافق على سياسة المتجر","_trans":"true","class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})
        
        
        if string:
         return self.ins._ui._render( uidata)
        else:
         return uidata


    
    def payment_items_area(self):
        ## Items Area
        uidata = []
        sedata=self.ins._server._get_session(self.session_name)
        subtotal = 0
        chargs = 0
        for k,v in sedata.items():
            if v.get("new_price"):
             subtotal+= float(v["new_price"]) * float(v["count"])
            else:
             subtotal+= float(v["price"]) * float(v["count"])

            uidata+= ELUI(self.ins).small_pro_block(v)
            uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"class":"ins-line ins-col-12"})
        uidata.append({"class":"ins-space-m"})
        uidata.append({"_data": "Voucher", "_data-ar":" قسيمة","_trans":"true","class": "ins-col-12  ins-grey-d-color ins-strong-m  "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","placeholder-ar":" رمز","_trans":"true","name":"voucher","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details","_data-ar":"تفاصيلك","_trans":"true", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "_data-ar":"المجموع الفرعي","_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -subtotal-text"})
        pclass = "ins-hidden"

        total = subtotal  
        uidata.append({"start": "true", "class": f"-online-payment-fee  ins-col-12 ins-flex {pclass}"})
        uidata.append({"_data": "Online payment fee","_data-ar": "رسوم الدفع عبر الإنترنت", "_trans":"true","class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(chargs),"data-value" : chargs,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -chargs-text"})
        uidata.append({"end": "true"})
        uidata.append({"_data": "Shipping", "_data-ar":" شحن","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","_data-ar": "مجاني","_trans":"true","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "_data-ar":" المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(total),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})


        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        asession = self.ins._server._get_session(self.session_address_name)
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
             {"_data": f"Phone: {store["phone"]} | WhatsApp: {store["whatsapp"]} | Email:  {store["email"]}" ,"_data-ar": f"هاتف: {store["phone"]} | واتساب: {store["whatsapp"]} | بريد الكتروني:  {store["email"]}" ,"_trans":"true","class":"ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
             {"end": "true"},
             {"class":"ins-space-xl"}
             ]
        else:
            address = self.ins._db._get_row("gla_user_address","*",f"id='{asession["id"]}'")
            ainfo = [
            {"_data": "Shipping Address","_data-ar":"عنوان الشحن","_trans":"true", "class": "ins-col-8 ins-title-s ins-grey-d-color ins-strong-l "},
            {"_data": "Edit Address","_data-ar":"تعديل العنوان","_trans":"true","data-aid" : str(address["id"]),"class": "-update-address ins-col-4 ins-flex-end ins-gold-d-color ins-strong-m ins-text-upper ins-button-text"},
            {"class":"ins-space-s"},
            {"_data": address.get("title",""), "class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
            {"_data": address.get("address",""), "class": "ins-col-12 ins-grey-color"},
            {"_data": f"Mobile: {address.get("phone","")} | Email: {address.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
            {"end": "true"},
            {"class":"ins-space-xl"}
            ]
        uidata+=ainfo
        lbtitle = "Change in price"

        if self.ins._langs._this_get()["name"] == "ar":
            lbtitle = "تغير في السعر"

        uidata.append({"data-lbtitle":lbtitle,"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","_data-ar": "اتمام الشراء ","_trans":"true","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper -submit-order-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":"/checkout/delivery/","_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "_data-ar":"رجوع","_trans":"true","class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "_data-ar":"سيتم حفظ معلوماتك في حساب المتجر. من خلال الاستمرار، فإنك توافق على سياسة المتجر","_trans":"true","class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})
        
        
        return self.ins._ui._render( uidata)

   

    
    def _update_payment_data(self):
      rq = self.ins._server._post()
      pdata = {
         "type": rq["name"]
      }
      self.ins._server._set_session(self.session_payment_name, pdata)
      sedata = self.ins._server._get_session(self.session_name)
      newdata = {}

      if rq.get("charges"):
         for k, s in sedata.items():
            newdata[k] = s
            if not newdata[k].get("old_price"):
               newdata[k]["old_price"] = s["price"]
            if rq["charges_type"] == "fixed":
               newdata[k]["charges"] = float(rq["charges"]) * float(s["weight"])
               newdata[k]["new_price"] = float(s["price"]) + float(rq["charges"])
            else:
               per = float(rq["charges"]) / 100
               newdata[k]["charges"] = (float(s["price"]) * per * float(s["weight"]))
               newdata[k]["new_price"] = float(s["price"]) + (float(s["price"]) * per)
         self.ins._server._set_session(self.session_name, newdata)
      else:
         for k, s in sedata.items():
            newdata[k] = s
            if newdata[k].get("old_price"):
             newdata[k]["new_price"] = newdata[k]["old_price"]
            else:
             newdata[k]["new_price"] = s["price"]
            newdata[k]["charges"] = 0
         self.ins._server._set_session(self.session_name, newdata)

      return self.payment_items_area()

   
   
    def _check_order_status(self):
       url = self.ins._server._req()["url"]
       parsed_url = urlparse(url)
       query_params = parse_qs(parsed_url.query)

       merchant_order_id = query_params.get("merchant_order_id", [None])[0]
       if merchant_order_id:
         order_data = self.ins._db._get_row("gla_order","*",f"id='{merchant_order_id}'")
       
       
       if order_data["payment_status"] == "failed":
          return "/checkout/payment/"
       elif str(order_data["payment_method"]) == "8":
          return "1"
       else:
            return "/puser/order/"

            


    def _placed_step(self):
           url = request.url
           parsed_url = urlparse(url)
           query_params = parse_qs(parsed_url.query)

           merchant_order_id = query_params.get("merchant_order_id", [None])[0]
           if merchant_order_id:
            order_data = self.ins._db._get_row("gla_order","*",f"id='{merchant_order_id}'")

           if order_data and order_data["payment_status"] != "failed":
              self.ins._server._del_session(self.session_name)
              self.ins._server._del_session(self.session_address_name)
              self.ins._server._del_session(self.session_payment_name)

           text = "You will be directed to orders page in <span class='-countdown ins-strong-m'>10</span> seconds"
           if self.ins._langs._this_get()["name"] == "ar":
                  text = "سوف يتم اعادة توجيهك لصفحة الطلبات في <span class='-countdown ins-strong-m'>10</span> ثوان"
           uidata = [
               {"start":"true","class":"ins-col-12 gla-container ins-flex-center ins-padding-2xl"},
               {"data-url":url,"class":"-url-area"},
               {"start":"true","class":"ins-col-8 ins-card ins-flex"},
                 {"class":" lni lni-check-circle-1 ins-font-4xl"},
                  {"start":"true","class":"ins-col-grow","style":"    padding: 0px;line-height: 15px;"},
                 {"_data":"Your order has been placed","_data-ar":"لقد تم اتمام طلبك","_trans":"true","class":"ins-title-s ins-strong-m ins-grey-d-color ins-col-12"},
                 {"_data":text,"class":"ins-title-14 ins-grey-color ins-col-12" ,"style":"    text-transform: lowercase;"},
                 {"end":"true"},
                 {"end":"true"}
               ]
           if order_data:
             if order_data["payment_status"] == "failed":
               text = "You will be redirected to the payment page to try again in <span class='-countdown ins-strong-m'>10</span> seconds"
               if self.ins._langs._this_get()["name"] == "ar":
                  text = " سيتم إعادة توجيهك إلى صفحة الدفع للمحاولة مرة أخرى في <span class='-countdown ins-strong-m'>10</span> ثوان"
               uidata = [
               {"start":"true","class":"ins-col-12 gla-container ins-flex-center ins-padding-2xl"},    
               {"data-url":url,"class":"-url-area"},
               {"start":"true","class":"ins-col-8 ins-card ins-flex"},
               {"class":" lni lni-xmark-circle ins-font-4xl ins-danger-color"},
               {"start":"true","class":"ins-col-grow","style":"    padding: 0px;line-height: 15px;"},
               {"_data":"There was an issue with the payment process.","_data-ar":"حدثت مشكلة أثناء عملية الدفع.","_trans":"true","class":"ins-title-s ins-strong-m ins-grey-d-color ins-col-12"},
               {"_data":text,"class":"ins-title-14 ins-grey-color ins-col-12" ,"style":"    text-transform: lowercase;"},
               {"end":"true"},
               {"end":"true"}
                 ]
                  
             if str(order_data["payment_method"]) == "8":
              text = f"Please transfer the amount of {order_data["total"]} EGP to one of the following bank accounts"
              if self.ins._langs._this_get()["name"] == "ar":
                  text = f"برجاء تحويل مبلغ {order_data["total"]} جينه الطلب لأحد الحسابات البنكية التالية"
              uidata = [
               {"start":"true","class":"ins-col-12 gla-container ins-flex-center ins-padding-2xl"},              
               {"data-url":url,"class":"-url-area"},
               {"start":"true","class":"ins-col-8 ins-card ins-flex"},
               {"class":" lni lni-check-circle-1 ins-font-4xl"},
               {"start":"true","class":"ins-col-grow","style":"    padding: 0px;line-height: 15px;"},
               {"_data":"Your order has been placed","_data-ar":"لقد تم اتمام طلبك","_trans":"true","class":"ins-title-s ins-strong-m ins-grey-d-color ins-col-12"},
               {"_data":text,"class":"ins-title-14 ins-grey-color ins-col-12" ,"style":"    text-transform: lowercase;"},
               {"end":"true"},
               {"end":"true"},
               {"class":"ins-space-l"}
               ]
              uidata += ELUI(self.ins)._bank_ui()
           return uidata
       




    def _ui(self):
        rq = self.ins._server._req()
        uidata = [{"start":"true","class":"ins-flex ","style":"background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata+=self.header_ui()
        uidata.append({"end":"true"})
        uidata.append({"start":"true","class":"ins-col-12 ins-flex-valign-start ins-gap-o gla-container","style":"position: relative;"})
        if "mode" in rq:
            if  rq["mode"] == "delivery":
              r=  self.user._check()
              if not r:
               self.ins._server._set_session("redirect", "/checkout/delivery")
               return """
               <script>
                   window.location.href = "/login/";
               </script>
               """
              else:
               uidata+= AppDelivery(self.app).out()
            elif rq["mode"] == "cart":
              uidata+= AppCart(self.app).out()
            elif rq["mode"] == "payment":
              uidata+= AppPayment(self.app).out()
            elif rq["mode"] == "order":
               uidata+=self._placed_step()
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    def no_data(self):
        uidata=[
              {"start":"true","class":"ins-col-12  ins-flex-center","style":"position: relative;top: 20px;"},
              {"_data":"There is no items in cart yet","_data-ar":"لا يوجد أي عناصر في سلة التسوق بعد","_trans":"true","class":"ins-col-8 ins-card ins-padding-2xl ins-text-center"},
              {"end":"true"}
              ]
        return self.ins._ui._render(uidata)
    
    def _get_chargs(self):
       sedata=self.ins._server._get_session(self.session_name)
       chargs = 0
       for k,v in sedata.items():
         chargs+= (float(v["weight"]) * float(v["count"])) * 20

       return str(chargs)

    
    def _submit_order(self):
         sdata = self.user._check()
         sedata=self.ins._server._get_session(self.session_name)
         address = self.ins._server._get_session(self.session_address_name)
         payment = self.ins._server._get_session(self.session_payment_name)
         r = {}
         if not payment:
            r["status"] == "-1"
            return r
         total =0 
         for k,v in sedata.items():
            total+= (float(v["price"]) * float(v["count"]))

         if total > 200000:
            total = total
            shipping =0
         else:
            shipping = 200
            total = total + 200
        
         order = {
            "fk_user_id":sdata["id"],
            "fk_address_id":address["id"],
            "delivery_type":address["type"],
            "payment_method":payment["type"],
            "total":total,
            "kit_modified":self.ins._date._date_time(),
            "payment_status":"pending",
            "order_status":"pending",
            "shipping":shipping
         }
         oid = self.ins._db._insert("gla_order",order)
         payment_url = ""
         ddata = self.ins._db._get_row("gla_payment_methods","*",f"id='{payment["type"]}'")
         if ddata["paymob_id"]:
            paymob = PaymobAPI()
            paytotal = total * 100
            payment_url = paymob.create_pay_wdgt(paytotal, oid, ddata["paymob_id"] )

         for k,v in sedata.items():
            kart = self.ins._db._get_row("gla_product","kart",f"id='{v["id"]}'")["kart"]
            gmprice = self.ins._db._get_row("gla_price","sell_24",f"1=1 order by id desc")["sell_24"]

            if kart == "21":
               gmprice = self.ins._db._get_row("gla_price","sell",f"1=1 order by id desc")["sell"]

            order_item = {
               "fk_order_id":oid,
               "fk_product_id":v["id"],
               "quantity":v["count"],
               "type":v["type"],
               "subtype":v["subtype"],
               "price":v["price"],
               "charges":v["charges"],
               "gram_price":gmprice,
              "gift_card": v["gift_card"]

            }
            self.ins._db._insert("gla_order_item",order_item)
         if payment_url:
            r["status"] = "2"
            r["url"] = payment_url
            return r
         else:
            r["status"] = "1"
            r["oid"] = oid
            return r
    
 

    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")


        if self.ins._langs._this_get()["name"] == "ar":
          self.app._include("style_ar.css")
        else:
          self.app._include("style_en.css")

        sdata = self.ins._server._get_session(self.session_name)
        if sdata:
           return self._ui()
        else:
            return self.no_data()
