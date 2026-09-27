"""
Basic Flask API demo - GET and POST, plain strings (no JSON).

Run with:
    pip install flask flask-cors
    python app.py

The API will start at http://127.0.0.1:5000
"""

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows index.html (opened as a separate file) to call this API


@app.route("/hello", methods=["GET"])
def hello_get():
    return "Hello, World!"


@app.route("/hello", methods=["POST"])
def hello_post():
    name = request.form.get("name", "stranger")
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
