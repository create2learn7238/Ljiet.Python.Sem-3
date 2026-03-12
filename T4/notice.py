import streamlit as st
from datetime import date
st.set_page_config(page_title="Notice",page_icon="📃",layout='wide')
st.title("Notice Board")
st.sidebar.header("Filter Notices")
select=st.sidebar.selectbox("Notice Category",['All','Exams','workshop','Intership'])
show_past=st.sidebar.checkbox("Show Past Notice :",value=True)

notices=[
    {"title":"T4 Exam ",'category':'Exams','Date : ':date(2026,1,1)},
    {"title":"Py Workshop ",'category':'workshop','Date : ':date(2026,1,5)},
    {"title":"Internship Orientation ",'category':'Intership','Date : ':date(2026,1,3)},
    {"title":"T5 SEE Exam ",'category':'Exams','Date : ':date(2026,1,2)}
]

st.header("Notices")
col1,col2=st.columns([1,2])
with col1:
    st.subheader("Filter Applied")
    st.write(f'Catergory : {select}')
    st.write(f'Including Past Notices : {show_past}')
    
with col2:
    st.subheader("Info")
    st.text('Below Show notices')
    
for notice in notices:
    if select!='All' and notice['category']!=select :
        continue
    with st.expander(f'{notice['title']}{notice['category']}'):
        st.write(f'**Date** {notice['Date : ']}')
        st.write("Notice Details")
