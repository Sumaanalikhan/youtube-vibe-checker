Multilingual YouTube Comment Vibe Checker
A real-time Streamlit web app that analyzes public YouTube comment sentiment using Hugging Face transformers, supporting multi-lingual and mixed-script text like English and Roman Urdu.


✨ Features
•	Live Comment Ingestion: Fetches top-level comments via the YouTube Data API v3.

•	Cross-Lingual Sentiment Analysis: Classifies text into Positive, Negative, and Neutral polarities using Hugging Face models.

•	Interactive UI: Enter your YouTube API key and target video URL directly on the frontend interface, and explore results via dynamic Plotly charts.

🚀 How to Run Locally
1. Clone the Repository
Bash
git clone https://github.com/your-username/youtube-vibe-checker.git
cd youtube-vibe-checker
2. Set Up a Virtual Environment
Bash
python -m venv venv
# On Windows PowerShell:
venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Get Your Free YouTube API Key
1.	Go to the Google Cloud Console.

2.	Create a new project (or select an existing one).

3.	Navigate to Enabled APIs & Services and click Enable APIs and Services.

4.	Search for YouTube Data API v3 and click Enable.

5.	Go to the Credentials tab on the left menu, click Create Credentials, and select API Key. Copy your new key for free.

5. Launch the Application
Start the Streamlit server:


Bash
streamlit run app.py
Open the local URL shown in your terminal (usually http://localhost:8501), paste your newly generated YouTube API key and any YouTube video URL right into the front screen, and analyze the vibes!


