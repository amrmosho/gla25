from datetime import datetime
import json
from ins_gla.ins_kit._elui import ELUI
from ins_kit._engine._bp import App


class AppOrder(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def get_order_status(self,status,type="5"):
        data = self.ins._data._get_options(type)["content"]
        ops = json.loads(data)
        return ops[status]




    def _status(ins, options, data):
     content = ins._data._get_options("5")["content"]
     ops = json.loads(content)
     status = ops[str(data["order_status"])]
     uiadta = [{"_data": status["text"], "_data-ar": status["text_ar"],"_trans":"true", "class" : f" {status['class']} ins-col-8 ins-text-center ins-title-14 ins-strong-m  ins-tag",}]
     return ins._ui._render(uiadta)

    def _payment_status(ins, options, data):
     content = ins._data._get_options("6")["content"]
     ops = json.loads(content)
     status = ops[str(data["payment_status"])]


     uiadta = [{"_data": status["text"], "_data-ar": status["text_ar"],"_trans":"true", "class" : f"{status['class']} ins-col-8 ins-text-center ins-title-14 ins-strong-m  ins-tag",}]
     return ins._ui._render(uiadta)
    
    def _total(ins, options, data):

     uiadta = [{"_data": str(data["total"]), "_view": "currency", "_currency_symbol": " EGP",
             "_currency_symbol_ar": " جنيه", "class" : " ins-primary-d ins-strong-l ins-flex-center ins-card ins-flex-space-between ins-col-9 ins-flex ins-padding-l ins-padding-h ins-text-center",}]
     return ins._ui._render(uiadta)
    def _deatils(ins, options, data):
     ptitle = ins._db._get_row("gla_payment_methods","title,kit_lang",f"id='{data['payment_method']}'",update_lang=True)

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
      data = self.ins._db._get_row("gla_order", "order_status,payment_status", f"id='{rq['tid']}'")
      o_status =  self.ins._data._get_options("5")["content"]
      o_status = json.loads(o_status)
      order_status = {}
      for ko,vo in o_status.items():
         order_status[ko] = vo["text"]

      if self.ins._langs._this_get()["name"] == "ar":
       for ko,vo in o_status.items():
         order_status[ko] = vo["text_ar"]


      p_status =  self.ins._data._get_options("6")["content"]
      p_status = json.loads(p_status)
      payment_status = {}
      for kp,vp in p_status.items():
         payment_status[kp] = vp["text"]

      if self.ins._langs._this_get()["name"] == "ar":
       for kp,vp in p_status.items():
         payment_status[kp] = vp["text_ar"]
     



      
      uidata = [
         {"start":"true","class":"ins-col-12 ins-flex "},
        {"_data":"Change Order Status","_data-ar":"تغيير حالة الطلب","_trans":"true","class":"ins-col-11 ins-strong-m ins-title-s "},
        {"class":"ins-col-1 ins-text-right lni lni-xmark _a_red ins-view-close  ins-font-xl"},
        {"start":"true","class":"ins-col-12 ins-padding-m ins-flex-center"},
        {"_type":"select","value":data["order_status"],"title":"Order Status","title-ar":"حالة الطلب","_trans":"true","fl_data":order_status,"pclass":"ins-col-12","name":"status"},
        {"_type":"select","value":data["payment_status"],"title":"Payment Status","title-ar":"حالة الدفع","_trans":"true","fl_data":payment_status,"pclass":"ins-col-12","name":"payment_status"},
        {"class":"ins-button ins-primary -save-status","_data":"Update Status","_data-ar":"تحديث","_trans":"true","data-tid":rq["tid"]},

        {"end":"true"},
        {"end":"true"}

        
        ]
      return self.ins._ui._render(uidata)


    
    def _update_statue(self):   
      rq = self.ins._server._post()
      update_data = {"order_status": rq["value"],"payment_status":rq["payment"]} 
      self.ins._db._update("gla_order", update_data, f"id='{rq['oid']}'")
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
      sedata = self.ins._db._jget("gla_order_item", "*", f"fk_order_id='{rq['tid']}'")
      sedata._jwith("gla_product product", "th_main,types_data,fk_product_category_id",rfk="fk_product_id", join="left join")
      sedata = sedata._jrun()
      data = self.ins._db._get_row("gla_order", "*", f"id='{rq['tid']}'")
      user = self.ins._db._get_row("kit_user", "title", f"id='{data['fk_user_id']}'")["title"]


      address = ""
      if data["delivery_type"] == "delivery":
          user_address = self.ins._db._get_row("gla_user_address", "*", f"id='{data['fk_address_id']}'", update_lang=True)
          address = f"{user_address['address']}, {user_address['city']}"
      else:
          store_address = self.ins._db._get_row("gla_address", "address,kit_lang", f"id='{data['fk_address_id']}'", update_lang=True)
          address = f"{store_address['address']}"

      payments = self.ins._db._get_row("gla_payment_methods", "title,kit_lang", f"id='{data['payment_method']}'", update_lang=True)
      uidata = []
      tcount = 0
      
      order_status = self.get_order_status(data["order_status"])
      payment_status = self.get_order_status(data["payment_status"],"6")


      uidata = [
         {"start":"true","class":"ins-col-12 ins-flex "}, 
{"_type": "input", "type": "upload", "title": "Upload image", "name": "_unname", "placeholder": "_add placeholder hear", "pclass": "ins-col-12 ", "required": "true", "_dir": "test", "_exts": "image/png"},
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
          {"_data": order_status["text"], "_data-ar": order_status["text_ar"], "_trans": "true","class": f"ins-col-12 {order_status['class']}-color ins-title-xs ins-strong-l"},
          {"end": "true"},

          {"start": "true", "class": "ins-col-3 ins-flex "},


          {"_data": "payment status", "_data-ar": "حالة الدفع",
              "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
          {"_data": payment_status["text"], "_data-ar": payment_status["text_ar"], "_trans": "true","class": f"ins-col-12 {payment_status['class']}-color ins-title-xs ins-strong-l"},
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
  




    def export(self, data):
        exdata = []
        for d in data:
            try:
                customer_row = self.ins._db._get_row("kit_user", "title", f"id='{d['fk_user_id']}'")
                customer = customer_row["title"] if customer_row else "Unknown"
                dt = datetime.strptime(str(d["kit_created"]), "%Y-%m-%d %H:%M:%S")


                if d["delivery_type"] == "store":
                    addr_row = self.ins._db._get_row("gla_address", "address", f"id='{d['fk_address_id']}'")
                else:
                    addr_row = self.ins._db._get_row("gla_user_address", "address", f"id='{d['fk_address_id']}'")
                address = f'"{addr_row["address"] if addr_row else "Unknown"}"'

                pay_row = self.ins._db._get_row("gla_payment_methods", "title", f"id='{d['payment_method']}'")
                pmethod = pay_row["title"] if pay_row else "Unknown"

                odata = self.ins._db._jget("gla_order_item", "*", f"fk_order_id='{d['id']}'")
                odata._jwith("gla_product product", "weight,kart", rfk="fk_product_id", join="left join")
                odata = odata._jrun()

                coins_amount = 0
                bars_amount = 0
                for o in odata:
                    try:
                        qty = float(o.get("quantity") or 0)
                        weight = float(o.get("product_weight") or 0)
                        if o.get("product_kart") == "24":
                            bars_amount += qty * weight
                        elif o.get("product_kart") == "21":
                            coins_amount += qty * weight
                    except Exception as oe:
                        print(f"[Item Error] Order ID {d['id']} → {oe}")

                exdata.append({
                    "ID": d["id"],
                    "Order Date":dt.date()    ,
                    "Order Time":dt.time() ,
                    "Customer": customer,
                    "Delivery Type": d["delivery_type"],
                    "Address": address,
                    "Payment Method": pmethod,
                    "Order Status": d["order_status"],
                    "Payment Status": d["payment_status"],
                    "Total amount": d["total"],
                    "Total 24K amount": int(bars_amount),
                    "Total 21K amount": int(coins_amount)
                })

            except Exception as e:
                print(f"[Order Error] Order ID {d.get('id')} → {e}")

        return exdata

    def export_products(self, data):
        exdata = []
        all_products = self.ins._db._get_data("gla_product", "id, title")
        product_titles = [p["title"] for p in all_products]
        for d in data:
            odata = self.ins._db._jget("gla_order_item", "*", f"fk_order_id='{d['id']}'")
            odata._jwith("gla_product product", "title", rfk="fk_product_id")
            odata = odata._jrun()
            item_map = {o["product_title"]: o["quantity"] for o in odata}

            row = {"ID": d["id"],
                    "Order Date": self.ins._date._format(d["kit_created"], format="date"),
                    "Order Time": self.ins._date._format(d["kit_created"], format="time")

                   }
            for title in product_titles:
                row[title] = item_map.get(title, 0)
            
            exdata.append(row)

        return exdata

       
       

        
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")

        g= self.ins._server._get()

        ops = self.ins._apps._crud_ops
        if "type" in g and g["type"] == "products":
         ops._list_export = self.export_products
         ops._list_export_all = self.export_products
        else:
         ops._list_export = self.export
         ops._list_export_all = self.export

        r = self.ins._apps._crud(ops, properties=self.app._properties)

        return r
    
