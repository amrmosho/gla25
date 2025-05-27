from flask import redirect
from ins_cg.ins_apps.app_users.app_users_orders import AppUsersOrders
from ins_cg.ins_apps.app_users.app_users_profile import AppUsersProfile
from ins_cg.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_cg.ins_kit._elui import ELUI
from ins_plgs.plg_login.plg_login import PlgLogin
p = "/ins_web/ins_uploads/"


class AppUsers(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)
    

    @property
    def _uid(self):
        return self.ins._users._session_get()["id"]
        



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
        elif g.get("mode") == "wishlist":
            sc = " ins-gold-bg "
        elif g.get("mode") == "order":
            oc = " ins-gold-bg "
        else:
            hc = " ins-gold-bg "
        ui = [{"start": "true", "class": "ins-col-7 ins-flex-end ins-m-col-12 ins-m-flex-center -user-page-btns-area"},
              {"_data": "<i class='lni ins-font-l lni-home-2 not-for-phone'></i>Home","_data-ar":"الرئيسية","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {hc}  ins-flex", "_type": "a", "href": self.u("")},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-user-4 not-for-phone'></i>Profile Management","_data-ar":"إدارة الملف الشخصي","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {pc}  ins-flex", "_type": "a", "href": self.u("profile")+"/user_setting"},
              {"_data": "|", "class": " "},
              {"_data": "<i class='lni ins-font-l lni-basket-shopping-3 not-for-phone'></i>My Orders","_data-ar":"طلبياتي","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper {oc} ins-flex ", "_type": "a", "href": self.u("order")},
              {"_data": "|", "class": "  "},
              {"_data": "<i class='lni ins-font-l lni-buildings-1 not-for-phone'></i>My wishlist","_data-ar":"قائمة الرغبات","_trans":"true",
                  "class": f"ins-button-s  -user-page-btn ins-text-upper   {sc} ins-flex ", "_type": "a", "href": self.u("wishlist")},
              {"end": "true"},

              ]
        return ELUI(self.ins).page_title("My Profile","ملفي الشخصي", [{"_data": "My Profile / ", "href": "/user","_data-ar":"ملفي الشخصي /","_trans":"true",}, {"_data": "Profile","_data-ar":"الملف الشخصي","_trans":"true",}], ui)

    def orders(self, g): 
        return AppUsersOrders(self.app).out()

    def profile(self, g): 
        return AppUsersProfile(self.app).out(self.ins)


    def _update_user_name(self):
        rq = self.ins._server._req()
        udata = self.ins._users._session_get()
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



        u = self.ins._users._session_get()
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
            udata = self.ins._users._session_get()
            if udata:
                self.ins._server._set_session("temp_mail",{"email":rq["email"]})
                link = self.user.generate_token(udata["id"],rq["email"], udata["mobile"], udata["password"])
                lang = {"link":link,"title":udata["title"]}
                self.ins._email.send_email(lang,rq["email"],1)
                
            return "1"



    def _check_email(self):
     rq = self.ins._server._req()
     u = self.ins._users._session_get()
     udata = self.ins._db._get_row("kit_user","email_status,email",f"id='{u['id']}'")

     if rq["email"] != udata["email"] or udata["email_status"] != "verified":
         return self.ins._ui._render( [{"_data": "Send Verification Code","_data-ar":"ارسال رمز التحقق","_trans":"true", "class": "ins-button-m ins-strong-m  -verified-area  ins-gold-bg  ins-col-12 -send-email-veri-btn ins-flex-center", "style": " margin-top: 35px;"}])
     ui_msg = "Verified Email <i class='lni lni-check ins-font-l'></i>"
     if self.ins._langs._this_get()["name"] == "ar":
        ui_msg = "تم التحقق  <i class='lni lni-check ins-font-l'></i> "
     return  self.ins._ui._render( [{"_data": ui_msg, "class": " ins-strong-m   ins-col-12 -verified-area ins-flex-center ins-border ins-radius-m", "style": " margin-top: 35px;min-height:40px"}])

     


    def _update_email(self):
        rq = self.ins._server._req()
        udata = self.ins._users._session_get()
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
                ui_msg = "Verified Email <i class='lni lni-check ins-font-l'></i>"
                if self.ins._langs._this_get()["name"] == "ar":
                    ui_msg = "تم التحقق  <i class='lni lni-check ins-font-l'></i> "
                r["ui"] = self.ins._ui._render( [{"_data":ui_msg, "class": " ins-strong-m   ins-col-12 -verified-area ins-flex-center ins-border ins-radius-m", "style": " margin-top: 35px;min-height:40px"}])
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
            title_wishlist = f'<i class="lni ins-font-l  lni-buildings-1 ins-m-col-1 -user-pages-icon"></i> عناويني '

        if self.ins._langs._this_get()["name"] == "en":
             title_profile = f'<i class="lni ins-font-l lni-user-4 ins-m-col-1 -user-pages-icon"></i>  Profile Management '
             title_order = f'<i class="lni ins-font-l lni-basket-shopping-3 ins-m-col-1 -user-pages-icon"></i>  My Orders '
             title_wishlist = f'<i class="lni ins-font-l  lni-buildings-1 ins-m-col-1 -user-pages-icon"></i> My wishlist '
             
        usmenu = [
            
            {"start": "true", "class": "  ins-col-12  ins-flex   ins-padding-2xl"},

            {"start": "true", "class": "  ins-col-4 ins-primary-w  ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"/user/profile/user_setting", "_data": title_profile,
                "class": " ins-title-s ins-col-12"},
                {"class":" not-for-web","style":"    width: 24px;"},
            {"_data": f'Update your name, email, and password to keep your account secure.',"_data-ar":"قم بتحديث اسمك والبريد الإلكتروني وكلمة المرور للحفاظ على حسابك آمنًا.","_trans":"true",
                "class": "ins-col-12 ins-padding-xl  ins-m-col-11  ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},


            {"start": "true", "class": "  ins-col-4    ins-primary-w ins-white ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a", "href":"/user/order", "_data": title_order,
                "class": " ins-title-s ins-col-12"},
                           {"class":" not-for-web","style":"    width: 24px;"},

            {"_data": f'Access detailed information about your current and past orders, including status and history.',"_data-ar":"احصل على معلومات مفصلة حول طلباتك الحالية والسابقة، بما في ذلك الحالة والتاريخ.","_trans":"true",
                "class": "ins-col-12 ins-padding-xl  ins-m-col-11   ins-padding-h ins-font-s ", "style": "line-height: 20px;margin-top: -11px;margin-bottom: 11px;"},
            {"end": "true"},



            {"start": "true", "class": "  ins-col-4  ins-primary-w ins-white  ins-flex ins-border ins-radius-xl    ins-padding-l"},
            {"_type": "a","href":"/user/wishlist",  "_data": title_wishlist,
                "class": " ins-title-s ins-col-12"},
                            {"class":" not-for-web","style":"    width: 24px;"},

            {"_data": f'Add, edit, or remove saved wishlist to simplify and speed up future purchases.',"_data-ar":"قم بإضافة أو تعديل أو إزالة العناوين المحفوظة لتبسيط وتسريع عمليات الشراء المستقبلية.","_trans":"true",
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
    
    def _wishlist_ui(self):
        wishlist = self.ins._users._get_settings('pro')["wishlist"]
        uidata=[{"_data":"My wishlist","_data-ar":"قائمة الرغبات","_trans":"ture","class":"ins-col-12 ins-title-m ins-strong-m ins-text-upper ins-grey-d-color"},
                {"start":True,"class":"ins-col-12 ins-flex"}]
       
       
       
       
        dd= self.ins._db._where_by_array( wishlist,field="gla_product.id")
       
       
        pdatas = self.ins._db._jget("gla_product","*",dd)
            
        pdatas._jwith("gla_product_category cat", "title,alias,id", "cat.id=Substring_Index(fk_product_category_id, ',', 1)", join="left join")
        
        pdatas._jwith("kit_user us", "title",
                       "gla_product.fk_user_id = us.id", join="left join")
            
        pdatas= pdatas._jrun()
       
       
       
        for pdata in pdatas:
         
            
            
            
            if pdata:
                uidata+= ELUI(self.ins).shop_pro_block(pdata)
        uidata.append({"end":"true"})
       
       
       
        return uidata


    def wishlist(self, g,udata):


        uidata=[{"start":"true","class":"ins-col-12 ins-flex   gla-container"},
                {"start":"true","class":"ins-flex ins-col-12 "},
                {"start":"true","class":"  ins-col-12 ins-gap-20  ins-flex   ins-padding-2xl"},
                {"_data":self._wishlist_ui(),"class":"ins-col-12 ins-flex"},
                {"end":"true"},
               {"end":"true"},
               {"end":"true"}
                ]
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


                  
        url = self.ins._server._url()
        self.ins._tmp._data_social_tags({"title":"My Profile","des":"Your gold journey starts here – manage your profile and preferences easily.","img":"ins_web/ins_uploads/images/seo/seo_logo.png","url":url})

        self.app._include("script.js")
        self.app._include("style.css")
       
        udata = self.ins._users._session_get()
 

        l=PlgLogin(self)
      
      
        l._login()

      
        if l.is_login():

            g = self.ins._server._get()
            r = self.header(g)
            if g.get("mode") == "profile":
                r += self.profile(g)
            elif g.get("mode") == "wishlist":
                r += self.wishlist(g,udata)
            elif g.get("mode") == "order":
                r += self.orders(g)
            else:
                r += self.home(g)
            return r
        else:
           return l._login_ui()
