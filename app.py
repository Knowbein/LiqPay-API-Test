from liqpay import LiqPay

class PaymentService:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def getPaymentForm(self, amount):
        liqpay = LiqPay(self.public_key, self.private_key)
        params = {
            "action": "pay",
            "amount": str(amount),
            "currency": "UAH",
            "description": f"Оплата товару на {amount} грн",
            "order_id": "order_" + str(int(amount * 1000)),  # приклад order_id
            "version": "3",
            "sandbox": 1,  # обов’язково для тестового режиму
            "result_url": "http://localhost:8000/success",
            "server_url": "http://localhost:8000/callback"
        }
        data, signature = liqpay.cnb_form(params)
        return data, signature
