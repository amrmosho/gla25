from ins_kit._ui.ui import Ui


class PlgPanel(Ui):

    def _ui(self):
        ui_data = []

        st = {"class": f"ins-col-12   ins-panel  ", "start": True}

        if "style" in self.ops:
            st["style"] = self.ops["style"]

        if "class" in self.ops:
            st["class"] += " " + self.ops["class"]

        ui_data.append(st)

        hr = {"class": f"ins-col-12  ins-header ", "start": True}

        if "_header_style" in self.ops:
            hr["style"] = self.ops["header_style"]

        if "_header_class" in self.ops:
            hr["class"] += " " + self.ops["header_class"]

        hr["_data"] = self.ops["_header"]
        hr["_data"].append({"class": "ins-icon lni lni-angle-double-right "})
        ui_data.append(hr)

        ui_data.append({"end": True})

        bo = {"class": f"ins-col-12 ins-flex    ins-body ", "start": True}

        if "_data_style" in self.ops:
            hr["style"] = self.ops["body_style"]
        if "_data_class" in self.ops:
            hr["class"] += " " + self.ops["body_class"]

        bo["_data"] = self.ops["_data"]

        ui_data.append(bo)
        ui_data.append({"end": True})

        ui_data.append({"end": True})

        
        
        
        r = self.ins._ui._render(ui_data)
        return r

    def render(self, ops):
        self.ops = ops
        return self._ui()
