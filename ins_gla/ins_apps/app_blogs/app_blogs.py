from datetime import date, datetime
from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App


class AppBlogs(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def header_ui(self):

        self.app._include("script.js")



        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({}, ["mode", "id", "alias"])

        path = [
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": home_url, "_data": "Home /","_data-ar":"الرئيسية /","_trans":"true",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        rq = self.ins._server._req()

        if "mode" in rq and rq["mode"] == "blog":
            blogs_url = self.ins._server._url({}, ["mode", "id"])
            title = self.ins._db._get_row(
                "cg_blog", "title,kit_lang", f"id={rq['id']}",update_lang=True)
            path.append({"_data": "Media & News","_data-ar":"أحدث الأخبار","_trans":"true", "_type": "a", "href": blogs_url,
                        "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
            path.append(
                {"_data": " / "+title["title"], "class": " ins-title-12	ins-grey-color ins-strong-m"})

        else:
            path.append({"_data": "Media & News","_data-ar":"أحدث الأخبار","_trans":"true",
                        "class": " ins-title-12	ins-grey-color ins-strong-m"})

        path.append({"end": "true"})

        uidata += path

        uidata.append({"_data": "Media / News","_data-ar":"أحدث الأخبار","_trans":"true",
                      "class": "ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})

        # checkout steps

        uidata.append({"end": "true"})
        return uidata

    def _ui(self):

        data = self.ins._db._get_data("cg_blog", "*"," fk_blog_category_id <>'18'",update_lang=True)
        p = "/ins_web/ins_uploads/"
        uidata = [{"start": "true", "class": "ins-flex ",
                   "style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata += self.header_ui()
        uidata.append({"end": "true"})

        uidata.append(
            {"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l ins-m-col-12"})

        for d in data:
            st = "width:316px;margin-bottom: 32px;"
            burl = self.ins._server._url({"mode": "blog", "id": d["id"]})
            turl = d["link"]
            blog = [

                {"_type": "a", "href": burl,"start": "true", "class": "ins-flex   pro-blog-block ins-m-col-12", "style": st},
                { "_type": "a","src": p + d["image"],"loading":"lazy", "_type": "img","href": turl, "target": "_blank",},
                {"_data": d["title"], "class": "ins-col-12 ins-title-m   ins-grey-color"},

                {"_type": "a", "end": "true"}

            ]

            uidata += blog

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)

    def blog_ui(self, rq):
        bdata = self.ins._db._get_row("cg_blog", "*", f"id={rq['id']} ",update_lang=True)
        p = "/ins_web/ins_uploads/"

        uidata = [{"start": "true", "class": "ins-flex ",
                   "style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata += self.header_ui()
        uidata.append({"end": "true"})
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
        return self.ins._ui._render(uidata)

    def out(self):
        rq = self.ins._server._req()
        self.app._include("style.css")

        if "mode" in rq and rq["mode"] == "blog":
            return self.blog_ui(rq)
        else:
            return self._ui()
