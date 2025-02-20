import json
from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from ins_gla.ins_apps.app_products.app_product_details import AppProductDetails
from urllib.parse import parse_qs
import math
class AppProducts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    @property
    def session_name(sel):
        return "glaproducts"
    def _filter_redirect(self):
        rq = self.ins._server._post()
        if "type" in rq and rq["type"] == "reset":
            return "http://127.0.0.1:5000/product/"
        url = f'http://127.0.0.1:5000/product/do/filter/{rq["sql"]}'
        return url
    

    def _filter_redirect_inner(self):
        rq = self.ins._server._post()
        if "type" in rq and rq["type"] == "reset":
            return "http://127.0.0.1:5000/product/"
        url = f'http://127.0.0.1:5000/product/product/{rq["pid"]}/do/type/{rq["sql"]}'
        return url

    

    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata=self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"]) 
        self.ins._server._set_session(self.session_name,sedata)
        ndata=self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"
        if not ndata:
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-secondary ins-text-upper ins-text-center ins-title-12"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)
        return r
    


    def _cart_lightbox_ui(self):
         return ELUI(self.ins)._cart_lightbox_ui(True)



    def generate_product_html(self,string = False):
        items_per_page = 12
        f = self.ins._server._get("page")
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}
        tys = filter_data.get("types", "")


        sql_parts = []
        for key, value in filter_data.items():
                values = value.split(",")
                if len(values) > 1:
                    condition = " OR ".join([f"{key} = '{v.strip()}'" for v in values])
                    sql_parts.append(f"({condition})")
                else:
                    if key != "price_range" and key != "weight" :
                        sql_parts.append(f"{key} LIKE '%{value.strip()}%'")
                    elif key == "price_range":
                        range_price = value.split("-")
                        min_price = range_price[0]
                        max_price = range_price[1]
                        sql_parts.append(f"price BETWEEN '{min_price}' AND '{max_price}'")
                    elif key == "weight":
                         sql_parts.append(f"{key} ='{value}'")



        sql_query = " AND ".join(sql_parts)
      
        rq = self.ins._server._post()
        
        
        if sql_query:
            tcount = self.ins._db._get_row("gla_product", "count(id) as count", f"{sql_query}")["count"]
        else:
            tcount = self.ins._db._get_row("gla_product", "count(id) as count", "1=1")["count"]
       
       
       
       
       
        num_pages = math.ceil(tcount / items_per_page)
        if not f:
            current_page = 1
        else:
            current_page = int(f)
        offset = (current_page - 1) * items_per_page
       

       
        if sql_query:
            rpdata = self.ins._db._get_data("gla_product", "*", f"{sql_query} limit {offset}, {items_per_page}",update_lang=True)
        else:
         rpdata = self.ins._db._get_data("gla_product", "*", f"1=1 limit {offset}, {items_per_page}",update_lang=True)
        ndata = []

        if tys:
         for r in rpdata:
                types_data = json.loads(r["types_data"])
                types = types_data[tys]["data"]
                for k,v in types.items():
                    new_r = r.copy()
                    new_r["subtype"] = k
                    ndata.append(new_r)
         if ndata:
            rpdata = ndata


       
       
        if rpdata:
            uidata = []
            for d in rpdata:
                uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}","width:300px;",d.get("subtype",""),tys)
            uidata.append({"class": "ins-space-xl"})
            uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-pagination-area ins-padding-l","style":"background:white;"})
            uidata.append({"start": "true", "class": "ins-flex-start"})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "prev","_data": "<i class='lni lni-chevron-left'></i>"})
            start_page = max(1, current_page - 2)
            end_page = min(num_pages, current_page + 2)
            for page in range(start_page, end_page + 1):
                active_class = "active" if page == current_page else ""
                uidata.append({"_type": "button", "class": f"ins-pagination-btn {active_class}", "data-page": page, "_data": str(page)})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "next", "data-tpages":num_pages,"_data": "<i class='lni lni-chevron-left' style='rotate:180deg'></i>"})
            uidata.append({"end": "true"})
            uidata.append({"class": "ins-col-grow"})
            uidata.append({"start": "true", "class": "ins-flex-end"})
            uidata.append({"_data": "Go to page","_data-ar": "انتقل إلى الصفحة", "_trans":"true","class": "ins-title-12 ins-grey-m-color"})
            uidata.append({"_type": "input","type":"text","class":"-page-input ins-radius-s ins-white ins-text-center","pclass":"ins-col-2"})
            uidata.append({"_data": "Go <i class='lni lni-chevron-left' style='rotate:180deg'></i>","_data-ar":"انتقل","_trans":"true", "data-tpages":num_pages,"class": "ins-title-14 -go-to-page-btn ins-grey-color ins-button-text"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
        else:
         uidata=[{"_data": "No data to show", "class": "ins-col-12 ins-card ins-text-center"}]
        if string:
            return uidata
        else:
            return self.ins._ui._render(uidata)
        


    def header_ui(self):
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}
        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({},["mode","id","alias"])
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","_data-ar":"الرئيسية /","_trans":"true","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "Product","_data-ar": "المنتجات","_trans":"true","class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]
        uidata+=path

        uidata.append({"start":"true","class":"ins-col-12 ins-flex"})
        uidata.append({"_data":"Products","_data-ar": "منتجات","_trans": "true","class":"ins-col-3 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})

        if filter_data:
            filter_area = [
                {"start":"true","class":"ins-col-grow ins-flex-end"},
                {"_data":"Filter by",  "_data-ar":"تصفية حسب","_trans":"true","class":"ins-strong-m ins-grey-d-color ins-title-14"}
            ]
            for k,v in filter_data.items():
                if k == "fk_product_category_id":
                    name = "Category"
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "تصنيف"
                    d = self.ins._db._get_row("gla_product_category","title,kit_lang",f"id='{v}'",update_lang=True)
                    v = d["title"]
                elif k == "types":
                    name = "Type"
                    d = self.ins._db._get_row("gla_product_types","title,kit_lang",f"alias='{v}'",update_lang=True)
                    v = d["title"]
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "النوع"
                elif k == "title":
                    name = "Title"
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "اسم المنتج"
                elif k == "weight":
                    name = "Weight"
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "الوزن"
                elif k == "price_range":
                    name = "Price range"
                    v = v.replace("-", ":" )
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "السعر"
                filter_area.append({"_data":f"{name}: {v} <i data-name={k} class='lni lni-xmark -remove-filter-btn'></i>","class":"ins-filter-card"})
            filter_area.append({"_data":"Clear All","_data-ar":"حذف الكل","_trans":"true","class":"ins-danger-color ins-button-text -remove-filter-all-btn ins-title-12"})
            filter_area.append({"end":"true"})
        
        
            uidata+=filter_area 
        

      
        uidata.append({"end":"true"})
        uidata.append({"end":"true"})
        return uidata
    

    def _filter(self):
        rq = self.ins._server._post()
        return rq
    

    def _show_subtypes_inner(self):

        
        rq = self.ins._server._post()
        
        pdata = self.ins._db._get_row("gla_product","types_data",f"id='{rq["pid"]}'")["types_data"]

        types_data = json.loads(pdata)
        subtypes =types_data[rq["name"]]["data"]

        if subtypes:
            uidata = [
            {"start":"true","class":"ins-flex ins-col-12"},
            {"_data": "Subtype","_data-ar": " نوع فرعي", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            for v,s in subtypes.items():
                uidata +=[{"_data": s["title"], "name":"type","data-name": v,"data-tid": s["id"],"class": f"ins-button-s  -subtype-inner-btn ins-flex-center ins-strong-m -product-filter-input"}]
            uidata.append({"end":"true"})
     
     
        return self.ins._ui._render(uidata)


    def _show_subtypes(self,tid="",stys="",string=True):
       
       
        
        rq = self.ins._server._post()
        if rq:
            subtypes = self.ins._db._get_data("gla_product_types","*",f"fk_parent_id='{rq["tid"]}'",update_lang=True)

        else:
            subtypes = self.ins._db._get_data("gla_product_types","*",f"fk_parent_id='{tid}'",update_lang=True)

        if subtypes:
            uidata = [
            {"start":"true","class":"ins-flex ins-col-12"},
            {"_data": "Subtype","_data-ar": " نوع فرعي", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            for s in subtypes:
                active = "ins-active" if s["alias"] == stys else ""
                uidata +=[{"_data": s["title"], "name":"type","data-name": s["alias"],"data-tid": s["id"],"class": f"ins-button-s  -subtype-btn ins-flex-center ins-strong-m -product-filter-input {active}"}]
            uidata.append({"end":"true"})
            if string:
                return self.ins._ui._render(uidata)
            else:
             return uidata


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

       
        types = self.ins._db._get_data("gla_product_types","*","fk_parent_id='0'",update_lang=True)
       
        uidata = [{"start":"true","class":"ins-flex ","style":"background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata+=self.header_ui()
        uidata.append({"end":"true"})
        uidata.append({"start": "true", "class": "ins-flex-valign-start gla-container ins-col-12 ins-padding-2xl ins-padding-h"})
       
        ## Filter Area
        uidata.append({"start": "true", "class": "ins-flex ins-col-3 -filter-area ins-grey-d-color ins-padding-2xl full-height ins-sticky-top","style":"background:white;"})
        uidata.append({"_type": "input", "name":"title","value":filter_data.get("title",""),"data-name":"title","type": "text", "placeholder":"Product name Search..","placeholder-ar": "انتقل إلى الصفحة","_trans": "true","class":" -product-filter-input -title-input",  "pclass": "ins-col-12 ins-hidden","style":"    background: white;border-radius:4px;"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-gap-o"})
        uidata.append({"_data": "Category","_data-ar": "تصنيف","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        category_ids = filter_data.get("fk_product_category_id", "").split(',')
        for c in categories:
            if str(c["id"]) in category_ids:
                uidata.append({"_type": "input", "name":"type", "checked": "checked", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "1", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
            else:
                uidata.append({"_type": "input", "name":"type", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "0", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
        
        uidata.append({"end":"true"})
        uidata.append({"class": "ins-space-m"})
        uidata.append({"_data": "Type","_data-ar": "نوع","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
      
      
        tys = filter_data.get("types", "").split(',')
        stys = filter_data.get("subtypes", "")
        
        tid = ""
        for t in types:
            active = ""
            if t["alias"] in tys:
                active = "ins-active"
                tid =  t["id"]
            uidata.append({"_data": t["title"], "name":"type","data-name": t["alias"],"data-tid": t["id"],"class": f"ins-button-s  -type-btn ins-flex-center ins-strong-m  ins-col-4  -product-filter-input {active}"})
      
        uidata.append({"class": "ins-space-m"})

        """if not stys:
            uidata.append({"class": "-subtypes-area"})

        else:
            uidata.append({"start":"true","class": "-subtypes-area"})
            uidata+=self._show_subtypes(tid,stys,False)
            uidata.append({"end": "true"})"""

       
       
        uidata.append({"_data": "Weight","_data-ar": "وزن","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        uidata.append({"_type": "select", "value":filter_data.get("weight",""),
                       
                       "data-name":"weight",
                       "_trans":"true",
                       
                       "fl_data":{
                           "0":"-",
  "0.25": "0.25gm",
  "0.5": "0.5gm",
  "1": "1gm",
  "2.5": "2.5gm",
  "5": "5gm",
  "10": "10gm",
  "15.55": "0.5oz / 15.55gm",
  "20": "20gm",
  "31.10": "1oz / 31.10gm",
  "50": "50gm",
  "100": "100gm",
  "116.65": "10 Tolas / 116.65gm",
  "250": "250gm",
  "500": "500gm",
  "1000": "1000gm"
}
,    "fl_data-ar":{
                           "0":"-",
  "0.25": "0.25 جرام",
  "0.5": "0.5 جرام",
  "1": "1 جرام",
  "2.5": "2.5 جرام",
  "5": "5 جرام",
  "10": "10 جرام",
  "15.55": "0.5oz / 15.55جرام",
  "20": "20 جرام",
  "31.10": "1 أونصة / 31.10 جرام",
  "50": "50 جرام",
  "100": "100 جرام",
  "116.65": "10 تولة / 116.65 جرام",
  "250": "250 جرام",
  "500": "500 جرام",
  "1000": "1000 جرام"
},
                       
                       "name": "weight", "pclass": "ins-col-12","class":" -product-filter-input -weight-select"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Price ","_data-ar": "السعر","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
      
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-gap-o"})
        uidata.append({"_type": "input", "name":"from","value":min_price,"data-name":"from","type": "text", "placeholder":"from","placeholder-ar": "من","_trans": "true","class":" -price-from-filter-input -price-from-input",  "pclass": "ins-col-5 "})
        uidata.append({"_type": "input", "name":"to","value":max_price,"data-name":"to","type": "text", "placeholder":"to","placeholder-ar": "إلى","_trans": "true","class":" -price-to-filter-input -price-to-input",  "pclass": "ins-col-5 "})
        uidata.append({"_data":"<i class='lni lni-search-1'></i>","class":" ins-gold-d-color ins-flex-center -filter-price-btn"})
        uidata.append({"end": "true"})

        uidata.append({"class": "ins-line ins-col-12"})

        uidata.append({"end": "true"})
        ## Products Area
        uidata.append({"start": "true", "class": "ins-col-9 ins-padding-m ins-flex"})
        # Add the product HTML
        uidata.append({"start": "true", "class": "ins-flex-valign-start -products-area   ins-col-12 ins-padding-l ins-gap-20"})
        uidata += self.generate_product_html(True)
        uidata.append({"end": "true"})
        return self.ins._ui._render( uidata)
    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        rq = self.ins._server._req()
        if not "mode" in rq:
         return self._list()
        else:
            app = AppProductDetails(self.app)
            return app.out()
