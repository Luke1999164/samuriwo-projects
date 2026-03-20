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

    # Ask the user for a question
    user_question = input("Ask Ether Bot a question: ")
    if not user_question.strip():
        print("You didn't ask a question.")
        return

    # Prefer the "latest" alias for compatibility; keep it within the 1.5-flash family.
    model_names = ["gemini-1.5-flash-latest", "gemini-1.5-flash", "gemini-flash-latest"]
    response = None
    last_error = None
    for name in model_names:
        try:
            model = genai.GenerativeModel(name)
            response = model.generate_content(user_question)
            break
        except Exception as e:
            last_error = e

    if response is None:
        print(f"Error while calling Gemini API: {last_error}")
        return

    # Print Gemini's answer
    print("\nEther bot says:\n")
    print(response.text)


if __name__ == "__main__":
    main()