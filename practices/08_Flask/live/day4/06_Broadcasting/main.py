from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

clients = set()  # 연결된 클라이언트 보관

@app.route("/")
def index():
    return render_template("chat.html")

@sock.route('/ws')
def websocket(ws):
    clients.add(ws)
    try:
        while True:
            data = ws.receive()
            if data is None:
                break
            # 모든 클라이언트에게 메시지 전송
            for client in clients:
                client.send(data)
    finally:
        clients.remove(ws)

if __name__ == "__main__":
    app.run(debug=True)

