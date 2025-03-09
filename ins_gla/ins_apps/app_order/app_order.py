from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App


class AppOrder(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

      


    def _status(ins, options, data):
     sclass = "" 

     if data["order_status"] == "pending":
        sclass = "ins-warning"
     elif data["order_status"] == "confirmed":
        sclass = "ins-secondary"

     uiadta = [{"_data": data["order_status"],  "class" : f" {sclass}  ins-col-8 ins-text-center ins-title-14 ins-strong-m  ins-tag",}]
     return ins._ui._render(uiadta)

    def _payment_status(ins, options, data):
     sclass = "" 

     if data["payment_status"] == "pending":
        sclass = "ins-warning"
     elif data["payment_status"] == "confirmed":
        sclass = "ins-secondary"

     uiadta = [{"_data": data["payment_status"], "class" : f"{sclass} ins-col-8 ins-text-center ins-title-14 ins-strong-m  ins-tag",}]
     return ins._ui._render(uiadta)
    
    def _total(ins, options, data):

     uiadta = [{"_data": str(data["total"]), "_view": "currency", "_currency_symbol": " EGP",
             "_currency_symbol_ar": " جنيه", "class" : " ins-primary-d ins-strong-l ins-flex-center ins-card ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center",}]
     return ins._ui._render(uiadta)
    def _deatils(ins, options, data):
     ptitle = ins._db._get_row("gla_payment_methods","title,kit_lang",f"id='{data["payment_method"]}'",update_lang=True)

     uiadta = [{"_data": ptitle["title"],  "class" : "  ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center",}]
     return ins._ui._render(uiadta)
    def _id(ins, options, data):
     uiadta = [{"_data": "#"+ str(data["id"]), "data-tid":data["id"], "class" : "  ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center -order-btn",}]
     return ins._ui._render(uiadta)
    
    def _change_status(ins,options,data):
      uiadta = [{"_data": "<span class='lni lni-refresh-user-1'></span>", "data-tid":data["id"], "class" : "   ins-col-12 ins-flex ins-padding-l ins-padding-h ins-font-xl -change-status",}]
      return ins._ui._render(uiadta)
    

    def _change_status_ui(self):   
      rq = self.ins._server._post()
      current_status = self.ins._db._get_row("gla_order", "order_status", f"id='{rq['tid']}'")["order_status"]
      
      uidata = [
         {"start":"true","class":"ins-col-12 ins-flex "},
        {"_data":"Change Order Status","class":"ins-col-11 ins-strong-m ins-title-s "},{"class":"ins-col-1 ins-text-right lni lni-xmark _a_red ins-view-close  ins-font-xl"},
        {"start":"true","class":"ins-col-12 ins-padding-m ins-flex-center"},
        {"_type":"select","_value":"pending","value":current_status,"placeholder":"Order Status","fl_data":{"pending":"Pending","confirmed":"Confirmed","canceled":"Canceled"},"pclass":"ins-col-12","name":"status"},
        {"class":"ins-button ins-primary -save-status","_data":"Update Status","data-tid":rq["tid"]},

        {"end":"true"},
        {"end":"true"}

        
        ]
      return self.ins._ui._render(uidata)


    
    def _update_statue(self):   
      rq = self.ins._server._post()
      new_status = rq["value"]
      update_data = {"order_status": new_status} 
      self.ins._db._update("gla_order", update_data, f"id='{rq["oid"]}'")
      return "1"


    def get_status_color(self, status):
        if status == "pending":
            return "warning"
        elif status == "confirmed":
            return "secondary"
        elif status == "canceled":
            return "danger"
        elif status == "delivered":
            return "success"
        return "default"

    def get_payment_status_color(self, status):
        if status == "success":
            return "success"
        elif status == "failed":
            return "danger"
        elif status == "pending":
            return "warning"
        return "default"


    def _order_ui(self):   
      rq = self.ins._server._post()
      sedata = self.ins._db._jget( "gla_order_item", "*", f"fk_order_id='{rq['tid']}'")
      sedata._jwith("gla_product product", "th_main",rfk="fk_product_id", join="left join")
      sedata = sedata._jrun()
      data = self.ins._db._get_row("gla_order", "*", f"id='{rq['tid']}'")
      user = self.ins._db._get_row("kit_user", "title", f"id='{data['fk_user_id']}'")["title"]


      address = ""
      if data["delivery_type"] == "delivery":
          user_address = self.ins._db._get_row(
              "gla_user_address", "*", f"id='{data['fk_address_id']}'", update_lang=True)
          address = f"{user_address['address']}, {user_address['city']}, {user_address['state']}"
      else:
          store_address = self.ins._db._get_row(
              "gla_address", "address,kit_lang", f"id='{data['fk_address_id']}'", update_lang=True)
          address = f"{store_address['address']}"

      payments = self.ins._db._get_row(
          "gla_payment_methods", "title,kit_lang", f"id='{data['payment_method']}'", update_lang=True)
      uidata = []
      tcount = 0
      if (data["order_status"] == "pending"):
          status = "Pending"
          status_ar = "قيد الانتظار "
      elif (data["order_status"] == "confirmed"):
          status = "Confirmed"
          status_ar = "مقبول"

      elif (data["order_status"] == "canceled"):
          status = "Canceled"
          status_ar = "ملغي"

      elif (data["order_status"] == "delivered"):
          status = "Delivered"
          status_ar = "تم التوصيل"

      if data['payment_status'] == "success":
          pstatus = "Success"
          pstatus_ar = "عملية ناجحة"
      elif data['payment_status'] == "failed":
          pstatus = "Failed"
          pstatus_ar = "عملية فاشلة"
      elif data['payment_status'] == "pending":
          pstatus = "Pending"
          pstatus_ar = "قيد الانتظار "

      uidata = [
         {"start":"true","class":"ins-col-12 ins-flex "}, 
          {"_data": f"Order ID({rq['tid']} /2025)", "_data-ar": f"طلب رقم ({rq['tid']} /2025) ",
              "_trans": "true", "class": "ins-col-11 ins-strong-m ins-title-s"},
              {"class":"ins-col-1 _a_red lni lni-xmark ins-view-close ins-font-xl"},
          {"start": "true", "class": "ins-col-12 ins-flex ins-card"},

          {"start": "true", "class": "ins-col-6 ins-flex "},

     {"_data": "Customer name", "_data-ar": "اسم العميل",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color "},
          {"_data": user, "class": "ins-col-12 ins-strong-l ins-grey-d-color"},


          {"_data": "Customer address", "_data-ar": "عنوان العميل",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color "},
          {"_data": address, "class": "ins-col-12 ins-strong-l ins-grey-d-color"},


     
          {"_data": "order status", "_data-ar": "حالة الطلب",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
          {"_data": status, "_data-ar": status_ar, "_trans": "true",
              "class": f"ins-col-12 ins-{self.get_status_color(data["order_status"])}-color ins-title-xs ins-strong-l"},
          {"end": "true"},

          {"start": "true", "class": "ins-col-3 ins-flex "},


          {"_data": "payment status", "_data-ar": "حالة الدفع",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
          {"_data": pstatus, "_data-ar": pstatus_ar, "_trans": "true",
              "class": f"ins-col-12 ins-{self.get_payment_status_color(data['payment_status'])}-color ins-title-xs ins-strong-l"},
          {"_data": "payment method", "_data-ar": "طريقة الدفع",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
          {"_data": payments["title"],
              "class": "ins-col-12 ins-grey-d-color ins-title-xs ins-strong-l"},
          {"end": "true"},

          {"start": "true", "class": "ins-col-3 ins-flex "},
                      
          {"data-oid":data["id"],"class":"-order-id-area"}]
          
          
          
      if data["payment_method"] == "8" and data["document"]:
           uidata.append(
              {"_data":"payment receipt","_data-ar":"إيصال الدفع","class":"ins-col-12 ins-grey-d-color"})
           uidata.append(
              {
             '_view': 'image',
             "_data":data["document"],
             "class":"ins-col-12"})



               
      uidata+=[ {"end": "true"},


          {"end": "true"},
          {"_data": "Products", "_data-ar": "المنتجات", "_trans": "true",
              "class": "ins-col-12 ins-strong-m ins-title-s"},

      ]
      for v in sedata:
          tcount += v["quantity"]
          uidata += ELUI(self.ins).counter_user_order_block(v)


      
      if data.get("shipping"):
            shipping = [
            {"start": "true", "class": "ins-col-12 ins-flex--space-between -item-card ins-card"},
            {"class": "ins-radius-m", "style": "width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex"},
            {"_data": "Shipping Fees", "_data-ar": "الكمية", "_trans": "true",
                "class": "ins-col-4 ins-title-xs ins-text-center ins-grey-color"},
            {"class": "ins-col-4"},


            {"_data": str(data["shipping"]), "_view": "currency", "_currency_symbol": " EGP",
             "_currency_symbol_ar": " جنيه", "class": "ins-col-4 ins-grey-d-color ins-text-center ins-title-xs"},
            {"end": "true"},
            {"end": "true"}
        ]
            uidata += shipping

      footer = [
          {"start": "true", "class": "ins-col-12 ins-flex--space-between -item-card ins-card "},
          {"class": "ins-radius-m", "style": "width: 97px;"},
          {"start": "true", "class": "ins-col-grow ins-flex"},
          {"_data": "count", "_data-ar": "العدد", "_trans": "true",
              "class": "ins-col-4 ins-title-xs ins-text-center ins-grey-color"},
          {"class": "ins-col-4"},

          {"_data": "total", "_data-ar": "الإجمالي", "_trans": "true",
              "class": "ins-col-4 ins-title-xs ins-text-center ins-grey-color"},

          {"_data": str(
              tcount), "class": "ins-col-4 ins-grey-d-color ins-text-center ins-title-xs"},
          {"class": "ins-col-4"},

          {"_data": str(data["total"]), "_view": "currency", "_currency_symbol": " EGP",
           "_currency_symbol_ar": " جنيه", "class": "ins-col-4 ins-grey-d-color ins-text-center ins-title-xs"},
          {"end": "true"},
          {"end": "true"},
          {"end": "true"}
          
      ]
      uidata += footer
      return self.ins._ui._render(uidata)
  



        
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")

        r = self.ins._apps._crud(properties=self.app._properties)

        return r
    
