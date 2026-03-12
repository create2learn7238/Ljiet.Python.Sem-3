import streamlit as st
st.set_page_config(page_title="Slider",page_icon="😎",layout='wide')
st.title("Number Input and Slidebar")
age=st.number_input("Enter your age:",min_value=0,max_value=100,value=21)
rate=st.slider("Rate this Session:",min_value=1,max_value=10,value=5)
st.write(f"Your age :**{age}**")
st.write(f"You rated this session **{rate}/10**")
