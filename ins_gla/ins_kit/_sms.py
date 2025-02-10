import requests

class SMS:
    def __init__(self):
        self.base_url = "https://api.epusheg.com/api/v2/send_bulk"
        self.username = "elgallagold@epushagency.com"
        self.password = "nh/tm8esg9u"
        self.api_key = "PWhm-xpx8-D)RH-sE*P"
        self.sender = "ELGALLAGOLD"

    def send_sms(self, message, phone_numbers):
        """
        Send SMS to single or multiple phone numbers.

        Args:
            message (str): The message content (max 402 Arabic or 918 English characters).
            phone_numbers (list): List of phone numbers (format: 01XXXXXXXXX or 201XXXXXXXXX).
        Returns:
            dict: API response JSON or error message.
        """
        if not phone_numbers or not message:
            return {"error": "Message and phone numbers are required."}

        numbers = ",".join(phone_numbers)
        payload = {
            "username": self.username,
            "password": self.password,
            "api_key": self.api_key,
            "message": message,
            "from": self.sender,
            "to": numbers,
        }

        # Generate the URL with parameters
        url = f"{self.base_url}?{requests.compat.urlencode(payload)}"  
        print(f"Request URL: {url}")  # Print the URL

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }

        # Use requests.Session to handle connections more efficiently
        with requests.Session() as session:
            try:
                # Send GET request with the parameters and timeout
                response = session.get(url, headers=headers, timeout=60, verify=False)
                response.raise_for_status()  # Raise exception for HTTP errors
                print("Response:", response.text)
            except requests.Timeout:
                print("Timeout Error")
            except requests.ConnectionError:
                print("Connection Error")
            except requests.RequestException as e:
                print(f"Error: {e}")
