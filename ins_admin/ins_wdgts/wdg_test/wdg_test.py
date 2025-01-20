
from ins_kit._engine._bp import Widget


class WdgTest(Widget):

    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)



    def ddddddd(s,a="adas"):
        pass


    def out(self):
        

      
       
       
        
        return  f"{ self.widget._options.get("ops_des","")} {self.widget._options.get("ops_test","dsfsdfds")}"
