
from ins_kit._engine._bp import Widget


class WdgContent(Widget):
    def __init__(self, widget) -> None:
        self.widget: Widget = widget
        super().__init__(widget.ins)

    def out(self):
        if "id" not in self.widget._options:
            return " No content selected "
        data = self.ins._db._get_row(
            "content_table", "*", f"id={self.widget._options["id"]}")
        if not data :
            return " No content selected "
        self.widget._include("script.js")
        ui = [
            {"_data":   data["content"], "class": "ins-col-12  ins-flex ap-wdgt-body "},
        ]
        return self.ins._ui._render(ui)