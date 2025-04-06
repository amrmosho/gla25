from ins_kit._engine._bp import App
class AppPartners(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def header_ui(self,add_filter=False):
        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({}, ["mode", "id", "alias"])
       
        g = self.ins._server._get()

        if "mode" in g:
         partner = self.ins._db._get_row("gla_blog", "title,kit_lang", f"id = '{g['mode']}'",update_lang=True)

         path = [
                {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
                {"_type": "a", "href": home_url, "_data": "Home /","_data-ar":"الرئيسية /","_trans":"true",
                    "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
            ]
         path.append({"_data": "Partners /","_type":"a","href":"/partner","_data-ar":"شركاؤنا / ","_trans":"true",
                            "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
         path.append({"_data": partner["title"],
                            "class": " ins-title-12	ins-grey-color ins-strong-m"})
         path.append({"end": "true"})
         uidata += path
     
        else:
         path = [
                {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
                {"_type": "a", "href": home_url, "_data": "Home /","_data-ar":"الرئيسية /","_trans":"true",
                    "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
            ]
         path.append({"_data": "Partners","_data-ar":"شركاؤنا ","_trans":"true",
                            "class": " ins-title-12	ins-grey-color ins-strong-m"})
         path.append({"end": "true"})
         uidata += path






        uidata.append({"_data": "Our Partners","_data-ar":"شركاؤنا","_trans":"true","class": "ins-col-grow ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"start":"true","class":"ins-col-grow ins-flex-end ins-m-flex-start -filter-area"})
        if add_filter:
            city_area = [
    {"start": "true", "class": "ins-flex-end ins-m-col-6"},
    {"_data": "Area", "_data-ar": "المنطقة", "_trans": "true", "class": "ins-strong-m ins-grey-d-color ins-m-col-2 ins-title-14"},
    {
        "_type": "select",
        "name": "city",
        "fl_data": {
            "all": "All",
            "cairo": "Cairo",
            "heliopolis": "    - Heliopolis",
            "nasr_city": "    - Nasr City",
            "new_cairo": "    - New Cairo",
            "rehab": "    - Al Rehab",
            "mohandeseen": "    - Mohandeseen",
            "tagamoa": "    - Tagamoa",
            "october": "    - 6 October",
            "maadi": "    - Maadi",
            "alexandria": "Alexandria",
            "suez": "Suez",
            "port_said": "Port Said"
        },
        "fl_data-ar": {
            "all": "الكل",
            "cairo": "القاهرة",
            "heliopolis": "    - مصر الجديدة",
            "nasr_city": "    - مدينة نصر",
            "new_cairo": "    - القاهرة الجديدة",
            "rehab": "    - الرحاب",
            "mohandeseen": "    - المهندسين",
            "tagamoa": "    - التجمع",
            "october": " - 6 أكتوبر",
            "maadi": " - المعادي",
            "alexandria": "الإسكندرية",
            "suez": "السويس",
            "port_said": "بور سعيد"
        },
        "_trans": "true",
        "pclass": "ins-col-grow ins-m-col-10",
        "class": "-area-select"
    },
    {"end": "true"}
]



            uidata+=city_area  



        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return uidata
    




    def _ui(self):
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata += self.header_ui(True)
        uidata.append({"end": "true"})
        data = self.ins._db._get_data("gla_blog", "*","fk_blog_category_id = '18'",update_lang=True)
        uidata.append(
            {"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l"})
        p = "/ins_web/ins_uploads/"
        for d in data:
            url = self.ins._server._url({ "mode": str(d["id"])})

            blog = [

                {"_type":"a","href":url,"start": "true", "class": f"ins-flex _{d.get('city')} _{d.get('state')}  pro-partner-block ins-card ins-m-col-12"},
                {"src": p + d["image"],"loading":"lazy", "_type": "img","class":"ins-radius-l"},
                {"_data": d["title"], "class": "ins-col-12 ins-title-s   ins-grey-color ins-strong-m"},
                {"_data": d["content"][:55] + '...' if len(d["content"]) > 55 else d["content"], "class": "ins-col-12 ins-title-s ins-grey-color"},  
                {"_type":"a","end": "true"}

            ]

            uidata += blog

        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
    


    def _partner_ui(self,pid):
        data = self.ins._db._get_row("gla_blog", "*", f"id = '{pid}'")
        p = "/ins_web/ins_uploads/"

        uidata = [{"start": "true", "class": "ins-flex ",
                   "style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto;"}]
        uidata += self.header_ui()
        uidata.append({"end": "true"})
        uidata.append(
            {"start": "true", "class": "ins-flex gla-container ins-padding-2xl ins-col-12 ins-gap-2xl"})
        img = [
            {"start": "true", "class": "ins-flex ins-col-4 ins-m-col-12"},
            {"src": p + data["image"],"loading":"lazy", "class":"-partner-ineer-img","_type": "img",
                "style": "max-width: 350px;"},
            {"end": "true"}
        ]
        uidata += img

        content = [
            {"start": "true", "class": "ins-flex ins-col-7 ins-m-col-12"},
            {"_data": data["title"], "class": "ins-col-12 ins-grey-d-color ins-title-l ins-m-col-12",
                "style": "    line-height: 45px;"},
            {"_data": data["content"], "class": "ins-col-12  ins-m-col-12"},

        ]

        uidata += content
        return self.ins._ui._render(uidata)





    def out(self):
           self.app._include("script.js")
           self.app._include("style.css")

           g = self.ins._server._get()

           if "mode" in g:
            return self._partner_ui(g["mode"])
          
           return self._ui()