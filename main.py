import streamlit as st

imgCol, introCol = st.columns([.3,.7])
# Display PFP


imgCol.image("pfp.jpg")
introCol.write("*-Intro-*")
for _ in range(9): introCol.write("")
introCol.write(":::Links to socials:::")
st.divider()

summaryContainer = st.container()
summaryContainer.write("Summarize my interests in the field of data")
summaryContainer.code("print('hello world')", language="python")

st.divider()
siteExplanation  = st.container()
siteExplanation.write("Explain usage of website and such.")



######## SideBar ########
st.sidebar.button("Big Button :o")