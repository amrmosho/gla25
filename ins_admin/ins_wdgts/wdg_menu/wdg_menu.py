
from ins_kit._engine._bp import Widget


class WdgMenu(Widget):

    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def test2(self):

        return "test2"

    def out(self):

        ui = []
        self.widget._include("script.js")
        self.widget._include("style.css")
        ui.append({"class": "ins-col-12 ins-flex wdg-admin-menu", "start": True})
        data = self.ins._db._get_data(
            "menu_item_table", "*", f"fk_menu_id='{self.widget._options["id"]}'  and fk_menu_item_id=0 order by kit_order",True)

        for d in data:

            if self.ins._users._per_check_menu(d["id"]) and str(d["kit_hidden"]) != "1":

                subdata = self.ins._db._get_data(
                    "menu_item_table", "*", f"fk_menu_id='{self.widget._options["id"]}'  and fk_menu_item_id={d["id"]} order by kit_order",True)

                mclass = ""
                if len(subdata) == 0:
                    url = self.ins._server._url(
                        {"alias": d["alias"]},["mode"], clear=True)
                    mclass = ""
                else:
                    url = "#"
                    mclass = "ins-menu-parent"

                row = [
                    {"_type": "li", "class": f"ins-menu-item {mclass}", "start": True},
                    {"_type": "a", "class": "ins-col-12 ins-padding-m ins-flex-center",  "href": url, "_data": [
                        {"_type": "i", "class": "ins-col-12 ins-text-center ins-title-xs",
                            "class": d["icon"]},
                        {"_type": "span", "class": "ins-col-12  ins-text-center",
                            "_data": d["title"]}

                    ]},
                ]

                if len(subdata) > 0:
                    row.append(
                        {"_type": "ul", "class": "sub-menu ins-padding-xl", "start": True})

                    subrow = [
                        {"_type": "li", "class": "sub-menu-title", "start": True},
                        {"class": "ins-padding-xl ins-title-m ins-strong",  "href": url, "_data": d["title"]}]
                    row += subrow

                    for s in subdata:
                        if self.ins._users._per_check_menu(s["id"]) and str(s["kit_hidden"]) != "1":
                            url = self.ins._server._url({"alias": s["alias"]},["mode"] ,clear=True)
                            subrow = [
                                {"_type": "li", "class": "sub-menu-item",
                                    "start": True},
                                {"_type": "a", "class": "ins-col-12 ins-padding-m ins-flex-center",  "href": url, "_data": [
                                    {"_type": "i", "class": "ins-col-2 ins-text-center",
                                        "class": s["icon"]},
                                    {"_type": "span", "class": "ins-col-10  ",
                                     "_data": s["title"]}

                                ]},
                            ]
                            row += subrow

                    row.append({"_type": "ul", "end": True})
                row.append({"_type": "li", "end": True})

                ui += row

        ui.append({"class": "ins-col-12", "end": True})
        return self.ins._ui._render(ui)
