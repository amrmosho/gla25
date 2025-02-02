from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from ins_gla.ins_apps.app_products.app_product_details import AppProductDetails
from urllib.parse import parse_qs
import math

items_per_page = 12


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

 

    def generate_product_html(self,string = False):
        global items_per_page
        g = self.ins._server._get("filter")
        parsed_data = parse_qs(g)

        filter_data = {key: value[0] for key, value in parsed_data.items()}
        sql_parts = []

        for key, value in filter_data.items():
            values = value.split(",")
            # Handle multiple values for the same key
            if len(values) > 1:
                condition = " OR ".join([f"{key} = '{v.strip()}'" for v in values])
                sql_parts.append(f"({condition})")
            else:
                sql_parts.append(f"{key} LIKE '%{value.strip()}%'")

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

        offset = (current_page - 1) * items_per_page

        # Fetch and display products for the current page

        if sql_query:
            rpdata = self.ins._db._get_data("gla_product", "*", f"{sql_query} limit {offset}, {items_per_page}")

        else:
            rpdata = self.ins._db._get_data("gla_product", "*", f"1=1 limit {offset}, {items_per_page}")

        if rpdata:
            uidata = []

            for d in rpdata:
                
                uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}",st="width:300px;")

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
            uidata.append({"_data": "Go to page", "class": "ins-title-12 ins-grey-m-color"})
            uidata.append({"_type": "input","type":"text","class":"-page-input ins-radius-s ins-white ins-text-center","pclass":"ins-col-2"})
            uidata.append({"_data": "Go <i class='lni lni-chevron-left' style='rotate:180deg'></i>", "data-tpages":num_pages,"class": "ins-title-14 -go-to-page-btn ins-grey-color ins-button-text"})

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

        uidata=[{"start":"true","class":"ins-flex ins-col-12 gla-container ins-padding-2xl"}]
        home_url = self.ins._server._url({},["mode","id","alias"])
       
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": "Product","class":" ins-title-12	ins-grey-color ins-strong-m"},
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
        uidata.append({"start": "true", "class": "ins-flex ins-col-3 -filter-area ins-grey-d-color ins-padding-m full-height ins-sticky-top","style":"background:white;top:95px"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"_type": "input", "name":"title","value":filter_data.get("title",""),"data-name":"title","type": "text", "placeholder":"Product name Search..","class":" -product-filter-input -title-input",  "pclass": "ins-col-12","style":"    background: white;border-radius:4px;"})
        uidata.append({"class": "ins-space-m"})



        uidata.append({"start": "true", "class": "ins-flex ins-col-12  ins-gap-o"})
        uidata.append({"_data": "Category", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        category_ids = filter_data.get("fk_product_category_id", "").split(',')

        for c in categories:
            if str(c["id"]) in category_ids:
                uidata.append({"_type": "input", "name":"type", "checked": "checked", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "1", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
            else:
                uidata.append({"_type": "input", "name":"type", "data-value":c["id"],"data-name":"fk_product_category_id","type": "checkbox", "value": "0", "_end": c["title"],"class":" -product-filter-input  -category-checkbox", "pclass": "ins-col-12  -product-list-chkbox","style":"    width: 20px;","pstyle":"    height: 35px;"})
                
       
       
        uidata.append({"end":"true"})


        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Type", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
       
        tys = filter_data.get("types", "").split(',')
        for t in types:
            active = "ins-active" if t.lower() in tys else ""
            uidata.append({"_data": t, "name":"type","data-name":t.lower(),"class": f"ins-button-s  -type-btn ins-strong-m  ins-col-4  -product-filter-input {active}"})

        uidata.append({"class": "ins-space-m"})

        uidata.append({"_data": "Weight", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})
        uidata.append({"_type": "select", "value":filter_data.get("weight",""),"data-name":"weight", "_data":",0.25gm,0.5gm,1gm,2.5gm,5gm,10gm,0.5oz / 15.55gm,20gm,1oz / 31.10gm,50gm,100gm,10 Tolas / 116.65gm,250gm,500gm,1000gm", "name": "weight", "pclass": "ins-col-12","class":" -product-filter-input -weight-select"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"class": "ins-line ins-col-12"})
        uidata.append({"class": "ins-space-m"})

        uidata.append({"start": "true", "class": "ins-col-12 ins-flex-space-between"})
        uidata.append({"_data": "Reset", "class": "ins-col-6  ins-button ins-border","_type":"a","href":"/product/"})
        uidata.append({"_data": "Filter", "class": "ins-col-6 ins-gold-d ins-button -product-filter-btn"})
        uidata.append({"end": "true"})



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
