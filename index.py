import streamlit as st
import pandas as pd
import datetime


st.set_page_config(page_title='JeyanJ-CS/2018/020_Research')


st.header('Sri Lankan University Students Academic Performance Prediction with Machine Learning')
st.image('img2.jpg', caption='Sunrise by the mountains')

st.subheader('Enter Your Details')



title = st.text_input('Full Name')
st.caption('Enter Your Full Name')


# Radio Button
st.radio('Gender:',('Male','Female'))
st.caption('Select Your Gender')


#Date and Time 
d = st.date_input("Date Of Birth", value=None)
st.caption('Select Your Date Of Birth')


#Selection Button for research
option1=['University of Colombo','Eastern University','University of Jaffna','University of Kelaniya','University of Moratuwa','University of Peradeniya','Rajarata University','University of Ruhuna','Sabaragamuwa University','South Eastern University','University of Sri Jayewardenepura','Uva Wellassa University','Wayamba University','University of Vavuniya']
year=st.selectbox('University Name:',option1)
st.caption('Select Your University')

#Selection Button for research
option1=['year1','year2','year3','year4']
year=st.selectbox('Academic Year:',option1)
st.caption('Select Your Current Academic Year')

#Number Input
g=st.number_input('Cumulative Grade Point Average (GPA)')
st.caption('Enter Your Current Cumulative Grade Point Average (GPA) ')



# Radio Button
st.radio('Lecture Attendance Regularity:',('Very regular','Somewhat regular','Irregular'))
st.caption('Select Your Answer')


# Radio Button
st.radio('stress level during the semester:',('Low','Moderate','High'))
st.caption('Select Your Answer')



# Radio Button
st.radio('How do you rate your level of engagement in class discussions and activities:',('Very engaged','Moderately engaged','Slightly engaged','Not engaged'))
st.caption('Select Your Answer')



# Radio Button
st.radio('How often do you use the university library or study spaces?:',('Daily',' Several times a week','Once a week','Rarely','Never'))
st.caption('Select Your Answer')


# Radio Button
st.radio('Do you feel supported by your university in terms of academic resources and facilities?:',('Strongly agree','Agree','Neutral','Disagree','Strongly disagree'))
st.caption('Select Your Answer')


# Radio Button
st.radio('How satisfied are you with the availability of academic resources such as textbooks and materials?:',('Very satisfied','Satisfied','Neutral','Dissatisfied','Very dissatisfied'))
st.caption('Select Your Answer')


# Radio Button
st.radio('Do you use any academic support services provided by the university?:',('Yes','No','Maybe'))
st.caption('Select Your Answer')




#slider type columns form my research

col1,col2,col3=st.columns(3)

with col1:
    x=st.slider('Daily Study Hours:',0,10)
    st.caption('Please Select Your Daily Study Hours')

with col2:
    y=st.slider('Social Media Spending Time',0,10)
    st.caption('Please Select Your Social Media Spending Time')


with col3:
    z=st.slider('Sleeping Hours on day',0,10)
    st.caption('Please Select Your Sleeping Hours on day')



# Radio Button
st.radio('Participation in Extracurricular Activities:',('Yes','No'))
st.caption('Select Your Answer')


# Radio Button
st.radio('Do you have a part-time job?:',('Yes','No'))
st.caption('Select Your Answer')


a=st.slider('Rate your overall physical health on a scale of 1 to 5',0,5)
st.caption('Select Your Answer')

submit=st.button('Predicted')










