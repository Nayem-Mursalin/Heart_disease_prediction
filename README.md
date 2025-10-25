# Heart Disease Prediction — FastAPI + Docker

## Quick start (local)

1. Put `heart.csv` (from Kaggle) into `data/`.
2. Create venv & install:


python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


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



## Deploy to Render (Docker service)
1. Push your repo to GitHub.
2. On Render:
   - New → Web Service → Connect GitHub → Select repository.
   - Environment: Docker.
   - Build context: root (if Dockerfile in repo root).
   - Start service; Render will build the Docker image and run it.
3. After deploy, check `<your-render-url>/docs` and test `/predict`.

## Notes & improvements
- Add model versioning (filename like `heart_model_v1.joblib`) and `/info` returns version.
- Add request validation & schema examples.
- Add logging, Sentry, and basic auth for the API in production.
- Use CI to run `train.py` and package model as artifact (or keep model saved & versioned in Git LFS).
