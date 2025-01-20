from ins_kit._engine._bp import App


class AjxCrudSetting(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    @property
    def k(self):
        return "crud"


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

    def sets(self):
        p = self.ins._server._post()
        name = p["o"]

        s = self.csets(name)
        return s[self.k].get(p["list_name"], {})

    def pros(self, get=""):
        p = self.ins._server._post()
        r = self._pros(p["p"], p["u"])
        if get != "":
            return r[get]
        return r

    def more(self):
        p = self.ins._server._post()
        r = self.pros()
        ths = []
        if "crud_setting" not in r:
            return ""
        if "more" not in r["crud_setting"]:
            return ""
        ms = r["crud_setting"]["more"]
        for m in ms:
            if m["id"] == p["i"]:
                ths = m
        return self.ins._ui._render(ths["data"])


    def data(self):
        st = self.sets()
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]

        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "query", ""), "name": "query",  "pclass": "ins-col-12", "title": "Query"})
        uidata.append({"_type": "input", "type": "number", "value": st.get(
            "pg_count", "6"), "name": "pg_count",  "pclass": "ins-col-12", "title": "Page Count limit"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def list(self):
        st = self.sets()
        sta = self.pros("list_data")
        if "list_data" not in st or st["list_data"] == "":
            st["list_data"] = self.ins._json._encode(sta, True)
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]
        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "list_data", ""), "name": "list_data",  "pclass": "ins-col-12", "style": "height:600px", "title": "List"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def filter(self):
        st = self.sets()
        sta = self.pros("list_filter")
        if "list_filter" not in st or st["list_filter"] == "":
            st["list_filter"] = self.ins._json._encode(sta, True)
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]
        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "list_filter", ""), "name": "list_filter",  "pclass": "ins-col-12", "style": "height:600px",  "title": "Filter"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def form(self):
        st = self.sets()
        sta = self.pros("form_data")
        if "form_data" not in st or st["form_data"] == "":
            st["form_data"] = self.ins._json._encode(sta, True)
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]
        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "form_data", ""), "name": "form_data",  "pclass": "ins-col-12", "style": "height:600px",  "title": "Form"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def opss(self):
        p = self.ins._server._post()
        a = self.ins._data._get_options(p["i"], True)
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]
        uidata.append({"_type": "input", "type": "textarea", "_data": a.get(
            "content", ""), "name": "options",  "data-i": p["i"], "pclass": "ins-col-12", "style": "height:600px",  "title": "filter"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def get_list_names(self):
        p = self.ins._server._post()
        name = p["o"]
        s = self.csets(name)

        r = ""
        if self.k not in s:
            return "<option value='defualt'>Defualt</option>"
        for l in s[self.k]:
            t = s[self.k][l]["for"] + " / " + s[self.k][l]["title"]
            if "insact" in s[self.k][l] and s[self.k][l]["insact"] == "1":
                t += " (Active)  "

            r += f"<option value='{l}'>{t}</option>"
        if r == "":
            r = "<option value='defualt'>Defualt</option>"
        return r

    def del_list(self):
        p = self.ins._server._post()
        name = p["o"]
        del p["o"]
        if "multiaple" in p:
            del p["multiaple"]
        s = self.ins._users._get_settings(name)
        del s[self.k][p["list_name"]]
        self.ins._users._updat_settings(name, s)
        return p

    def dupl_list(self):
        p = self.ins._server._post()
        name = p["o"]
        del p["o"]
        if "multiaple" in p:
            del p["multiaple"]

        n = self.csets(name, list_name=p["list_name"])
        s = self.csets(name, n["for"])
        un = self.ins._data.unid

        n["insact"] = "0"
        n["name"] = p["list_name"] + "_" + un
        n["title"] = n["title"] + " " + un

        s[self.k][n["name"]] = n
        self.ins._users._updat_settings(name, s, type=n["for"])
        return p

    def active_list(self):
        p = self.ins._server._post()
        name = p["o"]
        del p["o"]
        if "multiaple" in p:
            del p["multiaple"]

        n = self.csets(name, list_name=p["list_name"])
        s = self.csets(name, n["for"])

        if self.k in s:
            for l in s[self.k]:
                s[self.k][l]["insact"] = "0"
            s[self.k][p["list_name"]]["insact"] = "1"
        self.ins._users._updat_settings(name, s, type=n["for"])
        return p

    def del_list(self):
        p = self.ins._server._post()
        name = p["o"]
        del p["o"]
        if "multiaple" in p:
            del p["multiaple"]

        s = self.ins._users._get_settings(name)
        n = self.csets(name, list_name=p["list_name"])
        s = self.csets(name, n["for"])

        ad = {}

        if self.k in s:
            for l in s[self.k]:
                if l != p["list_name"]:
                    ad[l] = s[self.k][l]

        self.ins._users._updat_settings(name, {self.k: ad}, type=n["for"])
        return p

    def update_ops(self):
        p = self.ins._server._post()
        ps = self.ins._json._decode(p["data"])
        db_data = {"content": ps["options"]}
        self.ins._db._update("kit_options", db_data, f"id='{p["i"]}'")

  

    def update_set(self):
        p = self.ins._server._post()
        name = p["o"]
        p = self.ins._json._decode(p["data"])
        if "multiaple" in p:
            del p["multiaple"]

        rf = "me"
        fid = ""
        rfid = ""

        if "refor" in p:
            rf = p["refor"]

        f = "me"
        if "for" in p:
            f = p["for"]

        rs = self.ins._users._get_settings(name, uid=rfid, type=rf)
        s = self.ins._users._get_settings(name, uid=fid, type=f)
        if self.k not in rs:
            rs[self.k] = {}
        rs[self.k][p["rename"]] = s[self.k][p["list_name"]]
        rs[self.k][p["rename"]]["list_name"] = p["rename"]
        if "insact" in p and p["insact"] == "1":
            for l in s[self.k]:
                s[self.k][l]["insact"] = "0"
        adds = ["title", "insact", "for"]
        for a in adds:
            rs[self.k][p["rename"]][a] = p[a]
        if p["rename"] != p["list_name"]:
            del rs[self.k][p["list_name"]]
        if rf != f:
            del s[self.k][p["list_name"]]
            self.ins._users._updat_settings(name, s, uid=fid, type=f)

        self.ins._users._updat_settings(name, rs, uid=rfid, type=rf)
        return p

    def set(self):
        st = self.sets()
        uidata = [{"start": True, "class": "ins-flex ins-padding-xl ins-col-12"}]
        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "list_name", ""), "name": "rename",  "pclass": "ins-col-12", "title": "Name"})
        uidata.append({"_type": "input", "type": "textarea", "_data": st.get(
            "title", ""), "name": "title",  "pclass": "ins-col-12", "title": "Title"})
        uidata.append({"_data": "",    "class": "ins-col-12 ins-title-m"})

        ch = {"_type": "input", "type": "bool",   "value":st.get("insact", "0"),
              "name": "insact",  "pclass": "ins-col-3", "_end": "Active"}

  

        uidata.append(ch)
        uidata.append({"_data": "",    "class": "ins-col-12 ins-title-m"})
        uidata.append({"_data": "For",    "class": "ins-col-12 ins-title-m"})
        uidata.append({"_type": "input", "type": "text", "value": st.get(
            "for", "me"), "name": "for", "pclass": "ins-hidden"})

        foro = {"_type": "input", "type": "radio",  "class": "crd-set-for_rad", "value": "org",
                "name": "refor",  "pclass": "ins-col-3", "_end": "Org"}
        if st.get("for", "me") == "org":
            foro["checked"] = "true"

        uidata.append(foro)
        forme = {"_type": "input", "type": "radio",  "class": "crd-set-for_rad",
                 "value": "me", "name": "refor",  "pclass": "ins-col-3", "_end": "Me"}
        if st.get("for", "me") == "me" or st.get("for", "me") == "user":
            forme["checked"] = "true"
        uidata.append(forme)
        forj = {"_type": "input", "type": "radio", "class": "crd-set-for_rad",
                "value": "job", "name": "refor",  "pclass": "ins-col-3", "_end": "Job"}
        if st.get("for", "me") == "job":
            forj["checked"] = "true"
        uidata.append(forj)

        uidata.append({"class": "ins-col-12 crd-set-for_rad-op"})
        uidata.append({"end": True})
        r = self.ins._ui._render(uidata)
        return r

    def update_list(self):
        p = self.ins._server._post()
        name = p["o"]
        del p["o"]
        if "multiaple" in p:
            del p["multiaple"]
        if "data" in p:
            p = self.ins._json._decode(p["data"])
        n = self.csets(name, list_name=p["list_name"])
        s = self.csets(name, n["for"])
        
        if self.k in s:
            if p["list_name"] in s[self.k]:
                for k in s[self.k][p["list_name"]]:
                    if k not in p:
                        p[k] = s[self.k][p["list_name"]][k]
        else:
            s[self.k] = {}
        s[self.k][p["list_name"]] = p
        self.ins._users._updat_settings(name, s , type=n["for"])
        return p
