import streamlit as st
st.set_page_config(page_title="Fac Profile",page_icon="👨🏻‍🏫",layout='centered')
st.title("fac profile demo")
st.markdown("This is eg show how to use **sidebar**,**column**, and **ex**")

st.sidebar.header("Profile Setting")

fac_name=st.sidebar.text_input("Fac Name","Tejash Thakkar")
department=st.sidebar.selectbox("Department",['CE','IT','CSE','CEA'])
expirence=st.sidebar.slider("years of expirence",0,40,10)

st.sidebar.markdown("---")
st.sidebar.write("You can put filters,toggle etc in sidebar")

col1,col2=st.columns([1,2])

with col1:
    st.subheader('Basic info')
    st.write(f"**Name :** {fac_name}")
    st.write(f"**department :** {department}")
    st.write(f"**expirence :** {expirence}") 
    
with col2:
    st.header("About")
    st.markdown("Use this area")
    
with st.expander("Show Courses P"):
    st.write("P-1")
    st.write("P-2")
    st.write("P-3")
    
with st.expander("Show Courses H"):
    st.write("*H-1*")
    st.markdown("H-2[blue]")
    st.write("**H-3**")
    
    
