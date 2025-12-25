import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

def save(data):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes
    )

    sheet = gspread.authorize(creds).open("Database").worksheet("Sheet1")

    if not sheet.get_all_values():
        sheet.append_row(list(data.keys()))

    sheet.append_row(list(data.values()))
