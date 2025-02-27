import json
from openai import OpenAI
from ins_kit.ins_parent import ins_parent


class AI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def test(self):
        user_message = "make a component 'employees' and  make it item in menu and no data contains:  name (text), position (text), and hire_date (date)"
        g = self.get(user_message)
        print(json.dumps(g, indent=2))

    def _get(self, user_prompt):

        use = ""

        if use == "gpt":
            r = self._get_gpt(user_prompt)
        else:
            r = self._get_deep(user_prompt)
        return r

    @property
    def key(self):
        return "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"

    @property
    def role(self):
        return {"role": "system", "content": """Extract information structure and return as JSON with:
                - 'type': (what the user wants to create)
                - 'operation': (operation)
                - 'name' (name)
                - 'options' (list of  requirement or options)
                - 'fields' (list of objects containing 'name' and 'type' for each column)"""}

    def _get_gpt(self, user_message):
        client = OpenAI(api_key=self.key)
        msgs = [
            self.role,
            {
                "role": "user",
                "content": user_message,
            }
        ]
        mod = "gpt-4o"
        rformat = {"type": "json_object"}
        completion = client.beta.chat.completions.parse(
            model=mod,
            messages=msgs,
            response_format=rformat
        )
        # d= completion.model_dump()

        response_data = json.loads(completion.choices[0].message.content)
        return response_data

    @property
    def dkey(self):
        key = 'sk-94607bf6a3cc4319beda1b5992feb1d7'
        return key

    def _get_deep(self, user_prompt):
        from openai import OpenAI
        client = OpenAI(api_key=self.dkey, base_url="https://api.deepseek.com")

        system_prompt = """Extract information structure and return as JSON with:
                - 'type': (what the user wants to create)
                - 'operation': (operation)
                - 'name' (name)
                - 'options' (list of  requirement or options)
                - 'fields' (list of objects containing 'name' and 'type' for each column)
                
                EXAMPLE JSON OUTPUT:
                {
                    "type": what the user wants to create,
                    "operation": "operation",
                    "name": "name",
                    "options": "list of  requirement or options",
                    "fields": "list of objects containing 'name' and 'type' for each column",

                }
                """

        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}]

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            response_format={
                'type': 'json_object'
            }
        )

        data = response.choices[0].message.content
        d = json.loads(data)
        return d
