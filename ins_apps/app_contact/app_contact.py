

from ins_kit._engine._bp import App


class AppContact(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):

        ui = [

            {"_type": "span",   "class": " ins-col-12 ins-flex  ins-card", "start": True},


            {"class": "ins-col-6  ins-flex  ins-padding-l", "start": True},
            {"_type": "input", "title": "messahe title", "pclass": "ins-col-12"},
            {"_type": "input", "type": "textarea",
                "title": "messahe title", "pclass": "ins-col-12"},
            {"_data": "send", "class": "ins-col-4 ins-button ins-primary"},
            {"end": True},






        ]
        
        b =[
           
            {"start": True, "class": "ins-col-6 "},
            {"_data": "des des des des des des des des des des des des "}, 
            
        ]
        
        
        ui += b
        ui.append({"end": True})
        ui.append({"_type": "span", "end": True})

        return self.ins._ui._render(ui)
