import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    /* MOBILE FIRST */
    html, body, [class*="css"] {
        font-size: 16px;
    }

    /* APP BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: #f1f5f9;
    }

    /* CARD */
    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    /* QUESTION TEXT */
    .q-title {
        font-size: 17px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    /* BUTTONS */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
    }

    /* LIKERT CARD */
    .likert-card {
        background: #ffffff;
        padding: 16px;
        border-radius: 16px;
        border-left: 6px solid #22c55e;
        margin-bottom: 20px;
    }

    /* NAV BAR */
    .nav {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: white;
        padding: 12px;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.12);
        z-index: 999;
    }

    /* SPACING FOR NAV */
    .nav-space {
        height: 90px;
    }
    </style>
    """, unsafe_allow_html=True)
