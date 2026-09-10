import streamlit as st
from transformers import pipeline
from googleapiclient.discovery import build
import pandas as pd
import plotly.express as px

# 1. Load pre-trained multilingual sentiment model from Hugging Face
# 1. Load pre-trained multilingual sentiment model from Hugging Face
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis", truncation=True, max_length=512)
sentiment_analyzer = load_model()

# 2. Function to fetch YouTube comments
def fetch_youtube_comments(video_url, api_key, max_comments=50):
    try:
        if "watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        else:
            return None, "Invalid YouTube URL format."

        youtube = build('youtube', 'v3', developerKey=api_key)
        
        comments = []
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            
        return comments, None
    except Exception as e:
        return None, str(e)

# 3. Streamlit UI Layout
st.set_page_config(page_title="Multilingual YouTube Vibe Checker", layout="centered")

st.title("🌍 Multilingual YouTube Comment Vibe Checker")
st.markdown("Analyze YouTube comments across English, Roman Urdu, and mixed languages in real time.")

video_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
api_key = st.text_input("YouTube Data API Key", type="password", placeholder="Enter your YouTube Data API key")

if st.button("Analyze Vibe"):
    if not video_url or not api_key:
        st.warning("Please provide both a video URL and your YouTube API key.")
    else:
        with st.spinner("Fetching comments and analyzing sentiments..."):
            comments, error = fetch_youtube_comments(video_url, api_key)
            
            if error:
                st.error(f"Error fetching comments: {error}")
            elif not comments:
                st.info("No comments found for this video.")
            else:
                results = sentiment_analyzer(comments)
                
                df = pd.DataFrame({
                    "Comment": comments,
                    "Sentiment": [r['label'] for r in results],
                    "Confidence": [r['score'] for r in results]
                })
                
                st.subheader("📊 Vibe Breakdown")
                sentiment_counts = df['Sentiment'].value_counts().reset_index()
                sentiment_counts.columns = ['Sentiment', 'Count']
                
                fig = px.pie(sentiment_counts, names='Sentiment', values='Count', hole=0.4,
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("💬 Sample Comments Analyzed")
                st.dataframe(df[['Comment', 'Sentiment']], use_container_width=True)