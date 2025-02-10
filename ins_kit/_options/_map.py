from ins_kit.ins_parent import ins_parent
import datetime


class Map(ins_parent):

    DB_DATE_FORMAT = '%Y-%m-%d'
    DB_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    DB_TIME_FORMAT = '%H:%M:%S'
    

    UI_DATE_FORMAT = '%d/%m/%Y'
    UI_DATETIME_FORMAT = '%d/%m/%Y %I:%M %p'
    UI_TIME_FORMAT = '%I:%M %p'



    IMAGES_FOLDER = "ins_images"

    WEB_FOLDER = "ins_web"
    TEMPLATES_FOLDER = "ins_temps"
    KIT_FOLDER = "ins_kit"

    WEB_TMP_FOLDER = "ins_web/tmp/"



    APPS_FOLDER = "ins_apps"
    WIDGETS_FOLDER = "ins_wdgts"
    AJAX_FOLDER = "ins_ajax"
    
    LANGUAGES_FOLDER = "ins_langs"
    PROPERTIES_FOLDER = "ins_properties"

    PLGINS_FOLDER = "ins_plgs"
    UPLOADS_FOLDER = "/ins_web/ins_uploads/"
    INCLUDS_FOLDER = "ins_includes"

    PROPERTIES_PROJECT_FILE = "ins_properties/project.json"
    PROPERTIES_STRUCTURE_FILE = "ins_properties/structure.json"
    PROPERTIES_COMPONENTS_FILE = "properties.json"

    ERORR_TEMPLATE = "temp/error.html"


    def _get_class_name(self, name):
        cnames = name.split("_")
        cname = ""
        for n in cnames:
            cname += n.capitalize()
        return cname
    
    
class This(ins_parent):
    _area = {}
    _settings = {}
    _lang = {}
    _menu = ""
    _temp = {"url": ""}
    _temp_url = ""
    def _clear(self):
     self._area = {}
     self._settings = {}

     self._lang = {}
     self._menu = {}
     self._temp = {"url": ""}
     self._temp_url = ""
