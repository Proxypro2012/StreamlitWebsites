import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patche
r1col1, r1col2 = st.columns([2, 2])


class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width = 300)
            



nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)




if selected_page == nav_pages[0]:
    st.title("The Servius Sentinel")
    st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

    
    for i in range(10):
        st.write("")

    
    operation = "retrieveImage"
    data = RetrieveData(operation)
    with r1col2:
        data.perform_operation()
    with r2col2:
        st.write("HI")
