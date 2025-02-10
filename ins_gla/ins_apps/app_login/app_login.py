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
            {"_data": "Forgot Password?", "class": "ins-link ins-col-8 ins-title-14 -forgot-password-btn"},
            {"_data": "Login", "class": "ins-button-s ins-gold-d ins-col-4 -login-btn"},
            {"class": "ins-col-12 ins-flex-center ins-padding-top-m"},
            {"_data": "Don't have an account? <a class=' -signup-btn' >Signup now</a>", "class": " ins-col-12"},
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
            {"_data": "Next", "class": "ins-button-s ins-gold-d ins-col-4 -signup-step-1-btn"},
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
                {"_data": "Verify", "class": "ins-button-s ins-gold-d ins-col-4 -signup-step-2-btn"},
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
            {"_data": "Sign Up", "class": "ins-button-s ins-gold-d ins-col-4 -signup-step-3-btn"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    



         
    def _forgot_ui_step1(self):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start"},
            {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Mobile Number", "placeholder": "Enter Mobile Number", "type": "text", "name": "mobile", "class": "-forgot-mobile-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Next", "class": "ins-button-s ins-gold-d ins-col-4 -forgot-step-1-btn"},
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
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card -signup-form ins-text-start"},
                {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -forgot-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "mobile", "value": rq["mobile"], "class": "-forgot-mobile-inpt", "pclass": "ins-col-12 ins-hidden"},
                {"_data": "Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span>", "class": "ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
                {"_data": "Resend OTP", "class": "ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn -forgot-otp ins-hidden", "style": "cursor:pointer;"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex-end"},
                {"_data": "Verify", "class": "ins-button-s ins-gold-d ins-col-4 -forgot-step-2-btn"},
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
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start -signup-step-3-form"},
            {"_data": "Forgot Password", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "Mobile", "readonly":"true","value": rq["mobile"], "type": "text", "name": "mobile", "class": "-forgot-mobile-inpt", "pclass": "ins-col-12 ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Reset Password", "class": "ins-button-s ins-gold-d ins-col-4 -forgot-step-3-btn"},
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
        udata = self.user._check()
        if not udata:
                   uidata = [
            {"start": "true", "class": "-signup-area"},
            {"_data": self._email_password_ui(), "class": "ins-col-12"},
            {"end": "true"}
        ]
        else:
              uidata = [
                        {"start": "true", "class": "-signup-area ins-col-12 ins-flex-center gla-container ins-padding-2xl"},
                        {"_data": "You are already loged in", "class": "ins-col-8 ins-card ins-text-center"},
                        {"end": "true"}
                    ]
        return self.ins._ui._render(uidata)
