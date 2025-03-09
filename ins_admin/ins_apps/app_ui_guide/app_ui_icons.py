from ins_kit._engine._bp import App


class AppUiGuideIcons(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def icont(self ,c):
            return f"<div class='ins-border ins-col-2 ins-card ins-flex-center '> <div style='width: 90px;height: 90px;' class='ins-col-12 ins-icons {c}'></div> <b class='ins-col-12 ins-text-center'>{c}</b> </div>"

    def insya(self):
        r= "<div class='ins-flex ins-col-12 ins-card ins-padding-l'>"
        r+= self.icont("ins-icons-ai")
        r+= self.icont("ins-icons-search")
        r+= self.icont("ins-icons-arrow-up")
        r+= self.icont("ins-icons-arrow-down")
        r+= self.icont("ins-icons-arrow-left")
        r+= self.icont("ins-2-arrow-left")
        r+= self.icont("ins-icons-500")




        r+= "</div>"
        return r

    def out(self):
            return "<div class='ins-flex ins-col-12 ins-card'> <iframe style='       border: none; width: 100%;    height: calc(100vh - 120px); min-height: 550px;'  src='http://127.0.0.1:5000/ins_web/ins_incs/line_icons_2/examples/index.html'></iframe></div>"

