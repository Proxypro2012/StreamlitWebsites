import streamlit as st
import time

st.title("Mahatma Gandhi Quiz")

progress_text = "Operation in progress. Please wait."
progress_bar = st.progress(0, text=progress_text)

levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for level in levels:
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
progress_bar.empty()
  
