from flask import redirect
from ins_gla.ins_apps.app_users.app_users_orders import AppUsersOrders
from ins_gla.ins_apps.app_users.app_users_profile import AppUsersProfile
from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI
p = "/ins_web/ins_uploads/"


class AppUsers(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)
    
    @property
    def session_address_name(sel):
        return "glaaddress"


    def u(self, mode):
        return self.ins._server._url({"mode": mode},"id")

    def header(self, g):
        hc = ""
        pc = ""
        oc = ""
        sc = ""
        if g.get("mode") == "profile":
            pc = " ins-gold-bg "
        elif g.get("mode") == "addresses":
            sc = " ins-gold-bg "
        elif g.get("mode") == "order":
            oc = " ins-gold-bg "
        else:
            hc = " ins-gold-bg "
        ui = [{"start": "true", "class": "ins-col-7 ins-flex-end"},
              {"_data": "<i class='lni ins-font-l lni-home-2'></i>Home",
                  "class": f"ins-button-s  ins-text-upper {hc}  ins-flex", "_type": "a", "href": self.u("")},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-user-4'></i>Profile Management",
                  "class": f"ins-button-s ins-text-upper {pc}  ins-flex", "_type": "a", "href": self.u("profile")+"/user_setting"},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-basket-shopping-3'></i>My Orders",
                  "class": f"ins-button-s  ins-text-upper {oc} ins-flex ", "_type": "a", "href": self.u("order")},
              {"_data": "|", "class": "  "},
              {"_data": "<i class='lni ins-font-l lni-buildings-1'></i>My Addresses",
                  "class": f"ins-button-s ins-text-upper   {sc} ins-flex ", "_type": "a", "href": self.u("addresses")},
              {"end": "true"}
              ]
        return ELUI(self.ins).page_title("Users Panel", [{"_data": "Users Panel / ", "href": "/puser"}, {"_data": "Profile"}], ui)

    def orders(self, g): 
        return AppUsersOrders(self.app).out(self.ins)

    def profile(self, g): 
        return AppUsersProfile(self.app).out(self.ins)

    def home(self, g):
        usmenu = [
            {"start": "true", "class": "  ins-col-12  ins-flex   ins-padding-2xl"},
          
          
          


            {"start": "true", "class": "  ins-col-4 ins-primary-w  ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"profile/user_setting", "_data": f'<i class="lni ins-font-l lni-user-4"></i>  Profile Management ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Update your name, email, and password to keep your account secure.',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},


            {"start": "true", "class": "  ins-col-4    ins-primary-w ins-white ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"order", "_data": f'<i class="lni ins-font-l lni-basket-shopping-3"></i>  My Orders ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Access detailed information about your current and past orders, including status and history.',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},



            {"start": "true", "class": "  ins-col-4  ins-primary-w ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a","href":"addresses",  "_data": f'<i class="lni ins-font-l  lni-buildings-1"></i> My Addresses ',
                "class": " ins-title-s ins-col-12"},
            {"_data": f'Add, edit, or remove saved addresses to simplify and speed up future purchases.',
                "class": "ins-col-12 ins-padding-xl   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},
            {"end": "true"}
        ]
       
        uidata = [
            {"start": "true", "class": "ins-col-12  "},
            {"start": "true", "class": "gla-container ins-flex-start "},
        ]
        uidata .append({"start": "true", "class": "ins-flex ins-col-12 "})
        uidata += usmenu
        uidata .append({"end": "true"})
        uidata .append({"end": "true"})
        uidata .append({"end": "true"})
        return self.ins._ui._render(uidata)
    
    def _addresses_area_ui(self,string=True):
        rsdata=  self.user._check()
        
        addesses = self.ins._db._get_data("gla_address","*",f"fk_user_id = '{rsdata["id"]}' order by kit_created ASC")

        uidata=[{"_data":"My Address","class":"ins-col-9 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"}]
        uidata.append({"_data": "Add Address", "class": "ins-button-s -add-address ins-text-center ins-strong-m ins-col-3 ins-gold-bg  ins-text-upper"})
        asession = self.ins._server._get_session(self.session_address_name)

        if type(asession) != dict:
           asession = {"type":"delivery","id":"-1"}

        if addesses:
            for a in addesses:
               uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
               uidata.append({"start":"true","class":"ins-col-10 ins-flex"})
               uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
               uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
               uidata.append({"_data": "Mobile: "+a["phone"] + " | Email: "+ a["email"],"class":"ins-grey-d-color ins-col-12  ins-title-14"})
               uidata.append({"end":"true"})
               uidata.append({"start":"true","class":"ins-col-2 ins-flex-end"})
               uidata.append({"_data":"<i class='-update-address  _a lni lni-pencil-1' data-aid = "+ str(a["id"])+" ></i>","class":"ins-text-center"})
               uidata.append({"_data":"<i class='lni lni-trash-3 _a_red'></i>","data-aid":a["id"],"class":"ins-text-center -remove-address-btn"})
               uidata.append({"end":"true"})

               uidata.append({"end":"true"})

        else:
           uidata.append({"start":"true","class":"ins-col-12 ins-padding-m ins-flex-center"})
           uidata.append({"start":"true","class":"ins-col-8  ins-card ins-flex-center"})
           uidata.append({"_data":"No saved addresses yet"})
           uidata.append({"end":"true"})
           uidata.append({"end":"true"})


        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
  
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
        uidata.append({"class":"ins-col-grow"})
        uidata.append({"_data": "Update Address <img src='"+p+"style/right_arrow.svg'></img>", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -update-address-btn ins-gold-d ins-col-2","style":"height: 46px;    border: 1px solid var(--primary-d);"})
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
        uidata.append({"class":"ins-col-grow"})
        uidata.append({"_data": "Add Address <img src='"+p+"style/right_arrow.svg'></img>", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper  -add-address-btn ins-gold-d ins-col-2","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)

    

    def addresses(self, g,udata):


        uidata=[{"start":"true","class":"ins-col-12 ins-flex   gla-container"}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 "})
        uidata.append({"start":"true","class":"  ins-col-12 ins-gap-20  ins-flex -addresses-area   ins-padding-2xl"})
        uidata+= self._addresses_area_ui(False)
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})


        return self.ins._ui._render(uidata)

    def _mobile_no_ui(self):
       
        uidata=[
           {"start":"true","class":"ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
           {"start":"true","class":"ins-col-4 ins-flex-end ins-card -mobile-form  ins-text-start"},
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
           {"start":"true","class":"ins-col-4 ins-flex-center ins-card -otp-form  ins-text-start"},
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
   

    def _logout(self):
        self.user._logout()
        return "1"

    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")
       
        udata = self.user._check()
        if not udata:
            self.ins._server._set_session("redirect", "/puser")
            return """
            <script>
                window.location.href = "/login";
            </script>
            """
            

        g = self.ins._server._get()
        r = self.header(g)
        if g.get("mode") == "profile":
            r += self.profile(g)
        elif g.get("mode") == "addresses":
            r += self.addresses(g,udata)
        elif g.get("mode") == "order":
            r += self.orders(g)
        else:
            r += self.home(g)
        return r
