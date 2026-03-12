import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
st.set_page_config(page_title="Streamlit graph",page_icon="📈",layout='wide')
st.title("Streamlit inbuilt Graph")
m=np.random.randint(50,100,size=10)
a=np.random.randint(0,100,size=10)

chart_data=pd.DataFrame({
    "Marks":m,"Attendence":a
})

st.subheader("Line chart")
st.line_chart(chart_data)

st.subheader("Area chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
counts,bins=np.histogram(m,bins=3)
st.bar_chart(counts)
