from flask import Flask, request, jsonify, render_template

app = Flask()


@app.route("/")
def home():
    return render_template("")
