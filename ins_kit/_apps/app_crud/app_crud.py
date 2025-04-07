from ins_kit._apps.app_crud.app_crud_form import APPCRUDForm
from ins_kit._apps.app_crud.app_crud_list import APPCRUDList
from ins_kit._apps.app_crud.app_crud_settings import APPCRUDSettings
from ins_kit._apps.app_crud.app_crud_tarsh import APPCRUDTrash

from ins_kit.ins_parent import ins_parent


class AppCrudOps:
    def __init__(self):

        self._table = "kit_content"

        self._url = ""
        self._pros_name = ""
        self._list_query = ""
        self._list_where = ""

        self._list_limit = 12
        self._list_data = []
        self._list_filter = []
        self._form_data = []
        self._user_settings = {}
        self._ai = {}

        self._form_befor_insert: function = None
        self._form_after_insert: function = None
        self._form_befor_update: function = None
        self._form_after_update: function = None
        self._form_befor_update_data: function = None

        self._form_edit_append: function = None
        self._form_add_append: function = None
        self._crud_setting = {}
        self._list_settings = {}


class APPCRUD(ins_parent):

    ops: AppCrudOps

    @property
    def k(self):
        return "crud"

    def __init__(self, Ins, ops: AppCrudOps, properties={}) -> None:
        self.ins = Ins
        self.ops = self.__update(ops, properties)
        super().__init__(Ins)

    def csets(self, name, getfor="", list_name=""):
        r = {}
        r[self.k] = {}
        al = self.ins._users._collect_settings(name)
        if ("job" in al and self.k in al["job"]) or ("user" in al and self.k in al["user"]) or ("job" in al and self.k in al["job"]):

            for a in al:
                if getfor == "" or getfor == a:
                    for cu in al[a][self.k]:
                        al[a][self.k][cu]["for"] = a
                    r[self.k].update(al[a][self.k])

            if list_name != "":
                if ("job" in al and self.k in al["job"]):
                    return r[self.k][list_name]
            return r
        else:
            return {}

    def __update(self, ops: AppCrudOps, properties):
        if type(properties) == dict and len(properties) > 0:

            if "table" in properties:
                ops._table = properties["table"]

            ops._list_settings = self.csets(ops._table)

            ops._user_settings = self.ins._users._get_settings(ops._table)

            actclt = {}
            if "inscl" in self.ins._server._get():
                cl = self.ins._server._get("inscl")
                if "crud" in ops._list_settings and cl in ops._list_settings["crud"]:
                    actclt = ops._list_settings["crud"].get(cl)
            elif "crud" in ops._list_settings:
                for k, v in ops._list_settings["crud"].items():
                    if "insact" in v and v["insact"] == "1":
                        actclt = ops._list_settings["crud"].get(k)
                        self.ins._server._get_add("inscl", k)

            jdata_names = ["list_data", "form_data", "list_filter", "ai"]
            for p in properties:
                if p in actclt:
                    if p in jdata_names:
                        properties[p] = self.ins._json._decode(actclt[p])
                    else:
                        properties[p] = actclt[p]

            if ops._user_settings != False and "pg_count" in ops._user_settings:
                ops._list_limit = int(ops._user_settings["pg_count"])
            elif "list_limit" in properties:
                ops._list_limit = int(properties["list_limit"])

            ls = ["list_data", "table", "list_filter", "form_data",
                  "crud_setting", "url", "url", "pros_name", "ai", "list_query", "list_where"]

            for l in ls:
                if l in properties:
                    setattr(ops, f"_{l}", properties[l])

            return ops
        else:
            return ops

    def render(self):

        mode = self.ins._server._get("mode")
        if mode == "add" or mode == "edit":
            l = APPCRUDForm(self)
            return l.render()
        if mode == "trash":
            l = APPCRUDTrash(self)
            return l.render()
        if mode == "settings":
            l = APPCRUDSettings(self)
            return l.render()

        else:
            l = APPCRUDList(self)

            return l.render()
