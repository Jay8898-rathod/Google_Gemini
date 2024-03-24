from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

# Function to load the gemini model and get response
def get_gemini_response(question):
    model.generate_content(question)
    return response.text

#Stramlit app
st.set_page_config(page_title="Q&A Demo")
st.header("GEMINI LLM APPLICATION")
input = st.text_input("Input :", key="input")
submit = st.button("Ask the question...")

#When submit is pressed
if submit:
    response = get_gemini_response(input)
    st.header("The response is ")
    st.write(response)