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
            {"_data": "A Legacy of Gold<br/> The Story of El-Galla Gold ","_data-ar":"إرث من الذهب<br/> قصة الذهب في الجلا" ,"_trans":"true",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"/about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>","_data-ar":"معلومات عنا","_trans":"true",
                "style": "width:250px", "class": "ins-button-l -about-button ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ins-m-col-12  -about-title-area ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning","_data-ar":"البداية" ,"_trans":"true",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1950s","_data-ar":"١٩٥٠" ,"_trans":"true", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12 ins-text-none",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "El Galla Gold was established in 1950, our family-owned business has been passed down through generations, each adding to our rich legacy with their unique knowledge and experience, carrying forward the vision that originally started with Hassan El Galla.",
                "_data-ar":"تأسست شركة الجلا جولد عام 1950 تحت قيادة مؤسسها الحاج حسن الجلا،  وتم توارثها من جيل لجيل، وزي الذهب اتعرف الحاج حسن بصدقه والتزامه وكانت القيم والدروس التي اكتسبها في حياته مصدر إلهام في مسيرته لتحقيق الجودة و الوصول إلى رضاء العملاء و اللي بنعتبره القوة الدافعة وراء نجاحنا." ,"_trans":"true",
                
                "class": " ins-col-12 -legacy-content", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start","style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img","loading":"lazy", "src": "/ins_web/ins_uploads/images/about_us/1950s.png"},
            {"end": "true"},
     
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]

        data_60 = [

            {"start": "true", "class": "ins-col-12 _2  gla-ltabs-item leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold<br/> The Story of El-Galla Gold ","_data-ar":"إرث من الذهب<br/> قصة الذهب في الجلا" ,"_trans":"true",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"/about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>","_data-ar":"معلومات عنا","_trans":"true",
                "style": "width:250px", "class": "ins-button-l  -about-button ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ins-m-col-12  -about-title-area ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning","_data-ar":"البداية" ,"_trans":"true",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "1980s", "_data-ar":"١٩٨٠" ,"_trans":"true","class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12 ins-text-none",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "The second generation, led by Ahmed Hassan El-Galla, expanded our operations and embraced modern business practices. He was a mentor and leader to many, and his tenure marked a significant growth phase as we expanded our product range and strengthened our market presence.",
                
                "_data-ar":"ومع تطور الشركة، ابتدي الجيل الثاني بقيادة الحاج أحمد حسن الجلا في توسيع عملياتنا واعتماد ممارسات تجارية حديثة وكان أول من بدأ تصنيع بيع العملات والسبائك الذهبية في السوق المصرية. مكنش مجرد قائد، بل كان أب روحي لناس كتير في صناعة و تجارة الذهب. كانت الفترة دي مرحلة نمو كبيرة، قمنا بتوسيع مجموعة منتجاتنا وتعزيز وجودنا في السوق." ,"_trans":"true",
                "class": " ins-col-12 -legacy-content ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex   gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img","loading":"lazy", "src": "/ins_web/ins_uploads/images/about_us/1980s.png"},
            {"end": "true"},
           
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]

        data_70 = [

            {"start": "true", "class": "ins-col-12 _3  gla-ltabs-item leg-item ins-flex"},
            {"class": "ins-space-l"},

            {"_data": "A Legacy of Gold<br/> The Story of El-Galla Gold ","_data-ar":"إرث من الذهب<br/> قصة الذهب في الجلا" ,"_trans":"true",
             
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"/about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>","_data-ar":"معلومات عنا","_trans":"true",
                "style": "width:250px", "class": "ins-button-l  -about-button ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ins-m-col-12  -about-title-area ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning","_data-ar":"البداية" ,"_trans":"true",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "2020s","_data-ar":"٢٠٢٠" ,"_trans":"true", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12 ins-text-none",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "Today, the third generation, under the leadership of our CEO Osama Ahmed Hassan El-Galla, continues to build upon the strong foundation laid by our predecessors. He introduced new ways of using technology to simplify buying and selling gold.",
                "_data-ar":"النهاردة، الجيل الثالث بقيادة المهندس أسامة أحمد حسن الجلا يواصل البناء على الأسس القوية خلال عمر شركة الجلا جولد. وبدأ استخدام طرق جديدة زي التكنولوجيا لتسهيل عملية بيع وشراء الذهب " ,"_trans":"true",
                "class": " ins-col-12 -legacy-content ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex  gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img","loading":"lazy", "src": "/ins_web/ins_uploads/images/about_us/2020.png"},
            {"end": "true"},
          
            {"end": "true"},
            {"end": "true"}
            # end imegsa
        ]
        data_80 = [

            {"start": "true", "class": "ins-col-12 gla-ltabs-item   _4 leg-item ins-flex"},
            {"class": "ins-space-l"},
            {"_data": "A Legacy of Gold<br/> The Story of El-Galla Gold ","_data-ar":"إرث من الذهب<br/> قصة الذهب في الجلا" ,"_trans":"true",
                "class": "ins-title-xl ins-grey-d-color ins-strong-m", "style": "line-height:50px"},
            {"class": "ins-col-grow "},
            {"_type":"a","href":"/about_us","_data": "About US  <i class=' lni ins-icon lni-arrow-right'></i>","_data-ar":"معلومات عنا","_trans":"true",
                "style": "width:250px", "class": "ins-button-l  -about-button ins-text-upper ins-gold-d"},
            {"class": "ins-space-l"},
            {"start": "true", "class": "ins-flex-center ins-grey-color ins-m-col-12  -about-title-area ",
                "style": "width:500px;height:406px"},
            {"_data": "The Beginning","_data-ar":"البداية" ,"_trans":"true",
                "class": "ins-text-upper ins-title-m  ins-strong-m ins-col-12"},
            {"class": "ins-space-s"},
            {"_data": "Present Day","_data-ar":"اليوم الحاضر" ,"_trans":"true", "class": "ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12",
                "style": "line-height:60px"},
            {"class": "ins-space-s"},
            {"_data": "As we look to the future, we remain committed to our heritage, morals, and passion. The name of El-Galla Gold will remain, as we have always promised, a symbol of trust.",
                "_data-ar":"ننظر إلى المستقبل بنفس القيم والمبادئ اللي بدأنا بيها، هدفنا هو تقديم قطع من الذهب تحمل جزءًا من تاريخنا، إلى عملائنا. حتى تستمر الرحلة، ويبقى اسم الجلّا جولد، زي ما وعدناكم دائمًا، رمزًا للثقة." ,"_trans":"true",
                "class": " ins-col-12 -legacy-content ", "style": "line-height:24px;font-size:20px"},
            {"end": "true"},

            # data
            {"class": "ins-col-grow"},
            # end imegsa
            {"start": "true", "class": "ins-flex gla-alogo-primary-l",
             "style": "    background-size: 166px auto;background-position: 58% top;"},
            {"start": "true", "class": "ins-flex-start",
             "style": "width:316px;height:406px;margin:0 10px"},
            {"_type": "img","loading":"lazy", "src": "/ins_web/ins_uploads/images/about_us/now.png"},
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
            
            
            {"_data": "1950s","_data-ar":"١٩٥٠" ,"_trans":"true", "data-show":"_1", "style": "font-size:20px",
             "class": "ins-col-3 gla-ltabs gla-active ins-m-col-3"},
            {"_data": "1980s","_data-ar":"١٩٨٠" ,"_trans":"true","data-show":"_2",  "style": "font-size:20px",
             "class": "ins-col-3 gla-ltabs ins-m-col-3", },
            {"_data": "2020s","_data-ar":"٢٠٢٠" ,"_trans":"true", "data-show":"_3", "style": "font-size:20px",
             "class": "ins-col-3  gla-ltabs ins-m-col-3", },
            {"_data": "Present Day","_data-ar":"اليوم الحاضر" ,"_trans":"true", "data-show":"_4", "style": "font-size:20px",
             "class": "ins-col-3  gla-ltabs ins-m-col-3"},



            {"end": "true"},
            {"class": "ins-space-l"},
            {"end": "true"}, {"end": "true"}

        ]

        uidata += footer

        return self.ins._ui._render(uidata)
