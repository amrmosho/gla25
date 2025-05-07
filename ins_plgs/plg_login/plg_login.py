from flask import redirect, url_for
from ins_kit._engine._bp import Plgin
class PlgLogin(Plgin):
    def __init__(self, plg) -> None:
        self.plg: Plgin = plg
        super().__init__(plg.ins)

    def is_login(self) -> bool:
        """hi this's method return is user login or no """
        return self.ins._users._is_login()
    
    
    
    def _login(self):
        p = self.ins._server._post()
        if "password" in p:
            self.ins._users._login(p)
   


    def __forget_ui(self):
        p = self.ins._server._post()
        if "step" in p and p["step"] == "otp":
            url = self.ins._server._url({"step": "otp"})
            self.ins._server._redirect(url)

        back = self.ins._server._url({},{"show"})
        uidata = [
            {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -forgot-form ins-text-start"},
            {"_data": "Forgot Password", "_data-ar": "هل نسيت كلمة السر؟","_trans":"true","class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email Address","title-ar":"البريد الالكتروني", "placeholder": "Enter Email Address","placeholder-ar":"أدخل البريد الالكتروني ", "_trans":"true","type": "email", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "type": "text", "name": "step","value":"otp", "pclass": "ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":back,"_data": "<i class='lni lni-arrow-left'></i> Back","_data-ar":"خلف","_trans":"true", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data": "Next <i class='lni lni-arrow-right ins-font-l'></i>","_type":"button","class": "ins-button-m ins-flex-center ins-gold-d ins-col-3"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true","_type": "form" }
        ]
        return self.ins._ui._render(uidata)
    


    def __sginup(self):
        return "_sginup"
    def __login_ui_body(self):
        furl = self.ins._server._url({"show": "forgot"})        
        surl = self.ins._server._url({"show": "signup"})
        forgot_password = f"<a href='{furl}' >{self.ins._langs._get("forget_password", "users")}</a>"
        signup = f"Don't have an account? <a href='{surl}' >Signup now</a>"
        uidata = [
            {"start": "true", "_type": "form", "method": "post",
                "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
            {"start": "true", "class": "ins-col-5 ins-flex ins-card -email-form ins-text-start"},
            {"_data": "Login", "_data-ar": "تسجيل الدخول", "_trans": "true",
                "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required": "true", "title": "Email Address", "title-ar": "البريد الإلكتروني", "placeholder": "Enter Email Address",
                "placeholder-ar": "أدخل البريد الإلكتروني أو رقم الهاتف المحمول", "_trans": "true", "type": "email", "name": "email", "class": "-login-email-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "title": "Password", "title-ar": "كلمة المرور", "placeholder": "Enter Password",
                "placeholder-ar": "أدخل كلمة المرور", "type": "password", "_trans": "true", "name": "password", "class": "-login-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": forgot_password, "class": "ins-link ins-col-9 ins-title-14"},
            {"_data": "Login", "_type": "button", "_data-ar": "تسجيل الدخول",
                "_trans": "true", "class": "ins-button-m ins-gold-d ins-col-3 -login-btn"},
            {"class": "ins-col-12 ins-flex-center ins-padding-top-m"},
            {"_data": signup, "class": " ins-col-12"},
            {"end": "true"},
            {"end": "true", "_type": "form", }
        ]
        return self.ins._ui._render(uidata)
    def _login_ui(self):
        self._login()
        g= self.ins._server._get() 
        if "show" in g  and g["show"] =="forgot":
            return self.__forget_ui()
        elif   "show" in g  and g["show"] =="signup":
            return self.__sginup()
        else:
            return self.__login_ui_body()
