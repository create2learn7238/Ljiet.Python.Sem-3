import streamlit as st
import matplotlib.pyplot as pit
import numpy as np
st.set_page_config(page_title="Chart",page_icon="📊",layout='centered')
st.title("Matplotlib + streamlit demo")
x=np.arange(1,11)
y=np.random.randint(50,100,size=10)
#Line Chart
st.subheader("Line Chart")
pit.figure(figsize=(6,4))
pit.plot(x,y,marker="o")#
pit.xlabel("Student Index")
pit.ylabel("Marks of 10 student")
st.pyplot(pit)
pit.clf() # Clear 
# Bar chart
pit.figure(figsize=(6,4))
pit.bar(x,y,color='red')
pit.grid()
pit.xlabel("Index")
pit.ylabel("Marks")
st.pyplot(pit)
pit.clf()
# Histogram
st.subheader("Histogram")
pit.figure(figsize=(6,4))
pit.hist(y)
pit.xlabel("Student")
pit.ylabel("Marks")
pit.title("Marks Histogram")
st.pyplot(pit)
# ScaterPlot
st.subheader("Scatter Plot")
pit.figure(figsize=(5,3))
pit.scatter(x,y,marker="o")
pit.xlabel("Student")
pit.ylabel("Marks")
pit.title("Marks Scatter")
st.pyplot(pit)
