from ins_kit._engine._bp import App


class AppUserApps(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _get_menus(s, menu=""):
        ds = s.ins._db._get_data("kit_menu_item", "*",
                                 f"fk_menu_id='{menu}'")
        r = ""
        for d in ds:
            r += f"<option value='{d["id"]}'>{d["title"]}</option>"
        return r

    def _get_menus_update(s, menu="", value=""):
        ds = s.ins._db._get_data("kit_menu_item", "*",
                                 f"fk_menu_id='{menu}'")
        r = []
        for d in ds:
            ro = {"value": d["id"], "text": d["title"]}
            if d["id"] == value:
                ro["selected"] = "true"
            r.append(ro)
        return r

    def _get_apps_get_apps(s):
        req = s.ins._server._req()
        return s._get_menus(req["_v"])

    def _get_apps_per_delete(s):
        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        np = s.ins._json._decode(d["apps_permissions"])
        tmp = []
        for n in np:
            if req["mid"] != n["id"]:
                tmp.append(n)

        nd = {"apps_permissions": s.ins._json._encode(tmp)}
        d = s.ins._db._update("kit_user_group", nd, f"id={req["gid"]}")
        return s._get_apps_per()

    def _get_apps_per_update(s):

        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        if d["apps_permissions"] == "":
            d["apps_permissions"] = "[]"

        np = s.ins._json._decode(d["apps_permissions"])
        if req["mid"] == "-1":
            np.append(
                {"menu": str(req["menu"]), "app": str(req["app"]),  "add": str(req["add"]), "edit": str(req["edit"]), "delete": str(req["delete"]), "level": str(req["level"]), "id": s.ins._data.unid})
        else:

            for n in np:
                if n["id"] == req["mid"]:
                    n["app"] = req["app"]
                    n["add"] = req["add"]
                    n["edit"] = req["edit"]
                    n["delete"] = req["delete"]
                    n["menu"] = req["menu"]
                    n["level"] = req["level"]

        nd = {"apps_permissions": s.ins._json._encode(np)}
        d = s.ins._db._update("kit_user_group", nd, f"id={req["gid"]}")

        return s._get_apps_per()

    def _get_apps_per_edit_ui(my):
        req = my.ins._server._req()
        d = my.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        np = my.ins._json._decode(d["apps_permissions"])

        t = {}
        for n in np:
            if str(req["mid"]) == str(n["id"]):
                t = n
                
        t["mode"] = "Update"
        t["menu_data"] = my._get_menus_update(t["menu"], t["app"])
        return my._get_apps_per_ui(t)

    def _get_apps_per_ui(self, data: dict = {}):
        req = self.ins._server._req()
        _app :dict = {"_type": "select", "title": "menu",
             "name": "app",  "pclass": "ins-col-12"}
        if "menu_data" in data:
            _app["_data"] = data["menu_data"]

        if "app" in data:
            _app["value"] = data["app"]
            
            
        ui = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-margin-xl  -apps-per-ui-cont ins-margin-v  ins-padding-xl  "},
            {"_type": "select", "fl_type": "db", "fl_table": "kit_menu", "title": "menu",
                "name": "menu", "value": data.get("menu", "0"), "pclass": "ins-col-12"}, _app,

            {"_type": "input", "title": "level", "type": "number",
                "name": "level", "value": data.get("level", "0"), "pclass": "ins-col-12"},
            {"_type": "input", "type": "bool", "_end": "Edit", "value": data.get("edit", "1"),
                "name": "edit", "pclass": "ins-col-4"},
            {"_type": "input", "type": "bool", "_end": "Add", "value": data.get("add", "1"),
             "name": "add", "pclass": "ins-col-4"},
            {"_type": "input", "type": "bool", "_end": "Delete", "value": data.get("delete", "1"),
             "name": "delete", "pclass": "ins-col-4"},
            {"_type": "input", "type": "hidden", "value": req["gid"],
                "name": "gid", "pclass": "ins-hidden"},
            {"_type": "input", "type": "hidden", "value": req.get("mid", "-1"),
                "name": "mid", "pclass": "ins-hidden"},
            {"class": "ins-line ins-col-12"},
            {"_data": data.get(
                "mode", "Add"), "class": "ins-col-12 ins-button -apps-per-ui-add-btn ins-primary"},
            {"end": "true"},
            {"end": "true"}]

        return self.ins._ui._render(ui)

    def _y(s, v):
        return "<i class='lni lni-checkmark'></i>" if str(v) == "1" else "<i class='lni  lni-xmark'></i>"

    def _get_apps_per(s):
        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")

        ui = [{"start": "true", "class": "ins-col-12 ins-flex ins-margin-xl   ins-margin-v  ins-padding-xl  "},
              {"start": "true", "class": "ins-col-12 ins-flex  ins-card  ins-border ins-padding-xl"},
              {"_data": "App", "class": "ins-col-grow ins-title-m"},
              {"_data": "level", "style": "width:100px", "class": "ins-title-m"},
              {"_data": "add", "style": "width:100px", "class": "ins-title-m"},
              {"_data": "edit", "style": "width:100px", "class": "ins-title-m"},
              {"_data": "delete", "style": "width:120px", "class": "ins-title-m"},
              {"_data": 'Actions',  "style": "width:100px", "class": "ins-title-m"}, {"end": "true"}]

        if d["apps_permissions"] == "" or d["apps_permissions"] == "[]":
            ui.append({"_data": "No Data :)",
                      "class": "ins-col-12 ins-message ins-warning"})
            ui.append({"end": "true"})
            return s.ins._ui._render(ui)

        np = s.ins._json._decode(d["apps_permissions"])

        for a in np:

            app = s.ins._db._get_row(
                "kit_menu_item", "title", f"id={a["app"]}")

            row = [
                {"start": "true", "class": "ins-col-12 ins-flex  ins-card  ins-border ins-padding-xl"},
                {"_data": app["title"], "class": "ins-col-grow"},
                {"_data": a["level"], "style": "width:100px"},
                {"_data": s._y(a["add"]), "style": "width:100px"},
                {"_data": s._y(a["edit"]), "style": "width:100px"},
                {"_data": s._y(a["delete"]), "style": "width:120px"},
                {"_data": '<i class="lni  lni-xmark"></i>', "data-mid": a["id"], "data-gid": req["gid"],
                    "style": "width:50px", "class": "ins-button-text -app-per-item-delete"},
                {"_data": '<i class="lni lni-pencil-1"></i>',
                    "style": "width:50px", "data-mid": a["id"], "data-gid": req["gid"], "class": "ins-button-text -app-per-item-edit"},
                {"end": "true"}
            ]
            ui += row
        ui.append({"end": "true"})

        return s.ins._ui._render(ui)
