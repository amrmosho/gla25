import json
from ins_kit.ins_parent import ins_parent
import uuid
import requests
import os
import shutil
from ins_kit.ins_parent import ins_parent

class SMS(ins_parent):
    

    def get_content(self,name,lang):

        temp_data = self.ins._data._get_options("4")["content"]
        sms_id = json.loads(temp_data)[name]
        data = self.ins._db._get_row("kit_sms_template","*",f"id='{sms_id}'",update_lang=True)
        message = self.ins._langs._update(data["content"],lang)

        return message

        

    def send_sms(self, temp,otp, phone_numbers):
        message = self.get_content(temp,{"otp":f"{otp}"})

        url = "https://app.community-ads.com/SendSMSService/SMSSender.asmx/SendSMS"
        payload = {
            "UserName": "ElgallaAPI",
            "Password": "{[[9u+9CgA",
            "SMSText": message,
            "SMSLang": "e",
            "SMSSender": "El Galla",
            "SMSReceiver": phone_numbers,
            "SMSID": str(uuid.uuid4()),
            "CampaignID": ""
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            return response.text
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def send_sms2(self, temp,otp, phone_numbers):
        message = self.get_content(temp,{"otp":f"{otp}"})

        if not phone_numbers or not message:
            return {"error": "Message and phone numbers are required."}

        numbers = ",".join(phone_numbers)
        payload = {
            "username": "elgallagold@epushagency.com",
            "password": "nh/tm8esg9u",
            "api_key": "PWhm-xpx8-D)RH-sE*P",
            "message": message,
            "from": "ELGALLAGOLD",
            "to": numbers,
        }

        url = f"https://api.epusheg.com/api/v2/send_bulk?{requests.compat.urlencode(payload)}"  
        print(f"Request URL: {url}")  # Print the URL

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }

        with requests.Session() as session:
            try:
                response = session.get(url, headers=headers, timeout=60, verify=False)
                response.raise_for_status()  # Raise exception for HTTP errors
                print("Response:", response.text)
            except requests.Timeout:
                print("Timeout Error")
            except requests.ConnectionError:
                print("Connection Error")
            except requests.RequestException as e:
                print(f"Error: {e}")


