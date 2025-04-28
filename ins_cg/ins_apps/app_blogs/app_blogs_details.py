from ins_cg.ins_kit._elui import ELUI
from ins_kit._engine._bp import App


class AppBlogsDetails(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _blog_body(self, bdata):
        p = self.ins._map.UPLOADS_FOLDER
        uidata = [
            {"start": "true", "class": "ins-flex gla-container ins-padding-2xl ins-col-12 ins-gap-2xl"},
            {"start": "true", "class": "ins-flex ins-col-4"},
            {"_type": "img", "src": p + bdata["image"], "loading": "lazy", "style": "width:100%;"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex ins-col-7"},
            {"_data": bdata["title"], "class": "ins-col-12 ins-grey-d-color ins-title-l", "style": "line-height: 45px;"},
            {"_data": bdata["content"], "class": "ins-col-12"}
        ]
        if "link" in bdata and bdata["link"]:
            uidata.append({"_type": "a", "_data": "Read More", "_data-ar": "معرفة المزيد", "_trans": "true", "href": bdata["link"], "target": "_blank", "class": "ins-col-12 ins-flex-end ins-gold-d-color ins-title-s"})
        uidata.append({"end": "true"})
        return uidata

    def _ui(self):
        rq = self.ins._server._get()
        bdata = self.ins._db._get_row("cg_blog","*",f"alias='{rq['id']}'",update_lang=True)
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata +=  ELUI(self.ins).page_title("Media / News","أحدث الأخبار", [{"_data": "Media & News /", "href": "/blogs","_data-ar":"أحدث الأخبار /","_trans":"true"},{"_data": bdata.get("title","")}],string=True)

        uidata.append({"end": "true"})
        uidata.append({"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l ins-m-col-12 ins-flex-valign-start -blogs-area"})
        uidata +=self._blog_body(bdata)
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)

    def out(self):
        return self._ui()
