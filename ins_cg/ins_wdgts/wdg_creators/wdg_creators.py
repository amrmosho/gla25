from ins_kit._engine._bp import Widget


class WdgCreators(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        self.widget._include("style.css")

        data = self.ins._db._get_data("kit_user", "*","1 LIMIT 4", update_lang=True)
        p = self.ins._map.UPLOADS_FOLDER
        uidata = [
            {"start":"true","class":"ins-padding-xl ins-col-12 ins-flex-center ins-gap-20  ins-secondary"},
        ]


        for d in data:
                url = self.ins._server._url({"alias":"products","mode":"user","id":d.get("id")})

                uidata+=[
                      
                      {"_type":"a","href":url,"start":"true","class":"ins-button-text ins-flex-center -creator-card"},
                      {"_type":"img","src":f"{p}/{d['image']}","style":"height:100%;","class":"ins-rounded ins-col-12"},
                      {"_data":d.get("title"),"class":"ins-col-12"},
                      {"_type":"a","end":"true"}
               ]

        uidata += [
                     
        {"end":"true"}

        ]


        return self.ins._ui._render(uidata)
