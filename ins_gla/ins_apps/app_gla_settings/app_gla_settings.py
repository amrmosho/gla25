import json
from uuid import uuid4
from ins_kit._engine._bp import App


class AppGlaSettings(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)




       
    def _remove_item(self):
        rq = self.ins._server._req()
        uid = rq.get("uid")

        if not uid:
            return ""
        data = {}
        if "area" in rq and rq["area"]:
            try:
                data = json.loads(rq["area"])
            except json.JSONDecodeError:
                pass

        if isinstance(data, list):
            data = [item for item in data if item.get("uid") != uid]

        return json.dumps(data)


    def _fill_messages(self):
        data = self.ins._db._get_row("gla_settings", "order_msg,order_msg_ar",  "1=1")

        return data

    def _fill_time_area(self):

        data = self.ins._db._get_row("gla_settings", "times", "1=1")
        uidata = []
        if data:
            jdata = json.loads(data["times"])
            for v in jdata:
                  uid = v["uid"]
                  uidata += [
            {"start":"true","class":"ins-col-12 ins-flex ins-padding-m -times-row ins-card ins-padding-l","data-uid":uid},
  {
            "name": "from",
            "title": "From",
            "_type": "input",
            "type":"text",
            "value":v["from"],
            "required": "true",
            "pclass": "ins-col-5",
            "class": "-from-time"
        },
 {
            "name": "to",
            "title": "To",
            "_type": "input",
                        "value":v["to"],

            "type":"text",
            "required": "true",
            "pclass": "ins-col-5",
            "class": "-to-time"
        },

     {"data-uid":uid,"class":"ins-button-icon ins-col-1 lni lni-xmark -remove-item ins-danger ins-font-xl","style":"    position: relative;top: 15px;"}
,{"end":"true"}
,{"class":"ins-space-l"}


                ]
                    
            r = {}

            r["textarea"] = data["times"]
            r["ui"] = self.ins._ui._render(uidata)
        else:
            r = {}
            r["textarea"] = ""
            r["ui"] = self._add_new_item()
        return r




    def _update_times(self):
        rq = self.ins._server._req()
        data = {}
        if "area" in rq and rq["area"]:
            try:
                data = json.loads(rq["area"])
            except json.JSONDecodeError:
                pass

        new_data = {
            "uid": rq["uid"],
            "from": rq["from"],
            "to": rq["to"]
        }

        if isinstance(data, list):
            for item in data:
                if item["uid"] == new_data["uid"]:
                    item.update(new_data)
                    break
            else:
                data.append(new_data)
        else:
            data = [new_data]

        return json.dumps(data)
    



    def _add_new_item(self):
        uid = uuid4().hex
        uidata = [
            {"start":"true","class":"ins-col-12 ins-flex ins-padding-m -times-row ins-card ins-padding-l","data-uid":uid},
  {
            "name": "from",
            "title": "From",
            "_type": "input",
            "type":"text",
            "required": "true",
            "pclass": "ins-col-5",
            "class": "-from-time"
        },
 {
            "name": "to",
            "title": "To",
            "_type": "input",
            "type":"text",
            "required": "true",
            "pclass": "ins-col-5",
            "class": "-to-time"
        },

     {"data-uid":uid,"class":"ins-button-icon ins-col-1 lni lni-xmark -remove-item ins-danger ins-font-xl","style":"    position: relative;top: 15px;"}
,{"end":"true"}
,{"class":"ins-space-l"}


                ]
        
        return self.ins._ui._render(uidata)
        

    def out(self):
        self.app._include("script.js")
        r = self.ins._apps._crud(properties=self.app._properties)
        return r