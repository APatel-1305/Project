# News Article Classification (Fake or Real)

This project classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP) and Machine Learning. It includes a trained model, a Jupyter notebook for exploration, and a `Streamlit` web application for deployment.

---

## Project Structure

```text
├── models/fake_news_dataset/News_Dataset/
│ ├── True.csv # Contains real news articles
│ └── Fake.csv # Contains fake news articles
├── news_classification.ipynb # Jupyter Notebook for data preprocessing, training, and evaluation
├── best_model.pkl # Serialized trained ML model
├── app.py # Streamlit app for live predictions
└── README.md # Project documentation
```
---

## Dataset

The dataset is stored in:
**models/fake_news_dataset/News_Dataset/
- `True.csv`: Contains real news articles.
- `Fake.csv`: Contains fake news articles.

Each file includes:
- `title`: Headline of the article.
- `text`: Full article content.
- `subject` and `date` (optional depending on dataset source).

---

## How to Run the Project

1. Install Required Packages
- bash
`
pip install pandas numpy scikit-learn streamlit nltk re pickle matplotlib seaborn
`

2. Run the Jupyter Notebook
`
news_classification.ipynb
`
