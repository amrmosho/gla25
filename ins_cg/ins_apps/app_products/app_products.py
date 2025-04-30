import json
from ins_cg.ins_apps.app_products.app_product_details import AppProductDetails
from ins_cg.ins_apps.app_products.app_products_search import AppProductsSearch
from ins_cg.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from urllib.parse import parse_qs
import math


class AppProducts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    @property
    def session_name(sel):
        return "glaproducts"



    def _call_search(self):
        q = self.ins._server._post()


        return eval(f"AppProductsSearch(self.app).{q["get"]}()")


    def _filter_redirect(self):
        rq = self.ins._server._post()
        if "type" in rq and rq["type"] == "reset":
            return "/product/"

        if rq.get("order") and rq.get("sql"):
            url = f'/product/do/filter/{rq["sql"]}/order/{rq["order"]}'

        elif rq.get("order") and not rq.get("sql"):
            url = f'/product/do/order/{rq["order"]}'

        else:
            url = f'/product/do/filter/{rq["sql"]}'

        return url

    def _pro_action(self):
        app = AppProductDetails(self.app)
        return app._pro_action()

    def _filter_redirect_inner(self):
        rq = self.ins._server._post()
        if "type" in rq and rq["type"] == "reset":
            return "/product/"
        url = f'/product/product/{rq["pid"]}/do/type/{rq["sql"]}'
        return url

    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata = self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"])
        self.ins._server._set_session(self.session_name, sedata)
        ndata = self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"

        count = 0
        if ndata:
            for _, s in ndata.items():
                count += int(s["count"])
        r["count"] = str(count)

        if not ndata:
            uidata = [{"_data": "There is no items in cart",
                       "class": "ins-col-12 ins-card ins-secondary ins-text-upper ins-text-center ins-title-12"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)
        return r

    def _cart_lightbox_ui(self):
        return ELUI(self.ins)._cart_lightbox_ui(True)


    def _filter(self):
        rq = self.ins._server._post()
        return rq

    def _show_subtypes_inner(self):

        rq = self.ins._server._post()

        pdata = self.ins._db._get_row(
            "gla_product", "types_data", f"id='{rq['pid']}'")["types_data"]

        types_data = json.loads(pdata)

        subtypes = types_data[rq["name"]]["data"]
        subtypes = {k: v for k, v in sorted(
            subtypes.items(), key=lambda item: int(item[1].get("order", float('1'))))}

        if subtypes:
            uidata = [
                {"start": "true", "class": "ins-flex ins-col-12"},
                {"_data": "Subtype", "_data-ar": " نوع فرعي", "_trans": "true",
                    "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            i = 0
            for v, s in subtypes.items():
                sdata = self.ins._db._get_row(
                    "gla_product_types", "title,kit_lang", f"alias='{v}'", update_lang=True)
                i += 1
                sclass = ""
                if i == 1:
                    sclass = "ins-active"

                uidata += [{"_data": sdata["title"], "name": "type", "data-name": v, "data-tid": s["id"],
                            "class": f"ins-button-s  -subtype-inner-btn  ins-m-col-3 ins-flex-center ins-strong-m -product-filter-input {sclass}"}]
            uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)


    def out(self):


        self.app._include("style.css")
        self.app._include("script.js")
        self.app._include("search.js")

        if self.ins._langs._this_get()["name"] == "ar":
            self.app._include("style_ar.css")
        else:
            self.app._include("style_en.css")

        rq = self.ins._server._req()

        if not "mode" in rq or rq["mode"] != "item":
            url = self.ins._server._url()

            self.ins._tmp._data_social_tags({"title": "SHOP NOW", "des": "Discover our wide collection of gold bars and coins at the best prices. Shop now with El Galla Gold – easy, secure, and reliable.",
                                            "img": "ins_web/ins_uploads/images/seo/product_now.png", "url": url})



            app = AppProductsSearch(self.app)
            return app.out()
        else:
            app = AppProductDetails(self.app)
            return app.out()
