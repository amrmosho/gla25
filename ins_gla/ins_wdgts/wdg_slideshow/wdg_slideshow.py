
from ins_kit._engine._bp import Widget


class WdgSlideshow(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        uidata = [
            {"start": "true", "class": "ins-primary-w "},

            {"start": "true", "class": "gla-container"},

            {"_type": "img", "src": "ins_web/ins_uploads/style/sh1.svg"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/sh1c.svg",
                "style": "position: absolute;left: 0;"},
            
            

            {"start": "true", "class": "gla-data ",
                "style": "position: absolute;left: 70px; bottom: 70px; width:100%;"},
            {"_data": "Premium <br/> Gold Bars", "style": "line-height:62px",
                "class": "ins-title-3xl ins-strong-m ins-white-color  ins-text-upper"},
            {"class": "ins-space-s"},


            {"_data": "El Galla Gold is one of the oldest family<br/>-owned businesses in the Egyptian gold <br/> market",
                "class": "  ins-white-color ", "style": "font-size:20px"},

            {"class": "ins-space"},

            {"_data": "Shop now <i class=' lni ins-icon lni-arrow-right'></i>",
                "style": "width:250px", "class": "ins-button-l  ins-text-upper ins-gold-d"},

            {"end": "true"},
            
               {"start": "true", "class": "ins-flex-end ",
                "style": "position: absolute;right: 70px; bottom: 70px; width:50%;"},

            {"_type": "img", "src": "ins_web/ins_uploads/style/sht1.svg"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/sht2.svg"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/sht3.svg"},


            {"end": "true"}, {"end": "true"}

        ]

        return self.ins._ui._render(uidata)
