from flask import Flask, jsonify, render_template, redirect
from controllers.employee_controller import employee_bp

app = Flask(__name__)
app.register_blueprint(employee_bp)   # <- INI KUNCINYA, mendaftarkan semua route di employee_controller.py

@app.route("/")
def home():
    return "My backend is running!"

if __name__ == "__main__":
    app.run(debug=True)