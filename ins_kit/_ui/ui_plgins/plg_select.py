from ins_kit._ui.ui import Ui
from ins_kit._ui.ui_plgins.plg_input import PlgInput
import json


class PlgSelect(Ui):
    __data = []

    def ui(self, ops):
        r = ""
        if "value" in ops:
            ops["data-value"] = ops["value"]
        if "class" not in ops:
            ops["class"] = " "
        if "name" in ops:
            ops["class"] += " ins-form-input  "+ops["name"]
        ops["not_plgin"] = True
        ops["start"] = True
        r = [ops]
        for i in self.__data:
            i["_type"] = "option"
            values = []
            if "value" in ops:
                values = str(ops["value"]).split(",")
            if "value" in ops and str(i["value"]) in values:
                i["selected"] = "true"
            else:
                if "selected" in i:
                    del i["selected"]
            r.append(i)
        r.append({"_type": "select", "not_plgin": True, "end": True})
        return self._render(r)



    def __update_data(self, ops):
        self.__data.clear()


        ops = self.ins._data_collect._render(ops)
        for k, v in ops["fl_data"].items():
            self.__data.append({"value": k, "_data": v})

    def trans(self, ops):
        self.__update_data(ops)
        for i in self.__data:
            if "value" in ops and ops["value"] == i["value"]:
                return i["_data"]
        return ops["value"]

    def render(self, ops):
        self.__update_data(ops)
        i = PlgInput(self)
        ops["_data"] = self.ui(ops)
        return i.container(ops)
