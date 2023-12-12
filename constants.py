import streamlit as st

TITLE = "ACADEMIC PRIOR BELIEFS ELICITATION SURVEY GENERATOR"

DESCRIPTION = ''' This document is intended for researchers use only. \\
It allows to create a personalized survey to elicit prior beliefs for impact evaluation. \\
    Please carefully fill in all the empty fields. Be aware that once you click submit it's not possible to make any further changes.'''

def title_and_introduction():
    st.subheader("Title and Introduction")
    survey_title = st.text_input('Write the title of your Survey here:', key = 'survey_title')

    survey_description = st.text_input('Write the description of the survey, the scope of your research and any information that you think might be usefull for the users that will fill in the survey:', key = 'survey_description')
    survey_title, survey_description = (st.session_state['survey_title'], st.session_state['survey_description'])

    return survey_title, survey_description

def secrets_to_json():
    return {
        "type": st.secrets["type"],
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"],
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": st.secrets["auth_uri"],
        "token_uri": st.secrets["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["client_x509_cert_url"],
        "universe_domain": st.secrets["universe_domain"]
        #"github_token": st.secrets["github_token"],
        #"github_repo": st.secrets["github_repo"]
    }