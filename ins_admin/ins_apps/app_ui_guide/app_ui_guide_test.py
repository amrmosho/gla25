from ins_kit._engine._bp import App

from openai import OpenAI
import json


class AppUiGuideTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    

    def _input(self):

        user_message = "make a component  'employees' type 'component' and  make it item in menu and no data contains:  name (text), position (text), and hire_date (date)."
        response_data = self.ins._ai.get(user_message)
        return response_data

    def out(self):
      
        r = self._input()
        return r
