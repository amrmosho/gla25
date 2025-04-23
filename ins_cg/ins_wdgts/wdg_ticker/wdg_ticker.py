
import datetime
from ins_kit._engine._bp import Widget


class WdgTicker(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def _ui(self):

        
         uidata = [
              {"start":"true","class":"ins-flex ins-secondary ins-sticky-top i ","style":"z-index: 1113"},
              {"start":"true","class":"ins-flex-center  ins-gap-20 ins-col-12"},
                          {"_data":"SOON"},

              {"end":"true"},
              {"end":"true"},
              ]
         
         return self.ins._ui._render(uidata)

    def out(self):
          
          return self._ui()
