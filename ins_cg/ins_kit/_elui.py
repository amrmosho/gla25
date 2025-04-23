from datetime import datetime, timedelta
import json
from ins_kit.ins_parent import ins_parent
class ELUI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
    
    @property
    def session_name(sel):
        return "cgproducts"
    

    def page_title(self, title="",title_ar = "", bc=[{}], right_ui=[],string=False):
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
        if string:
            return uidata
        return self.ins._ui._render(uidata)

    def shop_pro_block(self,data):


        p = self.ins._map.UPLOADS_FOLDER
        purl = self.ins._server._url({"alias":"shop","mode":"product","id":f"{data['id']}"})
        r = [
            {"_type":"a","start": "true", "class": "  ins-flex -pro-item-block  ins-col-3 "},
         
            {"start": "true", "class": "  ins-card  ins-col-12  "},
            {"href": purl,"start": "true", "class": "gla-img-cont", "style": ""},
            {"src": p + data.get("th_main"), "loading": "lazy", "_type": "img", "class": "gla-pro-img"},
            {"end": "true"},
            {"class": "ins-space-s"},
            {"_data": data.get("title"), "class": " ins-padding-s ins-primary-color    ins-title-s ins-col-12  ", "style": "line-height:24px"},
            {"start": "true", "class": "  ins-card  ins-col-12  "},
            {"end": "true"},

          
          
          
            {"_data": f"{data.get('price')}", "_view": "currency", "class": "ins-col-12 ins-strong-m ins-primary-d-color", "style": "line-height:24px"},
            {"end": "true"},
           
            {"_type":"a","end": "true"}
        ]

        return r