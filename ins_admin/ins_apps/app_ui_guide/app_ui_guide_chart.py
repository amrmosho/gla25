from ins_kit._engine._bp import App

# from openai import OpenAI
import json


class AppUiGuideCharts(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def org(self, colors):

        uidata = []

        e = [
            [{'v': 'Mike', 'f': 'Mike<div class=&quot; ins-danger-color &quot;>President</div>'},
                '', 'The President'],
            [{'v': 'Jim', 'f': 'Jim<div class=&quot; ins-info-color &quot;>Vice President</div>'},
             'Mike', 'VP'
             ],
            ['Alice', 'Mike', ''],
            ['Bob', 'Jim', 'Bob Sponge'],
            ['Carol', 'Bob', ''],
            ['Carosl', 'Jim', ''],
            ['Carosl', 'Bob', ''],


            ['Carosdfsdfdssl', 'Bob', ''],

            ['777', '', ''],



            ['88', '777', ''],
            ['99', '777', ''],

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
            {"_type": "chart", "type": "org", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]
        return self.ins._ui._render(uidata)

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
            ['Element', 'Density', {'role': 'style'}],
            ['Copper', 8.94, '#b87333'],
            ['Silver', 10.49, 'silver'],
            ['Gold', 19.30, 'gold'],
            ['Platinum', 21.45, 'color: #e5e4e2'],
        ]

        ops = {'legend': {'position': 'none'}, "colors": colors}

        infodata = """  e = [
            ['Element', 'Density', {'role': 'style'}],
            ['Copper', 8.94, '#b87333'],           
            ['Silver', 10.49, 'silver'],           
            ['Gold', 19.30, 'gold'],
            ['Platinum', 21.45, 'color: #e5e4e2'], 
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

      # ////////////////////////////////////////////////
        e = [
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', {'role': 'annotation'}],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
            ['2020', 16, 22, 23, 30, 16, 9, ''],
            ['2030', 28, 19, 29, 30, 12, 13, '']
        ]
        ops = {'legend': {'position': 'top', "maxLines": 3},
               "isStacked": "true", "colors": colors}

        infodata = """  
        e = [
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', {'role': 'annotation'}],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
            ['2020', 16, 22, 23, 30, 16, 9, ''],
            ['2030', 28, 19, 29, 30, 12, 13, '']
        ]
            
        ops = {'legend': {'position': 'top', "maxLines": 3},
               "isStacked": "true", "colors": colors}
    
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


# ////////////////////////////////////////////////
        e = [
            ['Year', 'Sales', 'Expenses', 'Profit'],
            ['2014', 1000, 400, 200],
            ['2015', 1170, 460, 250],
            ['2016', 660, 1120, 300],
            ['2017', 1030, 540, 350]
        ]
        ops = {"colors": colors}

        infodata = """  
        e = [
            ['Year', 'Sales', 'Expenses', 'Profit'],
            ['2014', 1000, 400, 200],
            ['2015', 1170, 460, 250],
            ['2016', 660, 1120, 300],
            ['2017', 1030, 540, 350]
        ]
            
        ops = { "colors": colors}
    
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

    def line(self, colors):

        uidata = []
        e = [
            ['Year', 'Sales', 'Expenses'],
            ['2004',  1000,      400],
            ['2005',  1170,      460],
            ['2006',  660,       1120],
            ['2007',  1030,      540]
        ]

        ops = {'legend': {'position': 'bottom'}, "colors": colors}

        infodata = """  e = [
          ['Year', 'Sales', 'Expenses'],
          ['2004',  1000,      400],
          ['2005',  1170,      460],
          ['2006',  660,       1120],
          ['2007',  1030,      540]
        ]
       ops = {  legend: { position: 'bottom' }, "colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "line", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "line", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        e = [
            ['Year', 'Sales', 'Expenses'],
            ['2004',  1000,      400],
            ['2005',  1170,      460],
            ['2006',  660,       1120],
            ['2007',  1030,      540]
        ]

        ops = {'curveType': 'function',  'legend': {
            'position': 'bottom'}, "colors": colors}

        infodata = """  e = [
          ['Year', 'Sales', 'Expenses'],
          ['2004',  1000,      400],
          ['2005',  1170,      460],
          ['2006',  660,       1120],
          ['2007',  1030,      540]
        ]
        ops = { 'curveType': 'function',  'legend': { 'position': 'bottom' }, "colors": colors} 
       
       [{"_type": "chart", "type": "line", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "line", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def stepped_area(self, colors):

        uidata = []
        e = [
            ['Director (Year)',  'Rotten Tomatoes', 'IMDB'],
            ['Alfred Hitchcock (1935)', 8.4,         7.9],
            ['Ralph Thomas (1959)',     6.9,         6.5],
            ['Don Sharp (1978)',        6.5,         6.4],
            ['James Hawes (2008)',      4.4,         6.2]
        ]

        ops = {'legend': {'position': 'bottom'},
               "isStacked": "true", "colors": colors}

        infodata = """  e = [
          ['Director (Year)',  'Rotten Tomatoes', 'IMDB'],
          ['Alfred Hitchcock (1935)', 8.4,         7.9],
          ['Ralph Thomas (1959)',     6.9,         6.5],
          ['Don Sharp (1978)',        6.5,         6.4],
          ['James Hawes (2008)',      4.4,         6.2]
        ]
        ops = { 'legend': { 'position': 'bottom' },          "isStacked": "true", "colors": colors} 
       
       [{"_type": "chart", "type": "stepped_area", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "stepped_area", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def pie(self, colors):

        uidata = []
        e = [
            ['Task', 'Hours per Day'],
            ['Work',     11],
            ['Eat',      2],
            ['Commute',  2],
            ['Watch TV', 2],
            ['Sleep',    7]
        ]

        ops = {"colors": colors}

        infodata = """  
        e =[
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]
        ops = { "colors": colors} 

       [{"_type": "chart", "type": "pie", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "pie", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        ops = {"colors": colors, "is3D": "true"}

        infodata = """  
        e =[
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]
        ops = { "colors": colors ,"is3D": "true"} 
       [{"_type": "chart", "type": "pie", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "pie", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        ops = {"colors": colors, "pieHole": "0.4"}

        infodata = """  
        e =[
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]
        ops = { "colors": colors ,"is3D": "true"} 
       [{"_type": "chart", "type": "pie", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "pie", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        ops = {"colors": colors, "pieSliceText": 'label', "slices": {"4": {
            "offset": "0.2"}, "12": {"offset": " 0.3"}, " 14": {"offset": "0.4"}, "15": {"offset": "0.5"}}}

        e = [
            ['Language', 'Speakers (in millions)'],
            ['Assamese', 13], ['Bengali', 83], ['Bodo', 1.4],
            ['Dogri', 2.3], ['Gujarati', 46], ['Hindi', 300],
            ['Kannada', 38], ['Kashmiri', 5.5], ['Konkani', 5],
            ['Maithili', 20], ['Malayalam', 33], ['Manipuri', 1.5],
            ['Marathi', 72], ['Nepali', 2.9], ['Oriya', 33],
            ['Punjabi', 29], ['Sanskrit', 0.01], ['Santhali', 6.5],
            ['Sindhi', 2.5], ['Tamil', 61], ['Telugu', 74], ['Urdu', 52]
        ]
        infodata = """  
        e =[
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]
        ops = { "colors": colors ,"is3D": "true"} 
       [{"_type": "chart", "type": "pie", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "pie", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def geo(self, colors):

        uidata = []
        e = [
            ['Country', 'Popularity'],
            ['Germany', 200],
            ['United States', 300],
            ['Brazil', 400],
            ['Canada', 500],
            ['France', 600],
            ['RU', 700]
        ]

        ops = {"colors": colors}

        infodata = """  
        e =[
          ['Country', 'Popularity'],
          ['Germany', 200],
          ['United States', 300],
          ['Brazil', 400],
          ['Canada', 500],
          ['France', 600],
          ['RU', 700]
        ]
        ops = { "colors": colors} 

       [{"_type": "chart", "type": "geo", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """

        uidata += [
            {"start": "true",  "class": "ins-col-12 ins-flex-center  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart",  "type": "geo", "data": e, "options": ops,
                "style": "width: 900px; height: 500px;", "class": ""},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def area(self, colors):

        uidata = []
        e = [
            ['Year', 'Sales', 'Expenses'],
            ['2004',  1000,      400],
            ['2005',  1170,      460],
            ['2006',  660,       1120],
            ['2007',  1030,      540]
        ]

        ops = {'legend': {'position': 'bottom'}, "colors": colors}

        infodata = """  e = [
          ['Year', 'Sales', 'Expenses'],
          ['2004',  1000,      400],
          ['2005',  1170,      460],
          ['2006',  660,       1120],
          ['2007',  1030,      540]
        ]
       ops = {  legend: { position: 'bottom' }, "colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "area", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "area", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def bar(self, colors):

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
       
       [{"_type": "chart", "type": "bar", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bar", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        e = [
            ['Element', 'Density', {'role': 'style'}],
            ['Copper', 8.94, '#b87333'],
            ['Silver', 10.49, 'silver'],
            ['Gold', 19.30, 'gold'],
            ['Platinum', 21.45, 'color: #e5e4e2'],
        ]

        ops = {'legend': {'position': 'none'}, "colors": colors}

        infodata = """  e = [
            ['Element', 'Density', {'role': 'style'}],
            ['Copper', 8.94, '#b87333'],           
            ['Silver', 10.49, 'silver'],           
            ['Gold', 19.30, 'gold'],
            ['Platinum', 21.45, 'color: #e5e4e2'], 
        ]
       ops = {'legend': {'position': 'none'}, "colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "bar", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bar", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

      # ////////////////////////////////////////////////
        e = [
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', {'role': 'annotation'}],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
            ['2020', 16, 22, 23, 30, 16, 9, ''],
            ['2030', 28, 19, 29, 30, 12, 13, '']
        ]
        ops = {'legend': {'position': 'top', "maxLines": 3},
               "isStacked": "true", "colors": colors}

        infodata = """  
        e = [
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', {'role': 'annotation'}],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
            ['2020', 16, 22, 23, 30, 16, 9, ''],
            ['2030', 28, 19, 29, 30, 12, 13, '']
        ]
            
        ops = {'legend': {'position': 'top', "maxLines": 3},
               "isStacked": "true", "colors": colors}
    
       [{"_type": "chart", "type": "bar", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """

        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bar", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]


# ////////////////////////////////////////////////
        e = [
            ['Year', 'Sales', 'Expenses', 'Profit'],
            ['2014', 1000, 400, 200],
            ['2015', 1170, 460, 250],
            ['2016', 660, 1120, 300],
            ['2017', 1030, 540, 350]
        ]
        ops = {"colors": colors}

        infodata = """  
        e = [
            ['Year', 'Sales', 'Expenses', 'Profit'],
            ['2014', 1000, 400, 200],
            ['2015', 1170, 460, 250],
            ['2016', 660, 1120, 300],
            ['2017', 1030, 540, 350]
        ]
            
        ops = { "colors": colors}
    
       [{"_type": "chart", "type": "bar", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """

        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bar", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def candles(self, colors):

        uidata = []
        e = [
            ['Mon', 20, 28, 38, 45],
            ['Tue', 31, 38, 55, 66],
            ['Wed', 50, 55, 77, 80],
            ['Thu', 77, 77, 66, 50],
            ['Fri', 68, 66, 22, 15]
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
       
       [{"_type": "chart", "type": "candles", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "candles", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        ops = {'legend': {'position': 'none'}, "bar": {"groupWidth": '100%'},
               "candlestick": {"fallingColor": {"strokeWidth": "0", "fill": '#a52714'}, "risingColor": {"strokeWidth": "0", "fill": '#0f9d58'}}}

        infodata = """  e = [
            ['Task', 'Hours per Day'],
            ['Work', 11],
            ['Eat', 2],
            ['Commute', 2],
            ['Watch TV', 2],
            ['Sleep', 7]
        ]
       ops = {'legend': {'position': 'none'}, "bar": {"groupWidth": '100%'},
               "candlestick": {"fallingColor": {"strokeWidth": "0", "fill": '#a52714'}, "risingColor": {"strokeWidth": "0", "fill": '#0f9d58'}}}
       
       [{"_type": "chart", "type": "candles", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "candles", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

        return self.ins._ui._render(uidata)

    def candles(self, colors):

        uidata = []
        e = [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]

        ops = {'legend': {'position': 'none'}, "colors": colors , "hAxis": {"title": 'Life Expectancy'},
    "vAxis": {"title": 'Fertility Rate'}}

        infodata = """   
        e = [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
       ops = {'legend': {'position': 'none'}, "colors": ["#3ba9b6"]} 
       
       [{"_type": "chart", "type": "scatter", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "scatter", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]

     

        return self.ins._ui._render(uidata)


    def Bubble(self, colors):

        uidata = []
        e = [
        ['ID', 'Life Expectancy', 'Fertility Rate', 'Region',     'Population'],
        ['CAN',    80.66,              1.67,      'North America',  33739900],
        ['DEU',    79.84,              1.36,      'Europe',         81902307],
        ['DNK',    78.6,               1.84,      'Europe',         5523095],
        ['EGY',    72.73,              2.78,      'Middle East',    79716203],
        ['GBR',    80.05,              2,         'Europe',         61801570],
        ['IRN',    72.49,              1.7,       'Middle East',    73137148],
        ['IRQ',    68.09,              4.77,      'Middle East',    31090763],
        ['ISR',    81.55,              2.96,      'Middle East',    7485600],
        ['RUS',    68.6,               1.54,      'Europe',         141850000],
        ['USA',    78.09,              2.05,      'North America',  307007000]
      ]

        ops = { "colors": colors ,   "hAxis": {"title": 'Life Expectancy'},
    "vAxis": {"title": 'Fertility Rate'}}

        infodata = """   
       e = [
        ['ID', 'Life Expectancy', 'Fertility Rate', 'Region',     'Population'],
        ['CAN',    80.66,              1.67,      'North America',  33739900],
        ['DEU',    79.84,              1.36,      'Europe',         81902307],
        ['DNK',    78.6,               1.84,      'Europe',         5523095],
        ['EGY',    72.73,              2.78,      'Middle East',    79716203],
        ['GBR',    80.05,              2,         'Europe',         61801570],
        ['IRN',    72.49,              1.7,       'Middle East',    73137148],
        ['IRQ',    68.09,              4.77,      'Middle East',    31090763],
        ['ISR',    81.55,              2.96,      'Middle East',    7485600],
        ['RUS',    68.6,               1.54,      'Europe',         141850000],
        ['USA',    78.09,              2.05,      'North America',  307007000]
      ]
        ops = { "colors": colors ,   "hAxis": {"title": 'Life Expectancy'},
    "vAxis": {"title": 'Fertility Rate'}}
       
       [{"_type": "chart", "type": "bubble", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bubble", "data": e, "options": ops,
                "style": "height:500px", "class": "ins-padding-xl ins-col-12"},
            {"_type": "code", "class": "ins-col-12 ins-hidden -ui-info-data",
                "_data": infodata},
            {"end": "true"}]


        e = [
          ['ID', 'X', 'Y', 'Temperature'],
          ['',   80,  167,      120],
          ['',   79,  136,      130],
          ['',   78,  184,      50],
          ['',   72,  278,      230],
          ['',   81,  200,      210],
          ['',   72,  170,      100],
          ['',   68,  477,      80]
        ]

        ops = { "colors": colors }


        infodata = """   
       e = [
          ['ID', 'X', 'Y', 'Temperature'],
          ['',   80,  167,      120],
          ['',   79,  136,      130],
          ['',   78,  184,      50],
          ['',   72,  278,      230],
          ['',   81,  200,      210],
          ['',   72,  170,      100],
          ['',   68,  477,      80]
        ]
        ops = { "colors": colors , colorAxis: {colors: ['yellow', 'red']}}
       
       [{"_type": "chart", "type": "bubble", "data": e, "options": ops, 
        "style": "height:500px","class": "ins-col-6  ins-flex  ins-card ins-padding-xl"}] """
        uidata += [
            {"start": "true",  "class": "ins-col-6  ins-flex-end  ins-card "},
            {"class": "ins-icons-search ins-button-icon  -ui-show-info"},
            {"_type": "chart", "type": "bubble", "data": e, "options": ops,
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

        r = ""
        r += self.column(colors)
        r += self.bar(colors)
        r += self.line(colors)

        r += self.area(colors)
        r += self.stepped_area(colors)
        r += self.pie(colors)


        r += self.candles(colors)
        
        r += self.Bubble(colors)

        
        
        r += self.org(colors)



       # r += self.geo(colors)
        return r
