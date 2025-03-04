from ins_gla.ins_kit._gusers import Gusers
from ins_kit._engine._bp import App
from ins_gla.ins_kit._elui import ELUI


class AppUsersOrders(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
        self.user = Gusers(app.ins)

    def u(self, mode):
        return self.ins._server._url({"mode": mode},)




    def order(self):
        g = self.ins._server._get()
        sedata = self.ins._db._jget(
            "gla_order_item", "*", f"fk_order_id='{g['id']}'")
        sedata._jwith("gla_product product", "th_main",
                      rfk="fk_product_id", join="left join")
        sedata = sedata._jrun()
        data = self.ins._db._get_row("gla_order", "*", f"id='{g['id']}'")
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
            {"_data": "order details", "_data-ar": "تفاصيل الطلب",
                "_trans": "true", "class": "ins-col-12 ins-strong-m ins-title-m"},
            {"start": "true", "class": "ins-col-12 ins-flex ins-card"},
            {"_data": f"Order ID({g['id']} /2025)", "class": "ins-col-12"},

            {"start": "true", "class": "ins-col-4 ins-flex "},


            {"_data": "user address", "_data-ar": "عنوان المستخدم",
                "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
            {"_data": address, "class": "ins-col-12"},
            {"_data": "order status", "_data-ar": "حالة الطلب",
                "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
            {"_data": status, "_data-ar": status_ar, "_trans": "true",
                "class": f"ins-col-12 ins-{self.get_status_color(data["order_status"])}-color ins-title-xs ins-strong-l"},
            {"end": "true"},

            {"start": "true", "class": "ins-col-4 ins-flex "},


            {"_data": "payment status", "_data-ar": "حالة الدفع",
                "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
            {"_data": pstatus, "_data-ar": pstatus_ar, "_trans": "true",
                "class": f"ins-col-12 ins-{self.get_payment_status_color(data['payment_status'])}-color ins-title-xs ins-strong-l"},
            {"_data": "payment method", "_data-ar": "طريقة الدفع",
                "_trans": "true", "class": "ins-col-12 ins-grey-d-color"},
            {"_data": payments["title"],
                "class": "ins-col-12 ins-grey-d-color ins-title-xs ins-strong-l"},
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
            {"start": "true", "class": "ins-col-12 ins-flex--space-between -item-card ins-card"},
            {"class": "ins-radius-m", "style": "width: 97px;"},
            {"start": "true", "class": "ins-col-grow ins-flex"},
            {"_data": "count", "_data-ar": "الكمية", "_trans": "true",
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
            {"end": "true"}
        ]
        uidata += footer
        return self.ins._ui._render(uidata)

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

    def out(self, ins):
        udata = self.user._check()
        odata = self.ins._db._get_data(
            "gla_order", "*", f"fk_user_id='{udata["id"]}'")
        usmenu = [
            {"start": "true", "class": "  ins-col-12 ins-gap-20  ins-flex    ins-padding-2xl"}]
        i = 0
        odata.reverse()
        for v in odata:
            icount = self.ins._db._get_row(
                "gla_order_item", "sum(quantity) as quantity", f"fk_order_id='{v["id"]}'")["quantity"]
            if (v["order_status"] == "pending"):
                status = "Pending"
                status_ar = "قيد الانتظار "
                status_class = "ins-warning"
            elif (v["order_status"] == "confirmed"):
                status_class = "ins-secondary"
                status = "Confirmed"
                status_ar = "مقبول"

            elif (v["order_status"] == "canceled"):
                status = "Canceled"
                status_ar = "ملغي"

                status_class = "ins-danger"
            elif (v["order_status"] == "delivered"):
                status_class = "ins-success"
                status = "Delivered"
                status_ar = "تم التوصيل"
            i += 1
            style = ""
            if i == 1:
                style = "border: 2px solid var(--gold) !important;"
            order = [{"start": "true", "class": " ins-flex-space-between  ins-card  ins-col-12 ins-border   ins-flex   ins-padding-l", "style": style},
                     {"_data": f'  Order  ID({v["id"]} /2025) ',
                      "class": " ins-col-9 ins-primary-d-color ins-title-s	 ins-strong-l "}
                     ]
            if i == 1:
                order += [{"_data": f'  New ', "_data-ar": "جديد", "_trans": "true",
                           "class": "ins-tag ins-gold  ins-strong-m  ins-text-upper ins-radius-m  ins-text-upper ins-text-center"}]

            arrow = "lni-arrow-right"
            if self.ins._langs._this_get()["name"] == "ar":
                arrow = "lni-arrow-left"
            order += [{"_data": status, "_data-ar": status_ar, "_trans": "true",
                       "class": f"{status_class} ins-col-2 ins-radius-m  ins-text-upper ins-avatar-s ins-gold-d "},
                      {"class": "ins-line ins-col-12"},
                      {"start": "true", "class": "ins-flex ins-col-10"},
                      {"_data": f' Date  ', "_data-ar": f' التاريخ ', "_trans": "true",
                       "class": " ins-col-4    ins-grey-color "},
                      {"_data": f' Items Count ', "_data-ar": f' العدد ',
                          "_trans": "true", "class": " ins-col-4    ins-grey-color"},
                      {"_data": f' Orders Total ', "_data-ar": f' اجمالي ', "_trans": "true",
                       "class": " ins-col-4 ins-grey-color "},
                      {"_data": f'{v["kit_created"]}', "_view": "date",
                       "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l ", "style": "    margin-top: -22px;"},
                      {"_data": f'{icount}',
                       "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
                      {"_data": f'{v["total"]}', "_view": "currency", "_currency_symbol": " EGP", "_currency_symbol_ar": " جنيه",
                       "class": " ins-col-4  ins-grey-d-color ins-title-xs ins-strong-l", "style": "    margin-top: -22px;"},
                      {"end": "true"},
                      {"class": " ins-col-1"},
                      {"_type": "a", "href": f"/puser/order/{v["id"]}", "class": "ins-button-cricle ins-grey-d",
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
