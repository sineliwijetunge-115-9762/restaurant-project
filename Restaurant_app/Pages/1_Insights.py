import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.load_data import load_reviews, load_recommendations

st.title("Insights Dashboard")

# Load data
reviews = load_reviews()
recommendations = load_recommendations()

# Rating distribution
st.subheader("Rating Distribution")
fig, ax = plt.subplots()
sns.histplot(reviews['stars'], bins=5, ax=ax)
st.pyplot(fig)

# Sentiment distribution
st.subheader("Sentiment Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(x='label', data=reviews, ax=ax2)
st.pyplot(fig2)

# Recommendation score distribution
st.subheader("Recommendation Score Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(recommendations['score'], bins=20, ax=ax3)
st.pyplot(fig3)

st.subheader("Top Cuisines")
top_cuisines = business['categories'].value_counts().head(10)
st.bar_chart(top_cuisines)

st.subheader("Average Rating by City")
avg_rating = business.groupby('city')['stars'].mean().sort_values(ascending=False).head(10)
st.bar_chart(avg_rating)

st.subheader("Review Length Distribution")
reviews['review_length'] = reviews['text'].str.len()
st.histogram(reviews['review_length'])
