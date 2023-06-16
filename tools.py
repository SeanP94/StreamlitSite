import streamlit as st
from st_pages import show_pages_from_config
from pathlib import Path
import json
import mysql.connector
currDir = Path(__file__).parent 


class assets:
    """
    Assets are to get different file locations from the other classes.
    """
    homePage = currDir / 'pages' / 'home.py'
    titanicPage = currDir / 'pages' / 'titanic.py'
    pfp = currDir / 'assets' / 'pfp.png'
    resume = currDir / 'assets' / 'SeanPerryResumeDA.pdf'
    cssFile = currDir / 'styles' / 'main.css'
    titanicTrain = currDir / 'assets' / 'train.csv'


def setStPageConfig(pageTitle, pageIcon=":frog:"):
    """
    Sets the page configuration for each page in uniform, 
    also reads in the css data since it's apart of configuring the page.
    """
    st.set_page_config(
            page_icon=pageIcon,
            page_title=pageTitle,
            layout="centered",
            #initial_sidebar_state="collapsed"
    )
    with open(assets.cssFile, 'r') as cssData:
        st.markdown(f'<style>{cssData.read()}</style>', unsafe_allow_html=True)

def pageData():
    show_pages_from_config()

class SqlInteractions:
    
    def __init__(self):
        """
        Launches the sql object
        Initializes core functionality and creates a self.__cur object.
        """
        # with open(".secrets.json", 'r') as f:
        #     data = json.load(f)
        #     connection = mysql.connector.connect(
        #         host=data['host'],
        #         database=data["database"],
        #         user=data['user'],
        #         passwd=data['password']
        #     )
        #     del data # We want to not keep .secrets in memory :) 
        # self.__cur = connection.cursor()

    def nonCommitWrapper(func):
        """
        Singular Input, resets the 
        """
        def wrapper(self, **x):
            with open(".secrets.json", 'r') as f:
                data = json.load(f)
                connection = mysql.connector.connect(
                    host=data['host'],
                    database=data["database"],
                    user=data['user'],
                    passwd=data['password']
                )
                del data # We want to not keep .secrets in memory :) 
            self.__cur = connection.cursor()
            print("Opening Connection.")
            func(self)
            print("Closing Connection.")
            self.__cur.close()
        return wrapper

    @nonCommitWrapper
    def getTableNames(self):
        """
        Used to return the table names for the class to function properly
        """
        pass

    @nonCommitWrapper
    def getTableNames2(self, z):
        """
        Used to return the table names for the class to function properly
        """
        pass
    def getTableCopy(tableName):
        pass