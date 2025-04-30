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
    def shop_pro_block(self, data ,url =""):
        p = self.ins._map.UPLOADS_FOLDER
        purl = self.ins._server._url({"alias": "products", "mode": "product", "id": f"{data['id']}"},["page"])
        
        if data["views"] == None:
            data["views"] ="0"

        r = [
            {"_type": "a", "href":purl,"start": "true", "class": "ins-flex ins-card -pro-item-block","style":"width:315px"},
           
            {"start": "true", "class": "gla-img-cont"},
            {"src": p + (data.get("th_main") or "default.png"), "loading": "lazy", "_type": "img", "class": "gla-pro-img"},
            {"end": "true"},
            
            
            {"class": "ins-space-s"},
            {"_data": data.get("title"), "class": "ins-padding-s ins-secondary-color ins-title-s ins-col-12", "style": "line-height:24px;min-height: 75px;"},
          
            {"start": "true", "class": "ins-col-4 ins-flex-center ins-card"},
            {"class": "ins-icons-eye", "style": "position: relative; top: 3px;"},
            {"_data": f"{data.get('views',"0")}"},
            {"end": "true"},
           
            {"start": "true", "class": "ins-col-4 ins-flex-center ins-card"},
            {"class": "ins-icons-heart", "style": "position: relative; top: 3px;"},
            {"_data": "15"},
            {"end": "true"},
           
            {"start": "true", "class": "ins-col-4 ins-flex-center ins-card"},
            {"class": "ins-icons-indent", "style": "position: relative; top: 3px;"},
            {"end": "true"},
          
            {"_data": 'by dika in Apple Products', "class": "ins-col-7 ins-title-xs ins-secondary-d-color", "style": "line-height:24px"},
            {"_data": f"{data.get('price')}", "_view": "currency", "class": "ins-col-3 ins-strong-m ins-secondary-d-color", "style": "line-height:24px"},
            {"_type": "a", "end": "true"}
            
            
        ]

        return r
