import json
from ins_cg.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_cg.ins_kit._elui import ELUI


class AppUsersOrders(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user = Gusers(app.ins)

    def u(self, mode):
        return self.ins._server._url({"mode": mode},)

    def get_order_status(self,status,type="5"):
        data = self.ins._data._get_options(type)["content"]
        ops = json.loads(data)
        sdata = ops[str(status)]
        return sdata



    def order(self):
        g = self.ins._server._get()
        udata = self.user._check()

        sql = f"(((payment.paymob_id IS NULL OR payment.paymob_id = '') AND payment_status <> 'failed') OR ((payment.paymob_id IS NOT NULL AND payment.paymob_id <> '') AND payment_status <> 'failed' AND payment_status <> 'pending')) and gla_order.id = {g['id']}    order by id desc "
        
        odata = self.ins._db._jget("gla_order", "*", sql)
        odata._jwith("gla_payment_methods payment", "paymob_id",rfk="payment_method")
        odata = odata._jrun()

        if odata:
            data = odata[0]
        else:
            data = odata


        uidata = []

                


        if not data or str(udata["id"]) != str(data["fk_user_id"]) :
            uidata +=[{"start":"true","class":"ins-col-12 ins-flex ins-padding-m ins-flex-center"},
                      {"_data":"There is no data to show","_data-ar":"لا يوجد بيانات لعرضها","_trans":"true","class":"ins-col-8 ins-text-center ins-card"},
                      {"end":"true"}]
            
            return self.ins._ui._render(uidata)
             
 
        sedata = self.ins._db._jget("gla_order_item", "*", f"fk_order_id='{g['id']}'")
        sedata._jwith("gla_product product", "th_main,types_data,fk_product_category_id",rfk="fk_product_id", join="left join")
        sedata = sedata._jrun()
        address = ""
        if data["delivery_type"] == "delivery":
            user_address = self.ins._db._get_row("gla_user_address", "*", f"id='{data['fk_address_id']}'", update_lang=True)
            address = f"{user_address['address']}, {user_address['city']}"
        else:
            store_address = self.ins._db._get_row("gla_address", "address,kit_lang", f"id='{data['fk_address_id']}'", update_lang=True)
            address = f"{store_address['address']}"

        payments = self.ins._db._get_row("gla_payment_methods", "title,kit_lang", f"id='{data['payment_method']}'", update_lang=True)

        tcount = 0

        

        status = self.get_order_status(data["order_status"])
        pstatus = self.get_order_status(data["payment_status"],"6")
     
        uidata = [
            {"_data": "order details", "_data-ar": "تفاصيل الطلب",
                "_trans": "true", "class": "ins-col-12 ins-strong-m ins-title-m"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-card"},
            {"_data": f"Order ID({g['id']} /2025)","_data-ar": f"طلب رقم ({g['id']} /2025) ",
              "_trans": "true", "class": "ins-col-12"},

            {"start": "true", "class": "ins-col-4 ins-flex "},


            {"_data": "User address", "_data-ar": "عنوان المستخدم","_trans": "true", "class": "ins-col-12 ins-m-col-4 ins-grey-d-color"},
            {"_data": address, "class": "ins-col-12 ins-m-col-8 "},
            {"_data": "Order status", "_data-ar": "حالة الطلب","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-m-col-4 "},
            {"_data": status["text"], "_data-ar": status["text_ar"], "_trans": "true","class": f"ins-col-12 {status['class']}-color ins-title-xs ins-strong-l ins-m-col-8 "},
            {"end": "true"},

            {"start": "true", "class": "ins-col-4 ins-flex "},


            {"_data": "Payment status", "_data-ar": "حالة الدفع", "_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-m-col-4 "},
            {"_data": pstatus["text"], "_data-ar": pstatus["text_ar"], "_trans": "true","class": f"ins-col-12 {pstatus['class']}-color ins-title-xs ins-strong-l ins-m-col-8 "},
            {"_data": "Payment method", "_data-ar": "طريقة الدفع","_trans": "true", "class": "ins-col-12 ins-grey-d-color ins-m-col-4 "},
            {"_data": payments["title"],"class": "ins-col-12 ins-grey-d-color ins-title-xs ins-strong-l ins-m-col-8 "},
            {"end": "true"},

            {"start": "true", "class": "ins-col-4 ins-flex "},
                        
            {"data-oid":data["id"],"class":"-order-id-area"}]
            
            
        if data["payment_method"] == "8":
            if data["document"]:
             uidata.append( {
               '_type': 'input',"nojs":"true", 'type': 'upload', 'title': 'Payment Receipt','title-ar': ' ايصال الدفع', "_trans":"true",'name': '_unname',"class":"-upload-image",
               'placeholder': '_add placeholder hear',
               'pclass': 'ins-col-12 ',
               "value":data["document"],
               'required': 'true'})
            else:
             uidata.append( {
               '_type': 'input',"nojs":"true", 'type': 'upload', 'title': 'Payment Receipt','title-ar': ' ايصال الدفع', "_trans":"true",'name': '_unname',"class":"-upload-image",
               'placeholder': '_add placeholder hear',
               'pclass': 'ins-col-12 ',
               'required': 'true'})




                 
        uidata+=[ {"end": "true"},


            {"end": "true"},
            {"_data": "Products", "_data-ar": "المنتجات", "_trans": "true",
                "class": "ins-col-12 ins-strong-m ins-title-m"},

        ]

        try:
            for v in sedata:
                tcount += v["quantity"]
                uidata += ELUI(self.ins).counter_user_order_block(v)

        except Exception as err:
            return  str(err)

        except SyntaxError as err:
            return  str(err)

        if data.get("shipping"):
            shipping = [
            {"start": "true", "class": "ins-col-12 ins-flex-space-between -item-card ins-card"},
            {"class": "ins-radius-m lni lni-truck-delivery-1 ins-font-3xl ins-text-center ins-m-col-2", "style": "width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex  ins-m-col-10"},
          
         
            {"start": "true", "class": "ins-col-grow ins-flex"},
            {"_data": "Shipping Fees", "_data-ar": "مصاريف الشحن", "_trans": "true","class": "ins-col-3 ins-m-col-4 ins-title-xs ins-text-center ins-grey-color"},
            {"class": "ins-col-6 not-for-phone"},
            {"_data": str(data["shipping"]), "_view": "currency", "_currency_symbol": " EGP",
             "_currency_symbol_ar": " جنيه", "class": "ins-col-3 ins-m-col-8 ins-grey-d-color ins-text-center ins-title-xs"},
            {"end": "true"},
           
           
           
            {"end": "true"},

            {"end": "true"}
        ]
            uidata += shipping

                 

        footer = [
            {"start": "true", "class": "ins-col-12 ins-flex-space-between -item-card ins-card not-for-phone"},
            {"class": "ins-radius-m", "style": "width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex"},
            {"_data": "Total QTY", "_data-ar": "الكمية", "_trans": "true","class": "ins-col-3 ins-title-xs ins-text-center ins-grey-color"},
            {"class": "ins-col-6"},

            {"_data": "total", "_data-ar": "الإجمالي", "_trans": "true","class": "ins-col-3 ins-title-xs ins-text-center ins-grey-color"},

            {"_data": str(tcount), "class": "ins-col-3  ins-grey-d-color ins-text-center ins-title-xs"},
            {"class": "ins-col-6"},

            {"_data": str(data["total"]), "_view": "currency", "_currency_symbol": " EGP","_currency_symbol_ar": " جنيه", "class": "ins-col-3  ins-grey-d-color ins-text-center ins-title-xs"},
            {"end": "true"},
            {"end": "true"},



            {"start": "true", "class": "ins-col-12 ins-flex-space-between -item-card ins-card not-for-web"},
            {"class": "ins-radius-m", "style": "width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex"},
            {"_data": "Total QTY", "_data-ar": "الكمية", "_trans": "true","class": "ins-m-col-6 ins-title-xs ins-text-center ins-grey-color"},
            {"_data": str(tcount), "class": "ins-m-col-6 ins-grey-d-color ins-text-center ins-title-xs"},

            {"_data": "total", "_data-ar": "الإجمالي", "_trans": "true","class": "ins-m-col-6 ins-title-xs ins-text-center ins-grey-color"},


            {"_data": str(data["total"]), "_view": "currency", "_currency_symbol": " EGP","_currency_symbol_ar": " جنيه", "class": "ins-m-col-6  ins-grey-d-color ins-text-center ins-title-xs"},
            {"end": "true"},
            {"end": "true"}


        ]
        uidata += footer
        return self.ins._ui._render(uidata)


    def out(self, ins):
        udata = self.user._check()
        sql = f"(((payment.paymob_id IS NULL OR payment.paymob_id = '') AND payment_status <> 'failed') OR ((payment.paymob_id IS NOT NULL AND payment.paymob_id <> '') AND payment_status <> 'failed' AND payment_status <> 'pending')) and fk_user_id = {udata["id"]}    order by id desc "
        
        odata = self.ins._db._jget("gla_order", "*", sql)
        odata._jwith("gla_payment_methods payment", "paymob_id",rfk="payment_method")
        odata = odata._jrun()


        usmenu = [
            {"start": "true", "class": "  ins-col-12 ins-gap-20  ins-flex    ins-padding-2xl"}]
        i = 0
        for v in odata:
            icount = self.ins._db._get_row(
                "gla_order_item", "sum(quantity) as quantity", f"fk_order_id='{v['id']}'")["quantity"]
            status = self.get_order_status(v["order_status"])


            i += 1
            style = ""
            if i == 1:
                style = "border: 2px solid var(--gold) !important;"
            order = [{"start": "true", "class": " ins-flex-space-between  ins-card  ins-col-12 ins-border   ins-flex   ins-padding-l", "style": style},
                     {"_data": f"Order ID(#{v['id']} /2025) ","_data-ar": f"طلب رقم ({v['id']} /2025) ","_trans": "true","class": " ins-col-9  ins-m-col-7 ins-primary-d-color ins-title-s	 ins-strong-l "}
                     ]
            if i == 1:
                order += [{"_data": f'  New ', "_data-ar": "جديد", "_trans": "true",
                           "class": "ins-tag ins-gold  ins-strong-m  ins-text-upper ins-radius-m ins-m-col-1  ins-text-upper ins-text-center"}]

            arrow = "lni-arrow-right"
            if self.ins._langs._this_get()["name"] == "ar":
                arrow = "lni-arrow-left"
            order += [{"_data": status["text"], "_data-ar": status["text_ar"], "_trans": "true",
                       "class": f"{status['class']} ins-tag ins-col-2 ins-radius-m  ins-m-col-3 ins-text-upper ins-avatar-s ins-gold-d "},
                      {"class": "ins-line ins-col-12"},
                      {"start": "true", "class": "ins-flex ins-col-10"}]
                    
            if v["kit_created"]:
                order.append({"_data": f' Date  ', "_data-ar": f' التاريخ ', "_trans": "true","class": " ins-col-4   ins-m-col-4    ins-grey-color "})
            else:
                order.append({"class": " ins-col-4"})
                    
                    
            order +=[{"_data": f' Items QTY ', "_data-ar": f' العدد ',"_trans": "true", "class": " ins-col-4   ins-m-col-4    ins-grey-color"},
                    {"_data": f' Orders Total ', "_data-ar": f' اجمالي ', "_trans": "true","class": " ins-col-4   ins-m-col-4  ins-grey-color "}]
            
            if v["kit_created"]:
              order.append({"_data": f'{v["kit_created"]}', "_view": "date","class": " ins-col-4   ins-m-col-4  ins-grey-d-color ins-title-xs ins-strong-l ", "style": "    margin-top: -22px;"})
            else:
                order.append({"class": " ins-col-4"})
            order +=  [{"_data": f'{icount}',
                       "class": " ins-col-4   ins-m-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
                      {"_data": f'{v["total"]}', "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه",
                       "class": " ins-col-4   ins-m-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
                      {"end": "true"},
                      {"class": " ins-col-1  ins-m-col-1"},
                      {"_type": "a", "href": f"/user/order/{v['id']}", "class": "ins-button-cricle ins-grey-d",
                       "_data": f'<i class=" lni ins-icon ins-white-color {arrow}"></i>'},
                      {"end": "true"}]

            usmenu += order

        usmenu.append({"end": "true"})

        uidata = [
            {"start": "true", "class": "ins-col-12  "},
            {"start": "true", "class": "gla-container ins-flex-start "},
        ]

        g = ins._server._get()

        if "id" in g:

            uidata .append(
                {"start": "true", "class": "  ins-flex-start  ins-padding-2xl  ins-col-12"})
            uidata .append(
                {"class": "  ins-flex-start  ins-gap-20   ins-col-12", "_data": self.order()})
            uidata .append({"end": "true"})

        else:

            uidata .append({"start": "true", "class": "ins-flex ins-col-12 "})
            uidata += usmenu
            uidata .append({"end": "true"})

        if not odata:
            uidata .append(
                {"start": "true", "class": "ins-flex-center ins-col-12 "})
            uidata += [{"_data": "There is no orders yet", "_data-ar": "لا يوجد طلبات قديمة",
                        "_trans": "true", "class": "ins-col-8 ins-flex-center ins-card"}]
            uidata .append({"end": "true"})

        uidata .append({"end": "true"})
        return self.ins._ui._render(uidata)
