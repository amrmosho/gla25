import json
import re
from openai import OpenAI
from ins_kit.ins_parent import ins_parent

class OpenAIChatbot:


    """
        A chatbot interface using OpenAI's API with conversation management
        
        Attributes:
            model (str): OpenAI model version
            conversation_history (list): Conversation context/memory
        """
    
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI chatbot agent
        
        Args:
            api_key: OpenAI API key (required)
            model: Model version identifier
        """
        if not api_key:
            raise ValueError("API key is required for OpenAI interactions")
            
        self.model = model
        self.conversation_history = []

    def start_conversation(self, system_prompt: str = "You are a helpful assistant"):
        """Initialize conversation with a system message"""
        self.conversation_history = [{
            "role": "system",
            "content": system_prompt
        }]

    def add_to_history(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def _api_call(self):
        """Make actual API call to OpenAI"""
        return openai.ChatCompletion.create(
            model=self.model,
            messages=self.conversation_history
        )

    def send_message(self, user_input: str) -> str:
        """
        Send message to OpenAI and get response
        
        Args:
            user_input: User's message text
            
        Returns:
            Assistant's response text
        """
        if not user_input.strip():
            raise ValueError("Message cannot be empty")
            
        self.add_to_history("user", user_input)
        
        try:
            response = self._api_call()
            assistant_response = response['choices'][0]['message']['content']
            self.add_to_history("assistant", assistant_response)
            return assistant_response
            
        except openai.error.APIError as e:
            self.conversation_history.pop()
            return f"OpenAI API Error: {str(e)}"
        except Exception as e:
            self.conversation_history.pop()
            return f"Error: {str(e)}"

    def end_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []










class DSAi(ins_parent):
    @property
    def dkey(self):
        key = 'sk-94607bf6a3cc4319beda1b5992feb1d7'
        return key

    def get_clinet(self):
        client = OpenAI(api_key=self.dkey, base_url="https://api.deepseek.com")
        return client

    def db_info(self, tables):
        # tables= ["kit_user" ,"gla_order" ,"gla_order_item" ,"kit_menu_item"]

        schema_info = {}
        for t in tables:
            tdata = self.ins._db._get_table_fields(t)
            schema_info[t] = tdata
        return schema_info

    def generate_sql(self, user_message, tables=[]):

        schema_info = self.db_info(tables)

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
            7. ignore chart 
            SQL Query:"""
            
        rules ="You are a SQL expert. Convert natural language to optimized SQL queries."

        sql_query =self.msg(prompt ,rules)

        if "```" in sql_query:
            sql_query = re.search(r"```sql\s*([\s\S]*?)\s*```", sql_query, re.IGNORECASE) #handles variations in whitespace and capitalization
            sql =sql_query.group(1).strip()
            return self.ins._db._get_query(sql)

        
        if sql_query:
            return self.ins._db._get_query(sql_query)

    def generate_from_docs(self,  question: str) -> str:
        """
        Generate answers based on provided documents
        :param api_key: OpenAI API key
        :param documents: List of text documents
        :param question: User's question
        :return: Generated response
        """
        
        docs = self.ins._json._file_read("test.json")
        # Combine documents into context
        context = "\n".join(
            [f"Document {i+1}: {doc}" for i, doc in enumerate(docs)])

        prompt = f"""Answer the question based on these documents:
        
        {context}
        
        Question: {question}
        
        Answer in simple terms:"""
        return  self.msg(prompt)
        
        
    def msg(self,prompt ,rol=""):
        client = self.get_clinet()
        msgs=[]
        if rol !="":
             msgs.append({"role": "system", "content": rol})
        msgs.append({"role": "user", "content": prompt})
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=msgs
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"       
        
        

class AI(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

    def generate_sql(self, user_message, tables=[]):
        return DSAi(self.ins).generate_sql(user_message, tables)

    def test(self):
        user_message = "make a component 'employees' and  make it item in menu and no data contains:  name (text), position (text), and hire_date (date)"
        g = self.get(user_message)
        print(json.dumps(g, indent=2))

    def _get(self, user_prompt):
        return DSAi(self.ins).generate_from_docs(user_prompt)

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
