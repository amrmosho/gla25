from ins_kit._engine._bp import App


class AppProduct(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def _label(ins , options , data):
        return data["title"]

    def out(self):
        
        r = self.ins._apps._crud(properties=self.app._properties)

        return r
