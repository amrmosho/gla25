from datetime import datetime
import locale
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

    def _format_currency(self,number, locale_str='en_US' , symbol =True):
        """
        
        
        
        Formats a number as currency using the specified locale.

        Args:
            number: The number to format.
            locale_str: The locale string to use (e.g., 'en_US', 'de_DE', 'fr_CA' ,ar_EG). 
                        If empty, it uses the system's default locale.

        Returns:
            A string representing the formatted currency, or None if there's an error.
        """

        try:
            if locale_str:
                locale.setlocale(locale.LC_ALL, locale_str)  # Set the locale
            else:
                locale.setlocale(locale.LC_ALL, '') #sets to default locale
                
            if symbol:
                return locale.currency(number, grouping=True)  # Format with grouping
            else:
                
                formatted = locale.format_string("%d", number, grouping=True) #for integers
                try:
                    formatted = locale.format_string("%10.2f", number, grouping=True) #for floats
                except ValueError:
                    pass #if the number is integer, then the previous line will raise ValueError, so we pass it
                return formatted

        except locale.Error as e:
            print(f"Locale error: {e}")  # Handle locale errors
            return None
        except TypeError as e:
            print(f"Type error: {e}")  # Handle type errors
            return None
        except Exception as e: #catch any other error
            print(f"An error occurred: {e}")
            return None

