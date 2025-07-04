#  Geology Assistant

A command-line assistant powered by OpenAI or Gemini, built for geology-related tasks:

-Ask geology questions
-Analyze CSV datasets
-Interpret geology images (Gemini only)

---

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py


## Configure .env

LLM_PROVIDER=gemini          # or "openai"

OPENAI_API_KEY=your_key

GEMINI_API_KEY=your_key


Choose from:

1️ Ask a question

2️ Analyze CSV

3️ Analyze image (Gemini only)
