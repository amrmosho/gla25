from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import Widget


class WdgProducts(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        data = self.ins._db._get_data("gla_product","*","fk_product_category_id = 1 limit 0,4")
        data_b= self.ins._db._get_data("gla_product","*","fk_product_category_id = 2 limit 0,4")
        data_c= self.ins._db._get_data("gla_product","*","fk_product_category_id = 3 limit 0,4 ")

        self.widget._include("wpros.js")
        uidata = [
            {"start": "true", "class": "ins-flex-center  ins-padding-2xl gla-container "},
            {"class": "ins-space-l"},
            {"_data": "Exceptional Collection",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m"},
            {"class": "ins-col-grow "},
           
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex gla-tabs-header"},
            {"_data": "Gold Bars", "data-view":".cat_a", "class": " ins-strong-m wi-pros-tab-btn  gla-active "},
            {"_data": "Gold Coins" , "data-view":".cat_b","class":"wi-pros-tab-btn"},
            {"_data": "Gifts", "data-view":".cat_c" ,"class":"wi-pros-tab-btn"},
            {"end": "true"},           
            {"class": "ins-space-s"},

          
        ]
        
        uidata.append({"start": "true", "class": " cat_a ins-flex-start wi-pros-tab-cont gla-show  gla-pro-cont"})
        
        for d in data:
            uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}",st="width:316px;")
        
        uidata.append({"end": "true"})
        
        uidata.append({"start": "true", "class": " cat_b ins-flex-start wi-pros-tab-cont gla-pro-cont"})
        
        for d in data_b:
            uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}",st="width:316px;")
        
        uidata.append({"end": "true"})
        
        
        uidata.append({"start": "true", "class": " cat_c ins-flex-start wi-pros-tab-cont gla-pro-cont"})
        
        for d in data_c:
            uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}",st="width:316px;")
        
        uidata.append({"end": "true"})
        
        
        uidata.append({"class": "ins-space"})
        uidata.append({"class": "ins-space-xs"})
        uidata.append({"_type":"a","href":"product","_data": "View MORE <i class=' lni ins-icon lni-arrow-right'></i>",
                      "style": "width:185px", "class": "ins-button  ins-text-upper ins-gold-d"},)
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
