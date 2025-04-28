import math
from ins_kit._apps.app_crud.app_crud_actions import APPCRUDActions
from ins_kit._apps.app_crud.app_crud_parent import appCrudParent


class APPCRUDList(appCrudParent):
    def __init__(self, P) -> None:
        self._footer_info = ""
        super().__init__(P)

    def __filter_data(self):
        r = {}
        fs = self.ins._server._get("f")
        if fs != "" and fs != None:
            rl = fs.split(";")
            for s in rl:
                if s != "":
                    row = {}
                    t = s.split("=")
                    row["filed"] = t[0]
                    row["name"] = t[0]

                    row["value"] = t[1]
                    for i in self.ops._list_filter:
                        if i["name"] == t[0]:
                            row["ops"] = i
                    row["query"] = self.__filter_get_query(row)
                    r[t[0]] = row
        return r

    def __tags(self, id=""):
        tgs = self.ins._db._get_data("kit_tags", "*")
        if id == "":
            return tgs
        else:
            for tg in tgs:
                if str(tg["id"]) == id:
                    return tg

    def __filter_data_url(self):

        fs = self.__filter_data()
        fdata = {}
        for k in fs:
            tk = fs[k]
            fdata[tk["filed"]] = tk["value"]
        return fdata

    def __filter_get_query(self, f):
        o = "like"
        vs = []
        if f["filed"] == "tag":

            r = self.ins._db._where_from_group(
                f["value"], f"{self.ops._table}.kit_tags")
            return r

        if "ops" in f:
            if "operator" in f["ops"]:
                o = f["ops"]["operator"]
            if "multi" in f["ops"]:
                vs = f["value"].split(" ")
            else:
                vs.append(f["value"])
        else:
            vs.append(f["value"])
        if o == "equal" or o == "=":
            r = "("
            sp = ""
            for v in vs:
                r += f"{sp}({f["filed"]} = '{v}')"
                sp = " or "
            r += ")"
        elif o == "not_equal" or o == "!=":
            r = f"({f["filed"]} <> '{f["value"]}')"
        elif o == "not_like" or o == "!=":
            r = f"({f["filed"]} Not like '%{f["value"]}%')"
        elif o == "less" or o == "<":
            r = f"({f["filed"]} < '{f["value"]}')"
        elif o == "greater" or o == ">":
            r = f"({f["filed"]} > '{f["value"]}')"
        elif o == "less_equal" or o == "<=":
            r = f"({f["filed"]} <= '{f["value"]}')"
        elif o == "greater_equal" or o == ">=":
            r = f"({f["filed"]} >= '{f["value"]}')"
        elif o == "empty":
            r = f"  ({f["filed"]} IS  NULL)"
        elif o == "not_empty":
            r = f"  ({f["filed"]} IS NOT NULL)"
        else:
            r = f"({f["filed"]} like '%{f["value"]}%')"
        return r

    def __filter_to_query(self):
        r = ""
        fs = self.__filter_data()
        sp = ""
        for k, f in fs.items():
            r += sp + f["query"]
            sp = " and "
        return r
    __list_count = 0
    __page = 2

    def __get_data(self, f, count=False, no_limit=False):
        self.__page = self.ins._server._get("page")
        if self.__page == "" or self.__page == None:
            self.__page = 1
        else:
            self.__page = int(self.__page)

        if f == "":
            f = "1=1"
        f += f" and  ({self.ops._table}.kit_deleted=0) "
        custom = " * "
        if count:
            custom = " count(id) "
        self.ins._db._connect()

        if "orderby" in self.ins._server._get():
            ord = f"{self.ops._table}.{self.ins._server._get("orderby")}"
        else:
            ord = f" {self.ops._table}.id "

        if "forderby" in self.ins._server._get():
            ord = f" {self.ins._server._get("forderby")}"

        if "ordertype" in self.ins._server._get():
            ord += f" {self.ins._server._get("ordertype")} "
        else:
            ord += " DESC "


        if self.ops._list_where != "":
            f+=" and " +self.ops._list_where
    
        
       
            
            

        if self.ops._list_query =="":
            sql = f"select {custom} from {
                self.ops._table} where {f} order by {ord}"
        else:
            sql =self.ins._langs._update(self.ops._list_query  ,{"where":f,"order":ord}) 
            
             
        

        if no_limit == False:
            li = ((self.__page - 1) * self.ops._list_limit)
            sql += f"limit {li},{self.ops._list_limit}"

        data = self.ins._db._get_query(sql)
        sql = f"select  count(id) as cid  from {self.ops._table} where {f} "
        cdata = self.ins._db._get_query(sql)
        self.ins._db._close()
        self.__list_count = cdata[0]["cid"]
        return data

    def _actions(self, id):
        
        
        
        edit_url = self.ins._server._url(_set={"mode": "edit", "id": id},remove= ["ids" ,"insrender","page"])
        
        
        
        
        more_menu = [
            {"start": True, "class": "ins-menu ins-end"},
            {"style": "transform: rotate(90deg);",
             "class": "lni ins-icon ins-header  lni-menu-meatballs-1 ins-padding-s", "style": "    margin-top: -10px;"},
            {"_type": "ul", "start": True},
            {
                "data-cm": self.__w("copy_item_msg"),
                "_type": "li", "class": "app-crud-list-copy", "data-id": id,
                "_data": f"<i class='lni ins-icon lni-clipboard'></i>{self.__w("duplicate")}"},
            {"_type": "ul", "end": True},
            {"end": True}
        ]
        data = [{"_type": "a", "href": edit_url, "title": self.__w("edit"), "title": self.__w("edit"),
                 "class": "lni ins-col-4  lni-pencil-1"},
                {"_type": "i", "data-id": id, "title": self.__w("delete"),
                    "class": "lni ins-col-4 app-crud-list-delete  lni-xmark",
                    "data-cm": self.__w("del_item_confirm_msg"), "data-dm": self.__w("del_item_msg")},
                {"_type": "a", "_data": more_menu, "class": " ins-col-4  "}
                ]
        return {"_data": data, "class": "ins-col-1 ins-no-print ins-gap-o _actions ins-flex-center"}

    def _list(self):
        ui = [{"class": "ins-col-12 l-search-bar", "_data": ""}]
        add_url = self.ins._server._url(_set={"mode": "add"} ,remove= ["ids" ,"insrender"])
        reload_url = self.ins._server._url({}, clear=True)
        t_url = self.ins._server._url({"mode": "trash"}, clear=True)

        ex_url = self.ins._server._url({"mode": "curd_export", "insrender": "app"})

        ex_all_url = self.ins._server._url(
            {"mode": "curd_exportall", "insrender": "app"})

        p_url = self.ins._server._url({"insrender": "print"}, ["mode"])
        s_url = self.ins._server._url({"mode": "settings"}, clear=True)

        
        more_menu = []
        more_menu.append({"start": True, "class": "ins-menu ins-end"})
        more_menu.append({"style": "transform: rotate(90deg);", "class": "lni ins-icon ins-header  lni-menu-meatballs-1 ins-padding-s"})
        more_menu.append({"_type": "ul", "start": True})
        more_menu.append({
            "data-cm": self.__w("del_items_confirm_msg"),
            "data-dm": self.__w("del_items_msg"),
            "_type": "li",
            "class": "app-crud-list-mdelete",
            "_data": f"<i class='lni ins-icon   lni-xmark'></i>{self.__w('delete')}"
        })
        more_menu.append({
            "data-cm": self.__w("copy_items_msg"),
            "_type": "li",
            "class": "app-crud-list-mcopy",
            "_data": f"<i class='lni ins-icon lni-clipboard'></i>{self.__w('duplicate')}"
        })
        more_menu.append({"_type": "li", "class": "ins-separator ins-line"})
        
        g = self.ins._server._get()

        if "alias" in g and g["alias"] == "order":
             more_menu.append({
                "_type": "a",
                "target": "blank",
                "href": ex_url,
                "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i> Export orders"
            }) 
             
             pr_url = self.ins._server._url({"mode": "curd_export","type":"products", "insrender": "app"})
             more_menu.append({
                "_type": "a",
                "target": "blank",
                "href": pr_url,
                "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i> Export Products"
            })
             more_menu.append({
                    "_type": "a",
                    "target": "blank",
                    "href": ex_all_url,
                    "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i> Export all orders"
                })
             pr_all_url = self.ins._server._url({"mode": "curd_exportall","type":"products", "insrender": "app"})

             more_menu.append({
                    "_type": "a",
                    "target": "blank",
                    "href": pr_all_url,
                    "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i>  Export all products"
                })
        
        
        else:
            
            more_menu.append({
                "_type": "a",
                "target": "blank",
                "href": ex_url,
                "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i> {self.__w('export')}"
            })


            more_menu.append({
                "_type": "a",
                "target": "blank",
                "href": ex_all_url,
                "_data": f"<i class='lni ins-icon app-crud-list-mdelete lni-download-1'></i> {self.__w('export_all')}"
            })
        more_menu.append({
            "_type": "a",
            "target": "blank",
            "href": p_url,
            "_data": f"<i class='lni ins-icon app-crud-list-printer lni-printer'></i> {self.__w('print')}"
        })
        more_menu.append({"_type": "li", "class": "ins-separator ins-line"})
        more_menu.append({
            "_type": "li",
            "_data": f"<a href='{s_url}'><i class='lni ins-icon app-crud-list-settings lni-gears-3'></i> {self.__w('settings')} </a>"
        })
        more_menu.append({
            "_type": "li",
            "_data": f"<a href='{t_url}'><i class='lni ins-icon app-crud-list-mdelete lni-trash-3'></i> {self.__w('trash')} </a>"
        })
        more_menu.append({"_type": "ul", "end": True})
        more_menu.append({"end": True})


        search = {"class": "ins-flex-grow"}
        main_fliter = {}
        fdata = self.__filter_data_url()
        for k in self.ops._list_filter:
            if "main" in k and k["main"] == True:
                main_fliter = k

            if len(main_fliter) > 0 and "name" in main_fliter.keys():

                search = {"_type": "input", "data-to": main_fliter["name"], "placeholder": "search....", "pclass": "ins-flex-grow",
                          "name": main_fliter["name"],
                          "class": "ins-radius-xl -crud-list-search-txt  ins-col-12 ins-bg-none", "style": "height: 35px;min-height: 35px;border: none"}
                if main_fliter["name"] in fdata:
                    search["value"] = fdata[main_fliter["name"]]

        # self._list_settings

        lss = {}
        if len(self.ops._list_settings) > 0 and "crud" in self.ops._list_settings:

            _value = ""

            if "inscl" in self.ins._server._get():
                _value = self.ins._server._get("inscl")
            _data = {}
            for k, v in self.ops._list_settings["crud"].items():
                t = k
                if "title"  in v:
                    t = v["title"]
                _data[k] = t

            lss = {"_type": "select", "name": "lss", "value": _value, 
               "class": "app-crud-list-name-slc", "fl_data": _data}

        header = [
            {"class": "ins-col-grow  ins-padding-m  ins-flex-center", "_data": [
                {"start": True,   "class": "    ins-col-12 -header-searh-group  ins-group ins-flex  "},
                search,



                {"style": "width:35px", "_data": [
                 {"class": "lni ins-icon  app-crud-list-search-btn   lni-search-text ins-padding-s"}], "class": "ins-button     "},
                {"style": "width:4px",  "class": "ins-border ins-border-left    "},

                {"style": "width:35px", "_data": [
                 {"_type": "a", "href": reload_url, "class": "lni ins-icon  lni-refresh-circle-1-clockwise ins-padding-s"}], "class": "ins-button     "},
             
             
             
               {"style": "width:35px", "_data": [
                 {"class": " ins-icons-ai ins-icons  app-crud-list-ai-btn   ins-padding-s"}], "class": "ins-button   ins-flex-center   "},
        
                {"style": "width:65px", "_type": "a", "href": add_url, "_data": [
                    {"class": "lni ins-icon lni-plus ins-primary-color ins-padding-s"},
                    {"_data": " ADD ",
                     "class": "ins-flex-grow ins-font-s  ins-primary-color ins-strong"}
                ], "class": "ins-button ins-gap-o ins-flex  "},

                lss,

                {"style": "width:35px", "_data": more_menu, "class": "ins-button  "},
                {"end": True}
            ]}]

        self.ins._tmp._set_page_des(self.ins._ui._render(header))
        ui = [
            {"class": "ins-col-12 app-crud-body ins-padding-xl insaction ",  "data-cname": self.ops._table, "data-plgin": "ins_plg_py_crud",
                "data-insaction": "plgin", "_data": self._body()},
            {"class": "ins-col-12", "_data": self._filter_ui()},
            
            
            {"class": "ins-col-12", "_data": self._filter_ai()}

            
        ]
        return self.ins._ui._render(ui)
    
    
    def _filter_ai(self):




        inp = [
               
               
            
             {"start": "true", "class": "ins-flex-center ins-padding-l ins-col-12"},
             
            { "class": "ins-flex ins-col-12 app-crud-list-ai-body" ,"style":'    height: calc(100vh - 260px);  overflow: auto;'},

            
            {"start": "true", "class": "ins-flex-end  ins-bg ins-border ins-radius-xl ins-col-12"},
            {"_type": "input", "type": "textarea","style":"height:100px",
                "pclass": "ins-col-12", "placeholder":"Message Insya", "class": "ins-input-none  app-crud-list-ai-txt"},
            {"class": "ins-col-1 lni lni-upload-circle-1 app-crud-list-ai-send-btn ins-button-icon  ins-primary"},
            {"class": "ap-ai-data ins-col-12 ins-bg-2"},
            {"end": "true"},
            {"end": "true"}
        ]


        ui = [
            {"start": "true", "class": " ins-fixpanel-end -crud-list-ai-panel ",
                "style": "width:80%"},
            {"class": " ins-header ins-flex-space-between", "_data": [
                {"class": "ins-title-m",
                    "_data":  '<i class=" ins-icon  lni lni-magnifier"></i>'+self.ins._langs._get("chat with insya", "crud") },
                {"class": "-crud-list-ai-close-btn ins-button-text-danger  lni  lni-xmark"}, ]},
            {"start": "true", "class": " ins-col-12 ins-filter-body ",
             
                "style": "background: var(--ins-color-4);border-radius: 5px;margin-top: 10px;"},


        ]
        

        ui +=inp

        ui.append({"end": "true"})

        return self.ins._ui._render(ui)
    
    

    def _filter_ui(self):

        fdata = self.__filter_data_url()

        for fpro in self.ops._list_filter:
            if "class" not in fpro:
                fpro["class"] = " "
            fpro["class"] += f" filter-item-{fpro["name"]}"
            if fpro["name"] in fdata:
                fpro["value"] = fdata[fpro["name"]]

        url = self.ins._server._url({}, remove=["filter"])
        filter = [{"start": "true", "_type": "form", "data-url": url, "method": "post",
                   "data-url": "", "class": " ins-col-12 -crud-list-filter-area ins-flex"}]
        filter += self.ops._list_filter

        filter_footer = [


            {"start": "true", "class": "ins-flex-center ins-padding-xl ins-col-12"},
            {"class": "ins-line ins-col-12"},
            {"_data": "Reset",   "_type": "a", "href": url,
                "class": "ins-button -crud-list-fliter-reset-btn ins-col-4"},
            {"_data": "Search",
                "class": "ins-button ins-primary -crud-list-filter-update-btn ins-col-4"},
            {"end": "true", "class": "ins-flex ins-col-12"},
            {"end": "true", "_type": "form"},
        ]

        filter += filter_footer

        ui = [
            {"start": "true", "class": " ins-fixpanel-end  -crud-list-filter-panel ",
                "style": "width:600px"},
            {"class": " ins-header ins-flex-space-between", "_data": [
                {"class": "ins-title-m",
                    "_data":  '<i class=" ins-icon  lni lni-magnifier"></i>'+self.ins._langs._get("filter", "crud") },
                {"class": "-crud-list-filter-close-btn ins-button-text-danger  lni  lni-xmark"}, ]},
            {"start": "true", "class": " ins-col-12 ins-filter-body  ins-padding-xl ",
             "_data": filter,
                "style": "background: var(--ins-color-4);min-height: calc(98% - 70px);border-radius: 5px;margin-top: 10px;verflow: auto;height: calc(100% - 200px);"},


        ]

        ui.append({"end": "true"})
        return self.ins._ui._render(ui)

      #  return '/div><i class="ins_close ins-close  lni  lni-xmark"></i></div><div class=" ins-data  " style="position: relative;top: 0;">xxx</div></div></div>'

    def __update_body_item(self, ops, v):
        if "_view" in ops:
            rv = self.ins._ui._format(ops, v)
        elif "_type" in ops and ops["_type"] == "tags":

            tg = ""
            if v["kit_tags"] != "":
                tgs = v["kit_tags"].split(",")
                for t in tgs:
                    db_tg = self.__tags(t)

                    turl = self.ins._server._url({"f": f"tag={db_tg["id"]}"})
                    tg += f"<b style='background:{db_tg["color"]}' class='ins-tag ins-flex-center ins-text-center '><span class='app-crud-list-remove-tag-actions ins-flex-center'><a class='ins-button-text' href='{
                        turl}'><i class='lni ins-font-l  lni-search-text'></i> </a><i data-oid='{v["id"]}'  data-mid='{db_tg["id"]}' data-obj='{self.ops._table}'   class='lni ins-button-text-danger  ins-font-l  app-crud-list-remove-tag lni-xmark'></i></span> {db_tg["title"]}</b>"

            mclass = f"_{self.ops._table}_{v["id"]}_tags"

            rv = f"<div class='ins-flex ins-k-tags-area {mclass} ins-col-12'><i data-oid='{v["id"]}' data-obj='{
                self.ops._table}' class='lni ins-button-text app-crud-list-add-tag  lni-bookmark-circle'></i>{str(tg)}</div>"
        elif "_type" in ops and ops["_type"] == "method":
            #area = self.ins._this._area["url"]
            #type = "ins_apps"
            ds = ops["_data"].split(".")
            _path = f'{ds[0]}.{ds[1]}.{ds[2]}.{ds[2]}'
            _class_name = self.ins._map._get_class_name(ds[2])
            exec(f"from {_path} import {_class_name}")
            rv = eval(f"{_class_name}.{ds[3]}(self.ins,ops,v)")
        else:
            rv = str(v)
        return rv

    def _pgs_bar(self):
        pcount = self.__list_count / self.ops._list_limit
        pcount = math.ceil(pcount)
        
        
        n = int(self.__page)+1
        e = int(pcount)
        next_url = self.ins._server._url({"page": str(n)})
        end_url = self.ins._server._url({"page": str(e)})
        p = int(self.__page)-1
        prv_url = self.ins._server._url({"page": str(p)})
        start_url = self.ins._server._url({}, remove=["page"])
        ps = {}
        if pcount > 1:
            for i in range(1, (pcount+1)):
                ps[str(i)] = str(i)
        plui = {"_type": "select",


                "data-url": start_url,

                "class": "ins-text-center app-crud-list-page-slct  ins-form-input",
                "value": str(self.__page), "fl_data": ps,        "style": "height: 10px;min-height: 30px; line-height: 30px !important;width:80px"
                }

        nui = {"_type": "a",    "href": next_url, "class": "lni lni-chevron-left ins-text-center",
               "style": "width:35px; transform: rotate(180deg);"}
        dnui = {"_type": "i", "class": "lni lni-chevron-left ins-text-center",
                "style": "width:35px;opacity:0.3;transform: rotate(180deg);"}
        eui = {"_type": "a", "href": end_url,  "class": "lni lni-shift-left  ins-text-center",
               "style": "width:35px; transform: rotate(180deg);"}
        deui = {"_type": "i", "class": "lni lni-shift-left  ins-text-center",
                "style": "width:35px;opacity:0.3;transform: rotate(180deg);"}
        sui = {"_type": "a", "href": start_url,
               "class": "lni lni-shift-left", "style": "width:35px"}
        dsui = {"_type": "i",  "class": "lni lni-shift-left",
                "style": "width:35px;opacity:0.3"}
        pui = {"_type": "a",  "href": prv_url, "class": "lni ins-padding-l lni-chevron-left ins-text-center",
               "style": "width:35px"}
        dpui = {"_type": "i", "class": "lni ins-padding-l lni-chevron-left ins-text-center",
                "style": "width:35px;opacity:0.3"}
        if e <= self.__page:
            next = [plui, dnui, deui]
        elif pcount > 1:
            next = [plui, nui, eui]
        else:
            next = [dnui, deui]
        if pcount > 1 and self.__page > 1:
            prv = [sui, pui]
        else:
            prv = [dsui, dpui]
        pgs = []
        pgs += prv
        pgs += next
        cdata = [
            {"_data": " ", "style": "width:25px"},
            {"_type": "select", "class": "ins-text-center app-crud-list-page-count-slct   ins-form-input",

             "value": str(self.ops._list_limit), "fl_data": {"6": "6", "12": "12", "24": "24", "50": "50", "70": "70", "100": "100", "120": "120"},

             "style": "height: 10px;min-height: 30px; line-height: 30px !important;width:80px"

             }, {"_data": f" / {self.__list_count}", "class": ""}
        ]
        ui = [
            {"class": "  ins-flex-grow ins-no-print   app-crud-list-status-bar", "_data": f"<span class='-status-bar-select-info' ></span><span class='ins-font-s ins-padding-xl ins-padding-h  -status-bar-footer-info' >{
                self._footer_info}</span><span class='ins-font-s ins-padding-xl ins-padding-h  -status-bar-fliter-info' >{self._filter_info()}</span> "},
            {"class": "  ins-flex", "_data": pgs},
            {"class": "  ins-flex", "_data": cdata},
            {"class": "  "}
        ]
        return ui

    def _filter_info(self):
        r = ""
        fs = self.__filter_data()
        for f in fs:
            if f == "tag":

                tsg = self.__tags(fs[f]["value"])
                r = f" Tag :{tsg["title"]}"

                return r

            tf = fs[f]
            if "_info" in tf["ops"]:
                tr = tf["ops"]["_info"]
                tr = self.ins._langs._update(tr, tf)
                r += tr
        return r

    def _body(self):
        f = self.__filter_to_query()
        data = self.__get_data(f)
        ui = []
        if len(data) == 0:
            ui.append({
                "data-insaction": "plgin",
                "data-plgin": "ins_plg_py_crud",
                "_data": "No data To show",
                      "class": "ins-message  insaction ins-danger"})
            return self.ins._ui._render(ui)
        header = []
        for h in self.ops._list_data:
            if "_trans" in h:
                    h = self.ins._langs._render_tags(h)
            
            hr = {}
            url = ""
            if "name" in h:
                url = self.ins._server._url(
                    {"orderby": h["name"], "ordertype": "desc"}, ["mode", "page", "id"])

            if self.ins._server._get("ordertype") == "desc":
                if "name" in h:

                    url = self.ins._server._url(
                        {"orderby": h["name"], "ordertype": "asc"}, ["mode", "page", "id"])
            if url != "":
                if self.ins._server._get("orderby") == h["name"]:
                    if self.ins._server._get("ordertype") == "desc":
                        self._footer_info = f"Order By <b>{
                            h["title"]}</b> Desc"
                        h["title"] += "  <span class=' lni lni-chevron-down'></span>"

                    else:
                        self._footer_info = f"Order By <b>{h["title"]}</b> Asc"

                        h["title"] += "  <span class=' lni lni-chevron-up'></span>"

                hr["_data"] = f"<a href='{url}'>{h["title"]}</a>"
            else:
                hr["_data"] = h["title"]

            hr["class"] = h.get("class")
            header.append(hr)
      # add Actions Header Label
        header.append({"_data": "actions", "class": "ins-col-1 ins-no-print _actions"})
        # add Selector all ui to Header
        header[0]["_data"] = f"<span class='ins-raw-selector-all ins-no-print' ></span>{
            header[0]["_data"]}"
        body = []
        for d in data:
            rd = []
            for h in self.ops._list_data:
                hr = {}
                data = d
                if "name" in h:
                    data = d.get(h["name"] ,"")

                hr["_data"] = self.__update_body_item(h, data)
                hr["class"] = h.get("class")
                rd.append(hr)
            # add Actions  to  row
            rd.append(self._actions(d["id"]))
            # add Selector ui to  row
            rd[0]["_data"] = f"<span data-id='{d["id"]}' class='ins-raw-selector ins-no-print' ></span>{
                rd[0]["_data"]}"
            body.append(rd)
        # craete ui

        ui = [
            {"_type": "table", "data": body, "header": header,
             "class": " ins-col-12 ins-table ins-date-table ins-pading-xl "},
            {"_data": self._pgs_bar(),
             "class": " ins-col-12 ins-margin-l ins-margin-top ins-no-print  ins-flex app-crud-list-bottom-bar"}
        ]
        return self.ins._ui._render(ui)

    def __w(self, name):
        return self.ins._langs._get(name, "crud")

    def render(self):
        def update():
            return self._body()

        actions = APPCRUDActions(self)
        
       
        
        if self.ins._server._get("mode") == "curd_list_delete":
            return actions._delete(update)
        if self.ins._server._get("mode") == "curd_list_ai":
            return actions._ai(self.ops)
        if self.ins._server._get("mode") == "curd_list_copy":
            return actions._copy(update)
        if self.ins._server._get("mode") == "curd_list_body":
            return self._body()
        
        
        if self.ins._server._get("mode") == "curd_export":
            f = self.__filter_to_query()
            exdata =self.__get_data(f) 
            if self.ops._list_export != None:
                exdata = self.ops._list_export(exdata)
            return actions._export(exdata, self.ops._table)
        if self.ins._server._get("mode") == "curd_exportall":
            f = self.__filter_to_query()
            
            exdata =self.__get_data(f, no_limit=True) 
            if self.ops._list_export_all!= None:
                exdata = self.ops._list_export_all(exdata)
            return actions._export(exdata, self.ops._table)
        



        l = self._list()
        return l
