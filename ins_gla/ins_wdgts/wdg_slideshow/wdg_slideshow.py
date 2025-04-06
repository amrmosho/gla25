
from ins_kit._engine._bp import Widget


class WdgSlideshow(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        self.widget._include("shstyle.css")
        self.widget._include("sh.js")


        data = [
            


            {"img": "/ins_web/ins_uploads/style/bar.png",
             "img_ar": "/ins_web/ins_uploads/style/bar_ar.png",
             "img": "/ins_web/ins_uploads/style/bar.png",
             "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title">EL GALLA GOLDS <br>ONE-OUNCE GOLD BAR</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">A Lifetime of VALUE</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=1"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div></a>',
             "des_ar": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title"> سبيكة ذهب<br>  اونصة مصنوعة بإتقان من الجلا جولد</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">قيمة مدى الحياة</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=1"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">تسوق الآن <i class=" lni ins-icon lni-arrow-left"></i></div></a>',
             "th": "/ins_web/ins_uploads/style/bar2.png"},
           
           
           
           
            {"img": "/ins_web/ins_uploads/style/geroge.png",
             "img_ar": "/ins_web/ins_uploads/style/george_ar.png",
             "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title">FIVE-POUND <br> GEORGE GOLD COIN</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">A Timeless Symbol of - WEALTH AND HERITAGE</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=2&types_data=royal"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div></a>',
             "des_ar": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title"><br>خمسة جنية ذهب (جورج)</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">رمز خالد - للثروة والتراث</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=2&types_data=royal"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">تسوق الآن <i class=" lni ins-icon lni-arrow-left"></i></div></a>',
             "th": "/ins_web/ins_uploads/style/geroge2.png"},
           
           
           
            {"img": "/ins_web/ins_uploads/style/baby.png",
             "img_ar": "/ins_web/ins_uploads/style/baby_ar.png",
             "des": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title">EL GALLA GOLDS <br> GOLDEN BABY BOTTLES</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">The perfect gift to celebrate a newborn arrival</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=3"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">Shop now <i class=" lni ins-icon lni-arrow-right"></i></div></a>',
             "des_ar": '<div style="line-height:62px" class="ins-title-3xl -a ins-strong-m ins-white-color  ins-text-upper -slideshow-title"> ببرونة ذهب<br>  بتصميم فريد من الجلا جولد</div><div class="ins-space-s "></div><div class="  ins-white-color   -b -slideshow-des" style="font-size:20px">الهدية المثالية للاحتفال بوصول المولود الجديد</div><div class="ins-space"></div><a href="/product/do/filter/fk_product_category_id=3"><div style="width:250px" class="ins-button-l   -c ins-text-upper  ins-gold-d -slideshow-button">تسوق الآن <i class=" lni ins-icon lni-arrow-left"></i></div></a>',
             "th": "/ins_web/ins_uploads/style/baby2.png"},
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
            img = d["img"]
            if self.ins._langs._this_get()["name"] == "ar":
                img = d["img_ar"]

            item = [
                {"start": "true", "class": f"wi-slideshow-slide {a} _{itm}"},
                {"_type": "img", "class": "wi-slideshow-image","loading":"lazy","src": img},
                {"_data": d["des"], "_data-ar":d.get("des_ar",""),"_trans":"true","class": "gla-data  wi-slideshow-data","style": "position: absolute;left: 70px; bottom: 70px; width:100%;"},
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
             {"_type": "img","loading":"lazy",
                          "class": f"", "src": d["th"]},
                
                {"end": "true"}

            ]
            uidata +=item

        uidata.append({"end": "true"})
        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)
