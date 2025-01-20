from ins_kit._engine._bp import App


class AppTags(App):
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
                "class": "ins-col-5"
            },            {
                "name": "color",
                "title": "Color",
                "_view": "color",
                "class": "ins-col-2"
            },  {
                "name": "obj",
                "title": "obj",
                "class": "ins-col-4"
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
                "required": "true",
                "pclass": "ins-col-12"
            },                 {
                "name": "color",
                "title": "color",
                "_type": "input",
                "type": "color",
                "pclass": "ins-col-12"
            },

            {
                "name": "obj",
                "title": "obj",
                "_type": "input",
                "type": "text",
                "pclass": "ins-col-12"
            },

            {
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

        ops._table = "kit_tags"

        r = self.ins._apps._crud(ops)
        return r
