import json
from uuid import uuid4
from ins_kit._engine._bp import App
import zipfile
import pathlib
class AppProductsAdmin(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)
    def _getext(self, ps):
        ps = self.ins._server._post()
        p: str = ps["fullpath"]
        p = p.replace("/ins_web", "ins_web")
        archive = zipfile.ZipFile(p, 'r')
        ln = archive.namelist()
        for f in ln:
            if "." in f:
                file_extension = pathlib.Path(f).suffix
                r = file_extension.replace(".", "")
        return r
    
   
    
    
    def _file_ui(self):
            
        sop =[
                
                 {
                "_data": self._file_ui_row(),
                "class": "ins-col-12 ins-flex ins-card files-input-row ins-padding-m"
            }]
            
        r = self.ins._ui._render(sop)
        return str(r)      
    
    def _file_ui_row(self):
        ps = self.ins._server._post()
        exts = self.ins._json._file_read("ins_langs/file_ext.json")
        ext_value = ""
        if   "updatemode" in ps and ps["updatemode"] =="edit":
            ext_value =  ps.get("type")
            ps["oname"] =ps.get("name") 
        type = {}
        th = {}
        
        for k in exts:
            type[k] = exts[k]["title"]
            if ps["type"] == k:
                th = exts[k]
                if ext_value == "" :
                    ext_value = k
        if ext_value == "" and  ps["type"] =="zip":
            ext_value = self._getext(ps)
            th = exts[ext_value]           
        else:
            ext_value =  ps["type"]
            
            
        type = {"_type": 'select',"class":"type","name":"type",  "value": ext_value, "pclass": "ins-col-2","type": "input", "fl_data": type}
        version = {"_type": "input", "pclass": "ins-col-1",
                   "name": "version", "value":ps.get("version" ,"")}
        rversion = {"_type": "input", "pclass": "ins-col-1",
                   "name": "rende_rversion", "value":ps.get("rende_rversion","")}
        
        
        
        sop = [
            
            {
                "_data": ps["oname"]
            },
            {
                "start": "True",
                "class": "ins-col-12 ins-flex-end ins-card ins-border ins-padding-m"
            },
            {
                "pclass": "ins-hidden" ,"type":"hidden" ,"_type":"input" ,"name" :"path" ,"value":ps["path"]
            },{
                "pclass": "ins-hidden" ,"type":"hidden" ,"_type":"input" ,"name" :"name" ,"value":ps["oname"]
            },
        ]
        
        
        if "native" in th:
            sop.append({"_type": "input", "type":"bool", "pclass": "ins-col-grow","value":ps.get("native","1"),
                   "name": "native" ,"_end": "Native"})
        sop.append(type)
        sop.append(version)
        if "render" in th:
            sop.append({"_type": 'select', "pclass": "ins-col-2", "name": "render","value" : ps.get("render"),
                       "type": "input", "fl_data": th["render"]})
            sop.append(rversion)
        sop += [{"class": "ins-icons-x ins-button-text ins-danger-color files-input-del" },{"end": "True"}]
        r = self.ins._ui._render(sop)
        return str(r)
    
    
    
    
    
    
    def submit_setp_one(self):
        ps = self.ins._server._post()
        r = self.ins._db._insert("gla_product", ps)
        return str(r)
    def out(self):
        self.app._include("script.js")
        self.app._include("style.css")
        sop = [{
            "end": "True"
        },
            {
            "start": "True",
            "class": "ins-col-12 ins-flex ins-card ins-border ins-padding-m"
        },
            {
            "name": "th_main",
            "title": "thumbnail",
            "title-ar": "الصورة المصغرة",
            "_trans": "true",
            "_type": "input",
            "_exts": "image/png,image/jpg",
            "type": "upload",
            "required": "true",
            "_dir": f"prosi/_{self.ins._server._get("id")}",
            "pclass": "ins-col-12"
        },
            {
            "_type": "input",
            "type": "upload",
            "title": "Preview images",
            "name": "images",
            "pclass": "ins-col-12 ",
            "required": "true",
            "style": "height:250px",
            "_dir": f"prosi/_{self.ins._server._get("id")}",
            "_mode": "multi",
            "_exts": "image/png,image/jpg"
        },
            {
            "class": "ins-col-12 ins-padding-m ins-line"
        },
            {
            "name": "youtube",
            "title": "youtube",
            "title-ar": "youtube",
            "_type": "input",
            "type": "text",
            "pclass": "ins-col-6"
        },
            {
            "name": "sketchfab",
            "title": "sketchfab",
            "title-ar": "sketchfab",
            "_type": "input",
            "type": "text",
            "pclass": "ins-col-6"
        },
            {
            "end": "True"
        },
            {
            "start": "True",
            "class": "ins-col-12 ins-flex ins-card ins-padding-m _files_parents"
        },
            {
            "_type": "input",
            "type": "upload",
            "title": "Files",
            "name": "files_ui",
            "placeholder": "_add placeholder hear",
            "pclass": "ins-col-12 ",
            "required": "true",
            "style": "height:50px",
            "_dir": f"prosf/_{self.ins._server._get("id")}",
            "class": "upload_files_btn",
            "_mode": "multi",
            "class": "upload_files_btn",
            "_exts": "image/png", "nojs": "true"
        },
     {
            "_type": "input","type":"textarea",
            "pclass":"ins-hidden","name":"files_data","class":"files-data-inpt"
 },
            {
            "end": "True"
        },
            {
            "end": "True"
        }
        ]
        if self.ins._server._get("mode") != "edit":
            sop = [{
                "end": "True"
            }
            ]
            self.app._properties["form_actions"] = [{"style": "width:20px"}, {
                "_data": "Next", "class": "ins-button -save-and-next ins-primary ", "style": "width:150px"}, {"style": "width:20px"}]
        self.app._properties["form_data"] += sop
        self._include("script.js")
        r = self.ins._apps._crud(properties=self.app._properties)
        return r
