from datetime import datetime
import locale
from ins_kit.ins_parent import ins_parent
import hashlib
import secrets
import uuid

class Data(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
       
    @property 
    def unid(s):
       return uuid.uuid4().hex

   
    @property 
    def _unid(s):
       return  uuid.uuid4().hex

        
    
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





    def _format_currency(self, number, locale_str='en_US', symbol=True):
        """
        Formats a number as currency using the specified locale.

        Args:
            number: The number to format.
            locale_str: The locale string to use (e.g., 'en_US', 'de_DE', 'fr_CA', 'ar_EG').
                        If empty, it uses the system's default locale.
            symbol: Whether to include the currency symbol.

        Returns:
            A string representing the formatted currency, or None if there's an error.
        """
        try:
            available_locales = locale.locale_alias.keys()
            if locale_str.replace('-', '_').lower() not in available_locales:
                print(f"⚠️ Warning: Locale '{locale_str}' not available. Using 'en_US.utf8' instead.")
                locale_str = 'en_US.utf8'
            else:
                locale_str += '.utf8' if not locale_str.endswith('.utf8') else ''
            locale.setlocale(locale.LC_ALL, locale_str)

            if symbol:
                return locale.currency(number, grouping=True)
            else:
                formatted = locale.format_string("%d", number, grouping=True)
                try:
                    formatted = locale.format_string("%10.2f", number, grouping=True)
                except ValueError:
                    pass 
                return formatted

        except locale.Error as e:
            print(f"❌ Locale error: {e}")
            return None
        except TypeError as e:
            print(f"⚠️ Type error: {e}")
            return None
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            return None

