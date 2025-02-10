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
            {"_type": "a", "href": home_url, "_data": "Home /",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        path.append({"_data": "Partners",
                        "class": " ins-title-12	ins-grey-color ins-strong-m"})
        path.append({"end": "true"})
        uidata += path
        uidata.append({"_data": "Our Partners",
                      "class": "ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"end": "true"})
        return uidata
    




    def _ui(self):
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata += self.header_ui()
        uidata.append({"end": "true"})
        data = self.ins._db._get_data("gla_blog", "*","fk_blog_category_id = '18'")
        uidata.append(
            {"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l"})
        p = "/ins_web/ins_uploads/"
        for d in data:
            blog = [

                {"start": "true", "class": "ins-flex   pro-partner-block ins-card"},
                {"src": p + d["image"], "_type": "img","class":"ins-radius-l"},
                {"_data": d["title"], "class": "ins-col-12 ins-title-m   ins-grey-color ins-strong-m"},
                {"_data": d["content"], "class": "ins-col-12 ins-title-s   ins-grey-color"},
                {"end": "true"}

            ]

            uidata += blog

        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
    def out(self):
           self.app._include("style.css")
           return self._ui()