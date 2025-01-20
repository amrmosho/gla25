from ins_kit._engine._bp import App
import json


class AppWdgts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    @staticmethod
    def get_id(options, db_data, ins):
        return f"{db_data["id"]}"

    def _menu_data(self):

        g = self.ins._server._req()

        w = f"kit_menu_item.fk_menu_id={
            g["_v"]} and kit_menu_item.fk_menu_item_id='0' "
        q = self.ins._db._get_disabled()._jget("kit_menu_item", "title,id", w)
        q._jwith("kit_menu_item sub", "title,id", fk="fk_menu_item_id" ,join="left join")
        ops = q._jrun()

        t = "<option  name=''></option>"
        
        data ={}
        for f in ops:
            
            if f["id"] not in data:
                data[f["id"]] = {}
                
            data[f["id"]]["id"] = f["id"]

            data[f["id"]]["title"] = f["title"]
            
            if f["sub_id"] != None:
                if "sub" not in data[f["id"]]:
                    data[f["id"]]["sub"]=[]
                
                sub = {"id": f["sub_id"], "title": f["sub_title"] }
                data[f["id"]]["sub"].append(sub)
            
            
        
        for k in data:
            f= data[k]
            m = ""
            if "_mid" in g and g["_mid"] == f["id"]:
                m = "selected ='true' "

            t += f"<option {m} name='{f["id"]}'>{f["title"]}</option>"
            if "sub" in f:
                for sub in f["sub"]:
                    if "_mid" in g and g["_mid"] == sub["id"]:
                        m = "selected ='true' "
                    t += f"<option {m} name='{sub["id"]}'>&nbsp;&nbsp;&nbsp;|--&nbsp;{sub["title"]}</option>"



        r = {}
        r["type_ops"] = t
        return self.ins._json._encode(r)

    def get_pros(self):
        g = self.ins._server._req()
        area_url = self.ins._eng._areas(g["_warea"])["url"]
        url = f"{self.ins._map.WIDGETS_FOLDER}/{g["_type"]}/"
        url = f"{area_url}/{url}"
        ops = {}           
        opsa = {}

        if g["_mode"] == "edit":
            w = f"id={g["_id"]}"
            ops = self.ins._db._get_disabled()._get_row("kit_wdgts", "kit_options", w)
            if ops != False and ops["kit_options"] != "":
                opsa = json.loads(ops["kit_options"])

        properties = self.ins._eng._pros("properties", url)
        if "options" in properties:
            options: list = properties["options"]

            for o in options:
                if  o["name"] in opsa:
                    o["value"] = opsa[o["name"]]
                o["name"] = "options@" + o["name"]

            return self.ins._ui._render(options)

        else:
            return ""

    def get_src_data(self):

        a = self.ins._server._req("_v")
        type = self.ins._server._req("_type")

        area = self.ins._eng._areas(a)["url"]

        ls = self.ins._files._list_folders_with_prefix(
             f"./{area}/ins_wdgts", "wdg")
        t = "<option  name=''></option>"
        for f in ls:
            m = ""
            if type == f:
                m = "selected ='true' "

            t += f"<option {m} name='{f}'>{f}</option>"

        r = {}
        r["type_ops"] = t
        return self.ins._json._encode(r)

    def out(self):

        self.app._include("script.js")

        ops = self.ins._apps._crud_ops

        def func(data: dict):

            options = {}
            for k in data.keys():
                if "options@" in k:
                    tk = k.split("@")
                    options[tk[1].strip()] = data[k]

            if len(options) > 0:
                data["kit_options"] = self.ins._json._encode(options)

            return data

        ops._form_befor_insert = func
        ops._form_befor_update = func

        r = self.ins._apps._crud(ops, properties=self.app._properties)
        return r
