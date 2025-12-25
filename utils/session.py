import streamlit as st

def init_session():
    defaults = {
        "page": 1,
        "lang_choice": "en",
        "locked_lang": None,
        "responses": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset():
    st.session_state.responses = {}
    st.session_state.page = 1
    st.session_state.locked_lang = None
