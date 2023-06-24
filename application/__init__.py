from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home():
        return render_template('base.html')

    return app
