from ins_kit._ui.ui import Ui


class PlgInput(Ui):

    def _json(self, ops: dict):

        id = f"_{self.ins._data.unid}"
        ui = [
            {"start": "true", "data-id": id, "style": "width:100%;height:250px",  "data-insaction": 'plgin',
             "data-plgin": 'ins_plg_json_editor',
                "class": "ins-col-12 insaction ins-code-editor  ins-flex"},
            {"_type": "textarea", "name": ops["name"], "_data": ops.get("value", "{}"),
                "type": "textarea", "id": f"{id}_textarea",
                "clean": "true",

                "class": "ins-form-upload-input"},
            {"end": "true"}

        ]

        return ui

    def _upload(self, ops: dict):

        v = ""
        id = "_" + self.ins._data._unid
        if "value" in ops:

            v = self.ins._map.UPLOADS_FOLDER + ops.get("value", "")




        tar = {
            "_trans": "true",
            "data-plgin": "ins_plg_py_form_image",
            "data-p": id,
            "clean": "true", "style": 'line-height: 40px;',
            "class": " lni lni-upload-1 ins-primary-color ins-form-upload-btn  ins-font-l  ins-form-upload-input"}

        if "nojs" not in ops:
            tar["data-insaction"] ="plgin"
            tar["data-plgin"] ="ins_plg_py_form_image"
            tar["class"] +=" insaction "


        if "class"  in ops:
            tar["class"] += " " +ops["class"] +" "
            
            

        if "_mode" in ops:
            tar["data-mode"] = ops["_mode"]

        if "_dir" in ops:
            tar["data-_dir"] = ops["_dir"]
        if "_exts" in ops:
            tar["data-_exts"] = ops["_exts"]
        if "_size" in ops:
            tar["data-_size"] = ops["_size"]
        vals = {}
        row = []

        if ("value" in ops):
            if "_mode" in ops and ops["_mode"] == "multi":
                vls = ops["value"].split(",")

                for v in vls:
                    if v != "":

                        row.append(
                            {"start": "true", "class": "-img-cont ins-flex-center", "draggable": "true"})
                        row.append(
                            {"data-p": v,   "class": "lni lni-xmark  ins-rounded ins-danger    ins-button-text -img-remove"})

                        row.append({"_type": "a", "href": self.ins._map.UPLOADS_FOLDER + v, "target": "_black",
                                   "class": "lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link"})

                        row.append(
                            {"data-p": v,  "class": "lni lni-menu-meatballs-1  ins-rounded   ins-dark  -img-darg"})

                        row.append({"_type": "img",
                                    "src": self.ins._map.UPLOADS_FOLDER + v})
                        row.append({"end": "true"})

            else:
                row = [

                    {"start": "true", "class": "-img-cont ins-flex-center"},
                    {"data-p": ops["value"],   "class": "lni lni-xmark  ins-rounded ins-danger    ins-button-text -img-remove"},
                    {"_type": "a", "href": self.ins._map.UPLOADS_FOLDER +
                        ops["value"], "target": "_black",   "class": "lni lni-link-2-angular-right ins-rounded ins-dark   ins-button-text -img-link"},
                    {"_type": "img",
                        "src": self.ins._map.UPLOADS_FOLDER + ops["value"]},
                    {"end": "true"}


                ]

        ui = [
            {"start": "true", "data-id":id, "class": f"ins-col-12 {id} ins-form-input  ins-flex-end ins-form-upload-imgs-cont"},
            {"start": "true", "class": "ins-col-grow ins-form-upload-imgs ins-flex-center"}
        ]
        ui += row

        ui.append({"end": "true"})
        ui.append(tar)
        ui.append({"_type": "input", "name": ops["name"], "value": ops.get("value", ""),
                   "type": "hidden", "clean": "true",  "class": "ins-form-upload-input ins-hidden"})
        ui.append({"end": "true"})

        return ui

    def _bool(self, ops: dict):
        if "name" not in ops:
            ops["name"] = "_" + self.ins._data._unid

        chk = {"_type": "input",  "type": "checkbox",
               "value": ops["value"], "clean": "true", "class": "ins-form-bool-f"}

        if "value"not in ops:
            ops["value"] = "0"

        elif str(ops["value"]) == "1":
            chk["checked"] = "true"

        inpb = {"_type": "input", "name": ops["name"], "value": ops["value"],
                "type": "hidden", "clean": "true",  "class": "ins-form-checkbool"}

        for k, v in ops.items():
            if "data-" in k:
                chk[k] = v
            elif "class" == k:
                chk["class"] += f" {ops[k]} "

        ui = [
            {"_type": "label",  "start": True},
            chk, inpb,

            {"_type": "label",  "end": True}
        ]
        return ui

    @property
    def _n(self):
        return self.ins._data.__qualname__

    def auto_select(self, ops: dict):
        if "name" not in ops:
            ops["name"] = "_" + self.ins._data._unid

        ui = [



            {"class": f" -auto-list-cont-inp insaction",  "data-insaction": 'plgin',
                "data-plgin": 'ins_plg_py_input_select_auto',  "start": True},

            {"_type": "input", "name": ops.get("name"),  "value": ops.get(
                "value", ""), "clean": "true",  "class": " -auto-list-input-inp  ins-hidden"},


            {"class": f"{ops["name"]}_auto_list -auto-list-label-inp ins-border ins-form-input ins-flex", "start": True},

            {"_type": "input",  "class": "ins-col-grow -auto-list-value-inp ins-input-none",
                "style": 'width:auto', "clean": "true"},
            {"class": "   -auto-list-show-btn ins-icon   ins-font-xl  lni lni-chevron-down"},

            {"end": True},
            {"_type": "ul",
                "class": f"{ops["name"]}_auto_list -auto-list-inp ins-border ins-flex", "start": True},
        ]

        ops = self.ins._data_collect._render(ops)

        for k, v in ops["fl_data"].items():
            cls = ""
            if "value" in ops and str(ops["value"]) == str(k):
                cls = "-set-selected"

            ui.append({"_type": "li", "data-value": k,
                      "class": f"ins-col-12 {cls} ins-vis", "_data": v})

        ui.append({"_type": "ul", "end": True})
        ui.append({"end": True})

        return ui

    def _auto(self, ops: dict):
        if "name" not in ops:
            ops["name"] = "_" + self.ins._data._unid

        ui = [
            {"_type": "input", "name": ops.get("name"), "list": f"{
                ops["name"]}_list",  "value": ops.get("value", ""), "clean": "true",  "class": ""},
            {"_type": "datalist", "id": f"{ops["name"]}_list", "start": True},
        ]

        ops = self.ins._data_collect._render(ops)

        for k, v in ops["fl_data"].items():
            ui.append({"_type": "option", "value": v})

        ui.append({"_type": "datalist", "end": True})

        return ui

    def _multi(self, ops: dict):
        if "name" not in ops:
            ops["name"] = "_" + self.ins._data._unid

        ii = {"_type": "input", "placeholder": "Add new Item", "list": f"{ops["name"]}_list",
              "name": f"{ops["name"]}_adder",  "clean": "true",  "class": "ins-col-grow  ins-input-none ins-input-adder", "style": "width:auto"}

        if "data" in ops:
            ii["list"] = f"{ops["name"]}_list"

        ui = [


            {"data-insaction": 'plgin',
                "data-plgin": 'ins_plg_input_multi',    "start": True, "class": " insaction  ins-flex"},
            {"start": True, "class": " ins-input-cont ins-flex  ins-form-input  ins-col-12"},
            ii,
            {"end": True},
            {"_type": "input", "name": f"{ops["name"]}",  "clean": "true",
                "class": " ins-input  ins-hidden", "pclass": ""},




        ]

        ui.append(
            {"_type": "datalist", "id": f"{ops["name"]}_list", "start": True})

        ops = self.ins._data_collect._render(ops)

        for k, v in ops["fl_data"].items():
            ui.append({"_type": "option", "value": v})

        ui.append({"_type": "datalist", "end": True})

        ui.append({"end": True})

        return ui

    def __input(self, ops: dict):

        if "type" not in ops:
            ops["type"] = "text"

        if ops["type"] == "textarea":
            inp = {"_type": "textarea",  "not_plgin": True}

        elif ops["type"] == "bool":
            inp = self._bool(ops)
        elif ops["type"] == "auto":
            inp = self._auto(ops)
        elif ops["type"] == "auto_select":
            inp = self.auto_select(ops)
        elif ops["type"] == "multi" or ops["type"] == "tags":
            inp = self._multi(ops)

        elif ops["type"] == "json":
            inp = self._json(ops)
        elif ops["type"] == "upload":
            inp = self._upload(ops)

        else:
            inp = {"_type": "input",  "not_plgin": True}

        del ops["_type"]
        if type(inp) == dict:
            for k, v in ops.items():
                inp[k] = v

        #

        addcls = " ins-form-input "

        if type(inp) == dict and "class" not in inp:
            inp["class"] = addcls
        elif type(inp) == dict:
            inp["class"] += addcls

        return inp

    def container(self, ops):

        con: list = []

        """*---------- load widgets  data*"""

        m = ""

        if "type" in ops:
            m = f" ins-form-{ops["type"]}-cont "

            if "_lang" in ops:

                if "_end" in ops:
                    ops["_end"] += f"<i data-o='{ops.get('_table', "")}' data-i='{self.ins._server._get("id", "")}'   data-n='{
                        ops['name']}' class='lni lni-globe-1 ui-input-lang-ui  ins-button-text' style='width:auto'></i>"
                else:
                    ops["_end"] = f"<i data-o='{ops.get('_table', "")}' data-i='{self.ins._server._get("id", "")}'   data-n='{
                        ops['name']}' class='lni lni-globe-1 ui-input-lang-ui ins-button-text' style='width:auto'></i>"

        if "_start" in ops:
            m += " ins-form-item-hasstart "

        if "_end" in ops:
            m += " ins-form-item-hasend "

        p = {"class": f"ins-form-item ins-flex {m}", "start": True}

        if "pstyle" in ops:
            p["style"] = ops["pstyle"]
            del ops["pstyle"]

        if "pclass" in ops:
            p["class"] += " "+ops["pclass"]
            del ops["pclass"]

        con.append(p)
        lab = {}
        """*---------- load widgets  data*"""
        if "title" in ops:
            lab = {"class": "ins-form-label", "_data": ops["title"]}

        if "_title" in ops:
            lab = {"class": "ins-form-label", "_data": ops["_title"]}

        if "label_style" in ops:
            lab["style"] = ops["label_style"]

        if "label_class" in ops:
            lab["class"] += " " + ops["label_class"]
        if len(lab) > 0:
            con.append(lab)
        """*---------- load widgets  data*"""

        m = ""
        if "_start" in ops:
            sta = {"_data": ops["_start"],
                   "class": "ins-text ins-form-start", "_type": "span"}
            if "label_style" in ops:
                sta["style"] = ops["label_style"]

            if "label_class" in ops:
                sta["class"] += " " + ops["label_class"]

        if "_end" in ops:
            en = {"_data": ops["_end"],
                  "class": "ins-text ins-form-end", "_type": "span"}
            if "label_style" in ops:
                en["style"] = ops["label_style"]

            if "label_class" in ops:
                en["class"] += " " + ops["label_class"]
        mc = ""
        if "_end" in ops or "_start" in ops:
            mc = "ins-form-input"

        val = {"class":  "ins-form-value "+mc,
               "start": "true"}

        if "_data" in ops and "_start" not in ops and "_end" not in ops:
            val["_data"] = ops["_data"]

        if "value_style" in ops:
            val["style"] = ops["value_style"]

        if "value_class" in ops:
            val["class"] += " " + ops["value_class"]

        con.append(val)

        if "_start" in ops:
            con.append(sta)
            con.append({"class":  "  ins-form-input-cont ",
                       "_data":  ops["_data"]})

        if "_end" in ops:
            con.append({"class":  "   ins-form-input-cont ",
                       "_data":  ops["_data"]})
            con.append(en)

        val_end = {"end": "true"}
        con.append(val_end)

        """*---------- load widgets  data*"""
        con.append({"end": True})

        return self._render(con)

    def __ui(self, ops):

        inp = self.__input(ops)
        if "clean" in ops and ops["clean"] == "true":
            if type(inp) == dict:
                return self._render([inp])
            else:
                return self._render(inp)
        ops["_data"] = inp
        return self.container(ops)

    def render(self, ops):

        return self.__ui(ops)
