from datetime import datetime, timedelta
import json
from ins_kit.ins_parent import ins_parent
class ELUI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
    
    @property
    def session_name(sel):
        return "glaproducts"
    


    def get_order_status(self,status,type="5"):
        data = self.ins._data._get_options(type)["content"]
        return json.loads(data[status])
    
    def page_title(self, title="",title_ar = "", bc=[{}], right_ui=[]):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-white ins-border ins-border-top"},
            {"start": "true", "class": "gla-container ins-flex ins-padding-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": "/", "_data": "Home /","_data-ar":"الرئيسية /","_trans":"true",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        for b in bc:
            if "href" in b:
                uidata.append({"_type": "a", "href": b["href"], "_data": b["_data"],"_data-ar": b.get("_data-ar",""),"_trans":"true",
                              "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
            else:
                uidata.append({"_data":  b["_data"],"_data-ar": b.get("_data-ar",""),"_trans":"true",
                               "class": " ins-title-12  ins-text-upper	ins-grey-color ins-strong-m"})
        uidata.append({"end": "true"})
        uidata.append({"_data": title,"_data-ar":title_ar,"_trans":"true",
                       "class": "ins-col-grow ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        if len(right_ui) > 0:
            uidata += right_ui
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
    
    def process_product_data(self,p, data, sedata):
        prefix = str(data["id"])
        full_title = data["title"]
        if data.get("subtype"):
            prefix = f"{str(data['id'])}_{data['subtype']}"
            data["subtype_title"] = self.ins._db._get_row("gla_product_types", "title", f"alias='{data['subtype']}'")["title"]
            full_title = f"{data['title']} ({data['subtype_title']})"
        
        th_main_image = ELUI(self.ins).view_pro_image(data)

        adddata = {
            "id": data["id"],
            "prefix": prefix,
            "full_title": full_title,
            "th_main_image": f"/ins_web/ins_uploads/{th_main_image}",
            "title": data["title"],
            "category": data["category_title"],
            "subtype": data.get("subtype", ""),
            "type": data.get("type", ""),
            "weight": data["weight"],
            "price": data["price"],
            "des": data.get("des", ""),
            "th_main": data["th_main"],
            "count": p["count"],
            "gift_card": p.get("gift","0")
        }

        sedata[prefix] = adddata
        self.ins._server._set_session(self.session_name, sedata)

 
 
    def prepare_ui_data(self,sedata):
        uidata = [{"class": "ins-space-l"}, {"start": True, "class": "ins-col-12 ins-flex -cart-cont"}]
        for k, v in sedata.items():
            uidata += ELUI(self.ins).cart_pro_block(v)
            uidata.append({"class": "ins-space-xs"})
        footer = [
            {"start": True, "class": "ins-flex-space-between ins-col-12 ins-padding-l"},
            {"_data": "Continue Shopping","_data-ar":"متابعة التسوق","_trans":"true", "class": "ins-button-s ins-text-upper ins-gold-d ins-col-6 ins-m-col-6 -continue-shopping-btn"},
            {"_data": "To cart","_data-ar":"الى السلة","_trans":"true", "_type": "a", "href": "/checkout/cart", "class": "ins-button-s ins-gold-d ins-text-upper ins-col-5 ins-m-col-6 -to-cart-btn"},
            {"end": True},
            {"class": "ins-space-l"}
        ]
        uidata += footer
        uidata.append({"end": True})
        return uidata

    def format_time(self,time_str):
        hour, minute = map(int, time_str.split(":"))
        period = "AM" if hour < 12 else "PM"
        if self.ins._langs._this_get()["name"] == "ar":
         period = "صباحًا" if hour < 12 else "مساءً"
        hour = hour if 1 <= hour <= 12 else hour - 12 if hour > 12 else 12  # تحويل 24 ساعة إلى 12 ساعة
        return f"{hour}:{minute:02d} {period}"



    def order_check(self):


        ops = self.ins._db._get_row("gla_settings","*","id='1'")

    


        r = {"status": "0"}

        if ops["accept_order"] == 0:
            r["msg"] = "Store unavailable. Try again later"
            if ops["order_msg"] != "":
                r["msg"] = ops["order_msg"]

            if self.ins._langs._this_get()["name"] == "ar":
                r["msg"] = "المتجر غير متاح حاليًا. حاول لاحقًا"
                if ops["order_msg_ar"] != "":
                    r["msg"] = ops["order_msg_ar"]

            r["status"] = "2"
            return r
        
        now = datetime.now()
        weekday = now.weekday()

        if weekday == 6:
            r["msg"] = "We accept orders on working days, from Monday to Saturday."
            if self.ins._langs._this_get()["name"] == "ar":
              r["msg"] = "نستقبل الطلبات في أيام العمل من يوم الإثنين إلى يوم السبت."

            r["status"] = "3"
            return r

        #current_time = (datetime.now() + timedelta(hours=2)).time().replace(microsecond=0)
        current_time = (datetime.now()).time().replace(microsecond=0)




        available_periods = []

        is_open = False
        times = json.loads(ops["times"])
        if times:
            for t in times:
                opening_time = datetime.strptime(t.get("from"), "%H:%M").time()
                closing_time = datetime.strptime(t.get("to"), "%H:%M").time()

                if opening_time <= current_time <= closing_time:
                    is_open = True 
                    break

                otime = self.format_time(t.get('from', '09:00'))
                ctime = self.format_time(t.get('to', '23:00'))
                available_periods.append(f"from {otime} to {ctime}")

            if not is_open:
                r["status"] = "1"
                msg = "The store is currently closed. Business hours: " + " and ".join(available_periods)

                if self.ins._langs._this_get()["name"] == "ar":
                    msg = "المتجر مغلق حاليًا. ساعات العمل: " + " و ".join(available_periods)

                r["msg"] = msg

        return r



   



 
 
    def _cart_lightbox_ui(self, single_product=False):

        order_check = self.order_check()     
        if order_check["status"] !="0":
            return order_check
        
        else:    
            r = {}

            r["status"] = "0"
            sedata = self.ins._server._get_session(self.session_name)
            if type(sedata) != dict:
                sedata = {}
            if single_product:
                p = self.ins._server._post()
                pro = self.ins._db._jget("gla_product", "*", f"gla_product.id={p['pid']}")
                pro._jwith("gla_product_category category", "title,id", rfk="fk_product_category_id", join="left join")
                ddata = pro._jrun()
                for data in ddata:
                    data["subtype"] = ""
                    data["type"] = ""
                    if p["subtype"]:
                        data["subtype"] = p["subtype"]
                        data["type"] = p["type"]
                    
                    self.process_product_data(p, data, sedata)
                uidata = self.prepare_ui_data(sedata)

            else: 
                data = self.ins._server._post()["data"]
                products = json.loads(data)

                for k, p in products.items():
                    pro = self.ins._db._jget("gla_product", "*", f"gla_product.id={p['product_id']}")
                    pro._jwith("gla_product_category category", "title,id", rfk="fk_product_category_id", join="left join")
                    ddata = pro._jrun()
                    for data in ddata:
                        data["type"] = "standard" if data["category_id"] == 1 else "royal" if data["category_id"] == 2 else ""
                        data["subtype"] = "standard" if data["category_id"] == 1 else "george" if data["category_id"] == 2 else ""
                        self.process_product_data(p, data, sedata)
                uidata = self.prepare_ui_data(sedata)
            r["ui"] = self.ins._ui._render(uidata)
            return r





    def view_pro_image(self,data):

        th_main_image = data.get("th_main", "")

        types_data = json.loads(data["types_data"]) 
        if data["type"] in types_data and data["subtype"] in types_data[data["type"]].get("data", {}):
            stys_data = types_data[data["type"]]["data"][data["subtype"]]
            rimages = stys_data.get("images", "").strip()
            if rimages:
                image = rimages.split(",")
                th_main_image = image[0] if image else th_main_image

        return th_main_image
   
    def counter_pro_block(self,  data, string=False):
        title = self.ins._db._get_row("gla_product", "title,kit_lang", f"id='{data['id']}'",update_lang=True)
        full_title = title["title"]
        if data.get("subtype"):
            subtype_title = self.ins._db._get_row("gla_product_types", "title,kit_lang", f"alias='{data['subtype']}'",update_lang=True)
            full_title = f"{title['title']} ({subtype_title['title']})"
        
       
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card "},
            {"src": f"{data['th_main_image']}", "loading":"lazy","_type": "img", "class": "ins-radius-m  ins-m-col-2", "style": "    width: 97px;"}, 
            {"start": "true", "class": " ins-col-6 ins-flex ins-m-col-10"},
           
            {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o -pro-title-area ins-m-col-12  "},
             {"_data": f"{full_title}", "class": "ins-col-12 ins-title-20	 ins-strong-l ins-grey-d-color", "style": "    !important;"}, 
             {"_data": data.get("des", ""), "class": "ins-grey-color ins-col-12 ins-title-14", "style": "line-height: 20px; "},
               {"end": "true"},
                 {"_data": str(data["price"]),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-12 ins-m-col-12 ins-strong-l ins-primary-d-color  ins-title-20"}, {"end": "true"},
           
                      {"class":"ins-line ins-col-12 not-for-web"},

                                 {"class":" ins-m-col-grow not-for-web"},

            {"start": "true", "class": "ins-flex ins-col-3 -counter-cont ins-gap-o ins-m-col-4 "},
            {"_data": "-", "class": "ins-button-s ins-flex-center ins-col-4 ins-gold-bg ins-font-2xl -minus-btn ins-m-col-4",
                "data-pid": data["prefix"]},
            {"_type": "input",  "name": "count_inpt", "type": "text",
                "value": data["count"], "pclass": "ins-col-4  ins-m-col-4", "data-pid":data["prefix"],"class": "count-inpt ins-title-xs ins-strong-l"},
            {"_data": "+", "class": "ins-button-s ins-flex-center  ins-col-4 ins-m-col-4  ins-gold-bg ins-font-2xl  -plus-btn",
                "data-pid": data["prefix"]},
            {"end": "true"},
            {"_data": f"<i  class='lni lni-trash-3 _a_red'></i>","class": "ins-flex-center ins-col-1 -remove-item-cart-btn  ins-m-col-1", "data-pid": data["prefix"]},
            {"end": "true"},
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata
    


    def small_pro_block(self, data, string=False):
        mode = self.ins._server._get("mode")
        if data.get("new_price"):
            total = float(data.get("new_price",0)) * float(data.get("count",0))
        else:
         total = float(data.get("price",0)) * float(data.get("count",0))
        title = self.ins._db._get_row("gla_product", "title,kit_lang", f"id='{data['id']}'",update_lang=True)
        full_title = title["title"]
        if data.get("subtype"):
            subtype_title = self.ins._db._get_row("gla_product_types", "title,kit_lang", f"alias='{data['subtype']}'",update_lang=True)
            full_title = f"{title['title']} ({subtype_title['title']})"

      
      
      
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card "},
            {"src": f"{data['th_main_image']}", "loading":"lazy","_type": "img", "class": "ins-radius-m  ins-m-col-2", "style": "    width: 97px;"}, 
            {"start": "true", "class": "ins-col-8 ins-flex ins-m-col-10"}, 
            
            
            {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o ins-m-gap-10   -pro-title-area "},
            {"_data": f"{data.get('count',0)} x {full_title}", "class": "ins-col-12 ins-title-s	 ins-strong-l ins-grey-d-color", "style": "    !important;"},
            {"_data": data.get("des", ""), "class": "ins-grey-color ins-col-12 ins-title-14 ", "style": "line-height: 20px; "},
            {"end": "true"},
            {"_data": str(total),"_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه","data-weight":data["weight"],"data-count":data["count"],"data-price":data["price"],"class": "-pro-price  ins-m-col-12  ins-col-12 ins-strong-l ins-primary-d-color ins-title-20"},
            {"end": "true"},

            {"class": "ins-space-l not-for-web"},
            {"class": "ins-line ins-m-col-12 not-for-web"},
            {"class": "ins-space-l not-for-web"},

            
            
            {"_data": f"<i  class='lni lni-trash-3 _a_red'></i>", "class": "ins-flex-center ins-col-1 -remove-item-cart-small-btn ins-m-col-1", "data-mode":mode,"data-pid": data["prefix"]},
            {"end": "true"}
        ]

        if string:
            return self.ins._ui._render(uidata)
        return uidata

    def shop_pro_block(self,data,purl,st = "",stys="",tys =""):

        if not stys and not tys and (data["fk_product_category_id"] == 1 or data["fk_product_category_id"] == 3 ) :
            tys = "standard"
            stys = "standard"
            data["subtype"] = "standard"
        elif not stys and not tys and data["fk_product_category_id"] == 2 :
            tys = "royal"
            stys = "george"
            data["subtype"] = "george"


        p = "/ins_web/ins_uploads/"
        types_data = json.loads(data["types_data"]) if data.get("types_data") else {}

        th_main_image = ""
        th_overlay_image = ""

        if tys in types_data and stys in types_data[tys].get("data", {}):
            stys_data = types_data[tys]["data"][stys]
            rimages = stys_data.get("images", "").strip()
            if rimages:
                image = rimages.split(",")
                th_main_image = image[0] if image else th_main_image
                th_overlay_image = image[1] if len(image) > 1 else th_main_image

        purl += f"/do/type/types={tys}" if tys else ""
        purl += f"&subtypes={stys}" if stys else ""

        title = self.ins._db._get_row("gla_product", "title,kit_lang", f"id='{data['id']}'", update_lang=True)
        full_title = title["title"]

        if stys:
            subtype_title = self.ins._db._get_row("gla_product_types", "title,kit_lang", f"alias='{data['subtype']}'", update_lang=True)
            full_title = f"{title['title']} ({subtype_title['title']})"

        button_title = "SHOP NOW <i class='lni ins-icon lni-arrow-right'></i>"
        if self.ins._langs._this_get().get("name") == "ar":
            button_title = "تسوق الآن <i class='lni ins-icon lni-arrow-left'></i>"

        r = [
            {"start": "true", "class": "ins-flex gla-pro-block ins-co-", "style": st},
            {"_type":"a","href": purl,"start": "true", "class": "gla-img-cont", "style": ""},
            {"src": p + th_main_image, "loading": "lazy", "_type": "img", "class": "gla-pro-img"},
            {"src": p + th_overlay_image, "loading": "lazy", "_type": "img", "class": "gla-pro-himg"},
            {"_type":"a","end": "true"},
            {"class": "ins-space-s"},
            {"_type":"a","href": purl,"_data": full_title, "class": "ins-col-12 ins-title-20 ins-strong-m ins-grey-color", "style": "line-height:24px"},
            {"_type":"a","href": purl,"_data": f"{data['price']}", "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه",
             "class": "ins-col-12 ins-strong-m ins-primary-d-color", "style": "line-height:24px"},
            {"end": "true"}
        ]

        return r



    def cart_pro_block(self,data,string=False):
        title = self.ins._db._get_row("gla_product", "title,kit_lang", f"id='{data['id']}'",update_lang=True)
        full_title = title["title"]
        if data.get("subtype"):
            subtype_title = self.ins._db._get_row("gla_product_types", "title,kit_lang", f"alias='{data['subtype']}'",update_lang=True)
            full_title = f"{title['title']} ({subtype_title['title']})"

        item_total_amount = float(data["count"]) * float(data["price"])
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-border ins-radius-l ins-gap-o","style":"overflow: hidden;"},
            {"start": "true", "class": "ins-col-4 ins-flex-center -cart-img-cont ins-m-col-2","style": "height:100px;"},
            {"src": f"{data['th_main_image']}","loading":"lazy", "_type": "img","class": "ins-radius-m", "style": "    height: 100%;"},
            {"end": "true"},
            {"start": "true", "class": "ins-col-8  ins-flex-grow ins-primary-w ins-padding-l ins-m-flex-center -cart-img-cont ins-m-col-9","style": "border-radius: 0px 8px 8px 0px;    border-left: 1px solid var(--primary-l);"},
            {"_data": "Item summary","_data-ar": "ملخص السعر","_trans":"true","class": "ins-col-11 ins-m-col-11 ins-title-s ins-strong-l ins-grey-d-color item-summary-area"},
            {"_data": f"<i  class='lni lni-trash-3 _a_red'></i>","class": "ins-flex-center ins-col-1 ins-m-col-1 -remove-item-side-cart-btn", "data-pid": data["prefix"]},

            {"_data": f"{data.get('count', '')} x {full_title}", "class": "ins-col-7 ins-m-col-7 ins-strong-m ins-grey-color ins-title-14"},
            {"_data":  f"{item_total_amount}","_view":"currency","_currency_symbol":" EGP","_currency_symbol_ar":" جنيه", "class": "ins-col-5 ins-m-col-5 ins-strong-m ins-grey-d-color ins-flex-end ins-title-14"},
            {"end": "true"},
            {"end": "true"}
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata
    

   
    def counter_user_order_block(self,  data, string=False):

            title = self.ins._db._get_row("gla_product", "title,kit_lang", f"id='{data['fk_product_id']}'",update_lang=True)
            full_title = title["title"]
            if data.get("subtype"):
                subtype_title = self.ins._db._get_row("gla_product_types", "title,kit_lang", f"alias='{data['subtype']}'",update_lang=True)
                full_title = f"{title['title']} ({subtype_title['title']})"

            if data.get("gift_card"):
                full_title = f" <i class='lni lni-box-gift-1 ins-font-l'></i> {full_title}"

            tys = ""
            stys = ""

            if data["product_fk_product_category_id"] == 1 or data["product_fk_product_category_id"] == 3 :
                tys = "standard"
                stys = "standard"
            elif  data["product_fk_product_category_id"] == 2 :
                tys = "royal"
                stys = "george"


            p = "/ins_web/ins_uploads/"
            types_data = json.loads(data["product_types_data"]) if data.get("product_types_data") else {}

            th_main_image = ""
        
            if tys in types_data and stys in types_data[tys].get("data", {}):
                stys_data = types_data[tys]["data"][stys]
                rimages = stys_data.get("images", "").strip()
                if rimages:
                    image = rimages.split(",")
                    th_main_image = image[0] if image else th_main_image

           
           
            image = f"{p}{th_main_image}"
            uidata = [
                {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card not-for-phone"},
                {"src": image,"loading":"lazy", "_type": "img", "class": "ins-radius-m ins-m-col-2", "style": "    width: 97px;"},
                {"start": "true", "class": "ins-col-grow  ins-flex"},
                {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"},
                {"_data": "Product", "_data-ar": "المنتج", "_trans": "true", "class": " ins-col-3  ins-m-col-3  ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
                {"_data": "QTY", "_data-ar": "الكمية", "_trans": "true", "class": " ins-col-3  ins-m-col-3 ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
                {"_data": "Price", "_data-ar": "السعر", "_trans": "true", "class": " ins-col-3  ins-m-col-3 ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
                {"_data": "Total", "_data-ar": "الإجمالي", "_trans": "true", "class": " ins-col-3  ins-m-col-3 ins-title-xs  ins-text-center ins-grey-color ins-strong-m"},
                {"_data": full_title, "class": " ins-col-3 ins-m-col-3 ins-grey-d-color ins-text-center ins-title-xs"},
                {"_data": str(data["quantity"]), "class": " ins-col-3 ins-m-col-3 ins-grey-d-color ins-text-center ins-title-xs"},
                {"_data": str(data["price"]), "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه", "class": " ins-col-3 ins-m-col-3 ins-grey-d-color ins-text-center ins-title-xs"},
                {"_data": str(data["price"] * data["quantity"]), "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه", "class": "ins-col-3 ins-m-col-3 ins-grey-d-color ins-text-center ins-title-xs"},
                {"end": "true"},
                {"end": "true"},
                {"end": "true"},






                 {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-card not-for-web"},
                {"src": image,"loading":"lazy", "_type": "img", "class": "ins-radius-m ins-m-col-2", "style": "    width: 97px;"},
                {"start": "true", "class": "ins-col-grow  ins-m-col-10 ins-flex"},
                
                
                {"start": "true", "class": "ins-col-12 ins-flex  ins-gap-o"},
                {"_data": "Product", "_data-ar": "المنتج", "_trans": "true", "class": " ins-m-col-3   ins-grey-color ins-strong-m"},
                {"_data": full_title, "class": " ins-m-col-9 ins-grey-d-color ins-text-center "},

                {"_data": "QTY", "_data-ar": "الكمية", "_trans": "true", "class": "ins-m-col-3    ins-grey-color ins-strong-m"},
                {"_data": str(data["quantity"]), "class": " ins-m-col-9 ins-grey-d-color   ins-text-center"},

                {"_data": "Price", "_data-ar": "السعر", "_trans": "true", "class": "  ins-m-col-3    ins-grey-color ins-strong-m"},
                {"_data": str(data["price"]), "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه", "class": " ins-m-col-9 ins-grey-d-color ins-text-center  "},

                {"_data": "Total", "_data-ar": "الإجمالي", "_trans": "true", "class": " ins-m-col-3    ins-grey-color ins-strong-m"},
                {"_data": str(data["price"] * data["quantity"]), "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه", "class": "    ins-m-col-9 ins-grey-d-color  ins-text-center "},
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
    
    
    def _bank_ui(self):
        p = "/ins_web/ins_uploads/"
        bank_details = self.ins._db._get_data("gla_bank_accounts","*","1=1 order by kit_order asc ",update_lang=True)
        
        note = "Note: If you use InstaPay, please transfer the amount to our bank account at <a class='-african-bank-button ins-strong-m'>Arab African International Bank</a>"
        if self.ins._langs._this_get()["name"] == "ar":
            note =  "ملاحظة: إذا كنت تستخدم انستاباي ، يرجى تحويل المبلغ إلى حسابنا المصرفي في <a class='-african-bank-button ins-strong-m'>البنك العربي الأفريقي الدولي</a>"


        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex ins-gap-m ins-card ins-padding-l"},
            {"_data": note,"class": "ins-col-12 ins-title-xs ins-grey-color ins-text-none -bank-note"}
        ]


        for bank in bank_details:
            name = bank["title"].replace(" ", "_").lower()

            anumber = f"Account Number: {bank['account_number']} <i data-number='{bank['account_number']}' class='-copy-number lni lni-file-multiple'></i>"
            scode = f"Swift Code: {bank['swift']} <i data-number='{bank['swift']}' class='-copy-number lni lni-file-multiple'></i>"
            inumber = f"IBAN number: {bank['iban']} <i data-number='{bank['iban']}' class='-copy-number lni lni-file-multiple'></i>"

            if self.ins._langs._this_get()["name"] == "ar":
                anumber = f"رقم الحساب: {bank['account_number']} <i data-number='{bank['account_number']}' class='-copy-number lni lni-file-multiple'></i>"
                scode = f"رمز السويفت: {bank['swift']} <i data-number='{bank['swift']}' class='-copy-number lni lni-file-multiple'></i>"
                inumber = f"رقم الآيبان: {bank['iban']} <i data-number='{bank['iban']}' class='-copy-number lni lni-file-multiple'></i>"


            uidata.append({"start": "true", "class": f"ins-col-4 -bank-card-{bank['id']} -bank-info-card ins-padding-s ins-margin-xs"})
            uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-align-center"})
            uidata.append({"_type": "img", "style": "width: 30px;", "src": f"{p}{bank['logo']}", "loading": "lazy", "class": "ins-logo-xs"})
            uidata.append({"_data": f"{bank['title']}", "_data-ar": f"{bank['title']}", "_trans":"true","class": "ins-col-10 ins-title-xs ins-strong-m ins-grey-d-color ins-m-col-10"})
            uidata.append({"end": "true"})
            uidata.append({"_data": anumber, "class": "ins-col-12 ins-title-xs ins-grey-d-color -bank-info"})
            uidata.append({"_data":scode,"class": "ins-col-12 ins-title-xs ins-grey-d-color -bank-info"})
            uidata.append({"_data": inumber, "class": "ins-col-12 ins-title-xs ins-grey-d-color -bank-info"})
            uidata.append({"_data": f"Bank Branch: {bank['branch']}", "_data-ar": f"فرع البنك: {bank['branch']}",  "_trans":"true","class": "ins-col-12 ins-title-xs  -bank-info ins-grey-d-color"})
            uidata.append({"_data": f"Company Name: {bank['company_name']}", "_data-ar": f"اسم الشركة: {bank['company_name']}", "_trans":"true", "class": "ins-col-12 ins-title-xs -bank-info ins-grey-d-color"})
            uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return uidata
   
   
   

   
    def _cash_ui(self, string=False):
      uidata = [
         {"start": "true", "class": "ins-col-12 ins-flex ins-gap-s"},
         {"_data": "Pay with cash upon delivery. Please ensure you have the exact amount ready as our delivery personnel may not have change.", "class": "ins-col-12 ins-title-xs ins-grey-color ins-text-none"},
         {"end": "true"}
      ]
      if string:
         return uidata
      return self.ins._ui._render(uidata)
    
    def _online_ui(self, string=False):
         p = "/ins_web/ins_uploads/"
         online_methods = [
            {"name": "Aman", "logo": "aman_logo.png"},
            {"name": "Contact", "logo": "contact_logo.png"},
            {"name": "Mogo", "logo": "mogo_logo.png"}
         ]
         uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]
         for method in online_methods:
            uidata.append({"start": "true", "class": "ins-col-12 ins-card ins-padding-s ins-margin-xs"})
            uidata.append({"start": "true", "class": "ins-col-12 ins-flex ins-align-center"})
            uidata.append({"_type": "img", "style": "width: 30px;", "src": f"{p}images/payment/{method['logo']}","loading":"lazy", "class": "ins-logo-xs"})
            uidata.append({"_data": f"{method['name']}", "class": "ins-col-10 ins-title-xs ins-strong-m ins-grey-d-color"})
            uidata.append({"end": "true"})
            uidata.append({"end": "true"})
         uidata.append({"end": "true"})
         if string:
            return uidata
         return self.ins._ui._render(uidata)
  
  