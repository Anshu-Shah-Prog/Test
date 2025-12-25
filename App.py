import streamlit as st
from config.styles import load_styles
from utils.session import init_session
from pages import intro, section_a, section_b, section_c, section_d, section_e, section_f, final

st.set_page_config(layout="centered")
load_styles()
init_session()

page = st.session_state.page

if page == 1:
    intro.render()
elif page == 2:
    section_a.render(...)
elif page == 3:
    section_b.render(...)
elif page == 4:
    section_c.render(...)
elif page == 5:
    section_d.render(...)
elif page == 6:
    section_e.render(...)
elif page == 7:
    section_f.render(...)
elif page == 8:
    final.render()
