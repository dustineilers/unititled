from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "anton"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)