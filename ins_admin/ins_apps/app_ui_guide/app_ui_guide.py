from ins_admin.ins_apps.app_ui_guide.app_ui_guide_inputs import AppUiGuideInputs
from ins_admin.ins_apps.app_ui_guide.app_ui_guide_test import AppUiGuideTest
from ins_admin.ins_apps.app_ui_guide.app_ui_icons import AppUiGuideIcons
from ins_kit._engine._bp import App


class AppUiGuide(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def __url(self, a):
        return self.ins._server._url({"mode": a})

    def out(self):

        g = self.ins._server._get()

        icons = {"_type": "a", "href": self.__url(
            "icons"), "_data": "<i class='lni ins-icon  lni-helicopter-2'> </i>Icons", "class": "ins-title-s ins-strong-l ins-padding-m ins-radius-xl"}

        style = {"_type": "a", "href": self.__url(
            "style"), "_data": "<i class='lni ins-icon  lni-sun-1'> </i>Style", "class": "ins-title-s ins-strong-l ins-padding-m ins-radius-xl"}

        inputs = {"_type": "a", "href": self.__url(
            "inputs"), "_data": "<i class='lni lni-pen-to-square  ins-icon'> </i>inputs", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-xl"}
        test = {"_type": "a", "href": self.__url(
            "test"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> test", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-xl"}

        s = [] 
        r =""
        if "mode" in g and g["mode"] == "inputs":
            
            s = [{"_type": "a", "href": "#_input", "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> Input", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a",  "href": "#_select", "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> select", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a",   "href": "#_auto", "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> auto", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a",  "href": "#_upload", "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> upload", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"}
            ]
            
            r = AppUiGuideInputs(self.app).out()
            inputs["class"] += " ins-active "
        elif "mode" in g and g["mode"] == "test":
            r = AppUiGuideTest(self.app).out()
            test["class"] += " ins-active "

        elif "mode" in g and g["mode"] == "icons":
            
           
            s = [{"_type": "a", "href": self.__url(
                "insya_icons"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> Insya", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a", "href": self.__url(
                    "icons"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> Line", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                   ]
            r = AppUiGuideIcons(self.app).out()
            icons["class"] += " ins-active "
            
            
        elif "mode" in g and g["mode"] == "insya_icons":
            
           
            s = [{"_type": "a", "href": self.__url(
                "insya_icons"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> Insya", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a", "href": self.__url(
                    "icons"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> Line", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                   ]
            r = AppUiGuideIcons(self.app).insya()
            icons["class"] += " ins-active "
            
            

        elif "mode" in g and g["mode"] == "style":
            r = AppUiGuideIcons(self.app).out()
            style["class"] += " ins-active "




            s = [{"_type": "a", "href": self.__url(
                "test"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> test", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a", "href": self.__url(
                    "test"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> test", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a", "href": self.__url(
                    "test"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> test", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"},
                {"_type": "a", "href": self.__url(
                    "test"), "_data": "<i class='lni lni-select-cursor-1 ins-icon'> </i> test", "class": "ins-title-s ins-strong-l  ins-padding-m ins-radius-m"}
            ]

        header = [{"start": "true", "class": "ins-flex ins-col-grow"},
                  {"start": "true", "class": "ins-flex ins-col-12  "},icons, style, inputs, test]


        header.append(
            {"start": "true", "class": "ins-flex ins-radius-xl  ins-border ins-col-grow "})

        header += s
        header.append({"end": "true"})
        header.append({"end": "true"})
        header.append({"end": "true"})
        self.ins._tmp._set_page_des(self.ins._ui._render(header))

        
        uidata  =[{"_data": r, "class": "ins-col-12  ins-flex ins-padding-xl"}]
   
        
        
        
        
        self.app._include("script.js")

        return self.ins._ui._render(uidata)
