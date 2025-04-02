from ins_kit._engine._bp import App


class AppHome(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def ai_call(self):
        rq = self.ins._server._post()

        
        response_data = self.ins._ai.generate_sql(rq["v"], ["gla_product","gla_order" ,"gla_order_item" ,'kit_user'])

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


            if len(a) >1:
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

    def total(self):
        uidata = [
            {
                "start": "true",
                "class": "ins-flex-start in-col-12 "
            },
            {
                "class": "ins-flex-center  ins-col-12",  "_data": "New Customres "
            },
            {
                "class": "ins-flex-center  ins-col-12 ins-strong ins-title-xl",  "_data": "10000"
            },
            {
                "class": "ins-flex-center  ins-col-12",  "_data": " this month"
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def pie(self):
        e = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]
        uidata = [
            {"_data": "Total per item",  "data": e,
                "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"_type": "chart", "type": "pie", "data": e, "style": "width:100%",
                "class": "ins-col-12 ins-flex  "},
        ]
        return self.ins._ui._render(uidata)

    def col(self):
        e = [
            ['Task', 'Hours per Day'],
            ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50],
            ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50],  ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50], ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50],
            ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50],  ['1/4', 100],
            ['2/4', 200],
            ['3/4', 10],
            ['4/4', 500],
            ['5/4', 50]
        ]
        uidata = [
            {"_data": "Total per month",  "data": e,
                "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"_type": "chart", "type": "col", "data": e, "style": "width:100%",
                "class": "ins-col-12  ins-flex  "}
        ]
        return self.ins._ui._render(uidata)

    def bar(self):
        e = [
            ['Task', 'Hours per Day'],
            ['1/25', 100],
            ['2/204', 200],
            ['3/204', 10],
            ['4/204', 500],
            ['5/204', 50],
        ]
        uidata = [
            {"_data": "Total per user",  "data": e,
                "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"_type": "chart", "type": "bar", "data": e, "style": "width:100%",
                "class": "ins-col-12  ins-flex  "}
        ]
        return self.ins._ui._render(uidata)

    def line(self):
        e = [
            ['Task', 'Hours per Day'],
            ['1/25', 100],
            ['2/204', 200],
            ['3/204', 10],
            ['4/204', 500],
            ['5/204', 50],
        ]
        uidata = [
            {"_data": "Total per user",  "data": e,
                "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"_type": "chart", "type": "line", "data": e, "style": "width:100%",
                "class": "ins-col-12  ins-flex  "}
        ]
        return self.ins._ui._render(uidata)

    def ui(self):
        uidata = [



            {"start": "true", "class": "ins-flex-start in-col-12 "},


            {
                "start": "true", "class": "ins-flex ins-card ins-col-12"
            },


            {"_data": "<i style='  --color: var(--secondary);' class='ins-icons-bar-chart-dollar ins-padding-m'></i>Sales Dashboard",
             "class": "ins-col-grow ins-strong  ins-title-xl "},
            {"_data": "<i style='  --color: var(--secondary);font-size:35px' class='ins-icons-ai ins-padding-m'></i>",
             "class": "ins-button-text -home-ai-btn"},
            {"_data": "<i style='  --color: var(--secondary);font-size:35px' class='ins-icons-share-1 ins-padding-m'></i>",
             "class": "ins-button-text"},

            {
                "end": "true"
            },
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.total()},
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.total()},
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.total()},
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.total()},
            {
                "start": "true", "class": "ins-flex-center ins-card ins-col-12"
            },
            {"_data": "This month  per user",
             "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"class": "ins-flex-center  ins-col-9", "_data": self.col()},
            {
                "start": "true", "class": "ins-flex-center  ins-col-3"
            },
            {"class": "ins-flex-center ins-info ins-card  ins-col-12",
                "_data": self.total()},
            {"class": "ins-flex-center  ins-info  ins-card ins-col-12",
                "_data": self.total()},
            {
                "end": "true"
            },
            {
                "end": "true"
            },
            {
                "start": "true", "class": "ins-flex-center ins-card ins-col-12"
            },
            {"_data": "This month  per user",
                "class": "ins-col-12 ins-title-l  ins-flex  "},
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.pie()},
            {"class": "ins-flex-center ins-card ins-col-3", "_data": self.bar()},
            {"class": "ins-flex-center ins-card ins-col-6", "_data": self.line()},
            {
                "end": "true"
            },
            {
                "end": "true"
            }
        ]
        return self.ins._ui._render(uidata)

    def out(self):
        self.app._include("script.js")
        return self.ui()
