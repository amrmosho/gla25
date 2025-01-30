from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI


class AppUsersProfile(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def u(self, mode):

        return self.ins._server._url({"mode": mode},)


    def out(self,ins ):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-white ins-border ins-border-top"},


            {"start": "true", "class": "gla-container ins-flex ins-padding-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": "/", "_data": "AppUsersProfile /",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},







        ]

        return self.ins._ui._render(uidata)
