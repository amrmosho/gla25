import re
from ins_kit.ins_parent import ins_parent


class Languages(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def _this_set(self ,lang="",defu=False):
        
        if lang =="":
            g=  self.ins._server._get()
            if "lang" in g :
              lang = g["lang"]
        
        
        
        if lang !="":
            if  not defu or not self.ins._server._has_session("inslang") :
                 return self.ins._server._set_session("inslang" ,lang)
    
    def _this_get(self ,code=False):
       lang = self.ins._server._get_session("inslang" ,"en")
       
       if code:
           return lang
       else:
         return   self.ins._this._settings["langs"][lang]

       
       
    
    

    def _search(self, text: str) -> list[str]:
        pattern = r'\@\((.*?)\)'
        matches = re.findall(pattern, text)
        return matches

    def _get_all(self):
        return self.ins._this._settings["langs"]

    def _update(self, content: str, lang_data: dict):
        d = self.ins._this._lang
        f_search = self._search(content)
        r = content
        for w in f_search:

            if str(w).find(".") > 0:
              ws = w.split(".")
              d = lang_data[ws[0]]
              wb = ws[1]
            else:
              wb = w
              d = lang_data

            if wb in d:
                    r = r.replace(f"@({w})", d[wb])
        return r

    def _render(self, content, data: dict = {}):
        data["get"] = self.ins._server._get()
        data["session"] = self.ins._server._get_session()
        data["req"] = self.ins._server._req()

        return self._update(content, data)

    def _render_tags(self, data: dict = {}):
        
        del_keys=[]
        for k in data.keys():
            lk = f"{k}-{self.ins._this._lang["name"]}"
            if lk in data:
                data[k] = data[lk]
                del_keys.append(lk)
                
                
                
        for d in del_keys:
                del data[d]
                   
       
                
                
                
        return data

    def _render_db_row(self, r: dict = {}):
            lss = self.ins._json._decode(r["kit_lang"])
            self.ins._this._lang["name"] = "ar"
            ls = lss[self.ins._this._lang["name"]]
            for k, v in r.items():
                if k in ls.keys():
                    r[k] = ls[k]


            return r
    
    

    def _get(self, name, type ="crud"):
        l = self.ins._this._lang
        url = f"ins_langs/{l.get("name" ,"en")}"
        data = self.ins._json._file_read(f"./{url}/{type}.json")

        if name in data:
            return data[name]

        else:
            return name
