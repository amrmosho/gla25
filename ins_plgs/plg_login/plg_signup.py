from ins_kit._engine._bp import Plgin
class PlgSignup(Plgin):
    def __init__(self, plg) -> None:
        self.plg: Plgin = plg
        super().__init__(plg.ins)


    def __signup_form_ui(self):
        p = self.ins._server._post()
        error={}
        if "password" in p and "confirm_password" in p and p["password"] == p["confirm_password"]:
            self.ins._users._signup(p)
            return self.ins._server._redirect(self.ins._server._url({},["show","step"]))
        else:
                error = self.ins._ui._error_msg(self.ins._langs._get("password_not_match", "users"))

        uidata = [
            {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start -signup-step-3-form"},
           error,
            {"_data": self.ins._langs._get("signup", "users"), "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input","required":"true", "title": self.ins._langs._get("first_name", "users"), "placeholder": self.ins._langs._get("enter_first_name", "users"),"type": "text", "name": "first_name", "class": "-signup-first-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title":self.ins._langs._get("last_name", "users"),"placeholder":self.ins._langs._get("enter_last_name", "users"),"type": "text", "name": "last_name", "class": "-signup-last-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input","required":"true", "title":self.ins._langs._get("password", "users"),"_end":'<i class="-show-password lni lni-eye"></i>', "placeholder": self.ins._langs._get("enter_password", "users"), "type": "password", "name": "password", "class": "-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required":"true","title":self.ins._langs._get("confirm_password", "users"),"_end":'<i class="-show-confirm-password lni lni-eye"></i>', "placeholder":self.ins._langs._get("enter_confirm_password", "users"), "type": "password", "name": "confirm_password", "class": "-confirm-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "title": self.ins._langs._get("email_address", "users"), "readonly":"true","value": p["email"], "type": "email", "name": "email", "class": "-signup-email-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "type": "text", "name": "otp", "value": p["otp"],  "pclass": "ins-col-12 ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": self.ins._langs._get("signup", "users"),"_type":"button", "class": "ins-button-m ins-primary ins-col-3"},
            {"end": "true"},
            {"end": "true","_type": "form" }
        ]
        return self.ins._ui._render(uidata)
    

    def __signup_otp_ui(self):
        p = self.ins._server._post()
        if "otp" in p and p["otp"] != "":
            check_otp =  self.ins._users._check_otp(p["email"],p["otp"])
            if check_otp == "1":
                return self.__signup_form_ui()
        self.ins._users._create_otp(p["email"])
        back = self.ins._server._url({},{"step"})

        
        uidata = [
                {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
                {"start": "true", "class": "ins-col-5 ins-flex-center ins-card ins-text-start"},
                {"_data": self.ins._langs._get("forget_password", "users"), "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
                {"_type": "input", "title": self.ins._langs._get("otp", "users"), "placeholder": "----", "type": "text", "name": "otp", "class": "ins-title-l -forgot-otp-inpt ins-form-input ins-text-center", "pclass": "ins-col-6", "style": "letter-spacing: 25px; height: 60px;"},
                {"_type": "input", "type": "text", "name": "email", "value": p["email"],  "pclass": "ins-col-12 ins-hidden"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": "ins-col-12 ins-flex "},
                {"_type":"a","href":back,"_data":self.ins._langs._get("back", "users") , "class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
                {"class": " ins-col-6"},
                {"_data": self.ins._langs._get("verify", "users"),"_type":"button", "class": "ins-button-m  ins-flex-center ins-primary ins-col-3"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true","_type": "form" }
            ]
        return self.ins._ui._render(uidata)
    

    def _sginup_ui(self):
        p = self.ins._server._post()
        error = {}
        if "email" in p :
            check_email =  self.ins._users._email_exists(p["email"])
            if check_email == False:
                return self.__signup_otp_ui()
            else:
                error = self.ins._ui._error_msg(self.ins._langs._get("user_exists", "users"))

        back = self.ins._server._url({},{"show"})

        
        uidata = [
            {"start": "true", "_type": "form", "method": "post", "class": "ins-col-12 ins-flex-center ins-padding-2xl ins-text-center "},
            {"start": "true", "class": "ins-col-5 ins-flex-end ins-card -signup-form ins-text-start"},
            error,
            {"_data":  self.ins._langs._get("signup", "users"), "class": "ins-title-m ins-strong-m ins-grey-d-color ins-text-upper ins-col-12"},
            {"_type": "input", "required":"true","title": self.ins._langs._get("email_address", "users"), "placeholder": self.ins._langs._get("enter_email", "users"),"type": "email", "name": "email", "class": "-forgot-email-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": "ins-col-12 ins-flex "},
            {"_type":"a","href":back,"_data": self.ins._langs._get("back", "users"),"class": "ins-button-m ins-flex-center ins-col-3 ins-grey-d-color"},
            {"class": " ins-col-6"},
            {"_data":self.ins._langs._get("next", "users"),"_type":"button","class": "ins-button-m ins-primary ins-col-3 "},
            {"end": "true"},
            {"end": "true"},
            {"end": "true","_type": "form" }
        ]
        return self.ins._ui._render(uidata)    