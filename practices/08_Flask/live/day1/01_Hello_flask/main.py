from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/hello")
def hello():
    return "Hello!"

# 동적라우팅
@app.route("/user/<name>")
def greet(name):
    return f"Wellcome, {name}!"


if __name__ == "__main__":
    app.run(debug=True)