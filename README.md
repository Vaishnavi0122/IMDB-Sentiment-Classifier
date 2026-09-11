# 🎬 IMDB Sentiment Classifier

An end-to-end Machine Learning project that classifies IMDB movie reviews as **Positive** or **Negative** using TF-IDF features and Logistic Regression.

The trained model is served through a **FastAPI REST API** and connected to a professional **Streamlit web application** called **CineSense AI**.

---

## 📌 Project Overview

Movie reviews contain valuable information about audience opinions. Manually analyzing thousands of reviews is difficult and time-consuming.

This project uses Natural Language Processing (NLP) and Machine Learning to automatically determine whether a movie review expresses a **positive** or **negative** sentiment.

### What the application does

1. Accepts a movie review from the user.
2. Converts the review into numerical TF-IDF features.
3. Uses a trained Logistic Regression classifier.
4. Predicts the sentiment.
5. Returns the predicted sentiment with a confidence score.
6. Displays the result through a professional web interface.

---

## 🎯 Objectives

- Perform exploratory data analysis on the IMDB dataset.
- Prepare textual data for machine learning.
- Convert text into numerical features using TF-IDF.
- Build a Logistic Regression sentiment classifier.
- Establish a baseline model.
- Improve the baseline using word bigrams.
- Evaluate the model using standard classification metrics.
- Perform error analysis on incorrect predictions.
- Save the trained model as a reusable pipeline.
- Deploy the model through FastAPI.
- Build a user-friendly Streamlit frontend.

---

## 📊 Dataset

The project uses the **IMDB Movie Review Dataset** containing:

- **50,000 movie reviews**
- **25,000 reviews for training**
- **25,000 reviews for testing**
- Two sentiment classes:
  - Positive
  - Negative

The dataset contains two columns:

| Column | Description |
|---|---|
| `review` | Movie review text |
| `sentiment` | Positive or Negative |

> The dataset CSV is not included in this repository because it is excluded through `.gitignore`. Place `IMDB Dataset.csv` inside the `data/` directory when working locally.

---

## 🧠 Machine Learning Approach

### 1. Text Representation

The reviews are converted into numerical features using:

**TF-IDF (Term Frequency–Inverse Document Frequency)**

The final model uses:

```text
TF-IDF
ngram_range = (1, 2)
