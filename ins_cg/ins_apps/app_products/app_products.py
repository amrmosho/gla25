import json
from ins_cg.ins_apps.app_products.app_product_details import AppProductDetails
from ins_cg.ins_apps.app_products.app_products_search import AppProductsSearch

from ins_cg.ins_kit._elui import ELUI
from ins_cg.ins_kit._pros import Pros
from ins_kit._engine._bp import App
from urllib.parse import parse_qs
import math


class AppProducts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)




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
        Pros(self.ins)._remove_item_cart()
        return ELUI(self.ins)._cart_lightbox_ui()



    def _add_to_card(self):
        Pros(self.ins)._add_to_card()
        return ELUI(self.ins)._cart_lightbox_ui()
    
    
    def _cart_lightbox_ui(self):
        return ELUI(self.ins)._cart_lightbox_ui()





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


    def _list(self):

        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}
        categories = self.ins._db._get_data("gla_product_category", "title,id,kit_lang","1=1",update_lang=True)
        min_price = ""
        max_price = ""
        if "price_range" in filter_data and filter_data["price_range"]:
            price_range = filter_data["price_range"].split("-")
            min_price = price_range[0]
            max_price = price_range[1]
        w = "fk_parent_id='0' "
        if filter_data.get("fk_product_category_id"):
          w+= f" and fk_product_category_id like '%{filter_data.get('fk_product_category_id')}%'"
         
        types = self.ins._db._get_data("gla_product_types","*",f"{w} order by kit_order desc ",update_lang=True)

        uidata = [{"start":"true","class":"ins-flex -header-area","style":"background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata+=self.header_ui()
        uidata.append({"end":"true"})
        uidata.append({"start": "true", "class": "ins-flex-valign-start gla-container ins-col-12 ins-padding-2xl ins-padding-h -pro-cont"})
       
        ## Filter Area
        uidata.append({"start": "true", "class": "ins-flex ins-col-3  -filter-area ins-grey-d-color ins-padding-2xl full-height ins-sticky-top","style":"background:white;"})
        uidata.append({"_data": "Filter","_data-ar": "تصفية","_trans": "true", "class": "ins-m-col-11 ins-grey-d-color ins-font-xl not-for-web "})
        uidata.append({"class": " not-for-web ins-m-col-1 lni lni-xmark -close-filter ins-font-3xl _a_red"})

        uidata.append({"_type": "input", "name":"title","value":filter_data.get("title",""),"data-name":"title","type": "text", "placeholder":"Product name Search..","placeholder-ar": "انتقل إلى الصفحة","_trans": "true","class":" -product-filter-input -title-input",  "pclass": "ins-col-12 ins-hidden","style":"    background: white;border-radius:4px;"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-gap-o -category-area"})
        uidata.append({"_data": "Category","_data-ar": "تصنيف","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        category_ids = filter_data.get("fk_product_category_id", "").split(',')
        for c in categories:
            if str(c["id"]) in category_ids:
                uidata.append({"_type": "input", "name":"type", "checked": "checked", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "1", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12 ins-m-col-4  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
            else:
                uidata.append({"_type": "input", "name":"type", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "0", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  ins-m-col-4  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
        
        uidata.append({"end":"true"})
        uidata.append({"class": "ins-space-m"})
        if types:
            uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-m-co-12  -type-area"})

            uidata.append({"_data": "Type","_data-ar": "نوع","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})

            tys = filter_data.get("types_data", "").split(',')
            for t in types:
                active = ""
                if t["alias"] in tys:
                    active = "ins-active"
                
                uidata.append({"_data": t["title"], "name":"types_data","data-name": t["alias"],"data-tid": t["id"],"class": f"ins-button-s  -type-btn ins-flex-center ins-strong-m  ins-col-4   ins-m-col-4 -product-filter-input {active}"})
            uidata.append({"end":"true"})

            uidata.append({"class": "ins-space-m"})

       
        filter = self.ins._data._get_options("1")["content"]
        filter = json.loads(filter)
        fen = filter["gen"]["en"]
        far = filter["gen"]["ar"]

        if filter_data.get("fk_product_category_id"):
            fen = filter[filter_data.get("fk_product_category_id")]["en"]
            far = filter[filter_data.get("fk_product_category_id")]["ar"]


       
        uidata.append({"_data": "Weight","_data-ar": "وزن","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        uidata.append({"_type": "select", "value":filter_data.get("weight",""),"data-name":"weight","_trans":"true","fl_data":fen,"fl_data-ar":far,
                       
                       "name": "weight", "pclass": "ins-col-12","class":" -product-filter-input -weight-select"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Price ","_data-ar": "السعر","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
      
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-gap-o"})
        uidata.append({"_type": "input", "name":"from","value":min_price,"data-name":"from","type": "number", "placeholder":"from","placeholder-ar": "من","_trans": "true","class":" -price-from-filter-input -price-from-input",  "pclass": "ins-col-5 ins-m-col-5 "})
        uidata.append({"_type": "input", "name":"to","value":max_price,"data-name":"to","type": "number", "placeholder":"to","placeholder-ar": "إلى","_trans": "true","class":" -price-to-filter-input -price-to-input",  "pclass": "ins-col-5  ins-m-col-5 "})
        uidata.append({"_data":"<i class='lni lni-search-1'></i>","class":"ins-m-col-2 ins-gold-d-color ins-flex-center -filter-price-btn"})
        uidata.append({"end": "true"})

        uidata.append({"class": "ins-line ins-col-12"})

        uidata.append({"end": "true"})
        ## Products Area
        uidata.append({"start": "true", "class": "ins-col-9 ins-padding-m ins-flex -products-cont"})
        # Add the product HTML
        uidata.append({"start": "true", "class": "ins-flex-valign-start -products-area   ins-col-12 ins-padding-l ins-gap-20 ins-m-flex-center"})
        uidata += self._products_ui(True)
        uidata.append({"end": "true"})
        return self.ins._ui._render( uidata)
    def out(self):


        self.app._include("style.css")
        self.app._include("script.js")
        self.app._include("search.js")

        if self.ins._langs._this_get()["name"] == "ar":
            self.app._include("style_ar.css")
        else:
            self.app._include("style_en.css")

        rq = self.ins._server._req()

        if not "q1" in rq :
            url = self.ins._server._url()

            self.ins._tmp._data_social_tags({"title": "SHOP NOW", "des": "Discover our wide collection of gold bars and coins at the best prices. Shop now with El Galla Gold – easy, secure, and reliable.",
                                            "img": "ins_web/ins_uploads/images/seo/product_now.png", "url": url})



            app = AppProductsSearch(self.app)
            return app.out()
        else:
            app = AppProductDetails(self.app)
            return app.out()
