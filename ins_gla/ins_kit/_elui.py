from ins_kit.ins_parent import ins_parent
class ELUI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
    def page_title(self, title="", bc=[{}], right_ui=[]):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-white ins-border ins-border-top"},
            {"start": "true", "class": "gla-container ins-flex ins-padding-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": "/", "_data": "Home /",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        for b in bc:
            if "href" in b:
                uidata.append({"_type": "a", "href": b["href"], "_data": b["_data"],
                              "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
            else:
                uidata.append({"_data":  b["_data"],
                               "class": " ins-title-12  ins-text-upper	ins-grey-color ins-strong-m"})
        uidata.append({"end": "true"})
        uidata.append({"_data": title,
                       "class": "ins-col-grow ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        if len(right_ui) > 0:
            uidata += right_ui
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
    def small_pro_block(self, data, string=False):
        p = "/ins_web/ins_uploads/"
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card"}, {"src": f"{p}{data.get("th_main", "")}", "_type": "img", "class": "ins-radius-m", "style": "    width: 97px;"}, {"start": "true", "class": "ins-col-8 ins-flex"}, {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"}, {"_data": data.get("title", ""), "class": "ins-col-12 ins-title-s	 ins-strong-l ins-grey-d-color", "style": "    !important;"}, {
                "_data": data.get("des", ""), "class": "ins-grey-color ins-col-12 ins-title-14", "style": "line-height: 20px; "}, {"end": "true"}, {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-12 ins-strong-l ins-primary-d-color ins-title-20"}, {"end": "true"}, {"_data": f"<i  class='lni lni-trash-3'></i>", "class": "ins-flex-center ins-col-1 -remove-item-cart-btn", "data-pid": data["id"]}, {"end": "true"}
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata

    def shop_pro_block(self,data,purl,st = "width:316px;"):
         p = "/ins_web/ins_uploads/"
         r = [
                    {"start": "true", "class": "ins-flex  gla-pro-block  ", "style": st},
                    {"start": "true", "class": " gla-img-cont  ", "style": ""},
                    {"_data": "Bestseller", "class": "ins-tag ins-primary-d ins-strong-m ins-text-upper ins-title-10","style": "position: absolute;top: 8px;left: 8px;border-radius: 2px !important;"},
                    {"src": p + data["th_main"], "_type": "img", "class": "gla-pro-img"},
                    {"src": p + data["th_overlay"], "_type": "img", "class": "gla-pro-himg"},
                    { "_type":"a" ,"href":purl,"_data": "SHOP NOW <i class=' lni ins-icon lni-arrow-right'></i>", "class": "ins-button gla-pro-hbutton ins-strong-m   ins-gold-bg","data-pid":f"{data['id']}"},
                    {"end": "true"},
                    {"class": "ins-space-s"},
                    {"_data": f"{data["title"]}", "class": "ins-col-12 ins-title-20	 ins-strong-m   ins-grey-color", "style": "line-height:24px"},
                    {"_data": f"{data["price"]}","_view":"currency","_currency_symbol":" EGP", "class": "ins-col-12  ins-strong-m  ins-primary-d-color", "style": "line-height:24px"},
                    {"end": "true"}
                ]
         return r




    def cart_pro_block(self,data,string=False):
        
        p = "/ins_web/ins_uploads/"
        item_total_des = int(float(data["count"]) * float(data["weight"]))
        item_total_amount = float(data["count"]) * float(data["price"])
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-border ins-radius-l ins-gap-o"},
            {"start": "true", "class": "ins-col-4 ins-flex-center","style": "height:160px;overflow: hidden;    border-radius: 8px 0px 0px 8px;"},
            {"src": f"{p}{data.get("th_main", "")}", "_type": "img","class": "ins-radius-m", "style": "    height: 100%;"},
            {"end": "true"},
            {"start": "true", "class": "ins-col-8  ins-flex-grow ins-primary-w ins-padding-l","style": "border-radius: 0px 8px 8px 0px;    border-left: 1px solid var(--primary-l);"},
            {"_data": "Item summary","class": "ins-col-12 ins-title-s ins-strong-l ins-grey-d-color"},
            {"_data": f"{data.get("count", "")} x {data["title"]}", "class": "ins-col-7 ins-strong-m ins-grey-color ins-title-14"},
            {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-5 ins-strong-m ins-grey-d-color ins-flex-end ins-title-14"},
            {"class": "ins-line ins-col-12"},
            {"_data": f"{item_total_des}gm  {data.get("category", "")} ", "class": "ins-col-7 ins-strong-m ins-grey-color ins-title-14"},
            {"_data": f"{item_total_amount}","_view":"currency","_currency_symbol":" EGP","class": "ins-col-5 ins-strong-m ins-grey-d-color ins-flex-end ins-title-14"},
            {"end": "true"},
            {"end": "true"}
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata
    def counter_pro_block(self,  data, string=False):
        p = "/ins_web/ins_uploads/"
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card"}, {"src": f"{p}{data.get("th_main", "")}", "_type": "img", "class": "ins-radius-m", "style": "    width: 97px;"}, {"start": "true", "class": "ins-col-6 ins-flex"}, {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"}, {"_data": data.get(
                "title", ""), "class": "ins-col-12 ins-title-20	 ins-strong-l ins-grey-d-color", "style": "    !important;"}, {"_data": data.get("des", ""), "class": "ins-grey-color ins-col-12 ins-title-14", "style": "line-height: 20px; "}, {"end": "true"}, {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP", "class": "ins-col-12 ins-strong-l ins-primary-d-color  ins-title-20"}, {"end": "true"},
            {"start": "true", "class": "ins-flex ins-col-3 -counter-cont ins-gap-o"},
            {"_data": "-", "class": "ins-button-s ins-flex-center ins-col-4 ins-gold-bg ins-font-2xl -minus-btn",
                "data-pid": data.get("id", 0)},
            {"_type": "input",  "name": "count_inpt", "type": "text",
                "value": data["count"], "pclass": "ins-col-4 ", "class": "count-inpt ins-title-xs ins-strong-l"},
            {"_data": "+", "class": "ins-button-s ins-flex-center  ins-col-4  ins-gold-bg ins-font-2xl  -plus-btn",
                "data-pid": data.get("id", 0)},
            {"end": "true"},
            {"_data": f"<i  class='lni lni-trash-3'></i>",
                "class": "ins-flex-center ins-col-1 -remove-item-cart-btn", "data-pid": data["id"]},
            {"end": "true"},
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata
    def counter_user_order_block(self,  data, string=False):
        p = "/ins_web/ins_uploads/"
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card"},
            
            
            
            {"src": f"{p}{data.get("product_th_main", "")}", "_type": "img", "class": "ins-radius-m", "style": "    width: 97px;"},
            
            
            {"start": "true", "class": "ins-col-grow ins-flex"},
            
            
            {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"},
            
            
            
            {"_data": data.get(
                "title", ""), "class": "ins-col-12 ins-title-20	 ins-strong-l ins-grey-d-color", "style": "    !important;"},
            {"_data": data.get(
                "des", ""), "class": "ins-grey-color ins-col-12 ins-title-14", "style": "line-height: 20px; "},
            {"_data": f' Count  ',
                "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": f' Price  ',
                "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": f' Total  ',
             "class": " ins-col-4  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
            {"_data": str(data["quantity"]),
             "class": " ins-col-4  ins-grey-d-color   ins-text-center ins-title-xs ins-strong-l"},
            {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP",
             "class": " ins-col-4  ins-grey-d-color  ins-text-center ins-title-xs ins-strong-l"},
            
            
            {"end": "true"},
            
            {"end": "true"},
            
            {"end": "true"},
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata


    def to_currency (self,  amount1):
        n= self.ins._data._format_currency(amount1,symbol=False) 
        return f"{n}EGP"