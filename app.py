import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key not found. Please add GROQ_API_KEY to your .env file.")
else:
    client = Groq(api_key=api_key)

    # Streamlit UI
    st.set_page_config(page_title="Groq Chatbot", layout="centered")
    st.title("🤖 Groq LLM Chatbot")
    st.write("Ask anything to **LLaMA 3.3 70B**")

    # Text input
    user_input = st.text_input("You:", "")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": user_input}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                response = chat_completion.choices[0].message.content
                st.markdown(f"**Groq Bot:** {response}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
