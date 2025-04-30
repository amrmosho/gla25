import math
from ins_cg.ins_apps.app_blogs.app_blogs_details import AppBlogsDetails
from ins_cg.ins_kit._elui import ELUI
from ins_kit._engine._bp import App


class AppBlogs(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def _blogs_area(self):
        p = self.ins._map.UPLOADS_FOLDER
        rq = self.ins._server._get()
        page = int(rq.get("page", 1))
        filter = rq.get("mode")
        sql = "1 "

        if filter:
            sql = f"category.alias = '{filter}'"
       
        total_blogs = self.ins._db._jget("cg_blog", "count(cg_blog.id) as count", sql)
        total_blogs._jwith("cg_blog_category category", "id", rfk="fk_blog_category_id", join="left join")
        total_blogs = total_blogs._jrun()[0]["count"]
       
        per_page = 3
       
        num_pages = math.ceil(total_blogs / per_page)
       
        offset = (page - 1) * per_page
       
        sql += f" limit {offset},{per_page}"
        
        data = self.ins._db._jget("cg_blog", "*", sql)
        data._jwith("cg_blog_category category", "title,alias", rfk="fk_blog_category_id", join="left join")
        blogs = data._jrun()
       
        uidata = []
       
        uidata.append({"start": "true", "class": "ins-col-7 ins-flex"})

        if blogs:
            for blog in blogs:
                blog_url = self.ins._server._url({"mode": "blog", "id": blog["alias"]},["page","category"])
                uidata += [
                    {"start": "true", "class": "ins-col-12 ins-flex"},
                    {"_type":"a", "href": blog_url,"_data": blog.get("title"), "class": "ins-col-12 ins-title-l ins-strong"},
                    {"class": "ins-line ins-col-12"},
                    {"_data": str(blog.get("kit_created")) + ",", "class": "ins-title-xs ins-grey-m-color"},
                    {"_data": blog.get("category_title"), "class": "ins-title-xs ins-grey-m-color ins-primary-color ins-underline"},
                    {"start": "true", "class": "ins-col-12 ins-flex ins-flex-valign-start"},
                    {"_type": "img", "src": p + blog.get("image"), "loading": "lazy", "class": "ins-col-4"},
                    {"_data": blog.get("content"), "class": "ins-title-xs ins-col-8"},
                    {"end": "true"},
                    {"end": "true"},
                    {"class": "ins-space-3xl"},
                ]

          
        else:
            uidata.append({"class": "ins-col-12 ins-flex ins-card ins-padding-l ins-text-center","_data":"There is no data to show"})

        uidata.append({"end": "true"})
        uidata += [
            {"start": "true", "class": "ins-col-4 ins-flex-end"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-card ins-padding-xl"},
        ]
        categories = self.ins._db._get_data("cg_blog_category", "title,id,alias")
        for cat in categories:
            if filter and cat["alias"] == filter:
                uidata.append({
                    "_type": "input","checked":"checked", "type": "checkbox", "name": "type",
                    "data-alias": cat["alias"], "_end": cat["title"],
                    "class": "-category-checkbox", "pclass": "ins-col-12 ins-m-col-4 -product-list-chkbox",
                    "style": "width: 20px;"
                })
            else:
                    uidata.append({
                    "_type": "input", "type": "checkbox", "name": "type",
                    "data-alias": cat["alias"], "_end": cat["title"],
                    "class": "-category-checkbox", "pclass": "ins-col-12 ins-m-col-4 -product-list-chkbox",
                    "style": "width: 20px;"
                })
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-xl"})
        uidata += [
            {"start": "true", "class": "ins-flex ins-col-12 ins-m-flex-center ins-pagination-area ins-padding-l ins-m-col-12", "style": "background:white;"},
            {"start": "true", "class": "ins-flex-center ins-m-col-12 ins-m-flex-center -pro-pages-buttons ins-col-12"},
            {"_type": "button", "class": "ins-pagination-btn", "data-page": "prev", "_data": "<i class='lni lni-arrow-left'></i>"},
        ]
        start_page = max(1, page - 2)
        end_page = min(num_pages, page + 2)
        for pnum in range(start_page, end_page + 1):
            is_active = "ins-active" if pnum == page else ""
            uidata.append({
                "_type": "button",
                "class": f"ins-pagination-btn ins-m-flex-center {is_active}",
                "data-page": pnum,
                "_data": str(pnum),
            })
        uidata += [
            {"_type": "button", "class": "ins-pagination-btn", "data-page": "next", "data-tpages": num_pages, "_data": "<i class='lni lni-arrow-right'></i>"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
        ]
        return uidata


    def _ui(self):
        uidata = [{"start": "true", "class": "ins-flex ","style": "background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l);height:auto; "}]
        uidata += ELUI(self.ins).page_title("Media / News","أحدث الأخبار", [{"_data": "Media & News ", "href": "/blogs","_data-ar":"أحدث الأخبار /","_trans":"true"}],string=True)
        uidata.append({"end": "true"})
        uidata.append({"start": "true", "class": "ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l ins-m-col-12 ins-flex-valign-start -blogs-area"})
        uidata +=self._blogs_area()
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)

    def out(self):
        rq = self.ins._server._req()
        self.app._include("style.css")
        self.app._include("script.js")
        if not "mode" in rq or rq["mode"] != "blog":
         return self._ui()
        else:
            app = AppBlogsDetails(self.app)
            return app.out()

