
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
        ui.append({"class": "ins-col-12 ins-flex ins-menu", "start": True})
        data = self.ins._db._get_data(
            "menu_item_table", "*", f"fk_menu_id='{self.widget._options["id"]}' order by kit_order")

        for d in data:
            
            if  str(d["kit_hidden"]) != "1":
                url = f"/{d["alias"]}/"
                row = [
                    {"_type": "li", "class": "ins-menu-item", "start": True},
                    {"_type": "a", "href": url, "_data": [
                        {"_type": "span", "_data": d["title"]}

                    ]},
                    {"_type": "li", "end": True},
                ]

                ui += row

        ui.append({"class": "ins-col-12", "end": True})
        return self.ins._ui._render(ui)
