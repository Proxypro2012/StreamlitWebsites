import streamlit as st



r1col1, r1col2, r1col3 = st.columns([0.25, 4, 0.25])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])

with r1col2:
  st.title("Meme Soundboard")

with r2col2:
  st.divider()
  
