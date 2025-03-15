from flask import Flask, render_template
from payment_service import PaymentService  # створимо окремо цей файл
import os

app = Flask(__name__)

PUBLIC_KEY = "sandbox_i90752242997"
PRIVATE_KEY = "sandbox_edCMND25kpJIjkLBKatcD3EMeHCTgppHsH4Xhh6y"

payment_service = PaymentService(PUBLIC_KEY, PRIVATE_KEY)

@app.route('/')
def index():
    data, signature = payment_service.getPaymentForm(50)  # 50 грн — тестово
    return render_template('index.html', data=data, signature=signature)

@app.route('/success')
def success():
    return "Оплата успішна!"

@app.route('/callback', methods=['POST'])
def callback():
    return "Callback отримано", 200

if __name__ == '__main__':
    app.run(port=8000)
