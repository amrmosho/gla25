from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
from ins_gla.ins_apps.app_products.app_product_details import AppProductDetails

import math
items_per_page = 12


class AppProducts(App):
  
  
    @property
    def session_name(sel):
        return "glaproducts"
    

    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata=self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"]) 
        self.ins._server._set_session(self.session_name,sedata)
        ndata=self.ins._server._get_session(self.session_name)
        r = {}
        r["status"] = "2"

        if not ndata:
            uidata=[{"_data":"There is no items in cart","class":"ins-col-12 ins-card ins-gold ins-text-upper ins-text-center ins-font-s","style":"padding: 7px;margin-top: 30px;"}]
            r["status"] = "1"
            r["ui"] = self.ins._ui._render(uidata)


        return r



    def _cart_lightbox_ui(self):

        p =self.ins._server._post()
        data= self.ins._db._get_row("gla_product", "*", f"id={p["pid"]}")

        sedata=self.ins._server._get_session(self.session_name)
        if type(sedata) != dict:
            sedata ={}
        adddata = {"id":data["id"] ,"title":data["title"] ,"price" :data["price"],"des" :data.get("des" ,"") ,"th_main" :data["th_main"]  ,"count":p["count"] }
        sedata[str(data["id"])] =adddata

        self.ins._server._set_session(self.session_name,sedata)


        sedata=self.ins._server._get_session(self.session_name)

        uidata=[{"start":True ,"class":"ins-col-12 ins-flex -cart-cont"}]


        for k,v in sedata.items():
       
            uidata+= ELUI(self.ins).small_pro_block(v)



        footer=[{"start":True ,"class":"ins-flex-space-between ins-col-12 ins-padding-l"},

        {"_data":"Continue Shopping" ,"class":"ins-button-s ins-font-xs ins-text-upper ins-gold ins-col-6 -continue-shopping-btn"},
        {"_data":"To cart","_type":"a","href":"/checkout/cart" ,"class":"ins-button-s ins-font-xs ins-gold  ins-text-upper ins-col-5"},
        {"end":True},
        
        ]

        uidata += footer
        
        uidata.append({"end":True})


        return self.ins._ui._render(uidata)      


    
      
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def generate_product_html(self):
        global items_per_page
        tcount = self.ins._db._get_row("gla_product", "count(id) as count", "1=1")["count"]
        num_pages = math.ceil(tcount / items_per_page)
        rq = self.ins._server._req()
        uidata = []
        if not "page" in rq:
            current_page = 1
        else:
            current_page = int(rq["page"])


        p = "/ins_web/ins_uploads/"
        offset = (current_page - 1) * items_per_page

        # Fetch and display products for the current page
        rpdata = self.ins._db._get_data("gla_product", "*", f"1=1 limit {offset}, {items_per_page}")

        for d in rpdata:
            st = "width:230px;"

            pro_url =self.ins._server._url({"id": d["id"] ,"mode":"product"})
            r = [
                {"start": "true", "class": "ins-flex  gla-pro-block  ", "style": st},
                {"start": "true", "class": " gla-img-cont  ", "style": ""},
                {"_data": "Bestseller", "class": "ins-tag ins-primary  ins-radius-s", "style": "   position: absolute;top: 8px;left: 8px;"},
                {"src": p + d["th_main"], "_type": "img", "class": "gla-pro-img"},
                {"src": p + d["th_overlay"], "_type": "img", "class": "gla-pro-himg"},
                { "_type":"a" ,"href":pro_url,"_data": "SHOP NOW <i class=' lni ins-icon lni-arrow-right'></i>", "class": "ins-button gla-pro-hbutton ins-strong-m   ins-gold-bg","data-pid":f"{d['id']}"},
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
        if not "page" in rq:
            return uidata
        else:
            return self.ins._ui._render(uidata)

    def _list(self):
        categories = self.ins._db._get_data("gla_product_category", "title")

        uidata = [{"start": "true", "class": "ins-flex-valign-start gla-container ins-col-12"}]

        ## Filter Area
        uidata.append({"start": "true", "class": "ins-flex ins-col-3 ins-grey-bg-bg ins-padding-m full-height"})
        uidata.append({"_data": "Filter", "class": "ins-col-12  ins-grey-d-color ins-font-l ins-strong-l"})
        for c in categories:
            uidata.append({"_type": "input", "type": "checkbox", "value": "0", "_end": c["title"], "pclass": "ins-col-12  -product-list-chkbox"})
        uidata.append({"end": "true"})

        ## Products Area
        uidata.append({"start": "true", "class": "ins-flex-gow ins-col-9 ins-padding-m "})
        uidata.append({"_data": "Products", "class": "ins-col-9  ins-grey-d-color ins-font-l ins-strong-l"})
        uidata.append({"_type": "select", "_start": "Price", "_data": "High to Low,Low to High", "_value": "high_to_low,low_to_high", "name": "order_by", "pclass": "ins-col-3"})

    

        # Add the product HTML
        uidata.append({"start": "true", "class": "ins-flex-valign-start -products-area   ins-col-12 ins-padding-l ins-gap-m"})
        uidata += self.generate_product_html()
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
