from ins_kit._engine._bp import App


class AppBlogsDetails(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def header_ui(self,bdata):
        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({}, ["mode", "id", "alias"])
        blogs = self.ins._server._url({"alias":"blogs"}, ["mode", "id"])
        path = [
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": home_url, "_data": "Home /","_data-ar":"الرئيسية /","_trans":"true",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        path.append({"_type": "a", "href": blogs,"_data": "Media & News /","_data-ar":"أحدث الأخبار","_trans":"true",
                                        "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
        
        path.append({"_data": bdata.get("title"),"class": " ins-title-12	ins-grey-d-color ins-strong-m"})

        path.append({"end": "true"})
        uidata += path
        uidata.append({"_data": "Media / News","_data-ar":"أحدث الأخبار","_trans":"true",
                      "class": "ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"end": "true"})
        return uidata


    def _blog_body(self,bdata):
        p = self.ins._map.UPLOADS_FOLDER

        uidata = []
        uidata.append(
            {"start": "true", "class": "ins-flex gla-container ins-padding-2xl ins-col-12 ins-gap-2xl"})
        img = [
            {"start": "true", "class": "ins-flex ins-col-4"},
            {"src": p + bdata["image"],"loading":"lazy", "_type": "img",
                "style": "width:100%;"},
            {"end": "true"}
        ]
        uidata += img

        content = [
            {"start": "true", "class": "ins-flex ins-col-7"},
            {"_data": bdata["title"], "class": "ins-col-12 ins-grey-d-color ins-title-l",
                "style": "    line-height: 45px;"},
            {"_data": bdata["content"], "class": "ins-col-12 "},

        ]

        uidata += content
        if "link" in bdata and bdata["link"]:
            uidata.append(
                            {"_data": "Read More","_data-ar": "معرفة المزيد","_trans": "true", "_type": "a", "target":"_blank","href": bdata["link"], "class": "ins-col-12 ins-flex-end ins-gold-d-color ins-title-s"},
)
        uidata.append({"end": "true"})
        return uidata






    def _ui(self):
        rq = self.ins._server._get()
        bdata = self.ins._db._get_row("cg_blog","*",f"alias='{rq['id']}'",update_lang=True)
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata += self.header_ui(bdata)
        uidata.append({"end": "true"})
        uidata.append({"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l ins-m-col-12 ins-flex-valign-start -blogs-area"})
        uidata +=self._blog_body(bdata)
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)


    def out(self):
       return self._ui()
