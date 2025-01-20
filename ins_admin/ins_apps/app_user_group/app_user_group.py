from ins_kit._engine._bp import App
from .app_user_group_custom import AppUserCustom
from .app_user_group_apps import AppUserApps

class AppUserGroup(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _apps_call(self):
        req = self.ins._server._req()
        a = AppUserApps(self.app)
        return eval(f"a.{req["c"]}()")

    def _custom_call(self):
        req = self.ins._server._req()
        a = AppUserCustom(self.app)
        return eval(f"a.{req["c"]}()")


    def out(self):
        ops = self.ins._apps._crud_ops
        self.app._include("script.js")
        r = self.ins._apps._crud(ops, properties=self.app._properties)
        return r
