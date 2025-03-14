from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("")


if __name__ == "main":
    app.run()
