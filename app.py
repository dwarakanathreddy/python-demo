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

@app.route("/", methods=["GET"])
def default_route():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f4f9;
                color: #333;
            }
            h1 {
                color: #4CAF50;
            }
        </style>
    </head>
    <body>
        <h1>Hello from Flask on Render! 🚀</h1>
        <p>Your app is successfully up and running.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/hello", methods=["GET"])
def hello_get():
    return "Hello, World!"


@app.route("/hello", methods=["POST"])
def hello_post():
    name = request.form.get("name", "stranger")
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
