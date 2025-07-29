import streamlit as st
import pickle
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
from difflib import SequenceMatcher

# Download NLTK resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')

# Load model, vectorizer
model = pickle.load(open("best_model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning utility
def clean_text(text):
    text = re.sub(r'http\S+|[^a-zA-Z\s]', '', text.lower())
    tokens = text.split()
    stops = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(w) for w in tokens if w not in stops and len(w) > 2])

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.markdown(f"""
    <h1 style='text-align: center;'>📰 Fake News Detector</h1>
    <p style='text-align: center;'>Check whether a news article is <b>Fake</b> or <b>Real</b> and see what words contributed to the result.</p>
    """, unsafe_allow_html=True)

text_input = st.text_area("Paste news text here:", height=180)

if st.button("Predict"):
    if not text_input.strip():
        st.warning("Please enter some news text.")
    else:
        cleaned = clean_text(text_input)
        vec = tfidf.transform([cleaned])
        pred = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0]

        # Display prediction and confidence bar
        st.subheader("🧾 Prediction")
        label = "🟢 Real News" if pred == 1 else "🔴 Fake News"
        st.markdown(f"**{label}**")
        st.progress(float(max(proba)))
        st.markdown(f"**Confidence:** {max(proba)*100:.2f}%")

        # Show most important words contributing to prediction
        st.subheader("🧠 Reasoning")
        feature_names = np.array(tfidf.get_feature_names_out())
        class_idx = pred
        top_idxs = np.argsort(model.feature_log_prob_[class_idx])[-10:][::-1]
        top_words = feature_names[top_idxs]
        st.markdown("Top words that influenced this prediction:")
        st.write(", ".join(top_words))
