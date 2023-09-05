import streamlit as st
from github import Github
from components import *

introduction()


title = st.text_input('Write the title of your Survey here:', key = 'title')

description = st.text_input('Write the description of the survey, the scope of your research and any information that you think might be usefull for the users that will fill in the survey:', key = 'description')

submit = st.button('Submit!', on_click= submit, args=(title, description))




