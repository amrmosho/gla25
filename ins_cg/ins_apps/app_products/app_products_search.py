import json
from ins_cg.ins_apps.app_products.app_product_details import AppProductDetails
from ins_cg.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from urllib.parse import parse_qs
import math


class AppProductsSearch(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def data(self):
        g = self.ins._server._get()
        self._category = self.ins._db._get_row(
            "gla_product_category", "*", f"alias='{g["id"]}'", update_lang=True)

    def order(self):

        uidata = [{"start": "true", "class": "ins-col-12 ins-flex"},
                  {"class": "ins-font-xl ins-m-col-1  not-for-web lni lni-funnel-1 -filter-menu"}]

        vorder = "low"

        order_area = [
            {"start": "true", "class": "ins-col-grow ins-flex-end ins-m-flex-start -filter-results-area"},
            {"start": "true", "class": "ins-flex-end ins-m-col-6 ins-m-flex-start"},
            {"_data": "Order by",  "_data-ar": "ترتيب حسب", "_trans": "true",
                "class": "ins-strong-m ins-grey-d-color ins-title-14 ins-m-col-grow"},
            {"_type": "select", "name": "order", "fl_data": {
                "low": "Lowest to Highest",
                "high": "Highest to Lowest",
                "old": "Oldest to Newest",
                "new": "Newest to Oldest"
            }, "fl_data-ar": {
                "low": "من الارخص للأغلى",
                "high": "من الأغلى للأرخص",
                "old": "من الأقدم للأجدد",
                "new": "من الأجدد للأقدم"
            }, "_trans": "true", "value": vorder, "pclass": "ins-col-grow ins-m-col-7", "class": "-order-select"},
            {"end": "true"}
        ]

        uidata += order_area

        uidata += [{"end": "true"}, {"end": "true"}, {"end": "true"}]
        return uidata

    def filter(self):
        type = {"-": "File Format"}
        exts = self.ins._json._file_read("ins_langs/file_ext.json")

        for k in exts:
            if k != "textures":
                type[k] = exts[k]["title"]

        uidata = [

            {"_type": "select", "fl_data": type,"name":"format",
             "pclass": "ins-col-grow"},
            {"_type": "select", "name": "order",
                "fl_data": {"-": "Price"}, "pclass": "ins-col-2"},


            {"_type": "input", "_end": "3D print", "type": "bool",
                "pstyle": "width:150px" ,"name":"print"},
            {"_type": "input", "_end": "Animated", "type": "bool",
                 "pstyle":  "width:150px" ,"name":"animated"},
            {"_type": "input", "_end": "PBR", "type": "bool" ,"class":"fliter-pbr","name":"pbr",
                 "pstyle":  "width:150px"},
            {"_type": "input", "_end": "Rigged", "type": "bool",
                "pstyle":  "width:150px" ,"name":"rigged"},
            {"_type": "input", "_end": "Low poly", "type": "bool",
                 "pstyle":  "width:170px" ,"name":"low_poly"},


            {"class": "ins-flex "}]
        return uidata

    def header_ui(self):

        home_url = self.ins._server._url({}, ["mode", "id", "alias", "filter"])
        uidata = [
            {"start": "true", "class": "ins-flex ins-col-12 gla-container ins-padding-2xl"},
            # title
            {"_data": f"Products / {self._category['title']}", "_data-ar": "منتجات", "_trans": "true",
             "class": "ins-col-12 ins-title ins-strong-m ins-text-upper ins-grey-d-color"},
            # des

            {"_data": f" {self._category['des']}", "_data-ar": "منتجات", "_trans": "true",
             "class": "ins-col-12   ins-grey-d-color"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": home_url, "_data": "Home /", "_data-ar": "الرئيسية /",
                "_trans": "true", "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "3D models", "_data-ar": "المنتجات", "_trans": "true",
                "class": " ins-title-12	ins-grey-color ins-strong-m"},

            {"class": "ins-col-grow "},

            {"_data": self.order(), "class": "ins-flex  "},



            {"_data": self.filter(), "class": "ins-flex ins-col-12 -list-filter-ui "},

            {"end": "true"},



            {"end": "true"}

        ]

        return uidata

    def _products_data(self):

        p = self.ins._server._post()
        items_per_page = 24
        page = int(p.get("page", "1"))
        o = p.get("order", "")
        fdata = ["pbr", "rigged" ,"print" ,"animated"]

        sql_query = " 1 "
        for f in fdata:
            if f in p:
                sql_query += f" and  {f}='{p[f]}'"

        offset = (page - 1) * items_per_page

        order = "order by price asc"
        if o:
            if o == "old":
                order = "order by id asc"
            elif o == "new":
                order = "order by id desc"
            elif o == "high":
                order = "order by price desc"
            elif o == "trend":
                order = "order by kit_order desc"

        rpdata = self.ins._db._get_data(
            "gla_product", "*", f"{sql_query} {order} limit {offset}, {items_per_page}", update_lang=True)

        tcount = self.ins._db._get_row(
            "gla_product", "count(id) as count", f"{sql_query}")["count"]
        self.num_pages = math.ceil(tcount / items_per_page)
        return rpdata

    def _products_ui(self):
        p = self.ins._server._post()

        current_page = 1


        rpdata = self._products_data()
        start_page = max(1, current_page - 2)
        end_page = min(self.num_pages, current_page + 2)

        if rpdata:
            uidata = []
            for d in rpdata:
                uidata += ELUI(self.ins).shop_pro_block(d,
                                                        f"/product/product/{d['id']}")

            uidata += [
                {"class": "ins-space-xl"},
                {"start": "true", "data-page":p.get("page", "1") , "class": "ins-flex ins-col-12  ins-m-flex-center ins-pagination-area ins-padding-l ins-m-col-12",
                 "style": "background:white;"},
                {"start": "true", "class": "ins-flex-start ins-m-col-12 ins-m-flex-center -pro-pages-buttons"},
                {"_type": "button", "class": "ins-pagination-btn", "data-page": "prev",
                 "_data": f"<i class='lni lni-chevron-left' ></i>"}
            ]


            for page in range(start_page, end_page + 1):
                active_class = "active" if page == current_page else ""
                uidata += [{"_type": "button", "class": f"ins-pagination-btn ins-m-flex-center {active_class}",
                            "data-page": page, "_data": str(page)}]

            uidata += [

                {"_type": "button", "class": "ins-pagination-btn","data-page": "next",
                 "data-tpages": self.num_pages, "_data": f"<i class='lni lni-chevron-left'></i>"},
                {"end": "true"},
                {"class": "ins-col-grow ins-m-col-3"},
                {"start": "true", "class": "ins-flex-end not-for-phone"},
                {"_data": "Go to page", "_data-ar": "انتقل إلى الصفحة",
                 "_trans": "true", "class": "ins-title-12 ins-grey-m-color ins-m-col-3"},
                {"_type": "input", "type": "text",
                 "class": "-page-input ins-radius-s ins-white ins-text-center", "pclass": "ins-col-2 ins-m-col-2"},
                {"_data": "Go <i class='lni lni-chevron-left' style='rotate:180deg'></i>", "_data-ar": "انتقل",
                 "_trans": "true", "data-tpages": self.num_pages, "class": "ins-title-14 -go-to-page-btn ins-grey-color ins-button-text"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},
                {"class": "ins-space-xl"}
                
                ]

        else:
            uidata = [{"_data": "No matching results found",
                      "_data-ar": "لا توجد نتائج مطابقة", "_trans": "true", "class": "ins-col-12 ins-card ins-text-center"}]

        return self.ins._ui._render(uidata)

    def _list(self):

        uidata = [
            {"class": "ins-flex -header-area", "_data": self.header_ui(),
             "style": "background:white;position: relative;    border-bottom: 1px solid var(--grey-l); "},
            {"_data": self._products_ui(), "class": "ins-flex-valign-start -products-area   gla-container ins-col-12  ins-m-flex-center"}]
        return self.ins._ui._render(uidata)

    def out(self):
        self.data()

        return self._list()
