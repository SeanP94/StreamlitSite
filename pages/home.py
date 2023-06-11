import streamlit as st
from pathlib import Path
from st_pages import add_page_title, Page, show_pages_from_config
from tools import assets
import tools as myTools


myTools.setStPageConfig("Home Page", pageIcon=":house:")


def getResume():
    with open(str(assets.resume), 'rb') as pdf_file:
        resume = pdf_file.read()
    return resume

# Main page configuration.

imgCol, _, introCol = st.columns([.4, .02,.58])
# Display PFP

# Header code
imgCol.image(str(assets.pfp))
introCol.write("""
# Sean Perry  
Pricing Analyst  
Aspiring Data Scientist
""")
# Make this a download button later.
introCol.download_button(
    label=":page_with_curl: Download Resume",
    data=getResume(),
    file_name="SeanPerryDA_Resume.pdf",
    mime='application/octet-stream'
)
introCol.write(":email: seanep94@gmail.com")



# Using shields.io for the buttons.
introCol.write('''
<p align="left">
    <a href="https://www.linkedin.com/in/seanp1994/">
        <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin" alt="Linkedin">
    </a>
    <a href="https://leetcode.com/sperry1994/">
        <img src="https://img.shields.io/badge/LeetCode-blue?style=flat&logo=leetcode" alt="Leetcode">
    </a>
    <a href="https://github.com/SeanP94">
        <img src="https://img.shields.io/badge/Github-blue?style=flat&logo=github" alt="Github">
    </a>
    <a href="https://www.datacamp.com/profile/Seanp94">
        <img src="https://img.shields.io/badge/DataCamp-blue?style=flat&logo=datacamp" alt="DataCamp">
    </a>
</p>
''', unsafe_allow_html=True)

# Set as download button later.

st.divider()
st.write('''
### Programming Skills
:desktop_computer:Programming: Python, C++, Kotlin, Familiarity with Javascript and C#  
:blue_book: Python Libraries: Scikit-Learn, Pandas, Numpy, and Matplotlib  
:minidisc:Databases: Microsoft SQL Server, MySQL and Firestore

### Experience  
:mortar_board: Obtained my B.S. in Computer Science from California State University San Marcos    
:bar_chart: 1.5 years experience in data analytics.  
:male-teacher: 1 years experience running a team and store operations.  
:open_file_folder: 2 years experience on an engineering team.  
:telephone_receiver: 3 years of customer service experience. 
''')

st.divider()
# Summary code
summaryContainer = st.container()
summaryContainer.header("Introduction")
summaryContainer.write("""
&ensp;&ensp;Hello my name is Sean, and thank you for taking the time to check out my Portfolio Website! I wanted to create a place to help me showcase projects and discuss some achievements to prospective hiring managers.  

&ensp;&ensp;To summarize myself I love data and researching problems that need to be solved. It's what my passion and driving force was for finishing my degree in Computer Science. I'd love to find a position that would allow me to expand and grow my skill set. I'm interested in engineering data pipelines, data cleansing, analyzing information, researching business problems, helping management find problems through data, and most importantly LEARNING MORE SKILLS!


#### Some Career Achievements
- Self taught data analytics skills, to find solutions for business problems.
- Implementing Machine Learning to classify appliance and plumbing product meta data for companies internal use.
- Taking in multiple streams of data, to create reporting that has helped save the company money.
- Through initiative, analyzed information to help leadership find gaps and solve problems.

    """)


# Website code
st.divider()
siteExplanation  = st.container()
siteExplanation.header("What am I working on?")
siteExplanation.write("""
- June 2023:
    - Building this website!
    - Currently I am working on expanding my SQL skills.
    - Expanding my statistics knowledge. 
    - Learning cloud computing concepts to obtain either a certificate for Azure.  

- May 2023:
    - Began work on my PC Price Tracker project. It's on hold for now until I have this site built to a point.   

    - :tada: I Graduated!!! :tada:  
    - This month I was wrapping up my work on my group project SynapFlow, a Kotlin mobile app built to track study time. I also built the interface for the timer, the logic for making the timer work between screens (LiveData), built the code for interfacing with Firestore (A Google NOSQL database) to store the apps information, along with creating a simple data analytics page. Please see my Github page for more information.

""")



######## SideBar ########
st.sidebar.header("Please Select a Project Above to View")
