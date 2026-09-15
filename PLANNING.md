# StatGrow AI — POC Planning

## Goal

Hackathon POC for **StatGrow AI**: an AI-powered competency development platform for India’s Official Statistical System.

Prove one end-to-end loop:

**Learning material → AI competency extraction → competency assessment → gap detection → personalized learning → AI quiz → reassessment**

## Scope (In)

- Streamlit multi-page POC with polished government/enterprise UI
- In-memory / `st.session_state` persistence for the demo
- Simple Python AI engine functions (LLM if key present, realistic mocks otherwise)
- Dashboard, Assessment, Knowledge Studio, Quiz Generator, Learning Path, AI Assistant, Competency Intelligence
- Mock iGOT Karmayogi recommendations
- Before/after competency improvement tracking

## Scope (Out)

- Authentication, RBAC, user management
- Supabase / PostgreSQL / Firebase / production DBs
- REST APIs, microservices, Celery, Redis
- Docker / Kubernetes / deployment infrastructure
- Real iGOT API integration

## Stack

| Layer | Choice |
|-------|--------|
| UI | Streamlit |
| Data | Pandas + in-memory demo data |
| Charts | Plotly |
| AI | Optional LLM API; mock fallback |
| State | `st.session_state` |

## Architecture

```
User Input → AI Function → Structured Python Result → Streamlit UI → Session State
```

## Module Layout

```
app.py                 # Entry + sidebar navigation
ai_engine.py           # Core AI competency functions
demo_data.py           # Competencies, quizzes, org analytics
ui_helpers.py          # Theme, cards, shared widgets
pages/                 # One module per nav destination
```

## Design Language

- White/light background
- Deep navy primary (`#0B1F3A` / `#1B3A5F`)
- Subtle green accents (`#2E7D4F`)
- Rounded cards, soft shadows, clean spacing
- No neon, gaming, or cartoon aesthetics

## Demo Narrative

1. Dashboard — competency radar + priority gap
2. Assessment — AI questions → score → gaps
3. Recommendations — modules + mock iGOT
4. Learn — Knowledge Studio / Learning Path
5. Practice — AI Quiz
6. Reassess — score improves (e.g. Sampling 38% → 72%)
7. Dashboard updates visibly
