from ins_kit._engine._bp import App


class AppMcontent(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):
        ops = self.ins._apps._crud_ops
        ops._list_data = [
            {
                "name": "title",
                "title": "my title",
                "view": "text", 
                "class": "ins-col-grow"
            }
        ]
        ops._form_data = [
            {
                "start": True,
                "class": "ins-col-12 ins-flex ins-card"
            },
            {
                "name": "title",
                "title": "my title *",
                "_type": "input",
                "type": "text",
                "required":"true",
                "pclass": "ins-col-12"
            },                      {
                "name": "content",
                "title": "my content",
                "_type": "input",
                "_lang": "true",
            "_table": "kit_content",
                "type": "textarea",
                "style":"height:350px",
                "pclass": "ins-col-12"
            }, {
                "end": True
            }
        ]

        ops._list_filter = [{

            "name": "title",
            "title": "my title",
            "_type": "input",
            "type": "text",
            "operator": "=",
            "pclass": "ins-col-6"
        },            {
            "name": "content",
            "title": "my content",
            "_type": "input",
            "type": "text",
            "pclass": "ins-col-6"
        }


        ]


        def ex(data):
           
            for r in data:
               r["content"] ="xxxxxxx"
               del r["kit_lang"]
               
            return data
            


        ops._list_export =ex
        r = self.ins._apps._crud(ops)
        return r
