from ins_kit._engine._bp import App


class AppCal(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def d(self):
        return self.ins._json._file_read("test/a.json")

    def step(self, ops):
        data = self.d()
        r = {}
        lt = (ops["total"]/ops["count"])
        lf = lt-(lt/ops["offset"])
        for d in data:
            if float(d["Price"]) < lt and float(d["Price"]) > lf:
                r[d["id"]] = d
        x = 0
        xr = {}
        for k, a in r.items():
            if float(a["Price"]) > x:
                x = float(a["Price"])
                xr = a
        return xr

    def level(self, total, count=5, fill=[]):
        ops = {"offset": 10, "count": count, "total": total}
        d = self.step(ops)
        fill.append(d)
        count = count - 1
        if "Price" not in d:
            return fill
        if count > 0:
            nt = total - float(d["Price"])
            self.level(nt, count, fill)
        return fill

    def search(self):
        total = 500000
        ops = {"f": 4, "t": 9}
        xl = 0
        for i in range(ops["f"], ops["t"]+1):
            l = self.level(total, i, [])
            lc = 0
            rl = {}
            for k in l:
                if "Price" in k:
                    lc += float(k["Price"])
                    if int(k["id"]) in rl:
                        rl[int(k["id"])]["count"] += 1
                    else:
                        k["count"] = 1
                        rl[int(k["id"])] = k
            if lc > xl:
                xl = lc
                x = rl
        return x

    def ui(self):

        product = self.ins._db._get_data("gla_product","*","id='1'")
        p = "/ins_web/ins_uploads/"
        uidata = []
       
       
       
       
        title = [
            {"start": "true", "class": "ins-white"},
            {"start": "true", "class": " ins-flex-center gla-container ins-padding-xl "},
            {"_data": "Gold calculator", "style": "position: absolute;left: 20px;",
                "class": "ins-title-l ins-padding-xl ins-strong-m ins-text-upper"},
            {"start": "true", "class": "  ins-flex  ins-border ins-padding-m ins-radius-m"},
            {"_data": "E£", "class": "ins-border-end ins-padding-m ins-padding-h",
                "style": "height: 24px;line-height: 24px;"},
            {"_type": "input", "placeholder": "0000,00",
                "type": "text", "class": "ins-input-none"},
            {"_data": "<i class='lni ins-white-color lni-arrow-right'></i>",
                "class": "ins-button-s  ins-gold"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        uidata += title
      
        uidata.append({"class":"ins-space-2xl"})

        filter = [
            {"start":"true","class":"ins-col-12 ins-flex-end  gla-container"},
            {"_data":"Filter by","class":"ins-strong-m ins-grey-d-color","style":"font-size:14px"},
            {"_data": "Mix", "name":"type","class": "ins-button-s  -type-btn ins-strong-m ins-active"},
            {"_data": "24 Karat (Gold Bars)","class": "ins-button-s  -type-btn ins-strong-m "},
            {"_data": "21 Karat (Gold Coins)","class": "ins-button-s  -type-btn ins-strong-m "},
            {"end":"true"}
          
        ]
        uidata += filter

        ## 1 - 3 items
        body = [
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-white ins-radius-xl ins-border  gla-container "},
            {"start": "true", "class": " ins-flex ins-padding-xl  ins-col-12"},
            {"_data": " 1 - 3 items","class": "ins-font-l ins-strong-l ins-grey-d-color"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": " ins-radius-l ins-border ins-col-12 ins-flex","style": "overflow: hidden;"},
            {"start": "true", "class": "  ins-col-grow ins-padding-xl ins-flex"},

        ]
        uidata += body
        for pro in product:
            products = [
                {"start": "true", "style":"width:210px"},
                {"start": "true", "class": " product-img-cont ","style": ""},
                {"src": p + pro["th_main"], "_type": "img"},
                {"end": "true"},
                {"class": "ins-space-xl"},
                {"_data":pro["title"],"class":"ins-strong-m ins-grey-color ins-text-upper","style":"    line-height: 20px;"},
                {"_data":str(pro["price"]),"class":"ins-strong-m ins-primary-d-color ","style":"font-size:14px:"},
                {"class": "ins-space-s"},
                {"_data":f"Qty: 3","class":"ins-strong-l ins-grey-color "},
                {"end": "true"}
        ]
            uidata += products
        summary = [
            {"end": "true"},
            {"start": "true", "class": "ins-primary-w ins-padding-l ins-flex ins-gap-o", "style": "width:360px"},
            {"_data": "Item summary","class":"ins-col-12 ins-font-m ins-grey-d-color ins-strong-l"},
            {"class": "ins-space-xl"},
            {"_data": "3 x Gold bar 10G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-s"},
            {"class": "ins-line ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "Total 24K 30G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-2xl"},
            {"_data": "ADD TO CART <i class = 'lni lni-arrow-right ins-white-color'></i>", "class": "ins-col-12 ins-button-s ins-flex-center  ins-white-color ins-strong-m ins-gold-d -add-cart-btn","style":"    height: 32px;    border: 1px solid var(--primary-d);font-size:14px;"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            ]
        uidata += summary


        ## 4 - 9 items
        body = [
            {"class": "ins-space-xl"},
            {"start": "true", "class": "ins-white ins-radius-xl ins-border  gla-container "},
            {"start": "true", "class": " ins-flex ins-padding-xl  ins-col-12"},
            {"_data": " 4 - 9 items","class": "ins-font-l ins-strong-l  ins-grey-d-color"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": " ins-radius-l ins-border ins-col-12 ins-flex","style": "overflow: hidden;"},
            {"start": "true", "class": "  ins-col-grow ins-padding-xl ins-flex"},

        ]
        uidata += body
        for pro in product:
            products = [
                {"start": "true", "style":"width:210px"},
                {"start": "true", "class": " product-img-cont ","style": ""},
                {"src": p + pro["th_main"], "_type": "img"},
                {"end": "true"},
                {"class": "ins-space-xl"},
                {"_data":pro["title"],"class":"ins-strong-m ins-grey-color ins-text-upper","style":"    line-height: 20px;"},
                {"_data":str(pro["price"]),"class":"ins-strong-m ins-primary-d-color ","style":"font-size:14px:"},
                {"class": "ins-space-s"},
                {"_data":f"Qty: 3","class":"ins-strong-l ins-grey-color"},
                {"end": "true"}
        ]
            uidata += products
        summary = [
            {"end": "true"},
            {"start": "true", "class": "ins-primary-w ins-padding-l ins-flex ins-gap-o", "style": "width:360px"},
            {"_data": "Item summary","class":"ins-col-12 ins-font-m ins-grey-d-color ins-strong-l"},
            {"class": "ins-space-xl"},
            {"_data": "3 x Gold bar 10G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-s"},
            {"class": "ins-line ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "Total 24K 30G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-2xl"},
            {"_data": "ADD TO CART <i class = 'lni lni-arrow-right ins-white-color'></i>", "class": "ins-col-12 ins-button-s ins-flex-center  ins-white-color ins-strong-m ins-gold-d -add-cart-btn","style":"    height: 32px;    border: 1px solid var(--primary-d);font-size:14px;"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            ]
        uidata += summary
      

        ## 10 - 24 items
        body = [
            {"class": "ins-space-xl"},
            {"start": "true", "class": "ins-white ins-radius-xl ins-border  gla-container "},
            {"start": "true", "class": " ins-flex ins-padding-xl  ins-col-12"},
            {"_data": " 10 - 24 items","class": "ins-font-l ins-strong-l  ins-grey-d-color"},
            {"class": "ins-line ins-col-12"},
            {"start": "true", "class": " ins-radius-l ins-border ins-col-12 ins-flex","style": "overflow: hidden;"},
            {"start": "true", "class": "  ins-col-grow ins-padding-xl ins-flex"},

        ]
        uidata += body
        for pro in product:
            products = [
                {"start": "true", "style":"width:210px"},
                {"start": "true", "class": " product-img-cont ","style": ""},
                {"src": p + pro["th_main"], "_type": "img"},
                {"end": "true"},
                {"class": "ins-space-xl"},
                {"_data":pro["title"],"class":"ins-strong-m ins-grey-color ins-text-upper","style":"    line-height: 20px;"},
                {"_data":str(pro["price"]),"class":"ins-strong-m ins-primary-d-color ","style":"font-size:14px:"},
                {"class": "ins-space-s"},
                {"_data":f"Qty: 3","class":"ins-strong-l ins-grey-color"},
                {"end": "true"}
        ]
            uidata += products
        summary = [
            {"end": "true"},
            {"start": "true", "class": "ins-primary-w ins-padding-l ins-flex ins-gap-o", "style": "width:360px"},
            {"_data": "Item summary","class":"ins-col-12 ins-font-m ins-grey-d-color ins-strong-l"},
            {"class": "ins-space-xl"},
            {"_data": "3 x Gold bar 10G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-s"},
            {"class": "ins-line ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "Total 24K 30G","class":"ins-col-6 ins-strong-m ins-grey-color"},
            {"_data": "E£ 208,750.00","class":"ins-col-6  ins-grey-d-color ins-strong-l ins-flex-end"},
            {"class": "ins-space-2xl"},
            {"_data": "ADD TO CART <i class = 'lni lni-arrow-right ins-white-color'></i>", "class": "ins-col-12 ins-button-s ins-flex-center  ins-white-color ins-strong-m ins-gold-d -add-cart-btn","style":"    height: 32px;    border: 1px solid var(--primary-d);font-size:14px;"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            ]
        uidata += summary

        uidata.append({"class":"ins-space-4xl"})
        

        r = self.ins._ui._render(uidata)
        return r

    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        return self.ui()
