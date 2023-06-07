import streamlit as st
st.set_page_config(
        page_icon=":octopus:",
        page_title="SP Portfolio Site",
        layout="centered",
        initial_sidebar_state="collapsed"
)
# Main page configuration.
def homePage():
    

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
        <a href="https://github.com/SeanP94">
            <img src="https://img.shields.io/badge/Github-blue?style=flat&logo=github" alt="Linkedin">
        </a>
    </p>
    ''', unsafe_allow_html=True)

    # Set as download button later.

    st.divider()
    st.write('''
    ### Programming Skills
    :desktop_computer:Programming: Python, C++, Kotlin, Familiarity with Javascript and C#  
    :blue_book: Python Libraries: Scikit-Learn, Pandas, Numpy, and Matplotlib  
    :minidisc:Databases: PostgreSQL, Microsoft SQL Server, MySQL and Firestore
    
    ### Experience  
    :mortar_board: Obtained my B.S. in Computer Science from California State University San Marcos    
    :bar_chart: 1.5 Years experience in data analytics.  
    :male-teacher: 1 years experience running a team and store operations.  
    :open_file_folder: 2 years experience on an engineering team.  
    :telephone_receiver: 3 years of customer service experience. 
    ''')

    st.divider()
    # Summary code
    summaryContainer = st.container()
    summaryContainer.header("Introduction")
    summaryContainer.write("""
    &ensp;Hello my name is Sean, and thank you for taking the time to check out my Portfolio Website! I wanted to create a place to help me showcase projects and discuss some achievements to prospective hiring managers.  

    &ensp;To summarize myself I love data and researching problems that need to be solved. It's what my passion and driving force was for finishing my degree in Computer Science. I'd love to find a position that would allow me to expand and grow my skill set. I'm interested in engineering data pipelines, data cleansing, analyzing information, researching business problems, helping management find problems through data, and most importantly LEARNING MORE SKILLS!


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


homePage()

######## SideBar ########
st.sidebar.button("Big Button :o")