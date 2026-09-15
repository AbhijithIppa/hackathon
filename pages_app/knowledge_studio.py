"""AI Knowledge Studio — document → competencies → questions."""

from __future__ import annotations

import streamlit as st

from ai_engine import analyze_learning_material, demo_material_text, extract_text_from_upload
from demo_data import LEARNING_MATERIALS
from ui_helpers import page_header, process_flow, section_title


def render() -> None:
    page_header(
        "AI Knowledge Studio",
        "Turn learning material into topics, competencies, and assessment questions.",
    )

    process_flow(
        [
            "Document",
            "Text Extraction",
            "Topic Identification",
            "Competency Mapping",
            "Question Generation",
            "Learning Recommendations",
        ]
    )

    st.markdown("#### Upload learning material")
    uploaded = st.file_uploader(
        "PDF, DOCX, PPTX, or TXT",
        type=["pdf", "docx", "pptx", "txt"],
    )

    st.markdown("#### Or use demo material")
    demo_titles = {m["title"]: m for m in LEARNING_MATERIALS}
    demo_choice = st.selectbox("Example learning materials", list(demo_titles.keys()))

    col_a, col_b = st.columns(2)
    with col_a:
        run_upload = st.button("Process Uploaded Document", type="primary", disabled=uploaded is None)
    with col_b:
        run_demo = st.button("Process Demo Material")

    if run_upload and uploaded is not None:
        with st.spinner("Extracting and analysing document…"):
            text = extract_text_from_upload(uploaded.name, uploaded.getvalue())
            result = analyze_learning_material(text, filename=uploaded.name)
        st.session_state.knowledge_result = result
        st.session_state.generated_quiz = result["questions"]
        st.session_state.quiz_meta = {
            "topic": result["topics"][0] if result["topics"] else "Official Statistics",
            "competency": result["competencies"][0] if result["competencies"] else "Sampling Techniques",
            "difficulty": "Medium",
            "source": result["document"],
        }
        st.rerun()

    if run_demo:
        material = demo_titles[demo_choice]
        with st.spinner("Running AI knowledge pipeline…"):
            text = demo_material_text(material["id"])
            result = analyze_learning_material(text, filename=f"{material['title']}.pdf")
        st.session_state.knowledge_result = result
        st.session_state.generated_quiz = result["questions"]
        st.session_state.quiz_meta = {
            "topic": result["topics"][0] if result["topics"] else material["topics"][0],
            "competency": result["competencies"][0],
            "difficulty": "Medium",
            "source": result["document"],
        }
        st.rerun()

    result = st.session_state.get("knowledge_result")
    if not result:
        st.info("Upload a file or process demo material to see Document Analysis.")
        return

    section_title("Document Analysis")
    st.markdown(f"**Document:** {result['document']}")
    st.write(result.get("summary", ""))

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Detected Topics**")
        for t in result["topics"]:
            st.write(f"• {t}")
    with c2:
        st.markdown("**Mapped Competencies**")
        for c in result["competencies"]:
            st.write(f"• {c}")
    with c3:
        st.markdown("**Metadata**")
        st.write(f"Difficulty: **{result['difficulty']}**")
        st.write(f"Generated Questions: **{result['question_count']}**")

    st.markdown("**Learning Recommendations**")
    for r in result["recommendations"]:
        st.write(f"• {r}")

    if st.button("Open questions in AI Quiz Generator"):
        st.session_state.nav_goto = "🧠 AI Quiz Generator"
        st.rerun()
