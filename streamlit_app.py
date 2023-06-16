import streamlit as st
from pathlib import Path
from tools import assets
import tools as myTools
from streamlit_extras.switch_page_button import switch_page

myTools.setStPageConfig("SP Resume Website")
myTools.pageData()

# Driver file for the streamlit app. 
# Redirects to the Resume page. 
switch_page('Resume')