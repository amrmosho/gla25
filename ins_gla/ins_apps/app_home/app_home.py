from ins_kit._engine._bp import App


class AppHome(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

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
                    "menu_item_table", "*", f"   fk_menu_item_id={d["id"]} order by kit_order")

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
                                {"_type": "i", "class": " ins-font-xl "+ s["icon"]},
                                {"_type": "span", "class": "ins-col-12 ins-text-center ins-title-14",
                                 "_data": s["title"]}

                            ]},
                        ]
                        row += subrow
                row.append({"_type": "ul", "end": True})
                ui += row
                
                
                

        ui.append({"class": "ins-col-12", "end": True})
        return self.ins._ui._render(ui)

    def ui(self):

        uidata = [
            {
                "start": "true",
                "class": "ins-flex-start in-col-12 "
            },
            {
                "class": "ins-flex-center ins-card", "style": "width:300px", "_data": self.user_data()
            },

            {
                "class": "ins-flex  ins-col-grow", "_data": self.menu_data()
            },
            {
                "start": "end"
            }

        ]

        return self.ins._ui._render(uidata)

    def out(self):

        return self.ui()
