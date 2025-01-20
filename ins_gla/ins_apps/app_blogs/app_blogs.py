from ins_kit._engine._bp import App


class AppBlogs(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)



    def _ui(self):
        
        data = self.ins._db._get_data("gla_blog","*")
        p = "/ins_web/ins_uploads/"

        uidata = [{"start":"true","class":"ins-col-12 gla-container ins-padding-2xl ins-flex ins-gap-l"}]

        
        for d in data:
            st = "width:316px;margin-bottom: 32px;"
            blog = [{"start": "true", "class": "ins-flex   pro-blog-block ", "style": st},
                 {"src": p + d["image"], "_type": "img"},
                 {"_data": d["title"], "class": "ins-col-12 ins-title-m   ins-grey-color"},
                 {"end": "true"}]

            """  blog = [
            {"start":"true","class":"ins-col-12  ins-flex-start ins-padding-l ins-card ins-gap-l"},
            {"_data":f"<img style='    max-width: 320px;'  src= '{p}{d["image"]}'></img>","class":"ins-text-center"},
          
            {"start":"true","class":"ins-col-9"},
            {"_data": d["title"],"class":"ins-col-12 ins-grey-d-color ins-strong-l ins-title-m"},
            {"_data": str(d["kit_created"]),"_view":"date","class":"ins-col-12 ins-strong-m ins-grey-m-color ins-font-s"},
            {"_data": d["content"],"class":"ins-col-12"},
          
            {"start":"true","class":"ins-col-12 ins-flex-end "},
            {"class":"ins-space-l"},
            {"class":"ins-button-s ins-gold ins-col-2 ins-text-center","_data":"More"},
            {"end":"true"},
          
            {"end":"true"},
            
            {"end":"true"},
            
               ]

            blog = [
            {"start":"true","class":"ins-col-4 ins-padding-l   ins-card"},
            {"_data":f"<img style='max-width:320px' src= '{p}{d["image"]}'></img>","class":"ins-col-12 ins-text-center"},
            {"_data": str(d["kit_created"]),"_view":"date","class":"ins-col-12 ins-grey-m-color ins-strong-m ins-font-s"},
            {"_data": d["title"],"class":"ins-col-12 ins-grey-d-color ins-strong-l ins-title-m"},
            {"_data": d["content"],"_view":"limit", "limit_ops":"50","class":"ins-col-12"},
            {"start":"true","class":"ins-col-12 ins-flex-end "},
            {"class":"ins-button-s ins-gold ins-col-4 ins-text-center","_data":"More"},
            {"end":"true"},
            {"end":"true"},
            
               ]"""""
            uidata+=blog



        uidata.append({"end":"true"})


        return self.ins._ui._render(uidata)

       
    def out(self):
        
       return self._ui()