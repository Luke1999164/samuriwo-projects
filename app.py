import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


def get_model():
    """
    Configure and return a Gemini GenerativeModel using the GEMINI_API_KEY.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in your .env or environment.")

    genai.configure(api_key=api_key)
    # You can change the model name if needed
    return genai.GenerativeModel("gemini-2.0-flash")


def main() -> None:
    st.set_page_config(page_title="Ether Bot", page_icon="🤖", layout="centered")

    st.title("Ether Bot")
    st.caption("Powered by Gemini")

    # Persistent chat history in the session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show conversation history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask Ether Bot a question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            model = get_model()
            response = model.generate_content(prompt)
            answer = response.text or "(No response text returned.)"
        except Exception as e:
            answer = f"Error while calling Gemini API: {e}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)


if __name__ == "__main__":
    main()

