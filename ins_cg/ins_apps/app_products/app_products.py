import json
from ins_cg.ins_apps.app_products.app_product_details import AppProductDetails
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
        sedata=self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"]) 
        self.ins._server._set_session(self.session_name,sedata)
        ndata=self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"

        count = 0
        if ndata:
                for _, s in ndata.items():
                    count += int(s["count"])
        r["count"] = str(count)

        if not ndata:
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-secondary ins-text-upper ins-text-center ins-title-12"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)
        return r
    



    def _products_ui(self,string = False):
        items_per_page = 12
        f = self.ins._server._get("page")
        g = self.ins._server._get("filter")
        o = self.ins._server._get("order")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}
        tys = filter_data.get("types_data", "")


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







        if sql_query:
            rpdata = self.ins._db._get_data("gla_product", "*", f"{sql_query} {order} limit {offset}, {items_per_page}",update_lang=True)
        else:
         rpdata = self.ins._db._get_data("gla_product", "*", f"1=1 {order} limit   {offset}, {items_per_page}",update_lang=True)
        ndata = []


        
        if tys:
         for r in rpdata:
                types_data = json.loads(r["types_data"])
                types = {k: v for k, v in sorted(types_data[tys]["data"].items(), key=lambda item: int(item[1].get("order",float('1'))))}

                for k,v in types.items():
                    new_r = r.copy()
                    new_r["subtype"] = k
                    ndata.append(new_r)
         if ndata:
            rpdata = ndata

        rstyle = "rotate:180deg"
        lstyle = ""
        if self.ins._langs._this_get()["name"] == "ar":
            rstyle = ""
            lstyle = "rotate:180deg"


       
       
        if rpdata:
            uidata = []
            for d in rpdata:
                uidata+= ELUI(self.ins).shop_pro_block(d)
            uidata.append({"class": "ins-space-xl"})
            uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-m-flex-center ins-pagination-area ins-padding-l ins-m-col-12","style":"background:white;"})
            uidata.append({"start": "true", "class": "ins-flex-start ins-m-col-12 ins-m-flex-center -pro-pages-buttons"})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "prev","_data": f"<i class='lni lni-chevron-left' style='{lstyle}'></i>"})
            start_page = max(1, current_page - 2)
            end_page = min(num_pages, current_page + 2)
            for page in range(start_page, end_page + 1):
                active_class = "active" if page == current_page else ""
                uidata.append({"_type": "button", "class": f"ins-pagination-btn ins-m-flex-center {active_class}", "data-page": page, "_data": str(page)})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "next", "data-tpages":num_pages,"_data": f"<i class='lni lni-chevron-left' style='{rstyle}'></i>"})
            uidata.append({"end": "true"})
            uidata.append({"class": "ins-col-grow ins-m-col-3"})
            uidata.append({"start": "true", "class": "ins-flex-end not-for-phone"})
            uidata.append({"_data": "Go to page","_data-ar": "انتقل إلى الصفحة", "_trans":"true","class": "ins-title-12 ins-grey-m-color ins-m-col-3"})
            uidata.append({"_type": "input","type":"text","class":"-page-input ins-radius-s ins-white ins-text-center","pclass":"ins-col-2 ins-m-col-2"})
            uidata.append({"_data": "Go <i class='lni lni-chevron-left' style='rotate:180deg'></i>","_data-ar":"انتقل","_trans":"true", "data-tpages":num_pages,"class": "ins-title-14 -go-to-page-btn ins-grey-color ins-button-text"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
        else:
         uidata=[{"_data": "No matching results found",  
"_data-ar": "لا توجد نتائج مطابقة"  
,"_trans": "true", "class": "ins-col-12 ins-card ins-text-center"}]
        if string:
            return uidata
        else:
            return self.ins._ui._render(uidata)
        


    def header_ui(self):
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}


        order_data = self.ins._server._get("order")
        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({},["mode","id","alias","filter"])
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","_data-ar":"الرئيسية /","_trans":"true","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "Product","_data-ar": "المنتجات","_trans":"true","class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]
        uidata+=path

        uidata.append({"start":"true","class":"ins-col-12 ins-flex"})
        uidata.append({"_data":"Products","_data-ar": "منتجات","_trans": "true","class":"ins-col-grow ins-m-col-3 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        uidata.append({"class":"ins-font-xl ins-m-col-1  not-for-web lni lni-funnel-1 -filter-menu"})
        
        
        
        vorder = "low"
        if order_data:
            vorder =  order_data
        uidata.append({"start":"true","class":"ins-col-grow ins-flex-end ins-m-flex-start -filter-results-area"})

        order_area = [
                {"start":"true","class":"ins-flex-end ins-m-col-6 ins-m-flex-start"},
                {"_data":"Order by",  "_data-ar":"ترتيب حسب","_trans":"true","class":"ins-strong-m ins-grey-d-color ins-title-14 ins-m-col-grow"},
                {"_type":"select","name":"order","fl_data":{
                    "low":"Lowest to Highest",
                    "high":"Highest to Lowest",
                    "old":"Oldest to Newest",
                    "new":"Newest to Oldest"
                },"fl_data-ar":{
                    "low":"من الارخص للأغلى",
                    "high":"من الأغلى للأرخص",
                    "old":"من الأقدم للأجدد",
                    "new":"من الأجدد للأقدم"
                },"_trans":"true","value":vorder,"pclass":"ins-col-grow ins-m-col-7","class":"-order-select"},
                {"end":"true"}
            ]


        uidata+=order_area 


        if filter_data:
            filter_area = [
                {"start":"true","class":" ins-flex-end ins-m-flex-start"},
                {"_data":"Filter by",  "_data-ar":"تصفية حسب","_trans":"true","class":"ins-strong-m ins-grey-d-color ins-title-14"}
            ]
            for k,v in filter_data.items():
                if k == "fk_product_category_id":
                    name = "Category"
                    if self.ins._langs._this_get()["name"] == "ar" :
                        name = "تصنيف"
                    d = self.ins._db._get_row("gla_product_category","title,kit_lang",f"id='{v}'",update_lang=True)
                    v = d["title"]
                elif k == "types_data":
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
        uidata.append({"end":"true"})
        return uidata
    

    def _filter(self):
        rq = self.ins._server._post()
        return rq
    

    def _show_subtypes_inner(self):

        
        rq = self.ins._server._post()
        
        pdata = self.ins._db._get_row("gla_product","types_data",f"id='{rq['pid']}'")["types_data"]

        types_data = json.loads(pdata)

        subtypes =types_data[rq["name"]]["data"]
        subtypes = {k: v for k, v in sorted(subtypes.items(), key=lambda item: int(item[1].get("order",float('1'))))}

        if subtypes:
            uidata = [
            {"start":"true","class":"ins-flex ins-col-12"},
            {"_data": "Subtype","_data-ar": " نوع فرعي","_trans":"true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            i = 0
            for v,s in subtypes.items():
                sdata = self.ins._db._get_row("gla_product_types","title,kit_lang",f"alias='{v}'",update_lang=True)
                i+=1
                sclass = ""
                if i == 1:
                    sclass = "ins-active"

                uidata +=[{"_data": sdata["title"], "name":"type","data-name": v,"data-tid": s["id"],"class": f"ins-button-s  -subtype-inner-btn  ins-m-col-3 ins-flex-center ins-strong-m -product-filter-input {sclass}"}]
            uidata.append({"end":"true"})
     
     
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
        uidata.append({"start": "true", "class": "ins-flex-valign-start -products-area   ins-col-12 ins-padding-l ins-gap-10 ins-m-flex-center"})
        uidata += self._products_ui(True)
        uidata.append({"end": "true"})
        return self.ins._ui._render( uidata)
    def out(self):



        self.app._include("style.css")
        self.app._include("script.js")

        if self.ins._langs._this_get()["name"] == "ar":
          self.app._include("style_ar.css")
        else:
          self.app._include("style_en.css")

        rq = self.ins._server._req()
        if not "mode" in rq:
         url = self.ins._server._url()
         self.ins._tmp._data_social_tags({"title":"SHOP NOW","des":"Discover our wide collection of gold bars and coins at the best prices. Shop now with El Galla Gold – easy, secure, and reliable.","img":"ins_web/ins_uploads/images/seo/product_now.png","url":url})

         return self._list()
        else:
            app = AppProductDetails(self.app)
            return app.out()
