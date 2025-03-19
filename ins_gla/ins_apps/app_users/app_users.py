from random import randint
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
        return self.ins._server._url({"mode": mode},["id","lang"])



    def _upload_image(self):
        g = self.ins._server._req()
        if "id" in g:
            self.ins._db._update("gla_order", {"document": g["path"]}, f"id='{g['oid']}'")
        return "1"
    

    def _remove_image(self):
        g = self.ins._server._req()
        if "id" in g:
            self.ins._db._update("gla_order", {"document": ""}, f"id='{g['oid']}'")
        return "1"



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
        ui = [{"start": "true", "class": "ins-col-7 ins-flex-end ins-m-col-12 ins-m-flex-center"},
              {"_data": "<i class='lni ins-font-l lni-home-2'></i>Home","_data-ar":"الرئيسية","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {hc}  ins-flex", "_type": "a", "href": self.u("")},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-user-4'></i>Profile Management","_data-ar":"إدارة الملف الشخصي","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {pc}  ins-flex", "_type": "a", "href": self.u("profile")+"/user_setting"},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-basket-shopping-3'></i>My Orders","_data-ar":"طلبياتي","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {oc} ins-flex ", "_type": "a", "href": self.u("order")},
              {"_data": "|", "class": "  "},
              {"_data": "<i class='lni ins-font-l lni-buildings-1'></i>My Addresses","_data-ar":"عناويني","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper   {sc} ins-flex ", "_type": "a", "href": self.u("addresses")},
              {"end": "true"}
              ]
        return ELUI(self.ins).page_title("My Profile","ملفي الشخصي", [{"_data": "My Profile / ", "href": "/puser","_data-ar":"ملفي الشخصي /","_trans":"true",}, {"_data": "Profile","_data-ar":"الملف الشخصي","_trans":"true",}], ui)

    def orders(self, g): 
        return AppUsersOrders(self.app).out(self.ins)

    def profile(self, g): 
        return AppUsersProfile(self.app).out(self.ins)


    def _update_user_name(self):
        rq = self.ins._server._req()
        udata = self.user._check()
        data = {
            "first_name":rq["fname"],
            "last_name":rq["lname"],
            "title":f"{rq['fname']} {rq['lname']}",
            "user_name":f"{rq['fname']} {rq['lname']}"
        }
        r = {}
                
        r["status"] = "-1"
        r["msg"] = "There is an error while updating user data"

        if udata:
            self.ins._db._update("kit_user",data,f"id='{udata['id']}'")
            r["status"] = "1"
            r["msg"] = "User data updated successfully"
            return r
        return r
            



    def _update_password(self):
        rq = self.ins._server._req()



        u = self.user._check()
        udata = self.ins._db._get_row("kit_user","id,password",f"id='{u['id']}'")
        old_password = self.ins._data.hash_password(rq["old_password"])
        r = {}

        if old_password != udata["password"]:
          r["status"] = "-1"
          
          r["msg"] = "Old password is not conrect"
          if self.ins._langs._this_get()["name"] == "ar":
           r["msg"] = "كلمة المرور القديمة خاطئة"
        
          return r

       
       
        rq["password"] = self.ins._data.hash_password(rq["password"])
        data = {
          "password":rq["password"],
        }
        
        r["status"] = "-1"
        r["msg"] = "There is an error while updating password"

        if udata:
            self.ins._db._update("kit_user",data,f"id='{udata['id']}'")
            r["status"] = "1"
            r["msg"] = "Password updated successfully"
            return r
        return r
            
    def _send_email_otp(self):
        rq = self.ins._server._req()
        udata = self.user._check()
        otp = self.user._create_otp()
        if otp:
            self.ins._db._update("kit_user",{"otp":otp},f"id='{udata['id']}'")
            self.ins._server._set_session("temp_mail",{"email":rq["email"]})
        return "1"
    



    def _check_email(self):
     rq = self.ins._server._req()
     u = self.user._check()
     udata = self.ins._db._get_row("kit_user","email_status,email",f"id='{u['id']}'")

     if rq["email"] != udata["email"] or udata["email_status"] != "verified":
         return self.ins._ui._render( [{"_data": "Send Verification Code","_data-ar":"ارسال رمز التحقق","_trans":"true", "class": "ins-button-m ins-strong-m  -verified-area  ins-gold-bg  ins-col-12 -send-email-veri-btn ins-flex-center", "style": " margin-top: 35px;"}])

     return  self.ins._ui._render( [{"_data": "Verified Email <i class='lni lni-check ins-font-l'></i>","_data-ar":"تم التحقق  <i class='lni lni-check ins-font-l'></i> ","_trans":"true", "class": " ins-strong-m   ins-col-12 -verified-area ins-flex-center ins-border ins-radius-m", "style": " margin-top: 35px;min-height:40px"}])

     


    def _update_email(self):
        rq = self.ins._server._req()
        udata = self.user._check()
        data = self.ins._db._get_row("kit_user","*",f"id='{udata['id']}'")
        r = {}
        if data["otp"]:
             if data["otp"] == rq["otp"]:
                update_data = {
                    "email":self.ins._server._get_session("temp_mail")["email"],
                    "email_status":"verified",
                    "otp":""
                }
                self.ins._db._update("kit_user",update_data,f"id='{udata['id']}'")
                self.ins._server._del_session("temp_mail")
                r["status"] = "1"
                r["msg"] = "Your email has been successfully verified."
                r["ui"] = self.ins._ui._render( [{"_data": "Verified Email <i class='lni lni-check ins-font-l'></i>","_data-ar":"تم التحقق  <i class='lni lni-check ins-font-l'></i> ","_trans":"true", "class": " ins-strong-m   ins-col-12 -verified-area ins-flex-center ins-border ins-radius-m", "style": " margin-top: 35px;min-height:40px"}])
                if self.ins._langs._this_get()["name"] == "ar":
                 r["msg"] = "لقد تم التحقق بنجاح"


            
             else:
                r["status"] = "-1"
                r["msg"] = "The verification code you entered is invalid. Please try again."
                if self.ins._langs._this_get()["name"] == "ar":
                 r["msg"] = "كود تحقق غير صحيح"

        else:
            r["status"] = "-2"
            r["msg"] = "It seems the verification code wasn't sent successfully. Please try again."
            if self.ins._langs._this_get()["name"] == "ar":
                 r["msg"] = "لم يتم ارسال كود التحقق بنجاح. برجاء اعادة المحاولة"
        
        return r


 










    def home(self, g):
        if self.ins._langs._this_get()["name"] == "ar":
            title_profile = f'<i class="lni ins-font-l lni-user-4 ins-m-col-1 -user-pages-icon"></i>  إدارة الملف الشخصي '
            title_order = f'<i class="lni ins-font-l lni-basket-shopping-3 ins-m-col-1 -user-pages-icon"></i>  طلبياتي '
            title_adress = f'<i class="lni ins-font-l  lni-buildings-1 ins-m-col-1 -user-pages-icon"></i> عناويني '

        if self.ins._langs._this_get()["name"] == "en":
             title_profile = f'<i class="lni ins-font-l lni-user-4 ins-m-col-1 -user-pages-icon"></i>  Profile Management '
             title_order = f'<i class="lni ins-font-l lni-basket-shopping-3 ins-m-col-1 -user-pages-icon"></i>  My Orders '
             title_adress = f'<i class="lni ins-font-l  lni-buildings-1 ins-m-col-1 -user-pages-icon"></i> My Addresses '
             
        usmenu = [
            
            {"start": "true", "class": "  ins-col-12  ins-flex   ins-padding-2xl"},

            {"start": "true", "class": "  ins-col-4 ins-primary-w  ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"/puser/profile/user_setting", "_data": title_profile,
                "class": " ins-title-s ins-col-12"},
                {"class":" not-for-web","style":"    width: 24px;"},
            {"_data": f'Update your name, email, and password to keep your account secure.',"_data-ar":"قم بتحديث اسمك والبريد الإلكتروني وكلمة المرور للحفاظ على حسابك آمنًا.","_trans":"true",
                "class": "ins-col-12 ins-padding-xl  ins-m-col-11  ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},


            {"start": "true", "class": "  ins-col-4    ins-primary-w ins-white ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"/puser/order", "_data": title_order,
                "class": " ins-title-s ins-col-12"},
                           {"class":" not-for-web","style":"    width: 24px;"},

            {"_data": f'Access detailed information about your current and past orders, including status and history.',"_data-ar":"احصل على معلومات مفصلة حول طلباتك الحالية والسابقة، بما في ذلك الحالة والتاريخ.","_trans":"true",
                "class": "ins-col-12 ins-padding-xl  ins-m-col-11   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},



            {"start": "true", "class": "  ins-col-4  ins-primary-w ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a","href":"/puser/addresses",  "_data": title_adress,
                "class": " ins-title-s ins-col-12"},
                            {"class":" not-for-web","style":"    width: 24px;"},

            {"_data": f'Add, edit, or remove saved addresses to simplify and speed up future purchases.',"_data-ar":"قم بإضافة أو تعديل أو إزالة العناوين المحفوظة لتبسيط وتسريع عمليات الشراء المستقبلية.","_trans":"true",
                "class": "ins-col-12 ins-padding-xl  ins-m-col-11   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
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
        
        addesses = self.ins._db._get_data("gla_user_address","*",f"fk_user_id = '{rsdata['id']}' order by kit_created ASC")

        uidata=[{"_data":"My Address","_data-ar":"إضافة عنوان","_trans":"true","class":"ins-col-9 ins-m-col-6 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"}]
        uidata.append({"_data": "Add Address","_data-ar":"إضافة عنوان","_trans":"true", "class": "ins-button-s  ins-m-col-6 -add-address ins-text-center ins-strong-m ins-col-3 ins-gold-bg  ins-text-upper"})
        asession = self.ins._server._get_session(self.session_address_name)

        if type(asession) != dict:
           asession = {"type":"delivery","id":"-1"}

        if addesses:
            for a in addesses:
               uidata.append({"start":"true","class":"ins-col-12 ins-card ins-flex-valign-center ins-padding-s -address-cont","style":"    line-height: 20px;"})
               uidata.append({"start":"true","class":"ins-col-10 ins-flex ins-m-col-10"})
               uidata.append({"_data": a["title"],"class":" ins-title-s ins-strong-m ins-grey-d-color ins-col-12","style":"line-height: 24px;"})
               uidata.append({"_data": a["address"],"class":"ins-grey-color ins-col-12 ins-title-12","style":"line-height: 16px;"})
               uidata.append({"_data": "Mobile: "+a["phone"] + " | Email: "+ a["email"],"_data-ar": "الهاتف: "+a["phone"] + " | البريد الالكتروني: "+ a["email"],"_trans":"true","class":"ins-grey-d-color ins-col-12  ins-title-14 -address-info"})
               uidata.append({"end":"true"})
               uidata.append({"start":"true","class":"ins-col-2  ins-m-col-2 ins-flex-end"})
               uidata.append({"_data":"<i class='-update-address  _a lni lni-pencil-1' data-aid = "+ str(a["id"])+" ></i>","class":"ins-text-center"})
               uidata.append({"_data":"<i class='lni lni-trash-3 _a_red'></i>","data-aid":a["id"],"class":"ins-text-center -remove-address-btn"})
               uidata.append({"end":"true"})

               uidata.append({"end":"true"})

        else:
           uidata.append({"start":"true","class":"ins-col-12 ins-padding-m ins-flex-center"})
           uidata.append({"start":"true","class":"ins-col-8  ins-card ins-flex-center"})
           uidata.append({"_data":"No saved addresses yet","_data-ar":"لا يوجد عناوين محفوظة","_trans":"true"})
           uidata.append({"end":"true"})
           uidata.append({"end":"true"})


        if string == False:
            return uidata
        else:
            return self.ins._ui._render( uidata)
  
    def _remove_address(self):
      data = self.ins._server._post()
      self.ins._db._update("gla_user_address",{"kit_deleted":"1"},f"id='{data['aid']}'")

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
       self.ins._db._update("gla_user_address",data,f"id='{data['address_id']}'")
       adta = {
          "type":"delivery","id":data["address_id"]
       }
       self.ins._server._set_session(self.session_address_name,adta)
       return self._addresses_area_ui()
    
    def _update_address_ui(self):
        rq = self.ins._server._post()
        address = self.ins._db._get_row("gla_user_address","*",f"id='{rq['aid']}'")
        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -update-address-area"})
        uidata.append({"_data":"Update Address","_data-ar":"تعديل العنوان","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","value":address["first_name"],"type":"text","required":"true","placeholder":"First name*","placeholder-ar":"الاسم الأول*","_trans":"true","name":"first_name","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["last_name"],"type":"text","required":"true","placeholder":"Last name*","placeholder-ar":"اسم العائلة*","_trans":"true","name":"last_name","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["email"],"type":"text","required":"true","placeholder":"Email*","placeholder-ar":"بريد إلكتروني*","_trans":"true","name":"email","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["phone"],"type":"text","required":"true","placeholder":"Phone*","placeholder-ar":"هاتف*","_trans":"true","name":"phone","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["state"],"type":"text","required":"true","placeholder":"State*","placeholder-ar":"ولاية*","_trans":"true","name":"state","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["city"],"type":"text","required":"true","placeholder":"City*","placeholder-ar":"مدينة*","_trans":"true","name":"city","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address"],"type":"text","required":"true","placeholder":"Street address*","placeholder-ar":"عنوان الشارع*","_trans":"true","name":"address","pclass":"ins-col-12 ins-m-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["address_2"],"type":"text","placeholder":"Apartment, suits, etc (Optional)","placeholder-ar":"شقة، جناح، الخ (اختياري)","_trans":"true","name":"address_2","pclass":"ins-col-12 ins-m-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","value":address["id"],"type":"text","placeholder":"ID","name":"address_id","pclass":"ins-hidden"})
        uidata.append({"end":"true"})

        uidata.append({"class":"ins-space-s"})
        uidata.append({"class":"ins-col-grow"})
        uidata.append({"_data": "Update Address <img src='"+p+"style/right_arrow.svg'></img>","_data-ar":" تحديث العنوان","_trans":"true", "class": "ins-button-s ins-strong-m ins-flex-center  ins-m-col-6 ins-text-upper  -update-address-btn ins-gold-d ins-col-2","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back","_data-ar":" رجوع","_trans":"true", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn ins-m-col-6  ins-col-2 ","style":"    height: 46px;"})
        uidata.append({"end":"true"})
        return self.ins._ui._render(uidata)

    def _add_address_ui(self):

        uidata = [{"start":"true","class":"ins-flex ins-col-12 "}]
        uidata.append({"start":"true","class":"ins-flex ins-col-12 -add-address-area"})
        uidata.append({"_data":"Add new Address","_data-ar":"إضافة عنوان جديد","_trans":"true","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"First name*","placeholder-ar":"الاسم الأول*","_trans":"true","name":"first_name","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Last name*","placeholder-ar":"اسم العائلة*","_trans":"true","name":"last_name","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Email*","placeholder-ar":"بريد إلكتروني*","_trans":"true","name":"email","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Phone*","placeholder-ar":"هاتف*","_trans":"true","name":"phone","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"State*","placeholder-ar":"ولاية*","_trans":"true","name":"state","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"City*","placeholder-ar":"مدينة*","_trans":"true","name":"city","pclass":"ins-col-6 ins-m-col-6","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","required":"true","placeholder":"Street address*","placeholder-ar":"عنوان الشارع*","_trans":"true","name":"address","pclass":"ins-col-12 ins-m-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"_type": "input","type":"text","placeholder":"Apartment, suits, etc (Optional)","placeholder-ar":"شقة، جناح، الخ (اختياري)","_trans":"true","name":"address_2","pclass":"ins-col-12 ins-m-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"end":"true"})

        uidata.append({"class":"ins-space-s"})
        uidata.append({"class":"ins-col-grow"})
        uidata.append({"_data": "Add Address <img src='"+p+"style/right_arrow.svg'></img>","_data-ar":"إضافة عنوان","_trans":"true", "class": "ins-button-s ins-strong-m ins-flex-center ins-text-upper ins-m-col-6  -add-address-btn ins-gold-d ins-col-2","style":"height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"_data": " Back","_data-ar":"رجوع ","_trans":"true", "class": "ins-button-s ins-flex-center ins-strong-m ins-text-upper ins-gold-d-color   -back-address-btn ins-m-col-6  ins-col-2 ","style":"    height: 46px;"})
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
            self.ins._server._set_session("redirect", "/puser/")
            return """
            <script>
                window.location.href = "/login/";
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
