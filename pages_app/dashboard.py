"""Dashboard — competency profile, gaps, recommendations."""

from __future__ import annotations

import streamlit as st

from ai_engine import (
    analyze_competency_gap,
    generate_course_recommendations,
    generate_learning_path,
    overall_competency,
)
from ui_helpers import alert_box, competency_radar, metric_card, page_header, section_title


def render() -> None:
    page_header(
        "Welcome to StatGrow AI",
        "AI-Powered Competency Development for India’s Official Statistical System",
    )

    profile = st.session_state.profile
    gap = analyze_competency_gap(profile)
    priority = gap["priority"]

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Overall Competency", f"{overall_competency(profile)}%")
    with c2:
        metric_card("Learning Progress", f"{st.session_state.learning_progress}%")
    with c3:
        metric_card("Assessments Completed", str(st.session_state.assessments_completed))
    with c4:
        metric_card("Skills Improved", str(st.session_state.skills_improved))

    section_title("Your Competency Profile")
    left, right = st.columns([1.4, 1])
    with left:
        st.plotly_chart(
            competency_radar(profile, highlight=priority["name"]),
            use_container_width=True,
        )
    with right:
        st.markdown("#### Priority Skill Gap")
        alert_box(
            f"<strong>{priority['name']}</strong> — {priority['score']}%<br/>"
            "Focus learning here to unlock the strongest improvement in your next reassessment."
        )
        if len(st.session_state.profile_history) > 1:
            prev = st.session_state.profile_history[-2]
            cur = profile
            name = priority["name"]
            # Show before/after for the competency that moved most recently if improved
            improved = [
                k
                for k in cur
                if cur.get(k, 0) > prev.get(k, 0)
            ]
            if improved:
                focus = max(improved, key=lambda k: cur[k] - prev.get(k, 0))
                st.markdown("#### Improvement Tracker")
                alert_box(
                    f"<strong>{focus}</strong><br/>"
                    f"Before: {prev.get(focus, 0)}% → After: {cur.get(focus, 0)}%",
                    kind="success",
                )

        st.markdown("#### Quick Actions")
        if st.button("Take Competency Assessment", use_container_width=True):
            st.session_state.nav_goto = "🎯 Competency Assessment"
            st.rerun()
        if st.button("Open Learning Path", use_container_width=True):
            st.session_state.nav_goto = "🗺️ My Learning Path"
            st.rerun()

    section_title("Recommended for You")
    path = generate_learning_path(profile, top_n=3)
    st.session_state.learning_path = path
    cols = st.columns(3)
    for i, item in enumerate(path):
        with cols[i]:
            st.markdown(
                f"""
                <div class="sg-card">
                    <div class="sg-metric-label">Learning Focus</div>
                    <div style="font-family:'IBM Plex Sans',sans-serif;font-size:1.15rem;font-weight:700;color:#0B1F3A;">
                        {item['competency']}
                    </div>
                    <p style="color:#5A6A7A;margin:0.5rem 0 0.25rem 0;">
                        {item['current_level']} → {item['target_level']}
                    </p>
                    <p style="color:#2E7D4F;font-weight:600;margin:0;">Progress: {item['progress']}%</p>
                    <p style="color:#5A6A7A;font-size:0.9rem;margin-top:0.6rem;">
                        {len(item['modules'])} recommended modules
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_title("Mock iGOT Recommendation Engine")
    st.caption("Demo only — recommendation logic is swap-ready for a future iGOT API.")
    recs = generate_course_recommendations(profile, top_n=3)
    for rec in recs:
        with st.expander(f"{rec['title']}  ·  Gap: {rec['competency']} ({rec['gap_score']}%)"):
            st.write(rec["description"])
            st.markdown(f"**Why recommended?** {rec['why']}")
            st.markdown(f"**Provider:** {rec['provider']}  |  **Duration:** {rec['duration']}")
            if st.button("View Course", key=f"igot_{rec['id']}"):
                st.session_state.selected_igot = rec
                st.info(
                    f"**{rec['title']}** (placeholder course detail)\n\n"
                    f"{rec['description']}\n\n"
                    "In production, this would deep-link to iGOT Karmayogi."
                )
