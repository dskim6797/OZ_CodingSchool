from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive() # 클라이언트 메시지 받기
        if data is None:    # 연결 끊기 대비
            break
        ws.send(f"서버가 클라이언트에게 보냄: {data}")


if __name__ == "__main__":
    app.run(debug=True)