
from ins_kit._engine._bp import Widget


class WdgTicker(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def _ui(self):
         coin = self.ins._db._get_row("gla_product","price,buy_price,stamp,vat,cashback","id='2'")
         bar = self.ins._db._get_row("gla_product","price,buy_price,stamp,vat,cashback","id='12'")
         coin_price = float(coin["price"]) -  float(coin["stamp"]) -  float(coin["vat"])
         coin_buy = float(coin["buy_price"]) -  float(coin["cashback"]) 
        
         coin_price = self.ins._data._format_currency(float(coin_price), symbol=False)
         coin_buy = self.ins._data._format_currency(float(coin_buy), symbol=False)

         bar_price = float(bar["price"]) -  float(bar["stamp"]) -  float(bar["vat"])
         bar_buy = float(bar["buy_price"]) -  float(bar["cashback"]) 

         bar_price = self.ins._data._format_currency(float(bar_price), symbol=False)
         bar_buy = self.ins._data._format_currency(float(bar_buy), symbol=False)




         def calculate_charge(self,data):
            chargs = 0
            if data["gram"] == 1:
                chargs = (float(data["stamp"]) + float(data["vat"]) ) * float(data["weight"])
            else:
                chargs = (float(data["weight"])  * float(data["vat"])  ) + float(data["stamp"]) 
            return chargs


         def calculate_chashback(self,data):
            chashback = 0
            if data["cashback_gram"] == 1:
                chashback = float(data["cashback"]) * float(data["weight"])
            else:
                chashback = data["cashback"]
            return chashback



        
         uidata = [
              {"start":"true","class":"ins-secondary ins-sticky-top i ","style":"z-index: 1113"},


              {"start":"true","class":"ins-flex-center  ins-gap-20 "},
             
              {"_data":"Updated At: 12:30 PM, Monday, 17 February 2025  ","_data-ar":"اخر تحديث: 12:30 مساءً, الأثنين, 17 فبراير 2025","_trans":"true"},
              {"_data":f"Buy -    {coin_price} EGP","_data-ar":f"شراء - {coin_price} جم","_trans":"true"},
                            {"_data":"(21K)","_data-ar":"(21عيار) ","_trans":"true","class":"ins-primary-d","style":"max-height: 24px;line-height: 21px;padding: 2px;"},

              {"_data":f"Sell -    {coin_buy} EGP","_data-ar":f"بيع - {coin_buy} جم","_trans":"true"},

{"_data":"|"},
                          {"_data":f"Buy -    {bar_price} EGP","_data-ar":f"شراء - {bar_price} جم","_trans":"true"},
               {"_data":"(24K)","_data-ar":"(24عيار) ","_trans":"true","class":"ins-primary-d","style":"max-height: 24px;line-height: 21px;padding: 2px;"},
             
              {"_data":f"Sell -    {bar_buy} EGP","_data-ar":f"بيع - {bar_buy} جم","_trans":"true"},

            
            
              {"end":"true"},
            
            
            
              {"end":"true"},


              ]
         
         return self.ins._ui._render(uidata)

    def out(self):
          
          return self._ui()
