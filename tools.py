import streamlit as st
from st_pages import show_pages_from_config
from pathlib import Path


currDir = Path(__file__).parent 


class assets:
    """
    Assets are to get different file locations from the other classes.
    """
    homePage = currDir / 'pages' / 'home.py'
    titanicPage = currDir / 'pages' / 'titanic.py'
    pfp = currDir / 'assets' / 'pfp.png'
    resume = currDir / 'assets' / 'SeanPerryResumeDA.pdf'
    cssFile = currDir / 'styles' / 'main.css'
    titanicTrain = currDir / 'assets' / 'train.csv'


def setStPageConfig(pageTitle, pageIcon=":frog:"):
    """
    Sets the page configuration for each page in uniform, 
    also reads in the css data since it's apart of configuring the page.
    """
    st.set_page_config(
            page_icon=pageIcon,
            page_title=pageTitle,
            layout="centered",
            #initial_sidebar_state="collapsed"
    )
    with open(assets.cssFile, 'r') as cssData:
        st.markdown(f'<style>{cssData.read()}</style>', unsafe_allow_html=True)

def pageData():
    show_pages_from_config()


"""


NOTES:

Emoji codes:
https://share.streamlit.io/streamlit/emoji-shortcodes


"""