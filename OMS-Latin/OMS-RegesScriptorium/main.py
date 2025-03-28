import streamlit as st



class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width = 100)
            


selected_page = "The Servius Sentinel"  
nav_pages = ["The Servius Sentinel", "Another Page"] 


if selected_page == nav_pages[0]:
    st.title("The Servius Sentinel")
    st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

    
    for i in range(10):
        st.write("")

    
    operation = "retrieveImage"
    data = RetrieveData(operation)
    data.perform_operation()
