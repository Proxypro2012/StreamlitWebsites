import streamlit as st
import time

r1col1, r1col2, r1col3 = (1, 2, 1)
r2col1, r2col2, r2col3 = (1, 2, 1)
r3col1, r3col2, r3col3 = (1, 2, 1)
r4col1, r4col2, r4col3 = (1, 2, 1)
r5col1, r5col2, r5col3 = (1, 2, 1)

st.title("Mahatma Gandhi Quiz")

progress_text = "Operation in progress. Please wait."
progress_bar = st.progress(0, text=progress_text)

# Create the list of levels
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


level = 1
for i in range(1, level + 1):
        progress_bar.progress(i * 10, text=(f'Question {str(level)}/10'))
        time.sleep(0.5)  # Simulating a delay for each level


level = 2
for i in range(1, level + 1):
        progress_bar.progress(i * 10, text=(f'Question {str(level)}/10'))
        time.sleep(0.5)  # Simulating a delay for each level

st.divider()

with r1col2:
    st.header("Questions")
    


