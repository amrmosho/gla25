import requests

class PaymobAPIOld:
    def __init__(self):
        self.api_key = "xxx"
        self.base_url = "https://accept.paymobsolutions.com/api"
    
    def authenticate(self):
        url = f"{self.base_url}/auth/tokens"
        payload = {"api_key": self.api_key}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json().get("token")
        except requests.RequestException as e:
            print("Authentication failed:", e)
            return None

    def create_order(self, auth_token, amount, order_id):
        url = f"{self.base_url}/ecommerce/orders"
        headers = {"Authorization": f"Bearer {auth_token}"}
        payload = {
            "merchant_order_id": order_id,
            "amount_cents": amount,
            "currency": "EGP",
            "delivery_needed": False,
            "billing_data": {
                "first_name": "ala", 
                "last_name": "zain",
                "email": "ali@gmail.com",
                "phone_number": "+92345xxxxxxxx",
                "address": "1234 Street",
                "city": "dumy",
                "state": "dumy",
                "country": "EG",
                "postal_code": "12345"
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json().get("id")
        except requests.RequestException as e:
            print("Order creation failed:", e)
            return None

    def get_payment_token(self, auth_token, payment_id, amount, integration_id):
        url = f"{self.base_url}/acceptance/payment_keys"
        headers = {"Authorization": f"Bearer {auth_token}"}
        payload = {
            "order_id": payment_id,
            "amount_cents": amount,
            "currency": "EGP",
            "integration_id": integration_id,
            "billing_data": {
                "apartment": "dumy",
                "first_name": "ala",
                "last_name": "zain",
                "street": "dumy",
                "building": "dumy",
                "phone_number": "+92345xxxxxxxx",
                "city": "dumy",
                "country": "dumy",
                "email": "ali@gmail.com",
                "floor": "dumy",
                "state": "dumy"
              }
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json().get("token")
        except requests.RequestException as e:
            print("Failed to get payment token:", e)
            return None



    def create_pay_wdgt(self, amount, order_id, integration_id):
        auth_token = self.authenticate()
        if auth_token:
            payment_id = self.create_order(auth_token, amount, order_id)
            if payment_id:
                payment_token = self.get_payment_token(auth_token, payment_id, amount, integration_id)
                if payment_token:
                    iframe_id = 892221
                    return f"https://accept.paymob.com/api/acceptance/iframes/{iframe_id}?payment_token={payment_token}"
    
    
    def create_kiosk_payment_url(self, amount, order_id, integration_id):
        auth_token = self.authenticate()
        if auth_token:
            payment_id = self.create_order(auth_token, amount, order_id)
            if payment_id:
                payment_token = self.get_payment_token(auth_token, payment_id, amount, integration_id)
                if payment_token:
                    return f"Your payment code is: {payment_token}. Please use this code at a Masary or AMAN POS machine."
        return None
