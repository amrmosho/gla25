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

    def __list(self, ops):
        self.__data.clear()
        if "_data" in ops and type(ops["_data"]) == str:
            a = ops["_data"].split(",")
            for k in a:
                self.__data.append({"value": k, "_data": k})
        if "_data" in ops and type(ops["_data"]) == dict:
            for k in ops["_data"]:
                self.__data.append({"value": k, "_data": ops["_data"][k]})
        if "_data" in ops and type(ops["_data"]) == list:
            for k in ops["_data"]:
                self.__data.append({"value": k, "_data": k})

    def __db(self, ops):
        if "_query" in ops:
            db_data = self.ins._db._get_query(ops["_query"])
        else:
            ops["_value"] = "id" if "_value" not in ops else ops["_value"]
            ops["_text"] = "title" if "_text" not in ops else ops["_text"]
            ops["_where"] = "1=1" if "_where" not in ops else ops["_where"]
            db_data = self.ins._db._get_data(ops["_table"], f"{ops["_value"]} ,{
                ops["_text"]}", ops["_where"])
        rd = {}
        rd["0"] = "-----"

        for d in db_data:
            rd[str(d[ops["_value"]])] = str(d[ops["_text"]])
        ops["_data"] = rd
        if "_value" in ops:
            del ops["_value"]
        if "_text" in ops:
            del ops["_text"]
        if "_where" in ops:
            del ops["_where"]
        if "_table" in ops:
            del ops["_table"]
        if "_data_type" in ops:
            del ops["_data_type"]
        return ops

    def __area(self, ops):
        d = {}
        d["-1"] = ""

        for k, v in self.ins._this._settings["areas"].items():
            d[v["name"]] = v["title"]
        ops["_data"] = d
        return ops

    def __update_data(self, ops):
        if "type" in ops:
            if ops["type"] == "areas":
                ops = self.__area(ops)
            elif ops["type"] == "db":
                ops = self.__db(ops)

        if "_data_type" in ops:
            if ops["_data_type"] == "areas":
                ops = self.__area(ops)
            elif ops["_data_type"] == "db":
                ops = self.__db(ops)

        self.__list(ops)

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
