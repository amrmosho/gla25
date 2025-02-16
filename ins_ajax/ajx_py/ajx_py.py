from ins_kit._engine._bp import App


class AjxPy(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)



    def r(self):
        return "AjxPy"
        