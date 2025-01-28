from ins_kit._engine._bp import App


class AppProductTypes(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _subtype(ins,ops,data):
        return "<i data-tid = "f'{data["id"]}'" class='lni lni-layers-1 -show-subtypes-btn ins-button-icon'></i>"
    
    def _parent(ins,ops,data):

        if data["fk_parent_id"] != 0:
            title = ins._db._get_row("gla_product_types", "title", f"id='{data['fk_parent_id']}'")["title"]
        else:
            title = " - "
        return title
    

    


    def _subtypes_ui(self):   
        rq = self.ins._server._post()
        type_data = self.ins._db._get_row("gla_product_types", "*", f"id='{rq['tid']}'")

        uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex"})
        uidata.append({"_data": f"{type_data['title']} types", "class": "ins-title-l ins-col-10"})
        uidata.append({
            "type": "i",
            "class": "ins-col-1 lni lni-close ins-text-right ins-view-close ins-button-text",
            "style": "font-size: 14px"
        })
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-line ins-col-12"})
        uidata.append({
            "class": "-sub-body ins-col-12 ins-flex",
            "_data": self._subtypes_body(rq)
        })
        
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)

    def _subtypes_body(self, rq):
        data = self.ins._db._get_data("gla_product_types", "*", f"fk_parent_id='{rq['tid']}'")
        
   
        
        uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]
        
        if data:
            header = [
            {"_data": "Title", "class": "ins-col-6"},
            {"_data": "Description", "class": "ins-col-6"},
]           
            uidata+=header

            for d in data:
                row = [
                        {"_data": d["title"], "class": "ins-col-6"},
                        {"_data": d["des"], "class": "ins-col-6"}
                ]
                uidata.append({"_data":row,"class":"ins-col-12 ins-flex ins-card"})
            
        else:
            uidata.append({"_data": "There is no data to show", "class": "ins-col-12"})
        
        uidata.append({"end": "true"})
        
        return self.ins._ui._render(uidata)

    def out(self):
        
        self.app._include("script.js")
    
        r = self.ins._apps._crud(properties=self.app._properties)
        return r