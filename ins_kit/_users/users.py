from ins_kit.ins_parent import ins_parent


class Users(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    __SESSION_KEY = "ins_u_data"
    __SESSION_KEY_PER = "ins_u_data_per"


    def _session_key(self):
        return self.__SESSION_KEY

    def _session_get(self,  name=""):
        if self._is_login():
            if name == "":
                return self.ins._server._get_session(self.__SESSION_KEY)
            else:
                return self.ins._server._get_session(self.__SESSION_KEY)[name]

    def _session_set(self,  data):
        del data["password"]
        self.ins._server._set_session(self.__SESSION_KEY, data)
        self._per_get_all(True)

    def _per_get_all(self, update=False):

        if self.__SESSION_KEY_PER in self.ins._server._get_session() and update == False:
            return self.ins._server._get_session(self.__SESSION_KEY_PER)
        else:
            w = self.ins._db._where_by_array(self._session_get("groups"))
            w += f" and  (`tar_area`='{self.ins._this._area["url"]}') "
            udata = self.ins._db._get_data(
                "kit_user_group", "*", f" {w}   ")
            self.ins._server._set_session(self.__SESSION_KEY_PER, udata)
            return udata

    def _per_get_menu(self, menu_id=""):
        ps = self._per_get_all()
        for p in ps:
            if p["apps_permissions"] != "":
                all_permissions = self.ins._json._decode(p["apps_permissions"])
                for ap in all_permissions:
                    if ap["app"] == str(menu_id):
                        return ap

        return False

    def _per_check_menu(self, menu_id=""):

        ps = self._per_get_all()
        if ps != False:
            for p in ps:
                if str(p["all_permissions"]) == "1":
                    return True
                if p["apps_permissions"] != "":
                    all_permissions = self.ins._json._decode(
                        p["apps_permissions"])
                    for ap in all_permissions:
                        if ap["app"] == str(menu_id):
                            return True

        return False

    def _user_user_pre(self):
        return (self.__SESSION_KEY in self.ins._server._get_session())

    def _is_login(self):
        return (self.__SESSION_KEY in self.ins._server._get_session())

    def _logout(self):
        return self.ins._server._del_session(self.__SESSION_KEY)

    def _get_settings(self, name, uid="", type="user"):
        if type == "me":
            type = "user"

        if type == "user" and uid == "":
            uid = self._session_get("id")

        if type == "job" and uid == "":
            uid = self._session_get("groups")

        if type == "org":
            path = f"ins_setngs/{type}/_{name}.json"

        else:
            path = f"ins_setngs/{type}/_{uid}/_{name}.json"

        a = self.ins._json._file_read(path)
        if not a or len(a) == 0:
            return {}
        return a

    def _collect_settings(self, name):
        r = {}
        org = self._get_settings(name, type="org")
        if len(org) > 0:
            r["org"] = org
        user = self._get_settings(name, type="user")
        if len(user) > 0:
            r["user"] = user

        job = self._get_settings(name, type="job")
        if len(job) > 0:
            r["job"] = job


        return r

    def _updat_settings(self, name, data, uid="", type="user"):

        if type == "me":
            type = "user"

        if type == "user" and uid == "":
            uid = self._session_get("id")

        if type == "job" and uid == "":
            uid = self._session_get("groups")

        if type == "org":
            path = f"ins_setngs/{type}/_{name}.json"
        else:

            path = f"ins_setngs/{type}/_{uid}/_{name}.json"

        self.ins._json._file_write(path, data)

    def _login(self,  data):
        r = False
        if "email" in data and "password" in data:
            passsword = self.ins._data.hash_password(data["password"])

            udata = self.ins._db._get_row(
                "kit_user", "*", f"email='{data["email"]}' and password ='{passsword}' ")
            
            if udata != False:
                area = self.ins._this._area["name"]
                group = self.ins._db._get_row(
                "kit_user_group", "*", f"id='{udata["groups"]}' and tar_area ='{area}' ")
                if group != False:
                    self._session_set(udata)
                    r = True

        return r
