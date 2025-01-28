from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from ins_gla.ins_apps.app_products.app_product_details import AppProductDetails
from urllib.parse import parse_qs
import math

items_per_page = 12


class AppProducts(App):
  
  
    @property
    def session_name(sel):
        return "glaproducts"
    

    def _filter_redirect(self):
        rq = self.ins._server._post()
        if "type" in rq and rq["type"] == "reset":
            return "http://127.0.0.1:5000/product/"
        
        url = f'http://127.0.0.1:5000/product/do/filter/{rq["sql"]}'
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
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-secondary ins-text-upper ins-text-center ins-font-s"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)


        return r



    def _cart_lightbox_ui(self):

        p =self.ins._server._post()
        pro= self.ins._db._jget("gla_product", "*", f"gla_product.id={p["pid"]}")
        pro._jwith("gla_product_category category", "title,id", rfk="fk_product_category_id" ,join="left join")
        ddata = pro._jrun()

        for data in ddata:

            sedata=self.ins._server._get_session(self.session_name)
            if type(sedata) != dict:
                sedata ={}
            adddata = {"id":data["id"] ,"title":data["title"],"category":data["category_title"] ,"weight":data["weight"] ,"price" :data["price"],"des" :data.get("des" ,"") ,"th_main" :data["th_main"]  ,"count":p["count"] }
            sedata[str(data["id"])] =adddata

            self.ins._server._set_session(self.session_name,sedata)


            sedata=self.ins._server._get_session(self.session_name)

            uidata=[{"start":True ,"class":"ins-col-12 ins-flex -cart-cont"}]


            for k,v in sedata.items():
           
                uidata+= ELUI(self.ins).cart_pro_block(v)
                uidata.append({"class":"ins-space-xs"})


            footer=[{"start":True ,"class":"ins-flex-space-between ins-col-12 ins-padding-l"},

            {"_data":"Continue Shopping" ,"class":"ins-button-s  ins-text-upper ins-gold-d ins-col-6 -continue-shopping-btn"},
            {"_data":"To cart","_type":"a","href":"/checkout/cart" ,"class":"ins-button-s  ins-gold-d  ins-text-upper ins-col-5"},
            {"end":True},
            
            ]

            uidata += footer
            
            uidata.append({"end":True})


            return self.ins._ui._render(uidata)      

    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def generate_product_html(self,string = False):
        global items_per_page
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}
        sql_parts = []
        for key, value in filter_data.items():
            sql_parts.append(f"{key} LIKE '%{value}%'")
        
        sql_query = " AND ".join(sql_parts)
        rq = self.ins._server._post()


        
        if sql_query:
            tcount = self.ins._db._get_row("gla_product", "count(id) as count", f"{sql_query}")["count"]
        else:
            tcount = self.ins._db._get_row("gla_product", "count(id) as count", "1=1")["count"]

        
        num_pages = math.ceil(tcount / items_per_page)

        if not "page" in rq:
            current_page = 1
        else:
            current_page = int(rq["page"])


        p = "/ins_web/ins_uploads/"
        offset = (current_page - 1) * items_per_page

        # Fetch and display products for the current page

        if sql_query:
            rpdata = self.ins._db._get_data("gla_product", "*", f"{sql_query} limit {offset}, {items_per_page}")

        else:
            rpdata = self.ins._db._get_data("gla_product", "*", f"1=1 limit {offset}, {items_per_page}")

        if rpdata:
            uidata = []

            for d in rpdata:
                st = "width:316px;"
                ##purl = self.ins._server._url({"mode":"product","id": f"{d["id"]}"})
                
                
                r = [
                    {"start": "true", "class": "ins-flex  gla-pro-block  ", "style": st},
                    {"start": "true", "class": " gla-img-cont  ", "style": ""},
                    {"_data": "Bestseller", "class": "ins-tag ins-primary-d ins-strong-m ins-text-upper","style": "   position: absolute;top: 8px;left: 8px; font-size: 10px;    border-radius: 2px !important;"},
                    {"src": p + d["th_main"], "_type": "img", "class": "gla-pro-img"},
                    {"src": p + d["th_overlay"], "_type": "img", "class": "gla-pro-himg"},
                    { "_type":"a" ,"_data": "SHOP NOW <i class=' lni ins-icon lni-arrow-right'></i>", "class": "ins-button gla-pro-hbutton ins-strong-m   ins-gold-bg","data-pid":f"{d['id']}"},
                    {"end": "true"},
                    {"class": "ins-space-s"},
                    {"_data": f"{d["title"]}", "class": "ins-col-12 ins-font-l ins-strong-m   ins-grey-color", "style": "line-height:24px"},
                    {"_data": "250,000.00", "class": "ins-col-12  ins-strong-m  ins-primary-color", "style": "line-height:24px"},
                    {"end": "true"}
                ]
                uidata += r

            uidata.append({"start": "true", "class": "ins-flex-center ins-col-12 ins-pagination"})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": 1, "_data": "<<"})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "prev", "_data": "<"})
            start_page = max(1, current_page - 2)
            end_page = min(num_pages, current_page + 2)
            for page in range(start_page, end_page + 1):
                active_class = "active" if page == current_page else ""
                uidata.append({"_type": "button", "class": f"ins-pagination-btn {active_class}", "data-page": page, "_data": str(page)})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": "next", "data-tpages":num_pages,"_data": ">"})
            uidata.append({"_type": "button", "class": "ins-pagination-btn", "data-page": num_pages, "_data": ">>"})
            uidata.append({"end": "true"})

            
            uidata.append({"end": "true"})
        else:
         uidata=[{"_data": "No data to show", "class": "ins-col-12 ins-card ins-text-center"}]

        if string:
            return uidata
        else:
            return self.ins._ui._render(uidata)



    def header_ui(self):

        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({},["mode","id","alias"])
       
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","class":" ins-font-s	ins-grey-d-color ins-strong-m"},
            {"_data": "Product","class":" ins-font-s	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]
      
        uidata+=path


        uidata.append({"_data":"Products","class":"ins-col-7 ins-title ins-strong-m ins-text-upper ins-grey-d-color"})

       

        ## checkout steps
       
        uidata.append({"end":"true"})
        return uidata


    def _filter(self):
        rq = self.ins._server._post()
        return rq

    def _list(self):
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)
        filter_data = {key: value[0] for key, value in parsed_data.items()}


        categories = self.ins._db._get_data("gla_product_category", "title,id")
        types = ["ISLAMIC","ROYAL","COPTIC"]
        uidata = [{"start":"true","class":"ins-flex ","style":"background:white;height:124px;position: relative;    border-bottom: 1px solid var(--grey-l); "}]
        uidata+=self.header_ui()
        uidata.append({"end":"true"})

        uidata.append({"start": "true", "class": "ins-flex-valign-start gla-container ins-col-12 ins-padding-2xl ins-padding-h"})

        ## Filter Area
        uidata.append({"start": "true", "class": "ins-flex ins-col-3 -filter-area ins-grey-d-color ins-padding-m full-height","style":"background:white;"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"_type": "input", "name":"title","value":filter_data.get("title",""),"data-name":"title","type": "text", "placeholder":"Product name Search..","class":" -product-filter-input -title-input",  "pclass": "ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class": "ins-space-m"})



        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-gap-o"})
        uidata.append({"_data": "Category", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-font-m  "})
        category_ids = filter_data.get("fk_product_category_id", "").split(',')

        for c in categories:
            if str(c["id"]) in category_ids:
                uidata.append({"_type": "input", "name":"type", "checked": "checked", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "1", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
            else:
                uidata.append({"_type": "input", "name":"type", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "0", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
                
       
       
        uidata.append({"end":"true"})




        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Type", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-font-m  "})
       
        tys = filter_data.get("types", "").split(',')
        for t in types:
            active = "ins-active" if t.lower() in tys else ""
            uidata.append({"_data": t, "name":"type","data-name":t.lower(),"class": f"ins-button-s  -type-btn ins-strong-m  ins-col-4  -product-filter-input {active}"})

        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Weight", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-font-m  "})
        uidata.append({"_type": "select", "value":filter_data.get("weight",""),"data-name":"weight", "_data":",0.25gm,0.5gm,1gm,2.5gm,5gm,10gm,0.5oz / 15.55gm,20gm,1oz / 31.10gm,50gm,100gm,10 Tolas / 116.65gm,250gm,500gm,1000gm", "name": "weight", "pclass": "ins-col-12","class":" -product-filter-input -weight-select"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"class": "ins-line ins-col-12"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"start": "true", "class": "ins-col-12 ins-flex-space-between"})
        uidata.append({"_data": "Reset", "class": "ins-col-6  ins-button -product-reset-btn ins-border"})
        uidata.append({"_data": "Filter", "class": "ins-col-6 ins-gold-d ins-button -product-filter-btn"})
        uidata.append({"end": "true"})



        uidata.append({"end": "true"})



        ## Products Area
        uidata.append({"start": "true", "class": "ins-flex-gow ins-col-9 ins-padding-m "})
        uidata.append({"_data": "", "class": "ins-col-9  ins-grey-d-color ins-font-xl ins-strong-m ins-text-upper"})
        uidata.append({"_type": "select", "_start": "Price", "_data": "High to Low,Low to High", "value": "high_to_low,low_to_high", "name": "order_by", "pclass": "ins-col-3"})

    

        # Add the product HTML
        uidata.append({"start": "true", "class": "ins-flex-valign-start -products-area   ins-col-12 ins-padding-l"})
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
