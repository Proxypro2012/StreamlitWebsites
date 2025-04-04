import streamlit as st
import time

r1col1, r1col2, r1col3 = st.columns([1.25, 4, 0.25])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
r4col1, r4col2, r4col3 = st.columns([3, 4, 0.25])
r5col1, r5col2, r5col3 = st.columns([1, 2, 1])
r6col1, r6col2, r6col3 = st.columns([1, 2, 1])


with r1col2:
        st.title("Mahatma Gandhi Quiz")

progress_text = "Operation in progress. Please wait."

with r2col2:
        progress_bar = st.progress(0, text=progress_text)

# Create the list of levels
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def retrieve_question(id)
        if id == int(1)
                

def update_progress_bar(currentLevel, delay):
        level = currentLevel
        for i in range(1, level + 1):
                progress_bar.progress(i * 10, text=(f'Question {str(level)}/10'))
                time.sleep(int(delay))  # Simulating a delay for each level


level = 7
update_progress_bar(currentLevel=level, delay=0.05)

with r4col1:
    st.header(f"Question {level}")
        
with r5col2:
    st.divider()

with r6col2:
    st.title("")
    


