# Heart Disease Prediction — FastAPI + Docker

## Quick start (local)

1. Put `heart.csv` (from Kaggle) into `data/`.
2. Create venv & install:

3. Train model:

This creates `model/heart_model.joblib`.

4. Run locally with docker-compose:

Open Swagger UI: http://localhost:8000/docs

## Test endpoints

Health: http://localhost:8000/health


Info: http://localhost:8000/info

curl -X POST "http://localhost:8000/predict
" -H "Content-Type: application/json" -d '{
"age": 63,
"sex": 1,
"cp": 3,
"trestbps": 145,
"chol": 233,
"fbs": 1,
"restecg": 0,
"thalach": 150,
"exang": 0,
"oldpeak": 2.3,
"slope": 0,
"ca": 0,
"thal": 1
}'
