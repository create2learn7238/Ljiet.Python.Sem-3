import streamlit as st
import pandas as pd
from datetime import date ,time
st.set_page_config(page_title="Media",page_icon="🎵",layout='wide')
st.title("Media Display")

st.subheader("Images")
st.image("img.jpeg",use_container_width=True)

st.subheader("Audio")
st.audio("ad.mp3")

st.subheader("Video")
st.video("vd.mp4")
