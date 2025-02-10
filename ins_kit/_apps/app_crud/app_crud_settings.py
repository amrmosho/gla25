from ins_kit._apps.app_crud.app_crud_parent import appCrudParent
class APPCRUDSettings(appCrudParent):
    def __init__(self, P) -> None:
        super().__init__(P)
    def ui(self):

        tmps = {"default": "Default", "new": "new"}
        uidata = [{"start": True, "data-insaction": "plgin",
                   "data-plgin": "ins_plg_py_crud_settings", "class": "ins-flex insaction ins-col-12"}]
        uidata.append({"start": True, "class": " ins-flex-end ins-col-12"})
        
        back_url = self.ins._server._url({},remove=["mode", "id"])

        to ="left"
        if self.ins._this._lang["direction"] =="rtl":
            to ="right"
        uidata.append(             {"style": "width:100px", "_type": "a", "href": back_url, "_data": [
                    {"class": f"lni ins-icon  lni-arrow-{to}  ins-padding-s"},
                    {"_data": self.ins._langs._get("back"),
                     "class": "ins-flex-grow ins-font-s  ins-strong-m"}
                ], "class": "ins-button ins-gap-o ins-flex  "});

        uidata.append({ "class": "ins-col-grow "})


        uidata.append({"start": True, "class": "ins-buttons-group "})
        

        uidata.append({"_type": "select", "name": "tm", "_data": tmps,
                      "style": "width:300px", "class": " crd-set-update-lists-slct "})
        uidata.append({"data-o": self.ops._table, "_data": '<i class="lni  ins-icon lni-check"></i> Active',
                      "style": "width:130px", "class": " crd-set-update-defa-btn   "})
        uidata.append({"data-o": self.ops._table, "_data": '<i class="lni  ins-icon lni-file-multiple"></i> duplicate',
                      "style": "width:150px", "class": "crd-set-update-dupl-btn  "})
        uidata.append({"data-o": self.ops._table, "_data": '<i class="lni  ins-icon lni-file-xmark"></i> delete',
                      "style": "width:130px", "class": "crd-set-update-del-btn "})
        uidata.append({"data-o": self.ops._table, "_data": '<i class="lni  ins-icon lni-floppy-disk-1"></i> Update',
                      "style": "width:130px", "class": " crd-set-update-data-btn  ins-primary "})
        uidata.append({"end": True})
        uidata.append({"end": True})
        uidata.append({"start": True, "class": "ins-card ins-flex",
                      "style": "width: 250px;min-height: calc(100vh - 200px);"})
        uidata.append({"_data": '<i class="lni lni-database-2 ins-icon"></i> Data', "data-g": "data",
                      "class": "ins-col-12 ins-padding-m ins-button-text crd-set-update-btn   ins-active  ins-radius-m"})
        uidata.append({"_data": '<i class="lni lni-agenda ins-icon"></i> List',
                       "data-g": "list",
                      "class": "ins-col-12 ins-padding-m ins-button-text  crd-set-update-btn ins-radius-m"})
        uidata.append({"_data": '<i class="lni lni-search-text ins-icon"></i> '+self.ins._langs._get("filter", "crud"),
                       "data-g": "filter",
                      "class": "ins-col-12 ins-padding-m  ins-button-text   crd-set-update-btn ins-radius-m"})
        uidata.append({"_data": '<i class="lni lni-pen-to-square ins-icon"></i> Form',
                       "data-g": "form",
                      "class": "ins-col-12 ins-padding-m  ins-button-text   crd-set-update-btn ins-radius-m"})
        if "more" in self.ops._crud_setting:
            for a in self.ops._crud_setting["more"]:
                uidata.append({"_data": f'<i class="lni lni-pencil-1 ins-icon"></i> {a["title"]}',
                               "data-g": "more",
                               "data-i": a["id"],
                               "class": "ins-col-12 ins-padding-m ins-button-text crd-set-update-btn  ins-radius-m"})
        if "options" in self.ops._crud_setting:
            for a in self.ops._crud_setting["options"]:
                uidata.append({"_data": f'<i class="lni lni-gear-1 ins-icon"></i> {a["title"]}',
                               "data-g": "opss", "data-i": a["id"],
                               "class": "ins-col-12 ins-padding-m ins-button-text crd-set-update-btn  ins-radius-m"})
        uidata.append({"_data": '<i class="lni lni-gears-3 ins-icon"></i> Settings', "data-g": "set",
                      "class": "ins-col-12 ins-padding-m  ins-col-12 ins-padding-m ins-button-text crd-set-update-btn    ins-radius-m"})
        uidata.append({"end": True})
        uidata.append({"_data": "", "data-o": self.ops._table, 
                       "data-u": self.ops._url,
                       "data-p": self.ops._pros_name, "data-t": "data", "class": "ins-col-grow crd-set-data-area ins-bg ins-border ins-radius-m",
                      "style": "min-height: calc(100vh - 200px);"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r
    def render(self):
        return self.ui()
