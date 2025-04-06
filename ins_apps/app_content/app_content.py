
from ins_kit._engine._bp import App


class AppContent(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def test(self):
        return self.ins._server._req()  



    def _logout(self):
      self.ins._server._del_session("gla_login")
      return "1"


    def out(self):
        if "id" not in self.app._options:
            return " No content selected "
        data = self.ins._db._get_row(
            "content_table", "*", f"id={self.app._options["id"]}" ,True)
        if not data :
            return " No content selected "
            
        self.app._include("script.js")
        self.app._include("style.css")
        ui = [

            {"_data":   data["content"], "class": "ins-col-12  ins-flex ap-content-body "},

        ]
        return self.ins._ui._render(ui)
