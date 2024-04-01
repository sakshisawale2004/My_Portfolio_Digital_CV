import streamlit as st 

st.set_page_config(
    page_title="Sakshi Savle Portfolio",
    page_icon="🕶️",  
)
st.title("Projects")
project_1,img_1=st.columns(2)

with project_1:
    st.write("#### G-mail Automation")
    st.write("###### In this project, I have developed a Gmail automation tool that includes features such as text-to-speech functionality, the ability to send emails to multiple recipients simultaneously, and access to pre-designed templates for quick and efficient communication. This tool streamlines the email sending process and enhances productivity in a user-friendly manner. ")

with img_1:
    img1="pages\G_Mail.jpeg"
    st.image(img1,width=250)

st.write("---")
img_2,project_2=st.columns(2)
with img_2:
    img2="pages\Weather_forecast.png"
    st.image(img2,width=300)
with project_2:
    st.write("#### Weather Forecast ")
    st.write("###### In this project-'Weather Forecast' I have developed a simple but interactive app using Python & API to provide the weather update and weekly/monthly statistic of weather.")

st.write("---")
project_3,img_3=st.columns(2)
with project_3:
    st.write("#### Digital CV")
    st.write("###### This project - 'Digital CV' I have developed my portfolio using Streamlit, which offers a dynamic & interactive showcase of my skills and projects. ")
with img_3:
    img3="pages\Portfolio.png"
    st.image(img3,width=300)

st.write("--------")
