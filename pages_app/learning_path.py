"""My Learning Path + mock iGOT recommendations."""

from __future__ import annotations

import streamlit as st

from ai_engine import (
    analyze_competency_gap,
    generate_course_recommendations,
    generate_learning_path,
)
from ui_helpers import alert_box, page_header, section_title


def render() -> None:
    page_header(
        "My Learning Path",
        "Personalised modules generated from your competency gaps.",
    )

    profile = st.session_state.profile
    if st.button("Refresh AI Learning Path") or not st.session_state.learning_path:
        st.session_state.learning_path = generate_learning_path(profile, top_n=3)

    path = st.session_state.learning_path
    priority = analyze_competency_gap(profile)["priority"]
    alert_box(
        f"Priority gap: <strong>{priority['name']}</strong> at {priority['score']}%. "
        "Complete modules below, then practise with an AI quiz."
    )

    section_title("Your AI-Generated Learning Path")
    for i, item in enumerate(path, start=1):
        st.markdown(
            f"### {i}. {item['competency']}\n"
            f"Current Level: **{item['current_level']}**  ·  "
            f"Target Level: **{item['target_level']}**  ·  "
            f"Progress: **{item['progress']}%**"
        )
        st.progress(item["progress"] / 100)

        for j, mod in enumerate(item["modules"]):
            with st.expander(f"Module: {mod['title']}  ·  {mod['duration']}"):
                st.markdown(f"**Overview**  \n{mod['overview']}")
                st.markdown("**Learning objectives**")
                for obj in mod["objectives"]:
                    st.write(f"• {obj}")
                st.markdown("**Learning resources**")
                for res in mod["resources"]:
                    st.write(f"• {res}")
                st.markdown("**Quiz**  \nShort check available in AI Quiz Generator.")
                done_key = f"mod_done_{item['competency']}_{j}"
                if st.checkbox("Mark module complete", key=done_key):
                    st.session_state.learning_progress = min(
                        99, st.session_state.learning_progress + 1
                    )
                if st.button(
                    "Practice quiz for this competency",
                    key=f"prac_{item['competency']}_{j}",
                ):
                    st.session_state.quiz_meta = {
                        "topic": mod["title"],
                        "competency": item["competency"],
                        "difficulty": "Medium",
                        "source": mod["title"],
                    }
                    st.session_state.nav_goto = "🧠 AI Quiz Generator"
                    st.rerun()
        st.divider()

    section_title("Mock iGOT Recommendation Engine")
    st.caption("Not a live iGOT API — structured for future integration.")
    recs = generate_course_recommendations(profile, top_n=4)
    for rec in recs:
        st.markdown(
            f"""
            <div class="sg-card" style="margin-bottom:0.75rem;">
                <div class="sg-metric-label">Identified Gap</div>
                <div style="font-weight:700;color:#0B1F3A;">{rec['competency']} — {rec['gap_score']}%</div>
                <div class="sg-metric-label" style="margin-top:0.75rem;">Recommended iGOT Learning</div>
                <div style="font-weight:650;">{rec['title']}</div>
                <p style="color:#5A6A7A;margin:0.4rem 0 0 0;">{rec['why']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("View Course", key=f"path_igot_{rec['id']}"):
            st.info(
                f"**{rec['title']}**\n\n{rec['description']}\n\n"
                f"Level: {rec['level']} · Duration: {rec['duration']}\n\n"
                "Placeholder link: https://igotkarmayogi.gov.in/ (mock)"
            )
