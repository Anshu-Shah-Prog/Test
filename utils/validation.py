import streamlit as st

def is_complete(keys):
    return all(
        st.session_state.responses.get(k) not in [None, ""]
        for k in keys
    )
