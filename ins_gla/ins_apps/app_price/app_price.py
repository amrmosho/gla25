from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App
import uuid
import json
class AppPrice(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def myround(self, x, base=5):
        x = round(x)
        return base * round(x/base)
    def reportui(self, data):
        r = ""
        header = [{"_data": "id", "class": "", "style": "width:50px"},
                  {"_data": "title", "class": "ins-col-grow", "style": ""},
                  {"_data": " buy price", "class": "", "style": "width:120px"},
                  {"_data": " sell price", "class": "", "style": "width:120px"},
                  {"_data": "weight", "class": "", "style": "width:50px"},
                  {"_data": "stamp", "class": "", "style": "width:150px"},
                  {"_data": "vat", "class": "", "style": "width:50px"},
                  {"_data": "cashback", "class": "", "style": "width:150px"},
                  {"_data": "", "class": "ins-danger", "style": "width: 1px;padding: 2px; min-width: 2px;  background: #4fa8b5 !important"},
                  {"_data": "buy price", "class": "", "style": "width:120px"},
                  {"_data": "Gram", "class": "", "style": "width:120px"},
                  {"_data": "price", "class": "ins-primary-color",
                      "style": "width:120px"},
                  {"_data": "sell price", "class": "", "style": "width:120px"},
                  {"_data": "Gram ", "class": "", "style": "width:120px"},
                  {"_data": "price", "class": " ins-primary-color",
                      "style": "width:120px"},
                  ]
        body = []
        for d in data:
            grm = "G"
            if str(d["gram"]) != "1":
                grm = "P"
            cgrm = "G"
            if str(d["cashback_gram"]) != "1":
                cgrm = "P"
            rw = [{"_data": str(d["id"]), "class": "", "style": "width:50px"},
                  {"_data": d["title"], "class": "ins-col-grow", "style": ""},
                  {"_data": str(d["price"]), "class": "ins-col-1"},
                  {"_data": str(d["price"]), "class": "ins-col-1"},
                  {"_data":  str(d["weight"]), "class": "",
                   "style": "width:50px"},
                  {"_data": str(d["stamp"])+"/"+grm,
                   "class": "", "style": "width:150px"},
                  {"_data": str(d["vat"]), "class": "", "style": "width:50px"},
                  {"_data": str(d["cashback"])+"/"+cgrm,
                   "class": "", "style": "width:150px"},
                  {"_data": "", "class": "ins-bg-6", "style": "width: 1px;padding: 2px; min-width: 2px;    background: #4fa8b5 !important;"},
                  {"_data": f"<b>{str(d["new_main_bprce"])}</b>",
                   "class": "", "style": "width:120px"},
                  {"_data": f"<b>{str(d["gram_price_bay"])}</b>",
                   "class": "", "style": "width:120px"},
                  {"_data": f"<b class='insaction ' data-insaction='ins_tooltip' data-tip='{d["new_bay_price_tip"]}'  class=''>{str(d["new_bay_price_f"])}</b>",
                   "class": " ins-primary", "style": "width:120px;    cursor: alias;"},
                  {"_data": f"<b>{str(d["new_main_prce"])}</b>",
                   "class": "", "style": "width:120px"},
                  {"_data": f"<b>{str(d["gram_price_sell"])}</b>",
                   "class": "", "style": "width:120px"},
                  {"_data": f"<b class='insaction ' data-insaction='ins_tooltip' data-tip='{d["new_sell_price_tip"]}'>{str(d["new_sell_price_f"])}</b>",
                   "class": "ins-primary", "style": "width:120px;    cursor: alias;"},
                  ]
            body.append(rw)
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-padding-xl "},
            {"start": "true", "class": "ins-col-12 ins-card ins-flex ins-gap-20"},
            {"_data": "<i class='lni-bar-chart-4 lni ins-icon '></i>  Update price report",
                "class": "ins-col-grow ins-title-m ins-flex"},
            {"_data": "", "class": "lni lni-refresh-circle-1-clockwise   lni-printer ins-font-xl "},
            {"_data": "", "class": "lni ins-icon  lni-printer ins-font-xl "},
            {"_data": "", "class": "lni ins-icon   ins-font-xl lni-download-1"},
            {"": "", "class": "ins-line ins-col-12"},
            {"_type": "table",
             "class": " ins-col-12 ins-table ins-table-regular ins-pading-xl ", "data": body, "header": header},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    def cal(self, g, st="report"):
        r = ""
        data = self.ins._db._get_data("gla_product")
        oprice = float(g["sell"])
        obprice = float(g["buy"])
        price_24 = (float(oprice) * 999.9) / 875
        bprice_24 = (float(obprice) * 999.9) / 875
        price_24 = round(price_24)
        bprice_24 = round(bprice_24)
        if st == "update":
        
            
            sql = {"sell": g["sell"], 
                       "bay": g["buy"] ,
                       
                       "sell_24": price_24, 
                       "bay_24": bprice_24
                       
                       
                       
                       }
            
            
            
            
            self.ins._db._update("gla_price", sql ,"1=1")

        for d in data:
      
            del d["images"]
            del d["th_main"]
            del d["kit_created"]
            del d["kit_modified"]
            del d["th_overlay"]
            del d["kit_deleted"]
            del d["kit_disabled"]
            del d["display_home"]
            del d["des"]
            del d["fk_product_category_id"]
            d["---"] = "--------------------------------------------"
            d["new_sell_price_tip"] ="<div>"
            d["new_bay_price_tip"] ="<div>"

            sptl ="<br/><hr/>"

            spt ="<br/>"
            if d["kart"] != "21":
                price = price_24
                bprice = bprice_24


                d["new_bay_price_tip"] +="<b> kart : 24  </b>"
                d["new_bay_price_tip"] +=f'{sptl} <b> Main Price </b> <br/> (price * 999.9) / 875 {spt} ({obprice} * 999.9) / 875 =  <b class="ins-info-color"> {bprice} </b>'


                d["new_sell_price_tip"] +="<b> kart : 24  </b>"

                d["new_sell_price_tip"] +=f'{sptl} <b> Main Price </b> <br/> (price * 999.9) / 875 {spt} ({oprice} * 999.9) / 875 =  <b class="ins-info-color"> {price} </b>'
            else :
                price =oprice 
                price = round(price)
                bprice = obprice
                bprice = round(bprice)
                d["new_sell_price_tip"] +="<b> kart : 21  </b> "
                d["new_sell_price_tip"] +=f'{sptl} <b> Main Price </b> <br/>  {oprice}'
                
                
                d["new_bay_price_tip"] +="<b> kart : 21  </b> "
                d["new_bay_price_tip"] +=f'{sptl} <b> Main Price </b> <br/>  {bprice}'

                
                

         
            d["new_main_prce"] = price
       
            d["new_main_bprce"] = bprice
            # sell price
            gram_price_sell = price + float(d["vat"])
            

            if d["gram"] == 1:
                gram_price_sell += float(d["stamp"])
                d["new_sell_price_tip"] +=f'{sptl} <b>  Gram Price  </b> <br/> (price + vat + stamp) {spt}  {price} + {d["vat"]} + {d["stamp"]} = <b class="ins-info-color"> {gram_price_sell} </b>'
            else :
                d["new_sell_price_tip"] +=f'{sptl} <b> Gram Price </b> <br/> (price + vat) {spt}  {price} + {d["vat"]} =  <b class="ins-info-color"> {gram_price_sell} </b>'

                
            
            d["gram_price_sell"] = round(gram_price_sell)
            new_sell_price = gram_price_sell * float(d["weight"])

            

            
            if d["gram"] != 1:
                new_sell_price += float(d["stamp"])
                d["new_sell_price_tip"] +=f'{sptl} <b> New Sell Price </b> <br/> (price * weight) + stamp {spt}  {gram_price_sell} * {d["weight"]} +{d["stamp"]} =  <b class="ins-info-color"> {new_sell_price} </b>'
            else:
                d["new_sell_price_tip"] +=f'{sptl} <b> New Sell Price </b> <br/> (price * weight) {spt}  {gram_price_sell} * {d["weight"]} =  <b class="ins-info-color"> {new_sell_price} </b>'
                
                
                
            d["new_sell_price"] = new_sell_price
            
        
            new_sell_price = self.myround(new_sell_price)
            d["new_sell_price_tip"] +=f'{sptl} <b> Price After Round </b> <br/> 5 * round(price/5) {spt}  5 * round({d["new_sell_price"]}/5)   =  <b class="ins-info-color"> {new_sell_price} </b>'

            d["new_sell_price_f"] = new_sell_price
            
            
            d["new_sell_price_tip"] +="</div>"


            
            
            # buy  pric
            if d["cashback_gram"] == 1:
                gram_price_bay = bprice + float(d["cashback"])
                d["gram_price_bay"] = round(gram_price_bay)

                d["new_bay_price_tip"] +=f'{sptl} <b> Gram Price </b> <br/> (price + cashback) {spt}  {bprice} + {d["cashback"]} =  <b class="ins-info-color"> {d["gram_price_bay"]} </b>'
            else:
                gram_price_bay = bprice
                d["gram_price_bay"] = round(gram_price_bay)
                d["new_bay_price_tip"] +=f'{sptl} <b> Gram Price </b> <br/>  =  <b class="ins-info-color"> {d["gram_price_bay"]} </b>'
 
                
                
            new_bay_price = gram_price_bay * float(d["weight"])


            
            
            if d["cashback_gram"] != 1:
                new_bay_price += float(d["cashback"])
                d["new_bay_price_tip"] +=f'{sptl} <b> New Bay Price </b> <br/> (price * weight) + cashback {spt}  {gram_price_bay} * {d["weight"]} + {d["cashback"]} =  <b class="ins-info-color"> {new_bay_price} </b>'

            else:
                d["new_bay_price_tip"] +=f'{sptl} <b> New Bay Price </b> <br/> (price * weight) {spt}  {gram_price_bay} * {d["weight"]} =  <b class="ins-info-color"> {new_bay_price} </b>'

            d["new_bay_price"] = new_bay_price
            new_bay_price = self.myround(new_bay_price)
            d["new_bay_price_f"] = new_bay_price

            d["new_bay_price_tip"] +=f'{sptl} <b> Price After Round </b> <br/> 5 * round(price/5) {spt}  5 * round({d["new_bay_price"]}/5)   =  <b class="ins-info-color"> {new_bay_price} </b>'

            
            
            
            d["new_bay_price_tip"] +="<div>"

            
            
            r = ""
            if st == "update":
                sql = {"price": d["new_sell_price_f"],
                       "buy_price": d["new_bay_price_f"]}
                self.ins._db._update("gla_product", sql, f"id='{d["id"]}'")
                
                
                uidata = [
                    {"start": "true", "class": "ins-col-12  ins-padding-l  ins-padding-v  ins-flex-center"},
                    { "class": "ins-card ins-flex ins-col-6 ins-font-xl ins-info" ,"_data": "<i class='lni lni-check-circle-1 ins-icon'> </i>  Data updated successfully."},
                    {"end": "true"},
                ]
                r = self.ins._ui._render(uidata)
        r += self.reportui(data)
        return r
    def report(self, g):
        return self.cal(g)
    def update(self, g):
        return self.cal(g, "update")
    def ui(self, g):
        uidata = [
            {"start": "true", "class": "ins-col-12 ins-flex-center a-price-cont"},
            {"start": "true", "class": "ins-col-6 ins-flex"},
            {"start": "true", "class": "ins-col-12  ins-card ins-flex "},
            {"_type": "input", "type": "number",
                "title": "Buy price", "value": g.get("buy", ""), "name": "buy", "required": "true", "pclass": "ins-col-12 "},
            {"_type": "input", "type": "number",
             "title": "Sell price", "name": "sell", "value": g.get("sell", ""), "required": "true",  "pclass": "ins-col-12 "},
            {"end": "true"},
            {"start": "true", "class": "ins-col-12 ins-card ins-gap-20 ins-flex-end"},
            {"_data": "Update",
                "class": "ins-col-4 ins-button  a-price-update-btn  ins-primary"},
            {"_data": "Report", "class": "ins-col-4 ins-button   a-price-report-btn ins-info"},
            {"end": "true"},
            {"end": "true"},
            {"end": "true"}
        ]
        return self.ins._ui._render(uidata)
    def out(self):
        g = self.ins._server._get()
        self.app._include("script.js")
        r = self.ui(g)
        if "set" in g and g["set"] == "report":
            r += self.report(g)
        elif "set" in g and g["set"] == "update":
            r += self.update(g)
        return r
