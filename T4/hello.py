import streamlit as st
st.set_page_config(page_title="Hello Stream Lit",page_icon="😎",layout='wide')
st.title("Welcome to streamlit HEHEHEH")
st.header("This is Header")
st.subheader("This is subtitle")
st.text("st.subtext() is used for simple fixed width text")
st.write("st.write() is more flixible and can display text , numbers , dataforms ")
st.markdown("**st.markdown()** lets you use to markdown for **rich text**")

code_example="""
def add(a,b):
    return(a+b)
result=add(5,7)
print(result)
"""
st.code(code_example,language='python')
