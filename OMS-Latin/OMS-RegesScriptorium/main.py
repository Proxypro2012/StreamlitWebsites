import streamlit as st

r1col1, r1col2 = st.columns([1, 0.5])
rgap1col1, rgap1col2 = st.columns([1, 0.5])
r2col1, r2col2 = st.columns([1, 2])
r3col1, r3col2 = st.columns([1, 2])# Create two columns, one smaller (1) and one larger (2)

class RetrieveData:
    def __init__(self, operation):
        self.operation = operation

    def perform_operation(self):
        if self.operation == "retrieveImage": 
            st.image("OMS-Latin/OMS-RegesScriptorium/servius-tullius.jpeg", width=230, caption="***In Pictura Est Servius Tullius***")
        if self.operation == "displayHomeTitle":
            st.title("The Servius Sentinel")
            st.markdown("***Veni, Vidi, Vici - I came, I saw, I conquered (Julius Caesar)***")

# Sidebar navigation
nav_pages = ["Home", "Credits"]
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("", nav_pages)

if selected_page == nav_pages[1]:
    st.title("Credits")
    st.write("Developers and Writers")

    for i in range(10):
        st.write("")

    st.write("Kabir Tiwari - Developer and Writer")
    st.write("Gunner Gordon - Writer and Designer")

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
        #st.write("Servius Tullius est sextus rex")
        st.write("Servius Tullius natus est servus")
        st.write("Tarquinnius Priscus est quintus rex. Uxor eius est Tanaquil. Tanaqil videt ignis cirum Servius caput.")

    for i in range(10):
        st.write("")

    with r3col1:
        st.header("The Rise")
        st.write("Servius Tullius was born a slave. One day, the wife of the fifth roman king Tarquinius Priscus, Tanaquil, saw the young boy with a ring of fire around his head. She interpreted this as a sign from the gods. She told Tarquinius Priscus, and the two of them decided to raise Servius Tullius to be the next king.")

    with r3col2:
        st.header("The Rule")


    
    
    

    
