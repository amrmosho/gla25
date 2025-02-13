from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App

class AppLogin(App):
    def __init__(self, app) -> None:
        self.app: App = app
        self.user = Gusers(app.ins)
        super().__init__(app.ins)

    def _resend_otp(self):
          rq = self.ins._server._post()
          self.user._create_otp(rq["mobile"])

          return "1"



    def _email_password_ui(self,string=False):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
            {"start": "true", "class": "ins-col-5 ins-flex ins-card -email-form ins-text-start"},
            {"_data": "Login", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email or Mobile Number", "placeholder": "Enter Email or Mobile Number", "type": "text", "name": "email_mobile", "class": "-login-email-mobile-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true", "title": "Password", "placeholder": "Enter Password", "type": "password", "name": "password", "class": "-login-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "<a href='forgot_password' >Forgot Password?</a>", "class": "ins-link ins-col-9 ins-title-14"},
            {"_data": "Login", "class": "ins-button-m ins-gold-d ins-col-3 -login-btn"},
            {"class": "ins-col-12 ins-flex-center ins-padding-top-m"},
            {"_data": "Don't have an account? <a href='signup' >Signup now</a>", "class": " ins-col-12"},
            {"end": "true"},
            {"end": "true"}
        ]
        if string:
         return self.ins._ui._render(uidata)
        return uidata
    
    def _signup_ui_step1(self):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start"},
            {"_data": "Sign Up", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Mobile Number", "placeholder": "Enter Mobile Number", "type": "text", "name": "mobile", "class": "-signup-mobile-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":"/login/","_data": "<i class='lni lni-arrow-left'></i> Back", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data": "Next <i class='lni lni-arrow-right'></i>", "class": "ins-button-m ins-gold-d ins-col-3 -signup-step-1-btn"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    
    def _signup_ui_step2(self):
        rq = self.ins._server._post()
        if self.user._mobile_exists(rq["mobile"]) == "-1":
            return "-1"
        
        if self.user._create_otp(rq["mobile"]):
            uidata = [
                {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card -signup-form ins-text-start"},
                {"_data": "Login", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -login-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "mobile", "value": rq["mobile"], "class": "-login-mobile-inpt", "pclass": "ins-col-12 ins-hidden"},
                {"_data": "Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span>", "class": "ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
                {"_data": "Resend OTP", "class": "ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn ins-hidden", "style": "cursor:pointer;"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex-end"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_data": "<i class='lni lni-arrow-left'></i> Back", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color -signup-back-1-btn"},
                {"class": " ins-col-6"},
                {"_data": "Verify <i class='lni lni-check ins-font-l'></i>", "class": "ins-button-m ins-gold-d ins-col-3 ins-flex-center -signup-step-2-btn"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]
            return self.ins._ui._render(uidata)
    
    def _signup_ui_step3(self):
        rq = self.ins._server._post()

        chck_otp = self.user._check_otp(rq["mobile"],rq["otp"])

        if chck_otp != "1":
            return chck_otp

        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start -signup-step-3-form"},
            {"_data": "Sign Up", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "First Name", "placeholder": "Enter First Name", "type": "text", "name": "first_name", "class": "-signup-first-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title": "Last Name", "placeholder": "Enter Last Name", "type": "text", "name": "last_name", "class": "-signup-last-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "Mobile", "readonly":"true","value": rq["mobile"], "type": "text", "name": "mobile", "class": "-signup-mobile-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "Email (Optional)", "placeholder": "Enter Email", "type": "email", "name": "email", "class": "-signup-email-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Sign Up", "class": "ins-button-m ins-gold-d ins-col-3 -signup-step-3-btn"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    



         
    def _forgot_ui_step1(self):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -forgot-form ins-text-start"},
            {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Mobile Number", "placeholder": "Enter Mobile Number", "type": "text", "name": "mobile", "class": "-forgot-mobile-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":"/login/","_data": "<i class='lni lni-arrow-left'></i> Back", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data": "Next <i class='lni lni-arrow-right ins-font-l'></i>", "class": "ins-button-m ins-flex-center ins-gold-d ins-col-3 -forgot-step-1-btn"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    

        
    def _forgot_ui_step2(self):
        rq = self.ins._server._post()
        if self.user._mobile_exists(rq["mobile"]) == "1":
            return "-1"
        
        if self.user._create_otp(rq["mobile"]):
            uidata = [
                {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card -forgot-form ins-text-start"},
                {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -forgot-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "mobile", "value": rq["mobile"], "class": "-forgot-mobile-inpt", "pclass": "ins-col-12 ins-hidden"},
                {"_data": "Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span>", "class": "ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
                {"_data": "Resend OTP", "class": "ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn -forgot-otp ins-hidden", "style": "cursor:pointer;"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_type":"a","href":"/login/","_data": "<i class='lni lni-arrow-left'></i> Back", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
                {"class": " ins-col-6"},
                {"_data": "Verify <i class='lni lni-check ins-font-l'></i> ", "class": "ins-button-m  ins-flex-center ins-gold-d ins-col-3 -forgot-step-2-btn"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]
            return self.ins._ui._render(uidata)
        
          
    def _forgot_ui_step3(self):
        rq = self.ins._server._post()

        chck_otp = self.user._check_otp(rq["mobile"],rq["otp"])

        if chck_otp != "1":
            return chck_otp

        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -forgot-form ins-text-start -signup-step-3-form"},
            {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "Mobile", "readonly":"true","value": rq["mobile"], "type": "text", "name": "mobile", "class": "-forgot-mobile-inpt", "pclass": "ins-col-12 ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Reset Password", "class": "ins-button-m ins-gold-d ins-col-4 -forgot-step-3-btn"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    
    def _reset_password(self):
        rq = self.ins._server._post()
        self.user._reset_password(rq)
        return self._email_password_ui(True)


    
    
    def _login(self):
        rq = self.ins._server._post()
        chck = self.user._login(rq)
        session = self.ins._server._get_session("redirect")
        if chck:
            if session:
             return session
            else:
               return "/"
        else:
            return "-1"
        
    def _signup(self):
        rq = self.ins._server._post()
        chck = self.user._signup(rq)
        if chck == "1":
            return self._email_password_ui(True)
        else:
            return "-1"
        
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")

        udata = self.user._check()


        g = self.ins._server._get()
        data = self._email_password_ui()

        if "mode" in g:
            if g["mode"] == "signup":
                data = self._signup_ui_step1()
            elif g["mode"] == "forgot_password":
                data = self._forgot_ui_step1()


        if not udata:
                   uidata = [
            {"start": "true", "class": "-signup-area"},
            {"_data": data, "class": "ins-col-12"},
            {"end": "true"}
        
        
        
        ]
        else:
              uidata = [
                        {"start": "true", "class": "-signup-area ins-col-12 ins-flex-center gla-container ins-padding-2xl"},
                        {"_data": "You are already loged in", "class": "ins-col-8 ins-card ins-text-center"},
                        {"end": "true"}
                    ]
        return self.ins._ui._render(uidata)
