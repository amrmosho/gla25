from datetime import datetime, timedelta
from ins_kit.ins_parent import ins_parent
class Pros(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
    
    @property
    def session_name(sel):
        return "cgproducts"
    
    def _remove_item_cart(self):
        data = self.ins._server._post()
        sedata = self.ins._server._get_session(self.session_name)
        sedata.pop(data["pid"])
        self.ins._server._set_session(self.session_name, sedata)
    
                    
    def _add_to_card(self):
        p = self.ins._server._post()
        sedata = self.ins._server._get_session(self.session_name)
        if type(sedata) != dict:
                sedata = {}
                
                
        rpdatas = self.ins._db._jget( "gla_product", "id,title,alias,th_main,views,price", f"gla_product.id='{p['pid']}'")
        rpdatas._jwith("gla_product_category cat", "title,alias,id", "cat.id=Substring_Index(fk_product_category_id, ',', 1)", join="left join")
        rpdata= rpdatas._jrun()[0]
              
        sedata[str(p['pid'])] =  rpdata
        self.ins._server._set_session(self.session_name, sedata)
 