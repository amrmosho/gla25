

from ins_kit._engine._bp import App


class AppBlogCategory(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):

        ops = self.ins._apps._crud_ops
        
        
        ops._table = "cg_blog_category"
        r = self.ins._apps._crud(ops,properties=self.app._properties)
        return r
