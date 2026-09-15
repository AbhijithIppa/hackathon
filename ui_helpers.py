"""Shared UI helpers and theme for StatGrow AI POC."""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

NAVY = "#0B1F3A"
NAVY_MID = "#1B3A5F"
GREEN = "#2E7D4F"
GREEN_SOFT = "#E8F5EE"
LIGHT_BG = "#F5F7FA"
CARD_BORDER = "#E2E8F0"
MUTED = "#5A6A7A"
ACCENT_LINE = "#C5D0DC"


def inject_styles() -> None:
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Sans:wght@500;600;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Source Sans 3', 'Segoe UI', sans-serif;
            color: {NAVY};
        }}
        .stApp {{
            background: linear-gradient(180deg, #FFFFFF 0%, {LIGHT_BG} 100%);
        }}
        section[data-testid="stSidebar"] {{
            background: {NAVY};
            color: #F8FAFC;
        }}
        section[data-testid="stSidebar"] * {{
            color: #E8EEF5 !important;
        }}
        section[data-testid="stSidebar"] .stRadio label {{
            padding: 0.35rem 0.5rem;
            border-radius: 8px;
        }}
        .sg-hero {{
            padding: 1.25rem 1.5rem 0.5rem 0;
        }}
        .sg-hero h1 {{
            font-family: 'IBM Plex Sans', sans-serif;
            font-size: 1.9rem;
            font-weight: 700;
            color: {NAVY};
            margin: 0 0 0.35rem 0;
            letter-spacing: -0.02em;
        }}
        .sg-hero p {{
            color: {MUTED};
            font-size: 1.02rem;
            margin: 0;
        }}
        .sg-card {{
            background: #FFFFFF;
            border: 1px solid {CARD_BORDER};
            border-radius: 14px;
            padding: 1.1rem 1.2rem;
            box-shadow: 0 4px 16px rgba(11, 31, 58, 0.06);
            height: 100%;
        }}
        .sg-metric-label {{
            color: {MUTED};
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }}
        .sg-metric-value {{
            font-family: 'IBM Plex Sans', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            color: {NAVY};
        }}
        .sg-badge {{
            display: inline-block;
            background: {GREEN_SOFT};
            color: {GREEN};
            border: 1px solid #B7DFC8;
            border-radius: 999px;
            padding: 0.2rem 0.7rem;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .sg-alert {{
            background: #FFF8EB;
            border-left: 4px solid #D4A017;
            border-radius: 8px;
            padding: 0.85rem 1rem;
            margin: 0.75rem 0 1rem 0;
        }}
        .sg-success {{
            background: {GREEN_SOFT};
            border-left: 4px solid {GREEN};
            border-radius: 8px;
            padding: 0.85rem 1rem;
            margin: 0.75rem 0 1rem 0;
        }}
        .sg-section-title {{
            font-family: 'IBM Plex Sans', sans-serif;
            font-size: 1.25rem;
            font-weight: 650;
            color: {NAVY};
            margin: 1.25rem 0 0.75rem 0;
        }}
        .sg-flow {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            align-items: center;
            margin: 1rem 0;
        }}
        .sg-flow-step {{
            background: #FFFFFF;
            border: 1px solid {CARD_BORDER};
            border-radius: 10px;
            padding: 0.55rem 0.85rem;
            font-size: 0.88rem;
            font-weight: 600;
            color: {NAVY_MID};
        }}
        .sg-flow-arrow {{
            color: {MUTED};
            font-weight: 700;
        }}
        div[data-testid="stMetric"] {{
            background: #FFFFFF;
            border: 1px solid {CARD_BORDER};
            border-radius: 14px;
            padding: 0.75rem 1rem;
            box-shadow: 0 4px 16px rgba(11, 31, 58, 0.05);
        }}
        .stButton > button {{
            border-radius: 10px;
            font-weight: 600;
            border: 1px solid {NAVY_MID};
            background: {NAVY_MID};
            color: white;
        }}
        .stButton > button:hover {{
            background: {NAVY};
            border-color: {NAVY};
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f'<div class="sg-hero"><h1>{title}</h1>{sub}</div>',
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="sg-card">
            <div class="sg-metric-label">{label}</div>
            <div class="sg-metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_badge(text: str) -> None:
    st.markdown(f'<span class="sg-badge">{text}</span>', unsafe_allow_html=True)


def alert_box(text: str, kind: str = "alert") -> None:
    cls = "sg-success" if kind == "success" else "sg-alert"
    st.markdown(f'<div class="{cls}">{text}</div>', unsafe_allow_html=True)


def section_title(text: str) -> None:
    st.markdown(f'<div class="sg-section-title">{text}</div>', unsafe_allow_html=True)


def process_flow(steps: list[str]) -> None:
    parts = []
    for i, step in enumerate(steps):
        parts.append(f'<span class="sg-flow-step">{step}</span>')
        if i < len(steps) - 1:
            parts.append('<span class="sg-flow-arrow">↓</span>')
    st.markdown(f'<div class="sg-flow">{"".join(parts)}</div>', unsafe_allow_html=True)


def competency_radar(profile: dict[str, int], highlight: str | None = None) -> go.Figure:
    """Radar chart for core demo competencies."""
    # Focus on the six shown in the brief for a clean visual
    keys = [
        "Statistical Methods",
        "Data Analysis",
        "Data Visualization",
        "Sampling Techniques",
        "Data Quality",
        "Data Governance",
    ]
    labels = keys + [keys[0]]
    values = [profile.get(k, 50) for k in keys] + [profile.get(keys[0], 50)]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            fillcolor="rgba(27, 58, 95, 0.25)",
            line=dict(color=NAVY_MID, width=2),
            name="Competency Profile",
        )
    )
    if highlight and highlight in keys:
        hi_vals = [profile.get(k, 0) if k == highlight else 0 for k in keys]
        hi_vals.append(hi_vals[0])
        fig.add_trace(
            go.Scatterpolar(
                r=hi_vals,
                theta=labels,
                fill="toself",
                fillcolor="rgba(46, 125, 79, 0.35)",
                line=dict(color=GREEN, width=2),
                name=f"Gap: {highlight}",
            )
        )
    fig.update_layout(
        polar=dict(
            bgcolor="#FFFFFF",
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10), gridcolor=ACCENT_LINE),
            angularaxis=dict(tickfont=dict(size=11, color=NAVY)),
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2),
        margin=dict(l=60, r=60, t=30, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        height=420,
    )
    return fig


def init_session_state() -> None:
    from demo_data import DEFAULT_PROFILE

    defaults = {
        "profile": dict(DEFAULT_PROFILE),
        "profile_history": [dict(DEFAULT_PROFILE)],
        "assessments_completed": 3,
        "skills_improved": 7,
        "learning_progress": 64,
        "last_assessment": None,
        "last_quiz_result": None,
        "generated_quiz": [],
        "quiz_meta": {},
        "active_quiz": None,
        "quiz_answers": {},
        "quiz_index": 0,
        "learning_path": None,
        "knowledge_result": None,
        "assistant_messages": [],
        "selected_igot": None,
        "demo_improved": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
