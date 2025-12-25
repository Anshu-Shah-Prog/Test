import streamlit as st
from components.mcq import mcq
from utils.validation import is_complete

def render(lang, t):
    required = ["A1","A2","A3"]

    for q in required:
        mcq(q, t(lang, f"Q.{q}.q"), t(lang, f"Q.{q}.opts"))

    st.markdown("<div class='nav-space'></div>", unsafe_allow_html=True)

    st.markdown("<div class='nav'>", unsafe_allow_html=True)
    disabled = not is_complete(required)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back"):
            st.session_state.page -= 1
            st.rerun()
    with col2:
        if st.button("Next ➡", disabled=disabled):
            st.session_state.page += 1
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
