
from ins_kit._engine._bp import Widget


class WdgSlideshow(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        self.widget._include("shstyle.css")
        self.widget._include("sh.js")

        data = [{

            "img": "ins_web/ins_uploads/style/sh1.svg",
            "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper">Premium1 <br> Gold Bars</div><div class="ins-space-s "></div><div class="  ins-white-color   -b" style="font-size:20px">El Galla Gold is one of the oldest family<br>-owned businesses in the Egyptian gold <br> market</div><div class="ins-space"></div><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div>',
            "th": "ins_web/ins_uploads/style/sht1.svg"},

            {"img": "ins_web/ins_uploads/style/sht2.svg",

                    "img": "ins_web/ins_uploads/style/sh1.svg",
            "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper">Premium1 <br> Gold Bars</div><div class="ins-space-s "></div><div class="  ins-white-color   -b" style="font-size:20px">El Galla Gold is one of the oldest family<br>-owned businesses in the Egyptian gold <br> market</div><div class="ins-space"></div><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div>',

                    "th": "ins_web/ins_uploads/style/sht2.svg"},
            {"img": "ins_web/ins_uploads/style/sh1.svg",

                    "img": "ins_web/ins_uploads/style/sht3.svg",
            "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper">Premium1 <br> Gold Bars</div><div class="ins-space-s "></div><div class="  ins-white-color   -b" style="font-size:20px">El Galla Gold is one of the oldest family<br>-owned businesses in the Egyptian gold <br> market</div><div class="ins-space"></div><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div>',

                    "th": "ins_web/ins_uploads/style/sht3.svg"},
            {"img": "ins_web/ins_uploads/style/sh1.svg",

                    "img": "ins_web/ins_uploads/style/sh1.svg",
            "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper">Premium1 <br> Gold Bars</div><div class="ins-space-s "></div><div class="  ins-white-color   -b" style="font-size:20px">El Galla Gold is one of the oldest family<br>-owned businesses in the Egyptian gold <br> market</div><div class="ins-space"></div><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div>',

                    "th": "ins_web/ins_uploads/style/sht3.svg"},
        ]
        uidata = [
            {"start": "true", "class": "ins-primary-w wi-slideshow-cont "},
            {"start": "true", "class": "ins-col-12   wi-slideshow-inner "},
            {"start": "true", "class": "ins-col-12   wi-slideshow-slides "},
        ]
        a = "loaded active"
        itm = 0
        for d in data:
            itm += 1

            item = [
                {"start": "true", "class": f"wi-slideshow-slide {a} _{itm}"},
                {"_type": "img", "class": "wi-slideshow-image",
                    "src": d["img"]},
                {"_type": "img", "class": "wi-slideshow-cimage", "src": "ins_web/ins_uploads/style/sh1c.svg",
                    "style": "position: absolute;left: 0;"},
                {"_data": d["des"], "class": "gla-data  wi-slideshow-data",
                    "style": "position: absolute;left: 70px; bottom: 70px; width:100%;"},
                {"end": "true"}

            ]
            uidata += item
            a = ""

        uidata.append({"end": "true"})

        e = [
            {"start": "true", "class": "ins-flex-end ins-m-hidden wi-slideshow-th "}]

        uidata += e
        itm=0
        for d in data:
            itm+=1
            
            
            item = [
            {"start": "true", "data-in": itm, "class": f"wi-slideshow-th-item _{itm} "},
             {"_type": "img",
                          "class": f"", "src": d["th"]},
                
                {"end": "true"}

            ]
            uidata +=item

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)
