import streamlit as st

# Main page configuration.
st.set_page_config(
    page_icon=":octopus:",
    page_title="SP Portfolio Site",
    layout="centered",
    initial_sidebar_state="collapsed"
)

imgCol, _, introCol = st.columns([.4, .02,.58])
# Display PFP

# Header code
imgCol.image("pfp.jpg")
introCol.write("""
# Sean Perry  
Pricing Analyst  
Aspiring Data Scientist
""")
# Make this a download button later.
introCol.button(":page_with_curl: Download Resume")
introCol.write(":email: seanep94@gmail.com")



# Using shields.io for the buttons.
introCol.write('''
<p align="left">
    <a href="https://www.linkedin.com/in/seanp1994/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin" alt="Linkedin">
    </a>
    <a href="https://leetcode.com/sperry1994/">
        <img src="https://img.shields.io/badge/LeetCode-blue?style=flat&logo=leetcode" alt="Linkedin">
    </a>
</p>
''', unsafe_allow_html=True)

# Set as download button later.

st.divider()

# Summary code
summaryContainer = st.container()
summaryContainer.header("Introduction")
summaryContainer.write("Summarize my interests in the field of data")


# Website code
st.divider()
siteExplanation  = st.container()
siteExplanation.header("Why I Made This Website")
siteExplanation.write("Explain usage of website and such.")


######## SideBar ########
st.sidebar.button("Big Button :o")