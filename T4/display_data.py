import streamlit as st
import pandas as pd
from datetime import date ,time
st.set_page_config(page_title="Display",page_icon="💻",layout='wide')
st.title("Display Table Json")
data={
    'student':['A','B','C','D','E'],
    'marks':[98,95,33,68,22],
    'pass':[True,True,False,True,False]
}
df=pd.DataFrame(data)
st.subheader("st.dataframe(Interactive)")
st.dataframe(df)

st.subheader("st.table(static)")
st.table(df)

st.subheader("st.json(structured JSON)")
st.json(data)
