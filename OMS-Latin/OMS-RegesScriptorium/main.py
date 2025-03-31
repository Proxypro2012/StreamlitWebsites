import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

r1col1, r1col2 = st.columns([1, 2])  # Create two columns, one smaller (1) and one larger (2)

class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width=300)

# Sidebar navigation
nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

if selected_page == nav_pages[0]:
    st.title("The Servius Sentinel")
    st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

    # Add spacing
    for i in range(10):
        st.write("")

    operation = "retrieveImage"
    data = RetrieveData(operation)
    data.perform_operation()

    # Add content in two columns
    with r1col1:  # Left column for the image
        st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width=300)

    with r1col2:  # Right column for the text
        st.write("***In Pictura Est Servius Tullius***")
