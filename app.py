"""StatGrow AI — Streamlit POC entry point."""

from __future__ import annotations

import streamlit as st

from pages_app import (
    assessment,
    assistant,
    dashboard,
    intelligence,
    knowledge_studio,
    learning_path,
    quiz_generator,
)
from ui_helpers import init_session_state, inject_styles

st.set_page_config(
    page_title="StatGrow AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_styles()
init_session_state()

NAV_ITEMS = [
    "🏠 Dashboard",
    "🎯 Competency Assessment",
    "📚 AI Knowledge Studio",
    "🧠 AI Quiz Generator",
    "🗺️ My Learning Path",
    "💬 AI Assistant",
    "📊 Competency Intelligence",
]

with st.sidebar:
    st.markdown("### StatGrow AI")
    st.caption("Competency Development POC")
    st.markdown("---")

    # Allow pages to request navigation via session_state.nav_goto
    if "nav_goto" in st.session_state and st.session_state.nav_goto in NAV_ITEMS:
        st.session_state.nav_radio = st.session_state.nav_goto
        del st.session_state.nav_goto

    if "nav_radio" not in st.session_state:
        st.session_state.nav_radio = NAV_ITEMS[0]

    choice = st.radio("Navigation", NAV_ITEMS, key="nav_radio")
    st.markdown("---")
    st.caption("Demo profile · session state only")
    if st.button("Reset demo profile"):
        from demo_data import DEFAULT_PROFILE

        st.session_state.profile = dict(DEFAULT_PROFILE)
        st.session_state.profile_history = [dict(DEFAULT_PROFILE)]
        st.session_state.assessments_completed = 3
        st.session_state.skills_improved = 7
        st.session_state.learning_progress = 64
        st.session_state.assessment_result = None
        st.session_state.last_assessment = None
        st.session_state.last_quiz_result = None
        st.session_state.demo_improved = False
        st.success("Profile reset.")
        st.rerun()

ROUTES = {
    "🏠 Dashboard": dashboard.render,
    "🎯 Competency Assessment": assessment.render,
    "📚 AI Knowledge Studio": knowledge_studio.render,
    "🧠 AI Quiz Generator": quiz_generator.render,
    "🗺️ My Learning Path": learning_path.render,
    "💬 AI Assistant": assistant.render,
    "📊 Competency Intelligence": intelligence.render,
}

ROUTES[choice]()
