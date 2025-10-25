# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

DATA_PATH = "data/heart.csv"
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "heart_model.joblib")

os.makedirs(MODEL_DIR, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)

# Inspect columns (example columns expected)
# print(df.columns)

# Typical columns in that Kaggle dataset:
FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]
TARGET = "target"  # 1 = disease, 0 = no disease

X = df[FEATURES]
y = df[TARGET]

# Simple train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Pipeline: scaler + RandomForest
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
])

print("Training model...")
pipe.fit(X_train, y_train)

# Evaluation (we don't need SOTA, just sanity)
y_pred = pipe.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save
joblib.dump({
    "model": pipe,
    "features": FEATURES,
    "model_type": "RandomForestClassifier Pipeline"
}, MODEL_PATH)

print(f"Saved model to {MODEL_PATH}")
