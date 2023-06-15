import streamlit as st
from st_pages import add_page_title, Page, show_pages_from_config
import tools as myTools
from tools import assets

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Set the dataset as both the training and test data.


sns.set_style('darkgrid')
myTools.setStPageConfig("Kaggle:Titanic", pageIcon=":ship:")

def stCorrMatrix(df: pd.DataFrame):
    '''Draws the correlation matrix for a dataframe in streamlit.'''
    fig = plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), cmap="YlGnBu")
    st.pyplot(fig) # Draws the figure onto the streamlit site.

titanic_data = pd.read_csv(assets.titanicTrain)


st.header("Titanic As a Beginner Kaggle Exercise")
st.write("""
To begin this exercise, we need to import some dependencies and begin some exploratory data analysis.

Disclaimer: This dataset can be found on Kaggle at 
https://www.kaggle.com/competitions/titanic


""")
st.code("""Python
import pandas as pd # Used to store our Dataframe.
import seaborn as sns # Plotting (Used in notebook, Streamlit has it's own graphing)
import matplotlib.pyplot as plt # (Same as before.)
import numpy as np # (Used for adjusting columns later.)
# Set the dataset as both the training and test data.
titanic_data = pd.read_csv("titanic/train.csv")
""")
# Visualize Dataset.
st.dataframe(titanic_data)
st.divider()
st.write("""
Now that we have the data imported, we want to start exploring it with the correlation matrix heatmap below.
""")
st.divider() 
stCorrMatrix(titanic_data)
st.write("""
We see that nothing is too HEAVILY correlated, but we do see that a couple things are around .4 and -.4
""")


st.sidebar.title("Kaggle Data Project")
st.sidebar.divider()
st.sidebar.markdown("""
The infamous Titanic ML project!  

As I've been learning Machine Learning through Datacamp, I wanted to start utilizing some of the skills I've developed on a simple kaggle project.
So I did a walkthrough for the Titanic project. Here I will elaborate on the choices that were made and the outcomes we found. I plan on adding more, better projects
in the near future but for now, here you go!


""")