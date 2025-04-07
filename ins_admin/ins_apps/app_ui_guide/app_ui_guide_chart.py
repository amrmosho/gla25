from ins_kit._engine._bp import App

# from openai import OpenAI
import json


class AppUiGuideCharts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def column(self, colors):
        uidata = []
        e = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]

        ops = {'legend': {'position': 'none'}, "colors": colors}

        infodata = """  e = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]
       ops = {'legend': {'position': 'none'}, "colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "ddd", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "ddd", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        e = [
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', {'role': 'annotation'}],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
            ['2020', 16, 22, 23, 30, 16, 9, ''],
            ['2030', 28, 19, 29, 30, 12, 13, '']
        ]
        ops = {'legend': {'position': 'top', "maxLines": 3},
               "isStacked": "true", "colors": colors}

        infodata = """  e = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]
       ops = {'legend': {'position': 'none'}, "colors": ["#3ba9b6"]} 
    
       [{"_type": "chart", "type": "ddd", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """

        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "ddd", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def out(self):

        uidata = []

        # Material Design Colors
        colors = ["#2196F3", "#F44336", "#4CAF50", "#FF9800",
                  "#9C27B0", "#009688", "#3F51B5"]
        # Pastel Colors (Soft on the eyes)
        colors = ["#A2C8E5", "#F8BBD0", "#B2DFDB", "#FFF9C4",
                  "#CE93D8", "#FFCCBC", "#3F51B5"]
        # Cool Modern Palette
        colors = ["#00BCD4", "#CDDC39", "#673AB7", "#FFC107",
                  "#03A9F4", "#9E9E9E", "#3F51B5"]

        colors = ["#FF3CAC", "#4FEEF4", "#00FFAB", "#A100F2",
                  "#FFA447", "#8D99AE", "#3F51B5"]

        # Colorblind Safe
        colors = ["#4477AA", "#66CCEE", "#228833",
                  "#CCBB44", "#EE6677", "#AA3377", "#BBBBBB"]

        d = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]

        infodata = """  d = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]
       ops = {"colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "pie", "data": d, "style": "height:500px",
             "class": "ins-col-12 ins-flex  ins-padding-xl"}] """

        ops = {"colors": colors}

        uidata += [

            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},

            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},

            {"_type": "chart", "type": "pie", "options": ops,  "data": d, "style": "height:500px",
             "class": "ins-col-12 ins-flex  ins-padding-xl"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
             "_data": infodata},

            {"end": "true"}


        ]

        r = self.column(colors)
        return r
