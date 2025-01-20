from ins_kit._ui.ui import Ui
import json


class PlgWdgt(Ui):

    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def __data(self, ops):
        g = self.ins._server._get()
        data = {"_w": ops["type"] ,"_s":g["alias"] ,"_a" : ops["src_area"],"_p" :self.ins._server._path}
        return json.dumps(data)

    def __ui(self, ops):

        con: list = []

        """*---------- load widgets  data*"""
        p = {"class": f"ins-wdgt _{ops["type"]}", "start": True}

        if "style" in ops:
            p["style"] = ops["style"]
            del ops["style"]

        if "class" in ops and ops["class"] != "":
            p["class"] += " "+ops["class"]
            del ops["class"]
        else:
            p["class"] += " ins-col-12 "

        p["data-data"] = self.__data(ops)

        con.append(p)
        con.append({"class": "ins-wdgt-body", "_data": ops["out"]})
        """*---------- load widgets  data*"""
        con.append({"end": True})

        return self._render(con)

    def render(self, ops):

        return self.__ui(ops)
