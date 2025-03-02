from urllib.parse import parse_qs
from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
import json

class AppProductDetails(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def _show_subtypes(self,subtypes,stys="",string=False):
       
        subtypes = {k: v for k, v in sorted(subtypes.items(), key=lambda item: int(item[1].get("order",float('1'))))}

        if subtypes:
            uidata = [
            {"start":"true","class":"ins-flex ins-col-12"},
            {"_data": "Subtype","_data-ar": "نوع فرعي","_trans":"true", "class": "ins-col-12 ins-grey-d-color ins-strong-l  ins-title-xs  "}
            ]
            for v,s in subtypes.items():
                sdata = self.ins._db._get_row("gla_product_types","title,kit_lang",f"alias='{v}'",update_lang=True)
                active = "ins-active" if v == stys else ""
                uidata +=[{"_data": sdata["title"], "name":"type","data-name": v,"data-tid": s["id"],"class": f"ins-button-s  -subtype-inner-btn ins-flex-center ins-strong-m -product-filter-input {active}"}]
            uidata.append({"end":"true"})
            if string:
                return self.ins._ui._render(uidata)
            else:
             return uidata


    def calculate_charge(self,data):
        chargs = 0
        if data["gram"] == 1:
            chargs = (float(data["stamp"]) + float(data["vat"]) ) * float(data["weight"])
        else:
            chargs = (float(data["weight"])  * float(data["vat"])  ) + float(data["stamp"]) 
        return chargs


    def calculate_chashback(self,data):
        chashback = 0
        if data["cashback_gram"] == 1:
            chashback = float(data["cashback"]) * float(data["weight"])
        else:
            chashback = data["cashback"]
        return chashback


    
    def _ui(self,rq):
        data = self.ins._db._get_row("gla_product", "*", f"id={rq["id"]}")
        filter_data = {}
        stys = ""
        tys = ""
        if rq.get("type") and rq["type"]:
            parsed_data = parse_qs(rq["type"])
            filter_data = {key: value[0] for key, value in parsed_data.items()}
            stys = filter_data.get("subtypes", "")
            tys = filter_data.get("types", "")



        if not stys:
         if data["fk_product_category_id"] == 2:
             stys = "george"
         else:
             stys = "standard"

        if not tys:
         if data["fk_product_category_id"] == 2:
             tys = "royal"
         else:
             tys = "standard"



        if not data:
            return self.ins._ui._error("Product not found") 
        uidata = [
            {"start": "true", "class": "ins-flex-valign-start  gla-container ins-col-12 ins-padding-2xl ins-gap-m"},
        ]   
        home_url = self.ins._server._url({},["mode","id","alias"])
        product_url = self.ins._server._url({},["mode","id"])
       
        path = [
            {"start":"true","class":"ins-col-12 ins-flex ins-text-upper"},
            {"_type":"a","href":home_url,"_data": "Home /","_data-ar":"الرئيسية /","_trans":"true","class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_type":"a","href":product_url,"_data": "Product /","_data-ar":"منتجات /","_trans":"true", "class":" ins-title-12	ins-grey-d-color ins-strong-m"},
            {"_data": data["title"],"class":" ins-title-12	ins-grey-color ins-strong-m"},
            {"end":"true"}
            ]

        uidata+=path


    ## Images Container
        image = {data["th_main"],data["th_overlay"]}
        if data["types_data"] != None:
            types_data = json.loads(data["types_data"])
            if tys in types_data:
                if stys in types_data[tys]["data"]:
                    rimages = types_data[tys]["data"][stys]["images"]
                    image = rimages.split(",")
          

        uidata.append({"start": "true", "class": "ins-flex-valign-start ins-col-6  -side-mimg-cont "})
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
            uidata.append({"start": "true", "class":f"-side-img-cont ins-text-center ins-radius-l  {aclass}"})
            uidata.append({"src": p + i, "loading":"lazy","_type": "img","data-src":p + i,"class": f" ins-radius-m -side-img {aclass}", "style":"width:100%;"})  
            uidata.append({"end": "true"})
            uidata.append({"class": "ins-space-xs"})
        uidata.append({"end": "true"})
        uidata.append({"src": p + aimage, "loading":"lazy","_type": "img",
                 "class": " ins-radius-m ins-col-grow -main-img","style":"max-width:450px;"})
        uidata.append({"end": "true"})

        
        ## Data Container
        uidata.append({"start": "true", "class": "ins-flex ins-col-6 ins-card","style":"padding: 24px;"})

        
        ## Tags
        uidata.append({"_data": "Bestseller","_data-ar":"الأكثر مبيعًا","_trans":"true", "class": "ins-tag ins-primary-d ins-strong-m  ins-text-upper ins-title-10","style":"border-radius: 2px !important;"})
        uidata.append({"_data": "In Stock","_data-ar":"متوفر","_trans":"true", "class": "ins-tag ins-secondary  ins-strong-m  ins-text-upper ins-title-10","style":"border-radius: 2px !important;"})
        uidata.append({"class": "ins-space-xs"})


        ## Title
        uidata.append({"_data": data["title"], "class": "ins-col-12 ins-title-l ins-grey-d-color ins-strong-m ins-text-upper "})   

        uidata.append({"class": "ins-space-s"})

        scharges  = self.calculate_charge(data)
        sprice_before = float(data.get("price","")) -  float(scharges)
        if data["buy_price"]:
         cashback  = self.calculate_chashback(data)
         bprice_before = float(data.get("buy_price","")) -  float(cashback)
        else:
         bprice_before = 9000
         cashback = 100
         data["buy_price"] = 10000

        ## Sell Card
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-card ins-primary-w","style":"border-radius:8px 8px 0 0 !important;"})
        uidata.append({"_data": "Sell price","_data-ar":"سعر البيع","_trans":"true", "class": "ins-col-12  ins-grey-d-color ins-title-s	 ins-strong-l "})
        uidata.append({"_data": "Gold Amount","_data-ar":"كمية الذهب","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data":  str(sprice_before),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end "})
        uidata.append({"_data": "Making Charge + VAT","_data-ar":"رسوم التصنيع + ضريبة القيمة المضافة","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data": str(scharges), "_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total","_data-ar":"المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data":  str(data.get("price",10000)),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-strong-l ins-flex-end ins-title-20	 ins-primary-d-color"})
        vat = str(data["vat"])
        uidata.append({"_data": "Note: Vat amount is " + "<spam class='ins-grey-d-color'>  "+vat+" EGP</span>", "_data-ar":" ملحوظة: مبلغ ضريبة القيمة المضافة هو"+vat,"_trans":"true","class": "ins-col-8 ins-grey-color ins-strong-m ins-title-14"})
        uidata.append({"end": "true"})


        ## Buy Card
        uidata.append({"start": "true", "class": "ins-flex ins-col-12 ins-card ins-primary-bg  -open-panel","style":"border-radius: 0 0 8px 8px !important;position: relative;top: -8px;height: 65px;overflow: hidden;    border-top: 1px solid var(--primary-l)"})
        uidata.append({"_data": "We buy at","_data-ar":"نحن نشتري في","_trans":"true", "class": "ins-col-11  ins-grey-d-color ins-title-20	 ins-strong-l"})
        uidata.append({"_data":"<span class=' lni lni-chevron-up'></span>","class": "ins-col-1  ins-grey-color ins-font-xl ins-strong-l -buy-div"})
        uidata.append({"start": "true", "class": "ins-flex ins-col-12"})
        uidata.append({"_data": "Gold Amount","_data-ar":"كمية الذهب","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color ins-strong-m"})
        uidata.append({"_data": str(bprice_before),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({"_data": "Cash back","_data-ar":"استرداد النقود","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data": str(cashback),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-grey-d-color ins-title-xs ins-strong-l ins-flex-end"})
        uidata.append({ "class": "ins-line ins-col-12"})
        uidata.append({"_data": "Total","_data-ar":"المجموع","_trans":"true", "class": "ins-col-6  ins-title-xs  ins-grey-color  ins-strong-m"})
        uidata.append({"_data":  str(data.get("buy_price",9000)),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه",  "class": "ins-col-6  ins-strong-l ins-flex-end ins-title-20	 ins-primary-d-color"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        uidata.append({"class": "ins-space-s"})
       
        ## Product types
        if data["types_data"]:
            data["types_data"] = json.loads(data["types_data"])
            subtypes = []

            uidata.append({"_data": "Type", "_data-ar": "نوع", "_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-strong-l ins-title-xs"})
            for t_key, t_value in data["types_data"].items():
                active = ""
                cclass= ""
                tdata = self.ins._db._get_row("gla_product_types","title,kit_lang",f"alias='{t_key}'",update_lang=True)

                if tys == t_key:
                    active = "ins-active"
                    subtypes = t_value["data"]



                uidata.append({
                    "_data": tdata["title"],"data-name": t_key,"data-pid":data["id"],
                    "class": f"ins-button-s {active} {cclass} -type-inner-btn ins-strong-m ins-grey-color"
                })

  

            uidata.append({"start": "true", "class": "-subtypes-area ins-col-12"})
            uidata += self._show_subtypes(subtypes, stys, False)
            uidata.append({"end": "true"})

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

        lbtitle = "Cart"
        if self.ins._langs._this_get()["name"] == "ar":
            lbtitle = "السلة"

        uidata.append({"_data": "<img src='"+p+"style/cart.svg'></img> ADD TO CART","_data-ar":"أضف إلى السلة","_trans":"true","data-lbtitle":lbtitle,"data-pid": str(data["id"]), "data-subtype":stys,"data-type":tys,"class": "ins-button-s ins-flex-center ins-title-xs ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn","style":"    height: 46px;    border: 1px solid var(--primary-d);"})
        uidata.append({"end": "true"})
        ## Terms area
        uidata.append({"_data": "<img src='"+p+"style/truck.svg ' style='position: relative;top: 4px;'></img> Free shipping for orders above EGP200k","_data-ar":"شحن مجاني للطلبات التي تزيد عن 200 ألف جنيه مصري","_trans":"true", "class": "ins-col-12 ins-grey-color ins-title-14"})
        uidata.append({"_data": "<img src='"+p+"style/gift.svg' style='position: relative;top: 4px;'></img> Include gift Card?", "_data-ar":"تشمل كارت هدايا؟","_trans":"true","class": "ins-col-11 ins-grey-color ins-title-14"})
        uidata.append({"_type": "input",  "type": "checkbox","value":"0", "class": "ins-form-bool-f"})
        uidata.append({"class": "ins-space-s"})

        ## Product Description
        uidata.append({"start": "true", "class": "ins-flex ins-col-12   -open-panel ins-active","style":"height: 30px;overflow: hidden;"})  
        uidata.append({"_data": "Product Description","_data-ar":"وصف المنتج","_trans":"true", "class": "ins-col-11  ins-grey-d-color ins-title-xs ins-strong-m"})
        uidata.append({"_data":"  <span class=' lni lni-chevron-up'></span>","class": "ins-col-1  ins-grey-color ins-font-xl ins-strong-l"})
        uidata.append({"_data": data["des"], "class": "ins-col-12  ins-grey-color ins-title-14"})
        uidata.append({"end": "true"})

      
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})
        ## Related Products
        uidata.append({"start": "true", "class": "ins-flex ins-col-12"})
        uidata.append({"_data": "Related Products","_data-ar":"المنتجات ذات الصلة","_trans":"true", "class": "ins-col-12 ins-grey-d-color ins-strong-m ins-text-upper","style":"font-size:36px"})
        uidata.append({"class": "ins-space-l"})
        rpdata = self.ins._db._get_data("gla_product","*", f"   fk_product_category_id={data["fk_product_category_id"]} and id <>{data["id"]} limit 0,4 ",update_lang=True)
        uidata.append({"start": "true", "class": "ins-flex-space-between ins-col-12"})
        for d in rpdata:
            uidata+= ELUI(self.ins).shop_pro_block(d,self.ins._server._url({"id":d["id"]},["filter","type"]))

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

