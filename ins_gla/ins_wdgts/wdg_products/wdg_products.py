from ins_kit._engine._bp import Widget


class WdgProducts(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        data = [
            {"title": "250gm Gold Bar", "price": "E£ 208,750.00",
             "image": "style/g1.svg", "class": ""},
            {"title": "250gm Gold Bar",
                "image": "style/g1.svg", "class": "", "price": "E£ 208,750.00"},
            {"title": "250gm Gold Bar",
                "image": "style/g1.svg", "class": "", "price": "E£ 208,750.00"},
            {"title": "250gm Gold Bar",
                "image": "style/g1.svg", "class": "", "price": "E£ 208,750.00"},
        ]
        gstyle = 'column-gap: 32px !important;row-gap: 32px !important;--flex-gap: 32px !important;'
        uidata = [
            {"start": "true", "class": "ins-flex-center  ins-padding-2xl gla-container "},
            {"class": "ins-space-l"},
            {"_data": "Exceptional Collection",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m"},
            {"class": "ins-col-grow "},
            {"_data": "<i class=' lni ins-icon lni-arrow-left'></i>",
                "style": "margin-right:12px", "class": "ins-button-cricle ins-grey-d"},
            {"_data": "<i class=' lni ins-icon lni-arrow-right'></i>",
                "class": "ins-button-cricle ins-grey-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex gla-tabs-header"},
            {"_data": "Gold Bars", "class": " ins-strong-m  gla-active "},
            {"_data": "Gold Bars"},
            {"_data": "Gold Bars"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex-start", "style": gstyle},
            {"class": "ins-space-s"},
        ]
        p = "/ins_web/ins_uploads/"
        for d in data:
            st = "width:316px;"
            r = [{"start": "true", "class": "ins-flex  gla-pro-block  ", "style": st},
                 {"start": "true", "class": " gla-img-cont  ",
                     "style": ""},
                 {"_data": "Bestseller", "class": "ins-tag ins-primary  ins-radius-s",
                     "style": "   position: absolute;top: 8px;left: 8px;"},
                 {"src": p + d["image"], "_type": "img",
                     "class": "gla-pro-img"},
                 {"src": p + "style/n5.svg", "_type": "img", "class": "gla-pro-himg"},
                 {"_data": "SHOP NOW <i class=' lni ins-icon lni-arrow-right'></i>",
                     "class": "ins-button gla-pro-hbutton ins-strong-m   ins-gold-bg"},
                 {"end": "true"},
                 {"class": "ins-space-s"},
                 {"_data": d["title"],
                     "class": "ins-col-12 ins-title-m ins-strong-m   ins-grey-color", "style": "line-height:24px"},
                 {"_data": d["price"],
                     "class": "ins-col-12  ins-strong-m  ins-primary-color", "style": "line-height:24px"},
                 {"end": "true"}]
            uidata += r
        uidata.append({"end": "true"})
        uidata.append({"class": "ins-space"})
        uidata.append({"class": "ins-space-xs"})
        uidata.append({"_data": "View MORE <i class=' lni ins-icon lni-arrow-right'></i>",
                      "style": "width:185px", "class": "ins-button  ins-text-upper ins-gold"},)
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
