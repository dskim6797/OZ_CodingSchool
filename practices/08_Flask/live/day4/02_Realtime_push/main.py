from flask import Flask
from flask_sock import Sock
import threading
import time


app = Flask(__name__)
sock = Sock(app)

connections = []


@sock.route('/ws')
def websocket(ws):
    connections.append(ws)
    while True:
        data = ws.receive() # 클라이언트 메시지 받기
        if data is None:    # 연결 끊기 대비
            break
    connections.remove(ws)

def background_job():
    # 5초에 1번 서버가 메시지를 보낼 수 있도록 세팅
    while True:
        time.sleep(5)
        for ws in connections:
            try:
                ws.send(f"서버가 클라이언트에게 알림 보냄")
            except Exception: # 연결이 끊어졌을 때
                pass

print('-'*30)
threading.Thread(target=background_job, daemon=True).start()


if __name__ == "__main__":
    app.run(debug=True)