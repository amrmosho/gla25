from ins_kit._engine._bp import App


class AjxTags(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def __tags(self, id=""):
        tgs = self.ins._db._get_data("kit_tags", "*")
        if id == "":
            return tgs
        else:
            for tg in tgs:
                if str(tg["id"]) == id:
                    return tg

    def save(self):
        ps = self.ins._server._post()
        db_data = ps
        self.ins._db._insert("kit_tags", db_data)
        return self.ui()

    def add(self):
        ps = self.ins._server._post()

        uidata = [

            {"start": "true", "class": "ins-flex ins-padding-2xl"},


            {"start": "true", "class": "ins-flex  ins-padding-m ins-border ins-radius-l ins-bg-2 ins-col-12"},
            {"_data": '<i class="lni ins-icon lni-plus"></i>'"Add New Tag",
                "class": "ins-col-grow ins-strong ins-title-s"},

            {"_data": "back", "data-obj": ps["obj"], "data-oid": ps["oid"],
                "class": "ins-button  ch-tag-item-back"},

            {"_data": "Save", "data-obj": ps["obj"], "data-oid": ps["oid"],
                "class": "ins-button ins-primary ch-tag-item-save"},

            {"end": "true"},


            {"start": "true", "class": "ins-flex ins-col-12 ch-tag-item-add-area ins-padding-m ins-card ins-border"},



            {"_type": "input","class": "ch-tag-item-title", "name":"title", "type":"text","title": "Tage name",
                      "pclass": "ins-col-12"},
            
            
                {"_type": "input","class": "ch-tag-item-title","name":"color", "type":"color", "title": "Tage Color",
                      "pclass": "ins-col-12"},
                
                {"_type": "input","value": ps["obj"],"name":"obj", "type":"hidden" ,
                      "pclass": "ins-col-grow"},
                
                                {"_type": "input", "type":"hidden","value": ps["oid"],"name":"oid", 
                      "pclass": "ins-col-grow"},
                
                
            {"end": "true"},



        ]

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)

        return "AjxTags"

    def remove(self):
        ps = self.ins._server._post()
        self.ins._db._delete("kit_tags", f"id={ps["mid"]}")
        return self.ui()

    def oui(self):
        rq = self.ins._server._req()
        ps = self.ins._server._post()
        v = self.ins._db._get_row(
            ps["obj"], "*", f"  id='{ps["oid"]}'")
        tg = ""

        if v["kit_tags"] != "":
            tgs = v["kit_tags"].split(",")
            for t in tgs:
                db_tg = self.__tags(t)
                area = self.ins._eng._areas(rq["_area"])["url"]
                turl = self.ins._server._url({"area": area, "alias": rq["_alias"], "f": f"tag={
                                             db_tg["id"]}"}, ["id", "mode"])
                tg += f"<b style='background:{db_tg["color"]}' class='ins-tag ins-flex-center ins-text-center '><span class='app-crud-list-remove-tag-actions ins-flex-center'><a class='ins-button-text' href='{
                    turl}'><i class='lni ins-font-l  lni-search-text'></i> </a><i data-oid='{v["id"]}'  data-mid='{db_tg["id"]}' data-obj='{ps["obj"]}'   class='lni ins-button-text-danger  ins-font-l  app-crud-list-remove-tag lni-xmark'></i></span> {db_tg["title"]}</b>"

        mclass = f"_{ps["obj"]}_{ps["oid"]}_tags"
        rv = f"<div class='ins-flex ins-k-tags-area {mclass}  ins-col-12'><i   data-oid='{ps["oid"]}' data-obj='{
            ps["obj"]}' class='lni ins-button-text app-crud-list-add-tag  lni-bookmark-circle'></i>{str(tg)}</div>"

        return rv

    def update(self):
        ps = self.ins._server._post()

        data = self.ins._db._get_row(
            ps["obj"], "*", f"  id='{ps["oid"]}'")
        kit_tags = []
        if data["kit_tags"] != "":
            kit_tags = data["kit_tags"].split(",")

        if ps["st"] == "1":
            if str(ps["mid"]) not in kit_tags:
                kit_tags.append(ps["mid"])

        if ps["st"] == "0":
            if str(ps["mid"]) in kit_tags:
                kit_tags.remove(ps["mid"])

        str_tags = ",".join(kit_tags)

        data = self.ins._db._update(
            ps["obj"], {"kit_tags": str_tags}, f"  id='{ps["oid"]}'")

        return self.oui()

    def ui(self):
        rq = self.ins._server._req()
        ps = self.ins._server._post()

        uidata = [{"start": "true", "class": "ins-flex ins-padding-2xl"}]

        saerch = [

            {"start": "true", "class": "ins-flex  ins-padding-m ins-border ins-radius-l ins-bg-2 ins-col-12"},
            {"_type": "input", "type":"search", "placeholder": "search....", "class":"ch-tag-search-inp", "pclass": "ins-col-grow "},
            {"_data": "add", "data-obj": ps["obj"], "data-oid": ps["oid"],
                "class": "ins-button ins-primary ch-tag-item-add"},

            {"end": "true"}
        ]

        uidata += saerch
        tags = self.ins._db._get_data(
            "kit_tags", "*", f"obj='' or  obj='{ps["obj"]}'")

        data = self.ins._db._get_row(
            ps["obj"], "*", f"  id='{ps["oid"]}'")
        kit_tags = []
        if data["kit_tags"] != "":
            kit_tags = data["kit_tags"].split(",")

        for t in tags:
            v = "0"
            if str(t["id"]) in kit_tags:
                v = "1"

            area = self.ins._eng._areas(rq["_area"])["url"]

            turl = self.ins._server._url(
                {"area": area, "alias": rq["_alias"], "f": f"tag={t["id"]}"}, ["id", "mode"])
            acs = f"<div class='ins-flex'><a href='{
                turl}'><i class=' lni lni-search-text'></i></a>"

            if t["obj"] != "":
                acs += f"<i  data-mid='{t["id"]}' data-obj='{ps["obj"]}' data-oid='{
                    ps["oid"]}' class=' lni ins-button-text ch-tag-item-remove lni-xmark'></i>"
                acs += "<i class=' lni lni-map-pin-5'></i>"

            acs += "</div>"

            row = [{"_type": "input", "value":  v, "class": "ch-tag-item",
                    "name": f"_{t["id"]}", "data-mid": t["id"], "data-oid": ps["oid"], "data-obj": ps["obj"], "data-mid": t["id"],
                    "type": "bool", "pclass": "ins-col-12 ch-tag-item-cont", "_end": f"<div class='ins-flex'><span style='width:10px;height:25px;border-radius: 5px;background:{t["color"]}'></span> <span class='ins-col-grow ins-text-start'>{t["title"]}</span> {acs} </div>"}]
            uidata += row

        uidata.append({"end": "true"})

        return self.ins._ui._render(uidata)

    def out(self):
        return "AjxTags"
