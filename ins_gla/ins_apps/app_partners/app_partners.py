from ins_kit._engine._bp import App
class AppPartners(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def header_ui(self):
        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({}, ["mode", "id", "alias"])
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
        uidata.append({"start":"true","class":"ins-col-grow ins-flex-end"})

        city_area = [
                {"start":"true","class":" ins-flex-end"},
                {"_data":"Area",  "_data-ar":"المنطقة","_trans":"true","class":"ins-strong-m ins-grey-d-color ins-title-14"},
                {"_type":"select","name":"city","fl_data":{
                    "all":"All",
                    "cairo":"Cairo",
                    "october":"    - 6 October",
                    "maadi":"    - Maadi",
                    "alexandria":"Alexandria"
                },"fl_data-ar":{
                     "all":"الكل",
                    "cairo":"القاهرة",
                    "october":" - 6 أكتوبر",
                    "maadi":" - المعادي",
                    "alexandria":"الأسكندرية"
                },"_trans":"true","pclass":"ins-col-grow","class":"-area-select"},
                {"end":"true"}
            ]


        uidata+=city_area  



        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return uidata
    




    def _ui(self):
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata += self.header_ui()
        uidata.append({"end": "true"})
        data = self.ins._db._get_data("gla_blog", "*","fk_blog_category_id = '18'",update_lang=True)
        uidata.append(
            {"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l"})
        p = "/ins_web/ins_uploads/"
        for d in data:
            blog = [

                {"start": "true", "class": f"ins-flex _{d.get("city")} _{d.get("state")}  pro-partner-block ins-card"},
                {"src": p + d["image"],"loading":"lazy", "_type": "img","class":"ins-radius-l"},
                {"_data": d["title"], "class": "ins-col-12 ins-title-m   ins-grey-color ins-strong-m"},
                {"_data": d["content"], "class": "ins-col-12 ins-title-s   ins-grey-color"},
                {"end": "true"}

            ]

            uidata += blog

        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
    def out(self):
           self.app._include("script.js")
           self.app._include("style.css")
           return self._ui()