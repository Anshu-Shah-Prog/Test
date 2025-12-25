import streamlit as st
from scoring.compute import compute_scores
from storage.google_sheets import save
from datetime import datetime

def render():
    scores = compute_scores(st.session_state.responses)

    data = {
        "timestamp": datetime.now().isoformat(),
        **st.session_state.responses,
        **scores
    }

    save(data)

    st.success("🎉 Submission Complete!")
    st.balloons()

    for k, v in scores.items():
        st.metric(k.replace("_"," ").title(), v)
