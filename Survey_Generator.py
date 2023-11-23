import streamlit as st
from github import Github
from components import *

introduction()

initialize_session_state()

# Read the JSON file
config_file = open('config.json')
config = json.load(config_file)

# Beginning of the Survey 

survey_title, survey_description = title_and_introduction()

st.subheader('Question 1')
q1_config = config['question1']
title_question_1, body_question_1, column_1_question_1, column_2_question_1, first_value_question1, min_value_question1, max_value_question1, step_size_question1, last_value_question1, title_barchart_question_1, effect_size_question1 = question(q1_config)

st.subheader('Question 2')
q2_config = config['question2']
title_question_2, body_question_2, column_1_question_2, column_2_question_2, first_value_question2, min_value_question2, max_value_question2, step_size_question2, last_value_question2, title_barchart_question_2, effect_size_question2 = question(q2_config)

st.subheader('Question 3')
q3_config = config['question3']
title_question_3, body_question_3, column_1_question_3, column_2_question_3, first_value_question3, min_value_question3, max_value_question3, step_size_question3, last_value_question3, title_barchart_question_3, effect_size_question3 = question(q3_config)

github_branch_name = st.text_input('Choose how to name the Github branch for your project', key = 'github_branch')

#Submission 

submit = st.button('Submit', on_click= submit)

if st.session_state['submit']:

    #new_app_generation(survey_title, survey_description, title_question_1, subtitle_question_1, column_1_question_1, column_2_question_1, min_value_graph_1, max_value_graph_1, step_size_graph_1, title_x_axis_question_1, title_y_axis_question_1, title_barchart_question_1)
    
    new_app_generation(survey_title, 
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
                        effect_size_question3)
    
    st.success("Thank you for completing the Academic Prior Beliefs Elicitation Survey Generator!")
    st.write('''Now please head to https://streamlit.io/ and access with the following credentials: \\
             Username: 'Username' \\
             Password: 'Password' \\
             Add your app clicking on "New App" and inserting the following information: \\
             Repository: \\
             Branch: \\
             Main file path: \\
             Click "Deploy!". \\
             Now your survey is ready to be shared!
             ''')




