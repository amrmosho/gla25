from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
import json

class AppProductDetails(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)




    
    def _ui(self,rq):
        data = self.ins._db._get_row("gla_product", "*", f"id={rq["id"]}")
        if not data:
            return self.ins._ui._error("Product not found") 
        uidata = [
            {"start": "true", "class": "ins-flex-valign-start  gla-container ins-col-12 ins-padding-2xl ins-gap-m"},
        ]   
        home_url = self.ins._server._url({},["mode","id","alias"])
        product_url = self.ins._server._url({},["mode","id"])
       
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":product_url,"_data": "Product /","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": data["title"],"class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]

        uidata+=path


    ## Images Container
        image = {data["th_main"],data["th_overlay"]}
        if data["images"] != None:
            images = json.loads(data["images"])
            if 'type' in rq:
                image = images[rq["type"]]
            else:
                image = images["george"]

        uidata.append({"start": "true", "class": "ins-flex-valign-start ins-col-6 "})
        uidata.append({"start": "true", "class": "ins-flex-center ins-col-2 "})
        p = "/ins_web/ins_uploads/"
        count = 0
        aimage = "" 
        for i in image:
            aclass = "" 
            count += 1
            if count == 1:
               aclass = "ins-active"
               aimage =  i
            uidata.append({"start": "true","class":f"-side-img-cont ins-text-center ins-radius-l  {aclass}"})
            uidata.append({"src": p + i, "_type": "img","data-src":p + i,"class": f" ins-radius-m -side-img {aclass}", "style":"width:100%;"})  
            uidata.append({"end": "true"})
            uidata.append({"class": "ins-space-xs"})
        uidata.append({"end": "true"})
        uidata.append({"src": p + aimage, "_type": "img",
                 "class": " ins-radius-m ins-col-grow -main-img","style":"max-width:450px;"})
        uidata.append({"end": "true"})

        
        ## Data Container
        uidata.append({"start": "true", "class": "ins-flex ins-col-6 ins-card","style":"padding: 24px;"})

        
        ## Tags
        uidata.append({"_data": "Bestseller", "class": "ins-tag ins-primary-d ins-strong-m  ins-text-upper ins-title-10","style":"border-radius: 2px !important;"})
        uidata.append({"_data": "In Stock", "class": "ins-tag ins-secondary  ins-strong-m  ins-text-upper ins-title-10","style":"border-radius: 2px !important;"})
        uidata.append({"class": "ins-space-xs"})


        ## Title
        uidata.append({"_data": data["title"], "class": "ins-col-12 ins-title-l ins-grey-d-color ins-strong-m ins-text-upper "})   

        uidata.append({"class": "ins-space-s"})

        ## Sell Card
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-card ins-primary-w","style":"border-radius:8px 8px 0 0 !important;"})
        uidata.append({"_data": "Sell price", "class": "ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "})
        uidata.append({"_data": "Gold Amount", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(data["price"]),"_view":"currency","_currency_symbol":" EGP",  "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end "})
        uidata.append({"_data": "Making Charge + VAT", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data": "1,960.00 EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data":  str(data["price"]),"_view":"currency","_currency_symbol":" EGP",  "class": "ins-col-6  ins-strong-l ins-flex-end ins-title-20	 ins-primary-d-color"})
        vat = "59.60"
        uidata.append({"_data": "Note: Vat amount is " + "<spam class='ins-grey-d-color'>  "+vat+" EGP</span>", "class": "ins-col-6 ins-grey-color ins-strong-m ins-title-14"})
        uidata.append({"end": "true"})


        ## Buy Card
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-card ins-primary-bg  -open-panel","style":"border-radius: 0 0 8px 8px !important;position: relative;top: -8px;height: 65px;overflow: hidden;    border-top: 1px solid var(--primary-l)"})
        uidata.append({"_data": "We buy at", "class": "ins-col-11  ins-grey-d-color ins-title-20	 ins-strong-l"})
        uidata.append({"_data":"<span class=' lni lni-chevron-up'></span>","class": "ins-col-1  ins-grey-color ins-font-xl ins-strong-l -buy-div"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12"})
        uidata.append({"_data": "Gold Amount", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Cash back", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data": "1,960.00 EGP", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data":  str(data["price"]),"_view":"currency","_currency_symbol":" EGP",  "class": "ins-col-6  ins-strong-l ins-flex-end ins-title-20	 ins-primary-d-color"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        uidata.append({"class": "ins-space-s"})

        ## Product types

        if data["types"] !=None:
            uidata.append({"_data": "Type", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "})

            for t in data["types"].split(","):
                uidata.append({"_data": t, "class": "ins-button-s  -type-btn ins-strong-m ins-grey-color ","style":"    border: 1px solid var(--grey-l);border-radius: 8px !important;"})
       
        uidata.append({"class": "ins-space-s"})

        uidata.append({ "class": "ins-line ins-col-12"})

        uidata.append({"class": "ins-space-s"})


        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-gap-o"})  
        ## Counter area
        counter= [{"start": "true", "class": "ins-flex ins-col-3 ins-gap-o"},
            {"_data": "-", "class": "ins-button-s ins-flex-center ins-col-4 ins-gold-bg ins-font-2xl -minus-btn"},
            {"_type": "input",  "name":"count_inpt","type": "text","value":"1", "pclass": "ins-col-4 ","class":"count-inpt ins-title-xs ins-strong-l"},
            {"_data": "+", "class": "ins-button-s ins-flex-center  ins-col-4  ins-gold-bg ins-font-2xl  -plus-btn"},
            {"end": "true"}
            ]
        uidata+=counter
        ## Add to cart button
        uidata.append({"_data": "<img src='"+p+"style/cart.svg'></img> ADD TO CART","data-pid":data["id"], "class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"end": "true"})
        ## Terms area
        uidata.append({"_data": "<img src='"+p+"style/truck.svg ' style='position: relative;top: 4px;'></img> Free shipping for orders above EGP200k", "class": "ins-col-12 ins-grey-color ins-title-14"})
        uidata.append({"_data": "<img src='"+p+"style/gift.svg' style='position: relative;top: 4px;'></img> Include gift wrapping?", "class": "ins-col-11 ins-grey-color ins-title-14"})
        uidata.append({"_type": "input",  "type": "checkbox","value":"0", "class": "ins-form-bool-f"})
        uidata.append({"class": "ins-space-s"})

        ## Product Description
        uidata.append({"start": "true", "class": "ins-flex ins-col-12   -open-panel ins-active","style":"height: 30px;overflow: hidden;"})  
        uidata.append({"_data": "Product Description", "class": "ins-col-11  ins-grey-d-color ins-title-xs ins-strong-m"})
        uidata.append({"_data":"  <span class=' lni lni-chevron-up'></span>","class": "ins-col-1  ins-grey-color ins-font-xl ins-strong-l"})
        uidata.append({"_data": data["des"], "class": "ins-col-12  ins-grey-color ins-title-14"})
        uidata.append({"end": "true"})

      
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})
        ## Related Products
        uidata.append({"start": "true", "class": "ins-flex ins-col-12"})
        uidata.append({"_data": "Related Products", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-text-upper","style":"font-size:36px"})
        uidata.append({"class": "ins-space-l"})
        rpdata = self.ins._db._get_data("gla_product","*", f"   fk_product_category_id={data["fk_product_category_id"]} and id <>{data["id"]} limit 0,4 ")
        uidata.append({"start": "true", "class": "ins-flex-space-between ins-col-12"})
        for d in rpdata:
            uidata+= ELUI(self.ins).shop_pro_block(d,self.ins._server._url({"id":d["id"]}))

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})
        return self.ins._ui._render(uidata)  
    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        rq = self.ins._server._req()
        return self._ui(rq)
