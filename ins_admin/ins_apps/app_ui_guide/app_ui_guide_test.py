from ins_kit._engine._bp import App

# from openai import OpenAI
import json


class AppUiGuideTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def _input(self):

        d = [
            ["Element", "Density", {"role": "style"}],
            ["Copddddper", 8.94, "#b87333"],
            ["Silver", 10.49, "silver"],
            ["Gold", 19.30, "gold"],
            ["Platinum", 21.45, "color: #e5e4e2"]
        ]


        e=[
                    ['Task', 'Hours per Day'],
                    ['Work', 11],
                    ['Eat', 2],
                    ['Commute', 2],
                    ['Watch TV', 2],
                    ['Sleep', 7]
                ]

        uidata = [

          {"_type": "chart","type":"ddd", "data": e, "style":"height:500px",
                "class": "ins-col-8  ins-flex  ins-padding-xl"},
 {"_type": "chart","type":"pie", "data": d, "style":"height:500px",
                "class": "ins-col-4  ins-flex  ins-padding-xl"},

        ]
        r = self.ins._ui._render(uidata)
        return r

    def out(self):

        r = self._input()
        return r
