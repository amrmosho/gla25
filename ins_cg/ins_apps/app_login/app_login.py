from ins_cg.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App

class AppLogin(App):
    def __init__(self, app) -> None:
        self.app: App = app
        self.user = Gusers(app.ins)
        super().__init__(app.ins)

    def _resend_otp(self):
          rq = self.ins._server._post()
          self.user._create_otp(rq["email"])

          return "1"



    def _login_ui(self,string=False):
        forgot_password = "<a href='/login/forgot_password' >Forgot Password?</a>"
        signup = "Don't have an account? <a href='/login/signup' >Signup now</a>"

        if self.ins._langs._this_get()["name"] == "ar":
            forgot_password = "<a href='/login/forgot_password' >هل نسيت كلمة المرور؟</a>"
            signup = "ليس لديك حساب؟ <a href='/login/signup' >انشاء حساب</a>"


        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center -login-area"},
            {"start": "true", "class": "ins-col-5 ins-flex ins-card -email-form ins-text-start"},
            {"_data": "Login", "_data-ar": "تسجيل الدخول","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email Address","title-ar":"البريد الإلكتروني", "placeholder": "Enter Email Address","placeholder-ar":"أدخل البريد الإلكتروني أو رقم الهاتف المحمول","_trans":"true", "type": "email", "name": "email", "class": "-login-email-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true", "title": "Password","title-ar":"كلمة المرور", "placeholder": "Enter Password", "placeholder-ar":"أدخل كلمة المرور","type": "password","_trans":"true", "name": "password", "class": "-login-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": forgot_password, "class": "ins-link ins-col-9 ins-title-14"},
            {"_data": "Login",  "_data-ar": "تسجيل الدخول","_trans":"true","class": "ins-button-m ins-gold-d ins-col-3 -login-btn"},
            {"class": "ins-col-12 ins-flex-center ins-padding-top-m"},
            {"_data": signup, "class": " ins-col-12"},
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
            {"_data": "Sign Up","_data-ar":"قم بالتسجيل","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email Address","title-ar":"البريد الالكتروني", "placeholder": "Enter Email Address","placeholder-ar":"أدخل البريد الالكتروني ", "_trans":"true","type": "email", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":"/login/","_data": "<i class='lni lni-arrow-left'></i> Back", "_data-ar":"خلف","_trans":"true","class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data": "Next <i class='lni lni-arrow-right'></i>",  "_data-ar":"التالي","_trans":"true","class": "ins-button-m ins-gold-d ins-col-3 -signup-step-1-btn"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    
    def _signup_ui_step2(self):
        if self.ins._langs._this_get()["name"] == "ar":
             otp = f" إعادة إرسال كود التحقق في   <span class='-otp-resend-counter ins-strong-m'>10</span> "
             verfiy =  "تحقق <i class='lni lni-check ins-font-l'></i> "
             back =  "<i class='lni lni-arrow-right'></i> خلف"

        if self.ins._langs._this_get()["name"] == "en":
             otp = f" Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span> "
             verfiy =  "Verify <i class='lni lni-check ins-font-l'></i> "
             back =  "<i class='lni lni-arrow-left'></i> Back"
        rq = self.ins._server._post()
        if self.user._email_exists(rq["email"]) == "-1":
            return "-1"
        
        if self.user._create_otp(rq["email"]):
           
            uidata = [
                {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card -signup-form ins-text-start"},
                {"_data": "Login", "_data-ar": "تسجيل الدخول","_trans":"true","class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "title-ar": "كود التحقق", "_trans":"true","placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -login-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "email", "value": rq["email"], "class": "-login-email-inpt", "pclass": "ins-col-12 ins-hidden"},
                {"_data": otp,"_trans":"true", "class": "ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
                {"_data": "Resend OTP","_data-ar":"إعادة إرسال كود التحقق","_trans":"true", "class": "ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn ins-hidden", "style": "cursor:pointer;"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex-end"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_data": back,"_trans":"true", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color -signup-back-1-btn"},
                {"class": " ins-col-6"},
                {"_data": verfiy,"_trans":"true","class": "ins-button-m ins-gold-d ins-col-3 ins-flex-center -signup-step-2-btn"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]
            return self.ins._ui._render(uidata)
    
    def _signup_ui_step3(self):
        rq = self.ins._server._post()
        chck_otp = self.user._check_otp(rq["email"],rq["otp"])
        if chck_otp != "1":
            return chck_otp

        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start -signup-step-3-form"},
            {"_data": "Sign Up","_data-ar":"قم بالتسجيل","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "First Name","title-ar":"الاسم الأول ","_trans":"true", "placeholder": "Enter First Name","placeholder-ar": "أدخل الاسم الأول","type": "text", "name": "first_name", "class": "-signup-first-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title": "Last Name", "title-ar":"اسم العائلة ","_trans":"true","placeholder": "Enter Last Name", "placeholder-ar": "أدخل الاسم الأخير","type": "text", "name": "last_name", "class": "-signup-last-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","title-ar":"كلمة المرور ","_trans":"true","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password","placeholder-ar": "أدخل كلمة المرور", "type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","title-ar":"تأكيد كلمة المرور ","_trans":"true","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password","placeholder-ar": "تأكيد كلمة المرور", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "Email Address","title-ar":"البريد الالكتروني ","_trans":"true", "readonly":"true","value": rq["email"], "type": "email", "name": "email", "class": "-signup-email-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Sign Up","_data-ar":"قم بالتسجيل","_trans":"true", "class": "ins-button-m ins-gold-d ins-col-3 -signup-step-3-btn"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    



         
    def _forgot_ui_step1(self):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -forgot-form ins-text-start"},
            {"_data": "Forgot Password", "_data-ar": "هل نسيت كلمة السر؟","_trans":"true","class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email Address","title-ar":"البريد الالكتروني", "placeholder": "Enter Email Address","placeholder-ar":"أدخل البريد الالكتروني ", "_trans":"true","type": "email", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":"/login/","_data": "<i class='lni lni-arrow-left'></i> Back","_data-ar":"خلف","_trans":"true", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data": "Next <i class='lni lni-arrow-right ins-font-l'></i>","_data-ar":"التالي","_trans":"true", "class": "ins-button-m ins-flex-center ins-gold-d ins-col-3 -forgot-step-1-btn"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    


    def _forgot_ui_step2(self):
        if self.ins._langs._this_get()["name"] == "ar":
             otp = f" إعادة إرسال كود التحقق في   <span class='-otp-resend-counter ins-strong-m'>10</span> "
             verfiy =  "تحقق <i class='lni lni-check ins-font-l'></i> "
             back =  "<i class='lni lni-arrow-right'></i> خلف"

        if self.ins._langs._this_get()["name"] == "en":
             otp = f" Resend OTP in <span class='-otp-resend-counter ins-strong-m'>10</span> "
             verfiy =  "Verify <i class='lni lni-check ins-font-l'></i> "
             back =  "<i class='lni lni-arrow-left'></i> Back"

        rq = self.ins._server._post()
        if self.user._email_exists(rq["email"]) == "1":
            return "-1"
        
        if self.user._create_otp(rq["email"]):
            uidata = [
                {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card -forgot-form ins-text-start"},
                {"_data": "Forgot Password","_data-ar": "هل نسيت كلمة السر؟","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "title-ar": "كود التحقق", "_trans":"true", "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -forgot-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "email", "value": rq["email"], "class": "-forgot-email-inpt", "pclass": "ins-col-12 ins-hidden"},
                {"_data": otp,"_trans":"true", "class": "ins-grey-color ins-title-14 ins-col-12 ins-text-start -resend-count-otp"},
                {"_data": "Resend OTP","_data-ar":"إعادة إرسال كود التحقق ","_trans":"true", "class": "ins-grey-d-color ins-strong-m ins-title-14 ins-col-12 ins-text-start -resend-otp-btn -forgot-otp ins-hidden", "style": "cursor:pointer;"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_type":"a","href":"/login/","_data": back,"_trans":"true", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
                {"class": " ins-col-6"},
                {"_data": verfiy,"_trans":"true", "class": "ins-button-m  ins-flex-center ins-gold-d ins-col-3 -forgot-step-2-btn"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]
            return self.ins._ui._render(uidata)
        
          
    def _forgot_ui_step3(self):
        rq = self.ins._server._post()

        chck_otp = self.user._check_otp(rq["email"],rq["otp"])

        if chck_otp != "1":
            return chck_otp

        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -forgot-form ins-text-start -signup-step-3-form"},
            {"_data": "Forgot Password","_data-ar": "هل نسيت كلمة السر؟","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","title-ar":"كلمة المرور","_trans":"true","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "placeholder-ar":"أدخل كلمة المرور","type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","title-ar":" تأكيد كلمة المرور","_trans":"true","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "placeholder-ar":"تأكيد كلمة المرور", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "email", "readonly":"true","value": rq["email"], "type": "text", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12 ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Reset Password", "_data-ar": "إعادة كلمة المرور","_trans":"true","class": "ins-button-m ins-gold-d ins-col-4 -forgot-step-3-btn"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    
    def _reset_password(self):
        rq = self.ins._server._post()
        self.user._reset_password(rq)
        return self._login_ui(True)


    
    
    def _login(self):
        rq = self.ins._server._post()
        rq["password"] = self.ins._data.hash_password(rq["password"])
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
            return self._login_ui(True)
        else:
            return "-1"
        
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")

        udata = self.user._check()


        g = self.ins._server._get()
        data = self._login_ui()

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
                        {"_data": "You are already logged in","_data-ar": "أنت مسجل الدخول بالفعل","_trans": "true", "class": "ins-col-8 ins-card ins-text-center"},
                        {"end": "true"}
                    ]
        return self.ins._ui._render(uidata)
