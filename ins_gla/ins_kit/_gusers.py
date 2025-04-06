from datetime import datetime, timedelta
from random import randint, random
import uuid

from itsdangerous import URLSafeTimedSerializer
from ins_gla.ins_kit._sms import SMS
from ins_kit.ins_parent import ins_parent


class Gusers(ins_parent):
        
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
        
    @property
    def n(self):
        return "gla_login"
    
    def _create_otp(self, mobile = "",method = "1"):
        try:
            otp = randint(1000, 9999)
            if mobile:
                current_time = datetime.now()
                expiry = current_time + timedelta(minutes=5)
                data = {
                    "mobile":mobile,
                    "otp":otp,
                    "expiry":expiry
                }
                old_data =  self.ins._db._get_row("gla_login_temp","*",f"mobile='{mobile}'")
                if old_data:
                 self.ins._db._update("gla_login_temp",data,f"mobile='{mobile}'")
                else:
                  self.ins._db._insert("gla_login_temp",data)
                
                sms = SMS()
                try:
                    if method == "1":
                        response = sms.send_sms(f"Hello from Elgalla Gold! This is OTP code {otp}", [mobile])
                    else:
                        response = sms.send_sms2(f"Hello from Elgalla Gold! This is OTP code {otp}", [mobile])
                except Exception as e:
                    return(f"Failed to send SMS: {e}")

                return "1"
            else:
                return otp
        except Exception as er:
          return(f"Error: {er}")

        

    def _check_otp(self, mobile, otp):
        w = f"mobile='{mobile}' and otp='{otp}'"
        odata = self.ins._db._get_row("gla_login_temp", "*", w)
        if odata:
            now = datetime.now()
            expiry = odata["expiry"]
            if now > expiry:
                return "-2" 
            return "1"

        return "-1"

    def _reset_password(self,rq):
        sql = f"mobile ='{rq['mobile']}'"
        rq["password"] = self.ins._data.hash_password(rq["password"])
        data = {"password":rq["password"]}
        self.ins._db._update("kit_user",data,sql)
        return "1"


    def _mobile_exists(self, mobile):
        sql = f"mobile ='{mobile}'"
        data = self.ins._db._get_row("kit_user", "*", sql)
        if data:
            return "-1"
        return "1"

    def _signup(self, rq):
        required_fields = ["mobile", "password","first_name","last_name"]
        
        if not all(field in rq for field in required_fields):
            return "Missing required fields"
        
        rq["password"] = self.ins._data.hash_password(rq["password"])
        new_user_data = {
            "mobile": rq["mobile"],
            "password": rq["password"],
            "first_name": rq["first_name"],
            "last_name": rq["last_name"]
        }
        new_user_data["user_name"] = rq["first_name"] + " " +  rq["last_name"]
        new_user_data["title"] = rq["first_name"] + " " +  rq["last_name"]

        if 'email' in rq:
            new_user_data["email"] = rq["email"]
        
        uid = self.ins._db._insert("kit_user", new_user_data)
        if uid and "email" in rq:
            link = self.generate_token(uid,rq["email"], rq["mobile"], rq["password"])
            lang = {"link":link,"title":new_user_data["title"]}
            self.ins._email.send_email(lang,rq["email"],1)

            
        return "1"
    
    
    def _login(self, rq):
        login_field = "email" if "@" in rq["email_mobile"] else "mobile"
        if login_field == "email":
            sql = f"{login_field} ='{rq['email_mobile']}' AND password ='{rq['password']}' AND email_status='verified'"
        else:
            sql = f"{login_field} ='{rq['email_mobile']}' AND password ='{rq['password']}'"
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
