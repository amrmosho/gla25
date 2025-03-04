import uuid
import requests

class SMS:
    
    def send_sms(self, message, phone_numbers):
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

    def send_sms2(self, message, phone_numbers):
     
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


