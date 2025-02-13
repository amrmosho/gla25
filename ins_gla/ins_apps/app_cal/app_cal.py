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
        w =  f" price>='{lf}'  and  price<='{lt}' and fk_product_category_id <> '3' "
        if "type" in ops:
            if ops["type"] == "bars":
                w += " and fk_product_category_id = '1'"
            elif ops["type"] == "coins":
                w += " and fk_product_category_id = '2'"

        r = self.ins._db._get_data(
            "gla_product", "*",w)

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

    def level(self, total, count=5, fill=[],type = ""):
        ops = {"offset": self.offset, "count": count, "total": total,"type":type}
        d = self.step(ops, fill)
        fill.append(d)
        count = count - 1
        if "price" not in d:
            return fill
        if count > 0:
            nt = total - float(d["price"])
            self.level(nt, count, fill,type)
        return fill

    def search(self, total, ops,type):
        x= {}
        xl = 0
        for i in range(ops["f"], ops["t"]+1):
            l = self.level(total, i, [],type)
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
        return ELUI(self.ins)._cart_lightbox_ui()

    def ui_header(self ,total):


        uidata = [
            {"start": "true", "class": "ins-white"},
                {"start": "true", "class": " ins-flex-center gla-container ins-padding-xl "},
                {"_data": "Gold calculator", "_data-ar":"حاسبة الذهب","_trans":"true","style": "position: absolute;left: 20px;",
                    "class": "ins-title-l ins-padding-xl ins-strong-m ins-text-upper"},
                {"start": "true", "class": "  ins-flex  ins-border ins-padding-m ins-radius-m"},
                {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h",
                    "style": "height: 24px;line-height: 24px;"},
                {"_type": "input", "value":total, "placeholder": "Enter your amount",
                    "type": "text", "class": " -cal-update-nput ins-input-none"},
                {"_data": "<i class='lni ins-white-color lni-arrow-right'></i>",
                    "class": "ins-button-s  -cal-update-btn ins-gold-d"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}
            ]



        r = self.ins._ui._render(uidata)
        return r




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
                    {"src": p + pro["th_main"], "loading":"lazy","_type": "img"},
                    {"end": "true"},
                    {"class": "ins-space-xl"},
                    {"_data": pro["title"], "class": "ins-strong-m ins-grey-color ins-text-upper",
                        "style": "    line-height: 20px;"},
                    {"_data": str(pro["price"]),"_view":"currency","_currency_symbol":" EGP",  "class": "ins-strong-m ins-primary-d-color ins-title-14"},
                    {"class": "ins-space-s"},
                    {"_data": f"Qty: {pro["count"]}",
                        "class": "ins-strong-l ins-grey-color "},
                    {"end": "true"},
                    {"end": "true"}
                ]
                inputs = [
                    {"start": "true", "class": " product-data-area ins-hidden","data-mname":uniq},
                    {"_type": "input","type":"text","value":pro["id"],"pclass":"ins-col-12","name":"product_id"},
                    {"_type": "input","type":"text","value":pro["count"],"pclass":"ins-col-12","name":"count"},
                    {"end": "true"}
                ]
                uidata += products
                uidata += inputs
                uniq = 0

           
            summary = [
                {"end": "true"},
                {"start": "true", "class": "ins-primary-w ins-padding-l ins-flex ins-gap-o","style": "width:400px"},
                {"_data": "Item summary","_data-ar":"ملخص العنصر","_trans":"true","class": "ins-col-12 ins-title-xs ins-grey-d-color ins-strong-l"},
                {"class": "ins-space-xl"}
                ]
            total = 0
            for k, pro in product.items():
                stotal = float(pro["count"]) * float(pro["price"])
                total +=stotal
                summary+=[{"_data": f"{pro["count"]} x {pro["title"]}","class": "ins-col-6 ins-strong-m ins-grey-color"},
                          {"_data": str(stotal),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"}]

            summary+=[
                {"class": "ins-space-s"},
                {"class": "ins-line ins-col-12"},
                {"class": "ins-space-s"},
                {"_data": "Total", "_data-ar":"المجموع","_trans":"true","class": "ins-col-6 ins-strong-m ins-grey-color"},
                {"_data": str(total),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
                {"class": "ins-space-2xl"},
                {"_data": "ADD TO CART <i class = 'lni lni-arrow-right ins-white-color'></i>", "class": "ins-col-12 ins-button-s ins-flex-center  ins-white-color ins-strong-m ins-gold-d -add-cart-btn ins-title-14","style": "    height: 32px;    border: 1px solid var(--primary-d);"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"}]

            uidata += summary

        return uidata


    def ui_body(self, total):
        g = self.ins._server._get()
        type = ""
        if "id" in g:
            type = g["id"]
        fproduct = self.search(total, {"f": 1, "t": 3},type)
        sproduct = self.search(total, {"f": 4, "t": 9},type)
        tproduct = self.search(total, {"f": 10, "t": 24},type)

        if len(fproduct) == 0 and len(sproduct) == 0 and len(tproduct) == 0:
            uidata = [
            {"class":"ins-space-l"},
            {"_data":"The entered amount doesn't match any available plan","_data-ar":"المبلغ المدخل لا يتطابق مع أي خطة متاحة","_trans":"true","class":"gla-container ins-card ins-padding-m ins-flex-center ins-col-6"}
            ]
            return self.ins._ui._render(uidata)
       
       
        uidata=[  {"class":"ins-space-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex-end  gla-container"},
             {"_data": "Filter by",  "_data-ar":"تصفية حسب","class": "ins-strong-m ins-grey-d-color ins-title-14"}]
        fdata = [
            {"name":"mix","title":"Mix","title_ar":"مزج","url":f"{self.ins._server._url({},"id")}"},
            {"name":"bars","title":"24 Karat (Gold Bars)","title_ar":"سبائك الذهب عيار 24","url":"bars"},
            {"name":"coins","title":"21 Karat (Gold Coins)","title_ar":"21 قيراط (عملات ذهبية)","url":"coins"}
                   ]
        
        for f in fdata:
            aclass = ""
            if "id" in g and g["id"] == f["name"] or "id" not in g and  f["name"] == "mix" :
                aclass = "ins-active"
            
            
            uidata+= [{"_data": f["title"],"_trans":"true","_data-ar":f["title_ar"],"_type":"a","href":f["url"],"class": f"ins-button-s {aclass}  -type-btn ins-strong-m"}]

        uidata.append( {"end": "true"})
        
        
        i = 1
        plan_data = [
            (fproduct),
            (sproduct),
            (tproduct)
        ]

        for product in plan_data:
            if product:
                title = f"Option {i}"
                uidata += self.plan_ui(product, title)
                i += 1


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
            {"_type": "img","loading":"lazy", "src": img},
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
        uidata.append({"_data":"Start your saving plan today and see the value of your money in gold!","_data-ar": "ابدأ خطة الادخار الخاصة بك اليوم وشاهد قيمة أموالك بالذهب!","_trans": "true", "class": "ins-col-12 ins-title-20 ins-text-upper ins-grey-d-color ins-strong-m"})
        uidata.append({"class":"ins-space-xs"})  
        uidata.append({"class":"ins-line ins-col-12"})  
        uidata.append({"class":"ins-space-xs"})  
       
        uidata.append({"start":"true", "class":"ins-col-12 ins-flex","style":"position:relative"})
        uidata.append({"class":"ins-line-vertical","style":"    height: 475px;position: absolute;left: -6px;top: 0;"})    
        steps_ar = [
        (f"{p}money_circle.svg", "مدخراتك", "أدخل مبلغ مدخراتك"),
        (f"{p}wallet_circle.svg", "اكتشف الذهب ضمن ميزانيتك", "اكتشف منتجات الذهب بناءً على ميزانيتك."),
        (f"{p}cart_circle.svg", "راجع سلة التسوق", "راجع سلة التسوق الخاصة بك للمتابعة مع اختيارك."),
        (f"{p}order_circle.svg", "أكمل طلبك", "أدخل تفاصيل الشحن الخاصة بك، ثم قم بتأكيد الطلب."),
        (f"{p}truck_circle.svg", "استمتع بالتوصيل إلى المنزل", "استرخ واستمتع بتوصيل مدخراتك الذهبية إلى باب منزلك بأمان وراحة.")
        ]
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
        uidata.append({"_data": "Gold calculator", "_data-ar":"حاسبة الذهب","_trans":"true","class": "ins-title-xl ins-grey-d-color ins-strong-m ins-col-12 ins-text-upper","style":"    line-height: 40px;"})
        uidata.append({"_data": "See how much gold you can own!","_data-ar":" شاهد كم من الذهب يمكنك أن تملكه!","_trans":"true", "class": "ins-title-20 ins-grey-color ins-col-12 "})
        uidata.append({"class": "ins-space-l"})

        uidata += [
                {"start": "true", "class": "  ins-flex  ins-border ins-radius-m ins-padding-m ","style":"width: 720px;background-color: white;"},
                {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h ins-title-20 ins-grey-color",
                    "style": "height: 24px;line-height: 24px;"},
                {"_type": "input",  "placeholder": "Enter your amount","_placeholder-ar":"أدخل المبلغ الخاص بك","_trans":"true",
                    "type": "text", "class": " -cal-update-nput ins-input-none","pclass":"ins-col-grow"},
                {"_data": "CALCULATOR <i class='lni ins-white-color lni-arrow-right'></i>","_data-ar":"احسب ","_trans":"true",
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
