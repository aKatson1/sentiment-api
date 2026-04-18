from transformers import pipeline

# Load the model ONCE at startup, default to distilbert
sentiment_pipeline = pipeline("sentiment-analysis")