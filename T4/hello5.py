import streamlit as st
st.set_page_config(page_title="Widget",page_icon="🛢",layout='wide')
st.title("Selection Widget")
course=st.selectbox("Select Course",['Python','FSD','PS','DE']) # st.selectbox
prefered_days=st.multiselect("Prefered Days for extra Lec",['Mon','Tues','Wed','Thus','Fri','Sat','Sun']) #st.multiselect
delivery_mode=st.radio("Prefered D Mode",['Offline','Online','Mode']) #st.radio
subscribe=st.checkbox("Subscribe") #st.checkbox

st.write(f"Your course :**{course}**")
st.write(f"Your prefered_days :{','.join(prefered_days) if prefered_days else 'None'}")
st.write(f"delivery mode :**{delivery_mode}**")
st.write(f"Subscription :**{subscribe}**")
