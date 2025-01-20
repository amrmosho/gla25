from ins_kit._engine._bp import App


class AjxUsers(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)



    def get_settings(self):
        p = self.ins._server._post()
        return self.ins._users._get_settings(p["name"])

    def set_settings(self):
        p = self.ins._server._post()
        name = p["name"]
        del p["name"]
        if "multiaple" in p:
            del p["multiaple"]
        
        if "data" in p :
             p = self.ins._json._decode(p["data"])
        self.ins._users._updat_settings(name, p)
        return p

    def logout(self):
        self.ins._users._logout()
        return {"status": "1"}
