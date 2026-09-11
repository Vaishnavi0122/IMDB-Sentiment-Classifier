# 🎬 IMDB Sentiment Classifier

An end-to-end Machine Learning project that classifies IMDB movie reviews as **Positive** or **Negative** using **TF-IDF feature extraction** and **Logistic Regression**.

The trained model is integrated into a professional Streamlit web application called **CineSense AI**, which provides instant sentiment predictions with confidence scores.

## 🚀 Live Demo

👉 **[Try CineSense AI](https://imdb-sentiment-classifier-nbqnngkyrgvng7dbwr8ta.streamlit.app/)**

Analyze movie reviews instantly using the trained Machine Learning model.

---

## 📌 Project Overview

Sentiment analysis is a Natural Language Processing (NLP) task used to determine the emotional tone of text.

In this project, an IMDB movie review dataset containing **50,000 reviews** is used to train a binary sentiment classification model.

The system predicts whether a given movie review expresses:

- 😊 **Positive Sentiment**
- 😞 **Negative Sentiment**

The project demonstrates a complete Machine Learning workflow, from data exploration and preprocessing to model development, evaluation, API development, and deployment.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA) on movie review data
- Prepare text data for Machine Learning
- Convert text into numerical features using TF-IDF
- Build a Logistic Regression sentiment classifier
- Establish a baseline model
- Improve the model using unigram and bigram features
- Evaluate model performance using multiple metrics
- Perform error analysis
- Save the trained Machine Learning pipeline
- Develop a REST API using FastAPI
- Build an interactive frontend using Streamlit
- Deploy the application using Streamlit Community Cloud

---

## 🧠 Machine Learning Approach

### 1. Data

The project uses the **IMDB Dataset**, containing:

- **50,000 movie reviews**
- **25,000 reviews for training**
- **25,000 reviews for testing**
- Two sentiment classes:
  - Positive
  - Negative

The dataset is intentionally excluded from the GitHub repository because of its size.

---

### 2. Text Preprocessing

The project follows a **minimal preprocessing approach** to preserve useful information from the original reviews.

The TF-IDF vectorizer handles text normalization such as lowercasing.

Aggressive preprocessing techniques such as:

- Stopword removal
- Stemming
- Lemmatization
- Excessive punctuation removal

were avoided because punctuation, word forms, and contextual words can contain useful sentiment information.

---

### 3. Feature Extraction

**TF-IDF (Term Frequency–Inverse Document Frequency)** is used to convert movie reviews into numerical feature vectors.

Two configurations were explored:

#### Baseline

```text
TF-IDF Unigrams
