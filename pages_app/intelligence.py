"""Competency Intelligence — organisation-level demo analytics."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from demo_data import ORG_ANALYTICS_ROWS
from ui_helpers import NAVY_MID, GREEN, alert_box, page_header, section_title


def render() -> None:
    page_header(
        "Competency Intelligence",
        "Organisation-level analytics using demo data for India’s Official Statistical System.",
    )

    df = pd.DataFrame(ORG_ANALYTICS_ROWS)

    f1, f2, f3, f4 = st.columns(4)
    with f1:
        dept = st.multiselect("Department", sorted(df["department"].unique()), default=[])
    with f2:
        desig = st.multiselect("Designation", sorted(df["designation"].unique()), default=[])
    with f3:
        comp = st.multiselect("Competency", sorted(df["competency"].unique()), default=[])
    with f4:
        exp = st.slider("Max experience (years)", 1, 20, 20)

    filtered = df[df["experience_years"] <= exp]
    if dept:
        filtered = filtered[filtered["department"].isin(dept)]
    if desig:
        filtered = filtered[filtered["designation"].isin(desig)]
    if comp:
        filtered = filtered[filtered["competency"].isin(comp)]

    # Top gaps = lowest average scores
    gap_tbl = (
        filtered.groupby("competency", as_index=False)["score"]
        .mean()
        .sort_values("score")
        .head(4)
    )
    section_title("Top Competency Gaps")
    for i, row in enumerate(gap_tbl.itertuples(), start=1):
        st.write(f"{i}. **{row.competency}** — {row.score:.0f}%")

    alert_box(
        "<strong>AI Insight</strong><br/>"
        "Sampling methodology is the largest competency gap across the organisation. "
        "Employees with less than 3 years of experience show the highest training need."
    )

    c1, c2 = st.columns(2)
    with c1:
        section_title("Competency distribution")
        dist = filtered.groupby("competency", as_index=False)["score"].mean().sort_values("score")
        fig = px.bar(
            dist,
            x="score",
            y="competency",
            orientation="h",
            color_discrete_sequence=[NAVY_MID],
        )
        fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=360, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        section_title("Department-wise competency")
        dept_avg = filtered.groupby("department", as_index=False)["score"].mean()
        fig2 = px.bar(
            dept_avg,
            x="department",
            y="score",
            color_discrete_sequence=[GREEN],
        )
        fig2.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=360, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        section_title("Learning progress")
        fig3 = px.box(
            filtered,
            x="department",
            y="learning_progress",
            color_discrete_sequence=[NAVY_MID],
        )
        fig3.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=360, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        section_title("Quiz performance")
        fig4 = px.scatter(
            filtered,
            x="quizzes_taken",
            y="score",
            color="department",
            size="learning_progress",
            hover_data=["competency", "designation"],
        )
        fig4.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=360, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig4, use_container_width=True)

    section_title("Most common competency gaps")
    fig5 = px.pie(
        gap_tbl,
        names="competency",
        values=100 - gap_tbl["score"],
        color_discrete_sequence=[NAVY_MID, GREEN, "#4A6FA5", "#7FA68A"],
    )
    fig5.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=380, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("View filtered demo data"):
        st.dataframe(filtered, use_container_width=True)
