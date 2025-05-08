from ins_kit._engine._bp import Plgin
from ins_plgs.plg_login.plg_forgot import PlgForgot
from ins_plgs.plg_login.plg_signup import PlgSignup
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
   
    
    def _login_ui_body(self):
        furl = self.ins._server._url({"show": "forgot"})        
        surl = self.ins._server._url({"show": "signup"})
        forgot_password = f"<a href='{furl}' >{self.ins._langs._get("forget_password", "users")}</a>"
        
        signup = f"{self.ins._langs._get("dont_have_account", "users")} <a href='{surl}' >{self.ins._langs._get("signup_now", "users")}</a>"
        uidata = [
            {"start": "true", "_type": "form", "method": "post","class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
            {"start": "true", "class": "ins-col-5 ins-flex ins-card -email-form ins-text-start"},
            {"_data": self.ins._langs._get("login", "users"), "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required": "true", "title": self.ins._langs._get("email_address", "users"), "placeholder":self.ins._langs._get("enter_email", "users") , "type": "email", "name": "email", "class": "-login-email-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "title": self.ins._langs._get("password", "users"), "placeholder":self.ins._langs._get("enter_password", "users"),"type": "password",  "name": "password", "class": "-login-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": forgot_password, "class": "ins-link ins-col-9 ins-title-14"},
            {"_data": self.ins._langs._get("forget_password", "users"), "_type": "button", "class": "ins-button-m ins-gold-d ins-col-3 -login-btn"},
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
            return PlgForgot(self.plg)._forgot_ui()
       
        elif "show" in g  and g["show"] =="signup":
            return PlgSignup(self.plg)._sginup_ui()
        else:
            return self._login_ui_body()
