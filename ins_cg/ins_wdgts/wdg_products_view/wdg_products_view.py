from ins_cg.ins_kit._elui import ELUI
from ins_kit._engine._bp import Widget


class WdgProductsView(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        data = self.ins._db._get_data("gla_product","*","1 order by price asc limit 0,12" ,True) 

        self.widget._include("wpros.js")
        self.widget._include("wpros.css")
        uidata = [
            {"start": "true", "class": "ins-flex-center  ins-padding-2xl gla-container "},
            {"class": "ins-space-l"},
            {"_data": "New Releases","_data-ar":"مضاف حديثاً","_trans":"true","class": "ins-col-10 ins-title-xl ins-grey-d-color ins-strong-m ins-text-upper"},
            {"_type":"a","_data": "Browse More Products","_data-ar":"اكتشف المزيد","_trans":"true","class":"ins-col-2"},
            {"class": "ins-col-grow "},
           
     
            {"class": "ins-space-s"},

          
        ]
        
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex"})
        
        for d in data:
            uidata+= ELUI(self.ins).shop_pro_block(d)
           
        uidata.append({"end": "true"})
        
        uidata.append({"start": "true", "class": " cat_b ins-flex-center wi-pros-tab-cont gla-pro-cont"})
        

        return self.ins._ui._render(uidata)
