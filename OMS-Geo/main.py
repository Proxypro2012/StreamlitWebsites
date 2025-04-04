import streamlit as st
import time

st.title("Mahatma Gandhi Quiz")

progress_text = "Operation in progress. Please wait."
progress_bar = st.progress(0, text=progress_text)

# Create the list of levels
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Button interaction for selecting levels
if st.button("Level 1"):
    level = 1
    for i in range(1, level + 1):
        progress_bar.progress(i * 10, text=(st.header(f'Question {str(level)}/10'))
        time.sleep(0.5)  # Simulating a delay for each level

if st.button("Level 2"):
    level = 2
    for i in range(1, level + 1):
        progress_bar.progress(i * 10, text=progress_text)
        time.sleep(0.5)  # Simulating a delay for each level
