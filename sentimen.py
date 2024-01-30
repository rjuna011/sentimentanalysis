import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_sentiment_category(sentiment_score):
    if sentiment_score > 0:
        return 'Positif'
    elif sentiment_score == 0:
        return 'Netral'
    else:
        return 'Negatif'

def main():
    st.title("Sentiment Analysis Tools")

    # Input teks dari pengguna
    text = st.text_area("Insert Your Text:")

    if st.button("Analyze"):
        if text:
            sentiment_score = analyze_sentiment(text)
            sentiment_category = get_sentiment_category(sentiment_score)

            st.success(f"Nilai Polaritas Sentimen: {sentiment_score}")
            st.success(f"Kategori Sentimen: {sentiment_category}")
        else:
            st.warning("Mohon masukkan teks terlebih dahulu.")

if __name__ == "__main__":
    main()