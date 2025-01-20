from ins_kit._engine._bp import App


class AppUser(App):
    def __init__(self, app) -> None:
        self.app: App = app
        super().__init__(app.ins)

    def out(self):

        ops = self.ins._apps._crud_ops

       
       
        def func(data: dict):
            if "password" in data:
                if data["password"] == "":
                    del data["password"]
                else :
                    data["password"] = d = self.ins._data.hash_password(
                        data["password"])
            return data

        ops._form_befor_insert = func
        ops._form_befor_update = func
        
        
        def ufunc(data: dict):
            if "password" in data:
                    del data["password"]
            return data
           

        
        ops._form_befor_update_data = ufunc

        

        r = self.ins._apps._crud(ops, properties=self.app._properties)
        return r
