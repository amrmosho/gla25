from ins_kit._engine._bp import App


class AppUiGuideTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _input(self, ):

        uidata = [
            {"start": "true", "class": "ins-col-6 ins-card  ins-flex "},

            {"_type": "input", "type": "auto_select", "title": "_Title",
             "name": "_unname", "pclass": "ins-col-12 ", "value":"3",
             "fl_data": {"0": 'sssss', "2": 'sasdasdss', "3": '888', "9": '8989'}},
            {"end": "true"},
           
           
           
            {"start": "true", "class": "ins-col-6 ins-card  ins-flex "},

         
            {"_type": "select",  "title": "_Title",
             "name": "_unname", "pclass": "ins-col-12 ",
            
               
             
             },
            
            
            
            {"end": "true"},


        ]




        d= self.ins._data_collect._render({ "fl_type":"areas" ,"fl_table":"kit_menu","fl_start":"-1,-----"})
        
        tt= d["fl_data"]

        return self.ins._ui._render(uidata)

    def out(self):

        r = self._input()
        return r
