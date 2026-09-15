"""AI Learning Assistant chatbot."""

from __future__ import annotations

import streamlit as st

from ai_engine import analyze_competency_gap, assistant_reply
from ui_helpers import page_header


def render() -> None:
    page_header(
        "StatGrow AI Assistant",
        "Explain concepts, gaps, incorrect answers, and generate practice prompts.",
    )

    if not st.session_state.assistant_messages:
        st.session_state.assistant_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello — I’m the StatGrow AI Assistant. Ask me to explain stratified sampling, "
                    "create practice MCQs, or interpret your competency gaps."
                ),
            }
        ]

    suggestions = [
        "Explain stratified sampling simply",
        "Give me an example",
        "Test my knowledge",
        "Create 5 MCQs",
        "Why did I get this question wrong?",
        "Explain my competency gap",
    ]
    st.markdown("**Suggested prompts**")
    cols = st.columns(3)
    for i, s in enumerate(suggestions):
        if cols[i % 3].button(s, key=f"sug_{i}"):
            st.session_state.assistant_pending = s

    for msg in st.session_state.assistant_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask StatGrow AI…")
    pending = st.session_state.pop("assistant_pending", None)
    user_text = prompt or pending
    if user_text:
        st.session_state.assistant_messages.append({"role": "user", "content": user_text})
        gap = analyze_competency_gap(st.session_state.profile)["priority"]
        reply = assistant_reply(
            user_text,
            context={
                "profile": st.session_state.profile,
                "priority_gap": gap,
                "last_assessment": st.session_state.get("last_assessment"),
            },
        )
        st.session_state.assistant_messages.append({"role": "assistant", "content": reply})
        st.rerun()
