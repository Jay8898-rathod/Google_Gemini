from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv["GOOGLE_API_KEY"])

# Function to load the model and get response
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data':bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Please upload the file")

# Streamlit 
st.set_page_config(page_title="Multi language text extractor")
st.header("GOOGLE LLM APP")
input = st.text_input("Input prompt :", key="input")
uploaded_file = st.file_uploader("Choose the file...", type=['png', 'jpg', 'jpeg'])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded file", use_column_width=True)

submit = st.button("Tell me about the invoice")
input_prompt = """
You are an expert in understanding invoices. We will upload the image as invoice and 
you have to give the answer to any question based on the uploaded image.
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The respone is ")
    st.write(response)