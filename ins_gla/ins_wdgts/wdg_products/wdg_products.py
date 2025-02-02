from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import Widget


class WdgProducts(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        data = self.ins._db._get_data("gla_product","*","1=1 limit 0,4")

        uidata = [
            {"start": "true", "class": "ins-flex-center  ins-padding-2xl gla-container "},
            {"class": "ins-space-l"},
            {"_data": "Exceptional Collection",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m"},
            {"class": "ins-col-grow "},
           
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex gla-tabs-header"},
            {"_data": "Gold Bars", "class": " ins-strong-m  gla-active "},
            {"_data": "Gold Bars"},
            {"_data": "Gold Bars"},
            {"end": "true"},           
            {"class": "ins-space-s"},

            {"start": "true", "class": "ins-flex-start gla-pro-cont"},
        ]
        for d in data:
            uidata+= ELUI(self.ins).shop_pro_block(d,f"/product/product/{d['id']}",st="width:316px;")
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space"})
        uidata.append({"class": "ins-space-xs"})
        uidata.append({"_type":"a","href":"product","_data": "View MORE <i class=' lni ins-icon lni-arrow-right'></i>",
                      "style": "width:185px", "class": "ins-button  ins-text-upper ins-gold-d"},)
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
