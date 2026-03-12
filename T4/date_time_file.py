import streamlit as st
from datetime import date ,time
st.set_page_config(page_title="File",page_icon="📂",layout='wide')
st.title("Date , Time And File Uploader Demo")
exam_date=st.date_input("Select Exam date :",value=date.today())
start_time=st.time_input("Select Start Time :",value=time(9,0))

upload_file=st.file_uploader("Upload CSV File ",type=['csv'])
st.write(f"Selected Exam Date {exam_date}")
st.write(f'Selected Starting Time {start_time}')

if upload_file is not None:
    st.success("File Uploaded Succesfully")
    st.info("Trial Info")
    st.warning("Trial warning")
    st.write("File Name : ",upload_file.name)
    st.write("File Type : ",upload_file.type)
