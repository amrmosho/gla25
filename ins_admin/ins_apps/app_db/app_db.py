from ins_kit._engine._bp import App

import re


class AppDb(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _del(self):
        p = self.ins._server._get()

        p = self.ins._server._post()
        q = ""
        r = ""
        if p["g"] == "ttable":
            q = f"TRUNCATE TABLE {p["t"]}"
            self.ins._db._set_query(q)
            r = self.dbs("table")
            
        elif p["g"] == "dtable":
            q = f"DROP TABLE {p["t"]}"
            self.ins._db._set_query(q)
            r = self.dbs("table")
        
        
        elif p["g"] == "dftable":
            q = f"ALTER TABLE `{p["t"]}` DROP `{p["f"]}`"
            a=self.ins._db._set_query(q)
            self._g = {"id" :p["t"] ,"mode":"set"}
            r = self.dbs("set")
            
        elif p["g"] == "ditem":
            q = f"DELETE FROM `{p["t"]}`  WHERE  id='{p["tid"]}'"
            a =self.ins._db._set_query(q)
            self._g = {"id" :p["t"] ,"mode":"data"}
            r = self.dbs("data")       
            
            
        
        

     
        
    
        return r

    def _q(self):
        p = self.ins._server._post()
        q = ""
        if p["g"] == "ctable":
            q = 'CREATE TABLE `$table_name` (\n `id` int(11) NOT NULL,\n`title` varchar(255) NOT NULL,\n `des` text DEFAULT NULL,\n`kit_deleted` tinyint(4) NOT NULL DEFAULT 0,\n`kit_disabled` tinyint(4) NOT NULL DEFAULT 0,\n`kit_modified` datetime NOT NULL,\n`kit_created` datetime NOT NULL\n) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;\nALTER TABLE `$table_name`  ADD PRIMARY KEY (`id`);\nALTER TABLE `$table_name` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT; COMMIT;'
        
        if p["g"] == "ccol":
            q = f' ALTER TABLE `{p["t"]}` ADD $column_name varchar(255);'
       
        if p["g"] == "rcol":
            q = f' ALTER TABLE `{p["t"]}` CHANGE   {p["f"]}   $new_column_name varchar(255);'
            
        if p["g"] == "mcol":
            q = f' ALTER TABLE `{p["t"]}` MODIFY {p["f"]}   varchar(255);'
        
        if p["g"] == "insert":
            
            ds = self.ins._db._get_query(f"DESCRIBE {p["t"]}")
            f = ""
            sp = ""
            v = ""

            for d in ds :
                f += f'{sp}`{d["Field"]}`'
                if d["Field"] =="id":
                    v += f'{sp}NULL'
                elif "int" in d["Type"]:
                    v += f'{sp}0'
                    
                elif "datetime" in d["Type"]:
                    v += f'{sp}\'{self.ins._date._date_time()}\''
                else:
                    v += f'{sp}\'${d["Field"]}_val\''

                sp =","
                
                
                
                
            q = f'INSERT INTO `{p["t"]}` ({f}) VALUES ({v})'   
          
          
        if p["g"] == "update":
  
            ds = self.ins._db._get_query(f"Select *  from {p["t"]} where id='{p["tid"]}' ")
            sp = ""
            f=""
            
            for k,v in  ds[0].items():
                    f += f'{sp}`{k}`=\'{v}\''
                    sp =","


            q = f'UPDATE  `{p["t"]}` SET {f} where id=\'{p["tid"]}\' '

        """                UPDATE `table_name` SET `id`='[value-1]',`title`='[value-2]' WHERE 1"""
        """INSERT INTO `kit_content`(`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]')"""
        """UPDATE `kit_content` SET `id`='[value-1]',`title`='[value-2]',`content`='[value-3]',`kit_deleted`='[value-4]',`kit_disabled`='[value-5]',`kit_modified`='[value-6]',`kit_created`='[value-7]' WHERE 1 """
       
        return q

    def _q_l(self, ds, mode=""):
        keys = []
        for d in ds:
            for k in d:
                keys.append(k)
            break

        header = []
        if len(keys) ==0 :
            return "no data"
        a = (90/len(keys))
        for k in keys:
            header.append({"class": "", "style": f"width:{a}%;    min-width: 200px;", "_data": k})
        header.append({"class": "ins-col-grow",
                      "style": "width:90px", "_data": "actions"})
        body = []

        for d in ds:
            r = []
            for k in keys:
                v = str(d[k])
                clean = re.compile('<.*?>')
                v = re.sub(clean, '', v)
                r.append({"class": "", "style": f"width:{
                         a}%", "_data": v[:50]})

            actions = ""

            if mode == "table":
                tbl = str(d[k])
                url = self.ins._server._url({"area":"ins_admin", "alias":"db", "id": tbl, "mode":  "data"})
                surl = self.ins._server._url({"area":"ins_admin", "alias":"db","id": tbl, "mode":  "set"})
                actions = f"<a  title='show data' class='ins-padding-m ins-button-text' href='{url}'><i class='lni lni-arrow-right'></i></a>"
                actions += f"<a title='settings'  class='ins-padding-m ins-button-text' href ='{surl}'><i class='lni lni-gears-3'> </i></a>"
                actions += f"<span data-m='Are you user you want empty {tbl} table?' data-g='ttable' data-t='{tbl}'  title='empty' class='ins-padding-m   -db-s-del ins-button-text-danger' ><i class='lni ins-button-text-danger lni-crop-2'> </i></span>"
                actions += f"<span data-m='Are you user you want drop {tbl} table?' data-g='dtable' data-t='{ tbl}' title='delete' class='ins-padding-m  -db-s-del ins-button-text-danger'><i class='lni ins-button-text-danger lni-xmark'> </i></span>"



            elif mode == "set":
                tbl =self._g.get("id")
                actions = f"<span  data-t='{tbl}' data-f='{str(d["Field"])}' data-g='mcol'  class='ins-button-text  ins-padding-m db-get-q'> <i class='lni  lni-gears-3'></i>  </span>"
                actions += f"<span  data-t='{tbl}' data-f='{str(d["Field"])}' data-g='rcol'  class='ins-button-text ins-padding-m db-get-q'> <i class='lni  lni-www-cursor'></i>  </span>"
                actions += f"<span data-m='Are you user you want drop {tbl} table?' data-g='dftable' data-t='{tbl}' data-f='{str(d["Field"])}'  title='delete' class='ins-padding-m  -db-s-del ins-button-text-danger'><i class='lni ins-button-text-danger lni-xmark'> </i></span>"

   
            elif mode == "data":
                tbl =self._g.get("id")
                actions = f"<span  data-t='{tbl}' data-tid='{str(d["id"])}' data-g='update'  class='ins-button-text  ins-padding-m db-get-q'> <i class='lni  lni-pencil-1'></i>  </span>"
                actions += f"<span data-m='Are you user you want drop {tbl} table?' data-g='ditem' data-t='{tbl}' data-tid='{str(d["id"])}'  title='delete' class='ins-padding-m  -db-s-del ins-button-text-danger'><i class='lni ins-button-text-danger lni-xmark'> </i></span>"



                    

            r.append({"class": "ins-col-grow",  "_data": actions})

            body.append(r)

        ui = [{"_type": "table",
               "class": " ins-col-12 ins-table ins-table-regular ins-pading-xl ", "data": body, "header": header}]
        return self.ins._ui._render(ui)

    def _update_q(self):

        p = self.ins._server._post()
        self._g = self.ins._server._post()
        ds = self.ins._db._get_query(p["q"],True)
        if type(ds) == list:
            return self._q_l(ds)
        else:
            
            cl  = "ins-info" 
            if "error" in ds.lower():
                cl  = "ins-danger" 
            ui=[{"_data":ds ,"class":f"ins-message ins-padding-xl ins-col-12  {cl}"}]
            return self.ins._ui._render(ui)

    def _get_data(self):
        p = self.ins._server._post()
        return self.dbs(p["g"])

    def dbs(self, mode ="table"):

        if mode == "data":
            q = f" select * from  `{self._g.get("id")}`  limit 0,100"
        elif mode == "set":
            q = f"  DESCRIBE `{self._g.get("id")}` "
        else:
            q = " show tables "

        ds = self.ins._db._get_query(q)
        return self._q_l(ds, mode)

    def ui(self):

        m= self._g.get("mode", "table")

        if m =="data":
            
            url = self.ins._server._url({},["mode" ,"id"])
            title = f"Select  {self._g.get("id", "table")}"
            actions = f"<a href='{url}' class='ins-button-text'> <i class='lni  lni-arrow-left'></i> Back </a> <span  data-t='{self._g.get("id", "table")}'  data-g='insert'   class='ins-button-text db-get-q'> <i class='lni  lni-plus'></i> Insert </span>"



        elif m =="set":
            
            url = self.ins._server._url({},["mode" ,"id"])
            title = f"Select  {self._g.get("id", "table")}"
            actions = f"<a href='{url}' class='ins-button-text'> <i class='lni  lni-arrow-left'></i> Back </a> <span data-t='{self._g.get("id", "table")}' data-g='ccol'  class='ins-button-text db-get-q'> <i class='lni  lni-plus'></i> Add Field </span>"



        else: 
            title = "Show Tables"
            actions = "<span data-g='ctable'  class='ins-button-text db-get-q'> <i class='lni  lni-plus'></i> Add Table </span>"

        ui = [
            {"start": True, "class": "ins-flex "},
            {"start": True, "class": "ins-flex-end ins-card ins-col-12 ins-padding-xl"},
            {"_type": "input", "type": "textarea",
                "pclass": "ins-col-12", "title": "sql", "class": "-db-sql-input"},
            {"class": "ins-col-2 ins-button -db-reload-btn ",  "_data": "Reload"},
            {"class": "ins-col-2 ins-button -db-sql-update-btn ins-primary",
                "_data": "Run"},
            {"end": True},
            {"start": True, "class": "ins-flex-end ins-col-12 ins-padding-xl "},
            {"class": "  isn-title-l ins-col-12 ins-flex ins-card ins-strong ins-bg-2",
                "_data": f"<span class='ins-col-grow'>{title}</span>{actions} "},
            {"class": "ins-flex ins-col-12 db-res",
                "_data": self.dbs(m)},
            {"end": True},
            {"end": True},

        ]

        return self.ins._ui._render(ui)

    def out(self):
        self.app._include("script.js")
        self._g = self.ins._server._get()
        return self.ui()
