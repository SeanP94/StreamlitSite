import streamlit as st
from st_pages import show_pages, Page
from pathlib import Path


currDir = Path(__file__).parent 

homePage = currDir / "main.py"
titanicPage = currDir / 'pages' / 'titanic.py'

def setStPageConfig(pageTitle, pageIcon=":frog:"):
    st.set_page_config(
            page_icon=pageIcon,
            page_title=pageTitle,
            layout="centered",
            #initial_sidebar_state="collapsed"
    )

def sideBarLogic():
    show_pages([
        Page(homePage, "Home Page"),
        Page(titanicPage,"Kaggle Project: Titanic")
    ])




"""
NOTES:

Emoji codes:
https://share.streamlit.io/streamlit/emoji-shortcodes


"""