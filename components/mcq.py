import streamlit as st

def mcq(q, question, options):
    if q not in st.session_state.responses:
        st.session_state.responses[q] = None

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='q-title'>{question}</div>", unsafe_allow_html=True)

    for i, opt in enumerate(options):
        selected = st.session_state.responses[q] == opt
        label = f"✅ {opt}" if selected else opt

        if st.button(label, key=f"{q}_{i}"):
            st.session_state.responses[q] = opt
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
