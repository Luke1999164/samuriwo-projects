import os
from dotenv import load_dotenv
from google import genai

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

    # Use Gemini Developer API (API key), not Vertex AI
    client = genai.Client(api_key=api_key)

    # Ask the user for a question
    user_question = input("Ask Ether Bot a question: ")
    if not user_question.strip():
        print("You didn't ask a question.")
        return

    try:
        # Basic text generation
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Update this to the model version you want
            contents=user_question  # Use the user question as content
        )
    except Exception as e:
        print(f"Error while calling Gemini API: {e}")
        return

    # Print Gemini's answer
    print("\nEther bot says:\n")
    print(response.text)

if __name__ == "__main__":
    main()