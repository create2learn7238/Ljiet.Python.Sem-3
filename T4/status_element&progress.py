import streamlit as st
import time
st.set_page_config(page_title="Element",page_icon="🟢",layout='wide')
st.title("Status element and Progress")
st.success("Success")
st.warning("Warning")
st.error("Error")
st.info("Info")
st.write("---")
st.subheader("progess and Spinner Ex")
if st.button("Start long task"):
    progress=st.progress(0)
    with st.spinner("Processing..."):
        for i in range(100):
            time.sleep(0.025)
            progress.progress(i+1)
        st.success("Task Completed")
