
import datetime
from ins_kit._engine._bp import Widget


class WdgTicker(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def _ui(self):
         price = self.ins._db._get_row("gla_price","*","1=1 order by id desc")
         coin_sell = price["sell"]
         coin_buy = price["buy"]

         bar_sell = price["sell_24"]
         bar_buy = price["buy_24"]
         date = self.ins._date._format(price["kit_created"] + datetime.timedelta(hours=2), "%I:%M %p, %A, %d %B %Y") 
         date_text = "Last Updated: " + date


         if self.ins._langs._this_get()["name"] == "ar":
            days_ar = {
                "Sunday": "الأحد", "Monday": "الإثنين", "Tuesday": "الثلاثاء",
                "Wednesday": "الأربعاء", "Thursday": "الخميس", "Friday": "الجمعة", "Saturday": "السبت"
            }

            months_ar = {
                "January": "يناير", "February": "فبراير", "March": "مارس", "April": "أبريل",
                "May": "مايو", "June": "يونيو", "July": "يوليو", "August": "أغسطس",
                "September": "سبتمبر", "October": "أكتوبر", "November": "نوفمبر", "December": "ديسمبر"
            }

            date = date.replace("AM", "ص").replace("PM", "م")
            for en, ar in days_ar.items():
                date = date.replace(en, ar)
            for en, ar in months_ar.items():
                date = date.replace(en, ar)

            arabic_digits = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
            date = date.translate(arabic_digits)
            date_text = "آخر تحديث: " + date
                

        
         uidata = [
              {"start":"true","class":"ins-flex ins-secondary ins-sticky-top i ","style":"z-index: 1113"},
              {"start":"true","class":"ins-flex  ins-gap-20 ins-col-12 ins-padding-xl"},
             
              {"start":"true","class":"ins-flex"},
              {"class":"gla-logo gla-logo","style":"width: 120px; height:120px"},
              {"end":"true"},

              {"_data":"EL GALLA GOLD","class":"ins-col-6 ins-title-xl"},

              {"start":"true","class":"ins-flex ins-col-4"},

              {"_data":date_text,"class":"ins-col-12 ins-flex"},
              {"start":"true","class":"ins-flex  ins-col-12 "},
              {"_data":f"Sell - {coin_sell} EGP","_data-ar":f"بيع - {coin_sell} جنيه","_trans":"true"},
              {"_data":"(21K)","_data-ar":"(21عيار) ","_trans":"true","class":"ins-primary-d","style":"max-height: 24px;line-height: 21px;padding: 2px;"},
              {"_data":f"Buy - {coin_buy} EGP","_data-ar":f"شراء - {coin_buy} جنيه","_trans":"true"},
              {"end":"true"},

              {"start":"true","class":"ins-flex  ins-col-12 "},
              {"_data":f"Sell -    {bar_sell} EGP","_data-ar":f"بيع - {bar_sell} جنيه","_trans":"true"},
              {"_data":"(24K)","_data-ar":"(24عيار) ","_trans":"true","class":"ins-primary-d","style":"max-height: 24px;line-height: 21px;padding: 2px;"},
              {"_data":f"Buy -    {bar_buy} EGP","_data-ar":f"شراء - {bar_buy} جنيه","_trans":"true"},
              {"end":"true"},

              {"end":"true"},

             
              {"end":"true"},
              {"end":"true"},
              ]
         
         return self.ins._ui._render(uidata)

    def out(self):
          
          return self._ui()
