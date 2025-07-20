# 🥗 CaloriGem - AI Calorie Analyzer by Gemini

CaloriGem is a Streamlit web app that uses **Google Gemini 1.5 Flash** to estimate the calorie content of food items from images. Upload a food image and let AI analyze and break down the estimated calories item-wise.

## 🚀 Features

- 📸 Upload food images (JPEG, PNG)
- 🧠 Powered by **Google Gemini** multimodal AI (text + vision)
- 🔍 Estimates calories and lists each item
- 🔒 Secure API key handling via `.env`
- 🌐 Live Streamlit Cloud deployment

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (`google-generativeai`)
- Pillow (PIL)
- `python-dotenv` for secure config

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CaloriGem.git
   cd CaloriGem

2. **Install dependencies**
pip install -r requirements.txt

3. **Add your Gemini API key**
GOOGLE_API_KEY="your-api-key-here"

4. **Run the app**
streamlit run app.py

## Live Demo
👉 Click here to try the app : https://gemini-calorie-analyzer-cvfyv3skrwcdbpphpx6nbv.streamlit.app/

## 🤖 Powered By
Google Gemini 1.5 Flash

Streamlit Cloud

