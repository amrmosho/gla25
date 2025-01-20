from ins_kit._engine._bp import App


class AppBlog(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):
        
        self.app._include("style.css")
        r = self.ins._apps._crud(properties=self.app._properties)

        return r
