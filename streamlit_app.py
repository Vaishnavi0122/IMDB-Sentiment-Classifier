import streamlit as st
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CineSense AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

MODEL_PATH = "models/imdb_sentiment_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("Unable to load the trained sentiment model.")
    st.code(str(e))
    st.stop()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(90, 70, 160, 0.18), transparent 28%),
        radial-gradient(circle at 90% 15%, rgba(30, 120, 180, 0.12), transparent 25%),
        #08090d;
    color: #f5f5f7;
}

/* Hide Streamlit default elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* Main container */

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* Header */

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 90px;
}

.brand {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
}

.brand-gradient {
    background: linear-gradient(90deg, #8b7cff, #b27cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.header-tag {
    color: #8e9bb5;
    font-size: 14px;
    font-weight: 500;
}


/* Hero */

.hero {
    text-align: center;
    margin-bottom: 80px;
}

.hero-badge {
    display: inline-block;
    padding: 10px 18px;
    border: 1px solid rgba(139, 124, 255, 0.45);
    border-radius: 30px;
    color: #b9a9ff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 28px;
}

.hero-title {
    font-size: 58px;
    line-height: 1.08;
    letter-spacing: -3px;
    font-weight: 800;
    margin: 0 auto;
    max-width: 850px;
    color: #f7f7f8;
}

.hero-gradient {
    background: linear-gradient(90deg, #8f7cff, #b27cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 800px;
    margin: 28px auto 0 auto;
    color: #91a0bb;
    font-size: 16px;
    line-height: 1.8;
}


/* Section */

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 8px;
    color: #ffffff;
}

.section-description {
    color: #7f8da7;
    font-size: 14px;
    margin-bottom: 18px;
}


/* Text area */

.stTextArea textarea {
    background: #11131a !important;
    color: #f3f3f5 !important;
    border: 1px solid #282c39 !important;
    border-radius: 14px !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
    padding: 18px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #806cff !important;
    box-shadow: 0 0 0 1px #806cff !important;
}

.stTextArea textarea::placeholder {
    color: #66718a !important;
}


/* Analyze button */

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    border: 1px solid rgba(139, 124, 255, 0.45);
    background: linear-gradient(
        135deg,
        rgba(115, 91, 220, 0.9),
        rgba(90, 65, 180, 0.9)
    );
    color: white;
    font-size: 15px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #a89aff;
    transform: translateY(-1px);
    box-shadow: 0 8px 30px rgba(104, 82, 220, 0.25);
}


/* Result card */

.result-card {
    margin-top: 35px;
    padding: 32px;
    border-radius: 18px;
    background: linear-gradient(
        145deg,
        rgba(25, 27, 37, 0.98),
        rgba(16, 18, 25, 0.98)
    );
    border: 1px solid #292d3b;
    text-align: center;
}

.result-label {
    color: #7f8da7;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.result-sentiment {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-positive {
    color: #65d69a;
}

.result-negative {
    color: #ff7272;
}

.confidence-text {
    color: #a2aec3;
    font-size: 14px;
    margin-top: 10px;
}

.confidence-bar {
    width: 100%;
    height: 8px;
    background: #282c38;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 14px;
}

.confidence-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #806cff, #b07cff);
}


/* Information cards */

.info-card {
    background: #11131a;
    border: 1px solid #252936;
    border-radius: 15px;
    padding: 22px;
    height: 100%;
}

.info-number {
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
}

.info-title {
    color: #8d99b0;
    font-size: 13px;
    margin-top: 6px;
}


/* Samples */

.sample-card {
    background: #11131a;
    border: 1px solid #252936;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}

.sample-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #8e7cff;
    margin-bottom: 8px;
}

.sample-text {
    color: #b2bccd;
    font-size: 13px;
    line-height: 1.6;
}


/* Divider */

.divider {
    height: 1px;
    background: #20232d;
    margin: 70px 0 40px 0;
}


/* Footer */

.footer {
    text-align: center;
    color: #59657c;
    font-size: 12px;
    padding-top: 30px;
}


/* Expander */

.streamlit-expanderHeader {
    color: #dce1eb !important;
    font-weight: 600 !important;
}

.streamlit-expanderContent {
    color: #8f9bb0 !important;
    line-height: 1.7 !important;
}


/* Responsive */

@media (max-width: 768px) {

    .hero-title {
        font-size: 40px;
        letter-spacing: -2px;
    }

    .top-header {
        margin-bottom: 55px;
    }

    .header-tag {
        display: none;
    }

}

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
"""
<div class="top-header">
<div class="brand">Cine<span class="brand-gradient">Sense AI</span></div>
<div class="header-tag">Movie Intelligence · ML Powered</div>
</div>
""",
unsafe_allow_html=True
)


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
"""
<div class="hero">

<div class="hero-badge">
✦ AI-POWERED SENTIMENT ANALYSIS
</div>

<h1 class="hero-title">
Understand the <span class="hero-gradient">feeling</span><br>
behind every review.
</h1>

<p class="hero-subtitle">
Analyze movie reviews with a machine learning model trained on
50,000 IMDB reviews. Discover whether the audience feels
positive or negative — instantly.
</p>

</div>
""",
unsafe_allow_html=True
)


# ============================================================
# REVIEW INPUT
# ============================================================

st.markdown(
"""
<div class="section-title">
Analyze a movie review
</div>

<div class="section-description">
Write or paste a movie review below and let CineSense AI understand its sentiment.
</div>
""",
unsafe_allow_html=True
)


review = st.text_area(
    label="Movie Review",
    placeholder="Write or paste a movie review here...",
    height=190,
    label_visibility="collapsed"
)


# ============================================================
# PREDICTION
# ============================================================

if st.button("✦  Analyze Sentiment"):

    if not review.strip():

        st.warning("Please enter a movie review before analyzing.")

    else:

        with st.spinner("Analyzing your review..."):

            try:

                # Directly use the trained pipeline.
                # No FastAPI / localhost connection is required.

                prediction = model.predict([review])[0]

                probabilities = model.predict_proba([review])[0]

                confidence = max(probabilities) * 100

                sentiment = str(prediction).lower()

                if sentiment == "positive":

                    icon = "😊"
                    sentiment_class = "result-positive"
                    display_sentiment = "Positive"

                else:

                    icon = "😞"
                    sentiment_class = "result-negative"
                    display_sentiment = "Negative"


                # ------------------------------------------------
                # RESULT
                # ------------------------------------------------

                st.markdown(
                f"""
<div class="result-card">

<div class="result-label">
PREDICTION RESULT
</div>

<div class="result-sentiment {sentiment_class}">
{icon} {display_sentiment}
</div>

<div class="confidence-text">
Model confidence: <strong>{confidence:.2f}%</strong>
</div>

<div class="confidence-bar">
<div class="confidence-fill" style="width: {confidence:.2f}%;"></div>
</div>

</div>
""",
                unsafe_allow_html=True
                )


            except Exception as e:

                st.error("Something went wrong while analyzing the review.")

                with st.expander("Technical details"):
                    st.code(str(e))


# ============================================================
# MODEL INFORMATION
# ============================================================

st.markdown('<div style="height: 45px;"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
    """
<div class="info-card">

<div class="info-number">
Machine Learning
</div>

<div class="info-title">
TF-IDF + Logistic Regression
</div>

</div>
""",
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
<div class="info-card">

<div class="info-number">
90.49%
</div>

<div class="info-title">
Accuracy on unseen test data
</div>

</div>
""",
    unsafe_allow_html=True
    )


with col3:

    st.markdown(
    """
<div class="info-card">

<div class="info-number">
Instant
</div>

<div class="info-title">
Real-time sentiment prediction
</div>

</div>
""",
    unsafe_allow_html=True
    )


# ============================================================
# SAMPLE REVIEWS
# ============================================================

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
"""
<div class="section-title">
Try a sample review
</div>

<div class="section-description">
Use one of these examples to test CineSense AI.
</div>
""",
unsafe_allow_html=True
)


sample1 = """
<div class="sample-card">

<div class="sample-label">
POSITIVE EXAMPLE
</div>

<div class="sample-text">
"This movie was absolutely fantastic. The acting was brilliant,
the story was engaging, and I enjoyed every moment of it."
</div>

</div>
"""


sample2 = """
<div class="sample-card">

<div class="sample-label">
NEGATIVE EXAMPLE
</div>

<div class="sample-text">
"This movie was extremely disappointing. The story was boring,
the acting felt weak, and I couldn't wait for it to end."
</div>

</div>
"""


st.markdown(sample1, unsafe_allow_html=True)
st.markdown(sample2, unsafe_allow_html=True)


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with st.expander("How does CineSense AI work?"):

    st.markdown(
    """
    **1. User Input**

    A movie review is entered into the application.

    **2. TF-IDF Feature Extraction**

    The trained TF-IDF vectorizer converts the review into numerical
    features. The model uses unigram and bigram features to capture
    useful phrases such as "not good".

    **3. Logistic Regression**

    The trained Logistic Regression classifier analyzes the extracted
    features and predicts whether the review is positive or negative.

    **4. Confidence Score**

    The probability returned by the classifier is displayed as the
    model's confidence.

    **5. Result**

    CineSense AI displays the final sentiment instantly.
    """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
"""
<div class="footer">
CineSense AI · Built with Python, Scikit-learn and Streamlit
<br>
End-to-End IMDB Sentiment Classification Project
</div>
""",
unsafe_allow_html=True
)