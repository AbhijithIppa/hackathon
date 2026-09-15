# StatGrow AI — POC

AI-powered competency development platform for India’s Official Statistical System.

**Hackathon POC** — Streamlit + Python + session state. No auth, no production database.

## Quick Start

```bash
cd hackathon
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Optional LLM (OpenAI-compatible):

```bash
export OPENAI_API_KEY=your_key_here
# optional:
export OPENAI_MODEL=gpt-4o-mini
```

Without an API key, the app uses realistic mock AI responses so the demo never breaks.

## Demo Flow

1. **Dashboard** — competency radar; priority gap: Sampling Techniques  
2. **Competency Assessment** — generate & take assessment  
3. **Gap → Learning Path / iGOT recommendations**  
4. **AI Knowledge Studio** — upload or use demo material  
5. **AI Quiz Generator** — practice from material  
6. **Complete quiz** — scores update competency profile  
7. **Dashboard** — before/after improvement visible  

## Navigation

- Dashboard  
- Competency Assessment  
- AI Knowledge Studio  
- AI Quiz Generator  
- My Learning Path  
- AI Assistant  
- Competency Intelligence  

## Project Structure

```
app.py           # Entry point & sidebar
ai_engine.py     # Competency AI functions
demo_data.py     # Static/demo datasets
ui_helpers.py    # Theme & shared UI
pages/           # Page modules
```

## Constraints

POC only: no Supabase, auth, REST APIs, microservices, or deployment stack.
