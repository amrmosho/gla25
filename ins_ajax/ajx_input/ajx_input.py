from ins_kit._engine._bp import App


class AjxInput(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def lang_ui(self):
        ps = self.ins._server._post()
        
    
        d = self.ins._db._get_row(
            ps["o"], f"{ps["n"]},kit_lang", f"id='{ps["i"]}'" )
        
        
        
        if d["kit_lang"] =="" or  d["kit_lang"] ==None :
            d["kit_lang"] ="{}"
            
            
        dbl = self.ins._json._decode(d["kit_lang"])

        ls = self.ins._langs._get_all()

        uidata = [
            {"start": "true", "class": "ins-flex ins-padding-xl ui-input-lang-area"},
            {"start": "true", "class": "ins-flex-end ins-gap-m ins-padding-2xl ins-card ins-col-12 ins-border "},
            {"_data": f"<i class='lni lni-database-2'></i> update languages : ", "class": "ins-flex ins-title-m ins-strong  ins-col-12"},
        ]
        for k, l in ls.items():
            v = ""
            if l["name"] in dbl and  ps["n"] in dbl[l["name"]]:
                v = dbl[l["name"]][ps["n"]]

            i = [{"_type": "textarea", "name": l["name"],
                  "title": l["title"], "_data": v, "pclass": "ins-col-12"}]
            uidata += i
        for k in ps:
            i = [{"_type": "input", "type": "hidden", "name": k,
                  "value": ps[k], "pclass": "ins-hidden"}]
            uidata += i
        uidata.append({"_data": "Update",  "data-i": ps["i"], "data-n": ps["n"],
                      "data-o": ps["o"],  "class": "ins-button ui-input-lang-update ins-primary ins-col-4"})
        uidata.append({"end": "true"})
        uidata.append({"end": "true"})
        return self.ins._ui._render(uidata)

    def lang_update(self):
        ps = self.ins._server._post()
        ls = self.ins._langs._get_all()

        d = self.ins._db._get_row(
            ps["o"], f"{ps["n"]},kit_lang", f"id='{ps["i"]}'")
        
        
        if d["kit_lang"] =="" or  d["kit_lang"] ==None :
            d["kit_lang"] ="{}"
            
            
        dbl = self.ins._json._decode(d["kit_lang"])

        ldata = {}

        for k, l in ls.items():
            if l["name"] in ps.keys():
                if l["name"] not in dbl:
                    dbl[l["name"]] = {}

                if ps["n"] not in dbl[l["name"]]:
                    dbl[l["name"]][ps["n"]] = {}

                dbl[l["name"]][ps["n"]] = ps[l["name"]]

        db_data = {
            "kit_lang": self.ins._json._encode(dbl)
        }
        self.ins._db._update(ps["o"], db_data, f"id='{ps["i"]}'")
        

        
        return "1"
