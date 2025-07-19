from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Major currencies with their symbols, flags, and country names
CURRENCIES = {
    "USD": {"name": "US Dollar", "symbol": "$", "flag": "🇺🇸"},
    "EUR": {"name": "Euro", "symbol": "€", "flag": "🇪🇺"},
    "INR": {"name": "Indian Rupee", "symbol": "₹", "flag": "🇮🇳"},
    "GBP": {"name": "British Pound", "symbol": "£", "flag": "🇬🇧"},
    "JPY": {"name": "Japanese Yen", "symbol": "¥", "flag": "🇯🇵"},
    "CNY": {"name": "Chinese Yuan", "symbol": "¥", "flag": "🇨🇳"},
    "SGD": {"name": "Singapore Dollar", "symbol": "$", "flag": "🇸🇬"},
    "AUD": {"name": "Australian Dollar", "symbol": "$", "flag": "🇦🇺"},
    "CAD": {"name": "Canadian Dollar", "symbol": "$", "flag": "🇨🇦"},
    "CHF": {"name": "Swiss Franc", "symbol": "CHF", "flag": "🇨🇭"},
    "KRW": {"name": "South Korean Won", "symbol": "₩", "flag": "🇰🇷"},
    "HKD": {"name": "Hong Kong Dollar", "symbol": "$", "flag": "🇭🇰"},
    "NZD": {"name": "New Zealand Dollar", "symbol": "$", "flag": "🇳🇿"},
    "SEK": {"name": "Swedish Krona", "symbol": "kr", "flag": "🇸🇪"},
    "NOK": {"name": "Norwegian Krone", "symbol": "kr", "flag": "🇳🇴"},
    "RUB": {"name": "Russian Ruble", "symbol": "₽", "flag": "🇷🇺"},
    "ZAR": {"name": "South African Rand", "symbol": "R", "flag": "🇿🇦"},
    "BRL": {"name": "Brazilian Real", "symbol": "R$", "flag": "🇧🇷"},
    "MXN": {"name": "Mexican Peso", "symbol": "$", "flag": "🇲🇽"},
    "TRY": {"name": "Turkish Lira", "symbol": "₺", "flag": "🇹🇷"},
}

API_URL = 'https://api.exchangerate-api.com/v4/latest/'

@app.route('/', methods=['GET', 'POST'])
def index():
    amount = 0
    from_currency = 'USD'
    to_currency = 'INR'
    result = None

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            # Fetch rates
            data = requests.get(f'{API_URL}{from_currency}').json()
            rate = data['rates'].get(to_currency)

            if rate:
                result = round(amount * rate, 2)
        except Exception as e:
            print("Error:", e)

    return render_template(
        'index.html',
        currencies=CURRENCIES,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency,
        result=result,
    )

if __name__ == '__main__':
    app.run(debug=True)
