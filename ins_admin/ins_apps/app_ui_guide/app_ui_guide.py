from ins_admin.ins_apps.app_ui_guide.app_ui_guide_inputs import AppUiGuideInputs
from ins_admin.ins_apps.app_ui_guide.app_ui_guide_test import  AppUiGuideTest
from ins_kit._engine._bp import App


class AppUiGuide(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):
     
        g= self.ins._server._get()
        
        if  "mode" in g  and   g["mode"] =="inputs":
            
            return AppUiGuideInputs(self.app).out()
        elif  "mode" in g  and   g["mode"] =="test":
            
            return AppUiGuideTest(self.app).out()      
        else:
            return "<div class='ins-flex ins-card'> <iframe style='       border: none; width: 100%;    height: calc(100vh - 120px); min-height: 550px;'  src='http://127.0.0.1:5000/ins_web/ins_incs/line_icons_2/examples/index.html'></iframe></div>"
