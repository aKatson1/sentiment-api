from transformers import pipeline

# Load the model ONCE at startup
sentiment_pipeline = pipeline("sentiment-analysis")