from ins_kit._engine._bp import Widget


class WdgLegacy(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        
        
        
        self.widget._include("leg.css")
        self.widget._include("leg.js")
        
        data_50 = [

            {"start": "true", "class": "ins-col-12 _1  active gla-ltabs-item leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold – Three <br/> Generations Strong",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>",
                "style": "width:250px", "class": "ins-button-l  ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1950s", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "Founder’s Vision: A humble start with a small shop focused on selling pure gold in local markets.",
                "class": " ins-col-12 ins-strong-m ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l1.svg"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex-end    ",
             "style": "width:316px;height:406px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l2.svg"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]

        data_60 = [

            {"start": "true", "class": "ins-col-12 _2  gla-ltabs-item leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold – Three <br/> Generations Strong",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>",
                "style": "width:250px", "class": "ins-button-l  ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1960s", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "Founder’s Vision: A humble start with a small shop focused on selling pure gold in local markets.",
                "class": " ins-col-12 ins-strong-m ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex   gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l1.svg"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex-end    ",
             "style": "width:316px;height:406px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l2.svg"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]

        data_70 = [

            {"start": "true", "class": "ins-col-12 _3  gla-ltabs-item leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold – Three <br/> Generations Strong",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>",
                "style": "width:250px", "class": "ins-button-l  ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1970s", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "Founder’s Vision: A humble start with a small shop focused on selling pure gold in local markets.",
                "class": " ins-col-12 ins-strong-m ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex  gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l1.svg"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex-end    ",
             "style": "width:316px;height:406px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l2.svg"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]
        data_80 = [

            {"start": "true", "class": "ins-col-12 gla-ltabs-item   _4 leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold – Three <br/> Generations Strong",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>",
                "style": "width:250px", "class": "ins-button-l  ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1980s", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "Founder’s Vision: A humble start with a small shop focused on selling pure gold in local markets.",
                "class": " ins-col-12 ins-strong-m ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l1.svg"},
            {"end": "true"},
            {"start": "true", "class": "ins-flex-end    ",
             "style": "width:316px;height:406px"},
            {"_type": "img", "src": "ins_web/ins_uploads/style/l2.svg"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]
        uidata = [
            {"start": "true", "class": "ins-primary-w "},
            {"start": "true", "class": "ins-flex  ins-padding-2xl gla-container ",
             "style": "padding-bottom:12px"},
            
               {"start": "true", "class": "gla-ltabs-cont ins-flex ins-col-12 ",
             },
            
             
            
            
        ]

        uidata += data_50
        uidata += data_60
        uidata += data_70
        uidata += data_80

        footer = [
                  {"end": "true"},
            {"class": "ins-space-l"},



            {"start": "true", "class": "ins-flex ins-col-12", },
            
            
            {"_data": "1950s", "data-show":"_1", "style": "font-size:20px",
             "class": "ins-col-3 gla-ltabs gla-active"},
            {"_data": "1960s","data-show":"_2",  "style": "font-size:20px",
             "class": "ins-col-3 gla-ltabs", },
            {"_data": "1970s", "data-show":"_3", "style": "font-size:20px",
             "class": "ins-col-3  gla-ltabs", },
            {"_data": "1980s", "data-show":"_4", "style": "font-size:20px",
             "class": "ins-col-3  gla-ltabs"},



            {"end": "true"},
            {"class": "ins-space-l"},
            {"end": "true"}, {"end": "true"}

        ]

        uidata += footer

        return self.ins._ui._render(uidata)
