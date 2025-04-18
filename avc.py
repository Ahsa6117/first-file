import streamlit as st
import os
from dotenv import load_dotenv
import requests

# Load .env file to get GEMINI_API_KEY
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY is not set. Please check your .env file.")
    st.stop()

# --- Constants ---
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

# --- Initialize Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# --- Page Config ---
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Panaversity Gemini Chatbot")

# --- Chat Box ---
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gemini-2.0-flash",
        "messages": st.session_state.chat_history,
    }

    with st.spinner("Thinking..."):
        try:
            response = requests.post(BASE_URL, headers=headers, json=payload)
            result = response.json()

            if response.status_code != 200:
                raise Exception(result)

            reply = result["choices"][0]["message"]["content"]

            st.session_state.chat_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error(f"❌ Error: {e}")

# --- Display Chat History ---
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])
