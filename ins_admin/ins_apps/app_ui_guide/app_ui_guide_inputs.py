from ins_kit._engine._bp import App


class AppUiGuideInputs(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _input(self, _type="input", type="text" ,title="_Title", m={}):

        v = {"_type": _type, "type": type, "title": title, "name": "_unname",
             "placeholder": "_add placeholder hear", "pclass": "ins-col-12 ", "required": "true"}
        v.update(m)
        uidata = [
            {"start": "true", "class": "ins-col-6 ins-card  ins-flex "},
            {"_data": f"> {type} {_type} ", "class": "ins-col-12 ins-title-m  "},

            v,
            {"_type": "em", "_data": f'{v}', "class": "code"},
            {"end": "true"}]

        return uidata

    def out(self):
        uidata = [{"start": "true", "class": "ins-col-12  ins-flex  ins-padding-xl"},]



        uidata.append( {"start": "true", "class": "ins-col-12  ins-margin-xl ins-bg-4 ins-border ins-card  ins-flex "})
        uidata.append({"_data": f"> Input ", "class": "ins-col-12 ins-title-m  "})

        uidata += self._input(title="sample input")
        uidata += self._input(title="input start by text",m={"_start" :"_start text"})
        uidata += self._input(title="input start by icon",m={"_start" :"<i class=\"lni ins-icon lni-user-4\"></i>"})
        uidata += self._input(title="input end by text",m={"_end" :"_end text"})
        uidata += self._input(title="input end by icon",m={"_end" :"<i class=\"lni ins-icon lni-user-4\"></i>"})
        
        
        uidata += self._input(type="email")


        uidata += self._input(type="email")

        uidata += self._input(type="tel")
        uidata += self._input(type="search")

        uidata += self._input(type="number")
        uidata += self._input(type="datetime-local")
        uidata += self._input(type="password")

        uidata += self._input(type="date")
        uidata += self._input(type="time")
        uidata += self._input(type="month")
        uidata += self._input(type="week")
        uidata += self._input(type="url")


        uidata += self._input(type="color")
        uidata += self._input(type="file")
        
        uidata.append({"end": "true"})

        
        uidata.append( {"start": "true", "class": "ins-col-12  ins-margin-xl ins-bg-4 ins-border ins-card  ins-flex "})
        uidata.append({"_data": f"> Select ", "class": "ins-col-12 ins-title-m  "})
        
        uidata += self._input(type="auto" ,title="Sample Auto" ,m={"fl_data": "option_1,option_2,option_3"})


        uidata += self._input(type="auto_select" ,title="Sample Auto" ,m={"fl_data": "option_1,option_2,option_3,option_4,option_5,option_6"})

        uidata += self._input(type="tags" ,title="Tages" ,m={"fl_data": "option_1,option_2,option_3,option_4,option_5,option_6"})







        uidata.append({"end": "true"})

        
        
       
        uidata.append( {"start": "true", "class": "ins-col-12 ins-bg-4  ins-margin-xl ins-border ins-card  ins-flex "})
        
    
        uidata.append({"_data": f"> Select ", "class": "ins-col-12 ins-title-m  "})
        uidata += self._input("select", "", "sample select",{"fl_data": "option_1,option_2,option_3"})
        uidata += self._input("select", "areas", " select areas" )
        
        uidata += self._input("select", "", " select from db ",m={"fl_table":"kit_menu" ,"fl_type":"db","fl_text":"title" ,"fl_value":"id" ,"fl_where":'id>2'} )

        uidata.append({"end": "true"})
        
        
        
        uidata.append( {"start": "true", "class": "ins-col-12 ins-bg-4  ins-margin-xl ins-border ins-card  ins-flex "})
        
    
        uidata.append({"_data": f"> Upload ", "class": "ins-col-12 ins-title-m  "})
     

        uidata += self._input(type="upload" ,title="Upload image" ,m={ "_dir": "test","_exts": "image/png" })
        
        
        uidata += self._input(type="upload" ,title="multi  images Upload" ,m={ "_dir": "test","_mode":"multi" ,"_exts": "image/png" })



       
        uidata.append({"end": "true"})
        
        
        
        
        

        uidata.append({"end": "true"})

        r = self.ins._ui._render(uidata)

        return r
