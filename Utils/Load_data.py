import pandas as pd

def load_reviews():
    return pd.read_csv("data/reviews_cleaned.csv")

def load_business():
    return pd.read_csv("data/business_cleaned.csv")

def load_recommendations():
    return pd.read_csv("data/recommendations.csv")