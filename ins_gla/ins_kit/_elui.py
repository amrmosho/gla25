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


    def cart_pro_block(self,data,string=False):
        
        p = "/ins_web/ins_uploads/"
        item_total_des = int(data["count"]) * int(data["weight"])
        item_total_amount = int(data["count"])* int(data["price"])

        uidata =[
         {"start":"true","class":"ins-col-12 ins-flex -item-card ins-border ins-radius-l ins-gap-o"},
         {"start":"true","class":"ins-col-4 ins-flex-center","style":"height: 200px;overflow: hidden;    border-radius: 8px 0px 0px 8px;"},
        
         {"src":f"{p}{data.get("th_main","")}", "_type": "img","class":"ins-radius-m","style":"    height: 100%;"},
                 {"end":"true"},



         {"start":"true","class":"ins-col-8  ins-flex-grow ins-primary-w ins-padding-l","style":"height: 200px;border-radius: 0px 8px 8px 0px;    border-left: 1px solid var(--primary-l);"},
         {"_data":"Item summary" ,"class":"ins-col-12 ins-title-s ins-strong-l ins-grey-d-color"},        
         {"_data": f"{data.get("count","")} x {data["title"]}" ,"class":"ins-col-8 ins-strong-m ins-grey-color","style":"font-size:14px"},
         {"_data":str(data["price"]),"class":"ins-col-4 ins-strong-m ins-grey-d-color ins-flex-end","style":"font-size:14px"},
         {"class":"ins-line ins-col-12"},
         {"_data": f"{item_total_des}gm  {data.get("category","")} " ,"class":"ins-col-6 ins-strong-m ins-grey-color","style":"font-size:14px"},
         {"_data":f"{item_total_amount}","class":"ins-col-6 ins-strong-m ins-grey-d-color ins-flex-end","style":"font-size:14px"},
         {"_data": "<img src='"+p+"style/cart.svg'></img> ADD TO CART","data-pid":data["id"], "class": "ins-button-s ins-flex-center ins-font-m ins-strong-m ins-flex-grow ins-gold-d -add-cart-btn","style":"border: 1px solid var(--primary-d);"},
         {"end":"true"},
         {"end":"true"}

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
       