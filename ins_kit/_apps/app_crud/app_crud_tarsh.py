import math
from ins_kit._apps.app_crud.app_crud_actions import APPCRUDActions
from ins_kit._apps.app_crud.app_crud_parent import appCrudParent


class APPCRUDTrash(appCrudParent):
    def __init__(self, P) -> None:
        super().__init__(P)

    def __tags(self, id=""):
        tgs = self.ins._db._get_data("kit_tags", "*")
        if id == "":
            return tgs
        else:
            for tg in tgs:
                if str(tg["id"]) == id:
                    return tg

    def __get_data(self):

        f = f"   ({self.ops._table}.kit_deleted=1) "
        custom = " * "
        self.ins._db._connect()
        sql = f"select {custom} from {self.ops._table} where {
            f} order by {self.ops._table}.id desc   "
        data = self.ins._db._get_query(sql)
        self.ins._db._close()
        return data

    def _list(self):
        ui = [{"class": "ins-col-12 l-search-bar", "_data": ""}]
        reload_url = self.ins._server._url({},remove=["mode", "id"], clear=True)

        header = [


            { "class": "ins-col-grow  ins-padding-m  ins-flex-center", "_data": [
                
             
                
                {"start": True, "class": " ins-gap-o  -header-searh-group   ins-col-12  ins-group ins-flex  "},
                  {"_data":[{"class": "lni ins-icon lni-trash-3  ins-padding-s"},
                     {"_data": "Trash", "type": "span"}],
                    "class": "ins-radius-xl ins-gap-o  ins-strong-l  ins-title-xs   ins-flex-grow"}, {"class": "ins-flex-grow"},

                {"style": "width:4px",  "class": "ins-border ins-border-left    "},

                {"style": "width:35px", "_data": [
                 {"_type": "a", "href": reload_url, "class": "lni ins-icon  lni-arrow-left ins-padding-s"}], "class": "ins-button     "},

                {"style": "width:105px",  "_data": [
                    {"class": "lni ins-icon lni-plus ins-primary-color ins-padding-s"},
                    {"_data": " Restore ",
                        "class": "ins-flex-grow ins-font-s  ins-primary-color ins-strong"}
                ], "class": "ins-button ins-gap-o ins-flex  app-crud-trash-res"},

                {"style": "width:120px",   "_data": [
                    {"class": "lni ins-icon lni-plus ins-primary-color ins-padding-s"},
                    {"_data": " Restore All ",
                        "class": "ins-flex-grow ins-font-s  ins-primary-color ins-strong"}
                ], "class": "ins-button ins-gap-o ins-flex  app-crud-trash-resall "},


                {"style": "width:105px",  "_data": [
                    {"class": "lni ins-icon lni-plus ins-danger-color ins-padding-s"},
                    {"_data": " remove ",
                        "class": "ins-flex-grow ins-font-s app-crud-trash-remove   ins-danger-color ins-strong"}
                ], "class": "ins-button ins-gap-o ins-flex  "},



                {"style": "width:105px", "_data": [
                    {"class": "lni ins-icon lni-plus ins-danger-color ins-padding-s"},
                    {"_data": " clear ", "class": "ins-flex-grow ins-font-s   ins-danger-color ins-strong"}],
                 "class": "ins-button app-crud-trash-clear  ins-gap-o ins-flex  "},


                {"end": True}
            ]}]
        self.ins._tmp._set_page_des(self.ins._ui._render(header))
        ui = [
            {"class": "ins-col-12 app-crud-body ins-padding-xl insaction ",  "data-cname": self.ops._table, "data-plgin": "ins_plg_py_crud",
                "data-insaction": "plgin", "_data": self._body()}

        ]
        return self.ins._ui._render(ui)

    def __update_body_item(self, ops, v):
        if "_view" in ops:
            rv = self.ins._ui._format(ops, v)
        elif "_type" in ops and ops["_type"] == "tags":

            tg = ""
            if v["kit_tags"] != "":
                tgs = v["kit_tags"].split(",")
                for t in tgs:
                    db_tg = self.__tags(t)

                    turl = self.ins._server._url({"f": f"tag={db_tg["id"]}"})
                    tg += f"<b style='background:{db_tg["color"]}' class='ins-tag ins-flex-center ins-text-center '><span class='app-crud-list-remove-tag-actions ins-flex-center'><a class='ins-button-text' href='{
                        turl}'><i class='lni ins-font-l  lni-search-text'></i> </a><i data-oid='{v["id"]}'  data-mid='{db_tg["id"]}' data-obj='{self.ops._table}'   class='lni ins-button-text-danger  ins-font-l  app-crud-list-remove-tag lni-xmark'></i></span> {db_tg["title"]}</b>"

            mclass = f"_{self.ops._table}_{v["id"]}_tags"

            rv = f"<div class='ins-flex ins-k-tags-area {mclass} ins-col-12'><i data-oid='{v["id"]}' data-obj='{
                self.ops._table}' class='lni ins-button-text app-crud-list-add-tag  lni-bookmark-circle'></i>{str(tg)}</div>"
        elif "_type" in ops and ops["_type"] == "method":
            area = self.ins._this._area["url"]
            type = "ins_apps"
            ds = ops["_data"].split(".")
            _path = f'{area}.{type}.{ds[0]}.{ds[0]}'
            _class_name = self.ins._map._get_class_name(ds[0])
            exec(f"from {_path} import {_class_name}")
            rv = eval(f"{_class_name}.{ds[1]}(ops,v,self.ins)")
        else:
            rv = str(v)
        return rv

    def _body(self):
        data = self.__get_data()
        ui = []
        if len(data) == 0:
            ui.append({
                "data-insaction": "plgin",
                "data-plgin": "ins_plg_py_crud",
                "_data": "No data To show",
                      "class": "ins-message  insaction ins-danger"})
            return self.ins._ui._render(ui)
        header = []
        for h in self.ops._list_data:
            hr = {}
            hr["_data"] = h["title"]
            hr["class"] = h["class"]
            header.append(hr)

        # add Selector all ui to Header
        header[0]["_data"] = f"<span class='ins-raw-selector-all' ></span>{
            header[0]["_data"]}"
        body = []
        for d in data:
            rd = []
            for h in self.ops._list_data:
                if "_trans" in h:
                    h = self.ins._langs._render_tags(h)
                hr = {}
                data = d
                if "name" in h:
                    data = d[h["name"]]

                hr["_data"] = self.__update_body_item(h, data)
                hr["class"] = h["class"]
                rd.append(hr)
            # add Actions  to  row
            # add Selector ui to  row
            rd[0]["_data"] = f"<span data-id='{d["id"]}' class='ins-raw-selector' ></span>{
                rd[0]["_data"]}"
            body.append(rd)
        # craete ui

        ui = [
            {"_type": "table", "data": body, "header": header,
             "class": " ins-col-12 ins-table ins-date-table ins-pading-xl "},

        ]
        return self.ins._ui._render(ui)

    def render(self):
        actions = APPCRUDActions(self)
        
        def update():
              return  self._body()
        if self.ins._server._get("id") == "curd_trash_clear":
            return actions._clear(update)
        if self.ins._server._get("id") == "curd_trash_res":
            return actions._restore(update)
        if self.ins._server._get("id") == "curd_trash_body":
            return self._body()
        if self.ins._server._get("id") == "curd_trash_remove":
            return actions._remove(update)
        if self.ins._server._get("id") == "curd_trash_resall":
            return actions._restore(update)
        l = self._list()
        return l
