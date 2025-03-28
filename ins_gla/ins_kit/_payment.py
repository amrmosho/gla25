import requests

class PaymobAPI:

    def create_intention(self, amount, payment_methods, order_id):
        secret_key = "xxxx"
        public_key = "xxx"
        base_url = "https://accept.paymob.com"


        if int(payment_methods) == 4919279:
            secret_key = "xxx"
            public_key = "xxxx"

                

        billing_data = {
            "apartment": "12",
            "first_name": "Ali",
            "last_name": "Mohamed",
            "street": "Main Street",
            "building": "10",
            "phone_number": "01234567890",
            "city": "Cairo",
            "country": "EG",
            "email": "ali@example.com",
            "floor": "3",
            "state": "Cairo"
        }

        url = f"{base_url}/v1/intention/"
        headers = {"Authorization": f"Token {secret_key}"}
        payload = {
            "amount": round(amount),
            "currency": "EGP",
            "payment_methods": [int(payment_methods)],
            "billing_data": billing_data,
            "special_reference":order_id
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            client_secret= response.json().get("client_secret")
            return f"{base_url}/unifiedcheckout/?publicKey={public_key}&clientSecret={client_secret}"

        except requests.RequestException as e:
            print("Failed to create intention:", e)
            return None

