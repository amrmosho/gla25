from ins_kit._engine._bp import App
from flask import request
from werkzeug.utils import secure_filename
import os


class AjxServer(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    
    def _get_session(self):
        p = self.ins._server._post()
        return  self.ins._server._get_session(p["name"])

    def _remove_session(self):
        p = self.ins._server._post()
        self.ins._server._del_session(p["name"])
        return "1"

    
    def _set_session(self):
        
        ps = self.ins._server._post()
        if "multiaple" in ps:
            del ps["multiaple"]
        
        for k in ps:
              self.ins._server._set_session(k,ps[k])
        return "1"

