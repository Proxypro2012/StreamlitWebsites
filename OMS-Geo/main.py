import streamlit as st
import time

st.title("Mahatma Gandhi Quiz")

progress_text = "Operation in progress. Please wait."
progress_bar = st.progress(0, text=progress_text)


level = 0
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




    
if st.button("Level 1"):
        level = 1
        for level in levels:
            progress_bar.progress(level, text=progress_text)
if st.button("Level 2"):
        level = 2
        for level in levels:
            progress_bar.progress(level, text=progress_text)
