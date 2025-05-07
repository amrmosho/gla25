from ins_kit._engine._bp import Widget


class WdgCategory(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        
        data = self.ins._db._get_data("gla_product_category","*")
        p = self.ins._map.UPLOADS_FOLDER
        self.widget._include("leg.css")
        self.widget._include("leg.js")
        uidata = [{"start":"true","class":"gla-container  -pro-all"},
                  {"start":"true","class":" ins-flex -pro-cont"},
                  {"start":"true","class":"ins-flex-center -pro-cats-row ins-padding-xl"}

                  
                  ]


        for d in data:
            url = self.ins._server._url({"alias":"products","mode":"3d-model","id":d.get("alias")})
            cblock = [{"_type":"a","href":url,"start":"true","class":"   ins-card img-card  -pro-cats-item  ins-padding-s ins-flex-center "},
                     {"_type": "img", "src": p + d.get("image"), "loading": "lazy"},
                     {"_data": d.get("title"),"class":" ins-padding-l ins-col-12 ins-object-bottom   ins-strong ins-title-s  "},
                     {"_type":"a","end":"true"}]
            uidata +=cblock

        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
                  


                  
                  
                  
        return self.ins._ui._render(uidata)
