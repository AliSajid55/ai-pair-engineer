## AI Pair Engineer

A Streamlit-based AI engineering assistant that reviews code like a senior developer - detects design flaws, 
assigns severity, suggests tests, and generates minimal-diff refactor patches with structured JSON output.

## Live Demo

[Launch AI Pair Engineer](https://ai-pair-engineer-oxpcyb8gnmk435dar2h1ej.streamlit.app/) Click and launch the app in your browser...

## Overview

 'AI Pair Engineer' acts as an intelligent pair-programming assistant.

It analyzes source code and returns:

- Structured design flaws (with severity)
- Unit, integration & edge-case tests
- Minimal-diff refactor patch
- Strict JSON schema output (machine-consumable)

Designed for:
- Engineering workflows
- Code quality pipelines
- Developer productivity
- Portfolio demonstration

## Key Features

| Feature                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| Structured JSON Output  | Strict schema ensures predictable responses |
| Severity Classification | `blocker`, `major`, `minor` issue tagging   |
| Minimal-Diff Refactor   | Preserves behavior unless bug detected      |
| Guardrails              | Forces raw JSON (no markdown wrapping)      |
| Copy & Download JSON    | Exportable analysis results                 |
| Retry-Free Gemini Call  | Single-call stable architecture             |
| Streamlit UI            | Clean, professional interface               |

## Architecture

High-Level Flow

```
User Code Input
  |
  v
build_user_prompt()
  |
  v
LLM API
  |
  v
chat_json()
  |
  v
JSON Parsing & Validation
  |
  v
Structured UI Rendering
  |- Summary
  |- Design Flaws
  |- Tests
  |- Refactor Patch
  |- Raw JSON (Copy + Download)
```
## 📁 Project Structure
```
ai-pair-engineer/
│
├── app.py                # Streamlit UI layer
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── .gitignore            # Excludes secrets (.env)
├── .env.example          # Environment variable template
│
└── src/
    ├── llm.py            # Gemini API wrapper
    ├── reviewer.py       # JSON parsing + review orchestration
    └── prompts.py        # System + user prompt templates
```
Core Components

## app.py
- UI layout
- Code input handling
- Displays structured output
- JSON copy + download support

## src/llm.py
- Loads environment variables
- Calls Gemini model
- Handles rate-limit behavior
- Returns raw JSON text

## src/reviewer.py
- Builds prompt
- Calls LLM
- Cleans markdown fences
- Parses JSON safely
- Fallback handling for invalid output

## src/prompts.py

Defines:
```
{
  "summary": "...",
  "design_flaws": [],
  "tests": [],
  "refactor": {
    "goals": [],
    "patch": "..."
  }
}
```
Includes strict instruction:

"Do not wrap JSON in markdown. Return raw JSON only."

## Installation

Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/ai-pair-engineer.git
cd ai-pair-engineer
```
## Create virtual environment

```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

## Install dependencies

```
pip install -r requirements.txt
```

## Configure Environment Variables

Create .env:

```
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-1.5-flash
```
".env is excluded via .gitignore."

## Run the app

```
streamlit run app.py
```
## Deployment (Streamlit Cloud)

- Push repo to GitHub
- Go to Streamlit Community Cloud
- Connect repository
- Add secrets:
```
GEMINI_API_KEY = your_key
GEMINI_MODEL = gemini-1.5-flash
```
- deploy

## Security Practices

- API keys stored in .env
- .env excluded from version control
- No hardcoded secrets
- Model guardrails enforce structured output

## Example Output Schema

```
{
  "summary": "Short overview",
  "design_flaws": [
    {
      "severity": "major",
      "title": "...",
      "why_it_matters": "...",
      "evidence": "...",
      "fix": "..."
    }
  ],
  "tests": [
    {
      "type": "unit",
      "title": "...",
      "what_to_test": "...",
      "example_test_code": "..."
    }
  ],
  "refactor": {
    "goals": ["..."],
    "patch": "..."
  }
}

```
## Engineering Decisions

```
| Decision                 | Reason                            |
| ------------------------ | --------------------------------- |
| Strict JSON schema       | Enables automation & reliability  |
| Single API call          | Avoid free-tier rate limit issues |
| Markdown stripping       | Prevent JSON parsing failures     |
| Minimal-diff refactor    | Preserve original logic           |
| Explicit severity levels | Professional review standard      |
```
## Known Limitations

- Free-tier Gemini quota may cause rate limits
- Large code inputs may hit token constraints
- No authentication layer (public demo app)

## Future Improvements

- Multi-file project analysis
- Diff-based patch viewer
- GitHub PR integration
- Static analysis hybrid mode
- CI/CD pipeline support
- Docker containerization

## Ideal Use Cases

- Developer portfolio demonstration
- Code quality experimentation
- AI-assisted refactoring
- Engineering workflow automation

## Branding Positioning

AI Pair Engineer is positioned not as a “code reviewer,”
But as an intelligent engineering partner.

## License

MIT License (or your chosen license)

## Author

#### Ali Sajid
AI Engineer | Computer Vision | Machine Learning | Generative AI



