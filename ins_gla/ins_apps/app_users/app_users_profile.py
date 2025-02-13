from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI

class AppUsersProfile(App):
    def __init__(self, app) -> None:
        self.app: App = app
        self.user = Gusers(app.ins)
        super().__init__(app.ins)

    def u(self, mode):
        return self.ins._server._url({"mode": mode})




    def user_setting(self, user):
        
        return [
            {"start": "true", "class": "ins-col-12 ins-flex-end ins-padding-2xl "},
            {"_type": "input", "required": "true", "value": user["first_name"], "title": "First Name", "placeholder": "Enter First Name", "type": "text", "name": "first_name", "class": "-signup-first-name-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "value": user["last_name"], "title": "Last Name", "placeholder": "Enter Last Name", "type": "text", "name": "last_name", "class": "-signup-last-name-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Update", "class": "ins-button-m ins-gold-d ins-col-2 ins-flex-center -update-name-btn"},
            {"end": "true"}

        ]

    def change_password(self, data):
        return [
            {"start": "true", "class": "ins-col-12 ins-flex-end ins-padding-2xl "},
            {"_type": "input", "required": "true", "title": "Password", "_end": '<i class="-show-password lni lni-eye"></i>', "placeholder": "Enter Password", "type": "password", "name": "password", "class": "-update-password-inpt", "pclass": "ins-col-12"},
            {"_type": "input", "required": "true", "title": "Confirm Password", "_end": '<i class="-show-confirm-password lni lni-eye"></i>', "placeholder": "Confirm Password", "type": "password", "name": "confirm_password", "class": "-update-confirm-password-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Update", "class": "ins-button-m ins-gold-d ins-col-2 ins-flex-center -update-password-btn"},
            {"end": "true"}

        ]

    def change_email(self, data):
        return [
            {"start": "true", "class": "ins-col-12 ins-flex ins-padding-2xl "},
            {"_type": "input", "value": data.get("email", ""), "title": "Email", "placeholder": "Enter Email", "type": "email", "name": "email", "class": "-update-email-inpt", "pclass": "ins-col-9"},
            {"_data": "Verification Code", "class": "ins-button-m ins-strong-m   ins-gold-bg  ins-col-3 -send-email-veri-btn ins-flex-center", "style": " margin-top: 35px;"},
            {"_type": "input", "title": "Verification Code", "placeholder": "Enter Verification Code", "type": "text", "name": "verification", "class": "-update-verification-inpt", "pclass": "ins-col-12"},
            {"class": "ins-line ins-col-12"},
            
            {"start": "true", "class": "ins-col-12 ins-flex-end "},
            {"_data": "Verify", "class": "ins-button-m ins-gold-d ins-col-2 ins-flex-center -update-email-btn"},
            {"end": "true"},
            {"end": "true"}

       
        ]

    def out(self, ins):
        g = self.ins._server._get()

        menus = [
            {"name": "user_setting", "title": "User Settings", "icon": "lni-user-4"},
            {"name": "change_password", "title": "Change Password", "icon": "lni-locked-1"},
            {"name": "change_email", "title": "Change Email", "icon": "lni-envelope-1"}
        ]

        usmenu = [{"start": "true", "class": "ins-col-12 ins-flex ins-padding-xl"}]

        for m in menus:
            bclass = "ins-gold-d-color" if g.get("id") == m["name"] else ""
            aclass = "ins-strong-l" if g.get("id") == m["name"] else ""

            usmenu.extend([
                {"start": "true", "class": f" ins-col-12 ins-primary-w ins-flex ins-border ins-radius-l ins-padding-m"},
                {"_type": "a", "href": f"{m['name']}", "_data": f'<i class="lni ins-font-l {bclass} {m['icon']}"></i>  {m['title']}', "class": f"{bclass} {aclass} ins-title-xs ins-col-12"},
                {"end": "true"}
            ])

        usmenu.append({"end": "true"})

        uidata = [
            {"class": "ins-space-l"},
            {"start": "true", "class": "gla-container ins-flex-center ins-padding-2xl  ins-card ins-flex-valign-start"},
            {"start": "true", "class": "ins-col-4 ins-flex ins-text-upper ins-border-right"},
        ]

        uidata += usmenu
        uidata += [
            {"end": "true"},
            {"start": "true", "class": "ins-col-8 ins-flex"},
        ]

        u = self.user._check()
        user = self.ins._db._get_row("kit_user","*",f"id='{u["id"]}'")


        if g.get("id") == "user_setting":
            uidata += self.user_setting(user)
        elif g.get("id") == "change_password":
            uidata += self.change_password(user)
        elif g.get("id") == "change_email":
            uidata += self.change_email(user)

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)
