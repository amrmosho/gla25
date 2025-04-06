from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from flask import request


class AppActive(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user= Gusers(app.ins)

    def get_token(self):
        url = request.url 
        token = url.split("/active/")[-1]
        return token


    def check_token(self, token):
        data = self.user._check_token(token)
        return data
    

    def prepare(self):
        uidata = [
            {"start":"true","class":"ins-col-12 gla-container ins-padding-l ins-flex-center"},
        ]

        data = self.user._check_token(self.get_token())

        if "status" in data and data["status"] == "1":
            udata = self.user._login(data["data"])
            if udata:
                self.ins._db._update("kit_user", {"email_status": "verified","email":data["data"]["email"]}, f"id = {data["data"]["user_id"]}")
                self.ins._db._update("gla_email_token", {"status": "expired"}, f"id = {data["data"]["token_id"]}")
                uidata.append({"_data":"Your email has been verified successfully.","class":"ins-card ins-padding-l ins-col-8 ins-flex-center ins-text-center"})
        elif "status" in data and data["status"] == "-1":
            uidata.append({"_data":"Invalid URL.","class":"ins-card ins-padding-l ins-col-8 ins-flex-center ins-text-center"})
        else:
            uidata.append({"_data":"URL has beed expired.","class":"ins-card ins-padding-l ins-col-8 ins-flex-center ins-text-center"})
                

        uidata.append({"end":"true"})     
        return self.ins._ui._render(uidata)
    def out(self):
     
        return self.prepare()
 
