from ins_kit._apps.app_crud.app_crud_parent import appCrudParent
import csv
from flask import Response, send_file


class APPCRUDActions(appCrudParent):

    def _ai(self, ops={}):
        rq = self.ins._server._post()

        if "tables" in ops._ai :
            
            tables = ops._ai["tables"]

        else:

            tables = [ops._table]
        response_data = self.ins._ai.generate_sql(rq["v"], tables)
        if type(response_data) == list:
            header = []
            body = []

            for k, v in response_data[0].items():
                header.append({"_data": str(k), "class": "ins-col-grow"})

            for a in response_data:
                row = []
                for k, v in a.items():
                    row.append({"_data": str(v), "class": "ins-col-grow"})

                body.append(row)

            uidata = [
                {"_type": "table", "data": body, "header": header,
                "class": " ins-col-12 ins-table ins-table-regular   ins-pading-xl "},
            ]
            return self.ins._ui._render(uidata)
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
