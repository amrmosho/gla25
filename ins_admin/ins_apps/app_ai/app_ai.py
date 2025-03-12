from ins_kit._engine._bp import App


class AppAi(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

   # create a component  'employees' type 'component' and  make it item in menu and no data contains:  name (text), position (text), and hire_date (date)
   #create a table 'employees' and don't add system fields,add id contains:  name (text), position (text), and hire_date (date)


    def _component(self,response_data):
        
        sql = f'create _component {response_data["name"]}'
        return sql
    def _sql(self,response_data):
        
        table_name =response_data["name"]
        
        sql = f'CREATE TABLE `{table_name}` ( `id` int(11) NOT NULL,'

        for f in  response_data["fields"]:
           
            type= 'varchar(255)'
            if f["type"] =="text":
                type= 'text'
            elif f["type"] =="datetime":
                type= 'datetime'
            elif f["type"] =="date":
                type= 'date'       
                
                
            sql += f'`{f["name"] }` {type} NOT NULL, <br/>'
         
        
        add_kit = True
       # for o in  response_data["options"]:
        if "kit" in  response_data["options"] or "system" in  response_data["options"]:
                add_kit =False
            
        if add_kit:
            sql += '`kit_deleted` tinyint(4) NOT NULL DEFAULT 0, <br/>'
            sql += '`kit_disabled` tinyint(4) NOT NULL DEFAULT 0, <br/>'
            sql += 'kit_modified` datetime NOT NULL, <br/>'
            sql += '`kit_created` datetime NOT NULL <br/>'
        sql += ')'
        
        
        sql += f'ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci; ALTER TABLE `{table_name}`  <br/>  ADD PRIMARY KEY (`id`); ALTER TABLE `{table_name}`  <br/> MODIFY `id` int(11) NOT NULL AUTO_INCREMENT; COMMIT;'
        return sql
    
    
    

    
    
    def _get(self):
        rq = self.ins._server._post()
        response_data = self.ins._ai._get(rq["v"])
        
        
        """
            if response_data["type"]=="table":
                response_data["output"] =self._sql(response_data)
            elif response_data["type"]=="component":
                response_data["output"] =self._component(response_data)
        """
            
        return response_data

    def out(self):

        self.app._include("script.js")
        uidata = [
            {"start": "true", "class": "ins-flex-center ins-col-12"},
            {"start": "true", "class": "ins-flex-end ins-card ins-col-6"},
            {"_type": "input", "type": "textarea","style":"height:300px",
                "pclass": "ins-col-12", "class": "ap-ai-txt", "title": "chat with insya"},
            {"_data": "send", "class": "ins-col-1 ap-ai-btn ins-button ins-primary"},


            {"class": "ap-ai-data ins-col-12 ins-bg-2"},

            {"end": "true"},
            {"end": "true"}
        ]
        r = self.ins._ui._render(uidata)
        return r
