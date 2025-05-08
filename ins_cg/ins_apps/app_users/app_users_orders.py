import json

from flask import send_from_directory
from ins_cg.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_cg.ins_kit._elui import ELUI
class AppUsersOrders(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user = Gusers(app.ins)
  
    def oui(self):
        r = ""
        orders = self.ins._db._get_data(
            "gla_order", "*", f"fk_user_id='{self.__user["id"]}' and order_id ='{self.g["id"]}'")
        
        
        dataui = [{"start": "true", "class": " ins-container ins-flex"}]
       
       
       
       
        for o in orders:
            items = self.ins._json._decode(o["items"])
            url = self.ins._server._url({"id": o["order_id"]})
            header = [
                {"start": "true", "class": "ins-col-12 ins-card ins-flex"},
                {"start": "true", "class": "ins-col-12  ins-flex"},
                {"_data": o["kit_created"], "_view": "date",
                    "class": "ins-col-grow"},
               
                {"end": "true"}
            ]
            d = []
            
           
            for k, v in items.items():
                d += ELUI(self.ins).cart_pro_block(v, delete={"_data": ""})
                if "files_data" in v :
                    files= self.ins._json._decode(v["files_data"])
                    

                    
                    
                    d+=[ {"start": "true", "class": "ins-col-12  ins-border ins-card ins-flex"},]
                    for f in files:
                       
                       
                        name = f["path"].split("/")[-1]
                       
                        dir =  self.ins._map.UPLOADS_FOLDER+ f["path"].replace(name,"")
                       
                       
                        dir = dir.replace("/ins_web/" ,"ins_web/")
                        url = send_from_directory(dir, name)

                       
                        d += [
                        {"_data": f["name"] ,"class":"ins-col-grow"},
                        
                         {"_type": "a", "href": url, "_data": f"<i  class='ins-icons-download  ins-font-3xl'></i>",
                 "class": "ins-flex-center ins-col-1 ins-m-col-1  "},
                    ]
                    d+=[ {"end": "true"}]

                
            footer = [
                {"end": "true"}
            ]
            dataui += header
            dataui += d
            dataui += footer
        dataui += [{"end": "true"}]
        return self.ins._ui._render(dataui)
    
    
    
    def ui(self):
        r = ""
        orders = self.ins._db._get_data(
            "gla_order", "*", f"fk_user_id='{self.__user["id"]}'")
        dataui = [{"start": "true", "class": " ins-container ins-flex"}]
        for o in orders:
            items = self.ins._json._decode(o["items"])
            url = self.ins._server._url({"id": o["order_id"]})
            header = [
                {"start": "true", "class": "ins-col-12 ins-card ins-flex"},
                {"start": "true", "class": "ins-col-12  ins-flex"},
                {"_data": o["kit_created"], "_view": "date",
                    "class": "ins-col-grow"},
                {"_type": "a", "href": url, "_data": f"<i  class='ins-icons-download  ins-font-3xl'></i>",
                 "class": "ins-flex-center ins-col-1 ins-m-col-1  "},
                {"end": "true"}
            ]
            d = []
            for k, v in items.items():
                d += ELUI(self.ins).cart_pro_block(v, delete={"_data": ""})
            footer = [
                {"end": "true"}
            ]
            dataui += header
            dataui += d
            dataui += footer
        dataui += [{"end": "true"}]
        return self.ins._ui._render(dataui)
    def out(self):
        
        self.g=self.ins._server._get()
        r = ""
        self.__user = self.ins._users._session_get()
        
        if "id" in self.g:
            return self.oui()

        else:
            
            return self.ui()
