import streamlit as st

file = open("test.md", "r")

st.write(file.read())

file.close()