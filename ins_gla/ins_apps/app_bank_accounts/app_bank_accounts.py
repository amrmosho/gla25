from ins_kit._engine._bp import App


class AppBankAccounts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def _image(ins , options , data):
     
        uiadta = [
            {"_data":data["logo"],"class":"ins-col-12 ins-size-m", "_view": "image","style": "max-width:100px"}
            
        ]
        return ins._ui._render(uiadta)


    def out(self):
        
        self.app._include("style.css")
        r = self.ins._apps._crud(properties=self.app._properties)

        return r
