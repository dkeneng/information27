from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "index 33333"


if __name__ == '__main__':
    app.run(debug=True)