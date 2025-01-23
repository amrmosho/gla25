from ins_gla.ins_kit._elui import ELUI
from ins_gla.ins_kit._gusers import Gusers
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
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-gold ins-text-upper ins-text-center ins-font-s","style":"padding: 7px;margin-top: 30px;"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)


        return r




    def _login(self):
        

        r=  self.user._loign()

        if r :
           return "1"
        else:
           return "-1"
        



    def _login_ui(self):
       
        uidata=[
           {"start":"true","class":"ins-col-12 ins-flex-center ins-padding-2xl ins-text-center"},
           {"start":"true","class":"ins-col-5 ins-flex-end ins-card -login-form  ins-text-start"},
           {"_type":"input","title":"email","placeholder":"Enter your Email","type":"email","name":"email","pclass":"ins-col-12"},
           {"_type":"input","title":"password","type":"password","placeholder":"Enter your Password","name":"password","pclass":"ins-col-12"},
           {"_data":"Forgot Password?","class":"ins-col-12 ins-strong-m ins-font-s ins-grey-color"},
           
           {"class":"ins-line ins-col-12"},
           {"_data":"Login","class":"ins-button ins-primary ins-col-3 -guser-login-btn"},
           
            {"end":"true"}
            ,{"end":"true"}
           ]


        return uidata


    def header_ui(self):
        rq = self.ins._server._req()

        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
      
      
        home_url = self.ins._server._url({},["mode","id","alias"])
        products_url = self.ins._server._url({"alias":"product"},["mode","id"])
        product_url = self.ins._server._url({"alias":"product","mode":"product","id":1})
       
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","class":" ins-font-s	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":products_url,"_data": "Product /","class":" ins-font-s	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":product_url,"_data": "250gm Gold Bar /","class":" ins-font-s	ins-grey-d-color ins-strong-m"},
            {"_data": "Checkout","class":" ins-font-s	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]

        uidata+=path

        if rq["mode"] == "cart":
           uidata.append({"_data":"My Cart","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        elif rq["mode"] == "delivery":
            uidata.append({"_data":"Shipping Address","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        else:
           uidata.append({"_data":"Payment Information","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})

       
        steps = [
            {"text":"My Cart",
             "img":"ecart.svg",
             "mode":"cart"
             },
               {"text":"Delivery",
             "img":"truck.svg",
             "mode":"delivery"
             },
               {"text":"Payment",
             "img":"money.svg",
             "mode":"payment"
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
         uidata.append({"_data": "<img src='"+p +"style/"+ s["img"]+"'></img>"+f"{i}"+". "+s["text"], "class": f"ins-button-s  ins-flex {active}"})
         sp="lni lni-chevron-left ins-font-l"
       
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        return uidata





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

        
        for a in addesses:
           img = "style/radio.svg"

           if str(a["id"]) == str(asession["id"]) and asession["type"] == "delivery":
              img = "style/radio_checked.svg"
           uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
           uidata.append({"_data":"<img data-aid = "+f"{a["id"]}"+" class='-address-btn' data-type='delivery' src='"+p + img+"'></img>","class":"ins-flex ins-col-1"})
           uidata.append({"start":"true","class":"ins-col-9 ins-flex"})
           uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
           uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-font-s","style":"line-height: 16px;"})
           uidata.append({"_data": "Mobile: "+a["phone"] + " | Email: "+ a["email"],"class":"ins-grey-d-color ins-col-12","style":"    font-size: 14px;"})
           uidata.append({"end":"true"})
           uidata.append({"start":"true","class":"ins-col-2 ins-flex-end"})
           uidata.append({"_data":"<img src='"+p + "style/pen.svg"+"'></img>","class":"ins-text-center"})
           uidata.append({"_data":"<img src='"+p + "style/trash.svg"+"'></img>","data-aid":a["id"],"class":"ins-text-center -remove-address-btn"})
           uidata.append({"end":"true"})

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
           uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-font-s","style":"line-height: 16px;"})
           uidata.append({"_data": f"Phone: {a["phone"]} | WhatsApp: {a["whatsapp"]} | Email:  {a["email"]}" ,"class":"ins-grey-d-color ins-col-12","style":"    font-size: 14px;"})
           uidata.append({"end":"true"})


           uidata.append({"end":"true"})


        uidata.append({"end":"true"})

        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
  


    def _upate_address_ui(self):
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
       self.ins._db._insert("gla_address",data)
       return self._addresses_area_ui()

   
    def _cart_step(self):
       
      ## Cart Area
        sedata=self.ins._server._get_session(self.session_name)

        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        subtotal = 0
        chargs = 3000
        for k,v in sedata.items():
            subtotal+= v["price"]
            uidata+= ELUI(self.ins).counter_pro_block(v)
        uidata.append({"end":"true"})

        total = subtotal + chargs



        ## Items Area
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;height:100%;   border-left: 1px solid var(--primary-l);"})
    

       
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details", "class": "ins-col-12  ins-grey-d-color ins-font-l ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "EGP "+str(subtotal), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Making Charge", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "EGP "+str(chargs), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Shipping", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "Free", "class": "ins-col-6  ins-gold-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data":"EGP "+str(total), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})

        payment_url = self.ins._server._url({"mode":"delivery"},["id"])
        back_url = self.ins._server._url({"alias":"product"},["id","mode"])
        uidata.append({"href":payment_url,"_type":"a","_data": "Procced to address <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-font-m ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-font-m	","style":"    height: 46px;"})
        uidata.append({"end":"true"})



                  
         

           

        return uidata


    def items_area(self):
       
        ## Items Area
        uidata = []
        sedata=self.ins._server._get_session(self.session_name)
        rq = self.ins._server._req()
        subtotal = 0
        chargs = 3000

        for k,v in sedata.items():
            subtotal+= v["price"]
            uidata+= ELUI(self.ins).small_pro_block(v)
            uidata.append({"class":"ins-space-m"})

    
        total = subtotal + chargs

        

        uidata.append({"class":"ins-space-m"})

        uidata.append({"class":"ins-line ins-col-12"})
        
        uidata.append({"class":"ins-space-m"})

        uidata.append({"_data": "Voucher", "class": "ins-col-12  ins-grey-d-color ins-strong-m  "})
        uidata.append({"_type": "input","type":"text","placeholder":"code","name":"voucher","pclass":"ins-col-12","style":"    background: white;border-radius:4px;"})
        
        uidata.append({"class":"ins-space-xl"})

        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
        uidata.append({"_data": "Your details", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "})
        uidata.append({"class":"ins-space-s"})
        uidata.append({"_data": "Subtotal", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "EGP "+ str(subtotal), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Making Charge", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "EGP "+ str(chargs), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Shipping", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "Free", "class": "ins-col-6  ins-gold-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-font-m  ins-grey-color ins-strong-m"})
        uidata.append({"_data": "EGP "+ str(total), "class": "ins-col-6  ins-grey-d-color ins-font-m ins-strong-l ins-flex-end"})
        uidata.append({"end": "true"})
        uidata.append({"class":"ins-space-xl"})
        payment_url = self.ins._server._url({"mode":"payment"},["id"])
        if "mode" in rq and rq["mode"] == "delivery":
         back_url = self.ins._server._url({"mode":"cart"},["id"])
        else:
         back_url = self.ins._server._url({"mode":"delivery"},["id"])

        if "mode" in rq and rq["mode"] == "payment":
            s = self.ins._server._get_session(self.session_address_name)
            uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-padding-m","style":"border-radius:8px !important;border: 1px solid var(--grey-l);"})
           

            address = self.ins._db._get_row("gla_address","*",f"id='{s["id"]}'")
            ainfo = [{"_data": "Shipping Address", "class": "ins-col-8 ins-title-s ins-grey-d-color ins-strong-l "},
            {"_data": "Edit Address", "class": "ins-col-4 ins-flex-end ins-gold-d-color ins-strong-m ins-text-upper ins-button-text"},
            {"class":"ins-space-s"},
            {"_data": address.get("title",""), "class": "ins-col-12  ins-font-l  ins-grey-d-color ins-strong-l"},
            {"_data": address.get("address",""), "class": "ins-col-12 ins-grey-color"},
            {"_data": f"Mobile: {address.get("phone","")} Email: {address.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ","style":"font-size:14px"},
            {"end": "true"},
            {"class":"ins-space-xl"},
            {"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-font-m ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"}
            ]

            asession = self.ins._server._get_session(self.session_address_name)
            if type(asession) == dict and "type" in asession and  asession["type"] == "store":
                stores = [
                   {"id":"1","address":"60 El Moez Le Din Allah St., El Gamalia, Cairo","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"},
                   {"id":"2","address":"Street 88 , Palm Hills , 6th of October, Giza","title":"EL-GALLA Store","whatsapp":"01009539999","phone":"17153","email":"info@elgallagold.com"}
                ]
                for s in stores:
                   if s["id"] == asession["id"]:
                      store = s
                ainfo = [{"_data": "Pickup Address", "class": "ins-col-12 ins-title-s ins-grey-d-color ins-strong-l "},
                {"class":"ins-space-s"},
                {"_data": store.get("title",""), "class": "ins-col-12  ins-font-l  ins-grey-d-color ins-strong-l"},
                {"_data": store.get("address",""), "class": "ins-col-12 ins-grey-color"},
                {"_data": f"Mobile: {store.get("phone","")} Email: {store.get("email","")}", "class": "ins-col-12 ins-grey-d-color ins-strong-m ","style":"font-size:14px"},
                {"end": "true"},
                {"class":"ins-space-xl"},
                {"_data": "Place Order <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-font-m ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"}
                ]

            uidata+=ainfo



        else:
          uidata.append({"href":payment_url,"_type":"a","_data": "Procced to payment <img src='"+p+"style/right_arrow.svg'></img>","class": "ins-button-s ins-flex-center ins-font-m ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn ins-text-upper","style":"    height: 46px;    border: 1px solid var(--primary-d);"})



        uidata.append({"href":back_url,"_type":"a","_data": " <img src='"+p+"style/left_arrow.svg'></img> Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   ins-col-12 ins-font-m	","style":"    height: 46px;"})
        uidata.append({"_data": "Your info will be saved to a Shop account. By continuing, you agree to Shop’s <a>Terms of Service</a> and acknowledge the  <a>Privacy Policy</a>.", "class": " ins-col-12 ins-grey-color ","style":"line-height:24px"})

        return uidata

    def _payment_step(self):
       

        uidata=[{"start":"true","class":"ins-col-7 ins-flex ins-padding-2xl"}]
        uidata.append({"start":"true","class":"ins-col-12 ins-flex"})

        uidata.append({"start":"true","class":"ins-col-12 ins-gap-o"})
        uidata.append({"_data":"payment","class":"ins-col-12 ins-font-l	 ins-strong-m ins-grey-d-color ins-text-upper"})
        uidata.append({"_data":"All transactions are secure and encrypted","class":"ins-col-12 ins-font-m ins-grey-color"})
        uidata.append({"end":"true"})

       
        uidata.append({"class":"ins-space-s"})


        uidata.append({"_data": "<img src='"+p + "style/radio.svg"+"'></img>"+"Cash on delivery", "class": "  ins-col-12   ins-flex ins-grey-m-color -payment-type-btn payment-card ins-strong-m"})
        uidata.append({"_data": "<img src='"+p + "style/radio.svg"+"'></img>"+"Pay Via card", "class": "  ins-col-12   ins-flex ins-grey-m-color -payment-type-btn payment-card ins-strong-m"})
        uidata.append({"_data": "<img src='"+p + "style/radio.svg"+"'></img>"+"InstaPay", "class": "  ins-col-12   ins-flex ins-grey-m-color -payment-type-btn payment-card ins-strong-m"})
        uidata.append({"_data": "<img src='"+p + "style/radio.svg"+"'></img>"+"Bank transfer", "class": "  ins-col-12   ins-flex ins-grey-m-color -payment-type-btn payment-card ins-strong-m"})

        
        
        
        uidata.append({"end":"true"})


        uidata.append({"end":"true"})
        uidata.append({"start":"true","class":"ins-col-5 ins-gap-o ins-flex   ins-padding-2xl","style":"background:white;   border-left: 1px solid var(--primary-l);"})
        uidata+=self.items_area()
        uidata.append({"end":"true"})




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
               uidata+=self._login_ui()
              else:
               uidata+=self._addresses_step()
          
            elif rq["mode"] == "cart":
              uidata+=self._cart_step()
            elif rq["mode"] == "payment":
               uidata+=self._payment_step()
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)
    
    def no_data(self):
        uidata=[
              {"start":"true","class":"ins-col-12  ins-flex-center","style":"position: relative;top: 20px;"},
              {"_data":"There is no items in cart yet","class":"ins-col-8 ins-card ins-padding-2xl ins-text-center"},
              {"end":"true"}
              ]
        return self.ins._ui._render(uidata)

    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        


        if self.ins._server._get_session(self.session_name):
           return self._ui()
        else:
           
            return self.no_data()


    
        