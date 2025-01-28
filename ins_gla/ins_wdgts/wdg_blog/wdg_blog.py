from ins_kit._engine._bp import Widget
class WdgBlog(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)
    def out(self):
        data = [
            {"title": "The History of Gold From Ancient Times to Modern Investments",
                "image": "style/n1.svg", "class": ""},
            {"title": "The History of Gold From Ancient Times to Modern Investments",
                "image": "style/n2.svg", "class": ""},
        ]
        data2 = [
              {"title": "The History of Gold From Ancient Times to Modern Investments","image": "style/n5.svg"},
        ]
        data3 = [
              {"title": "The History of Gold From Ancient Times to Modern Investments",
                "image": "style/n3.svg", "class": ""},
            {"title": "The History of Gold From Ancient Times to Modern Investments",
                "image": "style/n4.svg", "class": ""},
            ]
        gstyle='column-gap: 32px !important;row-gap: 32px !important;--flex-gap: 32px !important;'
       
       
       
        uidata = [
            {"start": "true", "class": "ins-flex  ins-padding-2xl gla-container " ,"style":"padding-bottom:12px"},
            {"class": "ins-space-l"},
            {"_data": "Explore Our Stories",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m"},
            {"class": "ins-col-grow "},
            {"_data": "ExpLORE MORE <i class=' lni ins-icon lni-arrow-right'></i>",  "style":"width:250px","class": "ins-button-l  ins-text-upper ins-gold"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-start pro-blog-parent " ,"style":gstyle},
        ]
        p = "/ins_web/ins_uploads/"
        uidata.append({"start": "true", "class": "ins-flex  pro-blog-cont -ba" ,"style":"width:316px"})
        for d in data:
            st = "width:316px;margin-bottom: 32px;"
            r = [{"start": "true", "class": "ins-flex   pro-blog-block ", "style": st},
                 {"src": p + d["image"], "_type": "img"},
                 {"_data": d["title"], "class": "ins-col-12 ins-title-m   ins-grey-color"},
                 {"end": "true"}]
            uidata += r
        uidata.append({"end": "true"})
        uidata.append({"start": "true", "class": "ins-flex  pro-blog-cont  -bb" ,"style":"width:664px"})
        for d in data2:
            st = "width:664px"
            r = [{"start": "true", "class": "ins-flex   pro-blog-block ", "style": st},
                 {"src": p + d["image"], "_type": "img"},
                 #{"_data": d["title"], "class": "ins-col-12"},
                 {"end": "true"}]
            uidata += r
        uidata.append({"end": "true"})  
        uidata.append({"start": "true", "class": "ins-flex pro-blog-cont -bc " ,"style":"width:316px"})
        for d in data3:
            st = "width:316px;margin-bottom: 32px;"
            r = [{"start": "true",  "class": "ins-flex pro-blog-block  ", "style": st},
                 {"src": p + d["image"], "_type": "img"},
                 {"_data": d["title"], "class": "ins-col-12 ins-title-m  ins-grey-color"},
                 {"end": "true"}]
            uidata += r
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)
