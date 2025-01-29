from ins_kit._engine._bp import App


class AppProduct(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _image(ins , options , data):
        uiadta = [
            {"_data":data["th_main"],"class":"ins-col-12 ins-size-m", "_view": "image","style": "max-width:100px"}
            
        ]
        return ins._ui._render(uiadta)

    def _title(ins,options,data):   
        uiadta = [
            {"_data":data["title"] ,"class":"ins-primary-color ins-col-12 ins-title-xs"},
            {"_data":data["weight"]+" GM","class":" ins-col-8 ins-text-center ins-title-xl ins-strong ins-font-s ins-tag ins-primary-color ins-flex-center"},
            {"_data":data["kart"]+" K","class":"ins-col-8 ins-text-center ins-title-xl ins-strong ins-font-s  ins-tag ins-primary-color ins-flex-cenetr"},
        ]
        return ins._ui._render(uiadta)
    


    def out(self):
        
        r = self.ins._apps._crud(properties=self.app._properties)

        return r
