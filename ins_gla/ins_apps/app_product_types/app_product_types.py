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
        title = self.ins._db._get_row("gla_product_types", "title", f"id='{rq['tid']}'")["title"]
        data = self.ins._db._get_data("gla_product_types", "*", f"fk_parent_id='{rq['tid']}'")


        uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]
        uidata.append({"_data": f"{title} types", "class": "ins-title-l ins-col-11"})
        uidata.append({"type": "i","class": "lni lni-xmark ins-text-right ins-view-close ins-button-text-danger ins-title-20	"})
        
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex"})
        uidata.append({"class": "ins-space-m"})

        if data:
            header = [
                {"_data": "Title", "class": "ins-col-6"},
            {"_data": "Description", "class": "ins-col-6"}]           
            uidata+=header

            for d in data:
                row = [
                        {"_data": d["title"], "class": "ins-col-6"},
                        {"_data": d["des"], "class": "ins-col-6"}
                ]
                uidata.append({"_data":row,"class":"ins-col-12 ins-flex ins-card"})
            
        else:
            uidata.append({"_data": "There is no data to show", "class": "ins-col-12 ins-flex ins-card ins-flex-center"})
        
        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)

    def out(self):
        
        self.app._include("script.js")
        self.app._include("style.css")
    
        r = self.ins._apps._crud(properties=self.app._properties)
        return r