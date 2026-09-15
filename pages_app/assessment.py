"""Competency Assessment page."""

from __future__ import annotations

import streamlit as st

from ai_engine import (
    evaluate_assessment,
    generate_assessment,
    generate_learning_path,
    update_profile_from_result,
)
from demo_data import COMPETENCIES
from ui_helpers import alert_box, page_header, section_title


def render() -> None:
    page_header(
        "Competency Assessment",
        "Generate an AI assessment aligned to India’s Official Statistical System.",
    )

    competency = st.selectbox("Select a competency", COMPETENCIES, index=COMPETENCIES.index("Sampling Techniques"))
    n_q = st.slider("Number of questions", 5, 10, 8)

    if st.button("Generate Assessment", type="primary"):
        with st.spinner("Generating assessment…"):
            questions = generate_assessment(competency, n=n_q)
        st.session_state.assessment_questions = questions
        st.session_state.assessment_competency = competency
        st.session_state.assessment_answers = [None] * len(questions)
        st.session_state.assessment_result = None
        st.rerun()

    questions = st.session_state.get("assessment_questions")
    if not questions:
        st.info("Select a competency and click **Generate Assessment** to begin.")
        return

    section_title(f"Assessment: {st.session_state.get('assessment_competency', competency)}")
    answers = st.session_state.get("assessment_answers", [None] * len(questions))

    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['question']}**")
        labels = [f"{chr(65 + j)}. {opt}" for j, opt in enumerate(q["options"])]
        choice = st.radio(
            f"q_{i}",
            options=list(range(4)),
            format_func=lambda x, labels=labels: labels[x],
            index=answers[i] if answers[i] is not None else None,
            key=f"assess_radio_{i}",
            label_visibility="collapsed",
        )
        answers[i] = choice
        st.divider()

    st.session_state.assessment_answers = answers

    if st.button("Submit Assessment", type="primary"):
        if any(a is None for a in answers):
            st.warning("Please answer all questions before submitting.")
            return
        result = evaluate_assessment(questions, answers)
        primary = st.session_state.get("assessment_competency", competency)
        before = st.session_state.profile.get(primary, 0)
        st.session_state.profile_history.append(dict(st.session_state.profile))
        st.session_state.profile = update_profile_from_result(
            st.session_state.profile, result, primary_competency=primary
        )
        after = st.session_state.profile.get(primary, 0)
        st.session_state.assessments_completed += 1
        if after > before:
            st.session_state.skills_improved += 1
            st.session_state.learning_progress = min(
                99, st.session_state.learning_progress + max(2, (after - before) // 3)
            )
        st.session_state.assessment_result = {
            **result,
            "primary": primary,
            "before": before,
            "after": after,
        }
        st.session_state.last_assessment = st.session_state.assessment_result
        st.session_state.learning_path = generate_learning_path(st.session_state.profile)
        st.rerun()

    result = st.session_state.get("assessment_result")
    if result:
        section_title("Assessment Results")
        m1, m2, m3 = st.columns(3)
        m1.metric("Score", f"{result['score']}/{result['total']}")
        m2.metric("Percent", f"{result['score_pct']}%")
        m3.metric(
            result["primary"],
            f"{result['after']}%",
            delta=f"{result['after'] - result['before']} pts",
        )
        alert_box(
            f"Competency updated: <strong>{result['primary']}</strong> "
            f"{result['before']}% → {result['after']}%",
            kind="success",
        )
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Strengths**")
            for s in result["strengths"]:
                st.write(f"• {s}")
            st.markdown("**Correct answers**")
            st.write(result["correct"])
        with c2:
            st.markdown("**Weak areas**")
            for w in result["weak_areas"] or ["None — strong performance"]:
                st.write(f"• {w}")
            st.markdown("**Knowledge gaps**")
            for g in result["knowledge_gaps"]:
                st.write(f"• {g}")
        st.markdown("**Recommended learning topics**")
        for t in result["recommended_topics"]:
            st.write(f"• {t}")

        b1, b2 = st.columns(2)
        with b1:
            if st.button("Generate Learning Path", use_container_width=True):
                st.session_state.nav_goto = "🗺️ My Learning Path"
                st.rerun()
        with b2:
            if st.button("Back to Dashboard", use_container_width=True):
                st.session_state.nav_goto = "🏠 Dashboard"
                st.rerun()
