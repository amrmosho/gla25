from ins_kit.ins_parent import ins_parent


class Gusers(ins_parent):
        
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
        
    @property
    def n(self):
        return "use_logindsds"
    


    
    
    def _loign(self):
        
       rq = self.ins._server._post()
       sql =f"email ='{rq["email"]}'"
       data= self.ins._db._get_row("kit_user" ,"*" ,sql)

       if data :        
            self.ins._server._set_session(self.n ,data)
            return self._check()
       else:
         return False


    def _check(self):
      return  self.ins._server._get_session(self.n)
    


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


         
        
        
