from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey")
def survey():
    # 설문 문항
    questions = [
        "오늘 기분은 어떠신가요?",
        "어제 수업은 이해하기 쉬웠나요?",
        "앞으로 배우고 싶은 내용은 무엇인가요?"
    ]
    return render_template("survey.html", questions=questions)

@app.route("/result", methods=["GET"])
def result():
    # query string에서 답변 받기: getlist 사용
    answers = request.args.getlist("answer")
    return render_template("result.html", answers=answers)

if __name__ == "__main__":
    app.run(debug=True)