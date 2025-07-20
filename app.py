import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import os
import io
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Function to get Gemini response
def get_gemini_response(prompt, image_file, user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Read image bytes
    image_bytes = image_file.getvalue()
    image = Image.open(io.BytesIO(image_bytes))

    full_prompt = f"{prompt}\n\nAdditional instruction: {user_input}"

    try:
        response = model.generate_content(
            [full_prompt, image],
            stream=False
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI setup
st.set_page_config(page_title="Gemini Health App")
st.title("🥗 Gemini Health Calorie Analyzer")

# User inputs
input_text = st.text_input("Add any additional instruction (optional):", key="input")
uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

# Display the image
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# Submit button
if st.button("🔍 Analyze Calories"):
    if uploaded_file is not None:
        input_prompt = """
You are a certified nutritionist and food image analysis expert. Analyze the food items in the uploaded image and estimate their calorie content.

Respond in the following format:

1. Food Item - Estimated Calories
2. Food Item - Estimated Calories
...
Total Calories: ___

Be as accurate as possible based on the appearance, color, and shape of food items.
"""
        response = get_gemini_response(input_prompt, uploaded_file, input_text)
        st.subheader("Estimated Calorie Breakdown:")
        st.write(response)
    else:
        st.error("Please upload an image to proceed.")