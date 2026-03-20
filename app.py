import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables once at the start
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not set in your .env or environment.")
    st.stop()

# Configure the API once
genai.configure(api_key=api_key)

def get_model():
    """
    Returns a Gemini 1.5 Flash model instance.
    """
    # Use the "latest" alias because not every project has the exact model name available.
    return genai.GenerativeModel("gemini-1.5-flash-latest")

def main() -> None:
    st.set_page_config(page_title="Ether Bot", page_icon="🤖", layout="centered")

    st.title("MAMBO DZEMA")
    st.caption("yakagadzirwa namambo dzema")

    # Persistent chat history in the session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show conversation history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("bvunza mambo dzema"):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        try:
            # Try multiple model aliases for better compatibility across projects/keys.
            model_names = [
                "gemini-1.5-flash-latest",
                "gemini-1.5-flash",
                "gemini-flash-latest",
            ]

            response = None
            last_error = None
            for name in model_names:
                try:
                    model = genai.GenerativeModel(name)
                    response = model.generate_content(prompt)
                    break
                except Exception as e:
                    last_error = e

            if response is None:
                raise last_error or RuntimeError("Model call failed without an error message.")

            if response.parts:
                answer = response.text
            else:
                answer = "The model didn't return a text response (it might have been flagged by safety filters)."
                
        except Exception as e:
            answer = f"Error while calling Gemini API: {e}"

        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)

if __name__ == "__main__":
    main()

