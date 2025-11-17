from flask import Flask, render_template
from flask_sock import Sock
import requests
import time


app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("btc.html")

@sock.route('/ws')
def websocket(ws):
    while True:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        res = requests.get(url).json()
        price = float(res["price"])
        
        ws.send(f"비트코인 현재가: ${price:,.4f}")
        time.sleep(2)
        
        
if __name__ == "__main__":
    app.run(debug=True)