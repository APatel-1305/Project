# Movie Recommendation System

This project is a personalized **Movie Recommendation System** built using collaborative and content-based filtering techniques, with visual enhancements such as poster integration and genre formatting. It uses the [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/100k/) as the source data.

## Project Structure

Movie Recommendation System/
│
├── Pages/ # Frontend components (HTML/CSS for Streamlit pages)
├── data/ # Preprocessed dataset files (CSV, pickle, etc.)
├── ml-100k/ # Original raw MovieLens 100k dataset
├── static/posters/ # Movie poster images downloaded from API
│
├── Home.py # Streamlit main app launcher
├── Prepare_data.ipynb # Notebook to preprocess the raw dataset
├── download_posters.py # Script to fetch and save movie posters
├── make_top_movies.py # Script to identify and store top movies
├── recommender.py # Core recommendation logic (Collaborative/Content-based)
├── README.md # This file

---

## How to Run the Project

1. **Prepare the dataset**
   '''Run the notebook to preprocess and generate the cleaned files:
   Prepare_data.ipynb
   
2. **Download posters**
   '''bash
   python download_posters.py

3. Start the application
   '''bash
   streamlit run Home.py
---

## Features
1. Collaborative Filtering
2. Content-Based Filtering
3. Movie posters using TMDB API
4. Formatted genre display
5. Multiple pages (Explore_Movies, Movie_Recommendation, Contact, etc.)
6. Streamlit-based interactive UI

---

## Recommendation Techniques
1. Collaborative Filtering: Suggests movies based on user similarity and historical ratings.
2. Content-Based Filtering: Recommends movies based on genres, tags, or descriptions.

---
## Files Explained

| File/Folder           | Description |
|-----------------------|-------------|
| `Pages/`              | Contains HTML/CSS for Streamlit pages |
| `data/`               | Cleaned and preprocessed datasets |
| `ml-100k/`            | Original MovieLens 100k dataset |
| `static/posters/`     | Downloaded movie posters |
| `Home.py`             | Streamlit main application |
| `recommender.py`      | Core recommendation logic |
| `make_top_movies.py`  | Script to extract top movies |
| `download_posters.py` | Fetches posters from TMDB API |
| `Prepare_data.ipynb`  | Cleans and prepares raw data |
| `README.md`           | Project documentation |

---

## Requirements

streamlit
pandas
scikit-learn
requests
numpy

---

## Acknowledgements

1. MovieLens by GroupLens
2. TMDB API for posters





