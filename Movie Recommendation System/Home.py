import streamlit as st

st.set_page_config(page_title="Home - Movie Recommendation", layout="wide")

# Optional styling (dark mode)
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ DO THIS — Raw HTML block inside st.markdown with unsafe_allow_html
st.markdown("""
    <h1 style="text-align: center; font-size: 2.8rem; color: #ff4b4b;">
        🍿 Welcome to the Movie Recommendation System!
    </h1>

    <p style="text-align: center; font-size: 1.2rem; color: #ccc;">
        Your personalized guide to discovering movies you’ll love — powered by smart algorithms and data.
    </p>

    <ul style="font-size: 1.1rem; list-style: none; padding-left: 0;">
        <li>1️⃣ <strong>Explore Movies</strong> – Browse top-rated films with posters and genres</li>
        <li>2️⃣ <strong>Movie Recommendation</strong> – Get intelligent suggestions based on your taste</li>
        <li>3️⃣ <strong>Contact</strong> – Reach out with feedback, suggestions, or issues</li>
    </ul>

    <p style="text-align:center; margin-top:2rem; font-size:1.1rem;">
        Sit back, relax, and enjoy discovering your next favorite movie 🎬✨
    </p>
""", unsafe_allow_html=True)
