import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(page_title="Explore Movies", layout="wide")

# Theme settings
bg_color = "#1e1e1e"
text_color = "#ffffff"
card_bg = "#2a2a2a"
rating_color = "#FFD700"  # gold

st.markdown(f"""
    <style>
        html, body, [class*="css"] {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .st-bw {{ background-color: {card_bg} !important; }}
    </style>
""", unsafe_allow_html=True)

st.title("🍿 Explore Top Movies")

movies = pd.read_csv("data/top_100_movies.csv")

min_rating = st.slider("Minimum Rating:", 0.0, 5.0, 4.0, 0.1)
genre_options = sorted(set(g for sublist in movies['genres'].str.split(', ') for g in sublist))
selected_genre = st.selectbox("Search by Genre:", ["All"] + genre_options)

filtered = movies[movies['rating'] >= min_rating]
if selected_genre != "All":
    filtered = filtered[filtered['genres'].str.contains(selected_genre)]

st.markdown(f"### Showing {len(filtered)} Movies")

# Display cards in grid layout
num_cols = 4
rows = [filtered[i:i+num_cols] for i in range(0, len(filtered), num_cols)]
for row in rows:
    cols = st.columns(num_cols)
    for i, row_data in enumerate(row.itertuples()):
        with cols[i]:
            if os.path.exists(row_data.poster):
                with open(row_data.poster, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode()
                    poster_html = f"<img src='data:image/jpeg;base64,{encoded}' style='width:200px; height:300px; object-fit:cover; border-radius:10px; display:block; margin:0 auto;'/>"
            else:
                poster_html = f"<div style='width:200px; height:300px; background-color:#888888; border-radius:10px; margin:0 auto;'></div>"

            st.markdown(f"""
                <div style='text-align: center; margin-bottom: 1.5rem; background-color:{card_bg}; padding: 1rem; border-radius: 10px;'>
                    {poster_html}
                    <div style='font-weight: bold; margin-top: 0.5rem; color: {text_color};'>{row_data.title}</div>
                    <div style='color: gray; font-size: 0.9rem;'>{row_data.genres}</div>
                    <div style='font-size: 0.85rem; margin-top: 0.3rem; color: {rating_color};'>⭐ {row_data.rating:.1f} / 5</div>
                </div>
            """, unsafe_allow_html=True)

st.download_button("⬇️ Download Movies as CSV", data=filtered.to_csv(index=False), file_name="explore_movies.csv", mime="text/csv")