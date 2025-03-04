from ins_kit.ins_parent import ins_parent
from flask import session, request


class Server(ins_parent):
    GET = {}
    _path = ""
    ERROR = {}
    DATE = {}

    def _update_get(self, path: str):
        self._path = path
        urls = path.split("do")
        paths = urls[0].split("/")
        while ("" in paths):
            paths.remove("")

        Server.GET = {}

        path_start = 0

        if len(paths) > 0 and paths[0] == "ajax":
            Server.GET["ajax"] = True
            path_start += 1

        if len(paths) > path_start:
            Server.GET["alias"] = paths[path_start]
        if len(paths) > (path_start+1):
            Server.GET["mode"] = paths[(path_start+1)]
        if len(paths) > (path_start+2):
            Server.GET["id"] = paths[(path_start+2)]
        if "alias" not in Server.GET:
            Server.GET["alias"] = "home"

        if len(urls) > 1:

            paths = urls[1].split("/")
            k = ""
            for p in paths:
                if k == "":
                    k = p
                else:
                    Server.GET[k] = p
                    k = ""
        if "lang" in Server.GET:
            self.LANG = Server.GET["lang"]

    def _post(self, name="", default="") -> dict:
        r = {}
        f = request.form
        for key in f.keys():
            m = f.getlist(key)
            l = len(m)
            if l > 1:
                r[key] = ','.join(str(e) for e in m)
            else:
                r[key] = m[0]

        if name == "":
            return r
        else:
            return r.get(name, default)

    @property
    def _request(self):
        p = self._post()
        g = self._get()
        p.update(g)
        return p

    def _req(self, name="", default="") -> str:
        p = self._post()
        g = self._get()
        p.update(g)
        if name == "":
            return p
        else:
            return p.get(name, default)

    def _up_get(self, data: dict):
        Server.GET.update(data)

        g = Server.GET

    def _get_add(self, name="", value=""):
        Server.GET[name] = value

    def _get(self, name="", default=""):

        if name == "":
            return Server.GET
        if name in Server.GET:
            return Server.GET.get(name, default)
        else:
            return default

    @property
    def _session(self):
        return session
    
    
    def _has_session(self, name: str = ""):
    
        return (name in session)
          


    def _get_session(self, name: str = "",defult=False):

        if name == "":
            return session

        elif name in session:
            return session[name]
        else:
            return defult

    def _set_session(self, name: str="", value ="",data={}):

        if len(data) >0:
            for k in data:
                   session[k] = data[k]

        
        else:

            session[name] = value


    def _del_session(self, name):
        del session[name]
        return True

    def _url(self, _set={}, remove=[], clear=False) -> str:
        url = "/"

        for k in self._get().keys():
            if k not in _set:
                _set[k] = self._get(k)

        if "area" in _set:
            area_url = _set["area"]
        else:
            area_url = self.ins._this._area["url"]

        if area_url != "":
            url += f"{area_url}/"

        if "alias" in _set and "alias" not in remove:
            url += f"{_set['alias']}/"

        if "mode" in _set and "mode" not in remove:
            url += f"{_set['mode']}/"

        """if "filter" in _set and "filter" not in remove:
            url += f"{_set['filter']}/"""

        if "page" in _set and "page" not in remove:
            url += f"{_set['page']}/"

        if clear == True:
            return url

        if "id" in _set and "id" not in remove:
            url += f"{_set['id']}/"
        ex = ["id", "mode", "alias", "area", "_t", "_area", "_alias","page"]

        exurl = ""
        for k in _set.keys():
            if k not in remove and k not in ex:
                exurl += f"{k}/{_set[k]}/"

        if exurl != "":
            url += f"do/{exurl}"

        return url

    @property
    def session(self):
        return session
