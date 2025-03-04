from datetime import datetime, timedelta
from random import randint, random
from ins_kit.ins_parent import ins_parent


class Gusers(ins_parent):
        
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
        
    @property
    def n(self):
        return "gla_login"
    
    def _create_otp(self, mobile = "",method = "1"):
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
            
            if method == "1":
                response = self.ins._sms.send_sms(f"Hello from Elgalla Gold! This is OTP code {otp}", [mobile])
            else:
                response = self.ins._sms.send_sms2(f"Hello from Elgalla Gold! This is OTP code {otp}", [mobile])

            return "1"
        else:
            return otp
        

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
        sql = f"mobile ='{rq["mobile"]}'"
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
        
        self.ins._db._insert("kit_user", new_user_data)
        return "1"
    
    
    def _login(self, rq):
        rq["password"] = self.ins._data.hash_password(rq["password"])
        login_field = "email" if "@" in rq["email_mobile"] else "mobile"
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
        sql =f"mobile ='{rq["mobile"]}'"
        data= self.ins._db._get_row("kit_user" ,"*" ,sql)

        if data :        
            return "1"
        else:
            return "-1"
            
    def _otp_check(self):
        rq = self.ins._server._post()
        sql =f"mobile ='{rq["mobile"]}' and otp ='{rq["otp"]}'" 
        data= self.ins._db._get_row("kit_user" ,"*" ,sql)

        if data :        
            self.ins._server._set_session(self.n ,data)
            return self._check()
        else:
         return False


         
        
        
