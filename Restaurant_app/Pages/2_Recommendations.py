import streamlit as st
from utils.load_data import load_recommendations

st.title("Restaurant Recommendations")

st.write("This page will be fully implemented in Week 2.")

recommendations = load_recommendations()

st.subheader("Top 10 Restaurants (Preview)")
top10 = recommendations.sort_values(by='score', ascending=False).head(10)
st.dataframe(top10)