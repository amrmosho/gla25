from ins_kit._engine._bp import App


class AppHomeSales(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    @property
    def g(self):
        return self.ins._server._get()

    def all(self):

        sql = f"SELECT       o.id AS order_id,       DATE_FORMAT(o.kit_created , '%Y/%m/%d') AS order_date,      u.first_name , u.last_name ,      u.email AS customer_email,      o.total AS total_sales,      COUNT(oi.id) AS items_sold,      o.order_status  FROM       gla_order o  JOIN       gla_order_item oi ON o.id = oi.fk_order_id  JOIN       kit_user u ON o.fk_user_id = u.id  WHERE       o.kit_created BETWEEN '{self.g['f']}' AND '{self.g['t']}'      AND o.kit_deleted = 0      AND o.kit_disabled = 0  GROUP BY       o.id, o.kit_created, u.first_name, u.last_name, u.email, o.order_status  ORDER BY       o.kit_created DESC;"

        data = self.ins._db._get_query(sql)

        header = []
        body = []

        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "order date"})
        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "items sold"})
        header.append(
            {"class": "", "style": f"    min-width: 200px;", "_data": "customer name"})
        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "total sales"})

        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "actions"})

        for f in data:
            r = []
            r.append({"class": " ins-strong ",
                     "style": f"min-width: 200px;", "_data": str(f["order_date"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": str(f["items_sold"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": str(f["first_name"]) + " "+f["last_name"]})
            r.append({"class": "ins-title-s ins-strong ins-info-color",
                     "style": f"min-width: 200px;", "_data": str(f["total_sales"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": "<i class='ins-icons-search ins-button-icon'></i><i class='ins-button-icon ins-icons-share-1'></i>"})
            body.append(r)

        uidata = [
            {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},



            {"start": "true", "class": "ins-col-12 ins-card i ins-padding-m  ins-flex-center"},

            {"_data": f"Order Report in   {self.g['f']} AND {self.g['t']} ",
                "class": "ins-col-grow  ins-title-m"},
            {
                "class": "ins-icons-printer ins-button-text"}, {
                "class": "ins-icons-download ins-button-text"},
            {"end": "true"},

            {"_type": "table",
             "class": " ins-col-12 ins-table ins-table-regular ins-pading-xl ", "data": body, "header": header},
            {"end": "true"},
        ]

        return self.ins._ui._render(uidata)

    def month(self):

        sql = f"SELECT     DATE_FORMAT(go.kit_created, '%Y-%m') AS month,    COUNT(go.id) AS order_count,    SUM(go.total) AS total_amount  FROM       gla_order go  WHERE  go.kit_created BETWEEN '{self.g['f']}' AND '{self.g['t']}'      AND   go.kit_deleted = 0      AND go.kit_disabled = 0  GROUP BY       DATE_FORMAT(go.kit_created, '%Y-%m')  ORDER BY       month;"

        data = self.ins._db._get_query(sql)

        header = []
        body = []

        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "month"})
        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "order_count"})
        header.append(
            {"class": "", "style": f"    min-width: 200px;", "_data": "total_amount"})

        for f in data:
            r = []
            r.append({"class": " ins-strong ",
                     "style": f"min-width: 200px;", "_data": str(f["month"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": str(f["order_count"])})
            r.append({"class": "ins-title-s ins-strong ins-info-color",
                     "style": f"min-width: 200px;", "_data": str(f["total_amount"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": "<i class='ins-icons-search ins-button-icon'></i><i class='ins-button-icon ins-icons-share-1'></i>"})
            body.append(r)

        uidata = [
            {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},



            {"start": "true", "class": "ins-col-12 ins-card i ins-padding-m  ins-flex-center"},

            {"_data": f"Order Report in   {self.g['f']} AND {self.g['t']} ",
                "class": "ins-col-grow  ins-title-m"},
            {
                "class": "ins-icons-printer ins-button-text"}, {
                "class": "ins-icons-download ins-button-text"},
            {"end": "true"},

            {"_type": "table",
             "class": " ins-col-12 ins-table ins-table-regular ins-pading-xl ", "data": body, "header": header},
            {"end": "true"},
        ]

        return self.ins._ui._render(uidata)

    def week(self):

        sql = f"SELECT   EXTRACT(WEEK FROM o.kit_created) AS week, DATE_FORMAT(o.kit_created , '%Y/%m/%d') AS order_date,  COUNT(o.id) AS order_count,    SUM(o.total) AS total_amount FROM     gla_order o WHERE    o.kit_created BETWEEN '{self.g['f']}' AND '{self.g['t']}' and o.kit_deleted = 0    AND o.kit_disabled = 0 GROUP BY    EXTRACT(WEEK FROM o.kit_created) ORDER BY     week DESC,    week DESC;"

        data = self.ins._db._get_query(sql)

        header = []
        body = []

        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "date"})
        header.append(
            {"class": "", "style": f"   min-width: 200px;", "_data": "order_count"})
        header.append(
            {"class": "", "style": f"    min-width: 200px;", "_data": "total_amount"})

        for f in data:
            r = []
            r.append({"class": " ins-strong ",
                     "style": f"min-width: 200px;", "_data": str(f["order_date"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": str(f["order_count"])})
            r.append({"class": "ins-title-s ins-strong ins-info-color",
                     "style": f"min-width: 200px;", "_data": str(f["total_amount"])})
            r.append({"class": "", "style": f"min-width: 200px;",
                     "_data": "<i class='ins-icons-search ins-button-icon'></i><i class='ins-button-icon ins-icons-share-1'></i>"})
            body.append(r)

        uidata = [
            {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},



            {"start": "true", "class": "ins-col-12 ins-card i ins-padding-m  ins-flex-center"},

            {"_data": f"Order Report in   {self.g['f']} AND {self.g['t']} ",
                "class": "ins-col-grow  ins-title-m"},
            {
                "class": "ins-icons-printer ins-button-text"}, {
                "class": "ins-icons-download ins-button-text"},
            {"end": "true"},

            {"_type": "table",
             "class": " ins-col-12 ins-table ins-table-regular ins-pading-xl ", "data": body, "header": header},
            {"end": "true"},
        ]

        return self.ins._ui._render(uidata)
    def noti(self):
        uidata= [
            {"start": "true", "class": "ins-flex ins-message ins-white ins-col-12"},
            {"class": "ins-icons-x  ins-flex-center ins-danger ins-rounded ins-border"},
            {"_data": "No data To show",
                "class": "ins-col-grow"},
            {"end": "true"},
        ]
        return self.ins._ui._render(uidata)

    def ui(self):


        burl = self.ins._server._url(remove=["mode"])
        uidata = [
            {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},
            {"_data": "<i style='  --color: var(--secondary);' class='ins-icons-bar-chart-dollar ins-padding-m'></i>Sales Report",
             "class": "ins-col-grow ins-strong  ins-title-m "},


            {"start": "true", "class": "ins-col-6 ins-border ins-form-input   ins-flex"},


         {"title":"Back", "_type":"a", "href":burl,"_data": "<i style='  --color: var(--secondary);font-size:25px;position: relative;top: 4px;' class='ins-icons-arrow-left  -sales-update-btn ins-padding-m'></i>",
             "class": "ins-button-text"},

            {"_type": "input", "type": "date", "value": self.g.get("f", ""),
                "placeholder": "From", "pclass": "ins-col-grow ", "class": "ins-input-none -sales-inpt-from"},
            {"_type": "input", "type": "date", "value": self.g.get("t", ""),
                "placeholder": "To", "pclass": "ins-col-grow ", "class": "ins-input-none -sales-inpt-to"},




            {"_type": "select", "value": self.g.get("a", ""), "type": "date", "fl_data": {"all": "all", "week": "week", "month": "month"},
                "placeholder": "To", "pclass": "ins-col-grow ", "class": "ins-input-none -sales-inpt-action"},


            {"_data": "<i style='  --color: var(--secondary);font-size:25px;position: relative;top: 4px;' class='ins-icons-search  -sales-update-btn ins-padding-m'></i>",
             "class": "ins-button-text"},


            {"end": "true"},
            {"_data": "<i style='  --color: var(--secondary);font-size:35px' class='ins-icons-ai ins-padding-m'></i>",
             "class": "ins-button-text -home-ai-btn"},
            {"end": "true"},
        ]

        self.ins._tmp._set_page_des(self.ins._ui._render(uidata))


        if  "f" in  self.g and "t" in self.g:
            if self.g.get("a") == "week":
                return self.week()

            elif self.g.get("a") == "month":
                return self.month()
            else:
                return self.all()
        else:
           return  self.noti()
        
        

    def out(self):
        return self.ui()
