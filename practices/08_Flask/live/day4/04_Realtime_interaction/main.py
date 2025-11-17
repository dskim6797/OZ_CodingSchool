from flask import Flask, render_template
from flask_sock import Sock


app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("sentiment.html")

@sock.route('/ws')
def websocket(ws):
    while True:
        text = ws.receive() # 클라이언트 메시지 받기
        if text is None:    # 연결 끊기 대비
            break
        
        pos_words = ['happy','love','good','great']
        neg_words = ['sad','bad','angry','tired']
        
        sentiment = "중립"
        if any(word in text.lower() for word in pos_words):
            sentiment = "😊 긍정!"
        elif any(word in text.lower() for word in neg_words):
            sentiment = "😡 부정!"
            
        ws.send(sentiment)


if __name__ == "__main__":
    app.run(debug=True)