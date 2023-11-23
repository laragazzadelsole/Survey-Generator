import streamlit as st

TITLE = "ACADEMIC PRIOR BELIEFS ELICITATION SURVEY GENERATOR"

DESCRIPTION = ''' This document is intended for researchers use only. \\
It allows to create a personalized survey to elicit prior beliefs for impact evaluation. \\
    Please carefully fill in all the empty fields. Be aware that once you click submit it's not possible to make any further changes.'''

def title_and_introduction():
    placeholder = st.empty()
    with placeholder.container():
        with st.expander("Title and Introduction", expanded=True):
            survey_title = st.text_input('Write the title of your Survey here:', key = 'survey_title')

            survey_description = st.text_input('Write the description of the survey, the scope of your research and any information that you think might be usefull for the users that will fill in the survey:', key = 'survey_description')
            survey_title, survey_description = (st.session_state['survey_title'], st.session_state['survey_description'])
    
    return survey_title, survey_description