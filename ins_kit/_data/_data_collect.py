
from datetime import datetime
from ins_kit.ins_parent import ins_parent


class DataCollect(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def __db(self, ops):
        if "fl_query" in ops:
            db_data = self.ins._db._get_query(ops["fl_query"])
        else:
            ops["fl_value"] = "id" if "fl_value" not in ops else ops["fl_value"]
            ops["fl_text"] = "title" if "fl_text" not in ops else ops["fl_text"]
            ops["fl_where"] = "1=1" if "fl_where" not in ops else ops["fl_where"]
            db_data = self.ins._db._get_data(ops["fl_table"], f"{ops["fl_value"]} ,{
                ops["fl_text"]}", ops["fl_where"])
        rd = {}
        
        if "fl_start" in ops:
            st= ops["fl_start"].split(",")
            rd[str(st[0])] = str(st[1]) 

        for d in db_data:
            rd[str(d[ops["fl_value"]])] = str(d[ops["fl_text"]])
        ops["fl_data"] = rd
        if "fl_value" in ops:
            del ops["fl_value"]
        if "fl_text" in ops:
            del ops["fl_text"]
        if "fl_where" in ops:
            del ops["fl_where"]
        if "fl_table" in ops:
            del ops["fl_table"]
        if "fl_type" in ops:
            del ops["fl_type"]
        return ops

    def __area(self, ops):
        d = {}
        d["-1"] = ""

        for k, v in self.ins._this._settings["areas"].items():
            d[v["name"]] = v["title"]
        ops["fl_data"] = d
        return ops

    def __data(self, ops):

        rd = {}
        if type(ops["fl_data"]) == str:
            fl_data = ops["fl_data"].split(",")
            for v in fl_data:
                rd[v] = v
        elif type(ops["fl_data"]) == dict:
            rd = ops["fl_data"]
        elif type(ops["fl_data"]) == list:
            for v in ops["fl_data"]:
                rd[v] = v

        ops["fl_data"] =    rd
        return ops
        
        
        

    def _render(self, ops={}):

        # fl

        if "fl_type" in ops:
            if ops["fl_type"] == "areas":
                ops = self.__area(ops)
            elif ops["fl_type"] == "db":
                ops = self.__db(ops)
        elif "fl_data" in ops:
            self.__data(ops)
        else:
               ops["fl_data"] ={}

        return ops
