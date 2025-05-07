from ins_kit.ins_parent import ins_parent
from flask import render_template
import json

"""Temp Class---------------------------------------"""


class Ajax(ins_parent):
    def _render(self,  area, path: str):
        self.ins._server._update_get(path)
        g = self.ins._server._get()
        data = path.split("/")
        area = data[0]
        app = data[1]
        out = data[2]
        if "_t" not in g:
            g["_t"] = "app"
        infos = self.ins._eng._class_infos(app, area, g["_t"])
        self._options = {}

        path = infos["path"]
        self._weburl = infos["weburl"]
        self._imagesurl = infos["images_url"]

        self._url = infos["url"]
        self._properties = infos["properties"]
        self._name = app

        a = self.ins._eng.run_class(app, path, self, out=out)
        return a


class Temp(ins_parent):
    header = ""
    header_end = ""

    def _header(self):
        self.header = ""
        lib_path = f"/{self.ins._map.WEB_FOLDER}/{self.ins._map.KIT_FOLDER}/"

        incs_path = f"/{self.ins._map.WEB_FOLDER}/ins_incs/"

        self.header += "\t\n" + self.ins._files._include(
            f"{incs_path}line_icons_2/assets/icon-fonts/lineicons.css")

        css = ["ins_root",
               "ins_elements",
               "ins_dark_style",  "ins_light_style",
               "ins-icons",
               "ins_colors", "ins_layout", "ins_content",
               "ins_forms", "ins_ui",

               "ins_lang-" +  self.ins._langs._this_get().get("name" )
               ]
        
        lng= self.ins._langs._this_get()
        css.append(lng["direction"])  
        
        for c in css:
            self.header += "\t\n" + \
                self.ins._files._include(f"{lib_path}css/{c}.css")

        mcss = ["ins_phone"]
        for c in mcss:
            att = {
                "media": "only screen and (min-width: 0px) and (max-width: 1000px)", "type": "text/css"}
            self.header += "\t\n" + \
                self.ins._files._include(f"{lib_path}css/{c}.css", att)

        js = ["swiped", "ins"]
        for j in js:
            self.header += "\t\n" + \
                self.ins._files._include(f"{lib_path}js/{j}.js")

    def _add_to_header(self, data: str):
        if data != None:
            self.header_end += data

    
    def _data_social_tags(self,data):
        
        s = f"""
        <meta property="og:site_name" content="ELGALLA GOLD">
        <meta property="og:url"                content="https://elgalla.insya.co/{data["url"]}" />
        <meta property="og:type"               content="article" />
        <meta property="og:title"              content="{data['title']}" />
        <meta property="og:description"        content="{data['des']}" />
        <meta property="og:image"              content="https://elgalla.insya.co/{data["img"]}" />   
        
        

        <meta name="site_name" content="ELGALLA GOLD">
        <meta name="url"                content="https://elgalla.insya.co/{data["url"]}" />
        <meta name="type"               content="article" />
        <meta name="description"        content="{data['des']}" />
        <meta name="image"              content="https://elgalla.insya.co/{data["img"]}" />   
        <meta name="keywords" content="GOLD , {data['title']}, ELGALLA ">

        <link rel="canonical" href="https://elgalla.insya.co/{data["url"]}" />

             
             
        """
        self._add_to_header(s)
   
   

    def _update(self):
        pass

    def _set_page_title(self,  title):
        self._page_title = title

    def _set_page_des(self,  des):
        self._page_des = des

    def _login(self,  area, path):

        self.header_end = ""
        self.ins._server._update_get(path)
        u = self.ins._users._session_get()

        if not u:
            u = {}

            u["settings"] = {}

        u["settings"] = self._user_settings = self.ins._users._get_settings(
            "gen")

        if "style" not in u["settings"]:
            u["settings"]["style"] = "light"

        if "lang" in u["settings"]:
            self.ins._langs._this_set(u["settings"]["lang"])


        self.ins._eng._run(area)
        
        self._weburl = f"{self.ins._this._temp_url}{
            self.ins._this._temp["type"]}/"

        area_url = self.ins._eng._areas(area)["url"]

        self._imagesurl = f"/{area_url}/{self.ins._map.WEB_FOLDER}/{
            self.ins._map.IMAGES_FOLDER}/"
            
        self._area = self.ins._eng._areas(area)


        p = self.ins._server._req()

        if "lgstatus" in p and p["lgstatus"] == "login":
            if self.ins._users._login(p) == False:
                m = "<div class='    ins_message   ins-message ins-danger'>Incorrect email or password. Please try again.</div>"
                return render_template(f'{self.ins._this._temp["type"]}/login.html', msg=m,   temp=self)

        if not self.ins._users._is_login():
            return render_template(f'{self.ins._this._temp["type"]}/login.html',   temp=self)



        
        return self.get_template(area ,u)
          
    
    
    def get_template(self ,area ,u):
        se = self.ins._server._get_session()

        self._header()

     
        self._page_title = self.ins._this._menu.get("title")

        self._properties = self.ins._json._file_read(
        f"./{self._weburl}/properties.json")
        area_url = self.ins._eng._areas(area)["url"]
        self._imagesurl = f"/{area_url}{self.ins._map.IMAGES_FOLDER}/"    
        ws = self.ins._eng._widgets()
        a = self.ins._eng._App()
        if self.ins._server._get("insrender") == "app":
            return a

        if "title" in u:
            u["avatar"] = u["title"][0]

        p_data = {}
        p_data["class"] = f"ins-{u["settings"]["style"]}-style"
        
        
        
        self._add_to_header(self.ins._this._settings["pro"].get("header" ,""))
        p_data["title"] =self.ins._this._settings["pro"].get("page_title" ,"")+ self._page_title
        
        

        if "insrender" in self.ins._server._get():
            s = f"{self.ins._server._get("insrender")}.html"
        else:
            s = "index.html"
           
        self.css = self.ins._this._menu["css"]
        lang = self.ins._langs._this_get()
        
        
        def url(_set={}, remove=[], claer=False):
            return self.ins._server._url(_set, remove, claer)
        
        
        def session_count(name):
            if name in se:
                return len(se[name])
            else:
             return 0

        return render_template(f'{self.ins._this._temp["type"]}/{s}', app=a, session=se,session_count=session_count, user=u, lang=lang, url=url, page=p_data,  wdgts=ws,  temp=self)



    def _con(self, message):
        a = message
        return render_template(f'tmp_admin_style/error.html', app=a,   temp=self)

    def _render(self,  area, path):

        self.header_end = ""

        self.ins._server._update_get(path)

        u = self.ins._users._session_get()

        if not u:
            u = {}

        u["settings"] = self._user_settings = self.ins._users._get_settings(
            "gen")

        if "style" not in u["settings"]:
            u["settings"]["style"] = "light"

        if "lang" in u["settings"]:
            self.ins._langs._this_set(u["settings"]["lang"],True)

        self.ins._eng._run(area)

        if  "type" in  self.ins._this._temp:
            self._weburl = f"{self.ins._this._temp_url}{
                self.ins._this._temp["type"]}/"





       
        return self.get_template(area ,u)
       
   


"""App Class---------------------------------------"""
class Plgin(ins_parent):

    def __init__(self, Ins) -> None:
        super().__init__(Ins)

class App(ins_parent):
    data = {}
    __apnds = []
    _weburl = ""

    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def _include(self, name):
        if name != None:
            path = self._weburl+name
            if path not in self.__apnds:
                self.__apnds.append(path)
                ad = self.ins._files._include(path)
                self.ins._tmp._add_to_header(ad)
            return "1"

    def _infos(self, type, area):
        r = {}

        try:

            area_url = self.ins._eng._areas(area)["url"]
            r["url"] = f"{self.ins._map.APPS_FOLDER}/{type}/"
            r["path"] = ""
            url_area = ""

            if area_url != "":
                r["path"] = f"{area_url}."
                url_area = f"{area_url}/"

            r["path"] += f"{self.ins._map.APPS_FOLDER}.{type}.{type}"
            r["weburl"] = f"/{url_area}{self.ins._map.WEB_FOLDER}/{r["url"]}"
            r["url"] = f"{url_area}{r["url"]}"

            r["properties"] = self._pros("properties", r["url"])

            r["lang"] = self._pros(self.ins._langs._this_get()["name"], r["url"])

            r["properties"]["url"] = r["url"]
            r["properties"]["pros_name"] = "properties"
            

            return r
        except FileNotFoundError as err:
            a = err
        except TypeError as err:
            a = err

    def _pros(self, name, url=""):
        if url == "":
            url = self._url
        return self.ins._eng._pros(name, url)

    def _render(self, app):
        self.__apnds.clear()
        if len(app) > 0:
            self._data = app
            self._name = app["type"]
            self._options = {}
            if app["kit_options"] != "":
                self._options = json.loads(app["kit_options"])

            """---------------------------------------"""

            infos = self._infos(app["type"], app["src_area"])
            path = infos["path"]
            self._weburl = infos["weburl"]
            self._url = infos["url"]
            self._properties = infos["properties"]
            self._lang = infos["lang"]

            """---------------------------------------"""

            a = self.ins._eng.run_class(app["type"], path, self)

            if type(a) == str:
                app["out"] = a
                app["class"] = app["class"].replace(",", " ")
                app["_type"] = "app"
                return self.ins._ui._item(app)

            else:

                return a

        else:
            return "404"


"""Widget Class---------------------------------------"""


class Widget(ins_parent):
    data = {}
    __apnds = []

    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def _include(self, name):
        path = self._weburl+name
       # if path not in self.__apnds:
        #    self.__apnds.append(path)
        ad = self.ins._files._include(path)
        self.ins._tmp._add_to_header(ad)
        return "1"

    def _pros(self, name, url=""):
        if url == "":
            url = self._url
        return self.ins._json._file_read(f"./{url}/{name}.json")

    def _render(self, mod):

        self._name = mod["type"]
        self._data = mod
        self._options = {}

        if mod["kit_options"] != "":
            self._options = json.loads(mod["kit_options"])

        """---------------------------------------"""
        infos = self.ins._eng._class_infos(
            mod["type"], mod["src_area"], "wdgt")
        path = infos["path"]
        self._weburl = infos["weburl"]
        self._url = infos["url"]
        self._properties = infos["properties"]

        """---------------------------------------"""

        a = self.ins._eng.run_class(mod["type"], path, self)

        mod["out"] = a
        if mod["class"] == None or mod["class"] == "":
            mod["class"] = ""
        else:
            mod["class"] = mod["class"].replace(",", " ")
        mod["_type"] = "wdgt"

        return self.ins._ui._item(mod)
