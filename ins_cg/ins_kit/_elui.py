from datetime import datetime, timedelta
from ins_kit.ins_parent import ins_parent


class ELUI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    @property
    def session_name(sel):
        return "cgproducts"

    def page_title(self, title="", title_ar="", bc=[{}], right_ui=[], string=False):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-white ins-border ins-border-top"},
            {"start": "true", "class": "gla-container ins-flex ins-padding-2xl"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-text-upper"},
            {"_type": "a", "href": "/", "_data": "Home /", "_data-ar": "الرئيسية /", "_trans": "true",
                "class": " ins-title-12	ins-grey-d-color ins-strong-m"},
        ]
        for b in bc:
            if "href" in b:
                uidata.append({"_type": "a", "href": b["href"], "_data": b["_data"], "_data-ar": b.get("_data-ar", ""), "_trans": "true",
                              "class": " ins-title-12	ins-grey-d-color ins-strong-m"})
            else:
                uidata.append({"_data":  b["_data"], "_data-ar": b.get("_data-ar", ""), "_trans": "true",
                               "class": " ins-title-12  ins-text-upper	ins-grey-color ins-strong-m"})
        uidata.append({"end": "true"})
        uidata.append({"_data": title, "_data-ar": title_ar, "_trans": "true",
                       "class": "ins-col-grow ins-title ins-strong-m ins-text-upper ins-grey-d-color"})
        if len(right_ui) > 0:
            uidata += right_ui
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        if string:
            return uidata
        return self.ins._ui._render(uidata)

    def cart_pro_block(self, data, string=False, delete={}):

        if len(delete) == 0:
            delete = {"_data": f"<i  class='lni lni-trash-3 _a_red'></i>",
                      "class": "ins-flex-center ins-col-1 ins-m-col-1 -remove-item-side-cart-btn", "data-pid": data["id"]}

        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex -item-card ins-border ins-radius-l ins-gap-o",
                "style": "overflow: hidden;"},
            {"start": "true", "class": "ins-col-4 ins-flex-center -cart-img-cont ins-m-col-2",
                "style": "height:100px;"},
            {"src": f"{self.ins._map.UPLOADS_FOLDER}{data['th_main']}", "loading": "lazy",
                "_type": "img", "class": "ins-radius-m", "style": "    height: 100%;"},
            {"end": "true"},
            {"start": "true", "class": "ins-col-8  ins-flex-grow ins-primary-w ins-padding-l ins-m-flex-center -cart-img-cont ins-m-col-9",
                "style": "border-radius: 0px 8px 8px 0px;    border-left: 1px solid var(--primary-l);"},
            {"_data": "Item summary", "_data-ar": "ملخص السعر", "_trans": "true",
                "class": "ins-col-11 ins-m-col-11 ins-title-s ins-strong-l ins-grey-d-color item-summary-area"},


            delete,

            {"_data": f" {data["title"]}",
                "class": "ins-col-7 ins-m-col-7 ins-strong-m ins-grey-color ins-title-14"},
            {"_data":  f"{data["price"]}", "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه",
                "class": "ins-col-5 ins-m-col-5 ins-strong-m ins-grey-d-color ins-flex-end ins-title-14"},
            {"end": "true"},
            {"end": "true"}
        ]
        if string:
            return self.ins._ui._render(uidata)
        return uidata

    def _cart_lightbox_ui(self):
        r = {}
        sedata = self.ins._server._get_session(self.session_name)
        if type(sedata) != dict:
            sedata = {}

        if len(sedata) == 0:
            uidata = [{"_data": "There is no items in cart",
                       "class": "ins-col-12 ins-card ins-secondary ins-text-upper ins-text-center ins-title-12"}]
        else:
            uidata = [{"class": "ins-space-l"}, {"start": True,
                                                 "class": "ins-col-12 ins-flex -cart-cont"}]
            for k, v in sedata.items():
                uidata += ELUI(self.ins).cart_pro_block(v)
                uidata.append({"class": "ins-space-xs"})
            uidata += [
                {"start": True, "class": "ins-flex-space-between ins-col-12 ins-padding-l"},
                {"_data": "Continue Shopping", "_data-ar": "متابعة التسوق", "_trans": "true",
                    "class": "ins-button-s ins-text-upper ins-gold-d ins-col-6 ins-m-col-6 -continue-shopping-btn"},
                {"_data": "To cart", "_data-ar": "الى السلة", "_trans": "true", "_type": "a", "href": "/checkout/cart",
                    "class": "ins-button-s ins-gold-d ins-text-upper ins-col-5 ins-m-col-6 -to-cart-btn"},
                {"end": True},
                {"class": "ins-space-l"},
                {"end": True}
            ]

        r["ui"] = self.ins._ui._render(uidata)
        return r

    def shop_pro_block(self, data, url=""):
        p = self.ins._map.UPLOADS_FOLDER
        if url == "":

            url = self.ins._server._url(
                {"alias": "products", "mode": "category", "id": data['cat_alias'], "q1": f"{data['alias']}"}, ["page"])
        else:
            url = url

        curl = self.ins._server._url(
            {"alias": "products", "mode": "category", "id": data['cat_alias']}, ["page"])

        uurl = self.ins._server._url(
            {"alias": "products", "mode": "user", "id": data['fk_user_id'], }, ["page"])

        if data["views"] == None:
            data["views"] = "0"

        r = [
            {"start": "true", "class": "ins-flex ins-card ins-col-3 -pro-item-block"},

            {"_type": "a", "href": url, "start": "true", "class": "ins-col-12"},
            {"start": "true", "class": "gla-img-cont"},
            {"src": p + (data.get("th_main") or "default.png"),
             "loading": "lazy", "_type": "img", "class": "gla-pro-img"},
            {"end": "true"},
            {"class": "ins-space-s"},
            {"_data": data.get("title"), "class": "ins-padding-s ins-secondary-color ins-title-s ins-col-12",
             "style": "line-height:24px;min-height: 75px;"},
            {"_type": "a", "end": "true"},
            {"start": "true", "class": "ins-col-4 ins-flex-center ins-card"},
            {"class": "ins-icons-eye", "style": "position: relative; top: 3px;"},
            {"_data": f"{data.get('views', "0")}"},
            {"end": "true"},
            
            
            
            {"start": "true","data-a":"like",  "data-pid":data["id"], "class": "ins-col-4 -pro-action ins-flex-center ins-card"},
            {"class": "ins-icons-heart",  "style": "position: relative; top: 3px;"},
            {"_data": "15"},

            
            {"end": "true"},
            {"start": "true", 
             "data-a":"wishlist",  "data-pid":data["id"],
             
             
             "class": "ins-col-4  -pro-action ins-flex-center ins-card"},
            {"class": "ins-icons-indent", "style": "position: relative; top: 3px;"},
            {"end": "true"},
            {"_data": f'by <a style="text-decoration: underline;" href="{uurl}">{data["us_title"]}</a> in  <a style="text-decoration: underline;" href="{curl}">{data["cat_title"]}</a>',
                "class": "ins-col-grow ins-title-xs ins-secondary-d-color", "style": "line-height:24px"},
            {"_data": f"{data.get('price')}", "_view": "currency",
             "class": " ins-strong-m ins-secondary-d-color", "style": "line-height:24px"},
            {"end": "true"}


        ]

        return r
