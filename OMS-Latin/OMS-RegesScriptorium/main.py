import streamlit as st

# Class definition (removed unnecessary inheritance)
class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg")

# Simulating page selection (e.g., a navigation bar selection)
selected_page = "The Servius Sentinel"  # Simulating that the first page is selected
nav_pages = ["The Servius Sentinel", "Another Page"]  # Example nav pages

if selected_page == nav_pages[0]:
    st.title("The Servius Sentinel")
    st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

    # Adding some spacing (optional)
    for i in range(10):
        st.write("")

    # Perform the operation
    operation = "retrieveImage"  # You can change this to test different operations
    data = RetrieveData(operation)
    data.perform_operation()
