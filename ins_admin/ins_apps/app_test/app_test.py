import json
from ins_kit._engine._bp import App


class AppTest(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)


    def out(self):

        from openai import OpenAI
        client = OpenAI(api_key="sk-94607bf6a3cc4319beda1b5992feb1d7", base_url="https://api.deepseek.com")
     
        system_prompt = """
        The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

        EXAMPLE INPUT: 
        Which is the highest mountain in the world? Mount Everest.

        EXAMPLE JSON OUTPUT:
        {
            "question": "Which is the highest mountain in the world?",
            "answer": "Mount Everest"
        }
        """


        system_prompt =  """Extract information structure and return as JSON with:
                - 'type': (what the user wants to create)
                - 'operation': (operation)
                - 'name' (name)
                - 'options' (list of  requirement or options)
                - 'fields' (list of objects containing 'name' and 'type' for each column)"""
                
                
        #user_prompt = "Which is the longest river in the world? The Nile River."
        user_prompt = "make a component 'employees' and  make it item in menu and no data contains:  name (text), position (text), and hire_date (date)"

        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}]



        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            response_format={
                'type': 'json_object'
            }
        )

        return json.loads(response.choices[0].message.content)