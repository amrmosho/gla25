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
       return "1"
    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata=self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"]) 
        self.ins._server._set_session(self.session_name,sedata)
        ndata=self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"
        if not ndata:
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-gold ins-text-upper ins-text-center ins-title-12","style":"padding: 7px;margin-top: 30px;"}]
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
        home_url = self.ins._server._url({},["mode","id","alias"])
        products_url = self.ins._server._url({"alias":"product"},["mode","id"])
        product_url = self.ins._server._url({"alias":"product","mode":"product","id":1})
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":products_url,"_data": "Product /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":product_url,"_data": "250gm Gold Bar /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "Checkout","class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]
        uidata+=path
        if rq["mode"] == "cart":
           uidata.append({"_data":"My Cart","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        elif rq["mode"] == "delivery":
            uidata.append({"_data":"Delivery Details","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        else:
           uidata.append({"_data":"Payment Information","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        steps = [
            {"text":"My Cart",
             "img":"ecart.svg",
             "mode":"cart",
             "url":"/checkout/cart"
             },
               {"text":"Delivery",
             "img":"truck.svg",
             "mode":"delivery",
             "url":"/checkout/delivery"
             },
               {"text":"Payment",
             "img":"money.svg",
             "mode":"payment",
             "url":""
             },
        ]
        ## checkout steps
        uidata.append({"start":"true","class":"ins-col-5 ins-flex"})
        i = 0
        sp = ""
        for s in steps:
         active = ""
         i+=1
         uidata.append({"class": sp,"style":"rotate:180deg"})
         if "mode" in rq and rq["mode"] == s["mode"]:
            active = "ins-gold-bg"
         if s["mode"] != "payment":
            uidata.append({"_type":"a","href":s["url"],"_data": "<img src='"+p +"style/"+ s["img"]+"'></img>"+f"{i}"+". "+s["text"], "class": f"ins-button-s -step-button ins-flex-center {active}"})
         else:
            uidata.append({"_data": "<img src='"+p +"style/"+ s["img"]+"'></img>"+f"{i}"+". "+s["text"], "class": f"ins-button-s -step-button ins-flex-center {active} -payment-step-btn"})
         sp="lni lni-chevron-left"
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        return uidata
    def _check_address(self):
       saddress = self.ins._server._get_session(self.session_address_name)
       if type(saddress) == dict and "id" in saddress and "type" in saddress:
          if saddress["type"] == "store":
             return "1"
          address = self.ins._db._get_row("gla_address","*",f"id='{saddress["id"]}'")
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
        addesses = self.ins._db._get_data("gla_address","*",f"fk_user_id = '{rsdata["id"]}' order by kit_created ASC")
        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Saved Address","class":"ins-col-9 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_data": "Add Address", "class": "ins-button-s -add-address ins-text-center ins-strong-m ins-col-3 ins-gold-bg  ins-text-upper"})
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
           uidata.append({"_data":"No saved addresses yet"})
           uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
    def _store_area_ui(self,string=True):
        stores = [
           {"id":"1","address":"60 El Moez Le Din Allah St., El Gamalia, Cairo","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"},
           {"id":"2","address":"Street 88 , Palm Hills , 6th of October, Giza","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"}
        ]
        uidata=[{"start":"true","class":"ins-col-12 ins-flex  -addresses-area"}]
        uidata.append({"_data":"Our Stores","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
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
           uidata.append({"_data": f"Phone: {a["phone"]} | WhatsApp: {a["whatsapp"]} | Email:  {a["email"]}" ,"class":"ins-grey-d-color ins-col-12   ins-title-14"})
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
    def _addresses_step(self):
        asession = self.ins._server._get_session(self.session_address_name)
      ## Addresses Area
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        uidata.append({"_data":"Select delivery type","class":"ins-col-12 ins-title-s ins-strong-m ins-grey-d-color "})
        atype_btns= [{"_data": "<img class='-address-radio-btn' src='"+p + "style/radio_checked.svg"+"'></img>"+"Home Delivery", "data-type":"delivery","class": f"ins-button-s ins-text ins-col-6  ins-gold-bg ins-flex-center -delivery-type-btn ins-strong-m ins-gold-bg"},
                {"_data": "<img class='-address-radio-btn' src='"+p +"style/radio.svg"+"'></img>"+"Pickup in Store", "data-type":"store","class": f"ins-button-s  ins-col-6 ins-flex ins-flex-center -delivery-type-btn ins-strong-m inactive insactive"}
                ]
        if type(asession) == dict and "type" in asession and  asession["type"] == "store":
         atype_btns= [{"_data": "<img class='-address-radio-btn' src='"+p +"style/radio.svg"+"'></img>"+"Home Delivery", "data-type":"delivery","class": f"ins-button-s ins-text ins-col-6 ins-flex-center -delivery-type-btn ins-strong-m inactive"},
                {"_data": "<img class='-address-radio-btn' src='"+p + "style/radio_checked.svg"+"'></img>"+"Pickup in Store", "data-type":"store","class": f"ins-button-s  ins-col-6 ins-flex ins-flex-center -delivery-type-btn ins-strong-m  ins-gold-bg"}
                ]
        uidata+=atype_btns
        uidata.append({"class":"ins-space-l"})
        asession = self.ins._server._get_session(self.session_address_name)
        if type(asession) == dict and "type" in asession and  asession["type"] == "store":
           uidata+=self._store_area_ui(False)
        else:
           uidata+=self._addresses_area_ui(False)
        uidata.append({"end":"true"})
        ## Items Area
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;   border-left: 1px solid var(--primary-l);"})
        uidata+=self.items_area()
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"end":"true"})
        return uidata
    def _remove_address(self):
      data = self.ins._server._post()
      self.ins._db._update("gla_address",{"kit_deleted":"1"},f"id='{data["aid"]}'")
      return "1"
    def _add_address(self):
       sdata = self.user._check()
       data = self.ins._server._post()
       data["fk_user_id"] = sdata["id"]
       data["title"] = data["first_name"] + " " +data["last_name"] 
       aid = self.ins._db._insert("gla_address",data)
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
       self.ins._db._update("gla_address",data,f"id='{data["address_id"]}'")
       adta = {
          "type":"delivery","id":data["address_id"]
       }
       self.ins._server._set_session(self.session_address_name,adta)
       return self._addresses_area_ui()
    def _update_address_ui(self):
        rq = self.ins._server._post()
        address = self.ins._db._get_row("gla_address","*",f"id='{rq["aid"]}'")
        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -update-address-area"})
        uidata.append({"_data":"Add new Address","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","value":address["first_name"],"type":"text","required":"true","placeholder":"First name*","name":"first_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["last_name"],"type":"text","required":"true","placeholder":"Last name*","name":"last_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["email"],"type":"text","required":"true","placeholder":"Email*","name":"email","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["phone"],"type":"text","required":"true","placeholder":"Phone*","name":"phone","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["state"],"type":"text","required":"true","placeholder":"State*","name":"state","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["city"],"type":"text","required":"true","placeholder":"City*","name":"city","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address"],"type":"text","required":"true","placeholder":"Street address*","name":"address","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address_2"],"type":"text","placeholder":"Apartment, suits, etc (Optional)","name":"address_2","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["id"],"type":"text","placeholder":"ID","name":"address_id","pclass":"ins-hidden"})
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Update Address <img src='"+p+"style/right_arrow.svg'></img>", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -update-address-btn ins-gold-d ins-col-4","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    def _add_address_ui(self):
        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -add-address-area"})
        uidata.append({"_data":"Add new Address","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"First name*","name":"first_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Last name*","name":"last_name","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Email*","name":"email","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Phone*","name":"phone","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"State*","name":"state","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"City*","name":"city","pclass":"ins-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Street address*","name":"address","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","placeholder":"Apartment, suits, etc (Optional)","name":"address_2","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Add Address <img src='"+p+"style/right_arrow.svg'></img>", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -add-address-btn ins-gold-d ins-col-3","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    def _cart_step(self):
      ## Cart Area
        sedata=self.ins._server._get_session(self.session_name)
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        subtotal = 0
        for k,v in sedata.items():
            subtotal+= float(v["price"]) * float(v["count"])
            uidata+= ELUI(self.ins).counter_pro_block(v)
        uidata.append({"end":"true"})
        ## Items Area
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;height:100%;   border-left: 1px solid var(--primary-l);"})
        total = subtotal 
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details", "class": "ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end  -subtotal-text"})
        uidata.append({"_data": "Shipping", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":str(total), "_view":"currency","_currency_symbol":" EGP","class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end  -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        payment_url = self.ins._server._url({"mode":"delivery"},["id"])
        back_url = self.ins._server._url({"alias":"product"},["id","mode"])
        uidata.append({"href":payment_url,"_type":"a","_data": "Procced to address <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return uidata
    def items_area(self):
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
        uidata.append({"_data": "Voucher", "class": "ins-col-12  ins-grey-d-color ins-strong-m  "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","name":"voucher","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class":"ins-space-xl"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(subtotal),"data-value" : subtotal,"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -subtotal-text"})
        pdata = self.ins._server._get_session(self.session_payment_name)
        pclass = "ins-hidden"
        if pdata and pdata["type"] == "online":
           pclass = ""
           sedata=self.ins._server._get_session(self.session_name)
           for k,v in sedata.items():
             chargs+= (float(v["weight"]) * float(v["count"])) * 20
        total = subtotal + chargs 
        uidata.append({"start": "true", "class": f"-online-payment-fee  ins-col-12 ins-flex {pclass}"})
        uidata.append({"_data": "Online payment fee", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(chargs),"data-value" : chargs,"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -chargs-text"})
        uidata.append({"end": "true"})
        uidata.append({"_data": "Shipping", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        if total > 200000:
          uidata.append({"_data": "Free","data-value" : 0, "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end  -shipping-text"})
        else:
          uidata.append({"_data": "200","data-value" : 200,"_view":"currency","_currency_symbol":" EGP",  "class": "ins-col-6  ins-gold-d-color ins-title-xs ins-strong-l ins-flex-end -shipping-text"})
          total +=200
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(total),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end -total-text"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        payment_url = self.ins._server._url({"mode":"payment"},["id"])
        if "mode" in rq and rq["mode"] == "delivery":
         back_url = self.ins._server._url({"mode":"cart"},["id"])
        else:
         back_url = self.ins._server._url({"mode":"delivery"},["id"])
        if "mode" in rq and rq["mode"] == "payment":
            uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
            asession = self.ins._server._get_session(self.session_address_name)
            if type(asession) == dict and "type" in asession and  asession["type"] == "store":
                stores = [
                   {"id":"1","address":"60 El Moez Le Din Allah St., El Gamalia, Cairo","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"},
                   {"id":"2","address":"Street 88 , Palm Hills , 6th of October, Giza","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"}
                ]
                for s in stores:
                   if s["id"] == asession["id"]:
                      store = s
                ainfo = [
                {"_data": "Pickup Address", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "},
                {"class":"ins-space-s"},
                {"_data": store.get("title",""), "class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
                {"_data": store.get("address",""), "class": "ins-col-12 ins-grey-color"},
                {"_data": f"Mobile: {store.get("phone","")} Email: {store.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
                {"end": "true"},
                {"class":"ins-space-xl"}
                ]
            else:
               address = self.ins._db._get_row("gla_address","*",f"id='{asession["id"]}'")
               ainfo = [
               {"_data": "Shipping Address", "class": "ins-col-8 ins-title-s ins-grey-d-color ins-strong-l "},
               {"_data": "Edit Address","data-aid" : str(address["id"]),"class": "-update-address ins-col-4 ins-flex-end ins-gold-d-color ins-strong-m ins-text-upper ins-button-text"},
               {"class":"ins-space-s"},
               {"_data": address.get("title",""), "class": "ins-col-12  ins-title-20	  ins-grey-d-color ins-strong-l"},
               {"_data": address.get("address",""), "class": "ins-col-12 ins-grey-color"},
               {"_data": f"Mobile: {address.get("phone","")} | Email: {address.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-title-14"},
               {"end": "true"},
               {"class":"ins-space-xl"}
               ]
            uidata+=ainfo
            uidata.append({"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d  ins-text-upper -submit-order-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        else:
          #"href":payment_url,"_type":"a",
          uidata.append({"_data": "Procced to payment <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -proccesd-payment-btn ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-title-xs	","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})
        return uidata
    def _format_currency(self):
          rq = self.ins._server._post()
          r = {}
          if "value" in rq and rq["value"] != "":
              v = [{"_data": rq["value"], "_view": "currency", "_currency_symbol": " EGP"}]
              r["value"] = self.ins._ui._render(v)
          if "total" in rq and rq["total"] != "":
              t = [{"_data": rq["total"], "_view": "currency", "_currency_symbol": " EGP"}]
              r["total"] = self.ins._ui._render(t)
          return r  
    def _prepare_order_data(self):
            sedata = self.ins._server._get_session(self.session_name)
            chargs = 200
            shipping = 200
            subtotal = 0
            for k, v in sedata.items():
                subtotal += float(v["price"]) * float(v["count"]) 
            amount = (chargs + subtotal + shipping) * 100
            return amount
    def _instapay_ui(self, string=False):
      uidata = [
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s"},
         {"_data": "Pay via Instapay and upload your payment receipt for confirmation. Once your payment is complete, simply submit the receipt to finalize your order.", "class": "ins-col-12 ins-title-xs ins-grey-color ins-text-none"},
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s ins-padding-s"},
         {"_data": "Instapay Numbers", "class": "ins-col-12 ins-title-s ins-strong-m ins-grey-d-color"},
         {"end": "true"},
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s ins-padding-s"},
         {"_data": "1234567890", "class": "ins-col-10 ins-title-xs ins-grey-d-color"},
         {"_type": "i", "data-number": "1234567890", "class": "lni lni-file-multiple -copy-number", "style": "cursor: pointer; font-size: 1.2em;"},
         {"end": "true"},
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s ins-padding-s"},
         {"_data": "0987654321", "class": "ins-col-10 ins-title-xs ins-grey-d-color"},
         {"_type": "i", "data-number": "0987654321", "class": "lni lni-file-multiple -copy-number", "style": "cursor: pointer; font-size: 1.2em;"},
         {"end": "true"},
         {"end": "true"},
      ]
      if string:
         return uidata
      return self.ins._ui._render(uidata)
    def _bank_ui(self,string=False):
          bank_details = [
            {"Bank Name": "CIB", "Account Number": "100022388147", "Swift Code": "CIBEEGCX097", "IBAN number": "EG590010009700000100022388147", "Bank Branch": "El Mokattam", "Company Name": "EL GALLA GOLD", "logo": "cib_logo.png"},
            {"Bank Name": "National Bank Of Egypt", "Account Number": "1033071123260201011", "Swift Code": "NBEGEGCX103", "IBAN number": "EG940003010330711232602010110", "Bank Branch": "Al Hamzawy", "Company Name": "EL GALLA GOLD", "logo": "nbe_logo.png"},
            {"Bank Name": "Banque Misr", "Account Number": "1070199000006941", "Swift Code": "BMISEGCXXX", "IBAN number": "EG920002010701070199000006941", "Bank Branch": "Cairo Branch", "Company Name": "EL GALLA GOLD", "logo": "banque_misr_logo.png"},
            {"Bank Name": "Bank Of Alexandria", "Account Number": "103026301001", "Swift Code": "ALEXEGCX003", "IBAN number": "EG21000510030000010302630100", "Bank Branch": "Sherif Branch", "Company Name": "EL GALLA GOLD", "logo": "alex_bank_logo.png"},
            {"Bank Name": "Arab African International Bank", "Account Number": "11066655", "Swift Code": "ARAIEGCXAZH", "IBAN number": "EG85005700200110666551001020", "Bank Branch": "Cairo Branch", "Company Name": "EL GALLA GOLD", "logo": "aaib_logo.png"},
            {"Bank Name": "Abu Dhabi Islamic Bank (ADIB)", "Account Number": "100000545327", "Swift Code": "ABDIEGCAXX", "IBAN number": "EG97003001280000010000054532", "Bank Branch": "Al Darasa", "Company Name": "EL GALLA GOLD", "logo": "adib_logo.png"},
            {"Bank Name": "Emirates NBD", "Account Number": "1019342954301", "Swift Code": "EBILEGCXXXX", "IBAN number": "EG10001400540000101934295430", "Bank Branch": "Al Azhar", "Company Name": "EL GALLA GOLD", "logo": "enbd_logo.png"}
          ]
          uidata = [{"start": "true", "class": "ins-col-12 ins-flex ins-gap-m"}]
          for bank in bank_details:
            uidata.append({"start": "true", "class": "ins-col-12 ins-card ins-padding-s ins-margin-xs"})
            uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-align-center"})
            uidata.append({"_type": "img", "style":"width: 30px;","src": f"{p}images/bank/{bank['logo']}", "class": "ins-logo-xs"})
            uidata.append({"_data": f"{bank['Bank Name']}", "class": "ins-col-10 ins-title-xs ins-strong-m ins-grey-d-color"})
            uidata.append({"end": "true"})
            uidata.append({"_data": f"Account Number: {bank['Account Number']}", "class": "ins-col-12 ins-title-xxs ins-grey-d-color"})
            uidata.append({"_data": f"Swift Code: {bank['Swift Code']}", "class": "ins-col-12 ins-title-xxs ins-grey-d-color"})
            uidata.append({"_data": f"IBAN number: {bank['IBAN number']}", "class": "ins-col-12 ins-title-xxs ins-grey-d-color"})
            uidata.append({"_data": f"Bank Branch: {bank['Bank Branch']}", "class": "ins-col-12 ins-title-xxs ins-grey-d-color"})
            uidata.append({"_data": f"Company Name: {bank['Company Name']}", "class": "ins-col-12 ins-title-xxs ins-grey-d-color"})
            uidata.append({"end": "true"})
          uidata.append({"end": "true"})
          if string:
             return uidata
          return self.ins._ui._render(uidata)
    def _cash_ui(self, string=False):
      uidata = [
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s"},
         {"_data": "Pay with cash upon delivery. Please ensure you have the exact amount ready as our delivery personnel may not have change.", "class": "ins-col-12 ins-title-xs ins-grey-color ins-text-none"},
         {"end": "true"}
      ]
      if string:
         return uidata
      return self.ins._ui._render(uidata)
    def _online_ui(self, string=False):
         online_methods = [
            {"name": "Aman", "logo": "aman_logo.png"},
            {"name": "Contact", "logo": "contact_logo.png"},
            {"name": "Mogo", "logo": "mogo_logo.png"}
         ]
         uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]
         for method in online_methods:
            uidata.append({"start": "true", "class": "ins-col-12 ins-card ins-padding-s ins-margin-xs"})
            uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-align-center"})
            uidata.append({"_type": "img", "style": "width: 30px;", "src": f"{p}images/payment/{method['logo']}", "class": "ins-logo-xs"})
            uidata.append({"_data": f"{method['name']}", "class": "ins-col-10 ins-title-xs ins-strong-m ins-grey-d-color"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
         uidata.append({"end": "true"})
         if string:
            return uidata
         return self.ins._ui._render(uidata)
    def _update_payment_data(self):
         rq = self.ins._server._post()
         pdata = {
          "type":rq["name"]
       }
         self.ins._server._set_session(self.session_payment_name,pdata)
         method_name = f"_{rq['name']}_ui"
         method = getattr(self, method_name)
         return method()
    def _payment_step(self):
        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        uidata.append({"start":"true","class":"ins-col-12 ins-flex"})
        uidata.append({"start":"true","class":"ins-col-12 ins-gap-o"})
        uidata.append({"_data":"payment","class":"ins-col-12 ins-title-m		 ins-strong-m ins-grey-d-color ins-text-upper"})
        uidata.append({"_data":"All transactions are secure and encrypted","class":"ins-col-12 ins-title-xs ins-grey-color"})
        uidata.append({"end":"true"})
        uidata.append({"class":"ins-space-s"})
        pdata = self.ins._server._get_session(self.session_payment_name)
        payments = [
           {"title":"Cash on delivery","name":"cash"},
           {"title":"Online Payment (Aman, Contact, Mogo)","name":"online"},
           {"title":"InstaPay","name":"instapay","img":"style/instapay.svg"},
           {"title":"Bank transfer","name":"bank"},
        ]
        for payment in payments:
            img = "style/radio.svg"
            pclass = ""
            st_data = ""
            if pdata and pdata["type"] == payment["name"]:
               img = "style/radio_checked_b.svg"
               pclass = "ins-active"
               method_name = f"_{pdata["type"]}_ui"
               method = getattr(self, method_name)
               st_data = self.ins._ui._render(method(True))
            pcard = [
                  {"start":"true","class":"ins-col-12 ins-flex ins-gap-o"},
                  {"start":"true","data-name":payment["name"],"class":f"{pclass} ins-col-12 ins-flex-center -payment-type-btn {payment.get("class","")}"},
                  {"_type":"img","src":f"{p}{img}","class":"-payment-type-btn-img"},
                  {"_data": payment["title"],"class":"ins-strong-m ins-grey-m-color payment-title"},
            ]
            pcard.append({"class":"ins-col-grow"})
            if "img" in payment:
              pcard.append({"_type":"img","src":f"{p}{payment['img']}","class":"ins-flex-end"})
            pcard.append({"end":"true"})
            pcard.append({"_data":st_data,"class":f"ins-col-12 -payment-subtype-area -payment-subtype-area-{payment["name"]} {pclass}"})
            pcard.append({"end":"true"})
            uidata+=pcard
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;   border-left: 1px solid var(--primary-l);"})
        uidata+=self.items_area()
        uidata.append({"end":"true"})
        return uidata
    def _placed_step(self):
          uidata = [
          {"start":"true","class":"ins-col-12 gla-container ins-flex-center ins-padding-2xl"},
          {"start":"true","class":"ins-col-8 ins-card ins-flex"},
            {"class":" lni lni-check-circle-1 ins-font-4xl"},
             {"start":"true","class":"ins-col-grow","style":"    padding: 0px;line-height: 15px;"},
            {"_data":"Your order has been placed","class":"ins-title-s ins-strong-m ins-grey-d-color ins-col-12"},
            {"_data":"You will be directed to orders page in <span class='-countdown ins-strong-m'>10 seconds</span>","class":"ins-title-14 ins-grey-color ins-col-12" ,"style":"    text-transform: lowercase;"},
            {"end":"true"},
            {"end":"true"}
         ]
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
                   window.location.href = "/login";
               </script>
               """
              else:
               uidata+=self._addresses_step()
            elif rq["mode"] == "cart":
              uidata+=self._cart_step()
            elif rq["mode"] == "payment":
               uidata+=self._payment_step()
            elif rq["mode"] == "order":
               uidata+=self._placed_step()
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    def no_data(self):
        uidata=[
              {"start":"true","class":"ins-col-12  ins-flex-center","style":"position: relative;top: 20px;"},
              {"_data":"There is no items in cart yet","class":"ins-col-8 ins-card ins-padding-2xl ins-text-center"},
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
         if not payment:
            return "-1"
         subtotal =0 
         for k,v in sedata.items():
            subtotal+= (float(v["price"]) * float(v["count"]))
         chargs = 0
         if payment["type"] == "online":
            for k,v in sedata.items():
               chargs+= (float(v["weight"]) * float(v["count"])) * 20
         total = subtotal + chargs
         order = {
            "fk_user_id":sdata["id"],
            "fk_address_id":address["id"],
            "delivery_type":address["type"],
            "payment_method":payment["type"],
            "total":total,
            "payment_status":"pending",
            "order_status":"pending"
         }
         oid = self.ins._db._insert("gla_order",order)
         payment_url = ""
         if payment["type"] == "online":
            paymob = PaymobAPI()
            payment_url = paymob.create_pay_wdgt(total, oid, 4919279 )
         for k,v in sedata.items():
            order_item = {
               "fk_order_id":oid,
               "fk_product_id":v["id"],
               "quantity":v["count"],
               "price":v["price"],
               "chargs":chargs
            }
            self.ins._db._insert("gla_order_item",order_item)
         if payment_url:
            return payment_url
         return "1"
    

    def payment_callback(self):
       data = self.ins._server._req()
       order_id = data.get("merchant_order_id")
       payment_status = data.get("payment_status")
       if payment_status == "success":
           self.update_payment_status(order_id, "paid")
           return f'<script>window.location.href = "/order_success/{order_id}";</script>'
       else:
           return f'<script>window.location.href = "/order_failed/{order_id}";</script>'
       


    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        rq = self.ins._server._get()
        if self.ins._server._get_session(self.session_name):
           if "mode" in rq and rq["mode"] == "payment_check":
              return self.payment_callback()
           return self._ui()
        else:
            return self.no_data()
