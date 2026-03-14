import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("upi_fraud_dataset.csv")

# Encode handle (text → number)
le = LabelEncoder()
df["handle"] = le.fit_transform(df["handle"])

# Features (X)
X = df[
    [
        "amount",
        "suspicious_keyword",
        "digit_count",
        "upi_length",
        "handle",
        "brand_impersonation",
        "trap_amount",
        "report_count",
        "is_blacklisted",
        "merchant_age_days"
    ]
]

# Target (Y)
y = df["is_fraud"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "fraud_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("Model saved as fraud_model.pkl")