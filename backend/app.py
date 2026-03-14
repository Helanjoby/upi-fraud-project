from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Enable CORS
CORS(app)

# Load dataset
data = pd.read_csv("upi_fraud_dataset.csv")

# remove extra spaces
data["upi_id"] = data["upi_id"].str.strip()

@app.route("/")
def home():
    return "UPI Fraud Detection Backend Running"

@app.route("/check_transaction", methods=["POST"])
def check_transaction():

    data_json = request.get_json()

    upi_id = data_json["upi_id"]

    fraud = data[data["upi_id"] == upi_id]

    if not fraud.empty:
        result = "⚠️ Fraud Merchant Detected"
    else:
        result = "✅ Safe Transaction"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)