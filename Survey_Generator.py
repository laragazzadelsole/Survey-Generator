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

st.subheader('Question 4')
q4_config = config['question4']
title_question_4, body_question_4, column_1_question_4, column_2_question_4, first_value_question4, min_value_question4, max_value_question4, step_size_question4, last_value_question4, title_barchart_question_4, effect_size_question4 = question(q4_config)

st.subheader('Question 5')
q5_config = config['question5']
title_question_5, body_question_5, column_1_question_5, column_2_question_5, first_value_question5, min_value_question5, max_value_question5, step_size_question5, last_value_question5, title_barchart_question_5, effect_size_question5 = question(q5_config)

st.subheader('Question 6')
q6_config = config['question6']
title_question_6, body_question_6, column_1_question_6, column_2_question_6, first_value_question6, min_value_question6, max_value_question6, step_size_question6, last_value_question6, title_barchart_question_6, effect_size_question6 = question(q6_config)

st.subheader('Question 7')
q7_config = config['question7']
title_question_7, body_question_7, column_1_question_7, column_2_question_7, first_value_question7, min_value_question7, max_value_question7, step_size_question7, last_value_question7, title_barchart_question_7, effect_size_question7 = question(q7_config)

st.subheader('Question 8')
q8_config = config['question8']
title_question_8, body_question_8, column_1_question_8, column_2_question_8, first_value_question8, min_value_question8, max_value_question8, step_size_question8, last_value_question8, title_barchart_question_8, effect_size_question8 = question(q8_config)

st.subheader('Question 9')
q9_config = config['question9']
title_question_9, body_question_9, column_1_question_9, column_2_question_9, first_value_question9, min_value_question9, max_value_question9, step_size_question9, last_value_question9, title_barchart_question_9, effect_size_question9 = question(q9_config)

st.subheader('Question 10')
q10_config = config['question10']
title_question_10, body_question_10, column_1_question_10, column_2_question_10, first_value_question10, min_value_question10, max_value_question10, step_size_question10, last_value_question10, title_barchart_question_10, effect_size_question10 = question(q10_config)

st.subheader('Data Saving')
github_branch_name, google_sheet_name = github_google_sheet_names()

#Submission 

submit = st.button('Submit', on_click= submit)

if st.session_state['submit']:

    google_sheet_creation(google_sheet_name)

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
                        github_branch_name)
    
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




