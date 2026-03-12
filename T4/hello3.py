import streamlit as st
st.set_page_config(page_title="Input",page_icon="😎",layout='wide')
st.title("Text Input Demo")
name=st.text_input("Enter Your Name")
comments=st.text_area("Any comments")
st.write("Live Output")
if name:
    st.write(f"hello **{name}** 😁")
if comments:
    st.write("Your comments")
    st.write(comments)
