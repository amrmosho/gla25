from ins_kit._engine._bp import App


class AppUserCustom(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _get_custom_per_delete(s):
        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        np = s.ins._json._decode(d["custom_permissions"])
        tmp = []
        for n in np:
            if req["mid"] != n["id"]:
                tmp.append(n)

        nd = {"custom_permissions": s.ins._json._encode(tmp)}
        d = s.ins._db._update("kit_user_group", nd, f"id={req["gid"]}")
        return s._get_custom_per()

    def _get_custom_per_update(s):

        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        if d["custom_permissions"] == "":
            d["custom_permissions"] = "[]"

        np = s.ins._json._decode(d["custom_permissions"])
        if req["mid"] == "-1":

            np.append(
                {"name": req["name"], "level": str(req["level"]), "id": s.ins._data.unid})
        else:

            for n in np:
                if n["id"] == req["mid"]:
                    n["name"] = req["name"]
                    n["level"] = req["level"]

        nd = {"custom_permissions": s.ins._json._encode(np)}
        d = s.ins._db._update("kit_user_group", nd, f"id={req["gid"]}")

        return s._get_custom_per()

    def _get_custom_per_edit_ui(my):
        req = my.ins._server._req()
        d = my.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        np = my.ins._json._decode(d["custom_permissions"])

        t = {}
        for n in np:
            if req["mid"] == n["id"]:
                t = n

            t["mode"] = "Update"
        return my._get_custom_per_ui(t)

    def _get_custom_per_ui(self, data: dict = {}):
        req = self.ins._server._req()

        ui = [
            {"start": "true", "class": "ins-col-12 ins-flex-center ins-margin-xl  -custom-per-ui-cont  ins-margin-v  ins-padding-xl  "},
            {"_type": "input", "title": "name",
                "name": "name", "value": data.get("name", ""), "pclass": "ins-col-12"},
            {"_type": "input", "title": "Level", "value": data.get("level", "0"), "type": "number",
                "name": "level", "pclass": "ins-col-12"},
            {"_type": "input", "type": "hidden", "value": req["gid"],
                "name": "gid", "pclass": "ins-hidden"},

            {"_type": "input", "type": "hidden", "value": req.get("mid", "-1"),
                "name": "mid", "pclass": "ins-hidden"},

            {"class": "ins-line ins-col-12"},
            {"_data": data.get(
                "mode", "Add"), "class": "ins-col-12 ins-button -custom-per-ui-add-btn ins-primary"},
            {"end": "true"},
            {"end": "true"}]

        return self.ins._ui._render(ui)

    def _get_custom_per(s):
        req = s.ins._server._req()
        d = s.ins._db._get_row("kit_user_group", "*", f"id={req["gid"]}")
        ui = [{"start": "true", "class": "ins-col-12 ins-flex ins-margin-xl   ins-margin-v  ins-padding-xl  "}]
        
        
        if d["custom_permissions"] == "" or   d["custom_permissions"] == "[]" :
            ui.append({"_data": "No Data :)",
                      "class": "ins-col-12 ins-message ins-warning"})
            ui.append({"end": "true"})
            return s.ins._ui._render(ui)
        
        np = s.ins._json._decode(d["custom_permissions"])
        for a in np:
            row = [
                {"start": "true", "class": "ins-col-12 ins-flex  ins-card  ins-border ins-padding-xl"},
                {"_data": a["name"], "class": "ins-col-grow"},
                {"_data": a["level"], "class": "ins-col-4"},
                {"_data": '<i class="lni  lni-xmark"></i>', "data-mid": a["id"], "data-gid": req["gid"],
                    "style": "width:50px", "class": "ins-button-text -custom-per-item-delete"},
                {"_data": '<i class="lni lni-pencil-1"></i>',
                    "style": "width:50px", "data-mid": a["id"], "data-gid": req["gid"], "class": "ins-button-text -custom-per-item-edit"},
                {"end": "true"}

            ]
            ui += row

        ui.append({"end": "true"})

        return s.ins._ui._render(ui)