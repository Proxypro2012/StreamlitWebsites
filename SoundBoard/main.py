import streamlit as st



r1col1, r1col2, r1col3 = st.columns([1.25, 4, 0.25])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])


r3col1, r3col2, r3col3 = st.columns([2, 2, 2])

with r1col2:
  st.title("Meme Soundboard")

with r2col2:
  st.divider()

with r3col1:
  st.audio('SoundBoard/myinstants.mp3')
  
