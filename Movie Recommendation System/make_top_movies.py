import pandas as pd
import os

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Compute average rating per movie
avg_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
avg_ratings.columns = ["movieId", "rating"]

# Merge with movie metadata
merged = pd.merge(movies, avg_ratings, on="movieId")

# Format genres
merged["genres"] = merged["genres"].str.replace("|", ", ")

# Sort by rating
top_100 = merged.sort_values("rating", ascending=False).head(100).copy()

# Add placeholder IMDb links (or real ones if you have them)
top_100["imdb_link"] = "https://www.imdb.com/"

# Add local poster path (e.g., from static/posters/<movieId>.jpg)
import re
def clean_title(title):
    title = re.sub(r"[\\/*?<>:\"|]", "", title)
    title = re.sub(r"\s*\(\d{4}\)", "", title)
    return title.strip()

top_100["poster"] = top_100["title"].apply(lambda t: f"static/posters/{clean_title(t)}.jpg")

# Save
os.makedirs("data", exist_ok=True)
top_100.to_csv("data/top_100_movies.csv", index=False)

print("✅ top_100_movies.csv generated with rating, poster, and IMDb link")

