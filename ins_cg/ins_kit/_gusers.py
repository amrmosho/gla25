from datetime import datetime, timedelta
from random import randint, random
import uuid

from itsdangerous import URLSafeTimedSerializer
from ins_kit.ins_parent import ins_parent


class Gusers(ins_parent):
        
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
        
    @property
    def n(self):
        return "gla_login"
    
    def _create_otp(self, email = ""):
        try:
            otp = randint(1000, 9999)
            if email:
                current_time = datetime.now()
                expiry = current_time + timedelta(minutes=5)
                data = {
                    "email":email,
                    "otp":otp,
                    "expiry":expiry
                }
                old_data =  self.ins._db._get_row("kit_login_temp","*",f"email='{email}'")
                if old_data:
                 self.ins._db._update("kit_login_temp",data,f"email='{email}'")
                else:
                  self.ins._db._insert("kit_login_temp",data)
                
                return "1"
            else:
                return otp
        except Exception as er:
          return(f"Error: {er}")

        

    def _check_otp(self, email, otp):
        w = f"email='{email}' and otp='{otp}'"
        odata = self.ins._db._get_row("kit_login_temp", "*", w)
        if odata:
            now = datetime.now()
            expiry = odata["expiry"]
            if now > expiry:
                return "-2" 
            return "1"

        return "-1"

    def _reset_password(self,rq):
        sql = f"email ='{rq['email']}'"
        rq["password"] = self.ins._data.hash_password(rq["password"])
        data = {"password":rq["password"]}
        self.ins._db._update("kit_user",data,sql)
        return "1"


    def _email_exists(self, email):
        sql = f"email ='{email}'"
        data = self.ins._db._get_row("kit_user", "*", sql)
        if data:
            return "-1"
        return "1"

    def _signup(self, rq):
        required_fields = ["email", "password","first_name","last_name"]
       
        if not all(field in rq for field in required_fields):
            return "Missing required fields"
        
        rq["password"] = self.ins._data.hash_password(rq["password"])
        new_user_data = {
            "email": rq["email"],
            "password": rq["password"],
            "first_name": rq["first_name"],
            "last_name": rq["last_name"],
            "email_status":"verified"
        }
        new_user_data["user_name"] = rq["first_name"] + " " +  rq["last_name"]
        new_user_data["title"] = rq["first_name"] + " " +  rq["last_name"]

        self.ins._db._insert("kit_user", new_user_data)
        return "1"
    
    
    def _login(self, rq):
        sql = f"email ='{rq['email']}' AND password ='{rq['password']}' AND email_status='verified'"
        data = self.ins._db._get_row("kit_user", "*", sql)
        if data:
            self.ins._server._set_session(self.n, data)
            return self._check()
        else:
            return False


    def _check(self):
      return  self.ins._server._get_session(self.n)
    
    def _logout(self):
      self.ins._server._del_session(self.n)
      return "1"


    def _mobile_login(self):
        rq = self.ins._server._post()
        sql =f"mobile ='{rq['mobile']}'"
        data= self.ins._db._get_row("kit_user" ,"*" ,sql)

        if data :        
            return "1"
        else:
            return "-1"
            
    def _otp_check(self):
        rq = self.ins._server._post()
        sql =f"mobile ='{rq['mobile']}' and otp ='{rq['otp']}'" 
        data= self.ins._db._get_row("kit_user" ,"*" ,sql)

        if data :        
            self.ins._server._set_session(self.n ,data)
            return self._check()
        else:
         return False


         
    def generate_token(self,user_id,email, mobile, password):
        secret_key = str(uuid.uuid4())
        s = URLSafeTimedSerializer(secret_key)
        token = s.dumps({"user_id": user_id, "email_mobile": mobile, "email": email, "password":password})
        current_time = datetime.now()
        expiry = current_time + timedelta(hours=5)
        insert_data = {
            "fk_user_id": user_id,
            "token": token,
            "secret_key": secret_key,
            "expiry": expiry
        }
        self.ins._db._insert("gla_email_token",insert_data)
        return f"http://127.0.0.1:5000/active/{token}"
            
        
    def _check_token(self, token):
        r = {}
        r["status"] = "1"
        token_data = self.ins._db._get_row("gla_email_token", "*", f"token='{token}'")
        if token_data:
            s = URLSafeTimedSerializer(token_data["secret_key"])
            r["data"] = s.loads(token, max_age=60 * 60 * 5)
            r["data"]["token_id"] = token_data["id"]
            now = datetime.now()
            expiry = token_data["expiry"]
            if now > expiry or token_data["status"] == "expired":
             r["status"] = "-2"
        else:
            r["status"] = "-1"
            
        return r
