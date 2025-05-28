import streamlit as st
import os
from groq import Groq

# Set up Groq API client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Streamlit UI
st.title("Groq LLM Chatbot")
st.write("Ask anything to LLaMA 3.3 70B!")

# Input from user
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
            st.error(f"Error: {e}")
