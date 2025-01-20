from ins_kit.ins_parent import ins_parent


class ELUI(ins_parent):
        
    def __init__(self, Ins) -> None:
        super().__init__(Ins)


    def small_pro_block(self,data,string=False):

        p = "/ins_web/ins_uploads/"
        uidata =[
         {"start":"true","class":"ins-col-12 ins-flex -item-card"}
        ,{"src":f"{p}{data.get("th_main","")}", "_type": "img","class":"ins-radius-m","style":"    width: 97px;"}
        ,{"start":"true","class":"ins-col-8 ins-flex"}
        ,{"start":"true","class":"ins-col-12 ins-flex  ins-gap-o"}
        ,{"_data":data.get("title","") ,"class":"ins-col-12 ins-font-l ins-strong-l ins-grey-d-color","style":"    !important;"}
        ,{"_data": data.get("des",""),"class":"ins-grey-color ins-col-12","style":"font-size:14px; line-height: 20px; "}
        ,{"end":"true"}
        ,{"_data": str(data["price"]),"class":"ins-col-12 ins-strong-l ins-primary-d-color","style":"    font-size: 20px;   ;"}
        ,{"end":"true"}
        ,{"_data":f"<img src='{p}/style/trash.svg'><img>","class":"ins-flex-center ins-col-1 -remove-item-cart-btn","data-pid":data["id"]}
        ,{"end":"true"}

        ]

        if string:
           return  self.ins._ui._render(uidata)
        return uidata

    def counter_pro_block(self ,  data,string=False):
        p = "/ins_web/ins_uploads/"

        uidata =[
         {"start":"true","class":"ins-col-12 ins-flex -item-card"}
        ,{"src":f"{p}{data.get("th_main","")}", "_type": "img","class":"ins-radius-m","style":"    width: 97px;"}
        ,{"start":"true","class":"ins-col-6 ins-flex"}
        ,{"start":"true","class":"ins-col-12 ins-flex  ins-gap-o"}
        ,{"_data":data.get("title","") ,"class":"ins-col-12 ins-font-l ins-strong-l ins-grey-d-color","style":"    !important;"}
        ,{"_data": data.get("des",""),"class":"ins-grey-color ins-col-12","style":"font-size:14px; line-height: 20px; "}
        ,{"end":"true"}
        ,{"_data": str(data["price"]),"class":"ins-col-12 ins-strong-l ins-primary-d-color","style":"    font-size: 20px;   ;"}
        ,{"end":"true"},
        {"start": "true", "class": "ins-flex ins-col-3 -counter-cont ins-gap-o"},
        {"_data": "-", "class": "ins-button-s ins-flex-center ins-col-4 ins-gold-bg ins-font-2xl -minus-btn","data-pid" : data.get("id",0)},
        {"_type": "input",  "name":"count_inpt","type": "text","value":data["count"], "pclass": "ins-col-4 ","class":"count-inpt ins-font-m ins-strong-l"},
        {"_data": "+", "class": "ins-button-s ins-flex-center  ins-col-4  ins-gold-bg ins-font-2xl  -plus-btn","data-pid" : data.get("id",0)},
        {"end": "true"},
        {"_data":f"<img src='{p}/style/trash.svg'><img>","class":"ins-flex-center ins-col-1 -remove-item-cart-btn","data-pid":data["id"]},
        {"end":"true"},

        ]

        if string :
           return  self.ins._ui._render(uidata)
        return uidata
       