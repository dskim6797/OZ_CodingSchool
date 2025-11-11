from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"

# 변수 바인딩
@app.route("/hello")
def hello():
    return render_template("hello.html", name="BE15")

# 조건문
@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

# 반복문
@app.route("/fruits")
def fruits():
    fruits = ["사과", "딸기", "키위", "포도"]
    return render_template("fruits.html", fruits=fruits)


if __name__ == "__main__":
    app.run(debug=True)   
    

