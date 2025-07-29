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
   
3. Run the Streamlit App
- bash
`
streamlit run app.py
`

---

## Jupyter Notebook
-Use news_classification.ipynb to:
1. Preprocess data
2. Vectorize text using TF-IDF
3. Train MultinomialNB or other models
4. Evaluate metrics like accuracy, precision, recall, F1-score

---

## Model
- best_model.pkl contains the trained machine learning model (likely TF-IDF + MultinomialNB).
- Can be reused in app.py to serve predictions.

---

## Example Prediction
Enter a news article in the Streamlit app and get real-time prediction as:
- Real News
- Fake News
- And words that helped us doing this prediction.
---

## Contact
For any questions, feel free to open an issue or contact APatel-1305.

