
# استخدام الكلاس
from ins_gla.ins_kit._payment import PaymobAPI


paymob = PaymobAPI()

# بيانات العميل
customer_info = {
    "first_name": "Ali",
    "last_name": "Mohamed",
    "email": "ali@example.com",
    "extras": {}
}

# بيانات الفواتير
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

items = [
    {
        "name": "Gold Coin",
        "amount": 10000,
        "description": "24k Gold Coin",
        "quantity": 1
    }
]
skey =  paymob.create_intention(10000,5013780,"5")

print(skey)
