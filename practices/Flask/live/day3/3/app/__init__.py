from .routes import todo_bp
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    return app
