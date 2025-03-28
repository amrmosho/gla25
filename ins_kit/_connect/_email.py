from ins_kit.ins_parent import ins_parent
import requests

class Email(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)
        self.api_key = "xxx"
        self.api_url = "https://api.brevo.com/v3/smtp/email"
        self.headers = {
            "accept": "application/json",
            "api-key": self.api_key,
            "content-type": "application/json"
        }
    
    def send_email(self,lang, recipient_email,temp,subject=""):
        sender_email = "hossameldeen.ismail@gmail.com"

        if isinstance(temp, int):
          data = self.ins._db._get_row("kit_email_template","*",f"id='{temp}'",update_lang=True)
          bmessage = data["content"]
          bsubject = data["subject"]
          if data["sender_email"]:
            sender_email = data["sender_email"]
      
      
        else:
          bmessage = temp
          bsubject = subject

        subject = self.ins._langs._update(bsubject,lang)
        message = self.ins._langs._update(bmessage,lang)


        data = {
            "sender": {"email": sender_email},
            "to": [{"email": recipient_email}],
            "subject": subject,
            "htmlContent": message
        }
        response = requests.post(self.api_url, json=data, headers=self.headers)
        return response.status_code, response.json()

