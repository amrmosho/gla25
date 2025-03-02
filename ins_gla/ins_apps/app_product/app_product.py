import json
from uuid import uuid4
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
    def _price(ins,options,data):
        uidata=[
        {"_data": str(data["price"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card ins-title-center ins-col-5 ins-flex-center ins-padding-l ins-padding-h ins-text-center",},
        {"_data": str(data["buy_price"])+" EGP",  "style" :"border:solid 2px #12437D" ,"class" : " ins-card  ins-col-5 ins-title-center ins-flex-center ins-padding-l ins-padding-h ins-text-center",},

        ]
        return ins._ui._render(uidata)
    def _stamp(ins,options,data):
        total = data["stamp"] + data["vat"]

        uidata=[
        {"_data": str(total),"style" :"background: #C4B293; color: white;" ,"class" : "  ins-card  ins-col-12 ins-title-center ins-flex-center ins-padding-l ins-padding-h ins-text-center",},

        ]
        return ins._ui._render(uidata)
        
    def _remove_item(self):

        rq = self.ins._server._req()
        uid = rq.get("uid")

        if not uid:
            return ""
        data = {}
        if "area" in rq and rq["area"]: 
            try:
                data = json.loads(rq["area"])
            except json.JSONDecodeError:
                pass
        for parent_alias, parent_data in list(data.items()):
            if "data" not in parent_data:
                continue
            subtypes_to_delete = [
                st for st, st_data in parent_data["data"].items()
                if isinstance(st_data, dict) and st_data.get("uid") == uid
            ]
            for st in subtypes_to_delete:
                parent_data["data"].pop(st, None)
            if not parent_data["data"]:
                data.pop(parent_alias, None)
        return json.dumps(data)


    def _update_product_type(self):
        rq = self.ins._server._req()
        data = {}
        if "area" in rq and rq["area"]:
            try:
                data = json.loads(rq["area"])
            except json.JSONDecodeError:
                pass

        uid = rq.get("uid")
        subtype_alias = rq.get("subtype")
        if not uid or not subtype_alias:
            return json.dumps(data)

        parents_to_delete = []
        for parent_alias, parent_data in list(data.items()):
            if "data" not in parent_data:
                continue
            subtypes_to_delete = [
                st for st, st_data in parent_data["data"].items()
                if isinstance(st_data, dict) and st_data.get("uid") == uid
            ]
            for st in subtypes_to_delete:
                parent_data["data"].pop(st, None)
            if not parent_data["data"]:
                parents_to_delete.append(parent_alias)
        for parent in parents_to_delete:
            data.pop(parent, None)
        try:
            new_subtype_data = self.ins._db._get_row(
                "gla_product_types",
                "title,alias,id,des,fk_parent_id",
                f"alias='{subtype_alias}' and fk_parent_id <> 0"
            )
            new_parent_data = self.ins._db._get_row(
                "gla_product_types", 
                "title,alias,id,des",
                f"id={new_subtype_data['fk_parent_id']}" if new_subtype_data else "1=0"
            )
        except Exception:
            return json.dumps(data)

        if not new_parent_data or not new_subtype_data:
            return json.dumps(data)
        new_parent_alias = new_parent_data["alias"]
        parent_entry = data.setdefault(new_parent_alias, {
            "title": new_parent_data["title"],
            "alias": new_parent_alias,
            "id": new_parent_data["id"],
            "des": new_parent_data["des"],
            "data": {}
        })
        subtype_entry = parent_entry["data"].get(subtype_alias, {})
        subtype_entry.update({
            "title": new_subtype_data["title"],
            "alias": subtype_alias,
            "id": new_subtype_data["id"],
            "des": new_subtype_data["des"],
            "fk_parent_id": new_subtype_data["fk_parent_id"],
            "uid": uid,
           "images" : rq.get("images",""),
           "order" : rq.get("order",""),
           "label" : rq.get("label","")
        })
        parent_entry["data"][subtype_alias] = subtype_entry

        return json.dumps(data)
    

    def _fill_subtype_area(self):

        id = self.ins._server._req("pid")
        if not id:
            return ""   
        uidata = []
        data = self.ins._db._get_row("gla_product", "types_data", f"id={id}")
        if data:
            jdata = json.loads(data["types_data"])
            for kp, vp in jdata.items():
                for k, v in vp["data"].items():
                    uidata+= [
                {"start":"true","class":"ins-col-12 ins-flex ins-padding-m -subtypes-row ins-card ins-padding-l","data-uid":v.get("uid")},
                {
                "name": "types",
                "title": "Product Types",
                "_type": "select",
                "_view": "select",
                "fl_type": "db",
                "fl_table": "gla_product_types",
                "fl_value": "alias",
                "fl_text": "title",
                "required": "true",
                "fl_query": "Select * From gla_product_types where fk_parent_id <> 0 ",
                "pclass": "ins-col-2",
                "class": "-types-select",
                "value": k
            },
            {"_type": "input", "type": "upload", "class":"-upload-image","value":v.get("images"),
             "title": "multi  images Upload","nojs":"true", 
             "name": "_unname", "placeholder": 
             "_add placeholder hear", "pclass": "ins-col-6 ",
               "required": "true", "_dir": "test", "_mode": "multi",
                 "_exts": "image/png"},
                 {"_type":"input","type":"number","value":v.get("order") ,"name":"order","title":"Order","placeholder":"Order","pclass":"ins-col-1","required":"true","class":"-order-inpt"},
                 {"_type":"select","value":v.get("label") ,"name":"label","title":"Label","fl_data":{"":"-","best_seller":"Bestseller","new":"New"},"placeholder":"Label","pclass":"ins-col-2","class":"-label-select"},
                 {"data-uid":v.get("uid"),"class":"ins-button-icon ins-col-1 lni lni-xmark -remove-item ins-danger ins-font-xl","style":"    position: relative;top: 15px;"}
            ,{"end":"true"}
            ,{"class":"ins-space-l"}


                    ]
                    
            r = {}

            r["textarea"] = data["types_data"]
            r["ui"] = self.ins._ui._render(uidata)
        else:
            r = {}
            r["textarea"] = ""
            r["ui"] = self._add_new_item()
        return r


        


    def _add_new_item(self):
        uid = uuid4().hex
        uidata = [
            {"start":"true","class":"ins-col-12 ins-flex ins-padding-m -subtypes-row ins-card ins-padding-l","data-uid":uid},
  {
            "name": "types",
            "title": "Product Types",
            "_type": "select",
            "_view": "select",
            "fl_type": "db",
            "fl_table": "gla_product_types",
            "fl_value": "alias",
            "fl_text": "title",
            "required": "true",
            "fl_query": "Select * From gla_product_types where fk_parent_id <> 0 ",
            "pclass": "ins-col-2",
            "class": "-types-select"
        },
{"_type": "input", "type": "upload", "class":"-upload-image",
 "title": "multi  images Upload","nojs":"true", 
 "name": "_unname", "placeholder": 
 "_add placeholder hear", "pclass": "ins-col-6 ",
   "required": "true", "_dir": "test", "_mode": "multi",
     "_exts": "image/png"},
     {"_type":"input","type":"number","name":"order","title":"Order","placeholder":"Order","pclass":"ins-col-1","required":"true","class":"-order-inpt"},
      {"_type":"select","name":"label","title":"Label","fl_data":{"":"-","best_seller":"Bestseller","new":"New"},"placeholder":"Label","pclass":"ins-col-2","class":"-label-select"},

     {"data-uid":uid,"class":"ins-button-icon ins-col-1 lni lni-xmark -remove-item ins-danger ins-font-xl","style":"    position: relative;top: 15px;"}
,{"end":"true"}
,{"class":"ins-space-l"}


                ]
        
        return self.ins._ui._render(uidata)
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")

        r = self.ins._apps._crud(properties=self.app._properties)

        return r
