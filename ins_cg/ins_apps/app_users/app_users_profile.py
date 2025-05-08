from ins_cg.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App

class AppUsersProfile(App):
    def __init__(self, app) -> None:
        self.app: App = app
        self.user = Gusers(app.ins)
        super().__init__(app.ins)






    def user_setting(self, user):
        
        return [
            {"start": "true", "class": "ins-col-12 ins-flex-end ins-padding-2xl "},
            {"_type": "input", "required": "true", "value": user["first_name"], "title": "First Name","title-ar":"الاسم الأول","_trans":"true", "placeholder": "Enter First Name", "placeholder-ar": "أدخل الاسم الأول", "type": "text", "name": "first_name", "class": "-signup-first-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "value": user["last_name"], "title": "Last Name","title-ar":"اسم العائلة","_trans":"true", "placeholder": "Enter Last Name", "placeholder-ar": "أدخل اسم العائلة", "type": "text", "name": "last_name", "class": "-signup-last-name-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Update","_data-ar":" تحديث","_trans":"true", "class": "ins-button-m ins-gold-d ins-col-2 ins-flex-center -update-name-btn"},
            {"end": "true"}

        ]

    def change_password(self, data):
        return [
            {"start": "true", "class": "ins-col-12 ins-flex-end ins-padding-2xl "},
            {"_type": "input", "required": "true", "title": "Old Password","title-ar":" كلمة المرور القديمة","_trans":"true", "_end": '<i class="-show-old-password lni lni-eye"></i>', "placeholder": "Enter Old Password", "placeholder-ar": " كلمة المرور القديمة", "type": "password", "name": "old_password", "class": "-update-old-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "title": "Password","title-ar":" كلمة المرور","_trans":"true", "_end": '<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "type": "password", "placeholder-ar": " كلمة المرور ",  "name": "password", "class": "-update-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "title": "Confirm Password","title-ar":"تأكيد كلمة المرور","_trans":"true", "_end": '<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password",  "placeholder-ar": "تأكيد كلمة المرور","type": "password", "name": "confirm_password", "class": "-update-confirm-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Update","_data-ar":" تحديث","_trans":"true", "class": "ins-button-m ins-gold-d ins-col-2 ins-flex-center -update-password-btn"},
            {"end": "true"}

        ]

    def change_email(self, data):
        u = self.ins._users._session_get()
        udata = self.ins._db._get_row("kit_user","email,email_status",f"id='{u['id']}'")
        uidata = [            {"start": "true", "class": "ins-col-12 ins-flex ins-padding-2xl "},
            {"_type": "input", "value": data.get("email", ""), "title": "Email","title-ar":"بريد إلكتروني","_trans":"true", "placeholder": "Enter Email","placeholder-ar": "ادخل البريد الالكتروني", "type": "email", "name": "email", "class": "-update-email-inpt", "pclass": "ins-col-8 ins-m-col-6"},
            {"start": "true", "class": " -verified-area ins-col-4  ins-m-col-6"},
            ]
        
        ui_msg = "Verified Email <i class='lni lni-check ins-font-l'></i>"
        if self.ins._langs._this_get()["name"] == "ar":
                    ui_msg = "تم التحقق  <i class='lni lni-check ins-font-l'></i> "



        if udata["email_status"] != "verified":
         uidata.append({"_data": "Send Verification Code","_data-ar":"ارسال رمز التحقق","_trans":"true", "class": "ins-button-m ins-strong-m   ins-gold-bg  ins-col-12 -send-email-veri-btn ins-flex-center", "style": " margin-top: 35px;"})
        else:
         uidata.append({"_data": ui_msg,"_trans":"true", "class": " ins-strong-m   ins-col-12 ins-flex-center ins-border ins-radius-m", "style": " margin-top: 35px;min-height:40px"})

       
        uidata+= [   
                        {"end": "true"},


             {"class": "ins-line ins-col-12"},
            
            {"end": "true"}]
        
        return uidata

       

    def out(self, ins):
        g = self.ins._server._get()

        menus = [
            {"name": "user_setting", "title": "User Settings","title-ar":"إعدادات المستخدم", "icon": "lni-user-4"},
            {"name": "change_password", "title": "Change Password","title-ar":" تغيير كلمة المرور", "icon": "lni-locked-1"},
            {"name": "change_email", "title": "Change Email","title-ar":" تغيير البريد الإلكتروني","icon": "lni-envelope-1"}
        ]

        usmenu = [{"start": "true", "class": "ins-col-12 ins-flex ins-padding-xl"}]

        for m in menus:
            bclass = "ins-gold-d-color" if g.get("id") == m["name"] else ""
            aclass = "ins-strong-l" if g.get("id") == m["name"] else ""
            url = self.ins._server._url({'alias':'user','mode':'profile','id':m['name']})
            text = f"<i class='lni ins-font-l {bclass} {m['icon']}'></i>  {m['title']}"
            if self.ins._langs._this_get()["name"] == "ar":
                text =f"<i class='lni ins-font-l {bclass} {m['icon']}'></i>  {m['title-ar']}"
            usmenu.extend([
                {"start": "true", "class": f" ins-col-12 ins-primary-w ins-flex ins-border ins-radius-l ins-padding-m"},
                {"_type": "a", "href":url , "_data":text , "class": f"{bclass} {aclass} ins-title-xs ins-col-12"},
                {"end": "true"}
            ])

        usmenu.append({"end": "true"})

        border = "ins-border-right"
        if self.ins._langs._this_get()["name"] == "ar":
                    border = "ins-border-left"

        uidata = [
            {"class": "ins-space-l"},
            {"start": "true", "class": "gla-container ins-flex-center ins-padding-2xl  ins-card ins-flex-valign-start"},
            {"start": "true", "class": f"ins-col-4 ins-flex ins-text-upper {border}"},
        ]

        uidata += usmenu
        uidata += [
            {"end": "true"},
            {"start": "true", "class": "ins-col-8 ins-flex"},
        ]

        u = self.ins._users._session_get()
        user = self.ins._db._get_row("kit_user","*",f"id='{u['id']}'")


        if g.get("id") == "user_setting":
            uidata += self.user_setting(user)
        elif g.get("id") == "change_password":
            uidata += self.change_password(user)
        elif g.get("id") == "change_email":
            uidata += self.change_email(user)

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)
