from ins_kit._ui.ui import Ui


class PlgTable(Ui):

    def _ui(self):
        ui_data = []

        ui_data.append({"class": f"ins-table-data " +self.ops["class"], "start": True})
        ui_data.append(
            {"class": f"   ins-tr ins-flex-space-between    ins-thead  ", "start": True})
        for h in self.ops["header"]:
            h["class"] += " ins-td "
            ui_data.append(h)
        ui_data.append({"end": True})

            
        for ds in self.ops["data"]:
            ui_data.append({"class": f" ins-tr ins-flex-space-between ", "start": True})
            for d in ds:
                d["class"] += " ins-td "
                ui_data.append(d)  
            ui_data.append({"end": True})
   
   
   
   
        ui_data.append({"end": True})
        r = self.ins._ui._render(ui_data)
        return r

    def render(self, ops):
        self.ops = ops
        return self._ui()
