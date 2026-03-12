import streamlit as st
import matplotlib.pyplot as plt
from datetime import date
import pandas as pd
st.set_page_config(page_title="Task",page_icon="🎒",layout='wide')
st.title("📄Student Marks & Feedback Form")
st.header("1.Student Information")
col1,col2=st.columns(2)
with col1:
    enroll=st.text_input("Enrollment Number")
    name=st.text_input("Student Name")
Exam_date=st.date_input("Input date",min_value=date(2025, 1, 9),max_value=date(2026, 12, 31))
with col2:
    sem=st.selectbox("Semester",[1,2,3,4,5,6,7,8])
    div=st.text_input("Division")
st.header("2.Mark Entry")
python=st.number_input("Python-1 Marks (out of 100)",0,100,0)
fsd=st.number_input("Fsd-1 Marks (out of 100)",0,100,0)
ps=st.number_input("PS-1 Marks (out of 100)",0,100,0)
de=st.number_input("DE-1 Marks (out of 100)",0,100,0)
st.header("3.Feedback")
feed=st.slider("How well did u understand the subject?:",min_value=1,max_value=10,value=7)
cls=st.radio("Class Participate",["Low","Mid","High"])
comments=st.text_area("Any comments")
if st.button("Submit"):
    st.success("Successfuly Submited")
    dat=pd.DataFrame([{
        "Enroll":enroll,
        "Name":name,
        "Exam":Exam_date,
        "Sem":sem,
        "div":div,
        "Python":python,
        "fsd":fsd,
        "DE":de,
        "PS":ps,
        "Feed":feed,
        "Class":cls,
        "Comments":comments    
    }])
    st.dataframe(dat)
    csv=dat.to_csv(index=True).encode('utf-8')
    a=st.download_button(label="download Custom File",data=csv,file_name='StudentData.csv',mime='text/csv')
    if a:
        st.info("File Has been Downloaded")
