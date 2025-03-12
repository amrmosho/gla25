from ins_kit._ui.ui import Ui
import json


class PlgApp(Ui):

    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def __data(self, ops):
        g = self.ins._server._get()
        
        
        l = self.ins._langs._this_get().get("name","en")
        data = {"_p": ops["type"], "_s": g["alias"],
                "_a": ops["src_area"], "_ta": ops["tar_area"], "_g": g, "_l": l, "_h": self.ins._server._path}
        data["_s"] = g["alias"]
        
        return json.dumps(data)

    def __ui(self, ops):

        con: list = []


        """*---------- load widgets  data*"""

        p = {"class": f"ins-app  _{ops['type']} ", "start": True}

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
        con.append({"class": "ins-app-body", "_data": ops["out"]})
        """*---------- load widgets  data*"""
        con.append({"end": True})


        return self._render(con)

    def render(self, ops):

        return self.__ui(ops)
