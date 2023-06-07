import streamlit as st
from st_pages import show_pages, Page



def setStPageConfig(pageTitle, pageIcon=":frog:"):
    st.set_page_config(
            page_icon=pageIcon,
            page_title=pageTitle,
            layout="centered",
            #initial_sidebar_state="collapsed"
    )

def sideBarLogic():
    show_pages([
        Page("main.py", "Home Page", ":home:"),
        Page("pages/titanic.py","Kaggle Project: Titanic", ":ship:")
    ])


"""
NOTES:

Emoji codes:
https://share.streamlit.io/streamlit/emoji-shortcodes


"""