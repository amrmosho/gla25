from ins_kit._apps.app_crud.app_crud_parent import appCrudParent
import csv
from flask import Response, send_file


class APPCRUDActions(appCrudParent):

    def _ai(self, ops={}):
        rq = self.ins._server._post()

        if "tables" in ops._ai:

            tables = ops._ai["tables"]

        else:

            tables = [ops._table]
        response_data = self.ins._ai.generate_sql(rq["v"], tables)

        if type(response_data) == list:
            header = []
            body = []

            e = [
                ['Task', 'Hours per Day'],
                ['Work', 11],
                ['Eat', 2],
                ['Commute', 2],
                ['Watch TV', 2],
                ['Sleep', 7]
            ]
            d = []
            rw = []
            for k, v in response_data[0].items():
                header.append({"_data": str(k), "class": "ins-col-grow"})
                rw.append(str(k))

            d.append(rw)

            for a in response_data:
                row = []
                rw = []
                for k, v in a.items():
                    row.append({"_data": str(v), "class": "ins-col-grow"})
                    if not self.ins._data._is_number(v):
                        v = str(v)
                    rw.append(v)
                body.append(row)
                d.append(rw)

            r = []

            r += [{"start": "true", "class": "ins-flex ins-col-12"},
                  {"start": "true", "class": "ins-flex ins-card  ins-col-12"}, {"_data": rq["v"], "class": "ins-flex ins-col-grow"}, {
                      "_data": '<i class="ins-icons-download"></i>', "style": "width:50px"}, {"_data": '<i class="ins-icons-printer"></i>', "style": "width:50px"},
                  {"end": "true"}
                  ]



            if len(a) >1:
                r += [
                    {"_type": "chart", "type": "ddd", "data": d, "style": "height:400px",
                    "class": "ins-col-8  ins-flex  ins-padding-xl"},
                    {"_type": "chart", "type": "pie", "data": d, "style": "height:400px",
                    "class": "ins-col-4  ins-flex  ins-padding-xl"}
                ]
            
            

            r += [
                {"_type": "table", "data": body, "header": header,
                 "class": " ins-col-12 ins-table ins-table-regular   ins-pading-xl "},
            ]
            r += [{"end": "true"}]

            return self.ins._ui._render(r)
        else:
            return response_data

    def _delete(self, _callback=None):
        id = self.ins._server._get("ids")
        ids = id.split(",")
        w = ""
        sp = ""
        if len(ids) > 0:
            for i in ids:
                w += f"{sp} id='{i}' "
                sp = "or"
            self.ins._db._update(self.ops._table, {"kit_deleted": "1"}, w)
        if _callback:
            return _callback()

    def _clear(self, _callback=None):
        w = f"   ({self.ops._table}.kit_deleted=1) "
        self.ins._db._delete(self.ops._table,  w)
        if _callback:
            return _callback()

    def _restore(self, _callback=None):
        id = self.ins._server._get("ids")
        ids = id.split(",")
        w = ""
        sp = ""
        if len(ids) > 0:
            for i in ids:
                w += f"{sp} id='{i}' "
                sp = "or"
            self.ins._db._update(self.ops._table, {"kit_deleted": "0"}, w)
        if _callback:
            return _callback()

    def _restore_all(self, _callback=None):
        w = f"   ({self.ops._table}.kit_deleted=1) "
        self.ins._db._update(self.ops._table, {"kit_deleted": "0"}, w)
        if _callback:
            return _callback()

    def _remove(self, _callback=None):
        id = self.ins._server._get("ids")
        ids = id.split(",")
        w = ""
        sp = ""
        if len(ids) > 0:
            for i in ids:
                w += f"{sp} id='{i}' "
                sp = "or"
            self.ins._db._delete(self.ops._table,  w)
        if _callback:
            return _callback()

    def _copy(self, _callback=None):
        id = self.ins._server._get("id")
        ids = id.split(",")
        w = ""
        sp = ""
        if len(ids) > 0:
            for i in ids:
                w += f"{sp} id='{i}' "
                sp = "or"

            src = self.ins._db._get_data(self.ops._table, "*", w)
            for s in src:
                del s["id"]
                src = self.ins._db._insert(self.ops._table, s)

        if _callback:
            return _callback()

    def _export(self, data, name):
        csv_data = ""

        sp = ""
        for k in data[0]:
            csv_data += sp + str(k)
            sp = ","
        csv_data += "\n"

        for r in data:
            sp = ""
            for k in r:
                csv_data += sp + str(r[k])
                sp = ","
            csv_data += "\n"

        response = Response(csv_data, content_type="text/csv")
        response.headers["Content-Disposition"] = f"attachment; filename={name}.csv"

        return response

    def _export_all(self, _callback):
        pass
