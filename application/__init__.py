from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home():
        return "Welcome to home"

    return app