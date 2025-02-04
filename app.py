import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"@\w+|#", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    stop_words = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

def main():
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📌 Facebook Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.write("🚀 Enter a Facebook post or comment to analyze its sentiment.")

    user_input = st.text_area("✍️ Enter your text here:", height=150)

    if st.button("🔍 Analyze Sentiment"):
        if user_input.strip():
            cleaned_text = clean_text(user_input)
            text_vectorized = vectorizer.transform([cleaned_text])
            prediction = model.predict(text_vectorized)
            sentiment_map = {0: "😐 Neutral", 1: "😡 Negative", 2: "😊 Positive"}
            result = sentiment_map.get(prediction[0], "🤔 Unknown Sentiment")
            st.markdown(f"<h3 style='text-align: center; color: #2ECC71;'>🎯 Sentiment: {result}</h3>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter some text to analyze.")

if __name__ == "__main__":
    main()
