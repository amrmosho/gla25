from ins_kit._engine._bp import Plgin
from ins_kit.ins_parent import ins_parent


class PlgComments(Plgin):

    def __init__(self, plg) -> None:
        self.plg: Plgin = plg
        super().__init__(plg.ins)

    def get_data(self, ps):
        r = []
        q = self.ins._db._jget(
            "plg_comments", "*", f"obj_id='{ps["obj_id"]}' and obj_type='{ps["obj_type"]}' order by plg_comments.id desc")
        q._jwith("kit_user u", "title,image",
                 "plg_comments.fk_user_id= u.id", join="left join")

        data = q._jrun()

        for d in data:
            ro = [
                {"start": "true", "class": "ins-flex ins-col-12 ins-padding-l"},


                {"start": "true", "class": "ins-flex ins-col-1 "},



                {"src": self.ins._map.UPLOADS_FOLDER +
                    d["u_image"], "_type": "img", "class": "ins-padding-s ", "style": "max-width: 100%;"},

                {"end": "true"},
                {"start": "true", "class": "ins-flex ins-col-11"},

                {"start": "true", "class": "ins-flex ins-col-12"},
                {"_data": d["u_title"], "class": "ins-font-m"},
                {"_data": d["kit_created"],
                    "class": "ins-font-s", "_view": "date"},
                {"end": "true"},
                {"_data": d["comment"],
                    "class": "ins-card ins-col-12 ins-border"},
                {"end": "true"},
                {"end": "true"},

            ]
            r += ro

        return self.ins._ui._render(r)

    def ajax(self):
        ps = self.ins._server._post()
        self.ins._db._insert("plg_comments", ps)
        return self.get_data(ps)

    def ui(self, obj_type, obj_id):
        dd = {"obj_type": obj_type, "obj_id": obj_id}
        r = [
            {"class": 'ins-col-12 ins-flex-end p-comments-data',
                "_data": self.get_data(dd)},

            {"start": "true", "class": 'ins-col-12 ins-flex-end p-comments-cont'},

            {"_type": "input", "type": "textarea", "required": "required",
                "title": 'Your comment *', "name": 'comment', "pclass": 'ins-col-12 ins-flex'},
            {"_type": "input", "type": "hidden", "name": "obj_type",
                "value": obj_type, "pclass": ' ins-hidden'},

            {"_type": "input", "type": "hidden", "name": "obj_id",
                "value": obj_id, "pclass": 'ins-hidden'},





            {"_type": "input", "type": "hidden", "name": "fk_user_id",
             "value": "1", "pclass": 'ins-hidden'},



            {"class": 'ins-col-12  ins-pading-l'},


            {"_data": "Post comment",
                "class": 'ins-col-3 p-comments-btn ins-gold-d ins-button'},

            {"end": "true"},


        ]

        return self.ins._ui._render(r)

    def out(self, obj_type, obj_id):
        return self.ui(obj_type, obj_id)
