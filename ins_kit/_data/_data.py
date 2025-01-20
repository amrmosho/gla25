from datetime import datetime
from ins_kit.ins_parent import ins_parent
import hashlib
import secrets


class Data(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
       
    @property 
    def unid(s):
       return  datetime.now().strftime('%Y%m%d%H%M%S')
   
    @property 
    def _unid(s):
       return  datetime.now().strftime('%Y%m%d%H%M%S')  
        
    
    def generate_salt(self):
        salt_length= 16
        return secrets.token_urlsafe(salt_length)


    def hash_password(self, password):
        
        # Implement your chosen hashing algorithm (e.g., bcrypt, Argon2)
        # Ensure strong password stretching and salting
        salt = "i1n2s3pass"
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000, 32)
        return hashed_password.hex()

    def verify_password(self, password, hashed_password, salt):
        salt = self.generate_salt()

        # Re-hash the provided password using the same algorithm and salt
        new_hashed_password = self.hash_password(password, salt)
        return hashed_password == new_hashed_password
    
    def _get_options(self, id ,all=False):
       data= self.ins._db._get_row("kit_options" ,"*" ,f"id={id}")
       if str :
            return data
       else:
           
         return self.ins._json._decode(data["content"]) 

