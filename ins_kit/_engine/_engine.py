from ins_kit.ins_parent import ins_parent
from ins_kit._engine._bp import Widget, App
from ins_kit.ins_parent import ins_parent
from ins_wdgts.wdg_content.wdg_content import WdgContent


class Engine(ins_parent):

    temp = []
    __widgets = []
    _kit_settings = []

    def run_class(self, name, _path, parent ,out ="out"):
        _class_name = self.ins._map._get_class_name(name)
        exec(f"from {_path} import {_class_name}")
        _class = eval(f"{_class_name}(parent).{out}()")
        return _class 

    def _app_settings(self, name=""):
        if name != "":
            return self.ins._this._settings[name]
        else:
            return self.ins._this._settings

    def _areas(self, name):

        areas = self._app_settings("areas")
        if name != "":
            return areas[name]
        else:
            return areas

    def _int(self, path):
        """*---------- load App settings*"""
        self.ins._this._clear()
        self.ins._this._settings = self.ins._json._file_read("./ins_pros/app.json")


        """ for k ,v in  self.ins._this._settings["areas"].items():
            if path.find(k) != -1:
                self.ins._this._area =v
            
        if len(self.ins._this._area) ==0 :
                self.ins._this._area = self.ins._this._settings["areas"]["home"]
                a= """""

    def _run(self, area):
        """*---------- load Kit settings*"""
        self._kit_settings = self.ins._json._file_read(
            "./ins_kit/_options/kit_settings.json")
        self.ins._this._area = self._areas(area)
        
        self.ins._langs._this_set()
        a = self.ins._langs._this_get()
        self.ins._this._lang = self.ins._langs._this_get()
        self.__data(area)

    def __data(self, area):
        if len(self.ins._this._area) == 0:
            return "404"
        self.ins._this._temp_url = ""
        if self.ins._this._area["url"] != "":
            self.ins._this._temp_url = f"/{self.ins._this._area["url"]}/"

        self.ins._this._temp_url += f"{self.ins._map.WEB_FOLDER}/{
            self.ins._map.TEMPLATES_FOLDER}/"

        self.ins._this._temp_url = self.ins._this._temp_url.replace("//", "/")

        self.ins._db._connect()


        """*---------- load temp data*"""
        self.ins._this._temp = self.ins._db._get_row(
            "template_table", where=f"tar_area='{area}' and kit_default ='1'" , update_lang=True)

        """*---------- load  menu data*"""
        self.ins._this._settings["pro"]=self.ins._db._get_row("kit_pro_settings	" , update_lang=True)
        
        if (self.ins._server.GET["alias"] == "home"):
            menus = self.ins._db._get_row("menu_item_table", where=f"tar_area='{
                                          area}' and kit_home ='1'" , update_lang=True )
        else:
            menus = self.ins._db._get_row("menu_item_table", where=f"tar_area='{area}' and alias ='{self.ins._server.GET["alias"]}'" , update_lang=True)


        if menus == False :
            return "404"
         
        """*---------- load widgets  data*"""
        view_in = self.ins._db._where_from_group(menus["alias"], "view_in")
        self.__widgets = self.ins._db._get_data("wdgts_table", where=f"tar_area='{
                                                self.ins._this._area["name"]}' and  ((view_all = 1) or {view_in} )  order by `kit_order`  ")
        self.ins._db._close()
        if menus:
            self.ins._this._menu = menus

    def _App(self):
        app = self.ins._this._menu
        a = App(self.ins)
        return a._render(app)

    def _widgets(self):
        w = Widget(self.ins)
        d = {}
        if not self.__widgets:
            return d
        for mod in self.__widgets:
            if mod["position"] not in d:
                d[mod["position"]] = ""
            d[mod["position"]] += w._render(mod)

        return d
    
    def _pros(self, name, url=""):
        return self.ins._json._file_read(f"./{url}/{name}.json")
    
    def _class_infos(self, name, area ,type="app"):
        r = {}
        
        if type=="wdgt":
            container =self.ins._map.WIDGETS_FOLDER
        
        elif type=="ajx":
            container =self.ins._map.AJAX_FOLDER
        else:
            container =self.ins._map.APPS_FOLDER
        area_url = self._areas(area)["url"]
        r["url"] = f"{container}/{name}/"
        r["path"] = ""
        url_area = ""
        

        if area_url != "":
            r["path"] = f"{area_url}."
            url_area = f"{area_url}/"

        r["path"] += f"{container}.{name}.{name}"
        r["weburl"] = f"/{url_area}{self.ins._map.WEB_FOLDER}/{r["url"]}"
        r["images_url"] = f"/{url_area}{self.ins._map.IMAGES_FOLDER}/"
        r["url"] = f"{url_area}{r["url"]}"
        r["c_name"] = self.ins._map._get_class_name(name)

        r["properties"] = self._pros("properties", r["url"])
        return r
