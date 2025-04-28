from ins_kit._engine._bp import Widget


class WdgPartner(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        self.widget._include("style.css")

        data = self.ins._db._get_data("cg_blog", "*","fk_blog_category_id='18' LIMIT 6", update_lang=True)
        p = "/ins_web/ins_uploads"
        uidata = [
            {"start":"true","class":"ins-col-12 "},
            {"class":"ins-space-xl "},
            {"start":"true","class":"ins-gap-o  ins-padding-2xl  gla-container ins-flex-space-between"},
            {"_data":"Our Partners","_data-ar":"شركاؤنا","_trans":"true","class":"ins-title-xl ins-grey-d-color ins-strong-m ins-text-upper","style":"margin-right: 16px;"},
        ]


        uidata.append({"start":"true","class":"-part-area ins-m-col-12 ins-m-flex ins-flex"})
        for d in data:
               url = self.ins._server._url({"alias":"partner","mode":str(d["id"])})

               uidata+=[
                      
                      {"_type":"a","href":url,"start":"true","class":"gla-icon-card gla-shadow-s  ins-radius-m ins-white -partner-card"},
                      {"_type":"img","src":f"{p}/{d['image']}","style":"height:100%;"},
                      {"_type":"a","end":"true"}
               ]
        uidata.append({"end":"true"})

        uidata += [
                     
        {"end":"true"},
        {"class":"ins-space-2xl ","style":"border-bottom:1px solid var(--primary)"},
        {"end":"true"}

        ]


        return self.ins._ui._render(uidata)
