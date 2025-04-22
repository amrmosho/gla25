import datetime
from ins_gla.ins_apps.app_home.app_home_sales import AppHomeSales
from ins_kit._engine._bp import App


class AppHome(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def ai_call(self):
        rq = self.ins._server._post()
        response_data = self.ins._ai.generate_sql(
            rq["v"], ["gla_product", "gla_order", "gla_order_item", 'kit_user'])
        if type(response_data) == list:
            header = []
            body = []
            e = [
                ['Task', 'Hours per Day'],
                ['Work', 11],
                ['Eat', 2],
                ['Commute', 2],
                ['Watch TV', 2],
                ['Sleep', 7]
            ]
            d = []
            rw = []
            for k, v in response_data[0].items():
                header.append({"_data": str(k), "class": "ins-col-grow"})
                rw.append(str(k))
            d.append(rw)
            for a in response_data:
                row = []
                rw = []
                for k, v in a.items():
                    row.append({"_data": str(v), "class": "ins-col-grow"})
                    if not self.ins._data._is_number(v):
                        v = str(v)
                    rw.append(v)
                body.append(row)
                d.append(rw)
            r = []
            r += [{"start": "true", "class": "ins-flex ins-col-12"},
                  {"start": "true", "class": "ins-flex ins-card  ins-col-12"}, {"_data": rq["v"], "class": "ins-flex ins-col-grow"}, {
                      "_data": '<i class="ins-icons-download"></i>', "style": "width:50px"}, {"_data": '<i class="ins-icons-printer"></i>', "style": "width:50px"},
                  {"end": "true"}
                  ]
            if len(a) > 1:
                r += [
                    {"_type": "chart", "type": "ddd", "data": d, "style": "height:400px",
                     "class": "ins-col-8  ins-flex  ins-padding-xl"},
                    {"_type": "chart", "type": "pie", "data": d, "style": "height:400px",
                     "class": "ins-col-4  ins-flex  ins-padding-xl"}
                ]
            r += [
                {"_type": "table", "data": body, "header": header,
                 "class": " ins-col-12 ins-table ins-table-regular   ins-pading-xl "},
            ]
            r += [{"end": "true"}]
            return self.ins._ui._render(r)
        else:
            return response_data

    def ai(self):
        ui = [
            {"start": "true", "class": " ins-col-12 ins-filter-body ",
                "style": "background: var(--ins-color-4);border-radius: 5px;margin-top: 10px;"},
            {"start": "true", "class": "ins-flex-center ins-padding-l ins-col-12"},
            {"class": "ins-flex ins-col-12 -home-ai-body",
                "style": '    height: calc(100vh - 260px);  overflow: auto;'},
            {"start": "true", "class": "ins-flex-end  ins-bg ins-border ins-radius-xl ins-col-12"},
            {"_type": "input", "type": "textarea", "style": "height:100px",
                "pclass": "ins-col-12", "placeholder": "Message Insya", "class": "ins-input-none  -home-ai-txt"},
            {"class": "ins-col-1 lni lni-upload-circle-1 -home-ai-send-btn ins-button-icon  ins-primary"},
            {"class": "ap-ai-data ins-col-12 ins-bg-2"},
            {"end": "true"}
        ]
        return self.ins._ui._render(ui)

    def new_user(self):
        sql = "SELECT COUNT(*) AS new_users_count from  kit_user WHERE  MONTH(kit_created)=MONTH(now() )   ;"
        data = self.ins._db._get_query(sql)[0]
        lsql = "SELECT COUNT(*) AS new_users_count from  kit_user WHERE  MONTH(kit_created)=(MONTH(now() ) - 1 ) ;"
        lsqldata = self.ins._db._get_query(lsql)[0]
        per  = 0
        if data["new_users_count"] and lsqldata["new_users_count"]:
         per = round((data["new_users_count"] /lsqldata["new_users_count"]) * 100)
        
        uidata = [
            {
                "start": "true",
                "class": "ins-flex in-col-12 "
            },
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-users sub-title-icon'></i> New Customres"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["new_users_count"])
            },
            {
                "class": "ins-text-center ins-padding-m  ins-radius-m ins-danger ",  "_data":  f"{str(per)}%"
            }, {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def new_price(self, t):
        sql = "SELECT COUNT(*) AS new_users_count from  gla_order WHERE  MONTH(kit_created)=MONTH(now() )   ;"
        data = self.ins._db._get_query(sql)[0]
        lsql = "SELECT COUNT(*) AS new_users_count from  gla_order WHERE  MONTH(kit_created)=(MONTH(now() ) - 1 ) ;"
        lsqldata = self.ins._db._get_query(lsql)[0]
        per = round((data["new_users_count"] /
                    lsqldata["new_users_count"]) * 100)
        uidata = [
            {
                "start": "true",
                "class": "ins-flex in-col-12 "
            },
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-cash sub-title-icon'></i> Total Sales"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(t)
            },
            {
                "class": "ins-text-center ins-padding-m  ins-radius-m ins-danger ",  "_data":  f"{str(per)}%"
            }, {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def new_order(self):
        sql = "SELECT COUNT(*) AS new_users_count from  gla_order WHERE  MONTH(kit_created)=MONTH(now() )   ;"
        data = self.ins._db._get_query(sql)[0]
        lsql = "SELECT COUNT(*) AS new_users_count from  gla_order WHERE  MONTH(kit_created)=(MONTH(now() ) - 1 ) ;"
        lsqldata = self.ins._db._get_query(lsql)[0]
        per = round((data["new_users_count"] /
                    lsqldata["new_users_count"]) * 100)
        uidata = [
            {
                "start": "true",
                "class": "ins-flex in-col-12 "
            },
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-file-multiple sub-title-icon'></i> New Orders"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["new_users_count"])
            },
            {
                "class": "ins-text-center ins-padding-m  ins-radius-m ins-danger ",  "_data":  f"{str(per)}%"
            }, {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def month(self):
        sql = "SELECT   DATE_FORMAT(gla_order.kit_created, '%m-%d') AS order_date,    COUNT(gla_order.id) AS total_orders,      SUM(gla_order.total) AS total_spent  FROM       gla_order  WHERE  MONTH(gla_order.kit_created) = MONTH(CURRENT_DATE)  and     gla_order.kit_deleted = 0      AND gla_order.kit_disabled = 0  GROUP BY       DATE(gla_order.kit_created)  ORDER BY       order_date;"
        data = self.ins._db._get_query(sql)
        e = [
            ['Date', 'Total Spent', {"role": 'annotation'}],
        ]
        to = 0
        for d in data:
            e.append([str(d["order_date"]), float(d["total_spent"]),
                     f"{str(d["total_orders"])} Order"])
        
            to += float(d["total_spent"])
        ops = {'legend': {'position': 'none'}, 'colors': ["#02285B"]}
        
        
        
        uidata = [
            {"_data": '<i class="ins-icons-credit-card-multiple"></i>' " Sales",
             "class": "ins-col-12 ins-title-l ins-padding-xl  ins-flex  "},
           
           
           
           
            {"_type": "chart", "type": "line", "data":  e, "options": ops, "style": "width:100%",
                "class": "ins-col-12  ins-flex  "},
            
            
            
            {"class": "ins-padding-l    ins-col-12"},
            {"class": "ins-flex ins-info ins-card  ins-col-3",
             "_data": self.new_user()},
            {"class": "ins-flex ins-info ins-card  ins-col-3",
             "_data": self.new_products()},
            {"class": "ins-flex ins-info ins-card  ins-col-3",
                "_data": self.new_order()},
            {"class": "ins-flex  ins-info  ins-card ins-col-3",
                "_data": self.new_price(to)}
        ]
        return self.ins._ui._render(uidata)

    def line(self):
        sql = "SELECT     DATE_FORMAT(go.kit_created, '%Y-%m') AS month,    COUNT(go.id) AS order_count,    SUM(go.total) AS total_amount  FROM       gla_order go  WHERE       go.kit_deleted = 0      AND go.kit_disabled = 0  GROUP BY       DATE_FORMAT(go.kit_created, '%Y-%m')  ORDER BY       month;"
        data = self.ins._db._get_query(sql)
        e = [['Month', 'Sales', {"role": 'annotation'}]]
        for d in data:
            e.append([str(d["month"]), float(d["total_amount"]),
                     f"{str(d["order_count"])} Order"])
        ops = {'legend': {'position': 'none'}}
        uidata = [
            {"_data": '<i class="ins-icons-credit-card-multiple"></i>' " Sales",
             "class": "ins-col-12 ins-title-l ins-padding-xl  ins-flex  "},
            {"_type": "chart", "type": "line", "options": ops, "data": e, "style": "width:100%",
                "class": "ins-col-12  ins-flex  "},
            {"class": "ins-padding-l    ins-col-12"},
        ]
        return self.ins._ui._render(uidata)

    def bar(self):
        sql = "SELECT       u.id AS customer_id,      u.first_name,      u.last_name,      COUNT(o.id) AS order_count  FROM       kit_user u  JOIN       gla_order o ON u.id = o.fk_user_id  WHERE       o.kit_deleted = 0      AND o.kit_disabled = 0      AND YEAR(o.kit_created) = YEAR(CURRENT_DATE)  GROUP BY       u.id, u.first_name, u.last_name  ORDER BY       order_count DESC  LIMIT 10;"
        data = self.ins._db._get_query(sql)
        e = [['Customres', 'order_count', {"role": 'annotation'}]]
        for d in data:
            e.append([d["first_name"], float(
                d["order_count"]), f"{d["first_name"]}"])
        ops = {'legend': {'position': 'none'}}
        uidata = [
            {"_data": "Top 10 Customres Order Count",  "data": e,
                "class": "ins-col-12 ins-title-m  ins-flex  "},
            {"_type": "chart", "type": "bar", "options": ops, "data": e, "style": "width:100%",
                "class": "ins-col-12 ins-flex  "},
        ]
        return self.ins._ui._render(uidata)

    def bar2(self):
        sql = "SELECT       u.id,      u.first_name,      u.last_name,      u.email,      SUM(oi.price * oi.quantity) AS total_spent  FROM       kit_user u  JOIN       gla_order o ON u.id = o.fk_user_id  JOIN       gla_order_item oi ON o.id = oi.fk_order_id  WHERE       EXTRACT(YEAR FROM o.kit_created) = EXTRACT(YEAR FROM CURRENT_DATE)      AND o.kit_deleted = 0      AND o.kit_disabled = 0  GROUP BY       u.id, u.first_name, u.last_name, u.email  ORDER BY       total_spent DESC  LIMIT 10;"
        data = self.ins._db._get_query(sql)
        e = [['Customres', 'Total Spent', {"role": 'annotation'}]]
        for d in data:
            e.append([d["first_name"], float(
                d["total_spent"]), f"{d["first_name"]}"])
        ops = {'legend': {'position': 'none'}}
        uidata = [
            {"_data": "Top 10 Customres Spent",  "data": e,
                "class": "ins-col-12 ins-title-m  ins-flex  "},
            {"_type": "chart", "type": "bar", "options": ops,  "data": e, "style": "width:100%",
                "class": "ins-col-12 ins-flex  "},
        ]
        return self.ins._ui._render(uidata)

    def pie(self):
        sql = "SELECT     p.id,    p.title,    p.price,   SUM(oi.quantity) AS total_sold FROM    gla_product p JOIN    gla_order_item oi ON p.id = oi.fk_product_id JOIN      gla_order o ON oi.fk_order_id = o.id WHERE    YEAR(o.kit_created)=YEAR(now() )   AND o.kit_deleted = 0     AND oi.kit_deleted = 0     AND p.kit_deleted = 0 GROUP BY    p.id, p.title, p.price ORDER BY    total_sold DESC LIMIT 5;"
        data = self.ins._db._get_query(sql)
        e = [['Product', 'Total Sold', {"role": 'annotation'}]]
        for d in data:
            e.append([d["title"], float(d["total_sold"]), f"{d["title"]}"])
        uidata = [
            {"_data": "Top 5 sold Proucts",  "data": e,
                "class": "ins-col-12 ins-title-m  ins-flex  "},
            {"_type": "chart", "type": "pie", "data": e, "style": "width:100%",
                "class": "ins-col-12 ins-flex  "},
        ]
        return self.ins._ui._render(uidata)

    def _year(self):
        uidata = [
            {
                "start": "true", "class": "ins-flex-center ins-border ins-card ins-col-12 "
            },
            {"class": "ins-flex   ins-col-8", "_data": self.line()},
            {"class": "ins-flex  ins-col-4", "_data": self.pie()},
            {
                "end": "true"
            },
            {"class": "ins-flex ins-card  ins-border ins-col-6", "_data": self.bar()
             }, {"class": "ins-flex ins-card ins-border  ins-col-6", "_data": self.bar2()}
        ]
        return self.ins._ui._render(uidata)

    def new_products(self):
        sql = "SELECT COUNT(*) AS new_users_count from  gla_product WHERE  MONTH(kit_created)=MONTH(now() )   ;"
        data = self.ins._db._get_query(sql)[0]
        lsql = "SELECT COUNT(*) AS new_users_count from  gla_product WHERE  MONTH(kit_created)=(MONTH(now() ) - 1 ) ;"
        lsqldata = self.ins._db._get_query(lsql)[0]
        if lsqldata["new_users_count"] == 0:
            per = 0
        else:
            per = round((data["new_users_count"] /
                        lsqldata["new_users_count"]) * 100)
        uidata = [
            {
                "start": "true",
                "class": "ins-flex in-col-12 "
            },
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-box-archive sub-title-icon'></i> New Products"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["new_users_count"])
            },
            {
                "class": "ins-text-center ins-padding-m  ins-radius-m ins-danger ",  "_data":  f"{str(per)}%"
            }, {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def _cart_count(self):
        sedata = self.ins._server._get_session("glaproducts")
        count = 0
        if sedata:
            for _, s in sedata.items():
                count += int(s["count"])
        return str(count)

    def user_data(self):
        udata = self.ins._users._session_get()
        img = '<i class="lni lni-user-4"></i>'
        uidata = [
            {
                "class": "ins-font-4xl  ins-text-center ins-card ins-rounded ins-secondary ", "style": "width:100px;height:100px;", "_data": img
            },
            {
                "class": "ins-col-12 ins-strong ins-text-center", "_data": udata["title"]
            },
            {
                "class": "ins-col-12 ins-font-s  ins-text-center", "_data": udata["email"]
            },
            {
                "start": "true",
                "_type": "ui",
                "class": "ins-flex ins-col-12 ins-padding-xl "
            },
            {
                "_type": "li",
                "class": "ins-col-12 ins-font-s", "_data": '<i class="lni ins-icon  lni-user-4"></i> Profile'
            },
            {
                "_type": "li",
                "class": "ins-danger-color   ins-font-s -tp-logout-btn ins-col-12", "_data": '<i class="lni ins-icon   lni-xmark"></i> Logout'
            },
            {"_type": "ui", "start": "end"
             }
        ]
        return self.ins._ui._render(uidata)

    def menu_data(self):
        ui = []
        m = "112"
        data = self.ins._db._get_data(
            "menu_item_table", "*", f"fk_menu_id='{m}'  and fk_menu_item_id=0 order by kit_order")
        ui.append({"class": "ins-col-12 ins-flex wdg-admin-menu", "start": True})
        for d in data:
            if self.ins._users._per_check_menu(d["id"]) and str(d["kit_hidden"]) != "1":
                subdata = self.ins._db._get_data(
                    "menu_item_table", "*", f"   fk_menu_item_id={d['id']} order by kit_order")
                row = [
                    {"_type": "ul", "class": " ins-flex-center ins-col-12 ins-card", "start": True},
                    {"_type": "li", "class": "ins-padding-xl ins-border ins-flex ins-col-12 ins-card", "start": True},
                    {"_type": "i", "class": " ins-title-xs",
                     "class": d["icon"]},
                    {"class": "ins-title-s ins-strong",
                     "_data": d["title"]},
                    {"_type": "li",  "end": True},
                ]
                for s in subdata:
                    if self.ins._users._per_check_menu(s["id"]) and str(s["kit_hidden"]) != "1":
                        url = self.ins._server._url({"alias": s["alias"]})
                        subrow = [
                            {"_type": "li", "class": "ins-col-2 ", "start": True},
                            {"_type": "a", "class": "ins-col-12  ins-flex-center ins-border ins-radius-m ins-padding-m ins-flex-center",  "href": url, "_data": [
                                {"_type": "i",
                                    "class": " ins-font-xl " + s["icon"]},
                                {"_type": "span", "class": "ins-col-12 ins-text-center ins-title-14",
                                 "_data": s["title"]}
                            ]},
                        ]
                        row += subrow
                row.append({"_type": "ul", "end": True})
                ui += row
        ui.append({"class": "ins-col-12", "end": True})
        return self.ins._ui._render(ui)

    def total(self, t):
        uidata = [
            {
                "start": "true",
                "class": "ins-flex-start in-col-12 "
            },
            {
                "class": "ins-flex-center  ins-col-12",  "_data": "New Customres "
            },
            {
                "class": "ins-flex-center  ins-col-12 ins-strong ins-title-xl",  "_data": str(t)
            },
            {
                "class": "ins-flex-center  ins-col-12",  "_data": " this month"
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def total_orders(self):
        sql = 'SELECT COUNT(*) AS user_count FROM gla_order WHERE kit_deleted = 0 AND kit_disabled = 0;'
        data = self.ins._db._get_query(sql)[0]
        uidata = [
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-notebook sub-title-icon'></i> Total Orders"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["user_count"])
            },  {
                "class": "ins-icons-arrow-right-circle sub-title-icon"
            },
            {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
        ]
        return self.ins._ui._render(uidata)

    def total_user(self):
        sql = 'SELECT COUNT(*) AS user_count FROM kit_user WHERE kit_deleted = 0 AND kit_disabled = 0;'
        data = self.ins._db._get_query(sql)[0]
        uidata = [
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-users sub-title-icon'></i> Total Customres"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["user_count"])
            },
            {
                "class": "ins-icons-arrow-right-circle sub-title-icon"
            },
            {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            }
        ]
        return self.ins._ui._render(uidata)

    def total_sales(self):
        sql = "SELECT SUM(gla_order.total) AS new_users_count from  gla_order "
        data = self.ins._db._get_query(sql)[0]
        uidata = [
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-cash sub-title-icon'></i> Total Sales"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["new_users_count"])
            },  {
                "class": "ins-icons-arrow-right-circle sub-title-icon"
            },
            {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            },
        ]
        return self.ins._ui._render(uidata)

    def total_products(self):
        sql = 'SELECT COUNT(*) AS user_count FROM gla_product WHERE kit_deleted = 0 AND kit_disabled = 0;'
        data = self.ins._db._get_query(sql)[0]
        uidata = [
            {
                "class": " ins-col-12 sub-title ins-strong",  "_data": "<i  class='ins-icons-users sub-title-icon'></i> Total Products"
            },
            {
                "class": "ins-flex-center  ins-padding-m ins-col-12", "_data": "  "
            },
            {
                "class": "  ins-col-grow ins-strong ins-font-2xl",  "_data": str(data["user_count"])
            },
            {
                "class": "ins-icons-arrow-right-circle sub-title-icon"
            },
            {
                "class": "ins-flex-center  ins-padding-s ins-col-12", "_data": "  "
            }
        ]
        return self.ins._ui._render(uidata)

    def noti(self):
        return [
            {"start": "true", "class": "ins-flex ins-message ins-white ins-col-12"},
            {"class": "ins-icons-info ins-flex-center ins-warning ins-rounded ins-border"},
            {"_data": "New Oeder  on 4/4/2025 <a href='#' class='ins-font-s ins-info-color'>more</a>",
                "class": "ins-col-grow"},
            {"class": "ins-icons-x ins-flex-center ins-danger-color ins-button-text "},
            {"end": "true"},
        ]

    def ui(self):
        burl = self.ins._server._url({"mode":"reports"})

        uidata = [
                        {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},

            {"_data": "<i style='  --color: var(--secondary);' class='ins-icons-bar-chart-dollar ins-padding-m'></i>Sales Dashboard",
             "class": "ins-col-grow ins-strong  ins-title-xl "},
            {"title":"Ai","_data": "<i style='  --color: var(--secondary);font-size:35px' class='ins-icons-ai ins-padding-m'></i>",
             "class": "ins-button-text -home-ai-btn"},
            {"title":"Reports", "_type":"a", "href":burl, "_data": "<i style='  --color: var(--secondary);font-size:35px' class='ins-icons-share-1 ins-padding-m'></i>",
             "class": "ins-button-text"},
            {
                "end": "true"
            },
         ]
        
        self.ins._tmp._set_page_des(self.ins._ui._render(uidata))

        
        
        uidata = [
            {"start": "true", "class": "ins-flex-space-between ins-padding-l in-col-12 "}]
        uidata += self.noti()
        uidata += self.noti()
        uidata += self.noti()
        uidata += self.noti()
        uidata += [{"end": "true"}]
        
        

        
        
        uidata += [
            {"start": "true", "class": "ins-flex-space-between ins-padding-l in-col-12 "},
           
            {"class": "ins-flex ins-card ins-border ins-col-3",
                "_data": self.total_user()},
            {"class": "ins-flex ins-card  ins-border  ins-col-3",
                "_data": self.total_products()},
            {"class": "ins-flex ins-card ins-border   ins-col-3",
                "_data": self.total_orders()},
            {"class": "ins-flex ins-card ins-border  ins-col-3",
                "_data": self.total_sales()},
            {"_data": '<i class="ins-icons-calendar-days "></i>' " This  month",
             "class": "ins-col-12 ins-title-l ins-padding-xl  ins-flex  "},
            {"class": "ins-flex-center ins-border   ins-card  ins-col-12",
                "_data": self.month()},
            {"_data": '<i class="ins-icons-calendar-days "></i>' " This  Year",
             "class": "ins-col-12 ins-title-l  ins-padding-xl  ins-flex  "}, {
                "_data": self._year(), "class": "ins-flex-space-between ins-col-12"
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def sales(self):
        
        app=  AppHomeSales(self.app)
        return app.out()


    @property
    def g(self):
        return  self.ins._server._get()
    
    
    def out(self):
        self.app._include("style.css")
        self.app._include("script.js")
        # 
        if self.g.get("mode") =="reports":
            
            return self.sales()
        else:
            return self.ui()
