import streamlit as st

r1col1, r1col2 = st.columns([1, 0.5])
rgap1col1, rgap1col2 = st.columns([1, 0.5])
r2col1, r2col2 = st.columns([1, 2])  # Create two columns, one smaller (1) and one larger (2)

class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width=300, caption="***In Pictura Est Servius Tullius***")
        if self.operation == "displayHomeTitle":
            st.title("The Servius Sentinel")
            st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

# Sidebar navigation
nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

if selected_page == nav_pages[0]:
    
    
    operation = "displayHomeTitle"
    data = RetrieveData(operation)
    with r1col1:
        data.perform_operation()

    with rgap1col1:
        for i in range(10):
            st.write("")

    operation = "retrieveImage"
    data = RetrieveData(operation)
    
    # Add content in two columns
    with r2col1:
        data.perform_operation()# Left column for the image
        

    with r2col2:
        st.subheader("**The Rise**")
        st.write("Servius Tullius est sextus rex")
    
    
    

    
