
# Sentiment Analysis API

A REST API built with FastAPI that performs sentiment analysis using a pretrained DistilBERT model. It classifies text as **POSITIVE** or **NEGATIVE**, returns a confidence score, and logs each prediction to a PostgreSQL database. The application is containerized with Docker and deployed on Google Cloud Run.

## Tech Stack

FastAPI · HuggingFace Transformers · PostgreSQL · SQLAlchemy · Docker · Google Cloud Run · Google Cloud SQL

## Run Locally (Docker)

```bash
git clone https://github.com/aKatson1/sentiment-api.git
cd sentiment-api
docker compose up --build
```

Open:

http://localhost:8080/docs

## Run Locally (without Docker)

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/sentimentdb
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API

POST /predict

```json
{
  "text": "I love this product"
}
```

Response:

```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

GET /predictions — returns all logged predictions. 
GET /health — returns application status.

## Deployment

Deployed on Google Cloud Run with PostgreSQL on Cloud SQL. A previous deployment of this API (https://sentiment-api-1095577141849.us-central1.run.app/docs) has been decommissioned to avoid unnecessary cloud costs. 


## Futures Improvements

- Add authentication to restrict access to the API  
- Add rate limiting to prevent excessive or abusive requests  
- Restrict and control what data is exposed in the `/predictions` endpoint  
- Add logging and error tracking for better debugging and monitoring  
- Improve or fine-tune the model for more domain-specific sentiment tasks  

## System Preview

### GET /predict Endpoint
<img src="docs/swagger-get-predict.png" width="500"/>

### POST /predict Endpoint
<img src="docs/swagger-post-predict.png" width="500"/>

### Database (Cloud SQL)

<img src="docs/cloud-sql-query.png" width="500"/>