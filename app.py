"""
Basic Flask API demo - GET and POST, plain strings (no JSON).

Run with:
    pip install flask flask-cors
    python app.py

The API will start at http://127.0.0.1:5000
"""

from flask import Flask, request,render_template_string
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
        <title>Soil Moisture Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f7f6;
                margin: 0;
                padding: 40px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 30px;
            }
            .dashboard {
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
                justify-content: center;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                width: 250px;
                text-align: left;
                border-top: 5px solid #27ae60;
            }
            .city-name {
                font-size: 20px;
                font-weight: bold;
                color: #34495e;
                margin-bottom: 10px;
            }
            .moisture-value {
                font-size: 32px;
                font-weight: bold;
                color: #27ae60;
                margin: 10px 0;
            }
            .status {
                font-size: 14px;
                color: #7f8c8d;
            }
        </style>
    </head>
    <body>

        <h1>🌱 Live Soil Moisture Dashboard</h1>

        <div class="dashboard">
            <!-- City 1 -->
            <div class="card">
                <div class="city-name">Fresno, CA</div>
                <div class="moisture-value">34%</div>
                <div class="status">Status: Optimal Range</div>
            </div>

            <!-- City 2 -->
            <div class="card" style="border-top-color: #e67e22;">
                <div class="city-name">Des Moines, IA</div>
                <div class="moisture-value" style="color: #e67e22;">18%</div>
                <div class="status">Status: Dry / Needs Irrigation</div>
            </div>
        </div>

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
