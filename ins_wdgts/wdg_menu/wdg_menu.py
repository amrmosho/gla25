
from ins_kit._engine._bp import Widget


class WdgMenu(Widget):

    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):

        ui = []
        self.widget._include("script.js")
        self.widget._include("style.css")
        ui.append({"class": "ins-col-12 ins-flex ins-menu", "start": True})
        gt = "title,id,kit_hidden,alias,add_to_url"
        data = self.ins._db._get_data(
            "menu_item_table", gt, f"fk_menu_id='{self.widget._options["id"]}'   and kit_menu_item.fk_menu_item_id='0' order by kit_order", True)

        for d in data:

            if str(d["kit_hidden"]) != "1":
                url = f"/{d["alias"]}/{d["add_to_url"]}"

                if len(subdata) >0 :
                    url ="#"
                    
                row = [
                    {"_type": "li", "class": "ins-menu-item", "start": True},
                    {"_type": "a", "href": url, "_data": [
                        {"_type": "span", "_data": d["title"]}]},

                ]

                subdata = self.ins._db._get_data(
                    "menu_item_table", gt, f"fk_menu_id='{self.widget._options["id"]}'  and kit_menu_item.fk_menu_item_id='{d["id"]}' order by kit_order", True)


                if len(subdata) >0 :

                    row.append({"_type": "ul", "start": True ,"class":"ins-menu-sub ins-white ins-padding-xl"})

                    for sd in subdata:
                        surl = f"/{d["alias"]}/{d["add_to_url"]}"
                        
                        
                        subrow = [
                            {"_type": "li", "class": "ins-menu-sub-item", "start": True},
                            {"_type": "a", "href": surl, "_data": [
                                {"_type": "span", "_data": sd["title"]}]},
                            {"_type": "li", "end": True}
                        ]
                        row += subrow
                        
                    row.append({"_type": "ul", "end": True})
                    
                


                row.append({"_type": "li", "end": True})

                ui += row

        ui.append({"class": "ins-col-12", "end": True})
        return self.ins._ui._render(ui)
