import streamlit as st
from pathlib import Path
import tools as myTools
from st_pages import show_pages_from_config, add_page_title, show_pages, Page

myTools.setStPageConfig("SP Resume Website")
myTools.pageData()

currDir = Path(__file__).parent 

resumeDir = currDir / 'assets' / 'SeanPerryResumeDA.pdf'
pfp = currDir / 'assets' / 'pfp.png'
cssMain = currDir / 'styles' / 'main.css'
homePage = currDir / "streamlit_app.py"
titanicPage = currDir / 'pages' / 'titanic.py'


# Read in custom CSS
with open(cssMain, 'r') as cssData:
    st.markdown(f'<style>{cssData.read()}</style>', unsafe_allow_html=True)

