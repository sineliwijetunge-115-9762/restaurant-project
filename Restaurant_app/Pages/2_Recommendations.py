import streamlit as st
import pandas as pd
import numpy as np
from utils.load_data import load_business, load_recommendations

st.title("Restaurant Recommendations")

# Loading data
business = load_business()
recs = load_recommendations()

df = recs.merge(business, on="business_id", how="left")

st.sidebar.header("Filters")

# Cuisine filter
all_cuisines = sorted(df['categories'].dropna().unique())
selected_cuisine = st.sidebar.selectbox("Cuisine", ["All"] + all_cuisines)

# Price filter
price_options = ["All", "$", "$$", "$$$", "$$$$"]
selected_price = st.sidebar.selectbox("Price Range", price_options)

# Distance filter
if "distance_km" in df.columns:
    max_distance = st.sidebar.slider("Max Distance (km)", 1, 30, 10)
else:
    max_distance = None

filtered = df.copy()

if selected_cuisine != "All":
    filtered = filtered[filtered['categories'] == selected_cuisine]

if selected_price != "All":
    filtered = filtered[filtered['price'] == selected_price]

if max_distance is not None:
    filtered = filtered[filtered['distance_km'] <= max_distance]

filtered = filtered.sort_values(by="score", ascending=False)

st.subheader("Top Recommendations")

cols_to_show = ['name', 'categories', 'stars', 'review_count', 'price', 'score']
st.dataframe(filtered[cols_to_show].head(10))
