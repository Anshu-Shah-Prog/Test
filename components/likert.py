import streamlit as st

EMOJI = {
    1: "😄",
    2: "🙂",
    3: "😐",
    4: "🙁",
    5: "😫"
}

def likert(q, question):
    if q not in st.session_state.responses:
        st.session_state.responses[q] = None

    st.markdown(f"<div class='q-title'>{question}</div>", unsafe_allow_html=True)

    for i in range(1,6):
        selected = st.session_state.responses[q] == str(i)
        label = f"{i} {EMOJI[i]}" if selected else str(i)

        if st.button(label, key=f"{q}_{i}"):
            st.session_state.responses[q] = str(i)
            st.rerun()


def likert_group(qmap, color="#22c55e"):
    st.markdown(
        f"<div class='likert-card' style='border-left-color:{color}'>",
        unsafe_allow_html=True
    )

    for q, text in qmap.items():
        likert(q, text)

    st.markdown("</div>", unsafe_allow_html=True)
