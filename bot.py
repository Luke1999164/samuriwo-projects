import os

from dotenv import load_dotenv
import google.generativeai as genai


def main() -> None:
    """
    Simple CLI chatbot using the Gemini API.
    """
    # Load environment variables from .env
    load_dotenv()

    # Set up the API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not set in your environment or .env file.")
        return

    # Configure the Gemini client (google-generativeai library)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Ask the user for a question
    user_question = input("Ask Ether Bot a question: ")
    if not user_question.strip():
        print("You didn't ask a question.")
        return

    try:
        # Basic text generation
        response = model.generate_content(user_question)
    except Exception as e:
        print(f"Error while calling Gemini API: {e}")
        return

    # Print Gemini's answer
    print("\nEther bot says:\n")
    print(response.text)


if __name__ == "__main__":
    main()