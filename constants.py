import streamlit as st

TITLE = "ACADEMIC PRIOR BELIEFS ELICITATION SURVEY GENERATOR"

DESCRIPTION = ''' This document is intended for researchers use only. \\
It allows to create a personalized survey to elicit prior beliefs for impact evaluation. \\
    Please carefully fill in the empty fields of the questions you need. \\
          The survey includes up to 10 questions, but feel free to use a fewer number if it better suits your needs. \\
            Just scroll down to the Data Saving section and click submit when you are done. \\
          Be aware that once you click submit it's not possible to make any further changes, as it directly creates a json file with your answers on a Github branch. \\
          If you want to modify things please refresh the page, fill in the survey again and choose a different name for the Github branch.'''

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
    }