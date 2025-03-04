import json
import re
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
    def db_info(self):
        schema_info = {

            "kit_user": [
                "id",
                "title",
                "email",
                "user_name"
            ],


            "gla_order": [
                "id",
                "fk_user_id",
                "total",
                "order_status",
                "kit_created"
            ],
            "gla_order_item": [
                "id",
                "fk_order_id",
                "price",
                "quantity",
                "fk_product_id"
            ]
        }
        
        
        
        return schema_info

    def generate_sql(self, user_message, schema_info=None):
        # Show me the total sales per customer in California after 2022

        schema_info = self.db_info

        schema_context = "\nDatabase Schema:\n"
        for table, columns in schema_info.items():
            schema_context += f"- {table} ({', '.join(columns)})\n"

        prompt = f"""Convert this natural language query to SQL using the following schema:

            {schema_context}

            User Message: {user_message}

            Follow these rules:
            1. Return only SQL code
            2. Use standard SQL syntax
            3. Use uppercase for SQL keywords
            4. Format with appropriate line breaks
            5. Make reasonable assumptions about table names and structure
            6. If unsure about field names, use common conventions
            7. Do not include explanations or markdown formatting

            SQL Query:"""

        client = OpenAI(api_key=self.dkey, base_url="https://api.deepseek.com")

        messages = [{"role": "system", "content": "You are a SQL expert. Convert natural language to optimized SQL queries."},

                    {"role": "user", "content": prompt}]

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages


        )

        content = response.choices[0].message.content

        sql_query = re.search(r"```sql\n(.*?)\n```", content, re.DOTALL)
        
      
        
        
        if sql_query:
           #  sql_query.group(1).strip()
            return  self.ins._db._get_query(sql_query.group(1).strip())

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

        )

        data = response.choices[0].message.content
        d = json.loads(data)
        return d
