from flask import redirect, request
from ins_kit._apps.app_crud.app_crud_parent import appCrudParent


class APPCRUDForm(appCrudParent):
    def __init__(self, P) -> None:
        super().__init__(P)

    def __db_actions(self):

        if "tb" in self.ins._server._post():
            if self.ins._server._post("m") == "edit":
                db_data = self.ins._server._post()

                if self.ops._form_befor_update != None:
                    db_data = self.ops._form_befor_update(db_data)

                self.ins._db._update(
                    self.ins._server._post("tb"), db_data, f"id={db_data["id"]}")

                if self.ops._form_after_update != None:

                    rdata = self.ins._db._get_row(
                        self.ins._server._post("tb"), "*", f"id={db_data["id"]}")

                    db_data = self.ops._form_after_update(rdata)

            else:
                db_data = self.ins._server._post()

                if self.ops._form_befor_insert != None:
                    db_data = self.ops._form_befor_insert(db_data)

                id = self.ins._db._insert(
                    self.ins._server._post("tb"),  db_data)

                if self.ops._form_after_insert != None:
                    rdata = self.ins._db._get_row(
                        self.ins._server._post("tb"), "*", f"id={id}")
                    db_data = self.ops._form_after_insert(rdata)

        return "1"

    def __update_data_item(self, data, db_data):

        if self.ops._form_befor_update_data != None:
            db_data = self.ops._form_befor_update_data(db_data)

        for m in data:
            if "name" in m:

                if db_data != False and m["name"] in db_data and "type" in m and (
                        m["type"] == "checkbox" or m["type"] == "radio"):
                    v = db_data[m["name"]]
                    if str(m["value"]) == str(v):
                        m["checked"] = "true"

                if db_data != False and m["name"] in db_data and "type" in m and (m["type"] == "textarea"):
                    m["_data"] = db_data[m["name"]]

                elif db_data != False and m["name"] in db_data:
                    m["value"] = db_data[m["name"]]

            if "_data" in m and type(m["_data"]) == list:
                m["_data"] = self. __update_data_item(m["_data"], db_data)

        return data

    def __update_data(self):

        if "id" in self.get:
            db_data = self.ins._db._get_disabled()._get_row(
                self.ops._table, "*", f"id='{self.get["id"]}'")
            if self.get["mode"] == "edit":
                self.ops._form_data = self. __update_data_item(
                    self.ops._form_data, db_data)

            id = {"_type": "input", "type": "hidden", "value": self.get["id"],
                  "name": "id", "class": "ins-button ins-col-2"}

            self.ops._form_data.append(id)

    def __form(self):
        ui = []
        self.__update_data()
        if self.get["mode"] == "edit":
            save_button_title = self.ins._langs._get("update")
        to = "left"
        if self.ins._langs._this_get()["direction"] == "rtl":
            to = "right"

        back_url = self.ins._server._url({}, remove=["mode", "id"])
        save_button_title = self.ins._langs._get("save")

        action_menu = [{"style": "width: 70px", "_type": "button",  "_data": [
            {"class": "lni ins-icon lni-plus ins-primary-color ins-padding-s"},
            {"_data": save_button_title,
             "class": "ins-flex-grow ins-font-s ins-strong-l   ins-primary-color ins-strong"}
        ], "class": "ins-button  crud-form-submit ins-gap-o ins-flex  "},
            {"style": "width:4px ;    height: 18px;",
                "class": f"ins-border ins-border-left    "},
            {"style": "width:25px", "_data": [
                {"start": True, "class": "ins-menu ins-end"},
                {"style": "transform: rotate(90deg);",
                 "class": "lni ins-icon ins-header  lni-menu-meatballs-1 ins-padding-s"},
                {"_type": "ul", "start": True},
                {"_type": "li", "class": 'crud-form-reset',
                 "_data": "<i class='lni ins-icon lni-refresh-circle-1-clockwise '></i>" + self.ins._langs._get("reset")},
                {"_type": "li", "class": "crud-form-submit-back",
                 "_data":  f"<i class='lni ins-icon  lni ins-icon  lni-arrow-{to}   '></i>" + self.ins._langs._get("add_back_list")},
                {"_type": "ul", "end": True},
                {"end": True}
            ], "class": "ins-button  "}]
        
      
            
        if type(self.ops._form_actions) is list and len( self.ops._form_actions ) >0:
                  action_menu =self.ops._form_actions

        
        header = [
            {"start": "true", "class": "ins-col-grow  ins-padding-m  ins-flex-center"},




            {"start": True,  "class": "    ins-col-12 -header-searh-group  ins-group ins-flex  "},


            {"_data": [{"class": "lni ins-icon lni-plus  ins-padding-s"},
                       {"_data":  self.ins._langs._get("new_item_title"), "type": "span"}],
             "class": "ins-radius-xl  ins-strong-l  ins-gap-o ins-title-xs   ins-flex-grow"},



            {"style": "width:75px", "_type": "a", "href": back_url, "_data": [
                {"class": f"lni ins-icon  lni-arrow-{to}  ins-padding-s"},
                {"_data": self.ins._langs._get("back"),
                 "class": "ins-flex-grow ins-font-s  ins-strong-m"}
            ], "class": "ins-button ins-gap-o ins-flex  "},
            {"style": "width:4px ;    height: 18px;",
             "class": f"ins-border ins-border-left    "},


        ]
        if self.ops._form_actions !=False :
            header += action_menu
        header += [{"end": True}, {"end": "true"}]

        self.ins._tmp._set_page_des(self.ins._ui._render(header))

        f_start = [

            {"_type": "form", "method": "post",
             "class": "ins-col-12 crud-form-body  ", "start": True},
        ]

        ui += f_start

        f_end = [{"class": "ins-col-12  insaction  ins-flex-center ", "data-insaction": "plgin",  "data-plgin": "ins_plg_py_crud",
                  "style": "    margin-top: 16px;", "start": True}]

        ui += f_end

        ui += self.ops._form_data
        m = self.ins._server._get("mode")

        if self.get["mode"] == "edit":
            if self.ops._form_edit_append != None:
                ui += self.ops._form_edit_append()
        else:
            if self.ops._form_add_append != None:
                ui += self.ops._form_add_append()

        f_end = [
            {"_type": "input", "type": "hidden",
                "value": self.ops._table, "name": "tb"},
            {"_type": "input", "type": "hidden", "value": m, "name": "m"},
            #  {"_type": "input", "type": "hidden", "value": self.ops._table,"name": "tb"},
            {"end": True},
            {"_type": "form", "end": True},

        ]
        ui += f_end
        return self.ins._ui._render(ui)

    def render(self):
        self.__db_actions()

        ps = self.ins._server._post()
        if "reaction" in ps and ps["reaction"] == "_tobak":
            back_url = self.ins._server._url({}, remove=["mode", "id"])
            return f"<div>loading....</div> <meta http-equiv='refresh' content='1; url={back_url}' />"
        return self. __form()
