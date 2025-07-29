import streamlit as st
import pandas as pd
import os
import base64
import re
from recommender import RecommenderSystem

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Theme settings
bg_color = "#1e1e1e"
text_color = "#ffffff"
card_bg = "#2a2a2a"
rating_color = "#FFD700"  # gold

# Apply dark theme styles
st.markdown(f"""
    <style>
        html, body, [class*="css"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .st-bw {{ background-color: {card_bg} !important; }}
        .stRadio > div {{
            background-color: {card_bg} !important;
            color: {text_color} !important;
            border-radius: 8px;
            padding: 10px;
        }}
        img {{ filter: brightness(0.9); }}
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommendation System")

# Reuse the same cleaning logic used for downloading posters
def clean_title(title):
    title = re.sub(r"[\\/*?<>:\"|]", "", title)        # Remove invalid characters
    title = re.sub(r"\s*\(\d{4}\)", "", title)         # Remove year in brackets
    title = title.replace(":", "").strip()
    return title

# Initialize recommender system
recommender = RecommenderSystem('data/movies.csv', 'data/ratings.csv')

# Choose recommendation type
option = st.radio("Choose Recommendation Type:", ("Content-Based", "Collaborative Filtering"))

def display_results(results):
    if not results.empty:
        st.markdown("### Top 5 Recommendations:")
        num_cols = 3 if len(results) > 3 else len(results)
        rows = [results[i:i+num_cols] for i in range(0, len(results), num_cols)]

        for row in rows:
            cols = st.columns(len(row))
            for i, row_data in enumerate(row.itertuples(index=False)):
                with cols[i]:
                    # Construct cleaned poster filename
                    clean_name = clean_title(row_data.title)
                    poster_path = os.path.join("static/posters", clean_name + ".jpg")

                    # Try loading the poster image
                    if os.path.exists(poster_path):
                        try:
                            with open(poster_path, "rb") as f:
                                encoded = base64.b64encode(f.read()).decode()
                                poster_html = f"<img src='data:image/jpeg;base64,{encoded}' style='width:200px; height:300px; object-fit:cover; border-radius:10px; display:block; margin:0 auto;'/>"
                        except Exception as e:
                            poster_html = "<div style='width:200px; height:300px; background-color:#888888; border-radius:10px; margin:0 auto;'></div>"
                    else:
                        poster_html = "<div style='width:200px; height:300px; background-color:#888888; border-radius:10px; margin:0 auto;'></div>"

                    # Render full card: poster + metadata (always)
                    st.markdown(f"""
                        <div style='text-align: center; margin-bottom: 1.5rem; background-color:{card_bg}; padding: 1rem; border-radius: 10px;'>
                            {poster_html}
                            <div style='font-weight: bold; margin-top: 0.5rem; color: {text_color};'>{row_data.title}</div>
                            <div style='color: gray; font-size: 0.9rem;'>{row_data.genres}</div>
                        </div>
                    """, unsafe_allow_html=True)

# Content-based recommendation
if option == "Content-Based":
    movie = st.text_input("Enter a movie you like:")
    if st.button("Get Recommendations"):
        if movie:
            results = recommender.get_content_recommendations(movie)
            display_results(results)

# Collaborative filtering recommendation
elif option == "Collaborative Filtering":
    user_id = st.number_input("Enter your user ID (1–943):", min_value=1, max_value=943)
    if st.button("Get Recommendations"):
        results = recommender.get_collab_recommendations(user_id)
        display_results(results)

