import streamlit as st
from scoring.compute import compute_scores
from storage.google_sheets import save
from datetime import datetime

def render():
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:
        scores = compute_scores(
            st.session_state.responses,
            st.session_state.locked_lang or "en"
        )

        data = {
            "timestamp": datetime.now().isoformat(),
            **st.session_state.responses,
            **scores
        }

        save(data)
        st.session_state.submitted = True
    else:
        scores = compute_scores(
            st.session_state.responses,
            st.session_state.locked_lang or "en"
        )

    st.success("🎉 Submission Complete!")
    st.balloons()

    for k, v in scores.items():
        st.metric(k.replace("_", " ").title(), v)
