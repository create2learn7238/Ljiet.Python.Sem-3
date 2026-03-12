import streamlit as st
import pandas as pd
from datetime import date ,time
st.set_page_config(page_title="Download",page_icon="👇🏻",layout='wide')
st.title("Button and Download")
if st.button("Click to generate sample data"):
    df=pd.DataFrame({
        'Enroll :':[1,2,3,4,5],
        'Marks :':[90,99,85,86,87]
    })
    st.write("Generate Data")
    st.dataframe(df)
    csv=df.to_csv(index=False).encode('utf-8')
    st.download_button(label="download Custom File",data=csv,file_name='custom.csv',mime='text/csv')
