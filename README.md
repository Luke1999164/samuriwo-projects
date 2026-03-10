# Simple Gemini Python Chatbot

This is a minimal command-line chatbot that uses the Gemini API via the `google-generativeai` Python library.

## Setup

1. **Create and activate a virtual environment (optional but recommended)**:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set your Gemini API key**:

Edit the `.env` file and replace `your_api_key_here` with your real Gemini API key:

```text
GEMINI_API_KEY=your_real_api_key
```

## Run the chatbot

From this directory:

```bash
python bot.py
```

You will be prompted to enter a question, and the script will print Gemini's answer.