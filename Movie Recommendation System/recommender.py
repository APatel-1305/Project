# recommender.py

import os
import pandas as pd
import re
import requests
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class RecommenderSystem:
    def __init__(self, movies_path='data/movies.csv', ratings_path='data/ratings.csv'):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.movies['genres'] = self.movies['genres'].str.replace('|', ', ')
        self.analyzer = SentimentIntensityAnalyzer()
        self.default_poster = "static/default_poster.jpg"
        self._prepare_models()

    def _prepare_models(self):
        genre_matrix = CountVectorizer().fit_transform(self.movies['genres'].str.replace(', ', ' '))
        self.genre_sim = cosine_similarity(genre_matrix)

        ratings_matrix = self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
        self.ratings_matrix = ratings_matrix
        self.collab_sim = cosine_similarity(ratings_matrix)

    def fetch_poster(self, title):
        safe_title = re.sub(r"[\\/*?<>:\"|]", "", re.sub(r"\s*\(\d{4}\)", "", title)).strip()
        local_path = f"posters/{safe_title}.jpg"
        if os.path.exists(local_path):
            return local_path
        return self.default_poster

    def fetch_imdb_link(self, title):
        base_url = "https://api.themoviedb.org/3/search/movie"
        API_KEY = '3395570476004276441e923c8148f5a4'
        clean_title = re.sub(r"\s*\(\d{4}\)", "", title).strip()

        try:
            response = requests.get(base_url, params={"api_key": API_KEY, "query": clean_title})
            response.raise_for_status()
            data = response.json()
            if data['results']:
                movie_id = data['results'][0].get('id')
                if movie_id:
                    return f"https://www.themoviedb.org/movie/{movie_id}"
        except Exception:
            return None

    def get_star_rating(self, score):
        stars = round((score + 1) * 2.5, 1)  # Converts -1 to 1 range into 0 to 5
        full_stars = int(stars)
        half_star = stars - full_stars >= 0.5
        star_display = '⭐' * full_stars + ('✨' if half_star else '')
        return f"{star_display} ({stars}/5)"

    def get_review_sentiment_text(self, title):
        fake_reviews = [
            f"{title} was absolutely amazing! A must-watch.",
            f"{title} had great acting and story.",
            f"I didn't enjoy {title} much.",
            f"{title} was boring and too long.",
            f"An emotional rollercoaster with {title}."
        ]
        text = fake_reviews[hash(title) % len(fake_reviews)]
        score = self.analyzer.polarity_scores(text)['compound']
        rating = self.get_star_rating(score)
        return f"{rating}: {text}"

    def get_content_recommendations(self, movie_title, top_n=5, sentiment_filter=False):
        idx_list = self.movies[self.movies['title'].str.lower() == movie_title.lower()].index.tolist()
        if not idx_list:
            idx_list = self.movies[self.movies['title'].str.contains(movie_title, case=False, na=False)].index.tolist()
        if not idx_list:
            return pd.DataFrame()

        idx = idx_list[0]
        sim_scores = list(enumerate(self.genre_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = [score for score in sim_scores if score[0] != idx][:top_n * 2]
        movie_indices = [i[0] for i in sim_scores]

        recs = self.movies.iloc[movie_indices][['movieId', 'title', 'genres']].copy()
        recs['poster'] = recs['title'].apply(self.fetch_poster)
        recs['review'] = recs['title'].apply(self.get_review_sentiment_text)
        recs['imdb_link'] = recs['title'].apply(self.fetch_imdb_link)

        if sentiment_filter:
            recs = recs[recs['review'].str.contains('⭐{4,}|✨')]

        return recs.head(top_n).reset_index(drop=True)

    def get_collab_recommendations(self, user_id, top_n=5, sentiment_filter=False):
        if user_id not in self.ratings_matrix.index:
            return pd.DataFrame()

        user_ratings = self.ratings_matrix.loc[user_id]
        sim_users = self.collab_sim[user_id - 1]
        sim_scores = sorted(list(enumerate(sim_users)), key=lambda x: x[1], reverse=True)[1:6]

        movie_scores = {}
        for sim_user, score in sim_scores:
            rated = self.ratings_matrix.iloc[sim_user]
            for movie_id, rating in rated.items():
                if rating > 0 and user_ratings[movie_id] == 0:
                    movie_scores[movie_id] = movie_scores.get(movie_id, 0) + rating * score

        top_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)[:top_n * 2]
        movie_ids = [m[0] for m in top_movies]

        recs = self.movies[self.movies['movieId'].isin(movie_ids)][['movieId', 'title', 'genres']].copy()
        recs['poster'] = recs['title'].apply(self.fetch_poster)
        recs['review'] = recs['title'].apply(self.get_review_sentiment_text)
        recs['imdb_link'] = recs['title'].apply(self.fetch_imdb_link)

        if sentiment_filter:
            recs = recs[recs['review'].str.contains('⭐{4,}|✨')]

        return recs.head(top_n).reset_index(drop=True)
