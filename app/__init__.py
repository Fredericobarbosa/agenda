from flask import Flask
from app.routes import task_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecret'
    app.register_blueprint(task_bp)
    return app
