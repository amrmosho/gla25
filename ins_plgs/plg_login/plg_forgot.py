from ins_kit._engine._bp import Plgin
class PlgForgot(Plgin):
    def __init__(self, plg) -> None:
        self.plg: Plgin = plg
        super().__init__(plg.ins)


    def __forget_reset_ui(self):
        p = self.ins._server._post()
        if "password" in p and "confirm_password" in p and p["password"] == p["confirm_password"]:
            self.ins._users._update_password(p)
            return self.ins._server._redirect(self.ins._server._url({},["show","step"]))
        uidata = [
            {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card  ins-text-start"},
            {"_data": "Forgot Password","_data-ar": "هل نسيت كلمة السر؟","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": "Password","title-ar":"كلمة المرور","_trans":"true","_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "placeholder-ar":"أدخل كلمة المرور","type": "password", "name": "password", "class": "-signup-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title": "Confirm Password","title-ar":" تأكيد كلمة المرور","_trans":"true","_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "placeholder-ar":"تأكيد كلمة المرور", "type": "password", "name": "confirm_password", "class": "-signup-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": "email", "readonly":"true","value": p["email"], "type": "text", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12 ins-hidden"},
            {"_type": "input", "type": "text", "name": "otp", "value": p["otp"],  "pclass": "ins-col-12 ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Reset Password","_type":"button", "_data-ar": "إعادة كلمة المرور","_trans":"true","class": "ins-button-m ins-gold-d ins-col-4 -forgot-step-3-btn"},
            {"end": "true"},
            {"end": "true","_type": "form"}
        ]
        return self.ins._ui._render(uidata)
    

    def __forget_otp_ui(self):
        p = self.ins._server._post()
        if "otp" in p and p["otp"] != "":
            check_otp =  self.ins._users._check_otp(p["email"],p["otp"])
            if check_otp == "1":
                return self.__forget_reset_ui()
        self.ins._users._create_otp(p["email"])
        back = self.ins._server._url({},{"step"})
        uidata = [
                {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card ins-text-start"},
                {"_data": "Forgot Password","_data-ar": "هل نسيت كلمة السر؟","_trans":"true", "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": "OTP", "title-ar": "كود التحقق", "_trans":"true", "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -forgot-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "email", "value": p["email"],  "pclass": "ins-col-12 ins-hidden"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_type":"a","href":back,"_data":"back" ,"_trans":"true", "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
                {"class": " ins-col-6"},
                {"_data": "Verify","_type":"button","_trans":"true", "class": "ins-button-m  ins-flex-center ins-gold-d ins-col-3 -forgot-step-2-btn"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true","_type": "form" }
            ]
        return self.ins._ui._render(uidata)
    
    
    def _forgot_ui(self):
        p = self.ins._server._post()
        if "email" in p :
            check_email =  self.ins._users._email_exists(p["email"])
            if check_email == True:
                return self.__forget_otp_ui()
        back = self.ins._server._url({},{"show"})
        uidata = [
            {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card ins-text-start"},
            {"_data": "Forgot Password", "_data-ar": "هل نسيت كلمة السر؟","_trans":"true","class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": "Email Address","title-ar":"البريد الالكتروني", "placeholder": "Enter Email Address","placeholder-ar":"أدخل البريد الالكتروني ", "_trans":"true","type": "email", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12"},
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
