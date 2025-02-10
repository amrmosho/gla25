import requests

class PaymobAPI:
    def __init__(self):
        self.api_key = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2TVRBeE5qTXpOeXdpYm1GdFpTSTZJbWx1YVhScFlXd2lmUS5kWmYzaFltS2tOVmpna3k2Wk1fcTFjLXd2QzJBNzBNQ3dFVllrMmRRWjh6VDgyWlBZMFdNYmljMV9QeVpZUnowNTYwTnNwOG5mSkt4Vk9XT2NlV2Nydw=="
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
            "delivery_needed": False
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
