"""AI Quiz Generator + exam-like quiz experience."""

from __future__ import annotations

import copy

import streamlit as st

from ai_engine import (
    evaluate_assessment,
    explain_answer,
    generate_learning_path,
    generate_mcqs,
    update_profile_from_result,
)
from demo_data import COMPETENCIES, LEARNING_MATERIALS
from ui_helpers import alert_box, page_header, section_title


def _ensure_quiz_defaults() -> None:
    if "generated_quiz" not in st.session_state:
        st.session_state.generated_quiz = []
    if "quiz_meta" not in st.session_state:
        st.session_state.quiz_meta = {}
    if "quiz_mode" not in st.session_state:
        st.session_state.quiz_mode = "builder"  # builder | exam | results


def render_builder() -> None:
    section_title("Generate Quiz")
    sources = ["Custom topic"] + [m["title"] for m in LEARNING_MATERIALS]
    source = st.selectbox("Source material", sources)
    topic = st.text_input(
        "Topic",
        value=st.session_state.quiz_meta.get("topic", "Stratified Sampling"),
    )
    competency = st.selectbox(
        "Target competency",
        COMPETENCIES,
        index=COMPETENCIES.index(
            st.session_state.quiz_meta.get("competency", "Sampling Techniques")
        ),
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        n = st.number_input("Number of questions", 3, 15, 8)
    with c2:
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    with c3:
        qtype = st.selectbox("Question type", ["MCQ", "True/False", "Scenario Based"])

    if st.button("Generate Quiz", type="primary"):
        material = ""
        if source != "Custom topic":
            material = next(
                (m["summary"] + " " + ", ".join(m["topics"]) for m in LEARNING_MATERIALS if m["title"] == source),
                "",
            )
        with st.spinner("Generating high-quality questions…"):
            questions = generate_mcqs(
                topic=topic,
                n=int(n),
                difficulty=difficulty,
                question_type=qtype,
                competency=competency,
                source_material=material,
            )
        st.session_state.generated_quiz = questions
        st.session_state.quiz_meta = {
            "topic": topic,
            "competency": competency,
            "difficulty": difficulty,
            "source": source,
            "type": qtype,
        }
        st.session_state.quiz_mode = "builder"
        st.rerun()

    questions = st.session_state.generated_quiz
    if not questions:
        st.info("Configure inputs and click **Generate Quiz**.")
        return

    section_title(f"Quiz Draft ({len(questions)} questions)")
    meta = st.session_state.quiz_meta
    st.caption(
        f"Topic: {meta.get('topic')} · Competency: {meta.get('competency')} · "
        f"Difficulty: {meta.get('difficulty')} · Source: {meta.get('source', '—')}"
    )

    for i, q in enumerate(list(questions)):
        with st.expander(f"Q{i + 1}. {q['question'][:90]}…", expanded=i == 0):
            st.markdown(f"**Question**\n\n{q['question']}")
            for j, opt in enumerate(q["options"]):
                mark = "✓ " if j == q["correct"] else ""
                st.write(f"{mark}{chr(65 + j)}. {opt}")
            st.markdown(f"**Correct Answer:** {chr(65 + q['correct'])}")
            st.markdown(f"**Explanation:** {q['explanation']}")
            st.markdown(f"**Competency:** {q['competency']}  |  **Difficulty:** {q['difficulty']}")

            e1, e2, e3, e4 = st.columns(4)
            with e1:
                if st.button("Edit", key=f"edit_{i}"):
                    st.session_state.editing_q = i
            with e2:
                if st.button("Regenerate", key=f"regen_{i}"):
                    new_q = generate_mcqs(
                        topic=meta.get("topic", topic),
                        n=1,
                        difficulty=meta.get("difficulty", difficulty),
                        question_type=meta.get("type", qtype),
                        competency=q.get("competency", competency),
                    )[0]
                    st.session_state.generated_quiz[i] = new_q
                    st.rerun()
            with e3:
                if st.button("Delete", key=f"del_{i}"):
                    st.session_state.generated_quiz.pop(i)
                    st.rerun()
            with e4:
                st.write("")

            if st.session_state.get("editing_q") == i:
                nq = st.text_area("Edit question", q["question"], key=f"eq_{i}")
                opts = [
                    st.text_input(f"Option {chr(65 + j)}", q["options"][j], key=f"eo_{i}_{j}")
                    for j in range(4)
                ]
                correct = st.selectbox(
                    "Correct option",
                    [0, 1, 2, 3],
                    index=q["correct"],
                    format_func=lambda x: chr(65 + x),
                    key=f"ec_{i}",
                )
                expl = st.text_area("Explanation", q["explanation"], key=f"ee_{i}")
                if st.button("Save edits", key=f"save_{i}"):
                    st.session_state.generated_quiz[i] = {
                        **q,
                        "question": nq,
                        "options": opts,
                        "correct": correct,
                        "explanation": expl,
                    }
                    st.session_state.editing_q = None
                    st.rerun()

    a1, a2, a3 = st.columns(3)
    with a1:
        if st.button("Add Question", use_container_width=True):
            new_q = generate_mcqs(
                topic=meta.get("topic", "Sampling"),
                n=1,
                difficulty=meta.get("difficulty", "Medium"),
                competency=meta.get("competency", "Sampling Techniques"),
            )[0]
            st.session_state.generated_quiz.append(new_q)
            st.rerun()
    with a2:
        if st.button("Regenerate All", use_container_width=True):
            st.session_state.generated_quiz = generate_mcqs(
                topic=meta.get("topic", topic),
                n=len(questions),
                difficulty=meta.get("difficulty", difficulty),
                question_type=meta.get("type", qtype),
                competency=meta.get("competency", competency),
            )
            st.rerun()
    with a3:
        if st.button("Publish / Start Quiz", type="primary", use_container_width=True):
            st.session_state.active_quiz = copy.deepcopy(st.session_state.generated_quiz)
            st.session_state.quiz_answers = {}
            st.session_state.quiz_index = 0
            st.session_state.quiz_mode = "exam"
            st.session_state.last_quiz_result = None
            st.rerun()


def render_exam() -> None:
    questions = st.session_state.active_quiz or []
    if not questions:
        st.session_state.quiz_mode = "builder"
        st.rerun()

    idx = st.session_state.quiz_index
    total = len(questions)
    q = questions[idx]

    section_title("Quiz Experience")
    st.markdown(f"**Question {idx + 1} of {total}**")
    st.progress((idx + 1) / total)
    st.markdown(f"### {q['question']}")

    labels = [f"{chr(65 + j)}. {opt}" for j, opt in enumerate(q["options"])]
    current = st.session_state.quiz_answers.get(idx)
    choice = st.radio(
        "Select an answer",
        options=list(range(4)),
        format_func=lambda x: labels[x],
        index=current if current is not None else None,
        key=f"exam_q_{idx}",
    )
    st.session_state.quiz_answers[idx] = choice

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("Previous", disabled=idx == 0, use_container_width=True):
            st.session_state.quiz_index = max(0, idx - 1)
            st.rerun()
    with b2:
        if st.button("Next", disabled=idx >= total - 1, use_container_width=True):
            st.session_state.quiz_index = min(total - 1, idx + 1)
            st.rerun()
    with b3:
        if st.button("Submit", type="primary", use_container_width=True):
            answers = [st.session_state.quiz_answers.get(i) for i in range(total)]
            if any(a is None for a in answers):
                st.warning("Please answer all questions before submitting.")
                return
            result = evaluate_assessment(questions, answers)
            primary = st.session_state.quiz_meta.get("competency", "Sampling Techniques")
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
                st.session_state.demo_improved = True
            st.session_state.last_quiz_result = {
                **result,
                "primary": primary,
                "before": before,
                "after": after,
                "questions": questions,
                "answers": answers,
            }
            st.session_state.learning_path = generate_learning_path(st.session_state.profile)
            st.session_state.quiz_mode = "results"
            st.rerun()


def render_results() -> None:
    result = st.session_state.last_quiz_result
    if not result:
        st.session_state.quiz_mode = "builder"
        st.rerun()

    section_title("Assessment Results")
    st.markdown(f"### Score: {result['score']}/{result['total']}")
    m1, m2, m3 = st.columns(3)
    m1.metric("Correct", result["correct"])
    m2.metric("Incorrect", result["incorrect"])
    m3.metric(
        result["primary"],
        f"{result['after']}%",
        delta=f"{result['after'] - result['before']} pts",
    )
    alert_box(
        f"<strong>{result['primary']}</strong><br/>Before: {result['before']}% → After: {result['after']}%",
        kind="success",
    )

    st.markdown("#### Competency-level analysis")
    for comp, pct in result.get("competency_scores", {}).items():
        st.progress(pct / 100, text=f"{comp} — {pct}%")

    st.markdown("#### What You Should Improve")
    for g in result.get("knowledge_gaps") or ["Continue advanced practice"]:
        st.write(f"• {g}")

    with st.expander("Review explanations"):
        for i, q in enumerate(result.get("questions") or []):
            ans = result["answers"][i]
            st.markdown(f"**Q{i + 1}.** {q['question']}")
            st.write(explain_answer(q, ans))
            st.divider()

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Generate Learning Path", type="primary", use_container_width=True):
            st.session_state.nav_goto = "🗺️ My Learning Path"
            st.rerun()
    with c2:
        if st.button("Back to Dashboard", use_container_width=True):
            st.session_state.nav_goto = "🏠 Dashboard"
            st.rerun()
    with c3:
        if st.button("Edit Quiz", use_container_width=True):
            st.session_state.quiz_mode = "builder"
            st.rerun()


def render() -> None:
    _ensure_quiz_defaults()
    page_header(
        "AI Quiz Generator",
        "Create, refine, and deliver competency-aligned quizzes.",
    )
    mode = st.session_state.quiz_mode
    if mode == "exam":
        render_exam()
    elif mode == "results":
        render_results()
    else:
        render_builder()
