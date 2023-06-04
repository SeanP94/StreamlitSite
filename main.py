import streamlit as st

file = open("test.md", "r")

st.markdown(file.read())

file.close()
