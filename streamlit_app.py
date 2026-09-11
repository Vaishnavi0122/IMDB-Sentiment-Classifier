import streamlit as st
import requests


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CineSense AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- Global ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(90, 70, 160, 0.18), transparent 28%),
        radial-gradient(circle at 90% 15%, rgba(30, 120, 180, 0.12), transparent 25%),
        #08090d;
}

.main .block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- Navigation ---------- */

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0 35px 0;
}

.brand {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #ffffff;
}

.brand span {
    color: #8b7cff;
}

.nav-right {
    color: #9da0ad;
    font-size: 14px;
}


/* ---------- Hero ---------- */

.hero {
    text-align: center;
    padding: 55px 20px 35px 20px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border: 1px solid rgba(139, 124, 255, 0.35);
    border-radius: 999px;
    background: rgba(139, 124, 255, 0.08);
    color: #b9b1ff;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 22px;
}

.hero-title {
    font-size: 58px;
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -2.5px;
    color: #ffffff;
    margin: 0;
}

.hero-gradient {
    background: linear-gradient(90deg, #ffffff, #a99cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 720px;
    margin: 20px auto 0 auto;
    color: #a7a9b5;
    font-size: 18px;
    line-height: 1.6;
}


/* ---------- Section ---------- */

.section-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin: 25px 0 12px 0;
}

.section-description {
    color: #858895;
    font-size: 14px;
    margin-bottom: 16px;
}


/* ---------- Text Area ---------- */

textarea {
    background: #11131a !important;
    color: #f4f4f7 !important;
    border: 1px solid #292c37 !important;
    border-radius: 16px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}

textarea:focus {
    border: 1px solid #8b7cff !important;
    box-shadow: 0 0 0 1px #8b7cff !important;
}


/* ---------- Button ---------- */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 12px;
    padding: 13px 20px;
    font-size: 16px;
    font-weight: 700;
    background: linear-gradient(90deg, #7667ff, #9b8fff);
    color: white;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(118, 103, 255, 0.25);
}


/* ---------- Result Card ---------- */

.result-card {
    margin-top: 30px;
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(
        145deg,
        rgba(24, 26, 36, 0.98),
        rgba(15, 17, 24, 0.98)
    );
    border: 1px solid #292c37;
    text-align: center;
}

.result-label {
    color: #858895;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.result-sentiment {
    font-size: 38px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
}

.confidence-text {
    color: #a7a9b5;
    font-size: 15px;
}


/* ---------- Info Cards ---------- */

.info-card {
    background: #11131a;
    border: 1px solid #252832;
    border-radius: 16px;
    padding: 22px;
    height: 100%;
}

.info-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.info-title {
    color: #ffffff;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 7px;
}

.info-text {
    color: #858895;
    font-size: 13px;
    line-height: 1.6;
}


/* ---------- Example ---------- */

.example-card {
    background: #101218;
    border: 1px solid #252832;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 10px;
}

.example-label {
    color: #9b8fff;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.example-text {
    color: #c7c9d2;
    font-size: 14px;
    line-height: 1.5;
}


/* ---------- Footer ---------- */

.footer {
    text-align: center;
    padding: 45px 0 10px 0;
    color: #626571;
    font-size: 13px;
}


/* ---------- Hide Streamlit Elements ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ---------- Mobile ---------- */

@media (max-width: 700px) {

    .hero-title {
        font-size: 40px;
    }

    .hero {
        padding-top: 30px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="nav">
<div class="brand">Cine<span>Sense</span> AI</div>
<div class="nav-right">Movie Intelligence · ML Powered</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">
<div class="hero-badge">✦ AI-POWERED SENTIMENT ANALYSIS</div>

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
""", unsafe_allow_html=True)


# =========================================================
# REVIEW INPUT
# =========================================================

st.markdown(
    '<div class="section-title">Analyze a movie review</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Paste a review below and let CineSense AI analyze its sentiment.'
    '</div>',
    unsafe_allow_html=True
)


review = st.text_area(
    "Movie review",
    placeholder=(
        "Example: The performances were incredible and the story "
        "kept me engaged from beginning to end..."
    ),
    height=190,
    label_visibility="collapsed"
)


st.write("")


# =========================================================
# PREDICTION
# =========================================================

if st.button("✦  Analyze Sentiment"):

    if not review.strip():

        st.warning("Please enter a movie review before analyzing.")

    else:

        try:

            with st.spinner("Analyzing your review..."):

                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json={"review": review},
                    timeout=10
                )

            if response.status_code == 200:

                result = response.json()

                sentiment = result["sentiment"]
                confidence = result["confidence"]

                if sentiment == "positive":
                    icon = "😊"
                    sentiment_text = "Positive"
                else:
                    icon = "😞"
                    sentiment_text = "Negative"

                st.markdown(
                    f"""
<div class="result-card">
<div class="result-label">Analysis Result</div>

<div class="result-sentiment">
{icon} {sentiment_text}
</div>

<div class="confidence-text">
Model confidence · <strong>{confidence:.2f}%</strong>
</div>
</div>
""",
                    unsafe_allow_html=True
                )

                st.write("")

                st.progress(
                    min(confidence / 100, 1.0),
                    text=f"Confidence: {confidence:.2f}%"
                )

            else:

                st.error(
                    f"The prediction service returned "
                    f"an error ({response.status_code})."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Unable to connect to the prediction service. "
                "Please make sure FastAPI is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The prediction service took too long to respond."
            )

        except Exception as e:

            st.error(
                f"An unexpected error occurred: {str(e)}"
            )


# =========================================================
# MODEL INFORMATION
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-title">'
    'Built for reliable sentiment analysis'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
<div class="info-card">
<div class="info-icon">🧠</div>
<div class="info-title">Machine Learning</div>
<div class="info-text">
TF-IDF features with word unigrams and bigrams,
combined with Logistic Regression.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
<div class="info-card">
<div class="info-icon">📊</div>
<div class="info-title">90.49% Accuracy</div>
<div class="info-text">
Evaluated on unseen IMDB test data using accuracy,
precision, recall and F1-score.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
<div class="info-card">
<div class="info-icon">⚡</div>
<div class="info-title">Instant Prediction</div>
<div class="info-text">
FastAPI serves the trained model and returns
sentiment together with confidence.
</div>
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# EXAMPLES
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-title">Try a sample review</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        """
<div class="example-card">
<div class="example-label">Positive</div>
<div class="example-text">
"An incredible movie with excellent acting and
a beautiful story. I enjoyed every moment."
</div>
</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
<div class="example-card">
<div class="example-label">Negative</div>
<div class="example-text">
"A boring and poorly written movie with terrible
acting. I couldn't wait for it to end."
</div>
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# ABOUT
# =========================================================

with st.expander("🔎 How does CineSense AI work?"):

    st.markdown("""
**1. Review Input**  
The user enters a movie review.

**2. TF-IDF Representation**  
The text is converted into numerical features based on
word importance. The improved model also considers
two-word combinations (bigrams).

**3. Logistic Regression**  
The classifier uses those features to determine whether
the review is positive or negative.

**4. Prediction**  
FastAPI returns the predicted sentiment and model confidence.

**5. Visualization**  
The Streamlit interface presents the result in an
easy-to-understand format.
""")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">
CineSense AI · IMDB Sentiment Classifier<br>
Built with Python · Scikit-learn · FastAPI · Streamlit
</div>
""",
    unsafe_allow_html=True
)