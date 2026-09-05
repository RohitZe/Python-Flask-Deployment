from flask import Flask

app = Flask(__name__)


@app.route("/info")
def about():
    return "Rohit sharma devops guy"


@app.route("/phone")
def myphone():
    return "89xxxxxxxx"

@app.route("/hello")
def hello():
    return "Hello, I am listening"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
