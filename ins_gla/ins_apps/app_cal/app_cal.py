from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
import uuid
import json


class AppCal(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def d(self):
        return self.ins._json._file_read("test/a.json")

    @property
    def offset(self):
        return 10
    
    @property
    def session_name(sel):
        return "glaproducts"

    def step(self, ops, fill):
        r = []
        lt = (ops["total"]/ops["count"])
        lf = lt-(lt/ops["offset"])

        r = self.ins._db._get_data(
            "gla_product", "*", f" price>='{lf}'  and  price<='{lt}'")

        if len(r) == 0:
            for f in fill:
                if f["price"] <= lt:
                    r = [f]

        x = 0
        xr = {}
        if len(r) > 0:
            for a in r:
                if float(a["price"]) >= x:
                    x = float(a["price"])
                    xr = a
        return xr

    def level(self, total, count=5, fill=[]):
        ops = {"offset": self.offset, "count": count, "total": total}
        d = self.step(ops, fill)
        fill.append(d)
        count = count - 1
        if "price" not in d:
            return fill
        if count > 0:
            nt = total - float(d["price"])
            self.level(nt, count, fill)
        return fill

    def search(self, total, ops):
        x= {}
        xl = 0
        for i in range(ops["f"], ops["t"]+1):
            l = self.level(total, i, [])
            lc = 0
            rl = {}
            for k in l:
                if "price" in k:
                    lc += float(k["price"])
                    if int(k["id"]) in rl:
                        rl[int(k["id"])]["count"] += 1
                    else:
                        k["count"] = 1
                        rl[int(k["id"])] = k
            if lc >= xl:
                xl = lc
                x = rl
        return x





    def _cart_lightbox_ui(self):

        data = self.ins._server._post()["data"]
        products = json.loads(data)

        for k, p in products.items():
                
            pro= self.ins._db._jget("gla_product", "*", f"gla_product.id={p["product_id"]}")
            pro._jwith("gla_product_category category", "title,id", rfk="fk_product_category_id" ,join="left join")
            ddata = pro._jrun()

            for data in ddata:

                sedata=self.ins._server._get_session(self.session_name)
                if type(sedata) != dict:
                    sedata ={}
                adddata = {"id":data["id"] ,"title":data["title"],"category":data["category_title"] ,"weight":data["weight"] ,"price" :data["price"],"des" :data.get("des" ,"") ,"th_main" :data["th_main"]  ,"count":p["product_count"] }
                sedata[str(data["id"])] =adddata

                self.ins._server._set_session(self.session_name,sedata)


                sedata=self.ins._server._get_session(self.session_name)

                uidata=[
                    {"class":"ins-space-l"}
                    ,{"start":True ,"class":"ins-col-12 ins-flex -cart-cont"}]


                for k,v in sedata.items():
               
                    uidata+= ELUI(self.ins).cart_pro_block(v)
                    uidata.append({"class":"ins-space-xs"})


                footer=[{"start":True ,"class":"ins-flex-space-between ins-col-12 ins-padding-l"},

                {"_data":"Continue Shopping" ,"class":"ins-button-s  ins-text-upper ins-gold-d ins-col-6 -continue-shopping-btn"},
                {"_data":"To cart","_type":"a","href":"/checkout/cart" ,"class":"ins-button-s  ins-gold-d  ins-text-upper ins-col-5"},
                {"end":True},
                                    {"class":"ins-space-l"}

                
                ]

                uidata += footer
                
                uidata.append({"end":True})


        return self.ins._ui._render(uidata)      


    def ui_header(self ,total):


        uidata = [
            {"start": "true", "class": "ins-white"},
                {"start": "true", "class": " ins-flex-center gla-container ins-padding-xl "},
                {"_data": "Gold calculator", "style": "position: absolute;left: 20px;",
                    "class": "ins-title-l ins-padding-xl ins-strong-m ins-text-upper"},
                {"start": "true", "class": "  ins-flex  ins-border ins-padding-m ins-radius-m"},
                {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h",
                    "style": "height: 24px;line-height: 24px;"},
                {"_type": "input", "value":total, "placeholder": "Enter your amount",
                    "type": "number", "class": " -cal-update-nput ins-input-none"},
                {"_data": "<i class='lni ins-white-color lni-arrow-right'></i>",
                    "class": "ins-button-s  -cal-update-btn ins-gold-d"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]



        r = self.ins._ui._render(uidata)
        return r


    def plan_ui(self,product,title):
        p = "/ins_web/ins_uploads/"
        uidata = []
        uniq = 0

        if len(product) !=0:
            body = [
                {"class": "ins-space-l"},
                {"start": "true", "class": "ins-white ins-radius-xl ins-border  gla-container "},
                {"start": "true", "class": " ins-flex ins-padding-xl  ins-col-12"},
                {"_data": title, "class": "ins-title-20	 ins-strong-l ins-grey-d-color"},
                {"class": "ins-line ins-col-12"},
                {"start": "true", "class": " ins-radius-l ins-border ins-col-12 ins-flex -plan-body",
                    "style": "overflow: hidden;"},
                {"start": "true", "class": "  ins-col-grow ins-padding-xl ins-flex"},

            ]
            uidata += body
            for k, pro in product.items():
                uniq = str(uuid.uuid4())[:8]
                products = [
                    {"start": "true", "class":"ins-col-grow"},

                    {"start": "true", "style": "width:210px"},
                    {"start": "true", "class": " product-img-cont ", "style": ""},
                    {"src": p + pro["th_main"], "_type": "img"},
                    {"end": "true"},
                    {"class": "ins-space-xl"},
                    {"_data": pro["title"], "class": "ins-strong-m ins-grey-color ins-text-upper",
                        "style": "    line-height: 20px;"},
                    {"_data": str(
                        pro["price"]), "class": "ins-strong-m ins-primary-d-color ins-title-14"},
                    {"class": "ins-space-s"},
                    {"_data": f"Qty: {pro["count"]}",
                        "class": "ins-strong-l ins-grey-color "},
                    {"end": "true"},
                    {"end": "true"}
                ]
                inputs = [
                    {"start": "true", "class": " product-data-area ins-hidden","data-mname":uniq},
                    {"_type": "input","type":"text","value":pro["id"],"pclass":"ins-col-12","name":"product_id"},
                    {"_type": "input","type":"text","value":pro["count"],"pclass":"ins-col-12","name":"product_count"},
                    {"end": "true"}
                ]
                uidata += products
                uidata += inputs
                uniq = 0

           
            summary = [
                {"end": "true"},
                {"start": "true", "class": "ins-primary-w ins-padding-l ins-flex ins-gap-o","style": "width:360px"},
                {"_data": "Item summary","class": "ins-col-12 ins-title-xs ins-grey-d-color ins-strong-l"},
                {"class": "ins-space-xl"}
                ]
            total = 0
            for k, pro in product.items():
                stotal = float(pro["count"]) * float(pro["price"])
                total +=stotal
                summary+=[{"_data": f"{pro["count"]} x {pro["title"]}","class": "ins-col-8 ins-strong-m ins-grey-color"},
                          {"_data": str(stotal),"class": "ins-col-4  ins-grey-d-color ins-strong-l ins-flex-end"}]

            summary+=[
                {"class": "ins-space-s"},
                {"class": "ins-line ins-col-12"},
                {"class": "ins-space-s"},
                {"_data": "Total", "class": "ins-col-6 ins-strong-m ins-grey-color"},
                {"_data": str(total),"class": "ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
                {"class": "ins-space-2xl"},
                {"_data": "ADD TO CART <i class = 'lni lni-arrow-right ins-white-color'></i>", "class": "ins-col-12 ins-button-s ins-flex-center  ins-white-color ins-strong-m ins-gold-d -add-cart-btn ins-title-14","style": "    height: 32px;    border: 1px solid var(--primary-d);"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}]

            uidata += summary

        return uidata


    def ui_body(self, total):
        fproduct = self.search(total, {"f": 1, "t": 3})
        sproduct = self.search(total, {"f": 4, "t": 9})
        tproduct = self.search(total, {"f": 10, "t": 24})

        if len(fproduct) == 0 and len(sproduct) == 0 and len(tproduct) == 0:
            uidata = [
            {"class":"ins-space-l"},
            {"_data":"The entered amount doesn't match any available plan","class":"gla-container ins-card ins-padding-m ins-flex-center ins-col-6"}
            ]
            return self.ins._ui._render(uidata)
       
       
        uidata=[]
        filter = [
            {"class":"ins-space-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex-end  gla-container"},
            {"_data": "Filter by", "class": "ins-strong-m ins-grey-d-color ins-title-14"},
            {"_data": "Mix", "name": "type",
                "class": "ins-button-s  -type-btn ins-strong-m ins-active"},
            {"_data": "24 Karat (Gold Bars)",
             "class": "ins-button-s  -type-btn ins-strong-m "},
            {"_data": "21 Karat (Gold Coins)",
             "class": "ins-button-s  -type-btn ins-strong-m "},
            {"end": "true"}

        ]
        uidata += filter

        uidata += self.plan_ui(fproduct,"1 - 3 items")
        uidata += self.plan_ui(sproduct,"4 - 9 items")
        uidata += self.plan_ui(tproduct,"10 - 24 items")

        uidata.append({"class": "ins-space-4xl"})

        r = self.ins._ui._render(uidata)
        return r

    def ui_body_nodata(self):
        uidata = [
            {"class":"ins-space-l"},
            {"_data":"Please enter an amount to view the results","class":"gla-container ins-card ins-padding-m ins-flex-center ins-col-6"}
            ]
        return self.ins._ui._render(uidata)
    


    def create_step(self,img, title, des):
        return [
            {"start": "true", "class": "ins-col-12 ins-flex", "style": "z-index: 1;"},
            {"_type": "img", "src": img},
            {"start": "true", "class": "ins-col-10"},
            {"_data": title, "class": "ins-title-xs ins-grey-d-color ins-strong-l", "style": "line-height: 24px;"},
            {"_data": des, "class": "ins-title-14 ins-grey-color", "style": "line-height: 20px;"},
            {"end": "true"},
            {"end": "true"},
            {"class": "ins-space-2xl"}
        ]


    def home_ui(self):
        p = "/ins_web/ins_uploads/style/"
        uidata = [{"start":"true", "class":"ins-col-12 ins-flex ins-padding-l gla-container"}]
       
       
        uidata.append({"start":"true", "class":"ins-flex ins-radius-xxl ins-padding-xl","style":"width:535px;background-color: white;"})
        uidata.append({"_data":"Start your saving plan today and see the value of your money in gold!", "class": "ins-col-12 ins-title-20 ins-text-upper ins-grey-d-color ins-strong-m"})
        uidata.append({"class":"ins-space-xs"})  
        uidata.append({"class":"ins-line ins-col-12"})  
        uidata.append({"class":"ins-space-xs"})  
       
        uidata.append({"start":"true", "class":"ins-col-12 ins-flex","style":"position:relative"})
        uidata.append({"class":"ins-line-vertical","style":"    height: 475px;position: absolute;left: -6px;top: 0;"})    
        steps = [
        (f"{p}money_circle.svg", "Your savings", "Insert Your Savings Amount"),
        (f"{p}wallet_circle.svg", "Discover gold within your budget", "Discover gold products based on your budget."),
        (f"{p}cart_circle.svg", "Review your cart", "Review your cart to proceed with your selection."),
        (f"{p}order_circle.svg", "Complete your order", "Fill in your delivery details, and confirm your order."),
        (f"{p}truck_circle.svg", "Enjoy Home Delivery", "Sit back and relax as your gold savings is delivered directly to your doorstep, securely and conveniently.")
    ]

        for img, title, des in steps:
            uidata.extend(self.create_step(img, title, des))
            
        uidata.append({"end":"true"})


        uidata.append({"end": "true"})

        uidata.append({"start":"true", "class":" ins-col-grow ins-flex-center ins-text-center"})

        uidata.append({"start":"true", "class":"ins-flex","style":"max-width: 720px;"})
        uidata.append({"_data": "Gold calculator", "class": "ins-title-xl ins-grey-d-color ins-strong-m ins-col-12 ins-text-upper","style":"    line-height: 40px;"})
        uidata.append({"_data": "See how much gold you can own!", "class": "ins-title-20 ins-grey-color ins-col-12 "})
        uidata.append({"class": "ins-space-l"})

        uidata += [
                {"start": "true", "class": "  ins-flex  ins-border ins-radius-m ins-padding-m ","style":"width: 720px;background-color: white;"},
                {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h ins-title-20 ins-grey-color",
                    "style": "height: 24px;line-height: 24px;"},
                {"_type": "input",  "placeholder": "Enter your amount",
                    "type": "number", "class": " -cal-update-nput ins-input-none","pclass":"ins-col-grow"},
                {"_data": "CALCULATOR <i class='lni ins-white-color lni-arrow-right'></i>",
                    "class": "ins-button-s  -cal-update-btn ins-gold-d ins-flex-center","style":"height: 46px;"},
                {"end": "true"}
            ]
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
     

        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space-4xl"})

        return self.ins._ui._render(uidata)
        

    def out(self):

        rq = self.ins._server._get()

        if "mode" in rq and "mode" !="":
            total = int(self.ins._server._get("mode", "0"))
                    
            r = self.ui_header(str(total))
                    
            if total ==0:
                r += self.ui_body_nodata()

            else:
             r += self.ui_body( total)

        else:
            r= self.home_ui()

        self.app._include("style.css")
        self.app._include("script.js")
        return r
