from github import Github
from constants import *
from tokens import *
import streamlit as st
import json
from google.oauth2 import service_account
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from requests_oauthlib import OAuth2Session

def introduction():
    st.title(TITLE)
    st.write(DESCRIPTION)

def initialize_session_state():
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'
        st.session_state['consent'] = False
        st.session_state['submit'] = False
        st.session_state['No answer'] = ''
       
    if 'data' not in st.session_state:
        st.session_state['data'] = {
            'Survey Title': [],
            'Survey Description': [],
            'Title Question 1': [],
            'Subtitle Question 1': [],
            'Column 1 Question 1': [],
            'Column 2 Question 1': [],
            'Min Value Question 1': [],
            'Max Value Question 1': [],
            'Step Size Question 1': [],
            'Title Question 2': [],
            'Subtitle Question 2': [],
            'Column 1 Question 2': [],
            'Column 2 Question 2': [],
            'Min Value Question 2': [],
            'Max Value Question 2': [],
            'Step Size Question 2': [],
            'Title Question 3': [],
            'Subtitle Question 3': [],
            'Column 1 Question 3': [],
            'Column 2 Question 3': [],
            'Min Value Question 3': [],
            'Max Value Question 3': [],
            'Step Size Question 3': [], 
            'Github Branch': [],
            'Google Sheet': []
        }
    
def safe_var(key):
    if key in st.session_state:
        return st.session_state[key]
    

def question(jsonfile):
    st.text_input('Write here the title of your first question:', key = jsonfile['key_title'])

    st.text_input('Write here the body of your question explaining it clearly, adding examples.', key = jsonfile['key_body_question'])

    st.text_input('Write here the name of the first column', key = jsonfile['key_column_1'])

    st.text_input('Write here the name of the second column', key = jsonfile['key_column_2'])

    st.text_input('Insert the first value of the x-axis:', key = jsonfile['key_first_value'])

    st.number_input('Insert the minimum value on the x-axis:', key = jsonfile['key_min_value'])

    st.number_input('''Insert the maximum value on the x-axis. Keep in my mind that the counting starts from 0, so to have 10 rows insert number 11:''', key = jsonfile['key_max_value'])

    st.number_input('Insert the step size on the x-axis:', key = jsonfile['key_step_size'])

    st.text_input('Insert the last value on the x-axis:', key = jsonfile['key_last_value'])

    st.text_input('Write here the title of the bar chart:', key = jsonfile['key_title_barchart'])

    st.text_input('Write here the text of the question on the effect size the user would want to see in order to extend the Program:', key = jsonfile['key_effect_size'])
    
    title_question, body_question, column_1, column_2, first_value, min_value, max_value, step_size, last_value, title_barchart, effect_size= (

        st.session_state[jsonfile['key_title']],
        st.session_state[jsonfile['key_body_question']],
        st.session_state[jsonfile['key_column_1']],
        st.session_state[jsonfile['key_column_2']],
        st.session_state[jsonfile['key_first_value']],
        st.session_state[jsonfile['key_min_value']],
        st.session_state[jsonfile['key_max_value']],
        st.session_state[jsonfile['key_step_size']],
        st.session_state[jsonfile['key_last_value']],
        st.session_state[jsonfile['key_title_barchart']],
        st.session_state[jsonfile['key_effect_size']]
    )
    
    return title_question, body_question, column_1, column_2, first_value, min_value, max_value, step_size, last_value, title_barchart, effect_size

def github_google_sheet_names():

    github_branch_name = st.text_input('Choose how to name the Github branch for your project', key = 'github_branch')
    google_sheet_name = st.text_input('Choose how to name the Google sheet where your data will be saved', key = 'google_sheet_name')

    return github_branch_name, google_sheet_name

def submit(): #survey_title, survey_description, title_question_1, subtitle_question_1, column_1_question_1, column_2_question_1, min_value_graph_1, max_value_graph_1, step_size_graph_1):
    st.session_state['submit'] = True

def new_app_generation(survey_title, 
                       survey_description, 
                       title_question_1,
                        body_question_1, 
                        column_1_question_1,
                        column_2_question_1,
                        first_value_question1,
                        min_value_question1,
                        max_value_question1,
                        step_size_question1,
                        last_value_question1,
                        title_barchart_question_1,
                        effect_size_question1,
                        title_question_2,
                        body_question_2,
                        column_1_question_2,
                        column_2_question_2,
                        first_value_question2,
                        min_value_question2,
                        max_value_question2,
                        step_size_question2,    
                        last_value_question2,         
                        title_barchart_question_2,
                        effect_size_question2,
                        title_question_3,
                        body_question_3,
                        column_1_question_3,
                        column_2_question_3,
                        first_value_question3,
                        min_value_question3,
                        max_value_question3,
                        step_size_question3,
                        last_value_question3, 
                        title_barchart_question_3,
                        effect_size_question3,
                        title_question_4,
                        body_question_4, 
                        column_1_question_4,
                        column_2_question_4,
                        first_value_question4,
                        min_value_question4,
                        max_value_question4,
                        step_size_question4,
                        last_value_question4,
                        title_barchart_question_4,
                        effect_size_question4,
                        
                        title_question_5,
                        body_question_5, 
                        column_1_question_5,
                        column_2_question_5,
                        first_value_question5,
                        min_value_question5,
                        max_value_question5,
                        step_size_question5,
                        last_value_question5,
                        title_barchart_question_5,
                        effect_size_question5,
                         
                        title_question_6,
                        body_question_6, 
                        column_1_question_6,
                        column_2_question_6,
                        first_value_question6,
                        min_value_question6,
                        max_value_question6,
                        step_size_question6,
                        last_value_question6,
                        title_barchart_question_6,
                        effect_size_question6,
                        
                        title_question_7,
                        body_question_7, 
                        column_1_question_7,
                        column_2_question_7,
                        first_value_question7,
                        min_value_question7,
                        max_value_question7,
                        step_size_question7,
                        last_value_question7,
                        title_barchart_question_7,
                        effect_size_question7,
                                             
                        title_question_8,
                        body_question_8, 
                        column_1_question_8,
                        column_2_question_8,
                        first_value_question8,
                        min_value_question8,
                        max_value_question8,
                        step_size_question8,
                        last_value_question8,
                        title_barchart_question_8,
                        effect_size_question8,
                        
                        title_question_9,
                        body_question_9, 
                        column_1_question_9,
                        column_2_question_9,
                        first_value_question9,
                        min_value_question9,
                        max_value_question9,
                        step_size_question9,
                        last_value_question9,
                        title_barchart_question_9,
                        effect_size_question9,
                        
                        title_question_10,
                        body_question_10, 
                        column_1_question_10,
                        column_2_question_10,
                        first_value_question10,
                        min_value_question10,
                        max_value_question10,
                        step_size_question10,
                        last_value_question10,
                        title_barchart_question_10,
                        effect_size_question10,

                        github_branch_name
                        ):
    

    branch_name = github_branch_name
    base_branch = "main"  # Replace with the branch you want to base the new branch on

    # Authenticate with GitHub using your personal access token
    g = Github(github_token)

    # Get the repository
    repo = g.get_repo(repository_name)

    # Create a new branch
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=repo.get_branch(base_branch).commit.sha)

    # Get the branch where you want to commit the new file
    branch = repo.get_branch(branch_name)

    # Create a new json file in the branch
    contents = {

        "header": {
            "survey_title": survey_title,
            "survey_description": survey_description
        },
        "question1": {
            "title_question": title_question_1,
            "body_question": body_question_1,
            "column_1": column_1_question_1,
            "column_2": column_2_question_1,
            "first_value": first_value_question1,
            "min_value": min_value_question1,
            "max_value": max_value_question1,
            "step_size": step_size_question1,
            "last_value": last_value_question1,
            "key": "data_editor1",
            "title_barchart": title_barchart_question_1, 
            "num_input_question": "num_input_question1",
            "effect_size": effect_size_question1
        },
        "question2": {
            "title_question": title_question_2,
            "body_question": body_question_2,
            "column_1": column_1_question_2,
            "column_2": column_2_question_2,
            "first_value": first_value_question2,
            "min_value": min_value_question2,
            "max_value": max_value_question2,
            "step_size": step_size_question2,
            "last_value": last_value_question2,
            "key": "data_editor2",
            "title_barchart": title_barchart_question_2, 
            "num_input_question": "num_input_question2",
            "effect_size": effect_size_question2
        },
        "question3": {
            "title_question": title_question_3,
            "body_question": body_question_3,
            "column_1": column_1_question_3,
            "column_2": column_2_question_3,
            "first_value": first_value_question3,
            "min_value": min_value_question3,
            "max_value": max_value_question3,
            "step_size": step_size_question3,
            "last_value": last_value_question3,
            "key": "data_editor3",
            "title_barchart": title_barchart_question_3, 
            "num_input_question": "num_input_question3",
            "effect_size": effect_size_question3
        },
        "question4": {
            "title_question": title_question_4,
            "body_question": body_question_4,
            "column_1": column_1_question_4,
            "column_2": column_2_question_4,
            "first_value": first_value_question4,
            "min_value": min_value_question4,
            "max_value": max_value_question4,
            "step_size": step_size_question4,
            "last_value": last_value_question4,
            "key": "data_editor4",
            "title_barchart": title_barchart_question_4, 
            "num_input_question": "num_input_question4",
            "effect_size": effect_size_question4
        },
        "question5": {
            "title_question": title_question_5,
            "body_question": body_question_5,
            "column_1": column_1_question_5,
            "column_2": column_2_question_5,
            "first_value": first_value_question5,
            "min_value": min_value_question5,
            "max_value": max_value_question5,
            "step_size": step_size_question5,
            "last_value": last_value_question5,
            "key": "data_editor5",
            "title_barchart": title_barchart_question_5, 
            "num_input_question": "num_input_question5",
            "effect_size": effect_size_question5
        },
        "question6": {
            "title_question": title_question_6,
            "body_question": body_question_6,
            "column_1": column_1_question_6,
            "column_2": column_2_question_6,
            "first_value": first_value_question6,
            "min_value": min_value_question6,
            "max_value": max_value_question6,
            "step_size": step_size_question6,
            "last_value": last_value_question6,
            "key": "data_editor6",
            "title_barchart": title_barchart_question_6, 
            "num_input_question": "num_input_question6",
            "effect_size": effect_size_question6
        },
        "question7": {
            "title_question": title_question_7,
            "body_question": body_question_7,
            "column_1": column_1_question_7,
            "column_2": column_2_question_7,
            "first_value": first_value_question7,
            "min_value": min_value_question7,
            "max_value": max_value_question7,
            "step_size": step_size_question7,
            "last_value": last_value_question7,
            "key": "data_editor7",
            "title_barchart": title_barchart_question_7, 
            "num_input_question": "num_input_question7",
            "effect_size": effect_size_question7
        },
        "question8": {
            "title_question": title_question_8,
            "body_question": body_question_8,
            "column_1": column_1_question_8,
            "column_2": column_2_question_8,
            "first_value": first_value_question8,
            "min_value": min_value_question8,
            "max_value": max_value_question8,
            "step_size": step_size_question8,
            "last_value": last_value_question8,
            "key": "data_editor8",
            "title_barchart": title_barchart_question_8, 
            "num_input_question": "num_input_question8",
            "effect_size": effect_size_question8
        },
        "question9": {
            "title_question": title_question_9,
            "body_question": body_question_9,
            "column_1": column_1_question_9,
            "column_2": column_2_question_9,
            "first_value": first_value_question9,
            "min_value": min_value_question9,
            "max_value": max_value_question9,
            "step_size": step_size_question9,
            "last_value": last_value_question9,
            "key": "data_editor9",
            "title_barchart": title_barchart_question_9, 
            "num_input_question": "num_input_question9",
            "effect_size": effect_size_question9
        },
        "question10": {
            "title_question": title_question_10,
            "body_question": body_question_10,
            "column_1": column_1_question_10,
            "column_2": column_2_question_10,
            "first_value": first_value_question10,
            "min_value": min_value_question10,
            "max_value": max_value_question10,
            "step_size": step_size_question10,
            "last_value": last_value_question10,
            "key": "data_editor10",
            "title_barchart": title_barchart_question_10, 
            "num_input_question": "num_input_question10",
            "effect_size": effect_size_question10
        }
    }

    json_string = json.dumps(contents)
    
    repo.create_file(
        path= 'config.json',
        message= 'configuration file',
        content=json_string,
        branch=branch_name
    )

def google_sheet_creation(sheet_name): 
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    #creds = ServiceAccountCredentials.from_json_keyfile_name('prior-beliefs-elicitation-keys.json', scope)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets_to_json())
    client = gspread.authorize(creds)
    sheet = client.create(sheet_name)

    # Load the Google Sheet
    #sheet = client.open("Test").sheet1

    #sheet_update = sheet.update([new_bins_df.columns.values.tolist()])
    #sheet = sheet.append_rows([df.values.tolist()[1]])
    #st.success('Data has been saved successfully.')
    
    #Navigate to the folder in Google Drive. Copy the Folder ID found in the URL. This is everything that comes after “folder/” in the URL.
    #backup_sheet = client.create(f'Backup_{datetime.now()}_{data[USER_FULL_NAME]}', folder_id='1Pjz6JAf9MaVe_eSaAFpDhLFr4GMPj2jX').sheet1
    #backup_sheet = backup_sheet.append_rows(concatenated_df.iloc[:2].values.tolist())
    #backup_sheet.share('sara.gironi97@gmail.com', perm_type = 'user', role = 'writer')

