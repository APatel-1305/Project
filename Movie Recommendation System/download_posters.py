import os
import re
import requests
import pandas as pd

API_KEY = '3395570476004276441e923c8148f5a4'
SAVE_DIR = 'static/posters'
os.makedirs(SAVE_DIR, exist_ok=True)

def clean_title(title):
    title = re.sub(r"[\\/*?<>:\"|]", "", title)        # Remove invalid characters
    title = re.sub(r"\s*\(\d{4}\)", "", title)         # Remove year in brackets
    title = title.replace(":", "").strip()
    return title

def download_poster(title):
    query = clean_title(title)
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": API_KEY, "query": query}
    try:
        res = requests.get(url, params=params).json()
        if res["results"]:
            path = res["results"][0].get("poster_path")
            if path:
                img_url = f"https://image.tmdb.org/t/p/w500{path}"
                img_data = requests.get(img_url).content
                filename = os.path.join(SAVE_DIR, f"{query}.jpg")
                with open(filename, "wb") as f:
                    f.write(img_data)
                print(f"✅ Downloaded: {query}")
            else:
                print(f"⚠️ No poster for: {query}")
    except Exception as e:
        print(f"❌ Error for {query}: {e}")

if __name__ == "__main__":
    df = pd.read_csv("data/movies.csv")
    titles = df["title"].unique()
    for title in titles:
        clean_name = clean_title(title)
        filename = os.path.join(SAVE_DIR, f"{clean_name}.jpg")
        if not os.path.exists(filename):
            download_poster(title)

