import streamlit as st
from st_pages import add_page_title, Page
import tools as myTools


myTools.setStPageConfig("Kaggle:Titanic", pageIcon=":ship:")


st.sidebar.title("Kaggle Data Project")
st.sidebar.divider()
st.sidebar.markdown("""
The infamous Titanic ML project!  

As I've been learning Machine Learning through Datacamp, I wanted to start utilizing some of the skills I've developed on a simple kaggle project.
So I did a walkthrough for the Titanic project. Here I will elaborate on the choices that were made and the outcomes we found. I plan on adding more, better projects
in the near future but for now, here you go!


""")