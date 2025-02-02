from ins_kit._engine._bp import App


class AppOrder(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

      


    def _status(ins, options, data):
     status_style = "background: #41b983; color: white;" 

     if data["order_status"] == "pending":
        status_style = "background: #12437D; color: white;"
     elif data["order_status"] == "confirmed":
        status_style = "background:#41b983; color: white;"

     uiadta = [{"_data": data["order_status"],  "style" :status_style ,"class" : " ins-col-8 ins-text-center ins-title-s ins-strong  ins-tag",}]
     return ins._ui._render(uiadta)

    def _payment_status(ins, options, data):
     status_style = "background: #41b983; color: white;" 

     if data["payment_status"] == "pending":
        status_style = "background: #12437D; color: white;"
     elif data["payment_status"] == "confirmed":
        status_style = "background:#41b983; color: white;"

     uiadta = [{"_data": data["payment_status"],  "style" :status_style ,"class" : " ins-col-8 ins-text-center ins-title-s ins-strong  ins-tag",}]
     return ins._ui._render(uiadta)
    
    def _total(ins, options, data):
     status_style = "border:solid 2px #12437D"

     uiadta = [{"_data": str(data["total"])+" EGP",  "style" :status_style ,"class" : " ins-card ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center",}]
     return ins._ui._render(uiadta)
    def _deatils(ins, options, data):

     uiadta = [{"_data": str(data["delivery_type"])+ " - "+str(data["payment_method"]),  "class" : "  ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center",}]
     return ins._ui._render(uiadta)
    def _id(ins, options, data):
     uiadta = [{"_data": "#"+ str(data["id"]), "data-tid":data["id"], "class" : "  ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center -order-btn",}]
     return ins._ui._render(uiadta)
    
    def _change_status(ins,options,data):
      uiadta = [{"_data": "<span class='lni lni-home-2'></span>", "data-tid":data["id"], "class" : "   ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center -change-status",}]
      return ins._ui._render(uiadta)
    

    def _change_status_ui(self):   
      rq = self.ins._server._post()
      
      uidata = [
        {"start":"true","class":"ins-col-12 ins-padding-m ins-flex"},
        {"_data":"Change status","class":"ins-col-9" },
        {"class":"ins-button ins-primary -save-status","_data":"Update Status","data-tid":rq["tid"]},
        {"_type":"select","_value":"pending","_data":"pending,confirmed","pclass":"ins-col-12","name":"status"},
        {"end":"true"}

        
        ]
      return self.ins._ui._render(uidata)


    
    def _update_statue(self):   
      rq = self.ins._server._post()
      new_status = rq["value"]
      update_data = {"payment_status": new_status} 
      self.ins._db._update("gla_order", update_data, f"id='{rq["oid"]}'")

      return "1"



    def _order_ui(self):   
      rq = self.ins._server._post()
      order_items = self.ins._db._ ("gla_order_item", "*", f"fk_order_id='{rq['tid']}'")

      
      uidata = [{"start": "true", "class": "ins-col-12 ins-flex"}]

      for item in order_items:
        uidata.append({"_data": f"{item['price']} ", "class": "ins-title-l ins-col-11"})
        uidata.append({"start": "true", "class": "ins-col-12 ins-flex"})
        uidata.append({"class": "ins-space-m"})

      uidata.append({"end": "true"})

      return self.ins._ui._render(uidata)
        
    def out(self):
        self.app._include("script.js")

        r = self.ins._apps._crud(properties=self.app._properties)

        return r
    
