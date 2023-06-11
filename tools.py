import streamlit as st
from st_pages import show_pages, Page, show_pages_from_config
from pathlib import Path


currDir = Path(__file__).parent 
homePage = currDir / "streamlit_app.py"
titanicPage = currDir / 'pages' / 'titanic.py'




def setStPageConfig(pageTitle, pageIcon=":frog:"):
    st.set_page_config(
            page_icon=pageIcon,
            page_title=pageTitle,
            layout="centered",
            #initial_sidebar_state="collapsed"
    )



"""

def sideBarPages():
    homePage = currDir / "streamlit_app.py"
    titanicPage = currDir / 'pages' / 'titanic.py'

    



NOTES:

Emoji codes:
https://share.streamlit.io/streamlit/emoji-shortcodes


"""