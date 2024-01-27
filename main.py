from flask import Flask

# pip install flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)
